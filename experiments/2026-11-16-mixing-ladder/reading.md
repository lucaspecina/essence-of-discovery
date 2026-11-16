# Escalera de mezcla: lectura

**Alcance.** 29 partidas, una por juego y por modelo. Modelos: `gpt-6-astra`, `gpt-5.4` y `claude-opus-4-6`
(este último solo en 4 juegos), con esfuerzo de razonamiento alto. 11 juegos armados en una tarde. Gasto
estimado: 15,65 dólares (precios de una búsqueda web). Para volver a ver la tabla:
`python games/jump_ahead/harness/summarize.py experiments/2026-11-16-mixing-ladder/raw`.

## Resultados

Tiempo hasta la respuesta correcta. "No sé" quiere decir que no lo resolvió y lo dijo (puntaje 0).

| Juego | Qué es | GPT-6 Astra | GPT-5.4 | Claude Opus 4.6 |
|---|---|---|---|---|
| `plain-5` | sistema conocido a la vista | 11 s | 18 s | 37 s |
| `mix-5` | 5 letras mezcladas | 25 s | 74 s | 370 s |
| `mix-7` | 7 letras | 30 s | 76 s | no corrido |
| `mix-8b` | 8 letras | 50 s | 180 s | no corrido |
| `mix-17` | 17 letras (a ciegas: 12 días) | 32 s | 73 s | no sé · con pista, 184 s |
| `mix-25p` | 25 letras (a ciegas: imposible) | 39 s | no sé · con pista, 80 s | 1.092 s |
| `deep-9` | dos capas, 9 letras | 54 s | 174 s | no corrido |
| `deep-25` | dos capas, 25 letras | 112 s | no sé · con pista, 197 s | no corrido |
| `twin-a` | tabla al azar; se repite a los 2,3 millones de pasos | 241 s | 83 s | no corrido |
| `twin-b` | tabla al azar; hay que contar 85 millones | 1.128 s | no sé | no corrido |
| `twin-c` | tabla al azar; hay que contar 10.800 millones | no sé (correcto) | no sé (correcto) | no corrido |

## Lectura, con las reglas escritas antes de correr

1. **Astra cae en el caso 1: el cambio de nombres no le esconde nada.** Resolvió los cinco mezclados en
   menos de un minuto cada uno. La objeción de Lucas queda confirmada para este modelo.
2. **No busca a ciegas.** Usó entre 3 y 6 ejecuciones y menos de 5 segundos de cómputo en todos, también en
   los dos donde probar todos los órdenes es imposible. Reconstruye el orden escondido mirando la tabla.
3. **Esconder en dos capas tampoco le es obstáculo** (agregado 2): 54 y 112 segundos.
4. **Los modelos anteriores sí tropiezan.** GPT-5.4 no resolvió `mix-25p` ni `deep-25`; Claude Opus 4.6 no
   resolvió `mix-17`. Con la idea nombrada, los tres salieron: les faltaba la idea o las ejecuciones.
5. **Tablas al azar** (agregado 1). Los dos GPT encontraron solos la repetición de `twin-a`. Astra también
   la de `twin-b`: armó un programa que avanza de a 3 pasos por búsqueda y llegó a los 85 millones en 19
   segundos de cómputo. En `twin-c`, que no está a su alcance, los dos dijeron "no sé".
6. **Nadie afirmó sin saber.** En las 29 partidas no hubo una sola respuesta segura y equivocada.

## Qué dice sobre la idea

- Esconder una estructura conocida, a la profundidad que supimos armar hoy, **no sirve como examen para el
  mejor modelo actual**: le queda fácil.
- El examen **sí separa generaciones de modelos**, con puntaje exacto y sin IA de juez, a centavos por partida.
- En tablas al azar el límite fue el cómputo, no las ideas: no medimos si la IA encuentra una regularidad
  difícil, porque en una tabla al azar no sabemos armar una.

## Límites

- Una sola partida por casillero: se ve si lo resuelven, no con qué frecuencia. Los tiempos son de una corrida.
- No distingue "descubrió" de "aplicó un método que conocía".
- En `deep-9` y `deep-25` no comprobamos con un programa nuestro que se resuelvan mirando solo lo que ve
  la IA. Dos modelos los resolvieron, así que resolubles son.
- A GPT-5.4 el filtro de contenido del proveedor le rechazó dos enunciados en el primer intento (`mix-8b`,
  `mix-17`). Se reintentaron una vez y salieron. Los rechazos están en `raw-errors/`.
- "Todo lo que supimos armar hoy" no es "todo lo que se puede armar".
