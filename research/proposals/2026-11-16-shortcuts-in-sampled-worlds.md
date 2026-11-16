# Un atajo que nadie tenía: cómo medir si una IA descubre

Premisa de investigación, 16-nov-2026. **Para que Lucas decida. No hay nada construido.** Salió de doce
vueltas con tres críticos (GPT Astra, Codex y Grok 4.3; registro completo en `research/reviews/`), de una
búsqueda bibliográfica con nueve lectores (sección 11) y de una corrección de Lucas: poner la validación en
el centro y concentrarse en cómo se fabrican los juegos.

## En cinco líneas

1. Descubrir algo sobre un mundo es encontrar un **atajo**: una forma de contestar preguntas sobre ese mundo
   gastando mucho menos que correrlo paso a paso.
2. El atajo tiene que ser **cierto**, y eso se comprueba con cuentas.
3. Y tiene que **ganarle a todo lo que no es descubrir**: correr paso a paso lo más rápido posible, las
   recetas generales y una máquina nuestra que busca atajos a ciegas, todo con el presupuesto de la IA.
4. Los mundos son reglas **sorteadas**, no dibujadas. Nos quedamos solo con las que tienen un atajo que
   nuestra máquina encontró con muchísimo más tiempo, y que ninguna receta saca.
5. Antes de cualquier IA hay una prueba que decide si esto vive: ¿cuántos mundos así existen?

---

## 1. De dónde venimos

Los días 15 y 16 probamos dos formas de preguntar.

- **Saltar adelante.** Una regla y una pregunta: ¿qué hay en tales casillas en el paso 10^18? `gpt-6-astra`
  resolvió todo lo que tenía estructura, en 25 a 112 segundos (29 partidas).
- **Un programa contra la realidad (`outrun`).** La IA entrega un programa que predice el mundo; se lo
  compara contra la regla corrida. `gpt-6-astra` y `gpt-5.4` sacaron todo bien (6 partidas).

Los programas eran chicos, rápidos y validados, pero no hubo descubrimiento:

- en el juego del rebote, la ley la habíamos escrito nosotros en la regla, y la IA la leyó;
- en el de choques, una receta general ("saltear los tramos donde nada se toca") sacaba puntaje perfecto.

Lo que sí funcionó fue la forma de medir: programa contra realidad, con tamaño y tiempo, y las "varas"
(programas nuestros contra los que se compara).

## 2. Qué es un descubrimiento, en concreto

Wolfram dice que la ciencia vive en los "bolsillos de reducibilidad": partes de un mundo donde se puede
predecir algo con poco esfuerzo, aunque el mundo entero no se pueda predecir así. Descubrir es encontrar uno.

**Un ejemplo real.** La regla elemental 146 dibuja un desorden que parece al azar. Israeli y Goldenfeld
(*Physical Review Letters*, 2004) notaron que si se agrupan las casillas de a tres, y se marca un grupo como
negro solo cuando las tres casillas están negras, los grupos siguen la regla 128, que es simplísima: un grupo
negro sigue negro solo si sus dos vecinos también lo están. Cada tres pasos del mundo es un paso de los
grupos.

- Es un **atajo**: predice algo de los grupos muy lejos en el tiempo sin correr el mundo casilla por casilla.
- Es **cierto**, y se comprueba con una cuenta finita: las 512 combinaciones posibles de 9 casillas.
- **No lo saca ninguna receta general**: hay que encontrar ese agrupamiento en particular.

Este ejemplo también muestra un problema técnico que hubo que resolver (sección 4): este atajo no dice el
color de ninguna casilla. Solo dice cosas como "este grupo no es negro-negro-negro".

## 3. Cómo se fabrica un juego (sin IA)

El problema técnico es armar mundos donde se cumplan cuatro cosas:

1. **Seguro hay un atajo útil.** Si no, que la IA falle no dice nada.
2. **No lo dibujamos nosotros.** Si no, se lee de la regla.
3. **Ninguno de los métodos rivales que ya existen lo saca con el presupuesto de la IA.** Ojo: no es "ninguna
   receta". Nuestra propia máquina es una receta que lo encuentra; la diferencia es el tiempo. Lo que se
   mide es justamente eso: si la IA llega con mucho menos.
4. **Verdad exacta** para corregir, sin jueces.

Los pasos:

**Paso 1, sortear.** Reglas de una fila, de 3 colores, cada casilla mirando a sus dos vecinas (hay 3^27, unos
7,6 billones de tablas posibles). Con un color "vacío" que se queda vacío. Nadie toca las tablas. Se agrupan
por propiedades medidas antes, que no son el atajo: cuánto se propaga un cambio chico, cuánto desorden produce,
cuánto tarda en asentarse, cuánto depende de cada vecina. Se canonizan las reglas que son la misma con los
colores renombrados o en espejo. Como alternativa, reglas de 2 colores mirando dos vecinas de cada lado.

