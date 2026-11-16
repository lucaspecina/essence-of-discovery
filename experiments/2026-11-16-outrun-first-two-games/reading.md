# Primeros dos juegos de `outrun`: lectura

**Alcance.** 6 partidas: `gpt-6-astra` dos veces en cada juego y `gpt-5.4` una vez en cada juego, con
esfuerzo de razonamiento alto. Dos juegos armados en una tarde, en el mismo mundo. Gasto estimado: 6,30
dólares (precios de una búsqueda web, sin descontar la entrada repetida). Para volver a ver la tabla:
`python games/outrun/summarize.py experiments/2026-11-16-outrun-first-two-games`.

## Resultados

"Bien" es la cantidad de casos donde el programa entregado dio exactamente lo que da la regla, en menos de
un segundo.

| Juego | Modelo | Bien | Horizonte | Bytes | Ejecuciones | Minutos | USD |
|---|---|---|---|---|---|---|---|
| `collisions` | `gpt-6-astra` (1) | 72/72 | 10^9 (el máximo) | 3.679 | 7 | 3,2 | 1,11 |
| `collisions` | `gpt-6-astra` (2) | 72/72 | 10^9 | 4.645 | 6 | 4,3 | 1,07 |
| `collisions` | `gpt-5.4` | 72/72 | 10^9 | 5.545 | 35 | 7,3 | 2,45 |
| `pingpong` | `gpt-6-astra` (1) | 80/80 | 10^10 (el máximo) | 2.089 | 4 | 1,5 | 0,50 |
| `pingpong` | `gpt-6-astra` (2) | 80/80 | 10^10 | 2.425 | 4 | 1,6 | 0,53 |
| `pingpong` | `gpt-5.4` | 80/80 | 10^10 | 2.084 | 13 | 2,9 | 0,63 |

Las varas (programas nuestros): el que corre todo llega a 10^5; la receta general completa `collisions` y
llega a 10^7 en `pingpong`; la ley completa `pingpong` con 3.773 bytes.

## Lectura, con las reglas escritas antes de correr

1. **Los dos modelos encontraron el resumen completo de los dos juegos.** Es la fila "completo / completo":
   a esta complejidad el modelo resume el mundo entero, el formato funciona y el examen queda corto.
2. **Los dos juegos no separan generaciones.** `gpt-5.4` también completó los dos. Le costó más
   ejecuciones (35 contra 7 en `collisions`).
3. **En `pingpong` los dos modelos entregaron la ley, no la receta general.** Sus programas traen la cuenta
   de las vueltas con raíz cuadrada y los dos comienzos de excepción (7 de 7). El de Astra pesa menos que
   el nuestro.
4. **En `collisions` los dos modelos encontraron además la ley del rebote**, que ahí no hacía falta: la
   situación de algo atrapado entre dos paredes aparece sola en 4 de cada 1.000 comienzos de ese juego
   (medido en 3.000 sorteados) y en ninguno de los 72 casos de prueba.
5. **Entre corridas no cambió nada**: las dos partidas de Astra en cada juego dieron lo mismo.

## Qué dice sobre la idea

- **La forma de medir funciona.** Programa entregado, comparado contra la regla corrida, con tamaño y
  tiempo: da puntaje por grados (la partida de humo con un modelo chico sacó 16 de 72), separa "corre todo"
  de "tiene la ley", y cuesta entre 50 centavos y 2,50 dólares por partida.
- **Estos mundos no sirven de examen.** La razón se podía decir antes de correr y está en lo que señalaron
  los críticos: el patrón lo dibujamos nosotros dentro de la regla. Tres de los 20 renglones son,
  literalmente, el rebote. Leer la regla es leer el dibujo. El hueco entre la regla y el patrón es chico
  por construcción.
- **Lo que queda planteado** (de la charla con Lucas, sin decidir): las dos cosas que queremos se pelean.
  Si elegimos nosotros el patrón, hay que escribirlo en la regla y se lee. Si el patrón sale solo, como en
  las reglas de Wolfram, el hueco es grande, pero no lo elegimos: lo tenemos solo si estudiamos ese mundo
  antes. Y en esos mundos casi nunca hay una fórmula del futuro lejano; hay hallazgos parciales (objetos
  que viajan, qué pasa cuando chocan) que se comprueban corriendo.

## Límites

- Dos modelos, dos juegos, una o dos partidas por casillero.
- Acertar todos los casos no demuestra que los programas valgan siempre.
- Las varas son los mejores programas que escribimos nosotros.
- El tiempo se midió en una sola máquina.
- "Estos mundos no sirven" vale para mundos dibujados como estos. No dice nada de mundos donde el patrón
  no se dibujó.
