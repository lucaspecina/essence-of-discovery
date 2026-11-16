# Lo que se les mandó a los críticos (16-nov-2026)

Dos vueltas, el mismo texto para GPT Astra (por API) y para Codex. Junto con cada carta fueron adjuntos
documentos del repo (README, lecciones, de-WAGER-a-jump-ahead, la lectura de la primera prueba, la nota del
16-nov y partes de la propuesta del 15-nov); en la segunda vuelta, además, las dos respuestas de la primera.
Las respuestas están en [Astra](2026-11-16-astra-two-rounds.md) y [Codex](2026-11-16-codex-two-rounds.md).

---

# PRIMERA VUELTA


Sos un revisor externo de un proyecto de investigación chico. **Sin halagos.** Separá siempre: [Dato] (sale
del material adjunto), [Literatura] (decí si citás de memoria o con certeza) y [Juicio] (opinión tuya).
Respuesta en castellano llano, sin jerga innecesaria, lo más corta que permita ser completo.

## 1. El proyecto en diez líneas

- Pregunta: **¿se puede medir si una IA descubre?** (se le ocurre la idea, en vez de recordarla o de probar
  cosas hasta que una funciona), con juegos mínimos y **sin que otra IA haga de juez**.
- Reglas duras: el puntaje es una cuenta contra una respuesta exacta; todo mundo se verifica sin IA antes
  de mostrárselo a un modelo; se mide contra el mejor rival que no usa el truco; reglas de lectura
  escritas antes de correr; titulares con su alcance; no afirmar lo no verificado.
- Historia: SREG (nota puesta por una IA: abandonado) → WAGER (regla escondida que genera datos; cuando
  el agente fallaba había demasiadas explicaciones posibles) → desde el 15-nov, `jump-ahead`: la regla del
  sistema va **a la vista** y la pregunta es por un futuro lejísimo (paso 10^18). Paso por paso no se
  llega: hay que encontrar un atajo. Nosotros conocemos la respuesta porque armamos el juego.
- Los documentos adjuntos (README, lecciones, de-WAGER-a-jump-ahead, la lectura de la primera prueba, la
  nota del 16-nov y partes de la propuesta del 15-nov con el trabajo previo) dan el detalle.

## 2. Lo que pasó ayer (primera prueba real, 29 partidas)

Juegos: un anillo de casillas, una tabla de reglas (el símbolo nuevo depende de izquierda, propia y
derecha), la fila inicial y una pregunta por 6 casillas en el paso 10^18. El modelo tiene `run_python`
(12 ejecuciones de 30 s, un núcleo, sin red). Debajo de cada juego "con atajo" había una regla lineal
(suma de las tres vecinas módulo p) con los símbolos renombrados al azar; en los "de dos capas", una capa
de tabla sorteada con ciclo corto y encima una capa lineal empujada por la primera.

Resultado: `gpt-6-astra` resolvió **todos** los juegos con estructura plantada en 25 a 112 segundos, con
3 a 6 ejecuciones. Pasar de 5 símbolos (1 orden útil de cada 6) a 25 (1 de cada 10^21) no le costó nada:
reconstruyó la suma escondida mirando la tabla. En tres juegos de tabla sorteada (sin estructura plantada)
resolvió dos contando más rápido y en el tercero dijo "no sé" (correcto). En 29 partidas ningún modelo dio
una respuesta segura y equivocada. Modelos anteriores (`gpt-5.4`, `claude-opus-4-6`) sí tropezaron y con
la idea nombrada salieron.

Conclusión nuestra: esconder una estructura conocida cambiándole los nombres no es un examen para el mejor
modelo de hoy. Según los criterios escritos antes ("techo → se cierra"), esa forma de armar el juego queda
cerrada.

## 3. Lo que pide Lucas (el dueño del proyecto), con sus palabras

