# Primeros dos juegos de `outrun`: reglas de lectura

**Escritas y subidas antes de correr ningún modelo.** Lo que diga el resultado se lee con esto.

## Qué se prueba

La idea: la IA entrega un programa que predice el mundo, y se lo compara contra la regla corrida paso por
paso ([propuesta](../../research/proposals/2026-11-16-outrun-a-program-that-summarizes.md),
[juego](../../games/outrun/README.md)).

Dos juegos en el mismo mundo:

- `collisions` (simple): entre dos y cuatro fichas que viajan y se encuentran pocas veces.
- `pingpong` (más complejo): una cosa que rebota entre dos paredes; en cada rebote la pared derecha se corre
  un lugar, y los rebotes no se acaban nunca.

## Condiciones

- **Modelos:** `gpt-6-astra` (el mejor disponible) y `gpt-5.4` (generación anterior), con esfuerzo de
  razonamiento alto. Una partida por juego y por modelo. Si el gasto lo permite, una segunda partida de
  `gpt-6-astra` por juego, para ver cuánto cambia de una corrida a otra.
- **Lo que tiene la IA:** el enunciado completo (dice cómo se la va a probar), el simulador del mundo, un
  programa para comparar su solución contra el simulador, 40 ejecuciones de hasta 2 minutos, hasta 90 turnos.
- **Lo que entrega:** `solution.py` con `predict(start, steps)`.
- **Tope de gasto:** 25 dólares estimados para toda la carpeta. El costo se mide en la primera partida.
- **Casos de prueba:** `cases_collisions.json` (72: ocho por tamaño, de 10 a 2·10^9 pasos) y
  `cases_pingpong.json` (80: ocho por tamaño, de 10 a 2·10^10 pasos). Se sortearon una vez, con semilla fija,
  y su realidad se calculó corriendo la regla en C. Ningún modelo los ve.
- **Antes de esto** se corrió una sola partida de humo con `gpt-5.4-mini` para comprobar que el programa que
  hace jugar anda de punta a punta. No cuenta y no está en `raw/`.

## Qué se mide (todo con cuentas)

Un caso está bien si el programa da **exactamente** la fila que da la regla y tarda **menos de 1 segundo**.
El archivo no puede pesar más de 20.000 bytes.

Por cada partida:

1. **La tabla por tamaño:** cuántos de los ocho casos están bien en cada tamaño.
2. **El horizonte:** hasta qué tamaño están todos bien, sin saltearse ninguno.
3. **Casos bien, en total.**
4. **Tamaño del archivo.**
5. En `pingpong`, además: el horizonte mirando solo los comienzos normales, y cuántos de los 7 comienzos de
   excepción están bien. (Una excepción es un comienzo en el que una pared desaparece: una `b` pegada a la
   pared izquierda o una `c` pegada a la derecha. Hay una sola excepción por tamaño, así que una sola falla
   corta el horizonte estricto; por eso se informan los dos.)
6. Como dato, no como puntaje: cuánto gastó la IA en llegar (ejecuciones, tokens, minutos).

## Las varas (programas nuestros, corregidos con el mismo corrector)

Medidas sin IA con `python games/outrun/verify_worlds.py experiments/2026-11-16-outrun-first-two-games`.
Cada columna es un tamaño, de 10 pasos en adelante.

`collisions` (72 casos; tamaños de 10 a 10^9):

| Programa nuestro | Bytes | Horizonte | Bien | 10 | 10^2 | 10^3 | 10^4 | 10^5 | 10^6 | 10^7 | 10^8 | 10^9 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Corre todo (`brute`) | 1.149 | 10^5 | 41/72 | 8 | 8 | 8 | 8 | 8 | 1 | 0 | 0 | 0 |
| Receta general (`events`) | 3.177 | 10^9 | 72/72 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 |

`pingpong` (80 casos; tamaños de 10 a 10^10; 73 comienzos normales y 7 de excepción):

