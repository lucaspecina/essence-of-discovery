"""Programa de referencia 2: una receta general, que no sabe nada de este mundo en particular.

La receta: partir la fila en grupos alejados entre sí; fijarse, corriendo cada grupo solo, si viaja o se
queda quieto sin cambiar; saltar de una vez todo el tramo en que los grupos no se pueden tocar; y aplicar
la regla paso por paso solo mientras dos grupos están cerca.

Resume los viajes, pero cada encuentro lo hace paso por paso. Alcanza cuando hay pocos encuentros.
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


def split(cells):
    """Grupos de casillas ocupadas separados por dos o más vacías (no se pueden influir en un paso)."""
    groups, current = [], {}
    last = None
    for p in sorted(cells):
        if last is not None and p - last > 2:
            groups.append(current)
            current = {}
        current[p] = cells[p]
        last = p
    if current:
        groups.append(current)
    return groups


def how_it_moves(group):
    """(cada cuántos pasos se repite, cuántas casillas se corre por paso), o None si el grupo solo no se repite."""
    one = step(group)
    for v in (-1, 0, 1):
        if one == {p + v: s for p, s in group.items()}:
            return 1, v
    two = step(one)
    for v in (-1, 0, 1):
        if two == {p + 2 * v: s for p, s in group.items()}:
            return 2, v
    return None


def predict(start, steps):
    cells, left = dict(start), steps
    while left > 0 and cells:
        groups = split(cells)
        moves = [how_it_moves(g) for g in groups]
        if any(m is None for m in moves):
            cells, left = step(cells), left - 1
            continue
        jump = left                                     # cuántos pasos se pueden saltar sin que nadie se toque
        for i in range(len(groups) - 1):
            closing = moves[i][1] - moves[i + 1][1]
            if closing > 0:
                gap = min(groups[i + 1]) - max(groups[i]) - 1
                jump = min(jump, (gap - 3) // closing + 1 if gap >= 3 else 0)
        if jump <= 0:
            cells, left = step(cells), left - 1
            continue
        new = {}
        for group, (period, v) in zip(groups, moves):
            rest = jump % period
            moved = {p + v * (jump - rest): s for p, s in group.items()}
            for _ in range(rest):
                moved = step(moved)
            new.update(moved)
        cells, left = new, left - jump
    return cells
