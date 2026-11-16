"""Los juegos de la primera prueba con IAs: la misma idea escondida cada vez más.

Todos preguntan por el paso 10^18. El anillo tiene 27 casillas, salvo en mix-7 y mix-17, que tienen 23:
con 27 esos dos se repetían a los 40 y 24 millones de pasos, y una IA podía resolverlos contando.

    plain-5    el sistema conocido, a la vista (números y fórmula). Control: tiene que salir.
    mix-5      5 letras.            A ciegas sirve 1 orden de cada 6.
    mix-7      7 letras.            1 de cada 120.
    mix-8b     8 letras (3 bits).   1 de cada 30.
    mix-17     17 letras.           1 de cada 1.307.674.368.000.
    mix-25p    25 letras (pares).   1 de cada 1,3·10^21.
    twin-5     5 letras, tabla sorteada al azar: sin regla de resultado conocida. Control: "no sé".
"""
from __future__ import annotations

from dataclasses import replace

from .linear import MixedGame, make_mixed
from .twin import TwinGame

N = 27
FAR = 10**18


def plain_game() -> MixedGame:
    game = make_mixed("plain-5", 5, 1, N, seed=500, far_step=FAR)
    return replace(game, order=tuple(range(5)))            # sin mezclar: cada valor se muestra como es


def mixed_games() -> list:
    return [
        make_mixed("mix-5", 5, 1, N, seed=501, far_step=FAR),
        make_mixed("mix-7", 7, 1, 23, seed=701, far_step=FAR),
        make_mixed("mix-8b", 2, 3, N, seed=801, far_step=FAR),
        make_mixed("mix-17", 17, 1, 23, seed=1701, far_step=FAR),
        make_mixed("mix-25p", 5, 2, N, seed=2501, far_step=FAR),
    ]


def twin_game(seed: int = 5001) -> TwinGame:
    return TwinGame("twin-5", 5, N, seed, FAR, (1, 6, 10, 15, 19, 24))
