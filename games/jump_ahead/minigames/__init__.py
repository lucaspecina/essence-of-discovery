"""Mini-juegos de jump-ahead. Cada uno tiene una regla de generación (a la vista) y,
si se conoce, una regla de resultado (lo que hay que encontrar)."""
from .base import MiniGame, Question, brief, picture, score
from .ring_shift import ring_shift
from .xor_ring import xor_ring

ALL = [ring_shift(), xor_ring()]

__all__ = ["MiniGame", "Question", "brief", "picture", "score", "ring_shift", "xor_ring", "ALL"]