| Programa nuestro | Bytes | Horizonte | Bien | 10 | 10^2 | 10^3 | 10^4 | 10^5 | 10^6 | 10^7 | 10^8 | 10^9 | 10^10 | Normales | Excepciones |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Corre todo (`brute`) | 1.149 | 10^5 | 40/80 | 8 | 8 | 8 | 8 | 8 | 0 | 0 | 0 | 0 | 0 | 37/73 | 3/7 |
| Receta general (`events`) | 3.177 | 10^7 | 60/80 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 2 | 1 | 1 | 53/73 | 7/7 |
| La ley (`law_pingpong`) | 3.773 | 10^10 | 80/80 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 73/73 | 7/7 |

En los tres tamaños más grandes de `pingpong`, los pocos casos que la receta general acierta son los de
excepción: ahí una pared desaparece, la cosa se va y ya no hay rebotes que seguir.

Qué significa cada vara:

- **Corre todo** (`brute`): no sabe nada. Es el piso.
- **Receta general** (`events`): salta los tramos en que nada se toca y hace cada encuentro paso por paso. No
  sabe nada de este mundo en particular. Es el mejor rival que no usa la ley.
- **La ley** (`law_pingpong`): sabe cómo es el rebote y cuánto dura cada vuelta. Prueba que el resumen
  completo existe.

## Cómo se lee cada partida

| Lo que saca | Quiere decir |
|---|---|
| Horizonte igual o menor que el de "corre todo" | No resumió: entregó un programa que hace todos los pasos, o uno que se equivoca |
| Más lejos que "corre todo", sin llegar al final | Resumió una parte. Los casos que falla dicen cuál le falta |
| Todos los tamaños bien | Encontró un resumen completo (para estos casos) |
| No entrega archivo, o falla el tamaño más chico | Hay que mirar si el problema es nuestro antes de leer nada |

En `pingpong`, lo que importa es contra qué vara queda: **igual que la receta general** (resumió los viajes
pero no la ley del rebote) o **igual que la ley**.

## Cómo se lee el conjunto

| `collisions` | `pingpong` | Lectura | Qué se hace |
|---|---|---|---|
| Completo | Completo | A esta complejidad, el modelo resume el mundo entero. El formato funciona y el examen queda corto | Armar patrones con más piezas. No se afirma que el juego sea difícil |
| Completo | Como la receta general | Entrega una receta general pero no la ley de este mundo | Repetir `pingpong` con la idea nombrada. Si con la idea sale: le faltaba la idea. Si no: le falta ejecutarla |
| Completo | Peor que la receta general | Algo se rompe antes de llegar a la ley | Mirar los casos que falla y repetir con la idea nombrada |
| No completo | cualquiera | El juego simple no salió | Revisar primero nuestro enunciado y nuestro corrector |

Y entre modelos: si `gpt-5.4` también completa los dos, estos dos juegos no separan generaciones y la
escalera tiene que empezar más arriba.

La idea nombrada es un texto fijo (está en `games/outrun/play.py`, `HINTS`). Nombra el mecanismo, no da el
programa.

## Lo que este experimento no puede decir

- **Con qué frecuencia.** Es una partida por casillero. En otros bancos, el mismo modelo cambió mucho de una
  corrida a otra.
- **Si "tuvo una idea".** Mide si el programa entregado es un resumen cierto, chico y rápido.
- **Que el programa valga siempre.** Acierta o no en estos 72 y 80 casos.
- **Nada sobre el patrón de los encuentros en `collisions`:** ahí una receta general saca puntaje completo.
- Las varas son los mejores programas que escribimos nosotros, no los mejores posibles.
- El tiempo se mide en una sola máquina (la de Lucas), con otras cosas corriendo lo menos posible.

## Errores del proveedor

Si una partida se corta por un error ajeno al modelo (filtro de contenido, caída de la conexión), el registro
va a `raw-errors/` y se repite una vez.
