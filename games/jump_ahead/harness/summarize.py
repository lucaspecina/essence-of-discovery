"""Resume las partidas guardadas en una carpeta: una línea por partida.

Uso:  python games/jump_ahead/harness/summarize.py experiments/2026-11-16-mixing-ladder/raw
"""
import json
import sys
from pathlib import Path

ORDER = ["plain-5", "mix-5", "mix-7", "mix-8b", "mix-17", "mix-25p", "twin-5"]


def main():
    records = [json.loads(p.read_text()) for p in sorted(Path(sys.argv[1]).glob("*.json"))]
    records.sort(key=lambda r: (r["model"], r["hint"], ORDER.index(r["game"]) if r["game"] in ORDER else 99))
    print(f"{'modelo':16s} {'juego':8s} {'pista':5s} {'puntaje':>7s} {'bien':>5s} {'corridas':>8s} {'cómputo':>8s} "
          f"{'llamadas':>8s} {'tok.sal':>8s} {'USD':>6s} {'tiempo':>7s}")
    total = 0.0
    for r in records:
        total += r.get("cost_usd", 0.0)
        if r.get("error"):
            print(f"{r['model']:16s} {r['game']:8s} ERROR {r['error'][:90]}")
            continue
        g = r["grade"]
        print(f"{r['model']:16s} {r['game']:8s} {'sí' if r['hint'] else 'no':5s} {g['score']:+7.2f} {g['right']:>3d}/{g['of']} "
              f"{r['code_runs']:>8d} {r['code_seconds']:>7.0f}s {r['usage']['calls']:>8d} {r['usage']['output']:>8d} "
              f"{r['cost_usd']:>6.2f} {r['wall_seconds']:>6.0f}s")
    print(f"gasto estimado total: {total:.2f} USD en {len(records)} partidas")


if __name__ == "__main__":
    main()
