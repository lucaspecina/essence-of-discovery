# jump-ahead

**El juego.** La IA ve la regla completa de un sistema simple y recibe una pregunta sobre un futuro
lejísimo (por ejemplo, el paso un trillón). Tiene una computadora chica para experimentar, que no alcanza
para llegar paso por paso. Entrega un programita que contesta rápido y dice cuán segura está. Se corrige
contra la respuesta exacta, sin ninguna IA de juez. Sin atajo es imposible; con atajo es fácil.

**Qué mide.** Si la IA encuentra el atajo y, sobre todo, si lo *ve* o lo *busca*: se esconde el mismo
atajo en pajares cada vez más grandes y se mira cuánto crece su esfuerzo, contra un buscador a ciegas.
También cuántas veces cree ver un atajo que no está (mundos sin atajo y trampas).

La explicación completa, con figuras, está en la [guía](../../docs/guide.md).

## Estado (15-nov-2026)

**Hecho, sin IA:** seis ejemplos de mundos verificados con cuentas. Para reproducirlos:

```
pip install numpy matplotlib
python games/jump_ahead/verify_examples.py
```

Corre en segundos y comprueba, entre otras cosas:

- un sistema con atajo donde el paso un trillón se contesta en una fracción de milisegundo;
- un sistema disfrazado (5 símbolos renombrados) donde la prueba estándar deja de ver el atajo, un
  buscador a ciegas lo recupera probando renombres (sirven 20 de 120), y el estado del paso un trillón
  sale en milisegundos; sin el atajo, el sistema recién se repite a los 794.728.597.005.208 pasos;
- una trampa: un dibujo que se repite 118 veces seguidas y a la vuelta siguiente cambia.

**Mini-juegos armados y verificados sin IA** (`minigames/`, se comprueban con
`python games/jump_ahead/verify_minigames.py`):

| Mini-juego | Regla de generación (la IA la ve) | Regla de resultado (la IA la tiene que encontrar) |
|---|---|---|
| `ring-shift-7` | Cada casilla copia a su vecina de la izquierda | Todo se repite cada 7 pasos. Es el control fácil: si una IA falla acá, lo roto es nuestro programa |
| `xor-ring-101` | Una casilla queda prendida si sus dos vecinas eran distintas | Después de 2, 4, 8, 16... pasos, cada casilla depende solo de las dos que están a esa distancia. Contando 200.000 pasos la fila no se repite |

En los dos, la regla de resultado coincide con la cuenta larga en los pasos 0 a 3.000, y las respuestas del
paso un trillón salen en milisegundos.

La fila del juego 2 sí vuelve a repetirse, pero recién en el paso 375.299.968.947.541 (calculado con la regla
de resultado; el script lo comprueba). A mil millones de pasos por segundo serían 4,3 días contando.

Los dos juegos se pueden tocar en una página: <https://claude.ai/artifact/1w2gYRZUJRW8Wk27LtxsaM> (enlace
privado de Lucas; su fuente es [`docs/first-two-games.html`](../../docs/first-two-games.html)). Lucas puede
editar el texto ahí mismo: si la página cambia, hay que traer la versión nueva al repo.

**Primera prueba con IAs (16-nov-2026):** 29 partidas con `gpt-6-astra`, `gpt-5.4` y `claude-opus-4-6`.
Resultado: esconder un sistema conocido cambiándole los nombres no le esconde nada al mejor modelo
(resolvió todo en menos de dos minutos por juego); los modelos anteriores sí tropiezan. Reglas, partidas
crudas y lectura en [`experiments/2026-11-16-mixing-ladder/`](../../experiments/2026-11-16-mixing-ladder/reading.md).

Para eso se agregaron: juegos mezclados y de dos capas (`mixed/`, se comprueban con
`python games/jump_ahead/verify_mixed.py`), juegos con tabla sorteada al azar cuya respuesta sale de contar
en C, y el programa que hace jugar a un modelo en una computadora chica y encerrada (`harness/play.py`).

