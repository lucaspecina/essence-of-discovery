# Críticos, vuelta 12 (16-nov-2026): el diseño técnico de los juegos

Lucas pidió dejar las ramas y concentrarse en cómo se fabrican los juegos para que la IA tenga que escribir
programas que descubran los patrones. Se les mandó el diseño técnico a GPT Astra, Codex y Grok 4.3. Abajo, el
pedido y las tres respuestas completas, sin tocar. Arriba, el resumen.

## Resumen

**Veredicto de los tres:** no se puede jugar todavía con IA; sí se puede armar el piloto sin IA, que es el que
decide.

- **El requisito "ninguna receta general lo saca" contradice el diseño**: nuestra propia máquina de bolsillos
  es una receta que lo saca. Se reescribe: ningún método del repertorio rival congelado lo saca con el
  presupuesto de la IA. Se mide ventaja de búsqueda.
- **Invertir el filtro (Astra):** una regla entra solo si el bolsillo se convierte en un predictor que le gana
  a todos los rivales en preguntas reservadas. El comprobante prueba la propiedad; el predictor prueba que
  sirve.
- **Responder con conjuntos, no casillas (Codex):** el programa devuelve las posibilidades que no descarta para
  una ventana chica en el paso T; vale log2(total / tamaño de la lista) bits si la verdad está adentro, y es
  error si no. Junta casillas, "no es 111", agrupamientos y conteos. Astra: no hay bits sin una referencia;
  la diferencia contra el rival en la misma pregunta no depende de ella.
- **El puntaje +1 / −10 premia apostar, no saber** (conviene con 91% de confianza). Cobertura y errores, por
  separado.
- **Faltaban muchos rivales:** simulación en paralelo de bits, recorte del cono, fondos fijos, detección de
  ciclos, hashlife, lineales con colores renombrados, palabras imposibles (De Bruijn), SAT, compresión del
  espacio-tiempo, síntesis de programas. Calibrar el tiempo contra el mejor rival, no contra un C cualquiera.
- **Rinde muy poco sortear al azar:** Astra estima menos de 1% de mundos útiles; Codex, menos de uno en un
  millón. Reglas de 3 colores, con un color vacío, estratificadas por propiedades medidas antes; canonizar
  renombres y espejos; dejar una rama sin estratos como control.
- **"Costo de nuestra máquina" no es dificultad intrínseca:** depende del algoritmo (Song y Grochow cambiaron
  radicalmente ese costo sin cambiar los bolsillos). Usar el mejor de varios buscadores, más tamaño del
  comprobante e información.
- **Predicciones para la mejor IA (Codex):** bolsillos chicos y visibles, 60 a 90%; los que exigen combinar
  buscador y verificador, 20 a 40%; agrupamientos grandes o partículas sobre fondos que no se ven, menos de 10%.
- **Piloto y muerte:** 3.000 reglas con un minuto de búsqueda cada una (Astra) o 100.000 con filtro barato
  (Codex). Vive con al menos 30 mundos útiles de 3 estratos y 2 clases, donde el mejor rival recupera menos de
  un cuarto de los bits. Muere con cero útiles en 3.000, menos de 20 en 100.000, ventaja casi toda trivial, o
  rivales que recuperan más del 80%.
- Grok cuenta mal el espacio de reglas (dice 3^9 para 3 colores y radio 1; son 3^27 tablas); su estimación de
  rendimiento se apoya en ese error.

**Qué decidí con esto.** La premisa (`research/proposals/2026-11-16-shortcuts-in-sampled-worlds.md`) queda con
el requisito reescrito, el filtro invertido, las respuestas por conjuntos, la lista de rivales y el piloto sin
IA con sus números de vida y muerte.

---

## Pedido de la vuelta 12

### Duodécima consulta — el diseño técnico de los juegos

Lucas pidió dejar las ramas (transmisión, filosofía) y centrarse en lo técnico: **cómo crear juegos en los que
la IA tenga que escribir programas que descubran los patrones**. Atacá este diseño técnico: dónde se rompe, qué
va a pasar, cómo se arregla. Sin halagos. [Dato] / [Literatura (de memoria o comprobada)] / [Juicio]. Castellano
llano. Hasta 1.300 palabras. Si ves un diseño técnico mejor para lo mismo, decilo.

