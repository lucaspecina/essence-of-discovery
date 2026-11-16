# essence-of-discovery

**La pregunta.** Cuando una IA resuelve algo difícil, ¿se le ocurrió la idea o probó cosas hasta que una
funcionó? ¿Se puede medir esa diferencia con juegos mínimos, sin que otra IA haga de juez?

**Estado (16-nov-2026).** Dos juegos.

- `jump-ahead`: primera prueba con IAs hecha (29 partidas, tres modelos). Esconder un sistema conocido
  cambiándole los nombres **no** le esconde nada al mejor modelo probado (`gpt-6-astra` resolvió todo en
  menos de dos minutos por juego); los anteriores sí tropiezan. Esa forma de armar el examen quedó cerrada.
  [Lectura](experiments/2026-11-16-mixing-ladder/reading.md).
- `outrun`: en vez de una respuesta, la IA entrega un programa que predice el mundo, y se lo compara contra
  la regla corrida paso por paso. Dos juegos armados y verificados sin IA, y una primera prueba con
  modelos (6 partidas): los dos modelos sacaron todo bien. La forma de medir funciona, pero en esos mundos el
  patrón lo dibujamos nosotros dentro de la regla y se lee. El rumbo que sigue no está decidido.
  [Lectura](experiments/2026-11-16-outrun-first-two-games/reading.md).
  [Propuesta](research/proposals/2026-11-16-outrun-a-program-that-summarizes.md).

## Para entender de qué se trata

Leé la [guía en llano](docs/guide.md). Son 7 minutos, sin jerga.

## Los juegos

| Juego | La idea en una línea | Estado |
|---|---|---|
| [`jump-ahead`](games/jump_ahead/) | La IA ve la regla completa de un sistema simple y tiene que contestar por un futuro lejísimo. Paso por paso no llega: tiene que encontrar un atajo. Medimos si lo *ve* o lo *busca*. | Primera prueba hecha: al mejor modelo le queda fácil. |
| [`outrun`](games/outrun/) | La IA ve la regla completa y entrega un programa que dice cómo queda el mundo después de cualquier cantidad de pasos. Se mide si acierta, cuánto pesa y cuánto tarda. | Primera prueba hecha: los dos modelos probados resuelven los dos juegos enteros. La forma de medir funciona; los mundos quedaron cortos. |

Cada juego vive en su carpeta. Si un juego no da señal, se cierra y el siguiente va al lado.

## Cómo está ordenado

En la raíz va solo lo oficial. Abajo, cada cosa en su lugar:

```
games/<game>/    el juego: su código y cómo se juega (games/shared/: lo que usan todos)
experiments/     cada corrida: reglas, resultados crudos, lectura
docs/            lo oficial y vigente: guide, lessons-learned, from-wager-to-jump-ahead, decisions/
research/        material de trabajo: proposals, readings, theory, notes, reviews, legacy/
CLAUDE.md        reglas para las sesiones de trabajo con IA
```

Los nombres de carpetas y archivos van en inglés; el contenido, en castellano.

## Reglas de la casa

1. Una sola pregunta, arriba de este README. Si cambia, se cambia acá.
2. Ningún documento de teoría nuevo antes del primer resultado.
3. Cada corrida es una carpeta en `experiments/`, con sus reglas escritas antes de correr.
4. Este README entra en una página. `CLAUDE.md` entra en 40 líneas.
5. En `docs/decisions/` van solo las decisiones que cambian el rumbo, una por archivo.

## De dónde viene

Continúa [`research-worlds-envs`](https://github.com/lucaspecina/research-worlds-envs) (proyecto WAGER). La
investigación de allá que sirve acá está en [`research/`](research/), incluida la
[propuesta de esta línea](research/proposals/2026-11-15-discovery-as-finding-a-shortcut.md).
Qué cambió respecto de WAGER: [De WAGER a jump-ahead](docs/from-wager-to-jump-ahead.md).
