"""La conversación con herramientas de un modelo, para cualquier juego.

`run_agent` le manda el enunciado, ejecuta las herramientas que pida y repite hasta que el modelo deja de
pedir herramientas. Ahí llama a `finish_check()`: si devuelve un texto, se lo manda como un mensaje más
(una sola vez) y sigue; si devuelve None, termina.

`tools` es {nombre: (descripción, esquema de parámetros, función(argumentos) -> texto)}.

Las claves van por variable de entorno (AZURE_FOUNDRY_BASE_URL, AZURE_INFERENCE_CREDENTIAL), nunca en el repo.
Los modelos GPT van por la API Responses (gpt-6-astra solo acepta herramientas por ahí); los Claude, por
`claude_loop.py`; el resto, por la API de chat.
"""
from __future__ import annotations

import json
import os

MAX_OUTPUT_TOKENS = 64000


def _client():
    from openai import OpenAI

    return OpenAI(base_url=os.environ["AZURE_FOUNDRY_BASE_URL"].rstrip("/") + "/",
                  api_key=os.environ["AZURE_INFERENCE_CREDENTIAL"], timeout=3600, max_retries=3)


def _call(tools: dict, name: str, raw_arguments) -> str:
    if name not in tools:
        return f"No existe la herramienta {name}."
    try:
        arguments = json.loads(raw_arguments) if isinstance(raw_arguments, str) else dict(raw_arguments)
    except (json.JSONDecodeError, TypeError, ValueError):
        return "Argumentos inválidos: tienen que ser un objeto JSON."
    return tools[name][2](arguments)


def _responses(model, effort, text, tools, max_turns, finish_check):
    client = _client()
    specs = [{"type": "function", "name": name, "description": desc, "parameters": schema}
             for name, (desc, schema, _) in tools.items()]
    transcript = [{"role": "user", "content": text}]
    usage = {"calls": 0, "input": 0, "output": 0, "reasoning": 0, "cached": 0}
    pending, previous, final, asked = [{"role": "user", "content": text}], None, None, False
    for _ in range(max_turns):
        kwargs = {"model": model, "input": pending, "tools": specs, "max_output_tokens": MAX_OUTPUT_TOKENS}
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
                           "tool_calls": [{"id": c.call_id, "name": c.name, "arguments": c.arguments} for c in calls]})
        if calls:
            pending = []
            for call in calls:
                output = _call(tools, call.name, call.arguments)
                pending.append({"type": "function_call_output", "call_id": call.call_id, "output": output})
                transcript.append({"role": "tool", "tool_call_id": call.call_id, "content": output})
            continue
        final = resp.output_text
        follow_up = None if asked else finish_check()
        if follow_up is None:
            break
        asked = True
        pending = [{"role": "user", "content": follow_up}]
        transcript.append(pending[0])
    return transcript, usage, final


def _chat(model, effort, text, tools, max_turns, finish_check):
    client = _client()
    specs = [{"type": "function", "function": {"name": name, "description": desc, "parameters": schema}}
             for name, (desc, schema, _) in tools.items()]
    messages = [{"role": "user", "content": text}]
    usage = {"calls": 0, "input": 0, "output": 0, "reasoning": 0, "cached": 0}
    final, asked = None, False
    for _ in range(max_turns):
        kwargs = {"model": model, "messages": messages, "tools": specs, "max_completion_tokens": MAX_OUTPUT_TOKENS}
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
                messages.append({"role": "tool", "tool_call_id": tc.id,
                                 "content": _call(tools, tc.function.name, tc.function.arguments)})
            continue
        final = msg.content
        follow_up = None if asked else finish_check()
        if follow_up is None:
            break
        asked = True
        messages.append({"role": "user", "content": follow_up})
    return messages, usage, final


def run_agent(model: str, effort: str | None, text: str, tools: dict, max_turns: int, finish_check):
    """Devuelve (conversación completa, tokens gastados, último texto del modelo)."""
    if model.startswith("claude"):
        from shared import claude_loop

        return claude_loop.run(model, effort, text, tools, max_turns, finish_check)
    if model.startswith("gpt-"):
        return _responses(model, effort, text, tools, max_turns, finish_check)
    return _chat(model, effort, text, tools, max_turns, finish_check)
