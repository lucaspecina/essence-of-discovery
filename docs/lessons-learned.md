# Lecciones heredadas

Lo que dejaron las etapas anteriores y sigue valiendo acá. Una página; el detalle está en el
[repo anterior](https://github.com/lucaspecina/research-worlds-envs).

## De dónde venimos

1. **SREG**: entornos amplios para que una IA "investigue", con la nota puesta por otra IA. Se abandonó
   porque una nota opinable no prueba nada.
2. **WAGER**: mundos-rompecabezas con una verdad escondida y nota por fórmula. Se trabó porque, cuando el
   agente fallaba, había demasiadas explicaciones posibles (datos, ruido, incentivo, o falta de idea).
3. **La esencia** (desde septiembre de 2026): juegos mínimos que aíslen una sola cosa.

Qué cambió exactamente entre WAGER y el juego de ahora está en
[De WAGER a jump-ahead](from-wager-to-jump-ahead.md).

## El método que se queda

- **Puntaje mecánico, sin ninguna IA.**
- **Medir contra el mejor rival que no usa el truco**, y optimizarlo. Una vez la historia simple sacaba
  0,986 y cambiarla no pagaba: el mundo no pedía la idea.
- **La idea nombrada como control.** Si ni nombrándole la idea el agente resuelve, el mundo está mal hecho.
- **Mundos gemelos**: uno con la cosa y otro igual sin ella.
- **Reglas congeladas antes de correr.**
- **Titulares con su alcance** (modelos, mundos, cantidad de partidas).
- **Agentes reales temprano**: no diseñar meses sin probar con un modelo.

## Lo que se observó (descriptivo, modelos de agosto de 2026)

Los agentes aceptaban el test y no cambiaban su historia; con la idea nombrada, algunos lo lograban. Se
caían antes de la idea (veían lo raro y no dejaban que les molestara) y después (no corrían la prueba que
decidía, o armaban el candidato correcto y lo descartaban).

**Aviso:** el modelo de esas tandas saca 0,2% en ARC-AGI-3, donde el mejor de noviembre de 2026 saca 81%.
Son observaciones de modelos viejos; no hay que repetirlas como hechos sobre "los agentes".

## El error que no hay que repetir

Tres reformulaciones entre agosto y noviembre de 2026, y ningún experimento. Un repo limpio no arregla
eso. Lo primero que tiene que entrar acá es un juego con su resultado.

## Dónde está la investigación previa

En [`research/legacy/`](../research/legacy/): lecturas, teoría, hallazgos, notas y revisiones traídas del
repo anterior. El índice está en [`research/`](../research/). Lo demás (unos 155 documentos de pruebas de WAGER y el código) quedó allá. Código
reutilizable cuando haga falta: `wager/agent/llm_client.py` y `wager/harness/kernel_proc.py`.
