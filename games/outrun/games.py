"""Los dos primeros juegos de `outrun`. Usan el mismo mundo (`world.py`) y cambian los comienzos.

- `collisions` (simple): cosas que viajan, se encuentran una o dos veces y se separan.
- `pingpong` (más complejo): una cosa atrapada entre dos paredes. Rebota, y en cada rebote contra la
  pared derecha esa pared se corre un lugar. Cada vuelta tarda un poco más que la anterior.

Cada juego define: cómo se sortea un comienzo, a qué distancias se pregunta y los topes del programa.
"""
from __future__ import annotations

import inspect
import math
import random
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

import world


def sample_collisions(rng: random.Random) -> dict:
    """Entre dos y cuatro fichas en fila, en cualquier orden: pares "a b" (uno o dos) y letras "c" (una o
    dos). Entre una ficha y la siguiente hay entre 2 y 1.000.000 de casillas vacías; la cantidad se sortea
    de modo que haya tanto separaciones chicas como grandes."""
    kinds = ["ab"] * rng.randint(1, 2) + ["c"] * rng.randint(1, 2)
    rng.shuffle(kinds)
    cells, x = {}, rng.randint(-1000, 1000)
    for kind in kinds:
        for i, ch in enumerate(kind):
            cells[x + i] = ch
        x += len(kind) + int(round(10 ** rng.uniform(math.log10(2), 6)))
    return cells


def sample_pingpong(rng: random.Random) -> dict:
    """Dos paredes "d" y, entre ellas, una sola cosa que se mueve: una letra "a", "b" o "c". La distancia
    entre las paredes va de 3 a 3.000 (sorteada de modo que haya chicas y grandes). Una de cada cuatro veces
    la cosa arranca pegada a una de las dos paredes; el resto, en cualquier casilla de adentro."""
    left = rng.randint(-1000, 1000)
    width = int(round(10 ** rng.uniform(math.log10(3), math.log10(3000))))
    mover = rng.choice("abc")
    inside = rng.choice([1, width - 1]) if rng.random() < 0.25 else rng.randint(1, width - 1)
    return {left: "d", left + width: "d", left + inside: mover}


@dataclass(frozen=True)
class Game:
    game_id: str
    title: str
    sample: Callable
    scales: tuple = tuple(range(1, 10))      # se pregunta por pasos entre 10^k y 2·10^k, para cada k
    cases_per_scale: int = 8
    limit_seconds: float = 1.0               # tope de tiempo de cada llamada a predict
    size_limit: int = 20_000                 # tope de tamaño de solution.py, en bytes
    eval_seed: int = 0

    @property
    def family_text(self) -> str:
        return " ".join(inspect.getdoc(self.sample).split())


GAMES = {
    "collisions": Game("collisions", "Cosas que viajan y chocan", sample_collisions, eval_seed=20261116),
    "pingpong": Game("pingpong", "Una cosa que rebota entre dos paredes", sample_pingpong,
                     scales=tuple(range(1, 11)), eval_seed=20261117),
}


def case_kind(game_id: str, start: dict) -> str:
    """Etiqueta mecánica de un comienzo, para desglosar el puntaje. En `pingpong`, "excepción" son los dos
    comienzos donde una pared desaparece: una "b" pegada a la pared izquierda o una "c" pegada a la derecha."""
    if game_id == "pingpong":
        cells = {int(p): s for p, s in start.items()}
        left, right = min(cells), max(cells)
        if cells.get(left + 1) == "b" or cells.get(right - 1) == "c":
            return "excepción"
    return "normal"


def make_cases(game: Game, seed: int | None = None) -> list:
    """Los casos de prueba: para cada distancia, comienzos nuevos y una cantidad de pasos de esa distancia."""
    rng = random.Random(game.eval_seed if seed is None else seed)
    cases = []
    for k in game.scales:
        for i in range(game.cases_per_scale):
            cases.append({"id": f"e{k}-{i}", "scale": k, "start": game.sample(rng),
                          "steps": rng.randint(10 ** k, 2 * 10 ** k)})
    return cases


# --- lo que recibe la IA en su carpeta de trabajo --------------------------------------------------

def world_file(game: Game) -> str:
    """`world.py` para la IA: la regla, el simulador paso por paso y el sorteo de comienzos de este juego."""
    source = Path(world.__file__).read_text(encoding="utf-8")
    sample = inspect.getsource(game.sample).replace(f"def {game.sample.__name__}(rng: random.Random)", "def _sample(rng)")
    return (source + "\n\nimport math\nimport random\n\n\n" + sample +
            "\n\ndef sample_start(seed: int) -> dict:\n"
            '    """Un comienzo de este juego, sorteado con esa semilla. La prueba usa otros comienzos de la misma familia."""\n'
            "    return _sample(random.Random(seed))\n")