#### Requisitos (los cuatro que salieron de todo lo anterior)

1. En el mundo **seguro hay un patrón** (para que fallar se pueda leer).
2. **No lo dibujamos** (si no, se lee de la regla).
3. **Ninguna receta general lo saca** (si no, se resume sin entender).
4. **Verdad exacta** para corregir, sin jueces.

#### El diseño

**Paso 1, sortear.** Reglas de una fila, radio 1, 3 o 4 colores, sorteadas en masa, por estratos de actividad
declarados. Nadie toca las tablas.

**Paso 2, la máquina de bolsillos (offline, mucho cómputo nuestro).** Para cada regla: (a) cantidades
conservadas de rango r (álgebra lineal exacta); (b) proyecciones exactas por bloques de N casillas hacia
reglas no triviales (búsqueda tipo Song–Grochow, con destinos sobreyectivos o al menos no constantes); (c)
dominios regulares invariantes y partículas sobre ellos (autómatas). Todo lo encontrado viene con comprobante
finito. Se registra el costo de encontrar cada bolsillo.

**Paso 3, filtrar.** Se quedan los mundos donde la máquina encontró un bolsillo no trivial y las recetas
generales (correr paso a paso, saltear tramos sin choques, detectar repeticiones, guardar bloques ya
calculados al estilo hashlife, resolver reglas lineales) no lo aprovechan en las preguntas del paso 4.

**Paso 4, la partida (formato outrun).** La IA recibe la regla, un simulador y un presupuesto (ejecuciones,
tiempo). Entrega `predict(start, T)`: devuelve, para el estado en el paso T, el color de las casillas de las que
está segura y "en blanco" en las demás. Comienzos y pasos T que la IA no vio; T elegido para que correr el mundo
no entre en el tope de 1 segundo por llamada, pero nosotros sí calculamos la verdad en C. Puntaje: casillas
acertadas, y cada casilla equivocada resta mucho (por ejemplo, 10 veces), o se exige cero errores. Tope de
tamaño del archivo.

**Por qué el paso 4 no delata el patrón.** No se dice qué buscar. Cualquier bolsillo se convierte en casillas
predichas: zonas de fondo periódico, partículas que viajan hasta chocar, regiones que se congelan, reglas
lineales. El "tamaño del bolsillo" es cuántas casillas del futuro lejano predice sin error.

**Dificultad.** El costo que le llevó a nuestra máquina encontrar el bolsillo (de segundos a días). Pregunta
principal: ¿hasta qué costo de máquina llega la IA con un presupuesto mucho menor?

**Varas.** Recetas generales (piso), y el predictor armado con el bolsillo de nuestra máquina (prueba de que se
podía, y cota inferior de lo que se puede acertar).

#### Dudas que ya tengo

