"""La misma conversación con herramientas, para los modelos Claude (SDK de Anthropic contra Microsoft Foundry).

Lazo manual, como lo documenta el SDK: se manda la conversación; si el modelo pide una herramienta, se
ejecuta y se le devuelve el resultado; así hasta que deja de pedir.
"""
from __future__ import annotations

import os

MAX_TOKENS = 64000


def run(model: str, effort: str | None, text: str, tools: dict, max_turns: int, finish_check):
    from anthropic import AnthropicFoundry

    base = os.environ["AZURE_FOUNDRY_BASE_URL"].split(".openai.azure.com")[0] + ".services.ai.azure.com/anthropic"
    client = AnthropicFoundry(api_key=os.environ["AZURE_INFERENCE_CREDENTIAL"], base_url=base, timeout=3600.0)
    specs = [{"name": name, "description": desc, "input_schema": schema} for name, (desc, schema, _) in tools.items()]
    messages = [{"role": "user", "content": text}]        # lo que se le manda al modelo (bloques tal cual)
    transcript = [{"role": "user", "content": text}]      # lo mismo, en texto plano, para guardar
    usage = {"calls": 0, "input": 0, "output": 0, "reasoning": 0, "cached": 0}
    final, asked = None, False
    for _ in range(max_turns):
        kwargs = {"model": model, "max_tokens": MAX_TOKENS, "messages": messages, "tools": specs,
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
            results = []
            for block in calls:
                handler = tools.get(block.name)
                output = handler[2](block.input if isinstance(block.input, dict) else {}) if handler else f"No existe la herramienta {block.name}."
                results.append({"type": "tool_result", "tool_use_id": block.id, "content": output})
            messages.append({"role": "user", "content": results})
            transcript.append({"role": "user", "content": results})
            continue
        final = "".join(b.text for b in response.content if b.type == "text")
        follow_up = None if asked else finish_check()
        if follow_up is None:
            break
        asked = True
        messages.append({"role": "user", "content": follow_up})
        transcript.append({"role": "user", "content": follow_up})
    return transcript, usage, final
