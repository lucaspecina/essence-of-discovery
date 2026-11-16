"""Verifica los juegos mezclados SIN ninguna IA, antes de mostrárselos a un modelo.

Uso:
    python games/jump_ahead/verify_mixed.py            # lo rápido (un minuto)
    python games/jump_ahead/verify_mixed.py --long     # además, las cuentas largas en C (varios minutos)

Para cada juego mezclado comprueba:
  1. que la tabla que ve la IA, aplicada paso por paso, da lo mismo que nuestro salto (pasos 0 a 3.000);
  2. que la prueba habitual ("¿esto es una suma?") NO reconoce la tabla tal como se la damos;
  3. que el juego se puede resolver con lo que ve la IA: un programa nuestro reconstruye la suma escondida
     a partir de la tabla y llega a la respuesta exacta;
  4. cuántos órdenes de letras destapan el sistema (contados uno por uno si son pocos) y cuántos por
     segundo prueba un buscador a ciegas;
  5. (--long) que la fila no se repite en 2.000 millones de pasos: contar no alcanza.
Para el juego de control sin regla: que nuestro programa NO encuentra ninguna suma escondida y,
con --long, dónde se repite la fila contando en C.
"""
import math
import sys
import time

import numpy as np

from mixed.instances import mixed_games, plain_game, twin_game
from mixed.linear import count_revealing_orders, naive_affine_test, step_table
from mixed.solver import blind_search_rate, solve_by_structure
from mixed.twin import far_state_from_cycle, find_cycle

AI_SECONDS = 12 * 30          # el tope de cómputo que va a tener la IA: 12 ejecuciones de 30 segundos


def affine_group_size(p: int, m: int) -> int:
    """Cuántos órdenes de letras respetan la suma de fondo (son los que destapan el sistema)."""
    gl = math.prod(p**m - p**k for k in range(m))
    return p**m * gl


def check_mixed(game, long_run: bool):
    table, start, order = game.visible_table(), game.visible_start(), np.array(game.order)
    q = game.q
    print("=" * 96)
    print(f"{game.game_id}: {q} símbolos, {game.n} casillas, tabla de {q**3} renglones, paso {game.far_step:.0e}")

    row = start.copy()
    for t in range(3001):
        assert np.array_equal(row, order[game.hidden_jump(t)]), f"difieren en el paso {t}"
        row = step_table(row, table)
    print(f"  [ok] la tabla paso por paso == nuestro salto, pasos 0 a 3.000 "
          f"(en el paso 3.000 hay {len(set(row.tolist()))} símbolos distintos en la fila)")

    plain = bool(np.array_equal(order, np.arange(q)))
    seen = naive_affine_test(table, game.p, game.m)
    assert seen == plain, "la prueba habitual tendría que reconocer solo el juego sin mezclar"
    print(f"  [ok] la prueba habitual {'reconoce' if seen else 'NO reconoce'} la tabla tal como se muestra")

    t0 = time.perf_counter()
    far = solve_by_structure(table, start, game.far_step)
    ms = (time.perf_counter() - t0) * 1000
    truth = game.truth()
    assert far is not None and [int(far[c]) for c in game.cells] == truth
    print(f"  [ok] resoluble con lo que ve la IA: nuestro programa reconstruye la suma escondida y acierta "
          f"las {len(truth)} casillas en {ms:.0f} ms")

    total = math.factorial(q)
    good = affine_group_size(game.p, game.m)
    if q <= 8 and not plain:
        counted = count_revealing_orders(table, game.p, game.m)
        assert counted == (good, total), counted
        how = "contados uno por uno"
    else:
        how = "por fórmula"
    rate, _ = blind_search_rate(table, game.p, game.m, seconds=1.5)
    expected = total / good
    secs = expected / rate
    print(f"  [dato] órdenes de letras que destapan el sistema: {good:,} de {total:,} ({how}); "
          f"a ciegas, 1 de cada {expected:,.0f}".replace(",", "."))
    print(f"  [dato] buscador a ciegas: {rate:,.0f} órdenes por segundo -> en promedio {secs:,.1f} s para dar "
          f"con uno; la IA tiene {AI_SECONDS} s -> {'LE ALCANZA' if secs < AI_SECONDS else 'NO le alcanza'}"
          .replace(",", "."))

    if long_run:
        limit = 2_000_000_000
        t0 = time.perf_counter()
        cyc = find_cycle(table, start, limit)
        took = time.perf_counter() - t0
        assert cyc is None, f"la fila se repite: {cyc}"
        print(f"  [ok] contando en C, la fila no se repite en {limit:,} pasos ({took:.0f} s)".replace(",", "."))
    return truth


def check_twin(game, long_run: bool, cycle=None):
    table, start = game.visible_table(), game.visible_start()
    print("=" * 96)
    print(f"{game.game_id}: {game.q} símbolos, {game.n} casillas, tabla sorteada al azar (semilla {game.seed})")
    assert solve_by_structure(table, start, game.far_step) is None
    print("  [ok] nuestro programa NO encuentra ninguna suma escondida en esta tabla")
    assert not naive_affine_test(table, game.q, 1)
    row = start.copy()
    for _ in range(3000):
        row = step_table(row, table)
    print(f"  [dato] en el paso 3.000 hay {len(set(row.tolist()))} símbolos distintos en la fila (no se apaga)")
    if long_run:
        t0 = time.perf_counter()
        cyc = find_cycle(table, start, 40_000_000_000)
        print(f"  [dato] contando en C ({time.perf_counter() - t0:.0f} s): "
              + (f"la fila entra en un ciclo en el paso {cyc[0]:,} y el ciclo mide {cyc[1]:,} pasos".replace(",", ".")
                 if cyc else "no se repite en 40.000 millones de pasos"))
        if cyc:
            far = far_state_from_cycle(table, start, game.far_step, *cyc)
            print("  [dato] respuestas del paso lejano:", [game.alphabet[int(far[c])] for c in game.cells])
        return cyc
    return None


def main():
    long_run = "--long" in sys.argv
    for game in [plain_game()] + mixed_games():
        truth = check_mixed(game, long_run)
        print("  respuestas exactas:", [game.alphabet[s] if game.game_id != "plain-5" else str(s) for s in truth],
              "en las casillas", list(game.cells))
    check_twin(twin_game(), long_run)


if __name__ == "__main__":
    main()
