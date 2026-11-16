# outrun ("ganarle a la cuenta")

**El juego.** La IA recibe la regla completa de un mundo simple (una fila de casillas que cambian mirando a
sus vecinas) y tiene que entregar **un programa**: "poné cualquier comienzo y cualquier cantidad de pasos, y
decí cómo queda el mundo". Ese programa se compara contra la realidad, que es la regla corrida paso por paso
por nosotros.

**Qué mide.** Si la IA convirtió lo que exploró en un **resumen** del mundo: un programa que acierta, pesa
poco y no tarda más cuanto más lejos se le pregunta. Se miden tres cosas, todas con cuentas:

1. ¿Coincide con la realidad? Exacto, en comienzos y pasos que la IA no vio.
2. ¿Cuánto pesa el archivo? (tope: 20.000 bytes)
3. ¿Cuánto tarda cada respuesta? (tope: 1 segundo)

Hay dos maneras de acertar sin haber resumido nada, y cada una se ve en una medida: correr todos los pasos
(programa chico, pero se queda sin tiempo lejos) y guardar respuestas ya calculadas (rápido, pero no entra en
el tope de tamaño ni sirve para comienzos nuevos).

La explicación completa, con un ejemplo, está en la
[propuesta](../../research/proposals/2026-11-16-outrun-a-program-that-summarizes.md).

## El mundo de los dos primeros juegos

Seis símbolos (`.` es casilla vacía) y una regla de 20 renglones (`world.py`). La armamos dibujando lo que
queríamos que pasara:

- un par `a b` y una letra sola (`a` o `b`) viajan a la derecha; una `c` viaja a la izquierda; una `d` se
  queda quieta;
- cuando un par se encuentra con una `c`, según la distancia a la que arrancaron queda una cosa u otra;
- cuando algo que viene de la izquierda toca una `d`, rebota como `c` y la `d` queda un lugar más a la
  derecha; cuando una `c` toca una `d` desde la derecha, rebota como letra y la `d` no se mueve.

Lo que el mundo hace de verdad tiene más cosas que las que dibujamos (aparecieron dos excepciones al
verificar). La verdad de los juegos es siempre lo que da la regla.

| Juego | Comienzos | Qué hace falta para llegar lejos |
|---|---|---|
| `collisions` (simple) | Entre dos y cuatro fichas (`a b` y `c`) separadas por hasta un millón de casillas | Saltar los tramos en que las cosas viajan solas. Hay pocos encuentros |
| `pingpong` (más complejo) | Dos paredes `d` y una cosa entre ellas | La ley del rebote: en cada vuelta la pared derecha se corre un lugar, así que cada vuelta tarda dos pasos más. Los rebotes no se acaban nunca |

Se pregunta por cantidades de pasos de todos los tamaños: de 10 a 2.000 millones en `collisions` y a 20.000
millones en `pingpong`. Ocho comienzos nuevos por tamaño.

## Verificación sin IA

```
python games/outrun/verify_worlds.py                    # un minuto
python games/outrun/verify_worlds.py <carpeta-de-experimento>   # además corrige nuestros programas de referencia
```

Comprueba que la realidad rápida (`truth.c`) da lo mismo que la regla en Python; que nuestros programas de
referencia dan exactamente lo mismo que la realidad en miles de comienzos; y qué puntaje saca cada uno con el
corrector de verdad. Esos puntajes son las varas contra las que se lee a un modelo:

| Programa nuestro (`references/`) | Qué sabe | Para qué sirve |
|---|---|---|
| `brute.py` | Nada: corre la regla | El piso |
| `events.py` | Una receta general: saltar los tramos sin encuentros y hacer cada encuentro paso por paso. No sabe nada de este mundo en particular | El mejor rival que no usa la ley |
| `law_pingpong.py` | La ley del rebote, en cuentas | Prueba que el resumen completo existe |

## Cómo se corre una partida

```
python games/outrun/evaluate.py build collisions <carpeta>     # sortea los casos y calcula su realidad (una vez)
python games/outrun/play.py --model gpt-6-astra --effort high --game collisions --exp <carpeta> --budget 25
```

La IA tiene una computadora encerrada (sin red, sin acceso a nuestros archivos), 40 ejecuciones de hasta 2
minutos, el simulador del mundo y un programa para comparar su solución contra él. No hay nada escondido: el
enunciado le dice cómo se la va a probar. Su `solution.py` se prueba después en una carpeta vacía.

## Estado (16-nov-2026)

Juegos armados y verificados sin IA. Primera prueba con modelos (6 partidas): `gpt-6-astra` y `gpt-5.4`
sacaron todos los casos bien en los dos juegos.
[Lectura](../../experiments/2026-11-16-outrun-first-two-games/reading.md). La forma de medir funciona. Estos
dos mundos no sirven de examen: el patrón lo dibujamos nosotros dentro de la regla, y se lee.

## Límites conocidos

- Solo se compara hasta donde nosotros podemos correr la regla (minutos de cómputo por caso).
- Acertar todos los casos no demuestra que el programa valga siempre.
- En `collisions` alcanza con una receta general: ese juego no prueba que la IA haya encontrado el patrón de
  los encuentros.
- El tiempo se mide en una sola máquina. Por eso los tamaños van de a diez veces.
