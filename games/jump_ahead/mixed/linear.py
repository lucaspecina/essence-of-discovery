"""Sistemas con regla de resultado conocida, y la mezcla que los esconde.

El sistema de fondo. Cada casilla guarda un vector de m números módulo p, o sea uno de q = p^m valores.
Regla de generación:

    nueva[i] = A·vieja[i-1] + B·vieja[i] + C·vieja[i+1]        (A, B, C: matrices m×m módulo p)

Como la regla es una suma, t pasos se pueden calcular con unas pocas multiplicaciones en vez de t pasos
(potencia por cuadrados). Esa es la regla de resultado, y es matemática publicada.

La mezcla. A cada uno de los q valores se le pone una letra, en un orden sorteado. La IA solo ve letras y
una tabla de q^3 renglones que dice qué letra sigue. Nosotros guardamos el orden sorteado: con él
calculamos la respuesta exacta.
"""
from __future__ import annotations

import itertools
import random
import string
from dataclasses import dataclass

import numpy as np

LETTERS = string.ascii_uppercase


# ---------- la suma de fondo y las matrices como tablas ----------
def digits(value: int, p: int, m: int) -> tuple:
    return tuple((value // p**k) % p for k in range(m))


def undigits(vec, p: int) -> int:
    return sum(int(d) * p**k for k, d in enumerate(vec))


def addition_table(p: int, m: int) -> np.ndarray:
    """add[x, y] = x + y, con x e y valores (vectores de m números módulo p escritos como un entero)."""
    q = p**m
    add = np.zeros((q, q), dtype=np.int64)
    for x in range(q):
        dx = digits(x, p, m)
        for y in range(q):
            dy = digits(y, p, m)
            add[x, y] = undigits([(a + b) % p for a, b in zip(dx, dy)], p)
    return add


def matrix_map(matrix, p: int, m: int) -> np.ndarray:
    """La matriz como tabla: out[x] = matrix·x."""
    q = p**m
    out = np.zeros(q, dtype=np.int64)
    for x in range(q):
        dx = digits(x, p, m)
        out[x] = undigits([sum(matrix[r][c] * dx[c] for c in range(m)) % p for r in range(m)], p)
    return out


def is_invertible(matrix, p: int, m: int) -> bool:
    return len(set(matrix_map(matrix, p, m).tolist())) == p**m


def random_matrix(rng: random.Random, p: int, m: int, invertible: bool):
    while True:
        matrix = [[rng.randrange(p) for _ in range(m)] for _ in range(m)]
        if any(any(row) for row in matrix) and (not invertible or is_invertible(matrix, p, m)):
            return matrix


# ---------- pasos y saltos, sobre cualquier suma dada como tabla ----------
def step_additive(state: np.ndarray, left, mid, right, add) -> np.ndarray:
    """Un paso de la regla de generación: nueva[i] = left[i-1] + mid[i] + right[i+1]."""
    return add[add[left[np.roll(state, 1)], mid[state]], right[np.roll(state, -1)]]


def kernel_of(left, mid, right, n: int, zero: int) -> np.ndarray:
    """La regla escrita como n tablas: kernel[j] es lo que aporta la casilla que está j lugares a la izquierda."""
    q = len(mid)
    kernel = np.full((n, q), zero, dtype=np.int64)
    kernel[1], kernel[0], kernel[n - 1] = left, mid, right
    return kernel


def kernel_mul(k1: np.ndarray, k2: np.ndarray, add: np.ndarray, zero: int) -> np.ndarray:
    """Aplicar k2 y después k1, como una sola regla."""
    n, q = k1.shape
    out = np.full((n, q), zero, dtype=np.int64)
    for i in range(n):
        out = add[out, np.roll(k1[i][k2], i, axis=0)]
    return out


def kernel_identity(n: int, q: int, zero: int) -> np.ndarray:
    kernel = np.full((n, q), zero, dtype=np.int64)
    kernel[0] = np.arange(q)
    return kernel


def kernel_power(kernel: np.ndarray, steps: int, add: np.ndarray, zero: int) -> np.ndarray:
    """La regla de `steps` pasos, con unas 2·log2(steps) multiplicaciones."""
    n, q = kernel.shape
    result = kernel_identity(n, q, zero)
    while steps:
        if steps & 1:
            result = kernel_mul(result, kernel, add, zero)
        kernel = kernel_mul(kernel, kernel, add, zero)
        steps >>= 1
    return result


def kernel_apply(kernel: np.ndarray, state: np.ndarray, add: np.ndarray, zero: int) -> np.ndarray:
    n = len(state)
    out = np.full(n, zero, dtype=np.int64)
    for j in range(n):
        out = add[out, kernel[j][np.roll(state, j)]]
    return out


def jump_additive(state, left, mid, right, add, zero: int, steps: int) -> np.ndarray:
    """Regla de resultado: el estado después de `steps` pasos, sin recorrerlos."""
    kernel = kernel_of(left, mid, right, len(state), zero)
    return kernel_apply(kernel_power(kernel, steps, add, zero), np.asarray(state), add, zero)


# ---------- un juego mezclado ----------
@dataclass(frozen=True)
class MixedGame:
    game_id: str
    p: int
    m: int
    n: int
    matrices: tuple          # (A, B, C) del sistema de fondo
    order: tuple             # order[valor de fondo] = número de letra. Es el secreto.
    hidden_start: tuple      # la fila del comienzo, en valores de fondo
    far_step: int
    cells: tuple             # casillas por las que se pregunta

    @property
    def q(self) -> int:
        return self.p**self.m

    @property
    def alphabet(self) -> str:
        return LETTERS[: self.q]

    # --- el sistema de fondo ---
    def hidden_parts(self):
        add = addition_table(self.p, self.m)
        left, mid, right = (matrix_map(mat, self.p, self.m) for mat in self.matrices)
        return add, left, mid, right

    def hidden_jump(self, steps: int) -> np.ndarray:
        add, left, mid, right = self.hidden_parts()
        return jump_additive(np.array(self.hidden_start), left, mid, right, add, 0, steps)

    # --- lo que ve la IA ---
    def visible_table(self) -> np.ndarray:
        """table[l, c, r] = letra nueva de una casilla cuya vecina izquierda es l, ella es c y la derecha es r."""
        add, left, mid, right = self.hidden_parts()
        order = np.array(self.order)
        back = np.argsort(order)                      # back[letra] = valor de fondo
        l, c, r = np.meshgrid(back, back, back, indexing="ij")
        return order[add[add[left[l], mid[c]], right[r]]]

    def visible_start(self) -> np.ndarray:
        return np.array(self.order)[np.array(self.hidden_start)]

    def truth(self) -> list:
        """La letra exacta de cada casilla preguntada, en el paso lejano."""
        far = np.array(self.order)[self.hidden_jump(self.far_step)]
        return [int(far[c]) for c in self.cells]


def step_table(state: np.ndarray, table: np.ndarray) -> np.ndarray:
    """Un paso usando solo la tabla que ve la IA."""
    return table[np.roll(state, 1), state, np.roll(state, -1)]


def is_affine_order(order, p: int, m: int) -> bool:
    """¿El orden sorteado respeta la suma de fondo? Si la respeta, la mezcla no esconde nada."""
    q = p**m
    add = addition_table(p, m)
    neg0 = [x for x in range(q) if add[x, order[0]] == 0][0]      # resta de order[0]
    g = [int(add[order[x], neg0]) for x in range(q)]                # g(x) = order(x) - order(0)
    return all(g[int(add[x, y])] == int(add[g[x], g[y]]) for x in range(q) for y in range(q))


def make_mixed(game_id: str, p: int, m: int, n: int, seed: int, far_step: int = 10**18, n_cells: int = 6) -> MixedGame:
    """Sortea un sistema de fondo, un comienzo y una mezcla. Todo sale de `seed`."""
    rng = random.Random(seed)
    q = p**m
    matrices = (random_matrix(rng, p, m, True), random_matrix(rng, p, m, False), random_matrix(rng, p, m, True))
    while True:
        order = list(range(q))
        rng.shuffle(order)
        if not is_affine_order(order, p, m):
            break
    hidden_start = tuple(rng.randrange(q) for _ in range(n))
    cells = tuple(sorted(rng.sample(range(n), n_cells)))
    return MixedGame(game_id, p, m, n, tuple(map(lambda mat: tuple(map(tuple, mat)), matrices)),
                     tuple(order), hidden_start, far_step, cells)


def naive_affine_test(table: np.ndarray, p: int, m: int) -> bool:
    """La prueba habitual: ¿la tabla, leyendo las letras en orden alfabético como números, es una suma?"""
    q = p**m
    add = addition_table(p, m)
    neg = np.zeros(q, dtype=np.int64)
    for x in range(q):
        neg[x] = [y for y in range(q) if add[x, y] == 0][0]
    g = add[table, neg[table[0, 0, 0]]]                             # g = f - f(0,0,0)
    idx = np.arange(q)
    for axis in range(3):                                           # aditiva en cada entrada, con las otras en 0
        line = g[idx, 0, 0] if axis == 0 else g[0, idx, 0] if axis == 1 else g[0, 0, idx]
        if not np.array_equal(line[add], add[line[:, None], line[None, :]]):
            return False
    l, c, r = np.meshgrid(idx, idx, idx, indexing="ij")
    return bool(np.array_equal(g, add[add[g[l, 0, 0], g[0, c, 0]], g[0, 0, r]]))


def count_revealing_orders(table: np.ndarray, p: int, m: int) -> tuple:
    """Fuerza bruta: de todos los órdenes posibles de las letras, cuántos dejan la tabla como una suma.

    Solo para alfabetos chicos (hasta 8 letras). Devuelve (los que sirven, el total).
    """
    q = p**m
    good = total = 0
    for perm in itertools.permutations(range(q)):
        total += 1
        relabel = np.array(perm)                                    # relabel[letra] = número
        back = np.argsort(relabel)
        l, c, r = np.meshgrid(back, back, back, indexing="ij")
        good += naive_affine_test(relabel[table[l, c, r]], p, m)
    return good, total
