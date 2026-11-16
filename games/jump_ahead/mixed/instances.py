"""Los juegos de la primera prueba con IAs: la misma idea escondida cada vez más.

Todos preguntan por el paso 10^18. El anillo tiene 27 casillas, salvo en mix-7 y mix-17, que tienen 23:
con 27 esos dos se repetían a los 40 y 24 millones de pasos, y una IA podía resolverlos contando.

    plain-5    el sistema conocido, a la vista (números y fórmula). Control: tiene que salir.
    mix-5      5 letras.            A ciegas sirve 1 orden de cada 6.
    mix-7      7 letras.            1 de cada 120.
    mix-8b     8 letras (3 bits).   1 de cada 30.
    mix-17     17 letras.           1 de cada 1.307.674.368.000.
    mix-25p    25 letras (pares).   1 de cada 1,3·10^21.
    twin-a/b/c 5 letras, tabla sorteada al azar: sin regla de resultado conocida (ver TWINS abajo).
    deep-9/25  dos capas escondidas en cada símbolo (ver layered.py).
"""
from __future__ import annotations

from dataclasses import replace

from .layered import make_layered
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


# Tablas sorteadas al azar: nadie las estudió y no esconden ningún sistema conocido. La respuesta lejana la
# sacamos contando en C hasta que la fila se repite. (comienzo del ciclo, largo del ciclo), medidos así:
TWINS = {
    "twin-a": dict(n=27, seed=5003, cycle=(2_219_180, 27), cells=(3, 6, 8, 15, 17, 24)),               # contando 2,3 millones de pasos se ve
    "twin-b": dict(n=27, seed=5002, cycle=(4_574_076, 80_926_938)),         # hacen falta 85 millones
    "twin-c": dict(n=31, seed=5001, cycle=(35_410_645, 10_799_066_256)),    # hacen falta 10.800 millones
}


def twin_game(game_id: str = "twin-c") -> TwinGame:
    spec = TWINS[game_id]
    cells = spec.get("cells", (1, 6, 10, 15, 19, 24))
    return TwinGame(game_id, 5, spec["n"], spec["seed"], FAR, cells)


def twin_games() -> list:
    return [twin_game(game_id) for game_id in TWINS]


def deep_games() -> list:
    """Dos capas escondidas en cada símbolo: una base sorteada que se repite, y arriba una suma con empujones."""
    return [make_layered("deep-9", 3, 29, seed=9001, far_step=FAR), make_layered("deep-25", 5, 27, seed=25001, far_step=FAR)]