- Algunos bolsillos no se traducen en casillas: el agrupamiento de la regla 146 (bloques de tres, negro solo si
  los tres son negros) solo dice "este bloque no es 111" para casi todos los bloques; eso no fija ninguna
  casilla. ¿Se agregan respuestas sobre bloques o conteos (por ejemplo, "en la ventana tal hay n casillas de
  color a")? ¿Cómo se puntúa sin volverlo arbitrario? ¿Bits de información acertados?
- ¿Cuántas reglas sorteadas de 3 o 4 colores tienen bolsillos no triviales que las recetas no sacan? Si son muy
  pocas, el paso 3 se queda sin mundos.
- La máquina encuentra bolsillos chicos (bloques chicos, rangos chicos). Si la IA solo puede encontrar los que
  encuentra la máquina, ¿la medida es solo "velocidad para encontrar lo mismo"? ¿Está bien eso?
- ¿Las preguntas en un paso T lejano dejan afuera bolsillos que solo valen un tiempo (transitorios)?

#### Preguntas

1. ¿Los cuatro pasos cumplen los cuatro requisitos? ¿Cuál se cae primero?
2. El formato "predecí las casillas que puedas, el resto en blanco": ¿es sano? ¿Cómo se lo infla sin
   descubrir? ¿Qué recetas generales le faltan a la lista?
3. Bolsillos que no son casillas: ¿cómo se incluyen sin delatar ni volver arbitrario el puntaje?
4. ¿Qué espacio de reglas y qué estratos maximizan los mundos útiles? Predecí la fracción.
5. La dificultad como "costo de nuestra máquina": ¿es una buena escala? ¿Qué la rompe?
6. ¿Qué va a pasar cuando juegue `gpt-6-astra`? Predecí.
7. El piloto sin IA mínimo que decide si esto vive, y qué número lo mata.

---

## Vuelta 12 — respuesta de Astra

#### 1. Qué requisito se cae

[Dato] **El 3, tomado literalmente, ya está contradicho por el paso 2:** vuestra máquina es una receta general que encuentra los bolsillos seleccionados. Además, simular siempre resuelve las preguntas finitas; lo que falta es presupuesto.

[Juicio] Reformulalo: **«ninguna receta del repertorio declarado logra suficiente rendimiento dentro del presupuesto»**. Eso es medible; «ninguna receta general» no.

[Dato] El requisito 1 tampoco está asegurado en la tarea: tener una conservación o una proyección no garantiza poder predecir casillas. El ejemplo de 146 lo muestra.

[Juicio] **Invertí el filtro:** solo aceptá una regla cuando tengáis un predictor ejecutable, construido con el bolsillo, que supere a las recetas en preguntas reservadas. El certificado prueba la propiedad; el predictor prueba su utilidad.

[Dato] No tocar tablas cumple una versión estrecha del requisito 2. Filtrar sí modifica la distribución: seleccionáis mundos reconocibles por vuestra máquina. No implantáis el patrón, pero elegís sus familias.

El 4 es alcanzable para sistemas finitos. Faltan longitud, bordes, distribución de comienzos y horizontes. Contrastá dos simuladores independientes: «lo calculamos en C» no garantiza ausencia de errores.

#### 2. Casillas y blancos: sano, pero explotable

[Dato] Con premio +1 y castigo −10, conviene contestar cuando la probabilidad de acierto supera **10/11**. No mide certeza. Cero errores observados tampoco demuestra corrección fuera del conjunto probado.

[Juicio] Conservá cobertura y errores como medidas separadas. Un puntaje único permite esconder errores importantes entre aciertos baratos.

Las primeras inflaciones serán:

- Predecir siempre el color dominante o el fondo absorbente.
- Buscar comienzos fáciles, cortos, periódicos o casi vacíos.
- Explotar longitudes y tiempos con divisores favorables.
- Ganar por implementación, no por descubrimiento.
- Aprovechar trabajo entre llamadas o precálculo que el presupuesto no contabiliza.

[Juicio] Fijá CPU, memoria, paralelismo, compilación y persistencia. El tamaño del archivo no limita el trabajo que ese archivo puede hacer. Separá costo de investigación, preparación y consulta.

Faltan recetas importantes: simulación vectorizada y empaquetada en bits, reducción del cono causal, descomposición en componentes independientes, eliminación de colores inaccesibles, tratamiento de defectos sobre fondos y búsqueda de cambios de representación que vuelvan la regla lineal. Incluí también pequeñas tablas exhaustivas para anillos cortos.

**Un segundo contra vuestro C no sirve si otro simulador general tarda diez milisegundos.**

#### 3. Bolsillos que no fijan casillas

[Dato] «Este bloque no es 111» contiene información, aunque ninguna casilla quede determinada. Bajo una referencia uniforme, aporta \(\log_2(8/7)\), unos 0,193 bits. Bajo otra distribución, aporta otra cantidad. **No existen “bits acertados” sin elegir una referencia.**

[Juicio] Mejor diseño: respuestas sobre un repertorio público y acotado de observables:

- bloques pequeños;
- conteos;
- sumas de funciones locales pequeñas, para incluir conservaciones.

El predictor puede abstenerse o entregar una distribución sobre los resultados. Revelar el lenguaje de respuestas no revela qué relación vale en cada mundo.

[Literatura (de memoria)] La puntuación logarítmica es una regla de puntuación propia: incentiva declarar las probabilidades reales. Podés medir la mejora respecto de una referencia fijada antes:

\[
\log_2 P(\text{resultado})-\log_2 P_0(\text{resultado}).
\]

[Juicio] Elegí consultas al azar y con pesos publicados. No sumes como información independiente afirmaciones solapadas sobre las mismas casillas. Mantené además un carril de afirmaciones exactas, con cobertura y errores.

No permitas predicados arbitrarios y luego intentes contar sus soluciones: verificar una respuesta concreta puede ser barato y calcular su información resultar intratable. Usá formatos donde ambas cosas sean manejables.

Registrá certificados aparte. **Encontrar estructura y explotarla son dos capacidades; conviene medir ambas, no confundirlas.**

#### 4. Qué reglas y cuántas

[Dato] Para radio 1 hay \(3^{27}\) reglas de tres colores y \(4^{64}\) de cuatro. El muestreo uniforme recorre espacios enormes; aumentar colores también encarece mucho la búsqueda de proyecciones.

[Literatura (de memoria)] Los trabajos sobre conservaciones, agrupamientos y dominios regulares ofrecen herramientas, no una tasa conocida de mundos útiles bajo vuestro filtro.

[Juicio] Empezaría con tres colores. Estratificaría por:

- distribución de colores de salida;
- cantidad de fondos uniformes fijos;
- dependencia efectiva de cada vecino;
- permutatividad respecto de las entradas;
- densidad inicial de perturbaciones.

La actividad sola mezcla mecanismos distintos. Canonizá cambios de nombres de colores y reflexión para evitar duplicados.

**Mi apuesta no medida:** con comienzos mezclados y exigencia de cinco puntos porcentuales de cobertura adicional sobre el mejor rival, la fracción uniforme útil será menor del 1%; trabajaría presupuestando entre \(10^{-4}\) y \(10^{-2}\). No tengo fundamento para estrecharla.

Sobremuestrear fondos estables con perturbaciones probablemente aumente el rendimiento, pero también favorecerá precisamente las recetas de partículas que queréis superar. Conservá una rama uniforme como control.

#### 5. El costo de vuestra máquina

[Dato] Ese costo depende del algoritmo, orden de búsqueda, implementación, representación y suerte. Dos reglas equivalentes por renombrar colores pueden recibir costos diferentes.

[Juicio] Llamalo **«costo de descubrimiento de nuestro repertorio»**, no dificultad intrínseca.

Usá varios buscadores, semillas y órdenes; publicá el menor costo y su variabilidad. Separá:

1. encontrar;
2. verificar;
3. convertir en predictor;
4. responder.

La escala principal debería ser rendimiento frente a cómputo total disponible. Si la IA solo reproduce vuestra búsqueda, mediréis aceleración de descubrimiento dentro de esas familias. Es una medida válida, pero más estrecha que «entender patrones».

#### 6. Qué hará `gpt-6-astra`

[Dato] No tengo datos verificables sobre las capacidades de ese sistema.

[Juicio] Mi predicción: primero ganará por simulación optimizada y clasificación de casos fáciles; después escribirá pequeños buscadores de conservaciones y proyecciones. Si las familias se repiten, reutilizará herramientas entre mundos.

Espero más dificultad en dominios raros y colisiones que en certificados algebraicos pequeños. También espero respuestas aparentemente seguras que fallen en comienzos infrecuentes.

Si el presupuesto no se contabiliza bien, dominará la ingeniería. Si se contabiliza bien, buena parte de la prueba será **elegir qué búsqueda conviene ejecutar**, no inventar una matemática distinta.

#### 7. Piloto sin IA y criterio de muerte

[Juicio] Antes de probar modelos:

1. Cerrá distribuciones, hardware y repertorio rival.
2. Sorteá **3.000 reglas independientes** de una mezcla publicada de estratos.
3. Dales, por ejemplo, 60 segundos de búsqueda por regla: 50 horas de CPU, aparte de evaluación.
4. Construí predictores testigo para los hallazgos.
5. Evaluá en comienzos nuevos y varios horizontes: cortos, intermedios y largos.
6. Reservá un segundo conjunto para confirmar los seleccionados.

Esto último incluye transitorios: el puntaje debe mostrar una curva temporal, no solo un futuro lejano.

Definí éxito previamente: por ejemplo, cinco puntos porcentuales más de cobertura que el mejor rival, sin errores observados, dentro del segundo permitido, cuando el simulador general más rápido necesite al menos treinta segundos.

**Número que mata esa configuración: cero éxitos entre 3.000.**

[Dato] Con muestreo independiente de una distribución fija, cero éxitos deja un límite superior aproximado del 0,1% al 95% para su tasa de éxito.

[Juicio] Eso no mata todos los autómatas ni búsquedas de días. Mata esa combinación de distribución, buscadores y presupuesto. Si solo sobreviven fondos obvios o ventajas contra un simulador lento, tampoco tenéis todavía la prueba que buscáis.
---

## Vuelta 12 — respuesta de Codex

**Veredicto — [Juicio].** Como partida, **NO-GO todavía**. Como piloto offline de fabricación, sí. Se caen primero dos cosas: el requisito 3 es lógicamente incompatible con la máquina de bolsillos, y el muestreo uniforme de reglas de 3–4 colores probablemente produzca casi ningún mundo útil.

#### 1. Los cuatro pasos contra los cuatro requisitos

[Dato] El requisito 3 dice que ninguna receta general encuentra el patrón, pero el paso 2 define precisamente una receta general que lo encuentra. La diferencia es sólo de presupuesto.

[Juicio] Debe reescribirse:

> Ningún método del portafolio congelado encuentra o explota el bolsillo dentro del presupuesto del agente.

Eso mide ventaja de búsqueda, no ausencia de receta universal.

Los demás requisitos:

- **Patrón seguro:** sí, condicionado a que la máquina lo encuentre.
- **No dibujado:** parcialmente. La tabla se sortea, pero el rechazo posterior selecciona reglas compatibles con las clases de bolsillo elegidas. No dibujan la solución, pero sí esculpen la población.
- **Verdad exacta:** sí para estados finitos y certificados, si se fijan límites, fondo y condiciones de frontera.
- **Fallo legible:** sólo si el bolsillo encontrado tiene utilidad real bajo la distribución de comienzos y consultas. Un dominio de medida casi cero o una proyección de entropía mínima no produce headroom.

El mundo experimental no es sólo la regla:

\[
\text{mundo}=(\text{regla},\ \text{distribución de comienzos},\ \text{consultas},\ \text{recursos}).
\]

#### 2. “Casillas seguras”

[Juicio] El formato se infla fácilmente sin descubrir el bolsillo certificado:

- predecir fuera del cono causal;
- detectar fondos quiescentes, colores absorbentes o reglas canalizantes;
- resolver sólo bordes del cono;
- apostar al color modal cuando la penalización lo permite;
- declarar poquísimas casillas;
- usar simulación bit-paralela, GPU o JIT más rápida que la calibración;
- simplificar simbólicamente el circuito causal de cada casilla;
- precomputar potencias de la transición en líneas finitas.

Con recompensa \(+1/-10\), conviene apostar siempre que la confianza supere \(10/11\). Eso premia calibración probabilística, no necesariamente conocimiento exacto.

Faltan rivales generales:

- SAT/SMT, BDD y ejecución simbólica;
- poda del cono causal y abstract interpretation;
- grafos de De Bruijn y transductores;
- detección de reglas afines bajo permutación de colores;
- conjugaciones, simetrías, totalisticidad y dependencias unilaterales;
- binary lifting y detección de ciclos en líneas finitas;
- simulación dispersa/event-driven, RLE, macroceldas y compilación especializada;
- síntesis de programas y búsqueda genética;
- transfer matrices y meet-in-the-middle;
- predictores probabilísticos selectivos.

[Juicio] Excluyan de la puntuación las casillas causalmente triviales y calibren \(T\) contra el mejor portafolio, no contra un simulador C. En una línea periódica finita, la detección de ciclos puede liquidar el examen; en fondo infinito quiescente, sólo debería puntuarse dentro del cono causal.

#### 3. Bolsillos que no fijan casillas

[Juicio] No agregaría una colección arbitraria de preguntas. Cambiaría la salida a **predicción conjuntista sobre ventanas pequeñas**.

Para una ventana de \(w\) casillas y alfabeto \(\Sigma\), el programa devuelve un conjunto

\[
A\subseteq\Sigma^w
\]

que afirma contener el bloque futuro verdadero. Se representa como bitmask: con tres colores y \(w=5\), sólo hay \(3^5=243\) posibilidades.

Si la verdad está en \(A\):

\[
I(A)=\log_2\frac{|\Sigma|^w}{|A|}
\]

bits ganados. Si no está, la respuesta es incorrecta. Devolver todos los bloques da cero.

Esto unifica:

- casilla conocida: restringe una coordenada;
- bloque exacto: singleton;
- “no es 111”: elimina una posibilidad;
- fibra de una proyección: devuelve \(P^{-1}(y)\);
- restricciones de conteo: conjunto de bloques con ese conteo.

No revela qué patrón buscar y evita ponderaciones inventadas. Para cantidades globales usaría consultas de respuesta finita —por ejemplo, conteo en una ventana— con la misma regla: devolver un subconjunto del espacio de respuestas.

Puntuación primaria: bits correctos con **cero violaciones** en la batería oculta. Separaría una pista probabilística si quieren permitir apuestas.

#### 4. Espacio de reglas y rendimiento de la fábrica

[Dato] El espacio uniforme es brutal:

\[
|\mathcal R_3|=3^{27}\approx7.6\times10^{12},\qquad
|\mathcal R_4|=4^{64}\approx3.4\times10^{38}.
\]

Un conteo reciente encuentra sólo 144 reglas ternarias y 89.588 cuaternarias radio 1 que conservan el número bajo la codificación estándar. Son fracciones aproximadas de \(1.9\times10^{-11}\) y \(2.6\times10^{-34}\), respectivamente ([Redeker, 2026](https://arxiv.org/abs/2605.31157)). Otras cantidades de rango mayor aumentan el conjunto, pero las igualdades exactas siguen imponiendo muchas restricciones.

[Literatura — comprobada] Los dominios regulares y partículas pueden certificarse mediante autómatas, pero primero hay que inferir el lenguaje candidato; además, una sola regla puede tener múltiples dominios de medidas muy distintas ([Hanson–Crutchfield](https://sfi-edu.s3.amazonaws.com/sfi-edu/production/uploads/sfi-com/dev/uploads/filer/5d/2f/5d2f74f1-6a70-45f8-858b-d1a214b88c22/95-10-095.pdf)).

[Juicio] Mi prior:

- tabla uniforme ternaria: menos de \(10^{-6}\) de mundos sobreviven con bolsillo **útil** y brecha frente a rivales;
- cuaternaria: peor;
- reglas con bolsillo meramente formal: más, debido a ciclos uniformes y dominios microscópicos, pero deben excluirse.

Empezaría con ternarias, estado quiescente y simetría izquierda–derecha, estratificadas no sólo por actividad sino también por propagación de perturbaciones, entropía, transitorio y respuesta a semillas dispersas. Eso define una población; no dibuja un bolsillo concreto.

También probaría binaria radio 2: tabla menor, instancias frescas y más manejable que cuatro colores radio 1.

#### 5. Costo de la máquina como dificultad

[Juicio] Es una mala escala intrínseca. Mezcla:

- orden de enumeración;
- implementación y hardware;
- clase de bolsillo;
- tamaño del certificado;
- simetrías no explotadas;
- suerte de encontrar temprano.

Song–Grochow sustituyeron una búsqueda doblemente exponencial por backtracking y cambiaron radicalmente esa “dificultad” sin cambiar los bolsillos ([paper](https://arxiv.org/abs/2012.12153)).

Usaría costo del **mejor portafolio congelado** como eje operacional, acompañado por tamaño mínimo del certificado, bloque/rango y contenido informativo del bolsillo. Si la IA encuentra sólo lo mismo más rápido, el resultado sigue siendo válido: mide eficiencia de descubrimiento dentro de clases conocidas. No mide invención de nuevas clases.

#### 6. Qué hará `gpt-6-astra`

[Juicio] Espero que:

- detecte casi siempre quiescencia, simetrías, afinidad evidente y dependencias unilaterales;
- escriba simulación especializada, búsqueda simbólica y quizá álgebra lineal;
- obtenga bastante puntuación de estructuras locales no registradas como “bolsillo”;
- rara vez descubra desde cero una proyección grande o un dominio regular complejo sin pista.

Predicción aproximada:

- bolsillos pequeños y visibles: 60–90%;
- bolsillos que exigen componer buscador y verificador: 20–40%;
- proyecciones grandes o partículas sobre dominios no obvios: menos de 10%.

Sin corregir el puntaje, dominarán casillas seguras por mecanismos genéricos, no los bolsillos de la fábrica.

#### 7. Piloto sin IA

[Juicio] Haría sólo ternarias al principio:

1. sortear \(10^5\) reglas entre estratos;
2. pantalla dinámica barata;
3. pasar las mejores \(10^3\)–\(10^4\) por búsquedas exactas pequeñas;
4. traducir cada bolsillo a bits conjuntistas;
5. enfrentar el oracle contra todo el portafolio general.

Para vivir, exigiría al menos:

- 30 mundos útiles;
- provenientes de tres estratos;
- al menos dos clases de bolsillo;
- oracle con información sustancial en consultas ocultas;
- mejor rival genérico recuperando menos del 25% de los bits del oracle.

Mata el diseño uniforme si de \(10^5\) reglas salen menos de 20 mundos útiles, si más del 80% del headroom proviene de congelamiento/quiescencia trivial o si el portafolio recupera más del 80% de la información del oracle.

El cambio técnico central es éste: **dejar de puntuar casillas y puntuar reducción exacta del conjunto de futuros posibles en ventanas selladas**. Sin eso, la fábrica puede encontrar buenos bolsillos y el juego medir otra cosa.

---

## Vuelta 12 — respuesta de Grok

**Respuesta técnica al diseño**

1. ¿Cumplen los cuatro requisitos?

El requisito 1 se sostiene: la máquina offline ya verificó la existencia del bolsillo con comprobante finito, así que el error de la IA es medible contra simulación exacta en C.  
El 2 también: la regla cruda no contiene el patrón dibujado; hay que extraerlo por simulación.  
El 3 es el que se rompe primero. La distinción “receta general vs descubrimiento específico” no es nítida en la práctica. Hashtlife, detección de periodicidad por bloques, resolución de sistemas lineales sobre GF(k) y muestreo de trayectorias con backtracking ya cubren la mayoría de los bolsillos chicos que la máquina encuentra (rangos ≤ 4, bloques ≤ 5). El filtro del paso 3 termina quedándose con reglas cuya reducibilidad es marginal o depende de un truco ad-hoc que ninguna receta lista explota hoy, pero que una receta ligeramente más ancha sí explotaría. El 4 se mantiene mientras el verificador sea simulación exacta, pero pierde valor si el filtro ya colapsó.

2. Formato predict(start, T) con casillas en blanco

Es el menos malo para mantener verdad exacta y penalización dura por error. Se infla de tres formas sin descubrir nada profundo:  
- Simular hasta el presupuesto y marcar solo las celdas que realmente se alcanzaron sin colisiones de hash.  
- Usar el propio hashlife de la IA para extender bloques ya vistos y declarar “seguro” cualquier celda que quede dentro de un ciclo comprobado.  
- Aplicar el método de “regiones tranquilas”: marcar como predecible todo lo que queda fuera de un cono de luz de ancho 2r·T′ donde T′ es el tiempo simulado.  

Recetas generales que faltan en la lista:  
- Análisis de autómatas lineales sobre anillos (Grochow–Song ya lo hace parcialmente).  
- Búsqueda de invariantes polinomiales de grado bajo vía SAT.  
- Compresión de trayectorias con Lempel-Ziv sobre el espacio-tiempo y predicción por repetición de diccionario.  
- Detección de partículas vía tracking de bordes y colisiones modeladas como autómatas finitos.  

Cualquiera de estas reduce el espacio de reglas “útiles” más de lo que el diseño actual contempla.

3. Bolsillos que no fijan casillas

El ejemplo de la regla 146 es correcto: el invariante “no 111” solo da una restricción, no un valor. Tres opciones realistas sin volver arbitrario el puntaje:  
- Permitir predicciones sobre bloques o conteos locales y puntuar con log-loss calibrado (información mutua entre la predicción y el ground truth). Esto sigue siendo exacto y comparable entre IAs.  
- Exigir que la IA entregue un predictor que, dado un estado parcial, complete el bloque o el conteo con probabilidad > 1−ε. El verificador mide bits de información ganados contra la distribución empírica.  
- Rechazar estos bolsillos para la versión piloto. Son interesantes, pero ensucian la métrica y no valen la pena hasta que el formato de casillas ya esté maduro.

4. Espacio de reglas y fracción esperada

Con 3 colores y radio 1 ya hay 3^9 = 19683 reglas; con 4 colores salta a ~262144. La mayoría de las de actividad media-alta (densidad 0.3–0.7, no triviales) tienen algún bolsillo chico, pero casi todos caen en las recetas generales (periodicidad local, partículas simples, o linealidad sobre subconjuntos).  

Estimación conservadora: entre 1 % y 4 % de las reglas de 3 colores sobreviven al filtro del paso 3 con un bolsillo que las recetas listadas no explotan y que la máquina encontró en menos de 10^5 operaciones. Con 4 colores la fracción baja a ~0.5–1.5 % porque aumenta el ruido. Los estratos que más rinden son los de actividad media con al menos un dominio invariante de tamaño ≥ 3 pero sin partículas estables obvias. Los de actividad muy baja o muy alta se filtran solos.

5. La escala “costo de nuestra máquina”

Es una escala útil mientras midamos costo en operaciones elementales (no en tiempo de pared). Se rompe en dos puntos:  
- Cuando la IA usa un método completamente distinto (por ejemplo, entrenamiento fino sobre trayectorias de esa regla) cuyo costo no es comparable con la búsqueda algebraica de la máquina.  
- Cuando el bolsillo depende de un truco combinatorio raro cuyo costo de descubrimiento es exponencial en el tamaño pero cuya verificación es barata; ahí la escala se vuelve discontinua.

6. Qué pasa con gpt-6-astra (o equivalente)

Va a resolver casi todos los bolsillos que nuestra máquina encontró en menos de unos minutos de cómputo, porque ya vio suficiente literatura y código de autómatas celulares para reconocer patrones de partículas y dominios invariantes por coincidencia. En las reglas donde el bolsillo requiere búsqueda exhaustiva de rango 5–6 o más de 10^7 operaciones, va a fallar o a inventar una predicción con error detectable. El resultado probable: sube mucho la vara de las recetas generales (porque el modelo las implementa implícitamente), pero no descubre bolsillos nuevos que la máquina no encontró. El experimento entonces mide principalmente “cuánto de la literatura de CA ya está dentro del modelo” más que capacidad de descubrimiento fresco.

7. Piloto mínimo sin IA que decide si el proyecto sigue

Generar 200 reglas de 3 colores filtradas por la máquina con costo < 10^6 operaciones. Aplicar las recetas generales existentes (hashlife + periodicidad + linealidad + partículas simples) y medir el accuracy máximo alcanzable en T = 200–500. Si ese accuracy ya está por encima del 85 % de las celdas en más del 60 % de las reglas, el experimento no tiene espacio para mostrar nada que no sea “mejor implementación de recetas conocidas”. Ese umbral mata el proyecto en su forma actual. Si el piso de recetas queda por debajo del 60 %, vale la pena correr una versión chica con modelos accesibles.

Diseño alternativo más limpio (si se quiere cambiar)

En lugar de pedir predicciones de casillas, pedir que la IA entregue un programa reductor verificable: un autómata o un conjunto de reglas locales que, aplicado al estado inicial, produzca el mismo resultado que la simulación original en un subconjunto de celdas o bloques, con tamaño de descripción menor que la simulación directa. El verificador ejecuta ambos en paralelo y mide la compresión efectiva. Esto evita el problema de “marcar casillas en blanco” y hace más difícil inflar sin entender. El costo de la máquina offline sigue siendo la vara, pero ahora se mide en bits de descripción del reductor encontrado.
---

