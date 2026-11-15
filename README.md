# essence-of-discovery

**La pregunta.** Cuando una IA resuelve algo difícil, ¿se le ocurrió la idea o probó cosas hasta que una
funcionó? ¿Se puede medir esa diferencia con juegos mínimos, sin que otra IA haga de juez?

**Estado (15-nov-2026).** Repo recién creado. Hay un juego en diseño, `jump-ahead`: seis ejemplos de
mundos verificados con cuentas, **cero partidas jugadas con una IA**. Nada de lo que hay acá es todavía un
resultado sobre modelos.

## Para entender de qué se trata

Leé la [guía en llano](docs/guide.md). Son 7 minutos, sin jerga.

## Los juegos

| Juego | La idea en una línea | Estado |
|---|---|---|
| [`jump-ahead`](games/jump_ahead/) | La IA ve la regla completa de un sistema simple y tiene que contestar por un futuro lejísimo. Paso por paso no llega: tiene que encontrar un atajo. Medimos si lo *ve* o lo *busca*. | Diseño. Ejemplos verificados sin IA. |

Cada juego vive en su carpeta. Si un juego no da señal, se cierra y el siguiente va al lado.

## Cómo está ordenado

En la raíz va solo lo oficial. Abajo, cada cosa en su lugar:

```
games/<game>/    el juego: su código y cómo se juega
experiments/     cada corrida: reglas, resultados crudos, lectura
docs/            lo oficial y vigente: guide, lessons-learned, decisions/, figures/
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
