"""La misma partida, para los modelos Claude: van por el SDK de Anthropic contra Microsoft Foundry.

Lazo manual de herramientas, como lo documenta el SDK: se manda la conversación, si el modelo pide
ejecutar código se ejecuta y se le devuelve el resultado, y así hasta que entrega su respuesta.
"""
from __future__ import annotations

import os

MAX_TOKENS = 64000


def play(model: str, effort: str | None, text: str, sandbox, run_tool, parse_answers, tool_description: str,
         ask_again: str, max_turns: int):
    from anthropic import AnthropicFoundry

    base = os.environ["AZURE_FOUNDRY_BASE_URL"].split(".openai.azure.com")[0] + ".services.ai.azure.com/anthropic"
    client = AnthropicFoundry(api_key=os.environ["AZURE_INFERENCE_CREDENTIAL"], base_url=base, timeout=3600.0)
    tools = [{"name": "run_python", "description": tool_description,
              "input_schema": {"type": "object", "required": ["code"],
                               "properties": {"code": {"type": "string", "description": "El código. Usá print() para ver resultados."}}}}]
    messages = [{"role": "user", "content": text}]        # lo que se le manda al modelo (bloques tal cual)
    transcript = [{"role": "user", "content": text}]      # lo mismo, en texto plano, para guardar
    usage = {"calls": 0, "input": 0, "output": 0, "reasoning": 0, "cached": 0}
    final, asked_again = None, False
    for _ in range(max_turns):
        kwargs = {"model": model, "max_tokens": MAX_TOKENS, "messages": messages, "tools": tools,
                  "thinking": {"type": "adaptive"}}
        if effort:
            kwargs["output_config"] = {"effort": effort}
        with client.messages.stream(**kwargs) as stream:
            response = stream.get_final_message()
        u = response.usage
        usage["calls"] += 1
        usage["input"] += u.input_tokens + (u.cache_read_input_tokens or 0) + (u.cache_creation_input_tokens or 0)
        usage["output"] += u.output_tokens
        usage["cached"] += u.cache_read_input_tokens or 0
        messages.append({"role": "assistant", "content": response.content})
        transcript.append({"role": "assistant", "stop_reason": response.stop_reason,
                           "content": [b.model_dump(mode="json", exclude_none=True) for b in response.content]})
        calls = [b for b in response.content if b.type == "tool_use"]
        if response.stop_reason == "tool_use" and calls:
            results = [{"type": "tool_result", "tool_use_id": b.id,
                        "content": run_tool(sandbox, b.input.get("code") if isinstance(b.input, dict) else None)}
                       for b in calls]
            messages.append({"role": "user", "content": results})
            transcript.append({"role": "user", "content": results})
            continue
        final = "".join(b.text for b in response.content if b.type == "text")
        if parse_answers(final) is not None or asked_again:
            break
        asked_again = True
        messages.append({"role": "user", "content": ask_again})
        transcript.append({"role": "user", "content": ask_again})
    return transcript, usage, final
