# CLAUDE.md — essence-of-discovery

Al arrancar: leé `README.md` (la pregunta y el estado) y `DECISIONS.md`. Si no conocés el proyecto,
`docs/guide.md`. El repo anterior (`research-worlds-envs`, WAGER) es biblioteca de solo lectura: sus reglas
y su vocabulario (vicios, saltos, perillas) **no** aplican acá.

## Reglas duras

- **Ninguna IA en el cálculo del puntaje.** El puntaje es una cuenta contra una respuesta exacta.
- **Nada se construye ni se corre sin el OK de Lucas**: mundos nuevos, partidas con modelos, gasto de API.
  Antes de gastar, medir el costo con una tanda mínima.
- **Reglas congeladas antes de correr.** Cómo se lee cada resultado posible se escribe antes de mirar.
- **Todo mundo se verifica sin IA** antes de mostrárselo a un modelo (la cuenta larga contra el atajo).
- **Medir contra el mejor rival sin el truco**, optimizado; nunca contra uno puesto a dedo.
- **Titulares con su alcance**: qué modelos, qué mundos, cuántas partidas. Sin eso, no es un resultado.
- **No afirmar lo no verificado.** Decir qué se leyó entero, qué de resumen y qué de segunda mano.
- **Trabajo previo antes de decir "nadie lo hizo"**: búsqueda seria, y contar cuántas búsquedas fueron.
- **Claves y credenciales nunca en el repo** (es público). Van por variable de entorno.

## Cómo se trabaja

- **Nombres de carpetas y archivos en inglés**, en minúsculas con guiones (`2026-11-15-short-name.md`);
  código en `snake_case`. El contenido de los documentos va en castellano llano.
- Dónde va cada cosa: código y experimentos de un juego en `games/<game>/` (cada experimento en
  `experiments/<date-name>/`: reglas, crudos, lectura de diez líneas); explicaciones para personas en
  `docs/`; investigación en `research/` (`readings/` lo leído, `theory/` marcos, `findings/` resultados,
  `notes/` notas de trabajo, `proposals/` propuestas, `reviews/` opiniones externas).
- Decisiones: una línea en `DECISIONS.md` (fecha — decisión — razón). No hay sistema de ADRs.
- Sin documentos de teoría antes del primer resultado. Topes: README una página, este archivo 40 líneas.
- Todo cierre a Lucas termina con dos cosas: qué se aprendió y qué límite tiene, y la lista de pendientes.
- Python 3.13.

## Con Lucas

Respuestas cortas, una idea por vez, sin jerga, empezando por el problema. Lo denso va a documentos. Si
algo se puede mostrar con una figura, mostrarlo. Él decide; Codex y GPT Astra son segundas opiniones.