- "¿No hay forma de NOSOTROS ELEGIR QUÉ FENÓMENO OCULTO, arbitrariamente (y no de una base de datos de
  sistemas ya conocidos por todo el mundo) Y DISEÑAR UN JUEGO PARA ESO? De una manera inteligente que no
  haga tener que meter cosas raras como disfraces."
- Sobre los programas diseñados: "no está mal... mi tema es que son cosas muy de juguete: siempre jugando
  con sumas, multiplicaciones, cambios básicos. No es que va a averiguar sistemas complejos como los de
  Wolfram con reglas arbitrarias, ¿o sí?"
- "Pensemos algo muy superador. Algo que sea revolucionario realmente, algo que sea publicable por lo
  interesante, algo que nos haga descubrir de verdad si las AIs pueden descubrir y cuándo, en qué
  situaciones, y analizar y evaluar la capacidad de descubrimiento."
- Sobre "verdad calculada con una computadora más grande": "¿esa es tu idea? ¿tener una máquina más grande
  y hacer más comprobaciones? ¿No es malísimo?"

## 4. Candidatas sobre la mesa (ninguna construida ni probada)

**C1. Relojes escondidos: fenómenos que todavía no ocurrieron.** Nosotros escribimos un mecanismo como
procedimiento y lo traducimos a reglas simples que se entregan a la vista, sin renombrar nada (lista del
tipo "modo A, leo 0 → escribo 1, voy a la derecha, paso a modo B", o la tabla de un autómata). El mecanismo
tiene niveles con escalas de tiempo muy separadas. Ejemplo: una zona de 40 casillas cuenta en binario
(nivel 1); cada vez que da la vuelta —por primera vez cerca del paso 2·10^12— otra zona avanza UN paso de
una regla cualquiera, incluso una regla arbitraria o "compleja" tipo regla 30 (nivel 2); un nivel 3 se
dispara cada tantas vueltas del 2, etc. El agente puede correr unos 10^9–10^10 pasos: **nunca ve ocurrir el
nivel 2**; las reglas que lo hacen están a la vista pero no se usan en nada de lo que puede correr desde la
fila dada. Se pregunta por el paso 10^18 (unas 450.000 vueltas después). Nosotros sabemos la respuesta
porque conocemos el reloj por diseño y corremos el sistema lento esa cantidad de pasos. Controles: (a)
**pares**: dos mundos iguales salvo en una regla que nunca se usa en lo observable (idénticos en todo lo que
el agente puede correr desde la fila dada; distintos en el paso 10^18); (b) gemelo donde el nivel de arriba
no existe; (c) la idea nombrada; (d) preguntas exactas intermedias ("¿en qué paso se usa por primera vez la
regla 17?", "¿cuántas veces se usa hasta el paso T?"). Medidas: hasta qué nivel predice bien cada modelo
("horizonte de previsión", sin techo); disociación entre extrapolar lo visto y derivar del mecanismo;
tasa de respuestas seguras y falsas. Nota: el agente puede fabricar una fila chica (zonas cortas) donde
todo ocurre rápido; eso se considera un experimento legítimo e inteligente.
Dudas propias: ¿es descubrimiento o paciencia para leer reglas (ingeniería inversa)? ¿lo resuelve Astra
a cualquier profundidad que sepamos construir? ¿"de juguete"?

**C2. Mundos salvajes.** Reglas que nadie diseñó (sorteadas, o todas las máquinas chicas tipo Busy
Beaver), descartando las que resuelven los métodos conocidos; la verdad se calcula a fuerza bruta con mil o
diez mil veces más cómputo que el del agente; se pregunta por un paso que nosotros alcanzamos y él no. Si
acierta, encontró un atajo que nadie plantó. Antecedente: Zenil, Soler-Toscano & Joosten 2011. Dudas: en la
mayoría no habrá atajo; no distingue "no hay" de "no lo encontró"; ayer Astra ganó 2 de 3 contando más
rápido; a Lucas le parece una versión barata de lo de DeepMind (arXiv:2610.22603) y no deja elegir el
fenómeno.

**C3. Disfraces más hondos.** Seguir la línea de ayer con transformaciones más fuertes: cambio de
coordenadas espacial (F = G⁻¹∘S∘G con G un autómata reversible sorteado y S simple; el problema general de
conjugación es indecidible), torres de emulación. Dudas: es justo lo que Lucas rechaza ("disfraces"); lo
de ayer sugiere que Astra ve a través de lo algebraico.

**C4. Que el juego lo diseñe otra IA igual de fuerte.** Una IA diseñadora entrega generador + solucionador
exacto + una pista corta que no depende de la semilla. El juego vale solo si (i) se verifica sin IA, (ii)
un modelo fuerte sin pista falla y (iii) un modelo más débil CON la pista acierta en semillas nuevas (eso
excluye "contraseñas" criptográficas). Definición operativa: una *idea* es una pista corta, independiente
de la instancia, que cambia el resultado. Antecedentes parciales: SKATE (arXiv:2508.06111), The Token Games
(arXiv:2602.17831), Absolute Zero Reasoner. Dudas: mete IA en la fabricación y en el filtro (no en el
puntaje); ¿qué mide del que resuelve?

**C5. Explorar sin pregunta y examen sorpresa, en mundos diseñados.** El agente explora un mundo con
varios fenómenos plantados (de distinto nivel) sin que se le diga qué buscar; después rinde un examen de
preguntas exactas que no conocía. Como el mundo lo diseñamos, sabemos qué fenómeno decide cuántas preguntas
("interesante = sirve para llegar a muchas cosas", medido por diseño). Antecedentes: WorldTest/AutumnBench
(arXiv:2510.19788), "Look Before You Leap" (arXiv:2605.16143), y es hacia donde apunta ARC-AGI-4. Duda: la
familia de preguntas del examen pasa a ser el objetivo.

**C6. Contar ideas por transferencia.** Familias de mundos diseñados que comparten (o no) un mismo concepto
oculto. Una idea = lo que, una vez encontrada en el mundo A, abarata B. La matriz de ahorros entre mundos
debería recuperar la estructura de conceptos que diseñamos. Responde a "no sé cómo contar ideas" (Wolfram,
cumbre de ARC, oct-2026). Duda: necesita mundos difíciles; ruido.

**C7. Redescubrir lo que se descubrió después del corte de entrenamiento.** La asimetría es el tiempo: el
mundo ya sabe la respuesta, el modelo no. Con verificación exacta (objetos formales, máquinas Busy Beaver
resueltas en 2026, récords de construcciones). Duda: pocos ítems; curación cara; caduca.

**C8. Microscopio: sondas por bifurcación.** En cualquier mundo con fenómenos diseñados: en cada punto de
la investigación se clona la conversación del agente y al clon (que se descarta) se le toma un examen
exacto. La partida principal no se contamina. Da una línea de tiempo exacta de qué sabe el agente y cuándo:
si el saber salta (idea) o crece de a poco (búsqueda); si ya sabía lo que iba a ver antes de mirar
(el clon predice el resultado del próximo experimento) o lo aprendió mirando; a qué distancia de la idea
estaba en cada momento (clones con pistas graduadas). Con personas esto es imposible (preguntar contamina).
Dudas: el clon puede razonar en el momento con la pista que trae la pregunta; costo.

## 5. Preguntas (contestá todas, numeradas)

1. Para cada candidata (C1–C8): la objeción más fuerte, en dos o tres líneas. ¿Qué la mata?
2. **C1 en particular, y con vos mismo como sujeto**: si te dieran un mundo así (reglas a la vista, 12
   ejecuciones de 30 s de Python), ¿cómo lo atacarías paso a paso? ¿Esperás resolverlo? ¿Hasta cuántos
   niveles? ¿Qué diseño concreto de C1 creés que NO podrías resolver, y por qué (idea vs paciencia vs
   contexto)? ¿Los pares de una regla te parecen un control válido de "entendió el mecanismo"?
3. ¿"Predecir un fenómeno que nunca ocurrió en lo observable, derivándolo del mecanismo" es una
   operacionalización defendible de descubrimiento? ¿Qué deja afuera? ¿Qué trabajo previo conocés que ya
   haga esto (decí qué es de memoria)?
4. Ranking: ¿cuál o qué combinación elegirías para un trabajo publicable que diga algo nuevo sobre *cuándo
   y en qué situaciones* una IA descubre? ¿Por qué?
5. **Tus propias ideas**: proponé al menos dos diseños que no estén en la lista y que consideres mejores o
   más audaces, respetando las reglas duras (puntaje exacto, sin IA de juez, sin depender de memoria, con
   margen en la frontera, y donde nosotros elegimos o conocemos el fenómeno, o hay un verificador barato).
   Buscamos una vuelta de tuerca de verdad, no una variante.
6. ¿Qué experimento mínimo (hasta 20 dólares de API) decide entre tus dos primeras opciones?
7. La objeción de Lucas a "de juguete": ¿es válida para C1 con un sistema arbitrario en cámara lenta en el
   nivel de arriba? ¿Hay forma de que el fenómeno oculto sea rico (tipo Wolfram) y aun así conozcamos la
   respuesta exacta?
8. Si fueras Lucas mañana: un párrafo.

---

# SEGUNDA VUELTA


Mismo formato: sin halagos; [Dato] / [Literatura (decir si es de memoria)] / [Juicio]; castellano llano; corto.

## Lo que saqué de la primera vuelta (dos críticos independientes: GPT Astra por API y Codex)

Coincidencias: (1) C2 y C3 afuera. (2) C1 (relojes) probablemente esté en techo para el modelo de frontera
si es transparente: la cantidad de niveles no es la dificultad; lo serían el acoplamiento entre niveles o
perder modularidad (y eso último ya es descompilar). Vale como prueba de descarte barata. (3) Los pares
de una regla prueban "la trayectoria observada no alcanza", no "entendió". (4) Nombre honesto de C1:
"predicción derivada del mecanismo fuera del tramo observado". (5) Los dos propusieron, por separado,
que el agente entregue un **artefacto que se verifica mecánicamente** en vez de una respuesta lejana: un
objeto con certificado finito (una partícula que viaja en un autómata nuevo), un experimento que separa
mecanismos (verificado corriéndolo contra todos), o una teoría ejecutable entregada antes de conocer las
preguntas. (6) La tensión de fondo: fenómeno rico + respuesta exacta lejana + verificación barata + regla
arbitraria no se pueden tener a la vez.

Una búsqueda de trabajo previo (tres lectores, unas 115 búsquedas, casi todo resúmenes) agregó: no apareció
ningún banco con eventos fuera del presupuesto de cómputo del agente ni con mundos de varias escalas de
tiempo; sí hay margen medido en la frontera donde hay que **encontrar estructura latente interactuando**
(autómata oculto de 8–9 estados: 57,5% el mejor, arXiv:2606.16576; DiG-bench 50/70; DiscoverPhysics 50%) y
donde hay que **construir un testigo no obvio** (contraejemplos, REFUTE 2025: <9%; ingeniería inversa a
escala real, SRE-Bench: 31,5%). AlphaGeometry define mecánicamente "la idea" como la construcción auxiliar
que la demostración usa y el enunciado no menciona, generando hacia adelante y rastreando hacia atrás.
En duelos proponente–resolvedor (Token Games) lo difícil colapsa en hashes y cifrados.

## Mi diagnóstico (decime si está mal)

Todo lo que el diseñador puede **construir de manera sistemática**, un modelo de frontera lo puede
**desarmar de manera sistemática** (pasó con las sumas renombradas y las dos capas; ustedes predicen lo
mismo para los relojes). Entonces un fenómeno plantado por construcción mide competencia y disciplina de
investigación sistemática, no "ideas". La asimetría que sí existe es otra: **generar hacia adelante es
barato e invertir es caro** (AlphaGeometry). En un sistema dinámico: correr desde una condición inicial es
barato; encontrar una condición inicial que produzca un resultado dado es un problema inverso. Y su
verificación es trivial: se corre.

## Síntesis v2 (nada construido)

**Tesis.** Dejar de pedir respuestas y pedir **artefactos que se comprueban corriéndolos**.

**Juego principal: "hacé que pase".** Universo = un autómata celular 1D nuevo, con la regla a la vista,
rico en estructuras localizadas (partículas que viajan, objetos quietos, choques). Dos fuentes de
universos: (a) *minados*: reglas sorteadas y filtradas por tener partículas sobre un fondo simple (nadie
las diseñó ni las estudió); (b) *con fenómenos plantados*: se generan juntas la tabla y los diagramas
espacio-temporales de las partículas y de algunos choques (cada vecindario con salida única), y el resto
de la tabla se completa al azar. La tarea: entregar una fila inicial acotada (símbolos permitidos, hasta m
casillas no vacías) tal que a los T pasos ocurra X; o contestar "imposible". Los X salen de **muestrear
hacia adelante** con mucho cómputo nuestro (tenemos un testigo y sabemos qué objetos intermedios usa, por
eliminación uno a uno) o son imposibles por construcción (requieren un símbolo que ninguna entrada
produce). Verificación: correr T pasos y comparar. Se acepta cualquier solución, no solo el testigo.
Dificultad: cantidad de objetos auxiliares que el testigo necesita y que X no menciona. Rival obligatorio:
búsqueda al azar, evolutiva y hacia atrás, optimizadas, con el mismo cómputo que el agente; solo cuentan
las tareas que el rival no cierra. Control de la idea nombrada: darle el catálogo de partículas, o el
choque clave. Medidas: éxito y costo contra el rival; qué pista destraba; respuestas "imposible" falsas.

**Variante: "experimento crucial".** Dos universos que difieren en una sola entrada de la tabla, que solo
se usa en un evento raro (lo encontramos muestreando). Entregar una fila donde se comporten distinto
(se verifica corriendo los dos), o contestar "equivalentes" (cuando la entrada es inalcanzable por
construcción).

**Prueba de descarte aparte:** C1 con tres pares, por si sorprende.

**Lo que no se promete:** separar "idea" de "búsqueda guiada" en general. Se mide ventaja sobre el mejor
buscador mecánico, costo, generalización y qué ayuda destraba.

## Preguntas

1. ¿El diagnóstico (construcción sistemática ⇒ desarmado sistemático; la asimetría útil es generar hacia
   adelante vs invertir) es correcto? ¿Dónde falla?
2. "Hacé que pase": la objeción más fuerte. Como sujeto, ¿cómo lo atacarías? ¿Esperás que una búsqueda
   bien escrita (hacia atrás, por columnas, evolutiva, por objetos descubiertos) lo barra? ¿Qué
   propiedades del universo y de X harían que el éxito dependa de entender la "física" del universo y no
   de cómputo? ¿Existe esa zona?
3. ¿Universos minados o plantados? ¿Cuál permite una afirmación más limpia? ¿Riesgos de cada uno?
4. "Experimento crucial": ¿aporta algo sobre "hacé que pase"? Antecedentes (mutation testing, REFUTE,
   secuencias distinguidoras): ¿qué quedaría como nuevo?
5. ¿Esto es mejor, igual o peor que tu propia propuesta de la primera vuelta? Si es peor, decí por qué y
   qué conservarías.
6. Piloto de hasta 20 dólares de API y pocos días de construcción: ¿qué armarías exactamente y con qué
   reglas de lectura escritas antes?
7. Un titular honesto para un trabajo, si saliera señal. Y cuál sería el resultado nulo publicable.