## Lo que sigue (espera el OK de Lucas)

1. Armar unos 12 mini-juegos (con atajo a dos niveles de disfraz, sin atajo, trampas) y verificarlos sin IA.
2. Probar un modelo actual: primero 4 partidas para medir el costo, después unas 48.
3. Leer el resultado contra reglas escritas de antemano:

| Si pasa esto | Quiere decir | Qué se hace |
|---|---|---|
| Resuelve todo, hasta lo más disfrazado | El juego es fácil para los modelos de hoy | Endurecer o cerrar |
| No resuelve ni con la idea nombrada | El juego está mal armado | Arreglar el juego |
| Resuelve, y su esfuerzo crece como el del buscador a ciegas | Busca | Resultado |
| Resuelve, y su esfuerzo casi no crece | Ve (si no era un truco de manual) | Resultado |

## Cómo se arma un juego con regla de resultado

Al revés: se empieza por la respuesta. La IA recibe las piezas en el orden contrario.

1. **Elegir una regla de resultado ya demostrada** (probada con un razonamiento, no solo vista en ejemplos).
2. **Escribir la regla de generación** que la produce: una línea, que es lo que ve la IA.
3. **Elegir el comienzo y la pregunta lejana**, tan lejos que contando no se llegue. Y revisar que no quede
   un camino más fácil que el que plantamos (en el juego 2: que la fila no se repita pronto).
4. **Verificar sin IA**: la cuenta paso por paso contra la regla de resultado, casilla por casilla. Si
   difieren una vez, el juego se tira.

Son dos seguros distintos. El razonamiento dice que la regla vale en el paso un trillón; la comparación
(que llega hasta el paso 3.000) dice que la escribimos bien.

Límites de armar así: solo salen juegos cuya regla de resultado ya conocía alguien, así que una IA puede
saberla de memoria (de eso se ocupan los disfraces). Los juegos sin regla de resultado y las trampas se
arman de otra manera. Y la IA no tiene que encontrar la misma regla que nosotros: solo se califican las
respuestas.

## Decisiones de diseño

- El titular no es la pregunta "¿ve o busca?" (ya la hicieron otros, con una IA de juez). Es medirla sin
  juez, con el atajo plantado.
- El esfuerzo se mide solo sobre partidas resueltas: una IA que se rinde también trabaja poco.
- El tamaño del pajar es "uno de cada cuántos intentos a ciegas funciona", no el total de opciones, porque
  varias opciones destapan el mismo atajo.

## Pendientes

- Fijar cuánto cómputo recibe la IA. Tiene que quedar muy por debajo de lo que cuesta el camino sin regla
  de resultado: en el juego 2, encontrar la repetición contando lleva unos 4 días a mil millones de pasos
  por segundo.
- Traer del repo anterior, para la primera prueba, el cliente de modelos y el proceso que ejecuta el código
  del agente (unas 400 líneas).
- Leer a texto completo el trabajo previo más cercano antes de afirmar novedad.

## Lo más cercano que hicieron otros

- DeepMind, [arXiv:2610.22603](https://arxiv.org/abs/2610.22603): una IA encuentra atajos verificados en
  máquinas de juguete sin resolver. La manera de mirar la arma un programa de los autores; un solo tipo de
  atajo; no mide cómo los encuentra.
- Han et al., [arXiv:2505.10844](https://arxiv.org/abs/2505.10844), y Hu et al.,
  [arXiv:2602.10329](https://arxiv.org/abs/2602.10329): la pregunta "¿fuerza bruta o algo más fino?", con
  una IA de juez leyendo la solución.
- Invariantes de ciclos con IA y verificador, por ejemplo [arXiv:2508.00419](https://arxiv.org/abs/2508.00419):
  los modelos ya resuelven el banco clásico completo.

Leído de resúmenes y partes, no a texto completo. El detalle y el resto de las fuentes están en el
[documento de la propuesta](../../research/proposals/2026-11-15-discovery-as-finding-a-shortcut.md) (§8).
