"""Programa de referencia 1: no resume nada. Copia la regla y la aplica paso por paso.

Tiene que acertar en las distancias chicas y quedarse sin tiempo en las grandes. Marca el piso: lo que
se logra sin haber entendido nada del mundo.
"""
RULE = {
    (".", "a", "b"): ".", ("a", "b", "."): "b", ("b", ".", "."): "a",
    (".", "b", "a"): ".", ("b", "a", "."): "a", ("a", ".", "."): "b",
    (".", ".", "c"): "c", (".", "d", "."): "d",
    ("a", ".", "c"): "d",
    ("a", ".", "d"): "b", ("b", ".", "d"): "a",
    (".", "b", "d"): "c", ("b", "d", "."): "e",
    (".", "a", "d"): "c", ("a", "d", "."): "e",
    ("e", ".", "."): "d",
    ("d", ".", "c"): "c", (".", "d", "c"): "d", ("d", "c", "."): "a", (".", "d", "a"): "d",
}


def step(cells):
    candidates = set()
    for p in cells:
        candidates.update((p - 1, p, p + 1))
    new = {}
    for p in candidates:
        s = RULE.get((cells.get(p - 1, "."), cells.get(p, "."), cells.get(p + 1, ".")), ".")
        if s != ".":
            new[p] = s
    return new


def predict(start, steps):
    cells = dict(start)
    for _ in range(steps):
        cells = step(cells)
    return cells
