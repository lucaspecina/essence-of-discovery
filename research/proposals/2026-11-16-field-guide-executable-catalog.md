# Propuesta (16-nov-2026): que la IA entregue la "guía de campo" de un mundo que armamos nosotros

**Estado: reemplazada el mismo día por una versión más simple, propuesta por Lucas:**
[que la IA entregue un programa que resuma el mundo](2026-11-16-outrun-a-program-that-summarizes.md).
**Queda como registro del camino y de lo que dijeron los críticos. Nada de esto se construyó.**

Nombre de trabajo del juego: `field-guide` (guía de campo: el cuaderno donde un naturalista anota qué
existe en un lugar y cómo se comporta). El nombre lo decide Lucas.

## 0. En diez líneas

1. **Qué pasó ayer.** El mejor modelo resolvió en uno o dos minutos todos los juegos donde escondíamos una
   estructura conocida. Esa forma de armar el juego quedó cerrada.
2. **Qué pidió Lucas.** Elegir nosotros el fenómeno oculto y diseñar el juego para eso, sin disfraces, que
   no sea de juguete (sumas y multiplicaciones), y que sirva para saber cuándo una IA descubre.
3. **Cómo se pensó esto.** Unas 150 búsquedas de trabajo previo (tres lectores), ocho candidatas, y dos
   críticos externos (GPT Astra y Codex) en dos vueltas cada uno. Me corrigieron tres cosas de fondo.
4. **Lo que no existe.** Ni los críticos ni yo encontramos cómo plantar algo que al mejor modelo le pida
   una idea y que sea barato de certificar. Hay una razón: no se puede tener a la vez fenómeno rico,
   respuesta exacta lejana, verificación barata y regla arbitraria.
