"""Verifica los juegos de `outrun` SIN ninguna IA, antes de mostrárselos a un modelo.

Uso:
    python games/outrun/verify_worlds.py                       # las comprobaciones (un minuto)
    python games/outrun/verify_worlds.py <carpeta-experimento> # además, corrige los programas de referencia
                                                               # con el corrector de verdad y sus tandas

Comprueba:
  1. que la realidad rápida (C) da lo mismo que la regla corrida en Python;
  2. que los programas de referencia traen la misma regla que el mundo;
  3. que la receta general (`references/events.py`) y la ley (`references/law_pingpong.py`) dan
     exactamente lo mismo que la realidad en miles de comienzos sorteados;
  4. con la carpeta del experimento: qué puntaje saca cada programa de referencia. Eso fija las varas:
     el que corre todo (piso), la receta general, y la ley (el mejor resumen que conocemos).
"""
from __future__ import annotations

import importlib.util
import json
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import world  # noqa: E402
from evaluate import evaluate, print_summary  # noqa: E402
from games import GAMES, check_file, world_file  # noqa: E402
from shared.sandbox import Sandbox  # noqa: E402
from truth import run_fast, run_many  # noqa: E402

HERE = Path(__file__).resolve().parent
REFERENCES = {"collisions": ["brute", "events"], "pingpong": ["brute", "events", "law_pingpong"]}


def load(name: str):
    spec = importlib.util.spec_from_file_location(name, HERE / "references" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def check_fast_truth():
    rng, bad = random.Random(3), 0
    for _ in range(3000):
        cells, x = {}, rng.randint(-20, 20)
        for _ in range(rng.randint(1, 5)):
            kind = rng.choice(["ab", "ba", "a", "b", "c", "d", "e", "dd", "cd"])
            for i, ch in enumerate(kind):
                cells[x + i] = ch
            x += len(kind) + rng.randint(0, 9)
        steps = rng.randint(0, 200)
        bad += world.run(cells, steps) != run_fast(cells, steps)
    assert bad == 0, f"C y Python difieren en {bad} filas"
    print("[ok] la realidad en C == la regla en Python, 3.000 filas al azar de hasta 200 pasos")


def check_references():
    for name in ("brute", "events"):
        assert load(name).RULE == world.RULE, f"{name} trae otra regla"
    print("[ok] los programas de referencia traen la misma regla que el mundo")
    for game_id, names in (("collisions", ["events"]), ("pingpong", ["events", "law_pingpong"])):
        game, rng, jobs = GAMES[game_id], random.Random(11), []
        for _ in range(4000):
            start = game.sample(rng)
            steps = rng.choice([rng.randint(0, 60), rng.randint(0, 3000), rng.randint(0, 200_000), rng.randint(0, 3_000_000)])
            jobs.append((start, steps))
        truths = run_many(jobs)
        for name in names:
            program = load(name)
            wrong = sum(program.predict(dict(start), steps) != truth for (start, steps), truth in zip(jobs, truths))
            assert wrong == 0, f"{name} difiere de la realidad en {wrong} casos de {game_id}"
            print(f"[ok] {game_id}: `{name}` == la realidad en 4.000 comienzos sorteados (hasta 3 millones de pasos)")


def check_ai_files():
    """Lo que recibe la IA funciona dentro de su computadora encerrada."""
    for game_id, game in GAMES.items():
        sandbox = Sandbox({"world.py": world_file(game), "check.py": check_file(game),
                           "solution.py": (HERE / "references" / "brute.py").read_text()}, max_runs=1,
                          run_seconds=60, prefix="outrun-verify-")
        out = sandbox.run("import world, check\nprint(world.sample_start(1))\ncheck.compare(cases=40, max_steps=500)").output
        assert "40 de 40 iguales" in out, out
    print("[ok] `world.py` y `check.py` de la IA funcionan en su computadora, en los dos juegos")


def baselines(folder: Path):
    print("\nVaras (programas nuestros, corregidos con el corrector de verdad; cada columna es una distancia, de 10 a 10^9 pasos):")
    for game_id, names in REFERENCES.items():
        path = folder / f"cases_{game_id}.json"
        if not path.exists():
            print(f"  (faltan las tandas de {game_id})")
            continue
        eval_set = json.loads(path.read_text())
        for name in names:
            summary = evaluate((HERE / "references" / f"{name}.py").read_text(), eval_set)
            print_summary(f"  {game_id} / {name}", summary)


if __name__ == "__main__":
    check_fast_truth()
    check_references()
    check_ai_files()
    if len(sys.argv) > 1:
        baselines(Path(sys.argv[1]))