**Paso 2, la máquina de bolsillos (nuestra, con mucho cómputo).** Para cada regla busca, con comprobante
finito: cantidades que se conservan (álgebra lineal exacta), agrupamientos exactos como el de la 146
(búsqueda al estilo de Song y Grochow, hacia reglas no triviales) y zonas que se repiten con partículas que
viajan sobre ellas (autómatas). Registra cuánto le costó encontrar cada cosa.

**Paso 3, convertir el bolsillo en un predictor y quedarse solo con lo útil.** Un comprobante prueba que la
propiedad vale; no prueba que sirva para predecir. Por eso, con cada bolsillo armamos un **predictor testigo**:
un programa que contesta las preguntas del juego usando ese bolsillo. **Una regla entra al juego solo si su
predictor testigo le gana a todos los rivales** en preguntas reservadas, con el presupuesto de la IA. Eso
garantiza que había algo útil para encontrar, y que lo sabemos nosotros, aunque no lo dibujamos.

**Los rivales**, congelados antes de mirar a ninguna IA. La lista que juntaron los críticos:

- simulación lo más rápida posible (bits en paralelo, compilada), y no un C cualquiera;
- recortar lo que está fuera del alcance de la señal (el "cono": lo que una casilla puede influir en T pasos);
- fondos que no cambian, colores que, una vez puestos, ya no se van, detección de repeticiones en anillos
  finitos;
- guardar bloques ya calculados para no recalcularlos (hashlife), simulación por eventos;
- reglas lineales, también con los colores renombrados; palabras que nunca pueden aparecer (grafos de De
  Bruijn);
- búsquedas generales con SAT, compresión del espacio-tiempo para predecir por repetición, búsqueda genética
  de programas;
- y nuestra propia máquina de bolsillos, con el presupuesto de la IA.

**La dificultad** de cada juego es lo que le cuesta a nuestro repertorio encontrar el bolsillo (el mejor de
varios buscadores), más el tamaño del comprobante y cuánta información da. No es una dificultad "intrínseca":
depende de nuestros buscadores, y así se la nombra.

## 4. Cómo se responde: conjuntos, no casillas

**El problema.** La primera idea era que el programa dijera el color de las casillas de las que está seguro
y dejara las demás en blanco. Los críticos encontraron dos fallas. Muchos bolsillos no fijan casillas (el de la
146 solo dice "no es negro-negro-negro"). Y con un puntaje de "+1 si acierta, −10 si se equivoca" conviene
apostar cuando uno está 91% seguro, lo que premia apostar bien, no saber.

**El arreglo (de Codex).** La pregunta es: "en el paso T, en estas 5 casillas, ¿qué puede haber?". Con 3
colores hay 3^5 = 243 posibilidades. El programa contesta con **la lista de posibilidades que no descarta**.

- Si la verdad está en la lista, ganó información: cuantas más posibilidades descartó, más. En bits:
  log2(243 / tamaño de la lista). Si contesta las 243, ganó cero. Si contesta una sola, ganó el máximo.
- Si la verdad no está en la lista, es un error. **El puntaje principal exige cero errores.**

Esto junta todo en una sola regla: una casilla conocida descarta muchas posibilidades; "no es
negro-negro-negro" descarta algunas; un agrupamiento, una cantidad que se conserva o una partícula que viaja
descartan las que no son compatibles. Y no delata qué patrón buscar.

**Lo que se mide** es la diferencia contra el mejor rival en la misma pregunta: si el rival deja 40
posibilidades y la IA 5, la IA ganó log2(40/5) = 3 bits que el rival no tenía. Esa diferencia no depende de
ninguna elección arbitraria. Se informan aparte la cobertura (en qué fracción de preguntas descarta algo) y
los errores.

## 5. La partida (formato `outrun`)

- La IA recibe la regla, un simulador y un presupuesto fijo y declarado: ejecuciones, tiempo de CPU, memoria,
  sin cómputo escondido entre llamadas.
- Entrega un programa: dado un comienzo, un paso T y una ventana, devuelve la lista de posibilidades.
- Se lo prueba en comienzos, pasos y ventanas que no vio, con la verdad calculada por nosotros con dos
  simuladores independientes. T se elige para que ningún rival lo resuelva con el presupuesto, pero nosotros sí
  podamos calcular la verdad sin apuro. También tiempos cortos y medianos, para no dejar afuera los atajos que
  valen un rato y después no.
