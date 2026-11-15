"""Mini-juego 2: las vecinas distintas.

La regla de generación es igual de corta que la del juego 1, pero el dibujo que sale parece
desordenado. La regla de resultado no se ve a simple vista:

    después de 1 paso, cada casilla depende de sus vecinas a distancia 1;
    después de 2 pasos, de las casillas a distancia 2;
    después de 4, de las de distancia 4; después de 8, de las de distancia 8; y así.

Con eso se puede saltar de a 1, 2, 4, 8, 16... pasos, y llegar a cualquier paso lejano en pocos saltos.
"""
from .base import MiniGame, Question, State

N = 101
FAR = 10**18


def step(state: State) -> State:
    """Regla de generación: una casilla queda prendida si sus dos vecinas eran distintas entre sí."""
    n = len(state)
    return tuple(state[(i - 1) % n] ^ state[(i + 1) % n] for i in range(n))


def far_step(state: State, distance: int) -> State:
    """Un salto de `distance` pasos de una, válido cuando `distance` es 1, 2, 4, 8, 16...

    Es la misma regla de siempre, pero mirando a las casillas que están a esa distancia.
    """
    n = len(state)
    return tuple(state[(i - distance) % n] ^ state[(i + distance) % n] for i in range(n))


def jump(state: State, steps: int) -> State:
    """Regla de resultado: descompone el paso en saltos de 1, 2, 4, 8... y los aplica."""
    distance = 1
    while steps:
        if steps & 1:
            state = far_step(state, distance)
        steps >>= 1
        distance *= 2
    return state


def xor_ring() -> MiniGame:
    lit = {3, 4, 17, 40, 41, 42, 77, 90}
    start = tuple(1 if i in lit else 0 for i in range(N))
    cells = [0, 5, 13, 29, 50, 64, 88, 100]
    return MiniGame(
        game_id="xor-ring-101",
        kind="with-rule",
        rule_text="una casilla queda prendida si sus dos vecinas (izquierda y derecha) eran distintas "
                  "entre sí; si eran iguales, queda apagada.",
        start=start,
        step=step,
        jump=jump,
        questions=[Question(FAR, c) for c in cells],
        result_rule_text="después de 2^k pasos, cada casilla depende solo de las dos casillas a distancia "
                         "2^k; cualquier paso lejano se arma con pocos de esos saltos.",
    )
