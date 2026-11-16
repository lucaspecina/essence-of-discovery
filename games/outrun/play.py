"""Hace jugar un juego de `outrun` a un modelo y guarda todo lo que pasó.

Uso (las claves van por variable de entorno, nunca en el repo):
    export AZURE_FOUNDRY_BASE_URL=...  AZURE_INFERENCE_CREDENTIAL=...
    python games/outrun/play.py --model gpt-6-astra --effort high --game collisions \
        --exp experiments/2026-11-16-outrun-first-two-games --budget 25

El modelo investiga el mundo con su computadora y deja un `solution.py`. Después el corrector
(`evaluate.py`) prueba ese archivo contra la realidad. Cada partida deja un JSON en `<exp>/raw/` con el
enunciado, la conversación entera, los tokens, el programa entregado y la corrección caso por caso.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from evaluate import evaluate, print_summary  # noqa: E402
from games import GAMES, check_file, make_brief, world_file  # noqa: E402
from shared.agent_loop import run_agent  # noqa: E402
from shared.sandbox import Sandbox  # noqa: E402

# Dólares por millón de tokens (entrada, salida). De una búsqueda web del 16-nov-2026, no de la página
# oficial: sirven para estimar el gasto, no para facturar. No descuentan la entrada repetida (caché).
PRICES = {"gpt-6-astra": (10.0, 50.0), "gpt-5.4": (2.5, 15.0), "claude-opus-4-6": (5.0, 25.0)}
MAX_RUNS, RUN_SECONDS, MAX_TURNS = 40, 120.0, 90
HINTS = {
    "pingpong": "\nPISTA\nLa pared izquierda no se mueve. La cosa de adentro va y viene entre las dos paredes, y cada vez "
                "que rebota contra la pared derecha, esa pared queda una casilla más a la derecha. Por eso cada vuelta "
                "tarda dos pasos más que la anterior, y la cantidad de vueltas que entran en un tiempo dado sale de una "
                "raíz cuadrada.\n",
    "collisions": "\nPISTA\nLas fichas viajan solas a velocidad constante hasta que dos quedan cerca. Lo que pasa en un "
                  "encuentro dura pocos pasos y depende de la distancia a la que arrancaron. No hace falta recorrer los "
                  "pasos en que nadie está cerca de nadie.\n",
}
MISSING = ("No encuentro `solution.py` en tu directorio de trabajo. Escribilo (con `write_file` o desde `run_python`) "
           "y respondé LISTO.")


def cost_of(model: str, usage: dict) -> float:
    price_in, price_out = PRICES.get(model, (10.0, 50.0))
    return usage["input"] / 1e6 * price_in + usage["output"] / 1e6 * price_out


def spent(raw: Path) -> float:
    return sum(json.loads(p.read_text()).get("cost_usd", 0.0) for p in raw.glob("*.json"))


def play(game_id: str, model: str, effort: str | None, hint: bool, exp: Path, budget: float, tag: str) -> dict:
    raw = exp / "raw"
    raw.mkdir(parents=True, exist_ok=True)
    already = spent(raw)
    if already >= budget:
        return {"skipped": f"tope de gasto alcanzado ({already:.2f} de {budget:.2f} USD)"}
    game = GAMES[game_id]
    eval_set = json.loads((exp / f"cases_{game_id}.json").read_text())
    text = make_brief(game, MAX_RUNS, RUN_SECONDS) + (HINTS[game_id] if hint else "")
    sandbox = Sandbox({"world.py": world_file(game), "check.py": check_file(game)}, MAX_RUNS, RUN_SECONDS, prefix="outrun-")
    writes = []

    def run_python(arguments: dict) -> str:
        code = arguments.get("code")
        if not isinstance(code, str):
            return 'Argumentos inválidos. Mandá {"code": "..."}.'
        if sandbox.runs_left <= 0:
            return "No quedan ejecuciones. Dejá tu solution.py definitivo y respondé LISTO."
        result = sandbox.run(code)
        return f"{result.output}\n[ejecución {len(sandbox.runs)} de {sandbox.max_runs}; tardó {result.seconds:.1f} s]"

    def write_file(arguments: dict) -> str:
        name, content = arguments.get("name"), arguments.get("content")
        if not isinstance(name, str) or not isinstance(content, str) or not re.fullmatch(r"[A-Za-z0-9_.-]{1,60}", name) or name.startswith("."):
            return 'Argumentos inválidos. Mandá {"name": "solution.py", "content": "..."} (un nombre simple, sin carpetas).'
        (sandbox.workdir / name).write_text(content, encoding="utf-8")
        writes.append({"name": name, "bytes": len(content.encode("utf-8"))})
        return f"Escrito {name} ({len(content.encode('utf-8'))} bytes)."

    tools = {
        "run_python": ("Ejecuta código Python 3 (con numpy) en tu directorio de trabajo y devuelve lo que imprime.",
                       {"type": "object", "required": ["code"],
                        "properties": {"code": {"type": "string", "description": "El código. Usá print() para ver resultados."}}},
                       run_python),
        "write_file": ("Escribe un archivo de texto en tu directorio de trabajo (no gasta ejecuciones).",
                       {"type": "object", "required": ["name", "content"],
                        "properties": {"name": {"type": "string", "description": "Nombre del archivo, por ejemplo solution.py"},
                                       "content": {"type": "string", "description": "El contenido completo del archivo."}}},
                       write_file),
    }
    solution_path = sandbox.workdir / "solution.py"
    t0 = time.time()
    error, messages, final = None, [], None
    usage = {"calls": 0, "input": 0, "output": 0, "reasoning": 0, "cached": 0}
    try:
        messages, usage, final = run_agent(model, effort, text, tools, MAX_TURNS,
                                           lambda: None if solution_path.exists() else MISSING)
    except Exception as exc:  # noqa: BLE001  (se guarda y se informa; no se inventa un resultado)
        error = f"{type(exc).__name__}: {exc}"
    source = solution_path.read_text(encoding="utf-8", errors="replace") if solution_path.exists() else None
    summary = evaluate(source, eval_set) if source is not None else None
    record = {
        "game": game_id, "model": model, "effort": effort, "hint": hint, "tag": tag,
        "started": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t0)), "wall_seconds": round(time.time() - t0, 1),
        "limits": {"max_runs": MAX_RUNS, "run_seconds": RUN_SECONDS, "max_turns": MAX_TURNS},
        "error": error, "usage": usage, "cost_usd": round(cost_of(model, usage), 4),
        "code_runs": len(sandbox.runs), "code_seconds": round(sandbox.cpu_seconds, 1),
        "code_timeouts": sum(r.timed_out for r in sandbox.runs), "file_writes": writes,
        "final_text": final, "solution": source, "evaluation": summary, "brief": text, "messages": messages,
    }
    name = f"{game_id}__{model}__{effort or 'none'}{'__hint' if hint else ''}__{tag}__{int(t0)}.json"
    (raw / name).write_text(json.dumps(record, ensure_ascii=False, indent=1), encoding="utf-8")
    return record


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--effort", default=None)
    ap.add_argument("--game", required=True, choices=sorted(GAMES))
    ap.add_argument("--exp", required=True, help="carpeta del experimento (tiene cases_<juego>.json)")
    ap.add_argument("--budget", type=float, required=True, help="tope de gasto estimado de toda la carpeta, en dólares")
    ap.add_argument("--hint", action="store_true", help="con la idea nombrada")
    ap.add_argument("--tag", default="r1")
    args = ap.parse_args()
    record = play(args.game, args.model, args.effort, args.hint, Path(args.exp), args.budget, args.tag)
    if "skipped" in record:
        print("SALTEADO:", record["skipped"])
        return
    if record["error"]:
        print("ERROR:", record["error"][:300])
    if record["evaluation"]:
        print_summary(f"{args.game} / {args.model}", record["evaluation"])
    else:
        print("no entregó solution.py")
    print(f"ejecuciones {record['code_runs']} ({record['code_seconds']:.0f} s)  llamadas {record['usage']['calls']}  "
          f"tokens {record['usage']['input']}+{record['usage']['output']}  ~{record['cost_usd']:.2f} USD  "
          f"{record['wall_seconds']:.0f} s")
    print(f"gasto estimado acumulado: {spent(Path(args.exp) / 'raw'):.2f} USD")


if __name__ == "__main__":
    main()
