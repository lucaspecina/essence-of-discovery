"""La computadora de la IA se mudó a `games/shared/sandbox.py`, porque la usan los dos juegos."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from shared.sandbox import RunResult, Sandbox  # noqa: E402,F401
