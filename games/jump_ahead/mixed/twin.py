"""El juego de control: una tabla sorteada entera al azar, sin regla de resultado conocida.

Se ve igual que un juego mezclado (letras y una tabla), pero debajo no hay ningún sistema conocido.
La respuesta del paso lejano la sacamos a pura fuerza: contamos paso por paso, con un programa en C,
hasta que la fila vuelve a repetirse. Eso lleva miles de millones de pasos; la IA no tiene ese tiempo.
"""
from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path

import numpy as np

HERE = Path(__file__).parent
BUILD = HERE / ".build"


@dataclass(frozen=True)
class TwinGame:
    game_id: str
    q: int
    n: int
    seed: int
    far_step: int
    cells: tuple

    @property
    def alphabet(self) -> str:
        from .linear import LETTERS
        return LETTERS[: self.q]

    def visible_table(self) -> np.ndarray:
        rng = np.random.default_rng(self.seed)
        return rng.integers(0, self.q, size=(self.q, self.q, self.q))

    def visible_start(self) -> np.ndarray:
        rng = np.random.default_rng(self.seed + 1)
        return rng.integers(0, self.q, size=self.n)


def c_tool() -> Path:
    """Compila el contador en C la primera vez."""
    BUILD.mkdir(exist_ok=True)
    exe = BUILD / "cyclefind"
    src = HERE / "cyclefind.c"
    if not exe.exists() or exe.stat().st_mtime < src.stat().st_mtime:
        subprocess.run(["cc", "-O3", "-o", str(exe), str(src)], check=True)
    return exe


def _problem(table: np.ndarray, start: np.ndarray) -> str:
    q, n = table.shape[0], len(start)
    return f"{q} {n}\n" + " ".join(map(str, table.reshape(-1).tolist())) + "\n" + " ".join(map(str, start.tolist())) + "\n"


def find_cycle(table: np.ndarray, start: np.ndarray, max_steps: int):
    """Cuenta hasta que la fila se repite. Devuelve (mu, lam): el ciclo empieza en el paso mu y mide lam.
    None si no se repite en max_steps."""
    out = subprocess.run([str(c_tool()), "brent", str(max_steps)], input=_problem(table, start),
                         capture_output=True, text=True, check=True).stdout.split()
    return (int(out[1]), int(out[2])) if out[0] == "CYCLE" else None


def advance(table: np.ndarray, start: np.ndarray, steps: int) -> np.ndarray:
    """La fila después de `steps` pasos, contando uno por uno (en C)."""
    out = subprocess.run([str(c_tool()), "advance", str(steps)], input=_problem(table, start),
                         capture_output=True, text=True, check=True).stdout.split()
    return np.array(list(map(int, out)))


def far_state_from_cycle(table: np.ndarray, start: np.ndarray, far_step: int, mu: int, lam: int) -> np.ndarray:
    """Conociendo el ciclo, el paso lejano es igual a un paso cercano: se cuenta hasta ese."""
    near = far_step if far_step < mu else mu + (far_step - mu) % lam
    return advance(table, start, near)