_CHECK_FILE = '''"""Para probar tu solution.py: lo compara contra la regla corrida paso por paso y mide tiempos.

    import check
    check.compare()      # 200 comienzos sorteados, pasos chicos: ¿da lo mismo que world.run?
    check.timing()       # cuánto tarda predict a cada distancia (no comprueba el resultado)
"""
import importlib
import random
import time

import world

MAX_SCALE = __MAX_SCALE__     # el tamaño más grande que se prueba es 2 * 10 ** MAX_SCALE pasos


def compare(cases=200, max_steps=3000, seed=0):
    import solution
    importlib.reload(solution)
    rng, wrong = random.Random(seed), 0
    for i in range(cases):
        start = world.sample_start(rng.randrange(10 ** 9))
        steps = rng.randint(0, max_steps)
        truth = world.run(start, steps)
        got = {int(p): s for p, s in dict(solution.predict(dict(start), steps)).items() if s != "."}
        if got != truth:
            wrong += 1
            if wrong <= 3:
                print(f"DISTINTO  comienzo={start}  pasos={steps}\\n   regla:    {truth}\\n   solution: {got}")
    print(f"{cases - wrong} de {cases} iguales a la regla (pasos hasta {max_steps})")


def timing(seed=0, limit=1.0):
    import solution
    importlib.reload(solution)
    rng = random.Random(seed)
    for k in range(1, MAX_SCALE + 1):
        start = world.sample_start(rng.randrange(10 ** 9))
        steps = rng.randint(10 ** k, 2 * 10 ** k)
        t0 = time.perf_counter()
        solution.predict(dict(start), steps)
        dt = time.perf_counter() - t0
        print(f"pasos {steps:>13,}: {dt:8.4f} s {'  <-- pasa el tope' if dt > limit else ''}")
        if dt > 20:
            print("(corto acá: tarda demasiado)")
            break
'''


def check_file(game: Game) -> str:
    """`check.py` para la IA: compara su programa contra la regla y mide tiempos."""
    return _CHECK_FILE.replace("__MAX_SCALE__", str(max(game.scales)))


def rule_listing() -> str:
    lines = [f"  ({l} {c} {r}) -> {new}" for (l, c, r), new in world.RULE.items()]
    return "\n".join(lines)


def make_brief(game: Game, max_runs: int, run_seconds: float) -> str:
    top = 2 * 10 ** max(game.scales)
    return f"""Tu trabajo es escribir un programa que prediga cómo queda un mundo sin recorrer todos los pasos.

EL MUNDO
- Una fila de casillas sin fin hacia los dos lados, numeradas con enteros (..., -2, -1, 0, 1, 2, ...).
- Cada casilla tiene un símbolo: "." (vacía), "a", "b", "c", "d" o "e".
- En cada paso todas las casillas cambian a la vez. El símbolo nuevo de una casilla depende de tres símbolos
  del paso anterior: el de su izquierda, el suyo y el de su derecha.
- La regla completa son estos {len(world.RULE)} renglones, escritos (izquierda propia derecha) -> nuevo.
  Todo trío que no está en la lista da "." (vacía):
{rule_listing()}
- Una fila se escribe como un diccionario de Python {{posición: símbolo}} con las casillas NO vacías.

LOS COMIENZOS DE ESTE JUEGO
{game.family_text}

LO QUE TENÉS QUE ENTREGAR
Un archivo `solution.py` en tu directorio de trabajo, con una función:

    def predict(start, steps):
        # start: diccionario {{posición: símbolo}} con las casillas no vacías del paso 0
        # steps: entero >= 0
        # devuelve: diccionario {{posición: símbolo}} con las casillas no vacías después de `steps` pasos

CÓMO SE VA A PROBAR
- `solution.py` se prueba solo, en una carpeta vacía: no puede importar `world.py` ni leer archivos. Puede
  usar la biblioteca estándar de Python y numpy.
- Se lo llama con comienzos nuevos (sorteados igual que los de este juego, pero otros) y con cantidades de
  pasos de todos los tamaños: desde 10 hasta {top:,}. Hay {game.cases_per_scale} casos de cada tamaño
  (decenas, cientos, miles, y así hasta el más grande).
- Un caso está bien si el resultado es EXACTAMENTE el que da la regla corrida paso por paso (eso lo corremos
  nosotros) y la llamada tarda menos de {game.limit_seconds:g} segundo.
- El archivo no puede pesar más de {game.size_limit:,} bytes.

EL PUNTAJE
- Por cada tamaño, cuántos casos están bien. El número principal: hasta qué tamaño están todos bien.
- Hay crédito parcial. Un programa que aplica la regla paso por paso acierta en los tamaños chicos y se queda
  sin tiempo en los grandes. Para llegar lejos hace falta saber qué va a pasar sin hacer todos los pasos.
- Se miden tres cosas: si coincide con la regla, cuánto pesa el archivo y cuánto tarda.

TU COMPUTADORA
- Herramienta `run_python`: ejecuta código Python 3 (con numpy) en tu directorio de trabajo y devuelve lo
  que imprime. Tenés {max_runs} ejecuciones, de hasta {run_seconds:.0f} segundos cada una, en un solo núcleo,
  sin internet. Lo que guardes en el directorio queda para las ejecuciones siguientes.
- Herramienta `write_file`: escribe un archivo en tu directorio de trabajo (no gasta ejecuciones).
- Ya hay dos archivos:
  - `world.py`: la regla (`RULE`), `step(cells)`, `run(cells, steps)` que la corre paso por paso,
    `show(cells)`, `parse(texto)` y `sample_start(seed)` que sortea un comienzo de este juego.
  - `check.py`: `check.compare()` compara tu `solution.py` contra `world.run` en comienzos sorteados;
    `check.timing()` mide cuánto tarda a cada tamaño.
- Referencia de velocidad: en esta máquina `world.run` hace unos 500.000 pasos por segundo cuando hay tres
  casillas ocupadas.

Usá las ejecuciones que necesites para investigar el mundo y probar tu programa. Cuando termines, dejá el
`solution.py` definitivo en el directorio y respondé con la palabra LISTO y dos o tres líneas contando cómo
funciona tu programa.
"""
