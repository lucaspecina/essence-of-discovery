"""El puntaje. Es una cuenta contra la respuesta exacta; ninguna IA interviene.

Por cada casilla la IA dice un símbolo y cuán segura está (confidence, entre 0 y 1). Con K símbolos:

    acierta y está segura (1,0)        ->  +1
    dice "no sé" (confidence = 1/K)    ->   0
    se equivoca y estaba segura        ->  -(K+1)/(K-1)     (con 2 símbolos: -3; con 5: -1,5)

Es el mismo puntaje de los dos primeros juegos (1 - 4·(p - y)^2), extendido a más de dos símbolos.
"""
from __future__ import annotations


def score_cell(symbol: int, confidence: float, truth: int, k: int) -> float:
    c = min(1.0, max(0.0, float(confidence)))
    rest = (1.0 - c) / (k - 1)                       # lo que le queda a cada uno de los otros símbolos
    if symbol == truth:
        sq = (1.0 - c) ** 2 + (k - 1) * rest**2
    else:
        sq = c**2 + (1.0 - rest) ** 2 + (k - 2) * rest**2
    return 1.0 - k / (k - 1) * sq


def score_game(answers, truths, k: int) -> float:
    """answers: lista de (símbolo, confidence), una por casilla preguntada. Promedio de las casillas."""
    if len(answers) != len(truths) or not truths:
        raise ValueError("hace falta una respuesta por casilla")
    return sum(score_cell(s, c, y, k) for (s, c), y in zip(answers, truths)) / len(truths)
