"""Hace jugar juegos mezclados a un modelo y guarda todo lo que pasó.

Uso (las claves van por variable de entorno, nunca en el repo):
    export AZURE_FOUNDRY_BASE_URL=...  AZURE_INFERENCE_CREDENTIAL=...
    python games/jump_ahead/harness/play.py --model gpt-5.4 --effort high --games mix-5,plain-5 \
        --out experiments/2026-11-16-mixing-ladder/raw --budget 40

Cada partida deja un archivo JSON con: lo que recibió el modelo, cada código que corrió y su salida,
los tokens gastados, su respuesta, la respuesta exacta y el puntaje. El puntaje es una cuenta: ninguna
IA interviene en calcularlo.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from harness.sandbox import Sandbox  # noqa: E402
from mixed.brief import make_brief  # noqa: E402
from mixed.instances import mixed_games, plain_game, twin_games  # noqa: E402
from mixed.scoring import score_cell  # noqa: E402

# Dólares por millón de tokens (entrada, salida). De una búsqueda web del 16-nov-2026, no de la página
# oficial: sirven para estimar el gasto, no para facturar. No descuentan la entrada repetida (caché),
# así que la estimación tira para arriba.
PRICES = {
    "gpt-6-astra": (10.0, 50.0),
    "gpt-5.4": (2.5, 15.0),
    "gpt-5.4-mini": (0.75, 4.5),
    "claude-opus-4-6": (5.0, 25.0),
}
MAX_RUNS, RUN_SECONDS, MAX_TURNS = 12, 30.0, 40
TWIN_TRUTH = Path(__file__).resolve().parents[1] / "mixed" / "twin_truth.json"
TOOL_DESCRIPTION = "Ejecuta código Python 3 (con numpy) en tu directorio de trabajo y devuelve lo que imprime."
OPENAI_TOOLS = [{"type": "function", "function": {
    "name": "run_python", "description": TOOL_DESCRIPTION,
    "parameters": {"type": "object", "required": ["code"],
                   "properties": {"code": {"type": "string", "description": "El código. Usá print() para ver resultados."}}}}}]
ASK_AGAIN = 'Falta la respuesta final en el formato pedido: un único bloque JSON con "answers".'
_ledger_lock = threading.Lock()


def all_games() -> dict:
    return {g.game_id: g for g in [plain_game()] + mixed_games() + twin_games()}


def truth_of(game) -> list:
    """La respuesta exacta de cada casilla preguntada (número de símbolo)."""
    if hasattr(game, "truth"):
        return game.truth()
    stored = json.loads(TWIN_TRUTH.read_text())[game.game_id]        # contada en C: ver mixed/twin.py
    return [stored["far_state"][c] for c in game.cells]


def parse_answers(text: str | None):
    """Saca el último bloque JSON con "answers" del texto del modelo. None si no hay uno válido."""
    if not text:
        return None
    pos = text.rfind('"answers"')
    while pos >= 0:
        start = text.rfind("{", 0, pos)
        depth = 0
        for end in range(start, len(text)) if start >= 0 else []:
            depth += (text[end] == "{") - (text[end] == "}")
            if depth == 0:
                try:
                    data = json.loads(text[start:end + 1])
                    if isinstance(data.get("answers"), list):
                        return data
                except (json.JSONDecodeError, AttributeError):
                    pass
                break
        pos = text.rfind('"answers"', 0, pos)
    return None


def grade(data, game, symbols: list) -> dict:
    """El puntaje: por casilla y promedio. Una casilla sin respuesta válida cuenta como "no sé" (0)."""
    k = len(symbols)
    truths = truth_of(game)
    by_cell = {}
    for entry in (data or {}).get("answers", []):
        try:
            by_cell[int(entry["cell"])] = (str(entry["symbol"]).strip(), float(entry["confidence"]))
        except (KeyError, TypeError, ValueError):
            continue
    cells = []
    for cell, truth in zip(game.cells, truths):
        symbol, confidence = by_cell.get(cell, (None, 1 / k))
        valid = symbol in symbols and 0.0 <= confidence <= 1.0
        points = score_cell(symbols.index(symbol), confidence, truth, k) if valid else 0.0
        cells.append({"cell": cell, "truth": symbols[truth], "answer": symbol, "confidence": confidence,
                      "valid": valid, "right": valid and symbols.index(symbol) == truth, "score": round(points, 4)})
    return {"score": round(sum(c["score"] for c in cells) / len(cells), 4),
            "right": sum(c["right"] for c in cells), "of": len(cells), "cells": cells}


def run_tool(sandbox: Sandbox, code) -> str:
    if not isinstance(code, str):
        return 'Argumentos inválidos. Mandá {"code": "..."}.'
    if sandbox.runs_left <= 0:
        return "No quedan ejecuciones. Entregá tu respuesta final."
    result = sandbox.run(code)
    return f"{result.output}\n[ejecución {len(sandbox.runs)} de {sandbox.max_runs}; tardó {result.seconds:.1f} s]"


def play_openai(model: str, effort: str | None, text: str, sandbox: Sandbox):
    """Conversación con herramientas por la API compatible con OpenAI (GPT, Grok, DeepSeek, Kimi)."""
    from openai import OpenAI

    client = OpenAI(base_url=os.environ["AZURE_FOUNDRY_BASE_URL"].rstrip("/") + "/",
                    api_key=os.environ["AZURE_INFERENCE_CREDENTIAL"], timeout=3600, max_retries=3)
    messages = [{"role": "user", "content": text}]
    usage = {"calls": 0, "input": 0, "output": 0, "reasoning": 0, "cached": 0}
    final, asked_again = None, False
    for _ in range(MAX_TURNS):
        kwargs = {"model": model, "messages": messages, "tools": OPENAI_TOOLS, "max_completion_tokens": 64000}
        if effort:
            kwargs["reasoning_effort"] = effort
        resp = client.chat.completions.create(**kwargs)
        msg, u = resp.choices[0].message, resp.usage
        usage["calls"] += 1
        usage["input"] += u.prompt_tokens
        usage["output"] += u.completion_tokens
        usage["reasoning"] += getattr(getattr(u, "completion_tokens_details", None), "reasoning_tokens", 0) or 0
        usage["cached"] += getattr(getattr(u, "prompt_tokens_details", None), "cached_tokens", 0) or 0
        entry = {"role": "assistant", "content": msg.content or ""}
        if msg.tool_calls:
            entry["tool_calls"] = [{"id": tc.id, "type": "function",
                                    "function": {"name": tc.function.name, "arguments": tc.function.arguments}}
                                   for tc in msg.tool_calls]
        messages.append(entry)
        if msg.tool_calls:
            for tc in msg.tool_calls:
                try:
                    code = json.loads(tc.function.arguments).get("code")
                except (json.JSONDecodeError, AttributeError):
                    code = None
                messages.append({"role": "tool", "tool_call_id": tc.id, "content": run_tool(sandbox, code)})
            continue
        final = msg.content
        if parse_answers(final) is not None or asked_again:
            break
        asked_again = True
        messages.append({"role": "user", "content": ASK_AGAIN})
    return messages, usage, final


def play_responses(model: str, effort: str | None, text: str, sandbox: Sandbox):
    """Conversación con herramientas por la API Responses (modelos GPT; Astra solo acepta herramientas por acá)."""
    from openai import OpenAI

    client = OpenAI(base_url=os.environ["AZURE_FOUNDRY_BASE_URL"].rstrip("/") + "/",
                    api_key=os.environ["AZURE_INFERENCE_CREDENTIAL"], timeout=3600, max_retries=3)
    tools = [{"type": "function", "name": "run_python", "description": TOOL_DESCRIPTION,
              "parameters": OPENAI_TOOLS[0]["function"]["parameters"]}]
    transcript = [{"role": "user", "content": text}]
    usage = {"calls": 0, "input": 0, "output": 0, "reasoning": 0, "cached": 0}
    pending, previous, final, asked_again = [{"role": "user", "content": text}], None, None, False
    for _ in range(MAX_TURNS):
        kwargs = {"model": model, "input": pending, "tools": tools, "max_output_tokens": 64000}
        if effort:
            kwargs["reasoning"] = {"effort": effort}
        if previous:
            kwargs["previous_response_id"] = previous
        resp = client.responses.create(**kwargs)
        previous, u = resp.id, resp.usage
        usage["calls"] += 1
        usage["input"] += u.input_tokens
        usage["output"] += u.output_tokens
        usage["reasoning"] += getattr(getattr(u, "output_tokens_details", None), "reasoning_tokens", 0) or 0
        usage["cached"] += getattr(getattr(u, "input_tokens_details", None), "cached_tokens", 0) or 0
        calls = [item for item in resp.output if item.type == "function_call"]
        transcript.append({"role": "assistant", "content": resp.output_text or "",
                           "tool_calls": [{"id": c.call_id, "arguments": c.arguments} for c in calls]})
        if calls:
            pending = []
            for call in calls:
                try:
                    code = json.loads(call.arguments).get("code")
                except (json.JSONDecodeError, AttributeError):
                    code = None
                output = run_tool(sandbox, code)
                pending.append({"type": "function_call_output", "call_id": call.call_id, "output": output})
                transcript.append({"role": "tool", "tool_call_id": call.call_id, "content": output})
            continue
        final = resp.output_text
        if parse_answers(final) is not None or asked_again:
            break
        asked_again = True
        pending = [{"role": "user", "content": ASK_AGAIN}]
        transcript.append(pending[0])
    return transcript, usage, final


def cost_of(model: str, usage: dict) -> float:
    price_in, price_out = PRICES.get(model, (10.0, 50.0))
    return usage["input"] / 1e6 * price_in + usage["output"] / 1e6 * price_out


def spent(out_dir: Path) -> float:
    return sum(json.loads(p.read_text()).get("cost_usd", 0.0) for p in out_dir.glob("*.json"))


def play_one(game, model: str, effort: str | None, hint: bool, out_dir: Path, budget: float, tag: str) -> dict:
    with _ledger_lock:
        already = spent(out_dir)
    if already >= budget:
        return {"game": game.game_id, "skipped": f"tope de gasto alcanzado ({already:.2f} de {budget:.2f} USD)"}
    text, files, symbols = make_brief(game, MAX_RUNS, RUN_SECONDS, hint=hint)
    sandbox = Sandbox(files, MAX_RUNS, RUN_SECONDS)
    t0 = time.time()
    error = None
    messages, usage, final = [], {"calls": 0, "input": 0, "output": 0, "reasoning": 0, "cached": 0}, None
    try:
        if model.startswith("claude"):
            from harness import claude_player
            messages, usage, final = claude_player.play(model, effort, text, sandbox, run_tool, parse_answers,
                                                        TOOL_DESCRIPTION, ASK_AGAIN, MAX_TURNS)
        elif model.startswith("gpt-"):
            messages, usage, final = play_responses(model, effort, text, sandbox)
        else:
            messages, usage, final = play_openai(model, effort, text, sandbox)
    except Exception as exc:  # noqa: BLE001  (se guarda y se informa; no se inventa un resultado)
        error = f"{type(exc).__name__}: {exc}"
    data = parse_answers(final)
    record = {
        "game": game.game_id, "model": model, "effort": effort, "hint": hint, "tag": tag,
        "started": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t0)), "wall_seconds": round(time.time() - t0, 1),
        "limits": {"max_runs": MAX_RUNS, "run_seconds": RUN_SECONDS, "max_turns": MAX_TURNS},
        "error": error, "usage": usage, "cost_usd": round(cost_of(model, usage), 4),
        "code_runs": len(sandbox.runs), "code_seconds": round(sandbox.cpu_seconds, 1),
        "code_timeouts": sum(r.timed_out for r in sandbox.runs),
        "answered": data is not None, "method": (data or {}).get("method"),
        "grade": grade(data, game, symbols) if error is None else None,
        "brief": text, "messages": messages,
    }
    name = f"{game.game_id}__{model}__{effort or 'none'}{'__hint' if hint else ''}__{tag}__{int(t0)}.json"
    with _ledger_lock:
        (out_dir / name).write_text(json.dumps(record, ensure_ascii=False, indent=1))
    return record


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--effort", default=None, help="esfuerzo de razonamiento (low/medium/high); vacío = sin ese parámetro")
    ap.add_argument("--games", required=True, help="ids separados por coma, o 'all'")
    ap.add_argument("--out", required=True)
    ap.add_argument("--budget", type=float, required=True, help="tope de gasto estimado de TODA la carpeta, en dólares")
    ap.add_argument("--hint", action="store_true", help="segunda vuelta: con la idea nombrada")
    ap.add_argument("--tag", default="r1")
    ap.add_argument("--parallel", type=int, default=4)
    args = ap.parse_args()
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    games = all_games()
    chosen = list(games) if args.games == "all" else args.games.split(",")
    with ThreadPoolExecutor(max_workers=args.parallel) as pool:
        futures = [pool.submit(play_one, games[g], args.model, args.effort, args.hint, out_dir, args.budget, args.tag)
                   for g in chosen]
        for future in futures:
            r = future.result()
            if "skipped" in r:
                print(f"{r['game']:9s} SALTEADO: {r['skipped']}")
            elif r["error"]:
                print(f"{r['game']:9s} ERROR: {r['error'][:200]}")
            else:
                g = r["grade"]
                print(f"{r['game']:9s} puntaje {g['score']:+.2f}  aciertos {g['right']}/{g['of']}  "
                      f"ejecuciones {r['code_runs']} ({r['code_seconds']:.0f} s)  llamadas {r['usage']['calls']}  "
                      f"tokens {r['usage']['input']}+{r['usage']['output']}  ~{r['cost_usd']:.2f} USD  "
                      f"{r['wall_seconds']:.0f} s")
    print(f"gasto estimado acumulado en {out_dir}: {spent(out_dir):.2f} USD")


if __name__ == "__main__":
    main()
