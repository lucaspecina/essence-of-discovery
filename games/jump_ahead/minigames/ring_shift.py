"""Mini-juego 1: la luz que da vueltas.

Es el más fácil a propósito. Sirve para ver las piezas de un juego y como control:
si una IA falla acá, lo roto es nuestro programa, no la IA.
"""
from .base import MiniGame, Question, State

N = 7
FAR = 10**18


def step(state: State) -> State:
    """Regla de generación: cada casilla copia a su vecina de la izquierda."""
    return tuple(state[(i - 1) % len(state)] for i in range(len(state)))


def jump(state: State, steps: int) -> State:
    """Regla de resultado: la fila vuelve a ser la misma cada N pasos, así que solo importa el resto."""
    k = steps % len(state)
    return tuple(state[(i - k) % len(state)] for i in range(len(state)))


def ring_shift() -> MiniGame:
    start = (1, 0, 0, 0, 0, 0, 0)
    return MiniGame(
        game_id="ring-shift-7",
        kind="with-rule",
        rule_text="cada casilla pasa a valer lo que valía su vecina de la izquierda.",
        start=start,
        step=step,
        jump=jump,
        questions=[Question(FAR, c) for c in range(N)],
        result_rule_text="todo se repite cada 7 pasos; alcanza con el resto de dividir el paso por 7.",
    )
