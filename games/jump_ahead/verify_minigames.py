"""Verifica los mini-juegos SIN ninguna IA: la regla de resultado contra la cuenta larga.

Uso:  python games/jump_ahead/verify_minigames.py
"""
import time

from minigames import ALL, brief, picture, score
from minigames.xor_ring import far_step, step as xor_step


def check_game(game, compare_until):
    """La regla de resultado tiene que dar lo mismo que la cuenta larga, paso por paso."""
    state = game.start
    for t in range(compare_until + 1):
        assert game.jump(game.start, t) == state, f"{game.game_id}: difieren en el paso {t}"
        state = game.step(state)
    return compare_until


def find_repeat(game, limit):
    """Busca a fuerza bruta cuándo la fila vuelve a ser igual a una anterior. None si no pasa en `limit`."""
    seen = {game.start: 0}
    state = game.start
    for t in range(1, limit + 1):
        state = game.step(state)
        if state in seen:
            return seen[state], t
        seen[state] = t
    return None


def main():
    for game in ALL:
        print("=" * 78)
        print(f"MINI-JUEGO {game.game_id}   ({game.kind})")
        print("-" * 78)
        print("Lo que recibe la IA:\n")
        print(brief(game))
        print("\nLo que la IA NO recibe (la regla de resultado):")
        print("  " + game.result_rule_text)

        n = check_game(game, 3000)
        print(f"\n[ok] la regla de resultado coincide con la cuenta larga en los pasos 0 a {n}")

        rep = find_repeat(game, 200_000)
        if rep:
            print(f"[dato] contando paso por paso, la fila se repite: el paso {rep[1]} es igual al {rep[0]}")
        else:
            print("[dato] contando 200.000 pasos, la fila no se repite nunca: no alcanza con esperar")

        t0 = time.perf_counter()
        truths = [game.truth(q) for q in game.questions]
        ms = (time.perf_counter() - t0) * 1000
        print(f"[ok] respuestas exactas para el paso {game.questions[0].step:,} en {ms:.2f} ms:".replace(",", "."))
        for q, y in zip(game.questions, truths):
            print(f"       casilla {q.cell:>3}: {'prendida' if y else 'apagada'}")

        sure_right = score([float(y) for y in truths], truths)
        dont_know = score([0.5] * len(truths), truths)
        sure_wrong = score([1.0 - y for y in truths], truths)
        print(f"[puntaje] segura y bien: {sure_right:+.0f} | 'no sé' en todo: {dont_know:+.0f} | "
              f"segura y mal: {sure_wrong:+.0f}")

    # La idea del juego 2, comprobada directamente: 2, 4, 8... pasos = mirar a esa distancia.
    game = ALL[1]
    state, t = game.start, 0
    for distance in (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024):
        while t < distance:
            state, t = xor_step(state), t + 1
        assert state == far_step(game.start, distance), distance
    print("=" * 78)
    print("[ok] juego 2: dar 2, 4, 8 ... 1024 pasos es igual a aplicar la regla UNA vez mirando a esa distancia")

    print("\nPrimeros pasos del juego 1:")
    state = ALL[0].start
    for t in range(9):
        print(f"  paso {t}:  {picture(state)}")
        state = ALL[0].step(state)


if __name__ == "__main__":
    main()