5. **Lo que sí cambia todo: dejar de pedir una respuesta y pedir un artefacto.** Una respuesta ("la casilla
   12 es B") no dice cómo se llegó. Un artefacto se puede correr, reusar y poner a prueba.
6. **La propuesta.** Armamos un mundo (un autómata con la regla a la vista) donde **nosotros plantamos qué
   cosas existen y qué pasa cuando chocan**. La IA lo explora sin que le digamos qué buscar y entrega su
   **guía de campo**: una lista de afirmaciones comprobables ("este dibujo viaja", "si estos dos chocan así,
   queda este otro").
7. **Cómo se corrige, sin IA.** (a) Un programa corre cada afirmación y dice si es verdad. (b) Contamos
   cuántas de las cosas plantadas encontró. (c) Otro programa, fijo y sin IA, usa esa guía para lograr
   objetivos que la IA nunca vio ("hacé que aparezca tal cosa acá"). La guía vale lo que le ahorra a ese
   programa.
8. **Qué mide que hoy se mide con jueces.** Qué descubrió, si es cierto, y si sirve. Y el falso
   descubrimiento: afirmaciones que no se cumplen al correrlas.
9. **Qué la mata, antes de gastar un dólar.** Si un buscador mecánico (sin IA) resuelve los objetivos solo,
   el mundo no sirve y no se corre ningún modelo.
10. **Primer paso.** Una prueba de descarte sin API (dos mundos chicos y tres buscadores mecánicos) y, solo
    si pasa, doce partidas con un modelo, tope 20 dólares. Necesita el OK de Lucas.

## 1. Cómo se hizo (honesto)

| Qué | Cómo | Dónde quedó |
|---|---|---|
| Releer lo propio | La propuesta del 15-nov entera (§0–§13), lecciones, de-WAGER-a-jump-ahead, la lectura de ayer, y partes de la teoría heredada sobre problemas de insight | — |
| Trabajo previo | Tres lectores secundarios en paralelo, unas 150 búsquedas y 120 páginas. **Casi todo resúmenes; nada leído entero; yo no abrí esas fuentes** | [`readings/2026-11-16-prior-work-three-searches.md`](../readings/2026-11-16-prior-work-three-searches.md) |
| Crítica externa | GPT Astra (por API, esfuerzo alto) y Codex (`gpt-5.6-sol`, esfuerzo máximo, con el repo a la vista), dos vueltas cada uno. Codex abrió fuentes primarias en las dos | [`reviews/2026-11-16-astra-two-rounds.md`](../reviews/2026-11-16-astra-two-rounds.md), [`reviews/2026-11-16-codex-two-rounds.md`](../reviews/2026-11-16-codex-two-rounds.md) |
| Lo que se les mandó | Ocho candidatas y ocho preguntas; después una síntesis y siete preguntas | [`reviews/2026-11-16-critics-briefs.md`](../reviews/2026-11-16-critics-briefs.md) |

Gasto: dos llamadas a GPT Astra (unos 30 mil tokens de entrada y 20 mil de salida en total; no medí el
costo exacto, estimo menos de 2 dólares). Codex corre con la suscripción de Lucas (unos 4,8 millones de
tokens entre las dos vueltas).

**Dos errores míos de este día, para que consten.** (1) Propuse "reglas que nadie diseñó, con la respuesta
calculada en una computadora más grande" como si fuera nueva: ya estaba en nuestra propuesta del 15-nov
(§5.5, "mundos salvajes") y tiene un antecedente de 2011. (2) La descarté en un mensaje, ante la primera
objeción. Las dos cosas son el mismo error: opinar sin haber hecho el trabajo.

## 2. Lo que aprendí (y lo que me corrigieron)

**2.1 La tensión de fondo.** Los dos críticos la señalaron por separado. No se pueden pedir las cuatro
cosas a la vez:

1. que el fenómeno oculto sea rico (tipo Wolfram, con regla arbitraria);
2. que nosotros conozcamos una respuesta exacta sobre un futuro lejísimo;
3. que comprobarla sea barato;
4. que la IA no pueda llegar igual que nosotros.

Si conocemos la respuesta lejana es porque hay una fórmula o un reloj, y entonces arriba hay algo simple
(por eso "siempre sumas y multiplicaciones": la objeción de Lucas era válida). Si el fenómeno es rico y lo
calculamos corriéndolo, la IA también puede. Si le ganamos por cómputo, medimos cómputo.

**La salida: soltar la segunda.** No preguntar por un futuro lejano. Pedir algo que se compruebe corriendo
el mundo un rato corto.

**2.2 Mi diagnóstico estaba mal dicho.** Escribí: "todo lo que el diseñador construye con método, un modelo
de frontera lo desarma con método". Astra: es falso en general; lo de ayer muestra una debilidad de *ese*
generador. Codex dio la versión que sí se sostiene:

> Construcción sistemática + representación local transparente + poca profundidad suele dejar una inversión
> mecánica barata.

**2.3 "Correr y mirar" verifica que algo pasa, no que algo es imposible.** Para decir "imposible" hace
falta una enumeración completa o un certificado, dentro de un dominio acotado. Las respuestas "no se puede"
solo valen con ese certificado.

**2.4 Lo que no se puede medir, y lo que sí.** Acertar, tardar poco o mejorar de golpe no distingue por sí
solo recuerdo, búsqueda guiada e idea nueva (Astra lo llama un límite de identificación). Sí se puede
medir: si encontró algo nuevo para esa instancia, a qué costo, si lo que encontró se puede reusar, y qué
ayuda lo destraba. Con las reglas a la vista **no** es cierto que "solo puede faltar la idea": también
pueden fallar la comprensión, la implementación y el presupuesto.

**2.5 Dónde hay margen hoy.** Según lo buscado (resúmenes), los modelos de 2026 todavía fallan donde hay que
encontrar estructura escondida interactuando (un autómata oculto de 8–9 estados: 57,5% el mejor, y el
motivo informado es que conocen el algoritmo clásico y no lo ejecutan bien) y donde hay que construir un
testigo no obvio. No fallan donde hay que derivar consecuencias de reglas dadas y prolijas.

## 3. La propuesta

### 3.1 En una frase

> **La IA explora un mundo que armamos nosotros y entrega su guía de campo: qué cosas existen ahí y qué
> pasa cuando se encuentran. Un programa comprueba cada afirmación corriéndola, y otro programa usa la guía
> para lograr cosas que la IA nunca vio.**

### 3.2 El mundo: qué plantamos

Un autómata de una dimensión, como los de ayer: una fila de casillas, cada una con un símbolo, y una tabla
que dice cómo cambia cada casilla mirando a sus dos vecinas. Casi toda la fila está vacía (un símbolo de
fondo que no cambia).

Lo que plantamos nosotros es **qué cosas viven ahí**:

- **Partículas**: dibujos chicos que viajan sin deshacerse (por ejemplo, tres casillas que se corren un
  lugar a la derecha cada dos pasos) o que se quedan quietos.
- **Choques**: qué queda cuando dos partículas se encuentran a cierta distancia y en cierto momento de su
  ciclo.

Dibujo de la idea (no es un mundo real; el tiempo corre hacia abajo):

```
A→  .   .   .   .   .   .  ←B
.   A→  .   .   .   .  ←B   .
.   .   A→  .   .  ←B   .   .
.   .   .   A→ ←B   .   .   .
.   .   .   .   C   .   .   .      A y B chocaron y quedó C, quieta
.   .   .   .   C   .   .   .
```

Cómo se plantan: se dibuja el diagrama de cada partícula y de cada choque, y cada trío de vecinas que
aparece en el dibujo fija un renglón de la tabla. Si dos dibujos piden cosas distintas para el mismo trío,
se sortea de nuevo. Los renglones que ningún dibujo usa se completan al azar (la mayoría llevan al fondo,
para que los restos se apaguen). La regla se entrega a la vista y **no dice en ningún lado qué partículas
hay**: eso hay que encontrarlo.

Regla de diseño que puso Codex y adopto: **plantar el lenguaje de objetos, no la oración que resuelve el
objetivo.** Primero se arma y se congela el mundo (partículas y choques). Los objetivos del examen se
generan después y por separado.

Las partículas son dibujos de varias casillas que pasan por varias formas. Por eso un choque no es un
renglón de la tabla que se pueda leer: es el resultado de muchos pasos, y para saberlo hay que hacer el
experimento.

### 3.3 Qué hace la IA y qué entrega

Recibe la regla y una computadora chica (como ayer). **No recibe ninguna pregunta.** La consigna es:
"investigá este mundo; después se va a usar lo que anotes para lograr cosas ahí adentro".

Entrega una **guía de campo** en un formato estricto: una lista de afirmaciones de dos tipos.

```
partícula:  dibujo = "G K F"   vuelve a aparecer cada 2 pasos, corrida 1 casilla a la derecha
choque:     partícula 1 y partícula 3, separadas por 5 casillas  →  queda partícula 4 en tal lugar, tras 9 pasos
```

Una vez entregada la guía, la IA se retira.

### 3.4 Cómo se corrige (tres números, ninguno puesto por una IA)

1. **Verdad.** Un programa corre cada afirmación en el mundo. Para una partícula alcanza con correr un
   ciclo: si el dibujo vuelve a aparecer igual y corrido, va a seguir haciéndolo para siempre, porque la
   regla es la misma en todas partes. Para un choque se corre hasta que quedan solo partículas ya
   comprobadas. Cada afirmación es cierta o falsa. **Las falsas son el falso descubrimiento, contado exacto.**
2. **Cobertura.** Cuántas de las cosas que plantamos están en la guía, separadas por profundidad: las que
   aparecen solas tirando símbolos al azar, las que solo salen de un choque, las que solo salen del choque
   de un producto con otra cosa.
3. **Utilidad.** Un programa planificador, fijo y sin IA, recibe la guía y una lista de objetivos que la IA
   nunca vio ("con hasta 12 casillas no vacías en estas dos bandas, hacé que a los 64 pasos haya
   exactamente tal dibujo en el centro y se mantenga dos ciclos"). El planificador solo sabe combinar lo
   que la guía dice. Se mide cuántos objetivos logra y cuánto trabajo le lleva, contra tres referencias: el
   mismo planificador sin guía, con una guía hecha por un catalogador mecánico, y con nuestra guía completa
   (la de quien plantó el mundo).

El tercer número es el que importa: **una guía vale lo que le ahorra a un buscador tonto en problemas
nuevos.** No hace falta opinar si lo descubierto es "interesante": o sirve para lograr cosas, o no.

Más adelante, con el mismo aparato: sacarle a la guía una afirmación por vez y ver cuánto empeora el
planificador. Eso da el valor de cada pieza descubierta, y es una manera mecánica de contar ideas (en la
cumbre de ARC, Wolfram dijo que no sabe cómo contarlas).

### 3.5 Los controles

- **Rivales sin IA, corridos antes que cualquier modelo.** Para lograr los objetivos directamente: un
  solucionador de restricciones (SAT), búsqueda evolutiva y búsqueda al azar. Para armar la guía: un
  catalogador mecánico (tirar símbolos al azar, quedarse con lo que sobrevive, chocar todo con todo).
  Si los rivales alcanzan, el mundo no sirve.
- **La guía nuestra.** Si el planificador con la guía completa no logra todos los objetivos, el mundo está
  mal armado.
- **La idea nombrada.** Se le da a la IA el catálogo de partículas (sin los choques) y se ve si con eso
  alcanza.
- **El modo directo.** La IA resuelve ella misma los objetivos, con y sin catálogo. Dice dónde está el
  cuello: en descubrir los objetos o en combinarlos.
- **"Imposible" con certificado.** Algunos objetivos no tienen solución dentro de los límites, comprobado
  por enumeración completa. Se permite contestar "no encontré"; no se lo cuenta como "imposible".
- **Nada de filtrar después.** El generador se calibra en mundos de desarrollo, se congela, y se informan
  todos los mundos de prueba, también los que un rival resolvió.
- **Mundos que nadie plantó**, más adelante: reglas sorteadas y filtradas por tener partículas. Sirven para
  comprobar que el resultado no depende de nuestra manera de plantar.

### 3.6 Qué tiene de lo que pidió Lucas, y qué no

| Lo que pidió | Cómo queda |
|---|---|
| Elegir nosotros el fenómeno oculto | Sí: elegimos qué partículas existen y qué pasa cuando chocan |
| Que no venga de sistemas ya conocidos | La regla se sortea alrededor de lo plantado; no está en ningún libro |
| Sin disfraces | La regla va a la vista, sin renombrar nada |
| Que no sea de juguete (sumas, multiplicaciones) | Lo oculto son objetos y choques en un autómata, no una cuenta |
| Sistemas como los de Wolfram, con reglas arbitrarias | A medias: parte de la tabla la fijamos nosotros y el resto es al azar. Los mundos que nadie plantó quedan para una segunda etapa |
| Verificador barato | Sí: todo se comprueba corriendo el mundo decenas de pasos |
| Saber cuándo y en qué situaciones descubre | Es lo que se puede variar: cuántas cosas hay, a qué profundidad, cuánto presupuesto, qué pista |
| Algo revolucionario | **No lo puedo prometer.** Ver §3.7 |

### 3.7 Qué sería nuevo, y con qué confianza

Según lo buscado (unas 150 búsquedas, casi todo resúmenes; no alcanza para decir "nadie lo hizo"):

- **Puntuar lo que un explorador deja escrito por cuánto le ahorra a un resolvedor mecánico.** Era el hueco
  que nuestra propuesta del 15-nov ya había anotado (§8.5) y no apareció en estas búsquedas. Lo vecino usa
  un juez LLM o deja que el propio modelo vuelva a razonar ante cada pregunta.
- **Falso descubrimiento contado exacto** en un agente que explora. El banco de ARIA, por ejemplo, declara
  que no penaliza las reglas equivocadas.
- **Mundos con objetos plantados y agentes como analistas.** Con sistemas armados a propósito solo apareció
  un caso, sobre redes neuronales y con juez.

Lo que **no** es nuevo y no hay que vender: encontrar partículas en autómatas (búsqueda de naves en el
Juego de la Vida, décadas); elegir condiciones iniciales para lograr un resultado (ya se hace con
solucionadores de restricciones; Codex abrió dos fuentes); representaciones predictivas mínimas (estados
causales, bisimulación); explorar y después rendir examen (WorldTest). Y es hacia donde, de segunda mano,
apuntaba ARC para medir invención: puntuar si lo que la IA inventa acelera lo que sigue.

### 3.8 Qué mide y qué no (el nombre honesto)

Mide: **cuándo un agente convierte la exploración de un mundo nuevo en una descripción compacta, cierta y
que sirve.** Los dos críticos piden no poner todavía "creatividad" ni "descubrimiento científico" en un
titular, y tienen razón.

Deja afuera: elegir el problema; inventar el aparato de medida; el caso en que la regla está escondida; y
si la IA "tuvo una idea" o buscó con orden. Buscar con orden usando objetos ya es usar la física de ese
mundo; no hay forma mecánica de separar las dos cosas.

## 4. Por qué esta y no las otras

| Candidata | Qué era | Veredicto de los críticos | Qué queda |
|---|---|---|---|
| C1. Relojes escondidos | Predecir un fenómeno que nunca ocurre en lo que la IA puede correr | Los dos esperan que el mejor modelo lo resuelva a dos o tres niveles. La dificultad no es la cantidad de niveles sino que estén enganchados; perder modularidad ya es descompilar | [Nota guardada](../notes/2026-11-16-designed-programs-idea.md). Vale como prueba de descarte barata (§6) |
| C2. Mundos salvajes | Reglas que nadie diseñó; verdad a fuerza bruta | Afuera: un éxito puede ser más cómputo; un fracaso no distingue "no hay" de "no encontró" | Los mundos no plantados vuelven, pero con artefactos que se comprueban solos (§3.5) |
| C3. Disfraces más hondos | Seguir la línea de ayer | Afuera: carrera de ofuscación | Cerrada |
| C4. Que el juego lo arme otra IA | Diseñadora + pista corta | Sirve para fabricar candidatos, no como experimento. Medido en otros: lo difícil colapsa en hashes | En espera |
| C5. Explorar y examen sorpresa | Sin pregunta, después examen | Demasiado cerca de WorldTest salvo que se exija comprometer una teoría ejecutable antes | **Es la base de la propuesta, con esa corrección** |
| C6. Contar ideas por transferencia | Lo que abarata el mundo siguiente | Necesita antes un mundo con margen | Queda como "sacar una pieza por vez" (§3.4) |
| C7. Redescubrir lo posterior al corte | La asimetría es el tiempo | Validación final, no instrumento | En espera |
| C8. Sondas por bifurcación | Clonar la conversación y examinar al clon | Mide lo que puede resolver al preguntarle, no lo que ya sabía. Es un instrumento, no un fenómeno | En espera, para cuando haya un mundo con margen |
| "Hacé que pase" (síntesis mía de la segunda vuelta) | Entregar una fila que produzca un resultado | Como juego aislado no sobrevive todavía a un solucionador de restricciones; una fila correcta no dice de dónde salió | **Pasa a ser el examen oculto** |
| "Experimento crucial" (mía) | Fila donde dos mundos casi iguales difieren | Es probar programas contra mutantes en un sistema dinámico; con dos tablas a la vista, se resuelve escribiendo el trío distinto | Control, no juego principal |
| Partícula certificada (Astra) | Entregar un dibujo que viaje | Elegante: un ciclo certifica para siempre. Sola, la barre una búsqueda | **Es el primer tipo de afirmación de la guía** |
| Teoría en una botella (Codex) | Programa corto entregado antes de las preguntas | El mejor constructo; pide diseñar un lenguaje | **Es la guía de campo**, con un formato de dos tipos de afirmación en vez de un lenguaje general |
| Experimento decisivo (los dos, por separado) | Protocolo que distingue varios mecanismos | Mide producir información; otra habilidad | Anotado como juego siguiente posible |

Los tres llegamos al mismo armado por caminos distintos. Astra, segunda vuelta: "conservaría partículas
certificadas como base y 'hacé que pase' como examen posterior; después pediría que el catálogo producido
resuelva objetivos retenidos sin volver a consultar al modelo". Codex, segunda vuelta: "el agente explora
el mundo y congela un catálogo ejecutable; después se le retira y un planificador fijo usa ese artefacto
para resolver varios objetivos ocultos". Que coincidan no prueba que funcione.

## 5. Qué la mata (escrito antes de construir)

Tabla de Codex, que adopto. Se arma primero el mundo y se corren los rivales **sin gastar API**.

| Si pasa esto | Quiere decir | Qué se hace |
|---|---|---|
| El solucionador de restricciones o la cartera de buscadores logra 3 de 4 objetivos de choque | El mundo está barrido a esa escala | No se corre ningún modelo. Se agranda una vez; si sigue, se cierra |
| El planificador con nuestra guía completa no logra los 4 | La física plantada no alcanza para los objetivos | Mundo inválido: se rearma |
| El modelo falla alguno de los 2 objetivos directos (una sola partícula) | Piso, o el arnés está roto | Se arregla antes de leer nada |
| Sin pista logra 2 o más de 4 choques (al menos uno por mundo) y los rivales ninguno | El mundo sirve | Repetir en mundos frescos. No afirmar "entendió" |
| Sin pista logra 1 o menos; con el catálogo, 3 o más | El cuello está en descubrir o representar los objetos | Pasar al modo guía (§3.3) |
| Sin pista 1 o menos y con catálogo 2 o menos | Piso | Abandonar esa configuración |
| Todos resuelven todo | Techo | El juego no discrimina: se cierra con ese resultado escrito |

Lo que la mata como trabajo publicable: que un buscador mecánico iguale o supere a los agentes en todos los
tamaños. Eso también sería un resultado ("la búsqueda por restricciones elimina la aparente ventaja"), pero
solo con muchos mundos; dos mundos son una prueba de descarte, no un trabajo.

## 6. Primer paso (nada se hace sin el OK de Lucas)

**Etapa 1, sin API, dos o tres días de armado.** Dos mundos plantados chicos (radio 1; cuatro a ocho
símbolos, lo que el generador necesite; fondo quieto; tres partículas y dos choques encadenables cada uno).
Verificador. Tres rivales: solucionador de restricciones, búsqueda evolutiva y planificador con nuestra
guía. Cuatro objetivos por mundo: una partícula sola, un choque, dos choques, y uno imposible con
certificado. Se leen las dos primeras filas de la tabla de §5. Corte duro: si en tres días no hay dos
mundos que pasen, se para.

**Etapa 2, solo si la etapa 1 pasa: doce partidas, un modelo, tope 20 dólares.** Modo directo: ocho partidas
sin ayuda y las cuatro de choque repetidas con el catálogo de partículas. Reglas de lectura: las de §5,
copiadas a `rules.md` antes de correr.

**Etapa 3, solo si la etapa 2 da margen:** el modo guía completo (§3.3–§3.4), varias corridas por mundo y
mundos frescos.

**Aparte y opcional, unos 3 dólares:** tres pares de "relojes" (C1), porque los dos críticos lo ven como una
prueba de descarte barata y reusa el arnés de ayer. Predicción escrita de antemano: el mejor modelo los
resuelve.

## 7. Trabajo previo más cercano

Detalle y niveles de lectura en [el registro de las tres búsquedas](../readings/2026-11-16-prior-work-three-searches.md)
y en las respuestas de Codex.

| Trabajo | Qué hace | Qué le falta respecto de esto | Quién lo leyó y cómo |
|---|---|---|---|
| WorldTest / AutumnBench, [arXiv:2510.19788](https://arxiv.org/abs/2510.19788) | Explorar sin objetivo y después rendir examen | El examen lo contesta el propio modelo; mundos escritos a mano | Codex, fuente primaria; lector, texto vía herramienta |
| Wagner, "Synthesizing Initial Configurations for Cellular Automata" | Encuentra condiciones iniciales con un solucionador (Alloy) | No hay agente; es el rival | Codex, fuente primaria |
| Bagnoli et al., [arXiv:2504.03691](https://arxiv.org/abs/2504.03691) | Control de autómatas 1D como problema SAT | Ídem | Codex, fuente primaria |
| Eppstein, [arXiv:cs/0004003](https://arxiv.org/abs/cs/0004003) | Búsqueda estructurada de naves | Ídem: "el tamaño bruto no protege el benchmark" | Codex, fuente primaria |
| REFUTE, [arXiv:2502.19414](https://arxiv.org/abs/2502.19414) | Construir la entrada donde dos programas difieren; mejor agente, menos de 9% (2025) | Programas de competencia, no mundos | Codex, fuente primaria |
| AgenticInterpBench, [arXiv:2606.24026](https://arxiv.org/abs/2606.24026) | Agentes analizando sistemas compilados desde un programa conocido | Redes neuronales; juez LLM | Lector, resumen y texto vía herramienta |
| Menaged et al., [arXiv:2606.16576](https://arxiv.org/abs/2606.16576) | Descubrir un autómata oculto preguntando; vara clásica | Regla escondida; no hay artefacto reusable | Lector, texto vía herramienta |
| Shalizi & Crutchfield, [arXiv:cond-mat/9907176](https://arxiv.org/abs/cond-mat/9907176) | Teoría de representaciones predictivas mínimas | Es el fundamento, no un banco | Codex, fuente primaria |
| AlphaGeometry (Trinh et al. 2024) | Genera hacia adelante y define "la idea" como lo que la solución usa y el enunciado no menciona | Geometría; resolverlo pidió un modelo especializado | Lector y Codex |
| ASAL (2024) | Modelos de visión como objetivo para buscar vida artificial | No es un agente que invierte | Codex, fuente primaria |

No se encontró una fuente primaria que sea exactamente "un LLM sintetiza partículas o configuraciones en
autómatas" (Codex), ni mundos con eventos fuera del presupuesto del agente, ni gemelos que difieran solo en
reglas que nunca se usan (lectores).

## 8. Lo que NO se verificó

- **Que el mundo se pueda armar como digo.** Plantar tres partículas y dos choques en una tabla chica puede
  no entrar; por eso el tamaño del alfabeto queda abierto. No armé ninguno.
- **Que exista la zona útil**: mundos donde el solucionador de restricciones no llegue y una guía corta sí.
  Los dos críticos la creen plausible y ninguno la da por hecha.
- **Que el mejor modelo no lo resuelva todo.** Lo más probable, por lo de ayer, es que arme el catálogo con
  barridos ordenados. Si es así, el resultado es "esto sí lo pueden" y se cierra.
- **El trabajo previo**: resúmenes y lecturas mediadas. Antes de afirmar novedad en un texto público hay que
  leer a texto completo WorldTest, las dos fuentes de control de autómatas, REFUTE y lo que salga de
  ARC-AGI-4.
- **Las cifras de otros** que cito (57,5%, 31,5%, menos de 9%, 54,3%) no las cotejé contra los PDF.
- **Los costos** son estimaciones.

## 9. Pendientes

| Estado | Pendiente | Próximo paso |
|---|---|---|
| **VIVO** | Decisión de Lucas: ¿esta línea?, ¿nombre?, ¿OK a la etapa 1 (sin API)? | Lucas |
| **VIVO** | ¿Se corre la prueba de descarte de los relojes (unos 3 dólares)? | Lucas |
| **VIVO** | Si hay OK: escribir `rules.md` con la tabla de §5 antes de armar nada | después del OK |
| **VIVO** | Leer a texto completo el trabajo previo más cercano (§8) | antes de cualquier afirmación de novedad |
| **VIVO** | La página "Cómo se arma un juego" y la guía describen el plan de antes de la primera prueba | actualizar o retirar cuando haya rumbo |
| **VIVO** | En `deep-9` y `deep-25` (prueba de ayer) faltó comprobar con un programa propio que se resuelven desde lo que ve la IA. Lo señaló Astra | anotado en la lectura de ayer; pendiente si esos juegos se reusan |
