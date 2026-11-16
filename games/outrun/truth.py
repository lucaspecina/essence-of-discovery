"""La realidad corrida rápido: la misma regla, paso por paso, en C. Ver `truth.c`.

`run_fast(cells, steps)` da lo mismo que `world.run(cells, steps)`; `verify_worlds.py` lo comprueba.
"""
from __future__ import annotations

import subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from world import RULE, SYMBOLS

HERE = Path(__file__).resolve().parent
BINARY = HERE / ".build" / "truth"


def _tool() -> Path:
    source = HERE / "truth.c"
    if not BINARY.exists() or BINARY.stat().st_mtime < source.stat().st_mtime:
        BINARY.parent.mkdir(exist_ok=True)
        subprocess.run(["cc", "-O2", "-o", str(BINARY), str(source)], check=True)
    return BINARY


def _table() -> str:
    k = len(SYMBOLS)
    index = {s: i for i, s in enumerate(SYMBOLS)}
    flat = [0] * (k ** 3)
    for (l, c, r), new in RULE.items():
        flat[(index[l] * k + index[c]) * k + index[r]] = index[new]
    return f"{k}\n" + " ".join(map(str, flat)) + "\n"


def run_fast(cells: dict, steps: int) -> dict:
    index = {s: i for i, s in enumerate(SYMBOLS)}
    lines = [_table(), f"{steps}\n{len(cells)}\n"]
    lines += [f"{p} {index[cells[p]]}\n" for p in sorted(cells)]
    done = subprocess.run([str(_tool())], input="".join(lines), capture_output=True, text=True)
    if done.returncode != 0:
        raise RuntimeError(f"truth.c devolvió {done.returncode}: {done.stderr[:200]}")
    out = done.stdout.split()
    n = int(out[0])
    return {int(out[1 + 2 * i]): SYMBOLS[int(out[2 + 2 * i])] for i in range(n)}


def run_many(jobs: list, workers: int = 8) -> list:
    """jobs: lista de (cells, steps). Devuelve las filas finales en el mismo orden."""
    _tool()
    with ThreadPoolExecutor(max_workers=workers) as pool:
        return list(pool.map(lambda job: run_fast(*job), jobs))
