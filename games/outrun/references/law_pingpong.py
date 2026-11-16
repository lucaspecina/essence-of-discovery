"""Programa de referencia 3, solo para el juego `pingpong`: la ley del mundo, en cuentas.

Lo que hay que saber del mundo para escribirlo:
- La pared izquierda no se mueve nunca.
- La cosa de adentro va y viene. Hacia la derecha es una letra que alterna a, b, a, b...; hacia la
  izquierda es una c. Avanza una casilla por paso.
- Cuando la letra queda pegada a la pared derecha, al paso siguiente la letra pasa a ser c y la pared
  pasa a ser e; un paso después la c ya retrocedió y la pared reaparece como d una casilla más a la derecha.
- Cuando la c queda pegada a la pared izquierda, al paso siguiente es una a en esa misma casilla.
- Entonces, con la pared derecha a distancia R, una vuelta completa (de "a pegada a la izquierda" a "a
  pegada a la izquierda") dura 2R - 2 pasos, y la siguiente dura dos pasos más. Sumando: n vueltas duran
  n*n + n*(2R - 3) pasos. Dar vuelta esa cuenta pide una raíz cuadrada.
- Dos excepciones, que aparecieron al comparar contra la regla (no las dibujamos a propósito):
  si arranca una "b" pegada a la pared izquierda, esa pared desaparece en el primer paso; la letra sigue,
  rebota una vez a la derecha y la c que vuelve se va para siempre. Y si arranca una "c" pegada a la pared
  derecha, desaparece esa pared; la c rebota a la izquierda y la letra se va para siempre.
"""
from math import isqrt


def predict(start, steps):
    if steps == 0:
        return dict(start)
    left = min(start)
    wall = max(start) - left                      # distancia a la pared derecha
    (pos, mover), = [(p - left, s) for p, s in start.items() if s != "d"]
    if mover == "b" and pos == 1:                 # excepción 1: se pierde la pared izquierda
        cells = {}
        if steps <= wall - 2:
            cells[left + 1 + steps] = "b" if steps % 2 == 0 else "a"
            cells[left + wall] = "d"
        elif steps == wall - 1:
            cells[left + wall - 1] = "c"
            cells[left + wall] = "e"
        else:
            cells[left + wall - 1 - (steps - (wall - 1))] = "c"
            cells[left + wall + 1] = "d"
        return cells
    if mover == "c" and pos == wall - 1:          # excepción 2: se pierde la pared derecha
        cells = {left: "d"}
        if steps <= wall - 2:
            cells[left + wall - 1 - steps] = "c"
        else:
            after = steps - (wall - 1)
            cells[left + 1 + after] = "a" if after % 2 == 0 else "b"
        return cells
    if mover == "c":                              # ya rebotó: es la vuelta que empezó con la pared en wall-1
        wall -= 1
        time_in_lap, flipped = 2 * wall - 2 - pos, False
    else:                                         # va hacia la derecha; "a" toca en las casillas impares
        time_in_lap = pos - 1
        flipped = (mover == "a") != (time_in_lap % 2 == 0)
    t = time_in_lap + steps
    # cuántas vueltas enteras entran en t: el mayor n con n*n + n*(2*wall - 3) <= t
    b = 2 * wall - 3
    n = (isqrt(b * b + 4 * t) - b) // 2
    while n * n + n * b > t:
        n -= 1
    while (n + 1) * (n + 1) + (n + 1) * b <= t:
        n += 1
    t -= n * n + n * b
    wall += n
    if n > 0:
        flipped = False
    cells = {left: "d"}
    if t <= wall - 2:                             # yendo hacia la derecha
        letter = "a" if t % 2 == 0 else "b"
        if flipped:
            letter = "b" if letter == "a" else "a"
        cells[left + 1 + t] = letter
        cells[left + wall] = "d"
    elif t == wall - 1:                           # el instante del rebote
        cells[left + wall - 1] = "c"
        cells[left + wall] = "e"
    else:                                         # volviendo
        cells[left + 2 * wall - 2 - t] = "c"
        cells[left + wall + 1] = "d"
    return cells
