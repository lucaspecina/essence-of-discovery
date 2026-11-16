"""El corrector: prueba un `solution.py` contra la realidad y mide tamaño y tiempo. Ninguna IA interviene.

Dos pasos:
1. `build_eval_set(game, path)`: sortea los casos de prueba y calcula la realidad de cada uno corriendo la
   regla paso por paso (en C). Se hace una vez, antes de mostrarle el juego a ningún modelo.
2. `evaluate(source, eval_set)`: corre el programa en la computadora encerrada (sin red, sin acceso a
   archivos nuestros), caso por caso y con reloj, y compara cada resultado con la realidad.

Uso para armar las tandas:  python games/outrun/evaluate.py build collisions <carpeta>
"""
from __future__ import annotations

import json
import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from games import GAMES, Game, case_kind, make_cases  # noqa: E402
from shared.sandbox import Sandbox  # noqa: E402
from truth import run_many  # noqa: E402

DRIVER = '''
import json, signal, time
spec = json.load(open("cases.json"))
LIMIT = spec["limit_seconds"]

class TimeUp(Exception):
    pass

def _alarm(signum, frame):
    raise TimeUp()

signal.signal(signal.SIGALRM, _alarm)
try:
    import solution
    predict, import_error = solution.predict, None
except BaseException as exc:
    predict, import_error = None, repr(exc)[:300]

with open("results.jsonl", "w") as out:
    for case in spec["cases"]:
        record = {"id": case["id"]}
        if predict is None:
            record["error"] = "no se pudo cargar: " + import_error
        else:
            start = {int(p): s for p, s in case["start"].items()}
            t0 = time.perf_counter()
            signal.setitimer(signal.ITIMER_REAL, LIMIT * 1.5)        # corte un poco después del tope
            try:
                answer = predict(start, case["steps"])
                record["seconds"] = time.perf_counter() - t0
                signal.setitimer(signal.ITIMER_REAL, 0)
                record["answer"] = {str(int(p)): str(s) for p, s in dict(answer).items() if str(s) != "."}
            except TimeUp:
                record["seconds"], record["error"] = time.perf_counter() - t0, "tiempo"
            except BaseException as exc:
                record["seconds"], record["error"] = time.perf_counter() - t0, repr(exc)[:200]
            finally:
                signal.setitimer(signal.ITIMER_REAL, 0)
        out.write(json.dumps(record) + "\\n")
        out.flush()
print("fin")
'''


def build_eval_set(game: Game, path: Path, workers: int = 8) -> dict:
    cases = make_cases(game)
    truths = run_many([(c["start"], c["steps"]) for c in cases], workers=workers)
    for case, truth in zip(cases, truths):
        case["start"] = {str(p): s for p, s in sorted(case["start"].items())}
        case["truth"] = {str(p): s for p, s in sorted(truth.items())}
    eval_set = {"game": game.game_id, "limit_seconds": game.limit_seconds, "size_limit": game.size_limit,
                "scales": list(game.scales), "cases": cases}
    path.write_text(json.dumps(eval_set, indent=0), encoding="utf-8")
    return eval_set


def evaluate(source: str, eval_set: dict) -> dict:
    """Devuelve el resumen (por distancia) y el detalle de cada caso."""
    limit, cases = eval_set["limit_seconds"], eval_set["cases"]
    visible = {"limit_seconds": limit,
               "cases": [{"id": c["id"], "start": c["start"], "steps": c["steps"]} for c in cases]}   # sin la realidad
    sandbox = Sandbox({"solution.py": source, "cases.json": json.dumps(visible)}, max_runs=1,
                      run_seconds=len(cases) * limit * 1.5 + 120, prefix="outrun-eval-")
    run = sandbox.run(DRIVER)
    records = {}
    results = sandbox.workdir / "results.jsonl"
    if results.exists():
        for line in results.read_text().splitlines():
            try:
                record = json.loads(line)
                records[record["id"]] = record
            except json.JSONDecodeError:
                pass
    detail = []
    for case in cases:
        record = records.get(case["id"], {"error": "no se llegó a probar"})
        seconds = record.get("seconds")
        if "error" in record:
            reason = "tiempo" if record["error"] == "tiempo" else "error"
        elif record.get("answer") != case["truth"]:
            reason = "distinto"
        elif seconds is not None and seconds > limit:
            reason = "tiempo"
        else:
            reason = "bien"
        detail.append({"id": case["id"], "scale": case["scale"], "steps": case["steps"], "result": reason,
                       "kind": case_kind(eval_set["game"], case["start"]),
                       "seconds": None if seconds is None else round(seconds, 5),
                       "error": record.get("error") if reason == "error" else None})
    size = len(source.encode("utf-8"))
    by_scale = []
    for k in eval_set["scales"]:
        rows = [d for d in detail if d["scale"] == k]
        times = [d["seconds"] for d in rows if d["seconds"] is not None]
        by_scale.append({"scale": k, "of": len(rows), "ok": sum(d["result"] == "bien" for d in rows),
                         "wrong": sum(d["result"] == "distinto" for d in rows),
                         "slow": sum(d["result"] == "tiempo" for d in rows),
                         "error": sum(d["result"] == "error" for d in rows),
                         "median_seconds": round(statistics.median(times), 5) if times else None})
    horizon = 0
    for row in by_scale:
        if row["ok"] != row["of"]:
            break
        horizon = row["scale"]
    horizon_normal = 0                                                  # lo mismo, mirando solo los casos "normal"
    for k in eval_set["scales"]:
        rows = [d for d in detail if d["scale"] == k and d["kind"] == "normal"]
        if any(d["result"] != "bien" for d in rows):
            break
        horizon_normal = k
    by_kind = {}
    for d in detail:
        entry = by_kind.setdefault(d["kind"], {"ok": 0, "of": 0})
        entry["of"] += 1
        entry["ok"] += d["result"] == "bien"
    size_ok = size <= eval_set["size_limit"]
    return {"size_bytes": size, "size_ok": size_ok,
            "horizon": horizon if size_ok else 0,                       # hasta qué distancia acierta todo
            "horizon_normal": horizon_normal if size_ok else 0,
            "ok": sum(r["ok"] for r in by_scale), "of": len(detail),
            "by_scale": by_scale, "by_kind": by_kind, "detail": detail,
            "driver_output": run.output[-300:], "driver_timed_out": run.timed_out}


def print_summary(name: str, summary: dict) -> None:
    cells = " ".join(f"{r['ok']}/{r['of']}" for r in summary["by_scale"])
    kinds = "  ".join(f"{k} {v['ok']}/{v['of']}" for k, v in summary["by_kind"].items()) if len(summary["by_kind"]) > 1 else ""
    print(f"{name:28s} {summary['size_bytes']:>6} bytes  horizonte 10^{summary['horizon']} (normales: 10^{summary['horizon_normal']})  "
          f"bien {summary['ok']}/{summary['of']}  por distancia: {cells}  {kinds}")


if __name__ == "__main__":
    if len(sys.argv) == 4 and sys.argv[1] == "build":
        game, folder = GAMES[sys.argv[2]], Path(sys.argv[3])
        folder.mkdir(parents=True, exist_ok=True)
        built = build_eval_set(game, folder / f"cases_{game.game_id}.json")
        print(f"{game.game_id}: {len(built['cases'])} casos con su realidad en {folder}")
    else:
        print(__doc__)
