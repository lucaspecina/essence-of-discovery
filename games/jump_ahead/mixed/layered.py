"""Juegos de dos capas: la estructura está escondida más hondo que en los juegos mezclados.

Cada símbolo esconde un par (x, y), con x e y entre 0 y p-1.

- La capa de base (x) cambia con una tabla CUALQUIERA, sorteada, sin fórmula. Se elige una que se
  repita pronto (miles de pasos): eso se puede ver contando.
- La capa de arriba (y) cambia como una suma de sus vecinas, MÁS un empujón que depende de la base:

      y' = a·y_izq + b·y + c·y_der + g(x_izq, x, x_der)       (módulo p; g es una tabla sorteada)

- El símbolo que ve la IA es el par (x, y) con un nombre sorteado.

Ninguna de las dos herramientas alcanza sola. Contar no alcanza: el conjunto no se repite en miles de
millones de pasos. Reconstruir una suma tampoco: por el empujón, la tabla entera no es una suma. Hay que
ver las dos capas: una base que se repite, y arriba una suma con empujones que se repiten con la base.

Nuestro salto: se cuenta la base hasta que se repite; un ciclo entero de la base actúa sobre la capa de
arriba como "multiplicar por M y sumar C"; eso se repite millones de veces con potencia por cuadrados.
"""
from __future__ import annotations

import random
from dataclasses import dataclass

import numpy as np

from .linear import LETTERS
from .twin import find_cycle


@dataclass(frozen=True)
class LayeredGame:
    game_id: str
    p: int
    n: int
    base_seed: int           # la tabla de la capa de base sale de acá
    coeffs: tuple            # (a, b, c) de la capa de arriba
    push_seed: int           # la tabla del empujón g sale de acá
    order: tuple             # order[x + p·y] = número de letra. Es el secreto.
    start_x: tuple
    start_y: tuple
    far_step: int
    cells: tuple

    @property
    def q(self) -> int:
        return self.p**2

    @property
    def alphabet(self) -> str:
        return LETTERS[: self.q]

    def base_table(self) -> np.ndarray:
        return np.random.default_rng(self.base_seed).integers(0, self.p, size=(self.p,) * 3)

    def push_table(self) -> np.ndarray:
        return np.random.default_rng(self.push_seed).integers(0, self.p, size=(self.p,) * 3)

    # --- lo que ve la IA ---
    def visible_table(self) -> np.ndarray:
        p, q = self.p, self.q
        base, push, order = self.base_table(), self.push_table(), np.array(self.order)
        a, b, c = self.coeffs
        back = np.argsort(order)                                    # back[letra] = x + p·y
        l, m, r = np.meshgrid(back, back, back, indexing="ij")
        xl, yl, xm, ym, xr, yr = l % p, l // p, m % p, m // p, r % p, r // p
        new_x = base[xl, xm, xr]
        new_y = (a * yl + b * ym + c * yr + push[xl, xm, xr]) % p
        return order[new_x + p * new_y]

    def visible_start(self) -> np.ndarray:
        return np.array(self.order)[np.array(self.start_x) + self.p * np.array(self.start_y)]

    # --- nuestro salto ---
    def _parts(self):
        n, p = self.n, self.p
        a, b, c = self.coeffs
        kernel = np.zeros((n, n), dtype=np.int64)
        for i in range(n):
            kernel[i, (i - 1) % n], kernel[i, i], kernel[i, (i + 1) % n] = a, b, c
        base, push = self.base_table(), self.push_table()
        base_step = lambda x: base[np.roll(x, 1), x, np.roll(x, -1)]       # noqa: E731
        push_of = lambda x: push[np.roll(x, 1), x, np.roll(x, -1)]         # noqa: E731
        return kernel, base_step, push_of, p

    def hidden_jump(self, steps: int):
        prepared = _prepare(self)
        kernel, base_step, push_of, p = self._parts()

        def run(x, y, count):                                        # pasos de a uno
            for _ in range(count):
                y = (kernel @ y + push_of(x)) % p
                x = base_step(x)
            return x, y

        mu, lam = prepared["cycle"]
        if steps < mu:
            return run(np.array(self.start_x), np.array(self.start_y), steps)
        x, y = prepared["at_cycle_start"]
        laps, rest = divmod(steps - mu, lam)
        m_total, c_total = _affine_pow(prepared["block"], prepared["shift"], laps, p)
        return run(x, (m_total @ y + c_total) % p, rest)

    def base_cycle(self) -> tuple:
        """Cuándo se repite la capa de base: (empieza el ciclo, largo del ciclo)."""
        return _prepare(self)["cycle"]

    def truth(self) -> list:
        x, y = self.hidden_jump(self.far_step)
        far = np.array(self.order)[x + self.p * y]
        return [int(far[c]) for c in self.cells]


