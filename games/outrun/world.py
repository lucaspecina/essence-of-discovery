"""El mundo de los dos primeros juegos de `outrun`: la regla y cómo se corre paso por paso.

Una fila de casillas sin fin, hacia los dos lados. Cada casilla tiene un símbolo: "." (vacía), "a", "b",
"c", "d" o "e". En cada paso todas cambian a la vez; el símbolo nuevo de una casilla depende de tres
símbolos del paso anterior: el de su izquierda, el suyo y el de su derecha. La regla es la lista `RULE`;
todo trío que no figura da "." (vacía).

Cómo se armó la regla: dibujando lo que queríamos que pasara (cosas que viajan, una pared que rebota y se
corre) y anotando cada trío que aparecía en el dibujo. Lo que hace de verdad puede tener más cosas que las
que dibujamos: la verdad de los juegos es siempre lo que da esta regla al correrla.

Una fila se guarda como un diccionario {posición: símbolo} con las casillas no vacías.
"""
from __future__ import annotations

SYMBOLS = ".abcde"

RULE = {
    # un par "a b" y una letra sola (a o b) viajan a la derecha, un lugar por paso, cambiando de letra
    (".", "a", "b"): ".", ("a", "b", "."): "b", ("b", ".", "."): "a",
    (".", "b", "a"): ".", ("b", "a", "."): "a", ("a", ".", "."): "b",
    # la c viaja a la izquierda; la d se queda quieta
    (".", ".", "c"): "c", (".", "d", "."): "d",
    # un par que se encuentra con una c
    ("a", ".", "c"): "d",
    # algo que viene de la izquierda y toca una d
    ("a", ".", "d"): "b", ("b", ".", "d"): "a",
    (".", "b", "d"): "c", ("b", "d", "."): "e",
    (".", "a", "d"): "c", ("a", "d", "."): "e",
    ("e", ".", "."): "d",
    # una c que viene de la derecha y toca una d
    ("d", ".", "c"): "c", (".", "d", "c"): "d", ("d", "c", "."): "a", (".", "d", "a"): "d",
}


def step(cells: dict) -> dict:
    """Un paso. `cells` es {posición: símbolo} con las casillas no vacías."""
    candidates = set()
    for p in cells:
        candidates.update((p - 1, p, p + 1))
    new = {}
    for p in candidates:
        symbol = RULE.get((cells.get(p - 1, "."), cells.get(p, "."), cells.get(p + 1, ".")), ".")
        if symbol != ".":
            new[p] = symbol
    return new


def run(cells: dict, steps: int) -> dict:
    """Corre la regla `steps` pasos, uno por uno. Es la realidad contra la que se compara todo."""
    cells = dict(cells)
    for _ in range(steps):
        cells = step(cells)
    return cells


def show(cells: dict, lo: int | None = None, hi: int | None = None) -> str:
    """La fila como texto, entre las posiciones `lo` y `hi` (por defecto, de la primera a la última no vacía)."""
    if not cells:
        return "(vacía)"
    lo = min(cells) if lo is None else lo
    hi = max(cells) if hi is None else hi
    return " ".join(cells.get(p, ".") for p in range(lo, hi + 1))


def parse(text: str, origin: int = 0) -> dict:
    """Lo inverso de `show`: "d . a . d" con la primera casilla en `origin`."""
    return {origin + i: ch for i, ch in enumerate(text.split()) if ch != "."}


def clusters(cells: dict) -> list:
    """Parte la fila en grupos de casillas que se pueden influir (separadas por menos de dos vacías)."""
    groups, current = [], []
    for p in sorted(cells):
        if current and p - current[-1] > 2:
            groups.append(current)
            current = []
        current.append(p)
    if current:
        groups.append(current)
    return [{p: cells[p] for p in group} for group in groups]
