"""Dos resolvedores sin IA, para saber qué se le pide a la IA y contra qué compararla.

- `solve_by_structure`: mira solo la tabla que ve la IA y, si hay una suma escondida, la reconstruye y
  salta al paso lejano. Cuesta milisegundos. Prueba que el juego se puede resolver con lo que ve la IA.
- `blind_search_rate`: el rival a ciegas. Prueba órdenes de las letras uno por uno hasta que la tabla
  queda como una suma. Mide cuántos órdenes por segundo prueba, para saber hasta dónde llega.
"""
from __future__ import annotations

import time

import numpy as np

from .linear import addition_table, jump_additive


def recover_hidden_sum(table: np.ndarray):
    """Busca una suma escondida en la tabla. Devuelve (zero, add, left, mid, right) o None.

    La idea: si la tabla es left(l) + mid(c) + right(r) para alguna suma, y `zero` es su elemento neutro,
    entonces table[l, zero, r] = left(l) + right(r). De ahí se despeja la suma entera.
    """
    q = table.shape[0]
    idx = np.arange(q)
    for zero in range(q):
        if table[zero, zero, zero] != zero:
            continue
        left, mid, right = table[:, zero, zero], table[zero, :, zero], table[zero, zero, :]
        if len(set(left.tolist())) != q or len(set(right.tolist())) != q:
            continue
        left_inv, right_inv = np.argsort(left), np.argsort(right)
        add = table[left_inv[:, None], zero, right_inv[None, :]]         # add[x, y] = x + y
        if not (np.array_equal(add[zero], idx) and np.array_equal(add[:, zero], idx)):
            continue
        if not np.array_equal(add, add.T):
            continue
        if not np.array_equal(add[add[:, :, None], idx[None, None, :]], add[idx[:, None, None], add[None, :, :]]):
            continue                                                       # asociativa
        if not all(np.array_equal(f[add], add[f[:, None], f[None, :]]) for f in (left, mid, right)):
            continue                                                       # las tres partes respetan la suma
        l, c, r = np.meshgrid(idx, idx, idx, indexing="ij")
        if not np.array_equal(table, add[add[left[l], mid[c]], right[r]]):
            continue
        return zero, add, left, mid, right
    return None


def solve_by_structure(table: np.ndarray, start: np.ndarray, far_step: int):
    """La fila en el paso lejano, usando solo lo que ve la IA. None si no encuentra una suma escondida."""
    found = recover_hidden_sum(table)
    if found is None:
        return None
    zero, add, left, mid, right = found
    return jump_additive(start, left, mid, right, add, zero, far_step)


def blind_search_rate(table: np.ndarray, p: int, m: int, seconds: float = 2.0, batch: int = 20000, seed: int = 0):
    """Cuántos órdenes de letras por segundo prueba un buscador a ciegas bien hecho.

    Para cada orden sorteado comprueba primero unas pocas igualdades baratas; casi todos los órdenes
    equivocados caen ahí. Devuelve (órdenes por segundo, cuántos pasaron el filtro barato).
    """
    q = p**m
    add = addition_table(p, m)
    rng = np.random.default_rng(seed)
    probes = rng.integers(0, q, size=(6, 6))                               # seis igualdades de prueba
    tried = passed = 0
    t0 = time.perf_counter()
    while time.perf_counter() - t0 < seconds:
        relabel = np.argsort(rng.random((batch, q)), axis=1)               # relabel[k, letra] = número
        back = np.argsort(relabel, axis=1)                                 # back[k, número] = letra
        rows = np.arange(batch)

        def f(a, b, c):                                                    # la tabla, releída con cada orden
            return relabel[rows, table[back[rows, a], back[rows, b], back[rows, c]]]

        f0 = f(0, 0, 0)
        ok = np.ones(batch, dtype=bool)
        for a1, b1, c1, a2, b2, c2 in probes:
            lhs = add[f(add[a1, a2], add[b1, b2], add[c1, c2]), f0]
            rhs = add[f(a1, b1, c1), f(a2, b2, c2)]
            ok &= lhs == rhs                                               # f(x+y) + f(0) == f(x) + f(y)
        tried += batch
        passed += int(ok.sum())
    return tried / (time.perf_counter() - t0), passed