_PREPARED: dict = {}


def _prepare(game: "LayeredGame") -> dict:
    """Lo que se calcula una sola vez por juego: cuándo se repite la base y qué le hace una vuelta entera
    de la base a la capa de arriba (y -> block·y + shift)."""
    if game not in _PREPARED:
        kernel, base_step, push_of, p = game._parts()
        found = find_cycle(game.base_table(), np.array(game.start_x), 50_000_000)       # contando en C
        assert found is not None, "la base no se repite pronto"
        mu, lam = found
        x, y = np.array(game.start_x), np.array(game.start_y)
        for _ in range(mu):
            y = (kernel @ y + push_of(x)) % p
            x = base_step(x)
        shift, lap_x = np.zeros(game.n, dtype=np.int64), x
        for _ in range(lam):
            shift = (kernel @ shift + push_of(lap_x)) % p
            lap_x = base_step(lap_x)
        assert np.array_equal(lap_x, x), "la base no volvió al mismo estado"
        _PREPARED[game] = {"cycle": (mu, lam), "at_cycle_start": (x, y), "block": _mat_pow(kernel, lam, p), "shift": shift}
    return _PREPARED[game]


def _mat_pow(matrix: np.ndarray, power: int, p: int) -> np.ndarray:
    result = np.eye(matrix.shape[0], dtype=np.int64)
    while power:
        if power & 1:
            result = (result @ matrix) % p
        matrix = (matrix @ matrix) % p
        power >>= 1
    return result


def _affine_pow(matrix: np.ndarray, shift: np.ndarray, power: int, p: int):
    """Aplicar `power` veces  y -> matrix·y + shift.  Devuelve (M, C) del resultado."""
    n = matrix.shape[0]
    m_res, c_res = np.eye(n, dtype=np.int64), np.zeros(n, dtype=np.int64)
    while power:
        if power & 1:
            m_res, c_res = (matrix @ m_res) % p, (matrix @ c_res + shift) % p
        matrix, shift = (matrix @ matrix) % p, (matrix @ shift + shift) % p
        power >>= 1
    return m_res, c_res


def make_layered(game_id: str, p: int, n: int, seed: int, far_step: int = 10**18, n_cells: int = 6,
                 base_window: tuple = (2_000, 60_000)) -> LayeredGame:
    """Sortea las dos capas. Busca una base que se repita, pero no enseguida (entre miles y cientos de miles de pasos)."""
    rng = random.Random(seed)
    while True:
        base_seed = rng.randrange(10**9)
        start_x = tuple(rng.randrange(p) for _ in range(n))
        probe = LayeredGame(game_id, p, n, base_seed, (1, 1, 1), 0, tuple(range(p * p)), start_x, start_x, far_step, ())
        found = find_cycle(probe.base_table(), np.array(start_x), 5_000_000)
        if found and base_window[0] <= found[0] + found[1] <= base_window[1] and found[1] >= 100:
            break
    coeffs = (rng.randrange(1, p), rng.randrange(p), rng.randrange(1, p))
    order = list(range(p * p))
    rng.shuffle(order)
    start_y = tuple(rng.randrange(p) for _ in range(n))
    cells = tuple(sorted(rng.sample(range(n), n_cells)))
    return LayeredGame(game_id, p, n, base_seed, coeffs, rng.randrange(10**9), tuple(order), start_x, start_y, far_step, cells)
