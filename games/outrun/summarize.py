"""Resume las partidas de un experimento de `outrun`: una línea por partida.

Uso:  python games/outrun/summarize.py experiments/2026-11-16-outrun-first-two-games
"""
import json
import sys
from pathlib import Path


def main():
    raw = Path(sys.argv[1]) / "raw"
    rows = [json.loads(p.read_text()) for p in sorted(raw.glob("*.json"))]
    rows.sort(key=lambda r: (r["game"], r["model"], r["hint"], r["started"]))
    total = 0.0
    for r in rows:
        total += r["cost_usd"]
        head = f"{r['game']:11s} {r['model']:14s} {'con pista' if r['hint'] else 'sin pista':9s} {r['tag']:4s}"
        ev = r["evaluation"]
        if ev is None:
            print(f"{head} NO ENTREGÓ  ({r['error'] or 'sin solution.py'})")
            continue
        cells = " ".join(f"{s['ok']}/{s['of']}" for s in ev["by_scale"])
        kinds = "  ".join(f"{k} {v['ok']}/{v['of']}" for k, v in ev["by_kind"].items()) if len(ev["by_kind"]) > 1 else ""
        print(f"{head} horizonte 10^{ev['horizon']} (normales 10^{ev['horizon_normal']})  bien {ev['ok']}/{ev['of']}  "
              f"{ev['size_bytes']} bytes  | {cells} | {kinds}")
        print(f"{'':42s}ejecuciones {r['code_runs']}, {r['usage']['calls']} turnos, {r['wall_seconds'] / 60:.1f} min, "
              f"~{r['cost_usd']:.2f} USD")
    print(f"gasto estimado: {total:.2f} USD en {len(rows)} partidas")


if __name__ == "__main__":
    main()
