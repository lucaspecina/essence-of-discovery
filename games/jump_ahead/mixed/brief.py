"""Lo que recibe la IA en un juego mezclado: el texto y los dos archivos de su carpeta de trabajo.

Nada de acá dice si debajo hay un sistema conocido o no: el juego mezclado y el de control sin regla
se presentan igual. La pista (`hint=True`) solo se usa en la segunda vuelta, para los juegos que una IA
no resolvió: nombra la idea, sin dar la respuesta.
"""
from __future__ import annotations

import json

HINT = (
    "\nPISTA\n"
    "La tabla es un sistema conocido con los nombres de los símbolos cambiados. Existe una forma de "
    "\"sumar\" símbolos (una tabla de suma escondida) con la que el símbolo nuevo es la suma de tres partes: "
    "una que depende solo de la izquierda, otra solo de la propia casilla y otra solo de la derecha.\n"
)


def symbols_of(game) -> list:
    if game.game_id.startswith("plain"):
        return [str(v) for v in range(game.q)]
    return list(game.alphabet)


def make_brief(game, max_runs: int, run_seconds: float, hint: bool = False):
    """Devuelve (texto, archivos, símbolos). `archivos` es {nombre: contenido}."""
    symbols = symbols_of(game)
    k = len(symbols)
    table, start = game.visible_table(), game.visible_start()
    table_json = {symbols[l] + symbols[c] + symbols[r]: symbols[int(table[l, c, r])]
                  for l in range(k) for c in range(k) for r in range(k)}
    start_text = "".join(symbols[int(v)] for v in start)
    examples = ", ".join(f'"{key}" -> "{table_json[key]}"' for key in list(table_json)[1:k * k * k:max(1, k**3 // 5)][:5])
    wrong = -(k + 1) / (k - 1)
    extra = ""
    if game.game_id.startswith("plain"):
        a, b, c = (m[0][0] for m in game.matrices)
        extra = (f"- La misma regla, escrita como una cuenta: nuevo = ({a}·izquierda + {b}·propia + {c}·derecha) "
                 f"módulo {game.p}.\n")
    text = (
        "Tenés que predecir el estado lejano de un sistema simple.\n"
        "\nEL SISTEMA\n"
        f"- Hay {game.n} casillas en anillo, numeradas de 0 a {game.n - 1}. La casilla {game.n - 1} es vecina de la 0.\n"
        f"- Cada casilla tiene un símbolo. Hay {k} símbolos posibles: {' '.join(symbols)}.\n"
        "- En cada paso todas las casillas cambian a la vez. El símbolo nuevo de la casilla i depende solo de tres "
        "símbolos del paso anterior: el de la casilla i-1 (izquierda), el de la casilla i (ella misma) y el de la "
        "casilla i+1 (derecha).\n"
        f"- La regla es una tabla de {k**3} renglones. Está completa en el archivo `table.json`: un diccionario cuya "
        "clave son esos tres símbolos pegados, en ese orden (izquierda, ella misma, derecha), y cuyo valor es el "
        f"símbolo nuevo. Algunos renglones: {examples}.\n"
        f"{extra}"
        "- El estado del paso 0 está en `start.txt` (un símbolo por casilla, empezando por la casilla 0):\n"
        f"  {start_text}\n"
        "\nLA PREGUNTA\n"
        f"¿Qué símbolo tiene cada una de estas casillas en el paso {game.far_step} (10^18)? "
        f"Casillas: {', '.join(map(str, game.cells))}.\n"
        "\nTU COMPUTADORA\n"
        f"Tenés la herramienta `run_python` para ejecutar código Python 3 (con numpy). Límites: {max_runs} "
        f"ejecuciones en total, de hasta {run_seconds:.0f} segundos cada una, en un solo núcleo, sin internet y sin "
        "poder lanzar otros programas. `table.json` y `start.txt` están en el directorio de trabajo; lo que guardes "
        "ahí queda para las ejecuciones siguientes. Con esos límites no se llega al paso 10^18 simulando paso por paso.\n"
        f"{HINT if hint else ''}"
        "\nCÓMO RESPONDER\n"
        "Cuando termines, respondé con un único bloque JSON, sin texto después:\n"
        '{"answers": [{"cell": 3, "symbol": "' + symbols[0] + '", "confidence": 0.9}, ...], '
        '"method": "una línea sobre cómo lo resolviste"}\n'
        "- Una entrada por cada casilla preguntada.\n"
        "- `confidence` es tu probabilidad de que ese símbolo sea el correcto, entre 0 y 1.\n"
        f"- Si no hay forma de saberlo, decilo: poné confidence = {1 / k:.3g} (puro azar entre {k} símbolos).\n"
        "\nPUNTAJE (por casilla)\n"
        "- Acertar con confidence 1: +1.\n"
        f"- confidence = {1 / k:.3g} (\"no sé\"): 0.\n"
        f"- Equivocarse con confidence 1: {wrong:.2f}.\n"
        "Equivocarse estando seguro cuesta más que admitir que no se sabe.\n"
    )
    files = {"table.json": json.dumps(table_json), "start.txt": start_text}
    return text, files, symbols