- Se reusa lo de `outrun`: la realidad en C, el corrector y la caja cerrada donde corre el código.

## 6. Por qué esto es medir descubrimiento en el sentido de Wolfram

Citas textuales de "Can AI Solve Science?" (2024), comprobadas contra el ensayo completo bajado de su sitio:

- «whenever there's overall computational irreducibility, there are also an infinite number of pockets of
  computational reducibility». **El juego mide exactamente eso**: cuánto del futuro predice un atajo cierto,
  con poco cómputo.
- «We can, for example, enumerate possible computational systems or processes, and see "fundamental
  surprises"». **Nuestra máquina de bolsillos es esa enumeración**, como fábrica y como rival.
- «AI has the potential to give us streamlined ways to find certain kinds of pockets of computational
  reducibility». **Es lo que se pone a prueba**: si la IA encuentra con poco presupuesto lo que la enumeración
  encuentra con mucho.

La idea de que un hallazgo vale el cómputo que ahorra tiene un antecedente: Bennett (1988) definió el valor de
un mensaje como «the amount of mathematical or other work plausibly done by its originator, which its
receiver is saved from having to repeat».

## 7. Qué se busca (fijado antes de mirar)

**Pregunta principal.** En mundos sorteados donde nuestra máquina encontró un bolsillo útil con muchísimo
cómputo, ¿hasta qué costo de descubrimiento llega la IA con un presupuesto mucho menor, y cuántos bits le saca
al mejor rival?

| Si sale | Qué quiere decir |
|---|---|
| La IA llega a bolsillos caros para la máquina | Encuentra con ideas lo que la enumeración encuentra con fuerza bruta |
| Solo llega a los baratos | Su ventaja es implementar bien recetas conocidas |
| Encuentra bolsillos que la máquina no tenía | El bolsillo nuevo se verifica y se suma al catálogo |
| No le gana al rival en nada | En estos mundos no hay descubrimiento que medir con estas IAs |

Es una medida de **eficiencia para encontrar bolsillos de clases conocidas**. No mide la invención de clases
nuevas de bolsillo. Si la IA trae un bolsillo de otra clase y gana bits, se ve igual, pero no es lo que el
diseño garantiza.

## 8. Lo que creo que va a pasar

- **Habrá pocos mundos útiles.** Astra estima menos de 1% de las reglas sorteadas; Codex, mucho menos (menos de
  uno en un millón, sin estratos). Por eso el paso 1 estratifica, y se guarda una rama sin estratos como
  control.
- **Los atajos para el mundo entero son raros y chicos.** En las búsquedas exhaustivas sobre máquinas de
  Turing chicas, 122 algoritmos de 3.414, y 1,23 veces más rápidos en promedio.
- **Qué hará la mejor IA** (predicción de Codex, que comparto): bolsillos chicos y visibles, entre 60 y 90%;
  los que exigen combinar un buscador con un verificador, entre 20 y 40%; agrupamientos grandes o partículas
  sobre fondos que no se ven, menos de 10%. Astra agrega que primero va a ganar por simulación optimizada, y que
  buena parte del juego será elegir qué búsqueda conviene correr.
- **En las 16 reglas elementales sin agrupamiento conocido** (la 30, la 45, la 106, la 154 y sus simétricas):
  nada nuevo (90%). Quedan como apuesta lateral.

## 9. El piloto sin IA, que decide si esto vive

1. Congelar distribuciones, hardware y lista de rivales.
2. Sortear unas 3.000 reglas de 3 colores de una mezcla de estratos publicada.
3. Darle a la máquina de bolsillos un minuto por regla (unas 50 horas de CPU), y más a las prometedoras.
4. Armar los predictores testigo y enfrentarlos a todos los rivales en preguntas reservadas, en tiempos
   cortos, medianos y largos.
5. Confirmar lo seleccionado en un segundo conjunto de preguntas.
6. Reproducir lo conocido para calibrar: Israeli–Goldenfeld, Song–Grochow, la regla 184 (se conserva la
   cantidad de autos), las zonas y partículas de la 18 y la 54.

**Vive si** aparecen al menos 30 mundos útiles, de al menos 3 estratos y 2 clases de bolsillo, donde el mejor
rival recupera menos de un cuarto de los bits del predictor testigo.

**Muere, en esta forma, si:**

- no aparece ningún mundo útil entre 3.000 (eso deja la tasa por debajo de 0,1%, con 95% de confianza), o
  menos de 20 entre 100.000;
