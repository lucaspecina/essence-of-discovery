"""Piezas comunes de los mini-juegos.

Un mini-juego es: una fila de casillas (0 = apagada, 1 = prendida) cerrada en anillo,
una regla de generación que dice cómo cambia en un paso, y preguntas sobre pasos lejanos.
Todas las preguntas tienen la misma forma: "¿la casilla C está prendida en el paso T?".
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Optional, Sequence, Tuple

State = Tuple[int, ...]


@dataclass(frozen=True)
class Question:
    step: int  # el paso por el que se pregunta
    cell: int  # la casilla


@dataclass(frozen=True)
class MiniGame:
    game_id: str
    kind: str                # "with-rule" (hay regla de resultado) | "no-rule" | "trap"
    rule_text: str           # la regla de generación, en palabras: es lo que ve la IA
    start: State             # cómo arranca la fila
    step: Callable[[State], State]                    # regla de generación: un paso
    jump: Optional[Callable[[State, int], State]]     # regla de resultado; None si no se conoce
    questions: Sequence[Question]
    result_rule_text: str = ""   # la regla de resultado, en palabras. NUNCA se le muestra a la IA.

    def simulate(self, steps: int) -> State:
        """La cuenta larga: aplica la regla de generación paso por paso."""
        state = self.start
        for _ in range(steps):
            state = self.step(state)
        return state

    def truth(self, question: Question) -> int:
        """La respuesta exacta, calculada con la regla de resultado."""
        if self.jump is None:
            raise ValueError(f"{self.game_id}: no se conoce una regla de resultado")
        return self.jump(self.start, question.step)[question.cell]


def picture(state: State) -> str:
    """Dibuja una fila: ■ prendida, □ apagada."""
    return " ".join("■" if c else "□" for c in state)


def brief(game: MiniGame) -> str:
    """El texto que recibiría la IA. No incluye la regla de resultado."""
    lines = [
        f"Sistema: una fila de {len(game.start)} casillas en anillo (la última es vecina de la primera).",
        "Las casillas se numeran desde 0. Cada una está prendida (1) o apagada (0).",
        "",
        "Regla (se aplica a todas las casillas a la vez, una vez por paso):",
        f"  {game.rule_text}",
        "",
        "Paso 0:",
        "  " + "".join(str(c) for c in game.start),
        "",
        "Preguntas. Para cada una, contestá con la probabilidad de que la casilla esté prendida:",
    ]
    lines += [f"  - casilla {q.cell} en el paso {q.step}" for q in game.questions]
    return "\n".join(lines)


def score(probabilities: Sequence[float], truths: Sequence[int]) -> float:
    """El puntaje de una partida.

    1  = todo bien y segura.
    0  = contestó 0,5 en todo ("no sé").
    <0 = segura y equivocada (lo peor es -3).
    """
    if len(probabilities) != len(truths) or not truths:
        raise ValueError("hace falta una probabilidad por pregunta")
    return sum(1 - 4 * (p - y) ** 2 for p, y in zip(probabilities, truths)) / len(truths)
