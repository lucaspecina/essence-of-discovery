# essence-of-discovery

**La pregunta.** Cuando una IA resuelve algo difícil, ¿se le ocurrió la idea o probó cosas hasta que una
funcionó? ¿Se puede medir esa diferencia con juegos mínimos, sin que otra IA haga de juez?

**Estado (15-nov-2026).** Repo recién creado. Hay un juego en diseño, `jump-ahead`: seis ejemplos de
mundos verificados con cuentas, **cero partidas jugadas con una IA**. Nada de lo que hay acá es todavía un
resultado sobre modelos.

## Para entender de qué se trata

Leé la [guía en llano](docs/guia.md). Son 7 minutos, sin jerga.

## Los juegos

| Juego | La idea en una línea | Estado |
|---|---|---|
| [`jump-ahead`](games/jump_ahead/) | La IA ve la regla completa de un sistema simple y tiene que contestar por un futuro lejísimo. Paso por paso no llega: tiene que encontrar un atajo. Medimos si lo *ve* o lo *busca*. | Diseño. Ejemplos verificados sin IA. |

Cada juego vive en su carpeta. Si un juego no da señal, se cierra y el siguiente va al lado.

## Cómo está ordenado

- `games/<juego>/` — un juego: sus mundos, sus cuentas y sus experimentos.
- `docs/guia.md` — la explicación para personas.
- `docs/lecciones-heredadas.md` — lo que aprendimos antes y sigue valiendo.
- `biblioteca/` — la investigación previa que sirve acá (lecturas, fuentes, análisis), congelada.
- `DECISIONES.md` — una línea por decisión.
- `CLAUDE.md` — las reglas para las sesiones de trabajo con IA.

## Reglas de la casa

1. Una sola pregunta, arriba de este README. Si cambia, se cambia acá; no se agrega un documento.
2. Ningún documento de teoría antes del primer resultado.
3. Cada experimento es una carpeta: reglas congeladas, resultados crudos y una lectura de diez líneas.
4. Este README entra en una página. `CLAUDE.md` entra en 40 líneas.
5. Las decisiones van en un solo archivo, una línea cada una.

## De dónde viene

Es la continuación de [`research-worlds-envs`](https://github.com/lucaspecina/research-worlds-envs)
(proyecto WAGER). La investigación de allá que sirve acá está en [`biblioteca/`](biblioteca/), incluido el
[documento que propone esta línea](biblioteca/2026-11-15-reformulacion-descubrir-es-encontrar-un-atajo.md).