- más del 80% de la ventaja viene de cosas triviales (fondos congelados, el vacío);
- los rivales recuperan más del 80% de la información del predictor testigo;
- la máquina no reproduce lo conocido (el instrumento está roto).

Recién si vive se mide el costo con una tanda mínima de IA y se juega: unos 10 mundos útiles, `gpt-6-astra` y
`gpt-5.4`, varias corridas por mundo.

## 10. Lo que queda para después

- **Transmisión.** Si otros (IAs o personas) pueden entender y usar lo encontrado. Toca una preocupación
  textual de Wolfram: que los bolsillos de una IA queden en un «"interconcept space"—unable to create what we
  would consider a useful scientific narrative». El diseño (lectores de varias familias, cruzar quién descubre
  con quién explica) está en las vueltas 10 y 11 de los críticos.
- **El blanco abierto** de las 16 reglas elementales, con presupuesto tope.
- **Otras familias** de programas simples, para ver si lo que salga vale más allá de los autómatas de una fila.

## 11. Trabajo previo y qué sería nuevo

Nueve lectores; las notas están en `scratch/deep-research/`. El tope de búsquedas web de la sesión se agotó a
mitad del trabajo, así que algunas líneas quedaron sin buscar; se marcan en las notas.

- **Agentes con verificador sobre programas simples ya existen.** DeepMind (octubre de 2026) puso agentes con
  pruebas en Lean sobre las 1.094 máquinas de Busy Beaver de 6 estados sin resolver: 26 verificadas, 11 nuevas,
  cuyo comportamiento depende de un problema matemático abierto; no decidieron ninguna máquina, y no informan
  costo ni rival sin IA. El premio de la regla 30 para agentes (Wolfram Institute; primera entrega el 20 de
  octubre de 2026) tiene 366 entregas, 363 verificadas en Lean, todas resultados parciales, ningún premio; sus
  instrucciones dicen que mucho de lo que encuentran los agentes ya se sabía.
- **Medir con pruebas formales y gasto existe en matemática.** OEIS Open (2026): con Lean como juez, la tasa de
  resolución sube unos 10 puntos cada vez que se multiplica por diez el gasto, sin techo hasta 200 dólares por
  conjetura; las generaciones nuevas mejoran solo unos puntos.
- **Contra rivales clásicos, la evidencia es mixta.** Muestreos simples empatan con evolución de código en 6 de
  9 problemas de AlphaEvolve con igual presupuesto; un agente usa 23,5% más consultas que el algoritmo clásico
  para aprender un autómata oculto.
- **Programas cortos que reproducen datos** (KoLMogorov Test): más del 95% de los aciertos en datos reales son
  copias de la entrada. Mide tamaño, no atajos de tiempo.
- **Agrupamientos exactos:** Israeli y Goldenfeld (2004, 2006), Song y Grochow (2020, exhaustivo hasta grupos de
  7 entre reglas elementales).
- **"Descubrimientos" de IA corregidos:** varios anuncios resultaron conocidos (GPT-5 y problemas de Erdős;
  GNoME). Es la razón de comparar siempre contra rivales.
- **En el Juego de la Vida** no hay ningún resultado reconocido por la comunidad atribuido a una IA; los
  hallazgos humanos tardaron de un mes a casi 50 años.

Lo que no apareció: una IA buscando atajos en reglas nunca estudiadas, corregida con cuentas exactas, contra
una búsqueda sistemática optimizada con el mismo presupuesto. Un lector lo buscó con 10 búsquedas distintas,
más 6 anteriores. No digo "nadie lo hizo" hasta leer completos los trabajos más cercanos.

## 12. Límites

- Mide eficiencia para encontrar bolsillos de clases conocidas en programas simples. Deja afuera leyes
  estadísticas o aproximadas y la invención de clases nuevas.
- Elegir qué mundos entran (los que nuestra máquina sabe reconocer) moldea la población: no dibuja el atajo,
  pero elige sus familias. Por eso la rama de control sin estratos.
- "Le gana a los rivales" es relativo a la lista que armamos. Una buena lista es parte del trabajo.
- No dice nada sobre si la irreducibilidad pone un límite a la inteligencia. Dice qué atajos encuentran
  observadores concretos, con presupuestos concretos.
- Los críticos coinciden en que esto solo no es de primer nivel por su forma. Lo sería con un atajo nuevo en
  una regla clásica, auditado por especialistas, o con un resultado amplio y repetido sobre cuándo la IA le
  gana a la búsqueda sistemática.

## 13. Lo que tiene que decidir Lucas

1. Si se arma el piloto sin IA de la sección 9.
2. Si vive: medir el costo con una tanda mínima y jugar con IA.
