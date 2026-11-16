# Críticos, vueltas 8 a 11 (16-nov-2026): de "cuánto cómputo vale una idea" a "las tres cerraduras"

Cuatro vueltas más después del reinicio desde cero. Desde la vuelta 9 se sumó un tercer revisor de otro
laboratorio (Grok 4.3, en el mismo Azure) y, a pedido de Lucas, se les dio libertad para proponer cualquier
idea mejor. Abajo, los pedidos y las respuestas completas, sin tocar. Arriba, el resumen.

## Resumen

**Vuelta 8: v4, "¿cuánto cómputo vale una idea?"** Medir cuánta búsqueda a ciegas le ahorra la IA a la
mejor máquina de enumeración, para encontrar una ley certificada igual de buena.
- El agujero pasa a ser la atribución: ganarle a nuestro buscador no prueba una idea; puede ser un mal orden
  del buscador o una rutina que le faltaba. El número cambia mucho con el orden de búsqueda.
- La lectura de las frases de Wolfram (W1 a W4) es una hipótesis nuestra, no una prueba de su posición.
- Arreglos: el mejor portafolio retrospectivo (Codex), un trinquete que incorpora al rival lo que la IA hace
  (Astra), curvas de tiempo hasta el primer certificado con censura.

**Vuelta 9: v5, "¿qué parte del descubrimiento no se puede escribir como receta?"**, con cancha abierta.
- Los tres encuentran el mismo error de fondo: la IA también es una receta escrita antes de ver el mundo.
- Los tres: el descubrimiento es una propiedad del resultado, no del proceso; y la medida más estable es
  cuánto conocimiento útil queda incorporado y transfiere.
- Propuestas libres: Astra, representaciones con consecuencias nuevas ("¿qué conocimiento nuevo produce la
  IA que les permite a otros hacer ciencia que antes no podían?"); Codex, ensayos prospectivos con
  laboratorios reales y, sin laboratorio, teorías congeladas que funcionan en casos nuevos; Grok,
  descripciones predictivas mínimas validadas fuera de muestra.

**Vuelta 10: v6, "la prueba del lector".** Una IA autora escribe una guía de un mundo; una lectora acotada
contesta preguntas selladas con y sin la guía; lo que gana es lo descubierto.
- Los tres: mide transmisión (valor instrumental para un lector), no descubrimiento; una guía puede enseñar
  algo conocido o ser un simulador más rápido.
- Trabajo previo cercano que señalaron: "Studying Without a Syllabus" (2026), World Knowledge Exploration
  (2026), KnowledgeGain, ConSim, ALMANACS y las limitaciones de la simulabilidad automática (2026).
- Codex propone las **tres cerraduras** (nuevo, cierto con su alcance, transmisible) y la **disociación**
  entre ellas; Astra, dos productos congelados evaluados por separado; Grok, anclar en una reducción
  explícita probada a escalas mucho mayores.

**Vuelta 11: v7, "las tres cerraduras".** Veredicto de los tres: **sí con cambios, solo para un piloto**.
- Sacar al lector de la definición de novedad (si no, la incapacidad del lector se vuelve novedad).
- Dos credenciales que nunca se suman: ley certificada y regularidad validada en un rango explícito.
- Medir alcance y curvas de riesgo–cobertura; congelar el dominio de validez antes de las preguntas.
- Cuatro condiciones por lector: sin nada, solo el objeto, solo la guía, objeto más guía.
- Cruzar quién descubre, quién redacta la guía y quién la usa, con un lector que el autor no conozca
  (Astra y Codex, por separado).
- La unidad estadística es el mundo: el piloto de 10 mundos solo prueba el instrumento; la confirmación pide
  20 a 30 mundos, varios autores y un modelo jerárquico.
- Las 16 reglas elementales sin proyección conocida: apuesta lateral, no centro. Antes, recuperación a
  ciegas de proyecciones conocidas (Song y Grochow 2020 llegaron exhaustivamente a bloques de 7).
- D2 ("espacio entre conceptos") es hipótesis propia inspirada en Wolfram, no una predicción suya.
- No es de primer nivel por su arquitectura: lo sería con una ley clásica nueva o una disociación amplia y
  replicable que sobreviva a lectores humanos y auditoría externa.

**Qué decidí con esto.** La v7 queda como base, con los cambios de la vuelta 11. Se escribe como premisa en
`research/proposals/` para que Lucas decida. No se construye nada antes.

**Qué no se verificó.** Las referencias citadas "de memoria" por los críticos no se comprobaron acá. Las de
2026 marcadas "comprobada" las verificó el crítico, no yo.

---

## Pedido de la vuelta 8 (premisa v4)

### Octava consulta — premisa v4: "¿Cuánto cómputo vale una idea?"

Tu rol: crítico. **No diseñes un juego ni propongas otra línea.** Atacá, intentá refutar, predecí qué va a
pasar y decí qué falta. Discutí con el otro crítico (las dos respuestas de la vuelta 7 van adjuntas). Sin
halagos. [Dato] / [Literatura (de memoria o comprobada)] / [Juicio]. Castellano llano. Hasta 1.300 palabras.

#### Qué cambió desde la v3 (por sus objeciones)

- Teoremas y conjeturas ya no comparten nada: la pista principal solo admite leyes de **clases con
  comprobación decidible**; las conjeturas y las pruebas en Lean van aparte, con su propio informe.
- El dilema del lenguaje: **las clases de ley quedan fijas, el tamaño no** (bloques, rangos y autómatas de
  cualquier tamaño). Comparabilidad y deduplicación por forma canónica dentro de cada clase.
- El valor queda multiobjetivo (alcance, contenido, ahorro, con las definiciones de ustedes), con umbrales de
  no trivialidad congelados antes. No se suman.
- Lo nuevo: la medida principal ya no es "cuántas leyes" sino **cuánto cómputo de búsqueda reemplaza la
  idea**, y la pregunta se ancla en afirmaciones textuales de Wolfram.

#### La premisa v4

**1. La observación de fondo.** Descubrir es, en sí, una cuenta: buscar en el espacio de leyes posibles
hasta dar con una que valga. Wolfram dice que la ciencia vive en los bolsillos de reducibilidad de la
dinámica. La v4 pregunta si **la búsqueda de bolsillos tiene ella misma bolsillos**: si una IA puede
saltearse parte de esa búsqueda, y cuánto.

**2. Qué dice Wolfram (citas textuales, "Can AI Solve Science?", 2024).**
- W1: «AI has the potential to give us streamlined ways to find certain kinds of pockets of computational
  reducibility.»
- W2: «Will they be "accessible" to neural nets? Again, we don't know. Quite likely, if they are accessible,
  then there'll be some representation—or, say, visualization—in which the reducibility will be "obvious"
  to us.»
- W3: «a neural net trained from existing literature is basically going to be looking for "more of the
  same".»
- W4: «We can, for example, enumerate possible computational systems or processes, and see "fundamental
  surprises". In typical AI there's randomness that gives us a certain degree of "originality" in our
  exploration. But it's of a fundamentally lower level than we can reach with actual irreducible
  computations.»
Lectura operacional: la IA acelera la búsqueda de bolsillos de clases conocidas y visibles (W1, W2), no
encuentra los "raros" (W3), y la enumeración sistemática encuentra sorpresas que la IA no (W4).

**3. El objeto: leyes certificadas, por clases.** Para un sistema F (autómata de una fila, sorteado):
conservación aditiva de rango r (decidible por álgebra lineal); proyección exacta por bloques de tamaño N
con regla gruesa G y escala de tiempo k (cuenta finita); dominio regular invariante con autómata de m
estados y su dinámica inducida (inclusión de lenguajes); partícula sobre un dominio, con velocidad y período
(cuenta finita); atajo exacto dentro de una clase decidible (por ejemplo, lineal sobre un anillo finito
después de un cambio de coordenadas por bloques). Canonicalización por clase; una ley implicada por otras
ya contadas no suma.

**4. El rival: la máquina ruliológica.** Por cada clase, el mejor enumerador que sepamos armar (orden por
tamaño creciente, simetrías, SAT, refinamiento de particiones, álgebra lineal), afinado en sistemas de
desarrollo y congelado antes de mirar a ninguna IA; publicado. Su costo C_enum(v) para encontrar una ley de
valor ≥ v en un sistema se mide en una máquina de referencia (censurado en el presupuesto máximo).

**5. La medida principal: el tipo de cambio de una idea.** E = C_enum(v) / C_agente(v), donde C_agente es todo
lo que gastó el agente para entregar una ley certificada de valor ≥ v (tokens, CPU y dólares, informados por
separado). Dos condiciones: el agente solo, y el agente con la máquina ruliológica como herramienta (contra
la máquina sola con el mismo presupuesto de cómputo). E alto solo puede salir si todas las leyes de ese
valor son grandes: si hay una chica, el enumerador la encuentra rápido.

**6. Las otras dos medidas.** (b) **Qué bolsillos**: de las leyes certificadas, cuáles encuentra cada uno, y
qué fracción es "nombrable" (cae en una familia conocida: conservación de partículas, dominios periódicos,
linealidad) contra "rara". (c) **Tendencia**: E y (b) a lo largo de generaciones de modelos y de presupuesto
de pensamiento.

**7. Poblaciones.** Sistemas frescos de varios espacios de reglas, por estratos declarados (sin
contaminación de instancias). Clásicos (elementales, totalísticos de 3 colores) como prueba ciega de
recuperación y como fuente posible de resultados nuevos, con auditoría experta aparte.

**8. Lo que no se afirma.** Nada sobre irreducibilidad intrínseca. Sí: cuánto le ahorra la IA a la mejor
búsqueda sistemática conocida, en qué clases de bolsillo, y si el patrón coincide con W1–W4.

#### Mis predicciones (contradecilas)

1. Conservación: E ≤ 1 (el álgebra lineal es polinomial; no hay qué ahorrar).
2. Proyecciones por bloques: el enumerador es exponencial en N; el agente encuentra proyecciones
   estructuradas (armadas desde partículas o dominios que ve al correr el sistema) con E entre 10 y 1.000 en
   una minoría de reglas (20 a 30%), y no encuentra proyecciones "raras" que el enumerador sí encuentra con N
   chico.
3. Dominios y partículas: E de 10^2 a 10^4 donde se ven en las corridas; cero en reglas caóticas.
4. Contra la máquina como herramienta: E de 1 a 10 (casi todo el ahorro es escribir y dirigir la búsqueda).
5. Titular más probable: apoyo parcial a Wolfram: la IA acelera los bolsillos nombrables y no ve los raros.

#### Preguntas

1. ¿E está bien definido? ¿Cuál es la manera más barata de inflarlo sin idea ninguna? ¿Y de desinflarlo
   injustamente?
2. "Clases fijas, tamaño libre": ¿resuelve el dilema del lenguaje o lo esconde? ¿Qué clase sobra o falta?
3. ¿La lectura operacional de W1–W4 es fiel a Wolfram? ¿El test es circular o refutable? ¿Qué resultado lo
   refutaría de verdad?
4. "Nombrable" contra "raro": ¿se puede definir sin juez? ¿Cómo?
5. Como sujeto: ¿dónde sacarías E alto y dónde no? Corregí mis predicciones.
6. Trabajo previo más cercano: Busy Beaver BB(6) con IA y Lean (2026), el premio de la regla 30 abierto a
   agentes con verificación en Lean (Wolfram Institute, 2026), el KoLMogorov Test, las ablaciones de
   AlphaEvolve y FunSearch contra búsqueda al azar, Israeli–Goldenfeld. ¿Qué de esto ya está hecho?
7. ¿Qué la haría de primer nivel mundial y qué la dejaría olvidable? ¿Cuál es hoy el agujero principal?
8. Piloto mínimo (sin IA y con IA) y criterios para matarla.
9. Un solo cambio que la haga más fuerte.

---

## Vuelta 8 — respuesta de Astra

**Veredicto — [Juicio].** El agujero principal pasó de la certificación a la atribución: **ganarle a un buscador no demuestra haber evitado búsqueda mediante una idea**. Puede demostrar mejor ordenamiento, entrenamiento amortizado o una rutina ausente. Eso también puede valer, pero no es lo mismo.

#### 1. ¿Está definido E?

[Dato] Todavía no del todo. Necesitás:

- \(v\) como vector de umbrales, con ≥ componente a componente, fijado antes por clase.
- Costos comparables: CPU del enumerador dividida por tokens del agente no define un tipo de cambio. Dólares o tiempo pueden compararse bajo condiciones declaradas; falta contabilizar aceleradores.
- Tratamiento de azar, intentos fallidos y censura. Si el enumerador agota presupuesto, obtenés una cota inferior de su costo, no su costo. Si ninguno llega, no hay cociente observado.

[Juicio] **Inflación barata:** elegir retrospectivamente \(v\) justo donde ganó el agente; informar sólo éxitos; cobrar una llamada ganadora y omitir exploraciones; congelar un rival que ordena mal candidatos equivalentes.

[Juicio] **Desinflación injusta:** cargar todo el preentrenamiento a una instancia, comparar latencia paralela contra ejecución serial o enseñarle al rival la respuesta del examen. Distinguí costo marginal de descubrimiento y costo amortizado de preparación.

[Dato] Es falsa tu garantía «E alto sólo si todas las leyes valiosas son grandes». Una ley chica puede estar al final de un estrato enorme. Tamaño de descripción, costo de verificación y posición en la búsqueda son distintos.

#### 2. Clases fijas, tamaño libre

[Dato] Resuelve una parte: comprobar cada candidato puede ser decidible. **No garantiza decidir si existe algún candidato aceptable de tamaño arbitrario**, ni certificar que no existe.

[Juicio] Contra Codex: convertirse en síntesis dentro de una gramática no invalida el trabajo. Pero tampoco elimina el sesgo del lenguaje.

[Dato] Canonicalizar dentro de cada clase no resuelve «una ley implicada por otras no suma». Eso exige una relación de implicación explícita, posiblemente entre clases, y su propio procedimiento. Tampoco la corrección decidible vuelve automáticamente decidibles tus umbrales asintóticos de valor.

[Juicio] Sobra, por ahora, «atajo exacto dentro de una clase decidible»: es una promesa, no una clase especificada. En partículas falta precisar si certificás una trayectoria periódica aislada o estabilidad frente a todos los fondos y perturbaciones admitidos. La segunda no queda demostrada por verificar la primera.

#### 3. Wolfram: la lectura fuerza las citas

[Juicio] Tomando las citas suministradas como texto, sin cotejarlas:

- W1 expresa una posibilidad, no una superioridad cuantificada.
- W2 conjetura una representación que nos resulte obvia; no dice que deba ser conocida previamente.
- W3 dice «más de lo mismo», no «incapaz de encontrar familias raras».
- W4 compara niveles de originalidad; no establece que una enumeración concreta venza a una red con igual presupuesto.

[Dato] En tus clases, una enumeración completa acabaría encontrando también las leyes entregadas por la IA. La diferencia experimental será de presupuesto y orden, no de accesibilidad absoluta.

[Juicio] Tu lectura operacional es una hipótesis adicional, no una traducción fiel. La debilitarían ventajas repetidas de IA en familias excluidas de una taxonomía previa, resistentes a mejoras del rival. Eso **no refutaría literalmente** las posibilidades vagas de W1–W4.

[Juicio] Hay circularidad si «raro» significa aquello que la IA no encuentra y «visible» aquello que encuentra.

#### 4. Nombrable contra raro

[Dato] Todas tus leyes serán nombrables en el lenguaje formal. «Familia conocida» es otra propiedad.

[Juicio] Podés eliminar el juez durante la evaluación mediante un catálogo previo de familias con pertenencia decidible. «Raro» significaría exclusivamente «fuera de ese catálogo». No significaría nuevo, profundo ni sorprendente.

[Juicio] La selección del catálogo sigue siendo juicio humano. Y una transformación de coordenadas puede convertir una ley aparentemente rara en conservación elemental. Sin declarar qué transformaciones admitís, el resultado mide presentación además de estructura. No hay rareza científica objetiva por decreto de canonicalización.

#### 5. Tus predicciones

[Dato] «Álgebra lineal polinomial» no implica «nada que ahorrar»: la dimensión puede crecer exponencialmente con el rango.

[Juicio] Las corregiría así:

1. **Conservación:** derrota probable en rangos chicos; ventaja posible al seleccionar rangos, soportes o estructuras dispersas. No compraría \(E\leq1\) universal.
2. **Proyecciones:** partículas visibles no implican un cociente exacto global. Espero muchas propuestas plausibles rechazadas por el verificador. El 20–30% y los factores 10–1.000 carecen de base sin población y codificación concretas.
3. **Dominios y partículas:** buena zona para proponer candidatos, no necesariamente para vencer a detección automática competente. Apariencia caótica no excluye dominios que las corridas muestreadas nunca visitaron.
4. **Con herramienta:** puede superar mucho 10 si elegir representación cambia radicalmente la dificultad del solver.
5. **Titular:** espero que dependa más del rival y del catálogo que de generaciones de modelos.

[Juicio] Como sujeto, apostaría a reconocer coordenadas, modular restricciones y dirigir herramientas; no a superar álgebra lineal ya bien planteada.

#### 6. Qué está hecho

[Literatura (de memoria)] Israeli–Goldenfeld ya estudian reducciones mediante proyecciones y búsqueda sistemática acotada: antecedente directo del objeto. Hanson–Crutchfield, dominios y partículas. Síntesis guiada por contraejemplos y síntesis neuronal ya separan proponer, verificar y orientar búsquedas; DreamCoder incluye aprendizaje amortizado sobre búsqueda de programas.

[Literatura (de memoria)] FunSearch y AlphaEvolve combinan propuestas de modelos con evaluación ejecutable y búsqueda. Eso antecede a «IA que ahorra búsqueda», pero evaluación de programas no equivale automáticamente a certificar tus leyes universales. No recuerdo suficientemente sus ablaciones para atribuirles controles de cómputo específicos.

[Juicio] No puedo verificar aquí BB(6), la convocatoria de regla 30 de 2026 ni identificar inequívocamente el KoLMogorov Test. Necesitás referencias precisas. Un certificado de una máquina candidata o una cota inferior no equivale a determinar BB(6); abrir un premio tampoco es un resultado experimental.

#### 7. Primer nivel u olvidable

[Juicio] Primer nivel exigiría ahorro robusto ante rivales competentes, transferencia entre poblaciones y alguna estructura matemática sustantiva, no sólo certificados grandes. Olvidable: tablas de cocientes dominadas por censura, ejemplos vistosos y una conclusión sobre Wolfram que cualquier resultado permite narrar.

[Juicio] Astra acierta: invocar SAT no invalida el aporte. Falta atribuirlo. Inventar una rutina reutilizable puede ser una idea valiosa; dirigirla cada vez es otro resultado.

#### 8. Piloto y muerte

[Juicio] Sin IA: agotar estratos pequeños, contrastar verificadores y atacar los umbrales con leyes degeneradas. Medir cuánto cuesta encontrar frente a verificar.

Con IA: mismos sistemas, umbrales y herramientas; varios intentos cobrados completos; registrar fallos, no sólo cocientes ganadores. Incluir controles conocidos y casos frescos reservados.

Mataría la pretensión principal si las ganancias desaparecen cobrando intentos y certificación, si dependen de una omisión elemental del rival o si los umbrales admiten basura. Un piloto sin éxitos mata esa configuración, no demuestra incapacidad de la IA ni confirma a Wolfram.

#### 9. Un cambio

[Juicio] **Añadí una auditoría adversarial obligatoria del rival.** Tras observar éxitos de desarrollo, incorporá sus heurísticas reutilizables y repetí en sistemas reservados. Conservá ambos resultados. Distinguirías una contribución algorítmica portable de una ventaja recurrente del agente, sin borrar retrospectivamente el valor de la primera.
---

## Vuelta 8 — respuesta de Codex

**Diagnóstico general — [Juicio].** V4 corrige la confusión entre teorema y conjetura, pero todavía no mide “cuánto cómputo vale una idea”. Mide cuánto adelanta un agente a un orden de búsqueda diseñado por ustedes. Esa diferencia puede ser ciencia, una mejor heurística o simplemente un agujero del rival.

#### 1. ¿Está bien definido \(E\)?

[Dato] No completamente. “Valor \(\ge v\)” no está definido si alcance, contenido y ahorro forman una frontera de Pareto. Hace falta una región predeclarada:

\[
C_b(\mathcal V)=\min\{\text{costo hasta hallar }L:L\in\mathcal V\}.
\]

Además, tokens, CPU y dólares no forman un único \(C\). Deben existir \(E_{\$}\), \(E_{\text{tiempo}}\), etc., o curvas de éxito a presupuesto igual. No se pueden dividir vectores.

[Juicio] La inflación más barata es explotar un mal orden del enumerador: reconocer una familia que éste visita tarde, escribir una rutina que faltaba o aprovechar conocimiento preentrenado no cobrado. Una ley grande no necesariamente aparece tarde: un generador estructural puede producirla primero.

También se infla por censura: si el enumerador no llega al hallazgo, \(E\) es sólo una cota inferior, no un número.

Se desinfla injustamente si se cobra toda la inferencia del modelo pero no el desarrollo, precómputo y afinación del portafolio; o si el enumerador fue especializado por clase mientras un único agente debe resolverlas todas.

El otro Astra acertó en algo importante: invocar SAT no invalida el hallazgo. Elegir la representación que vuelve útil a SAT puede ser precisamente la contribución. Pero entonces el claim es “meta-búsqueda más eficiente”, no “una idea reemplazó cómputo”.

#### 2. Clases fijas, tamaño libre

[Juicio] Resuelve la decidibilidad local, pero desplaza el dilema al orden de enumeración. Una unión infinita de tamaños sigue necesitando una prioridad arbitraria. Cambiar esa prioridad puede cambiar \(E\) por órdenes de magnitud.

Hay además solapamientos entre clases: una partícula puede inducir un dominio, una proyección y un atajo. Canonicalizar dentro de cada clase no deduplica entre clases.

La clase que sobra tal como está escrita es “atajo exacto después de un cambio de coordenadas”: sin una gramática estricta del cambio y del predictor, vuelve a abrir todo el lenguaje. “Partícula” tampoco es todavía una clase decidible hasta fijar formalmente fondo, fase, soporte y equivalencias.

Faltan factores con memoria finita o transductores temporales, pero no los agregaría todavía. Primero hay que demostrar que las clases actuales no producen una métrica negociable.

#### 3. W1–W4

[Literatura — comprobada] En el [ensayo de Wolfram](https://writings.stephenwolfram.com/2024/03/can-ai-solve-science/), W1 y W2 sí sostienen que las redes podrían facilitar ciertos bolsillos alineados con alguna representación. Pero también contempla bolsillos desconocidos y “metamotivos”. W3 no es una prohibición estricta de novedad.

W4 contrapone las sorpresas producidas por cómputos irreducibles con la originalidad estocástica de la IA. No afirma que un enumerador congelado de clases conocidas vaya a encontrar las leyes “raras” que el agente omite.

[Juicio] La lectura operacional es una hipótesis nueva inspirada en Wolfram, no una prueba directa de su posición. Es refutable si se fija antes qué significa distancia a la biblioteca. Quedaría contradicha si los agentes obtienen su mayor ventaja precisamente en leyes de alta distancia y la enumeración domina las familiares. Un nulo no refuta a Wolfram: puede significar mala representación o presupuesto insuficiente.

#### 4. “Nombrable” contra “rara”

[Dato] No puede definirse por qué método la encontró: sería circular. Tampoco por rango en el enumerador, porque entonces \(E\) y rareza serían dos nombres del mismo orden.

[Juicio] La versión mecánica defendible es distancia descriptiva a una biblioteca congelada \(B\):

\[
K_B(L)=\min_{p:B(p)=L}|p|.
\]

No es complejidad de Kolmogórov verdadera; es MDL relativo a una gramática. Usaría “cercana/lejana a la biblioteca”, no “nombrable/rara”. Hay que repetir el análisis con varias bibliotecas razonables: si el resultado cambia de signo, no existe el fenómeno alegado.

#### 5. Mis predicciones y qué haría

[Juicio]

- Conservación: \(E<1\) normalmente. El agente sólo añade sobrecosto al álgebra lineal.
- Proyecciones: alguna ventaja al reconocer simetrías o dominios, pero 20–30% de reglas sorteadas parece alto. Espero \(E\) de 2–100; \(10^3\) será casi siempre censura o un agujero del enumerador.
- Dominios y partículas: después de automatizar fondos periódicos, fases y colisiones, espero 1–100, no \(10^4\).
- Agente más herramienta: mediana cercana a 1; cola ocasional superior a 10 cuando descubre una representación ausente.
- “Cero en reglas caóticas” es injustificado: una regla visualmente caótica puede tener factores exactos o conservaciones.

Como sujeto buscaría linealidad, simetrías, fondos periódicos y conjugaciones, y dirigiría los solvers. Sacaría \(E\) alto donde una representación conocida esté enterrada. Fallaría en factores de descripción larga sin señales locales.

#### 6. Trabajo previo

[Literatura — comprobada]

- [BB(6) con IA](https://arxiv.org/abs/2610.22603) ya combina búsqueda abierta, agentes y pruebas en Lean sobre problemas genuinos. No resolvió automáticamente toda la frontera, pero vuelve no novedoso “agente + verificador”.
- El [Rule 30 Prize for Agents](https://www.wolframcloud.com/obj/rule-30-prize/Agents/) ya enfrenta agentes con un sistema clásico y exige verificación formal en Lean.
- [KoLMogorov Test](https://arxiv.org/abs/2503.13992) mide capacidad de producir descripciones/programas compactos; no mide leyes certificadas ni speedup contra enumeradores.
- [FunSearch](https://www.nature.com/articles/s41586-023-06924-6) y [AlphaEvolve](https://arxiv.org/abs/2506.13131) ya muestran búsqueda guiada por LLM con evaluadores exactos. Las ablaciones contra azar hacen muy cercano el claim “la IA ahorra búsqueda”.
- [Israeli–Goldenfeld](https://arxiv.org/abs/nlin/0508033) es el antecedente directo para factores por bloques.

La novedad posible no es que una IA acelere búsqueda verificable. Sería una ley robusta que prediga cuándo y cuánto la acelera frente a rivales realmente competitivos.

#### 7. Importante u olvidable

[Juicio] Sería de primer nivel si entrega simultáneamente:

1. leyes nuevas sustantivas en sistemas clásicos, auditadas externamente;
2. ventajas prospectivas en sistemas frescos que sobrevivan a reforzar el portafolio;
3. una regularidad estable entre distancia a la biblioteca, clase de ley y speedup.

Sería olvidable como leaderboard de \(E\) contra enumeradores propios. El agujero principal es que ustedes controlan representación, orden de búsqueda, clases y umbrales. Por eso pueden fabricar el tipo de cambio casi sin querer.

#### 8. Piloto y muerte

[Juicio] Sin IA: conservación como control negativo y una sola clase con explosión real; reproducción de resultados conocidos, verdad exhaustiva en tamaños pequeños y al menos tres órdenes/buscadores independientes.

Con IA: sistemas ocultos apareados, repeticiones, agente solo, máquina sola y agente+máquina. Diez frescos sirven para depurar, no para probar tendencia.

Mataría la métrica si:

- cambiar razonablemente el orden o representación mueve \(\log_{10}E\) más de una década;
- las victorias desaparecen al añadir al portafolio la rutina escrita por el agente;
- todo \(E\) grande procede de denominadores censurados;
- “cercana/lejana” cambia al cambiar de biblioteca;
- no aparecen leyes certificadas no triviales fuera del portafolio.

#### 9. Un solo cambio

[Juicio] Reemplazá el enumerador único por la **frontera del mejor portafolio retrospectivo**, y calculá speedup sobre distribuciones de tiempo hasta el primer certificado:

\[
E_{\mathrm{robusto}}
=\frac{\min_b C_b(\mathcal V)}{C_{\mathrm{agente}}(\mathcal V)}.
\]

Con censura, reportá curvas de supervivencia y cotas, no cifras puntuales. Ese cambio no elimina el problema de representación, pero evita que “el valor de una idea” sea simplemente el costo de haber ordenado mal una lista.

---

## Pedido de la vuelta 9 (premisa v5 y cancha abierta)

### Novena consulta — premisa v5, y cancha abierta

Esta vuelta tiene dos partes. **Primera:** atacá la v5. **Segunda, con libertad absoluta:** si creés que hay
una forma mejor de medir descubrimiento, proponela, aunque no se parezca en nada a lo que venimos haciendo.
La única condición es la del proyecto: que responda a "cómo medir si una IA descubre", en el sentido de
Wolfram o cerca, y que sea algo que la comunidad (de IA, de sistemas complejos o de ciencia en general)
considere importante y publicable. Proponé direcciones, no especificaciones de juegos; quien decide y arma
soy yo. Sin halagos. [Dato] / [Literatura (de memoria o comprobada)] / [Juicio]. Castellano llano. Hasta
1.500 palabras.

#### Lo que ya existe (no lo propongas como nuevo)

Agentes con IA y pruebas en Lean sobre máquinas de Busy Beaver BB(6) (2026). El premio de la regla 30
abierto a agentes, con verificación en Lean (Wolfram Institute, 2026). El KoLMogorov Test (programas cortos
que reproducen datos). FunSearch y AlphaEvolve (búsqueda guiada por modelos con evaluadores exactos, con
ablaciones contra azar). Israeli–Goldenfeld (proyecciones exactas por bloques, búsqueda acotada). Nuestros
datos: los mejores modelos resuelven en minutos los mundos que dibujamos nosotros y reconocen sistemas
conocidos disfrazados.

#### Qué cambió desde la v4 (por sus objeciones de la vuelta 8)

- El agujero era la **atribución**: ganarle a nuestro buscador no prueba una idea; puede ser un mal orden
  del buscador o una rutina que le faltaba.
- Arreglo combinado de los dos: comparar contra **el mejor portafolio retrospectivo** y **trinquete**:
  todo lo que la IA hace que se pueda convertir en receta general pasa al portafolio, y se vuelve a medir en
  sistemas reservados.
- Medida: **curvas de tiempo hasta el primer certificado** (supervivencia, con censura), en una región de
  valor predeclarada por clase; dólares y tiempo por separado; cotas donde hay censura.
- "Nombrable/rara" pasa a ser **distancia a una biblioteca congelada** (largo mínimo de descripción en esa
  gramática), repetida con varias bibliotecas.
- Las hipótesis de Wolfram quedan como hipótesis nuestras inspiradas en él, no como una prueba de su
  posición.

#### La premisa v5: "¿Qué parte del descubrimiento no se puede escribir como receta?"

**La pregunta.** Cuando una IA encuentra una ley de un sistema, ¿hizo algo que una receta escrita antes
(por personas o por IAs, sin ver ese sistema) también habría hecho con el mismo presupuesto? Lo que no se
puede convertir en receta es descubrimiento propiamente dicho. Lo que sí, es una herramienta (y escribirla
también es un hallazgo, pero de otro tipo).

**El objeto.** Leyes certificadas de sistemas de una fila sorteados, en clases fijas con tamaño libre:
conservación aditiva (control negativo: el álgebra lineal ya es eficiente), proyección exacta por bloques,
dominio regular invariante con su dinámica inducida, partícula sobre un dominio (definición formal de
fondo, fase y soporte). Comprobación decidible por clase. Conjeturas y pruebas en Lean, aparte.

**Los competidores.** (A) La IA trabajando sobre el sistema, sola y con herramientas. (B) El mejor
portafolio retrospectivo: varios enumeradores y órdenes, más recetas generales escritas de antemano por
personas y por IAs (incluida la misma IA cuando se le pide "escribí el mejor buscador general que puedas"),
mejorado con trinquete en sistemas de desarrollo. (C) Evaluación en sistemas frescos reservados.

**Las medidas.** (1) **Lo que queda**: la ventaja de A sobre B en C, después de varias vueltas de trinquete,
en cuantiles de las curvas de tiempo hasta el primer certificado. (2) **La herramienta**: cuánto mejora B
cada vuelta gracias a las recetas que aportó la IA. (3) **Dónde**: cómo cambia (1) con la clase de ley y con
la distancia de la ley a la biblioteca. (4) En sistemas clásicos: recuperación a ciegas y posibles
resultados nuevos, con auditoría experta.

**Hipótesis (nuestras, inspiradas en Wolfram).** H1: queda ventaja en alguna clase. H2: esa ventaja baja
con la distancia a la biblioteca. H3: la enumeración encuentra leyes lejanas que la IA no.

**Muerte.** Si reordenar razonablemente mueve log10 de la ventaja más de una década; si toda ventaja se va
con una vuelta de trinquete; si todo lo grande viene de denominadores censurados; si la distancia cambia de
signo con la biblioteca; si no aparece ninguna ley no trivial fuera del portafolio.

#### Mis predicciones

Después de dos vueltas de trinquete, lo que queda es de 1 a 3 veces en la mediana, con una cola de casos
de 10 a 100 donde la IA eligió una representación que ninguna receta prevé. Lo que más produce la IA es
herramienta, no descubrimiento por caso.

#### Preguntas

1. ¿El trinquete resuelve la atribución o la esconde? ¿Converge? ¿"Receta escrita antes" está bien
   definida (qué puede ver quien la escribe, cuánto puede gastar)?
2. ¿Qué medida principal elegirías entre (1), (2) y (3), y por qué?
3. ¿Esto mide descubrimiento, o mide adaptación por caso? ¿Es lo mismo?
4. Si queda ventaja, ¿qué afirmación permite? Si no queda, ¿qué afirmación permite?
5. ¿Qué la haría importante para la comunidad y qué la dejaría olvidable?
6. **Cancha abierta:** ¿hay una forma mejor de medir descubrimiento? Proponé hasta tres direcciones,
   cualquiera sea su forma. Para cada una: qué se mide, por qué eso es descubrir, por qué le importaría a la
   comunidad, el riesgo principal, cómo se vería el primer resultado, y si le gana a la v5.
7. Si tuvieras que apostar todo a una sola de todas las opciones (la v5 o las tuyas), ¿cuál, y por qué?

---

## Vuelta 9 — respuesta de Astra

#### 1. El agujero principal es ahora la definición

[Dato] **La IA también es una receta escrita antes de ver el sistema.** Un agente digital, con sus pesos, instrucciones, herramientas y fuente de azar, es un procedimiento ejecutable. Que observe el sistema y cambie de estrategia durante la ejecución no lo vuelve menos algorítmico.

[Juicio] Por eso, «lo que no se puede convertir en receta es descubrimiento» no funciona. Si B puede incluir A, la separación desaparece por construcción. Si no puede, medís ventaja respecto de **una clase restringida de procedimientos**, no un residuo no automatizable del descubrimiento.

[Juicio] El trinquete controla omisiones del rival, pero no resuelve esa cuestión conceptual. Tampoco demuestra que una victoria provenga de una representación nueva: para atribuirla a eso, necesitás trasladar esa representación al rival y comprobar qué ganancia produce, manteniendo lo demás comparable.

[Juicio] «Escrita antes» debería fijar:

- Qué distribución, ejemplos, herramientas y modelos puede conocer quien escribe.
- Presupuesto de preparación, incluidos intentos descartados.
- Qué puede consultar la receta durante la ejecución.
- Costos marginales y amortizados, sin cargar todo el preentrenamiento a una instancia ni fingir que no existe.

[Dato] El mínimo retrospectivo por sistema es un **selector oráculo**: sabe qué competidor convenía ejecutar. No equivale a un portafolio realizable con ese presupuesto. Ejecutarlos todos cuesta más; elegir uno exige una política.

[Juicio] Informaría ambos: portafolio ejecutable seleccionado en desarrollo y envolvente oráculo como comparación más exigente. No los mezclaría.

[Dato] No hay garantía general de convergencia del trinquete. Ampliar un conjunto mejora su envolvente ideal, pero no necesariamente un portafolio ejecutable con presupuesto fijo. Una meseta tampoco demuestra agotamiento de las recetas posibles. Cada vuelta que influye en el diseño convierte sus datos en desarrollo; hace falta una reserva final intacta.

#### 2. Elegiría (2): cuánto conocimiento útil queda incorporado

[Juicio] Haría principal **la mejora transferible del portafolio atribuible a los aportes de la IA**. Es observable, acumulativa y científicamente interpretable. Además, no castiga al descubrimiento por volverse reproducible.

[Juicio] Compararía esa mejora con igual esfuerzo adicional de desarrollo sin esos aportes. De otro modo, «la IA produjo herramienta» puede significar simplemente «gastamos más afinando B». Informaría también cuántos casos nuevos hacen falta para amortizar la construcción.

[Literatura (de memoria)] DreamCoder, de Ellis y colaboradores, ya combina búsqueda y aprendizaje de bibliotecas reutilizables. La novedad no sería aprender recetas, sino demostrar su contribución a conocimiento científico certificado y transferible.

[Juicio] Dejaría (1) como medida secundaria de adaptación persistente y (3) como análisis explicativo. Para tiempos usaría éxito a presupuestos fijados y tiempo medio truncado en un corte predeclarado, además de las curvas. Las medianas no existen como estimaciones identificadas si demasiados casos siguen censurados.

#### 3. ¿Descubrimiento o adaptación?

[Juicio] **La adaptación es una capacidad del procedimiento; el descubrimiento es una propiedad del resultado y su justificación.** Adaptarse puede producir un descubrimiento o una solución rutinaria. Una receta puede descubrir una ley importante.

[Juicio] Tu diseño mide principalmente eficiencia de síntesis adaptativa dentro de clases elegidas. Puede contener descubrimientos, pero ganar la carrera no los identifica. La novedad, el contenido y las consecuencias de la ley requieren evaluación adicional. «Primer certificado aceptable» favorece encontrar la salida más barata, no necesariamente aumentar más nuestro conocimiento.

[Dato] La distancia a una biblioteca tampoco quedó automáticamente resuelta. Una gramática no garantiza que puedas calcular el mínimo semántico de descripción. Si admite cómputo general, normalmente no podés; con restricciones adecuadas, hay que justificar la computabilidad o informar cotas.

[Juicio] Además, si medís distancia solamente entre leyes encontradas, condicionás por el resultado de la búsqueda. Cada método seleccionará leyes distintas. H2 puede reflejar esa selección o dificultad computacional, no una preferencia cognitiva por lo familiar. Varias bibliotecas no eliminan ese problema.

[Juicio] Y las clases exactas predefinidas dejan fuera justamente parte de la invención de conceptos. Eso delimita el estudio; no lo invalida, pero achica su título posible.

#### 4. Qué permiten afirmar los resultados

[Juicio] **Si queda ventaja:** «Este agente aporta eficiencia adaptativa adicional frente a estos procedimientos, con estos recursos, en esta población». No permite afirmar que escapó de las recetas, evitó toda búsqueda, inventó conceptos ni encontró un límite de automatización.

[Juicio] **Si no queda:** «No detectamos ventaja residual bajo estas condiciones». Puede haber producido herramientas excelentes; también puede haber poca potencia estadística, problemas fáciles o una comparación que ya incorpora sus capacidades.

[Juicio] Sacaría de las muertes del proyecto «la ventaja desaparece con una vuelta». Si esa vuelta exportó una mejora general, es un resultado positivo para (2). Mata la interpretación del residuo como descubrimiento, no el aporte científico.

[Dato] «Fuera del portafolio» necesita presupuesto: un enumerador completo terminaría encontrando los candidatos certificados de su lenguaje. No encontrarlos a tiempo no significa que estén fuera de su alcance absoluto.

#### 5. Importante u olvidable

[Juicio] Importante sería obtener **una regularidad transferible sobre cuándo las IAs aportan conocimiento**, o un avance científico sustantivo acompañado de una evaluación convincente de cómo ocurrió. No exigiría ambas cosas como condición universal de publicación.

[Juicio] Olvidable: un ranking contra rivales propios, una distancia descriptiva negociable y relatos retrospectivos sobre «representaciones» para explicar la cola. Tus factores previstos no distinguen todavía esos escenarios.

[Juicio] La participación externa debería afectar poblaciones, rivales y valoración científica, no limitarse a revisar certificados al final.

#### 6. Cancha abierta: dos direcciones

### A. Descubrimiento como invención de representaciones con consecuencias nuevas

[Juicio]

- **Qué se mide:** cuánto mejora una representación, abstracción o teoría producida por la IA la capacidad de predecir, derivar o resolver problemas científicos posteriores, fuera de los casos usados para construirla. El artefacto debe poder ser utilizado por otro agente o investigador sin su autor.
- **Por qué es descubrir:** no porque comprima una descripción, sino porque revela estructura y permite obtener consecuencias que antes no estaban disponibles. Convertirse en receta sería una virtud.
- **Por qué importa:** conecta descubrimiento científico con abstracción, generalización y teorías efectivas. Para sistemas complejos, pregunta si la IA encuentra variables colectivas y relaciones entre comportamientos que nuestra descripción microscópica oculta.
- **Riesgo principal:** llamar concepto nuevo a una transformación conocida, o construir una población que ya contiene la abstracción que queremos recuperar. Transferencia sola tampoco demuestra novedad.
- **Primer resultado:** una representación no incluida en la biblioteca que conecte una familia seleccionada independientemente y permita anticipar propiedades reservadas, con garantías formales donde corresponda y auditoría de antecedentes.
- **¿Le gana a v5?:** en validez como medida de descubrimiento, sí. En automatización y cantidad de ensayos, probablemente no.

[Literatura (de memoria)] La mecánica computacional de Crutchfield y colaboradores y los trabajos sobre coarse-graining son antecedentes conceptuales. No serían nuevas la reconstrucción de estructura ni la transferencia; el aporte sería evaluar prospectivamente **la invención autónoma y las consecuencias científicas** de esas representaciones.

### B. Descubrimiento como ampliación de la frontera de predicción eficiente

[Juicio]

- **Qué se mide:** qué nuevas familias de preguntas sobre sistemas pasan a resolverse con menos cómputo gracias a un hallazgo, incluyendo preparación, certificación y dependencia del tamaño y horizonte temporal. No solamente cuánto tarda en encontrarse el certificado.
- **Por qué es descubrir:** identificar un bolsillo de reducibilidad significa aprender dónde no hace falta seguir toda la evolución microscópica para obtener una respuesta.
- **Por qué importa:** vincula directamente IA, dinámica y complejidad computacional. Está más cerca de la pregunta de Wolfram que la oposición entre idea y receta.
- **Riesgo principal:** atajos triviales, ahorro limitado a tamaños pequeños o comparación contra simulación ingenua. Probar superioridad respecto de algoritmos conocidos no prueba irreducibilidad de lo restante.
- **Primer resultado:** una familia con un atajo nuevo certificado cuyo ahorro persista al crecer tamaño u horizonte, acompañado de límites explícitos de aplicación y comparación con métodos especializados.
- **¿Le gana a v5?:** en contenido científico por éxito, sí; como evaluación amplia y rápida de modelos, no.

[Literatura (de memoria)] Israeli–Goldenfeld es antecedente directo, no novedad. El salto tendría que estar en nuevos mecanismos, alcance o límites de los atajos, y en medir cuánto amplía cada agente esa frontera.

#### 7. Mi apuesta

[Juicio] Apostaría a **A: representaciones con consecuencias prospectivas**. Conserva lo más valioso del trinquete —transferir lo aprendido—, pero deja de tratar esa transferencia como eliminación del descubrimiento. También permite distinguir reconocer un sistema disfrazado de aportar estructura nueva.

[Juicio] Usaría la v5 como infraestructura de búsqueda y certificación, con (2) como resultado auxiliar. Cambiaría la pregunta central por: **«¿Qué conocimiento nuevo produce la IA que permite a otros hacer ciencia que antes no podían hacer?»**
---

## Vuelta 9 — respuesta de Codex

#### 1. El trinquete no resuelve la atribución

[Dato] Hay una contradicción formal en el centro de v5. El agente A ya es una receta escrita antes de ver el sistema:

\[
R(F)=\text{ejecutar A sobre }F.
\]

Si B puede llamar al mismo agente con el mismo presupuesto, A y B son idénticos. Si B no puede hacer deliberación condicionada al sistema, la diferencia fue impuesta por la interfaz.

[Juicio] Para volverlo no trivial hay que restringir la clase de recetas: sin llamadas online al modelo, DSL determinada, memoria acotada, costo de compilación fijo. Entonces el residuo significa exclusivamente:

> ventaja sobre esta clase de procedimientos amortizados.

No significa “no se puede escribir como receta”. Puede ser un algoritmo que el destilador no supo extraer, conocimiento en los pesos, suerte o búsqueda online.

El trinquete tampoco tiene por qué converger. Converge sólo si la distribución es estacionaria, la familia de recetas puede representar la estrategia y hay datos suficientes. En una población abierta siempre puede perseguir la última excepción. Cada vuelta además consume otra muestra: hacen falta olas selladas sucesivas; una vez usada una ola para mejorar B, queda quemada.

La definición conceptual está invertida. Una ley descubierta no deja de ser descubrimiento porque luego se transforme en algoritmo. Convertir hallazgos en recetas reutilizables es precisamente progreso científico. Un algoritmo que descubre cien leyes puede ser más importante que una improvisación irrepetible.

Nombre honesto: **amortizabilidad de procedimientos de descubrimiento**, no “descubrimiento propiamente dicho”.

#### 2. Medida principal

[Juicio] Elegiría **(2), cuánto mejora la herramienta**, medido prospectivamente en la siguiente ola sellada.

Es el único objeto acumulativo y relativamente estable: cuánto del desempeño del agente se convirtió en método reutilizable. (1), “lo que queda”, depende demasiado de la potencia del compilador y de la clase permitida de recetas. (3), distancia a la biblioteca, es una variable explicativa secundaria.

La cantidad fuerte sería el desplazamiento de la curva tiempo–primer-certificado de \(B_k\) a \(B_{k+1}\) en sistemas nunca vistos. El residuo A–\(B_k\) se informa, pero no se lo bautiza creatividad ni descubrimiento irreducible.

#### 3. Descubrimiento versus adaptación

[Dato] Adaptarse por caso no implica producir conocimiento. Un optimizador puede ajustar cada instancia, obtener un certificado y no extraer ninguna regularidad transportable.

[Juicio] El descubrimiento está en el producto epistémico: una afirmación nueva, correcta, informativa y capaz de generar predicciones o intervenciones nuevas. Puede obtenerla una receta fija o una deliberación particular.

Por tanto, v5 mide:

- búsqueda condicionada a la instancia;
- cuánto puede amortizarse esa búsqueda;
- cuánto queda fuera del portafolio actual.

No mide por sí sola si ocurrió descubrimiento. Eso lo decide la ley certificada, su novedad y sus consecuencias.

#### 4. Qué permiten afirmar los resultados

[Juicio] Si queda ventaja:

> En estas clases, distribuciones y presupuestos, la búsqueda online guiada por el agente encuentra certificados antes que los procedimientos amortizados disponibles.

No permite afirmar que la ventaja sea intrínsecamente incompilable ni que provenga de una “idea”.

Si desaparece:

> Las estrategias útiles observadas pudieron amortizarse y transfirieron a sistemas nuevos.

No permite afirmar que la IA no descubre. Puede significar que descubrió un procedimiento general y después quedó incorporado al instrumental.

Si el portafolio mejora mucho aunque desaparezca el residuo, ése puede ser el resultado científicamente más importante.

#### 5. Importante u olvidable

[Juicio] Sería importante si muestra una dinámica general de acumulación:

- las recetas extraídas transfieren entre espacios de reglas y clases de ley;
- cada vuelta reduce de manera estable el costo de futuros descubrimientos;
- el residuo reaparece de forma predecible en determinadas representaciones;
- además aparecen leyes matemáticamente sustantivas.

Sería olvidable si termina en 1–3× sobre autómatas celulares, con destilación manual, bibliotecas elegidas por los autores y ninguna ley relevante fuera del benchmark.

El agujero que señalará un revisor es inmediato: **A también es una receta**. Sin una restricción formal de B, la pregunta central se deshace; con ella, el resultado queda relativo a esa restricción.

#### 6. Cancha abierta

### Dirección 1: ensayos prospectivos de descubrimiento real

[Juicio] Una red de laboratorios aporta preguntas todavía abiertas. El agente registra antes del experimento una hipótesis mecanística, una intervención discriminante y predicciones cuantitativas. Laboratorios independientes ejecutan y replican. Se mide conocimiento nuevo validado por costo, tiempo, tasa de falsos hallazgos y ganancia informativa frente a científicos y métodos automáticos.

Esto es descubrimiento porque el resultado no existía públicamente y cambia lo sabido sobre el mundo. Le importaría a toda la comunidad porque elimina la clave fabricada y el juez de estilo.

[Literatura — comprobada ahora] Ya existen piezas, pero no el ensayo abierto completo. **Science Prediction Universe** usa 100 tareas publicadas y 16 experimentos húmedos inéditos; evalúa predicción de resultados fijados, no generación libre de hipótesis, y el mejor desempeño sigue lejos del techo ([SPU](https://arxiv.org/abs/2611.15049)). AIntibody evaluó prospectivamente 511 anticuerpos de 29 equipos contra mediciones experimentales ([AIntibody](https://www.nature.com/articles/s41587-026-03238-6)). A-Lab sintetizó 41 de 58 materiales objetivo mediante un ciclo autónomo ([A-Lab](https://www.nature.com/articles/s41586-023-06734-w.pdf)). Adam ya generaba y probaba hipótesis genómicas autónomamente en 2009 ([Science](https://pubmed.ncbi.nlm.nih.gov/19342587/)).

Riesgo principal: bajo \(n\), costo, seguridad, fuerte selección humana de preguntas y múltiples hipótesis. El primer resultado convincente sería una relación causal novedosa, preregistrada, replicada y omitida por controles con igual presupuesto.

Le gana a v5 en validez de constructo. Pierde en velocidad, control y escala.

### Dirección 2: medir causalmente si la IA acelera ciencia

[Juicio] Randomizar proyectos o laboratorios entre investigación habitual, asistencia de IA y agente más autónomo. Resultado: tiempo y costo hasta un hallazgo preregistrado e independientemente replicado; no papers, citas ni cantidad de ideas.

Esto no mide “autonomía intelectual” del modelo. Mide la pregunta socialmente decisiva: **¿usar IA causa más descubrimiento?**

[Literatura — comprobada ahora] Ya se hacen evaluaciones aleatorizadas de IA dentro del trabajo científico, pero no existe todavía una referencia estable basada en descubrimientos replicados. Un ensayo reciente sobre reproducción de estudios encontró que la asistencia no aportó ventaja medible y redujo la detección de errores graves ([PNAS](https://doi.org/10.1073/pnas.2524747123)).

Riesgos: contaminación entre brazos, adopción desigual, años de demora y enorme heterogeneidad entre campos. El primer resultado fuerte sería una mejora causal en hallazgos replicados, no sólo productividad.

Le gana a v5 en relevancia externa; pierde la atribución limpia al agente porque mide sistemas humano–IA.

### Dirección 3: teorías que transfieren antes de volver a mirar

[Juicio] El agente estudia una población y entrega un artefacto teórico congelado: variables, ley y condiciones de aplicación. Después se evalúa en sistemas, escalas, observables e intervenciones nuevos, sin permitir adaptación. Se mide predicción prospectiva, control, compresión y cómputo ahorrado.

Es descubrimiento cuando una abstracción finita anticipa hechos nuevos y permite actuar; eso es el bolsillo de reducibilidad de Wolfram en su forma más defendible. La generalización fija separa teoría de solución por instancia.

[Literatura — comprobada/de memoria] La búsqueda automática de ecuaciones ya produjo leyes simbólicas desde datos experimentales ([Schmidt y Lipson, 2009](https://faculty.washington.edu/morgansn/pmwiki/uploads/Site/schmidt-science2009.pdf)). Por eso el aporte tendría que ser transferencia entre sistemas y regímenes, no otra demostración de regresión simbólica.

Riesgo: la distribución y el lenguaje de teorías siguen definiendo qué puede transferir. El primer resultado fuerte sería una teoría compacta que predice o controla fenómenos retenidos mejor que modelos negros y métodos expertos, con menos cómputo.

Le gana a v5 como medida de teoría; pierde la certificación exacta en dominios naturales.

#### 7. Mi apuesta única

[Juicio] Apostaría a la **Dirección 1: un ensayo prospectivo continuo de descubrimientos con resultados todavía desconocidos y replicación independiente**.

Es la única donde un positivo no necesita una defensa filosófica: antes no se sabía, la IA se comprometió, el mundo respondió y otro laboratorio lo reprodujo. V5 puede estudiar después cómo se obtuvo y cuánto se amortiza, pero no debería ser la medida principal. Sin acceso real a una red experimental, mi segunda opción sería la Dirección 3; no volvería a hacer de la ventaja sobre un buscador propio el centro del proyecto.

---

## Vuelta 9 — respuesta de Grok

**Ataque a la v5**

[Dato] El trinquete no resuelve la atribución; la difiere. Cada receta que la IA aporta al portafolio se convierte en conocimiento compartido, de modo que la siguiente ronda mide la capacidad del agente para generar herramientas portables, no para descubrir leyes en sistemas vírgenes. Después de dos vueltas el residuo ya no es “descubrimiento” sino la fracción de ideas que el agente produce más rápido que el proceso de explicitarlas y codificarlas.

[Dato] “Receta escrita antes” sigue mal definida. Quien escribe la receta puede ver los sistemas de desarrollo, los verificadores y los fracasos previos del portafolio. Eso equivale a permitir precomputación y afinación humana o de otra IA sobre el mismo conjunto que luego se usa para medir. El presupuesto de la receta no está acotado de forma simétrica al del agente en vivo.

[Juicio] El mecanismo converge, pero a un punto trivial: tras suficientes iteraciones el portafolio contiene todo lo que se puede escribir como procedimiento general reutilizable. Lo que queda mide entonces la capacidad de la IA para resolver instancias fuera de ese cierre, que es exactamente el problema de atribución que se quería evitar.

[Dato] La medida principal que conviene retener es (2): cuánto mejora B cada vuelta gracias a las recetas de la IA. (1) sigue dependiendo de la calidad inicial del portafolio y de la censura; (3) es útil como diagnóstico pero secundario.

[Juicio] Esto mide adaptación por caso más que descubrimiento. Descubrimiento, en el sentido operativo que se persigue, requeriría que la ventaja persista en sistemas que ningún procedimiento general escrito de antemano pueda atacar con el mismo presupuesto. La v5 no separa esos dos fenómenos; los confunde bajo el rótulo de “lo que queda”.

[Juicio] Si queda ventaja estable tras dos vueltas de trinquete y con bibliotecas distintas, la afirmación defendible es: “existen representaciones o atajos que la IA localiza sistemáticamente antes de que se los pueda escribir como receta general”. Si la ventaja desaparece, la afirmación es más débil: “la IA es un generador eficiente de procedimientos reutilizables cuando se le pide que los explicite”. Ninguna de las dos refuta ni confirma las hipótesis wolframianas sobre irreducibilidad; ambas son afirmaciones sobre meta-búsqueda.

[Juicio] Para que el trabajo importe a la comunidad de sistemas complejos y de IA haría falta que entregue, además de curvas de speedup, al menos una ley nueva no trivial en un sistema clásico (autómata celular o red de reacción-difusión) que haya sido auditada por investigadores externos y que no se derive de transformaciones ya catalogadas. Lo que lo volvería olvidable es que los resultados queden dominados por censura, que la distancia a la biblioteca cambie de signo con la gramática elegida, o que todo el efecto desaparezca al reemplazar el portafolio por cualquier enumerador razonable con buen ordenamiento.

**Cancha abierta: tres direcciones alternativas**

Dirección 1 — Descubrimiento de descripciones mínimas predictivas en sistemas de cómputo acotado.  
Se mide la longitud de la descripción más corta que un agente produce y que, al ejecutarse dentro de un presupuesto fijo de pasos, reproduce el comportamiento observado de un sistema (regla 110, regla 30 enmascarada, o red booleana aleatoria) con error acotado. El verificador es un simulador exacto más un test de equivalencia en distribuciones de estados no vistos.  
Es descubrir porque reduce el costo futuro de predecir el sistema sin simularlo exhaustivamente; captura el “bolsillo de reducibilidad” como compresión útil, no como mera clasificación.  
Le importaría a la comunidad porque conecta directamente con la literatura de MDL aplicado a autómatas celulares y con los tests de compresión como proxy de inteligencia (KoLMogorov Test ya existe, pero sin verificación de generalización fuera de la muestra).  
Riesgo principal: que el agente aprenda trucos de codificación que explotan regularidades del simulador y no del sistema subyacente.  
Primer resultado visible: un agente que, en 50 sistemas reservados de 20×20, produce descripciones al menos 30 % más cortas que el mejor compresor Lempel-Ziv adaptado a rejillas, con validación en 10^6 pasos no observados.  
Gana a la v5 porque mide directamente reducción de descripción en lugar de speedup contra un portafolio que nosotros controlamos.

Dirección 2 — Generación de invariantes verificables en sistemas dinámicos continuos discretizados.  
Se mide si el agente propone una función de Lyapunov o un invariante algebraico que, una vez certificado por un solver de desigualdades polinomiales (como en el trabajo de Ahmadi et al. sobre Lyapunov algebraicas), demuestra estabilidad o periodicidad en un dominio abierto del espacio de estados. El sistema se sortea entre familias de ecuaciones diferenciales parciales discretizadas con parámetros aleatorios.  
Es descubrir porque produce un certificado formal que vale para infinitos estados futuros sin simularlos.  
Le importaría a la comunidad de control y sistemas dinámicos porque la síntesis automática de invariantes sigue siendo un cuello de botella; trabajos como aquellos que combinan redes neuronales con certificados de Lyapunov ya se publican en NeurIPS y CDC.  
Riesgo principal: que el invariante sea trivial o solo local, aunque el verificador lo acepte.  
Primer resultado: cinco invariantes nuevos certificados en familias de PDE discretizadas que no aparecen en la literatura y que reducen el tiempo de verificación de estabilidad en dos órdenes de magnitud respecto de simulación de Monte Carlo.  
Gana a la v5 porque el output es un objeto matemático reutilizable y auditable por pares, no una curva de tiempo hasta certificado.

Dirección 3 — Meta-descubrimiento de órdenes de búsqueda que generalizan entre clases de sistemas.  
Se mide la capacidad del agente para proponer una heurística de priorización (por ejemplo, una red que ordena candidatos de leyes) que, entrenada en una distribución de sistemas de desarrollo, mejora el tiempo hasta primer hallazgo en una distribución distinta y no solapada de sistemas frescos. Se exige que la heurística se pueda ejecutar sin volver a llamar al modelo original.  
Es descubrir porque el agente está encontrando una regularidad en el espacio de problemas, no una solución a un problema aislado.  
Le importaría a la comunidad de AutoML y de “AI for Science” porque separa el costo de aprender la estrategia del costo de aplicarla, algo que FunSearch y AlphaEvolve rozan pero no aíslan cuando el evaluador es exacto y el dominio es científico.  
Riesgo principal: que la heurística capture sesgos del generador de sistemas en lugar de estructura matemática real.  
Primer resultado: una función de ordenamiento que, una vez extraída, reduce en factor 5–20 el tiempo hasta primer certificado en tres clases nuevas de sistemas que nunca vio durante su generación.  
Pierde contra la v5 en facilidad de ejecución inmediata, pero gana en separabilidad del aporte algorítmico.

**Apuesta única**

Apostaría todo a la Dirección 1. Mide directamente la noción wolframiana de reducibilidad como compresión predictiva verificable, exige menos infraestructura de verificación formal que la v5, y produce un output (descripciones mínimas) que la comunidad de sistemas complejos ya considera valioso publicar cuando está acompañado de generalización fuera de muestra. La v5 sigue midiendo principalmente qué tan bueno es nuestro propio portafolio; la Dirección 1 mide qué tan bien la IA comprime comportamiento observable sin que nosotros decidamos de antemano qué cuenta como “ley”.
---

## Pedido de la vuelta 10 (premisa v6)

### Décima consulta — premisa v6: "la prueba del lector"

Dos partes, como la vuelta anterior. **Primera:** atacá la v6 a fondo. **Segunda, con libertad absoluta:** si
ves algo mejor para medir descubrimiento (que sea publicable e importante para la comunidad), decilo. Quien
decide y arma soy yo. Sin halagos. [Dato] / [Literatura (de memoria o comprobada)] / [Juicio]. Castellano
llano. Hasta 1.500 palabras.

#### De dónde sale

En la vuelta 9 los tres críticos coincidieron (respuestas adjuntas): (a) la v5 tenía un error de fondo: la
IA también es una receta escrita antes; (b) **el descubrimiento es una propiedad del resultado, no del
proceso**; (c) Astra: "¿qué conocimiento nuevo produce la IA que les permite a otros hacer ciencia que antes
no podían?"; Codex: teorías congeladas que funcionan en casos nuevos sin volver a mirar; Grok: descripciones
predictivas mínimas validadas fuera de muestra.

#### La premisa v6

**1. Definición operativa.** Un descubrimiento sobre un mundo es **conocimiento transmisible** que le
permite a un **observador acotado** (el lector) contestar bien y barato preguntas sobre ese mundo que solo,
con el mismo presupuesto, no contestaría. Lectura en clave de Wolfram: un bolsillo de reducibilidad es algo
que un observador de cómputo acotado puede decir con poco esfuerzo; la guía le pasa bolsillos al lector.
Medir el descubrimiento es medir cuánto le extiende el alcance a ese observador.

**2. Protocolo.**
- *Mundo:* una regla simple, a la vista (sorteada de espacios declarados, por estratos; o una regla clásica).
- *Autor:* explora con presupuesto B_a (simulador, código) y entrega una **guía** de tamaño ≤ S, en
  cualquier forma: texto, código, tablas, lemas. No ve las preguntas.
- *Preguntas selladas:* familias declaradas antes, instancias sorteadas después, con respuesta exacta
  calculada por nosotros (fuerza bruta en C, procedimientos de decisión): predecir observables lejos;
  construir (dar un comienzo que logre X en el paso T); decidir propiedades (¿se conserva Q? ¿aparece P
  desde comienzos de tal familia?); contar.
- *Lector:* un modelo fijo, con presupuesto chico b y las mismas herramientas (incluido un simulador rápido),
  **con y sin guía**.
- *Medidas:* (i) **ganancia** = aciertos(lector + guía) − aciertos(lector solo), a b fijo; (ii)
  **equivalente en presupuesto**: el B* con el que el lector solo iguala al lector con guía y presupuesto b;
  valor = B*/b, con censura; (iii) **control de conocimiento genérico**: el lector recibe la guía de otro
  mundo de la misma familia; ganancia específica = ganancia con la guía propia − ganancia con la ajena.
- *Autores comparados:* IAs de varias generaciones y presupuestos; un **autor mecánico** (catálogo automático
  de leyes certificadas, partículas y choques, hecho por enumeración sistemática); en reglas clásicas, la
  literatura.

**3. Hipótesis (nuestras, inspiradas en Wolfram).** H1: en mundos con estructura, las guías de IA valen
B*/b ≫ 1; en mundos caóticos, ≈ 1 para preguntas lejanas. H2: las guías de IA ganan en preguntas que
dependen de bolsillos visibles al correr el mundo; la guía mecánica, en preguntas que dependen de leyes que
no se ven (la "sorpresa" de la enumeración). H3: el valor crece con el presupuesto del autor y con la
generación del modelo; ¿satura? H4 (fase 2): guías heredadas aumentan el valor de las siguientes
(acumulación).

**4. Qué resuelve, según yo.** Lenguaje abierto (la guía puede ser cualquier cosa; se la juzga por su
efecto). Atribución (mismo lector, con y sin guía). Recetas genéricas (control con guía ajena). "La IA es una
receta" (se mide el producto). Mundos dibujados (no se dibuja nada). Jueces (puntaje exacto sobre las
respuestas del lector).

**5. Riesgos que ya veo.** Varianza del lector y sensibilidad a la consigna. Guías que son simuladores más
rápidos (control: el lector solo ya tiene uno rápido; tope de tiempo por pregunta). Fuga de respuestas (las
preguntas se sortean de espacios enormes; tope de tamaño). Un lector demasiado fuerte que redescubre todo
(elegir b chico y mostrar la curva sobre b). Preguntas que no tocan los bolsillos.

**6. Trabajo previo (búsqueda rápida mía, solo resúmenes).** Simulabilidad en explicabilidad de IA (una
explicación vale si otro modelo, usándola, predice el comportamiento; neuronas explicadas por OpenAI en 2023;
ALMANACS; ConSim). KGain (mayo de 2026): ganancia de conocimiento de un lector antes y después de leer
divulgación científica. "Studying Without a Syllabus: Task-Agnostic Environment Preprocessing" (septiembre de
2026): un agente explora un entorno antes de ver las tareas y deja materiales; un resolvedor congelado los
usa en tareas nuevas. Destilación de "conocimiento del mundo" con recompensa por mejora posterior (2026).
No encontré esto aplicado a descubrimiento científico con verdad calculable.

**7. Mi predicción.** Mundos con partículas: guías de Astra con B*/b de 10 a 100, sobre todo en predicción
lejana y construcción. Mundos caóticos: ganancia en preguntas locales (conservaciones), no en lejanas. El
autor mecánico gana en propiedades decididas y pierde en construcción.

**8. Piloto.** Sin IA: mundos, familias de preguntas con verdad exacta, comprobación de que un programa
genérico no las contesta todas, autor mecánico. Con IA: 5 mundos, 2 autores, 1 lector chico, b fijo, más el
control con guía ajena.

#### Preguntas

1. ¿Esto mide descubrimiento o enseñanza/comunicación? ¿La diferencia importa para lo que queremos?
2. ¿Dónde se rompe? ¿La forma más barata de inflar la ganancia sin descubrir nada? ¿Y de desinflarla
   injustamente?
3. El lector: ¿modelo o programa fijo? ¿Qué presupuesto? ¿Cómo evitar que el lector redescubra o que la
   ganancia dependa sobre todo de él?
4. Las preguntas selladas: ¿qué familias aseguran que la ganancia refleje bolsillos y no trucos?
5. B*/b como unidad: ¿sana? ¿Qué hacer con la censura?
6. Novedad frente al trabajo previo listado: ¿qué ya está hecho?
7. ¿Qué la haría de primer nivel? ¿Cuál sería el titular si sale bien, y cuál si sale mal?
8. Piloto y criterios de muerte.
9. Cancha abierta: ¿algo mejor que esto? ¿O una forma de combinarla con otra idea que la haga más fuerte?

---

## Vuelta 10 — respuesta de Astra

#### Primera parte: dónde se rompe la v6

### 1. Medís utilidad transmitida, no identificás descubrimiento

[Juicio] La definición incluye enseñanza, recuperación de conocimiento conocido, compilación y optimización. Una guía que explica una técnica elemental puede producir una ganancia enorme. Un descubrimiento importante puede producir cero si el lector no sabe usarlo o las preguntas no lo necesitan. **La ganancia no es condición suficiente ni necesaria de descubrimiento.**

[Dato] Respuestas correctas tampoco certifican la guía: una explicación falsa puede recomendar un procedimiento que funciona en la distribución evaluada.

[Juicio] Llamaría al resultado **valor instrumental transferido**, relativo al mundo, las preguntas, el lector y el presupuesto. Para llamarlo descubrimiento agregaría evidencia separada de contenido correcto, novedad y alcance. La distinción importa: sin ella, el titular promete más de lo que identifica el experimento.

### 2. Inflarlo y desinflarlo es barato

[Juicio] La inflación más barata probablemente sea **adaptar conocimiento conocido al lector**: código listo para ejecutar, selección del algoritmo apropiado, ejemplos de uso, advertencias contra errores frecuentes. También sirve especializar un solucionador para las familias declaradas. Nada requiere conocer las instancias selladas.

[Dato] Tu “ganancia específica” se reduce algebraicamente a aciertos con guía propia menos aciertos con guía ajena. Si la ajena confunde, el contraste aumenta aunque la propia no aporte nada respecto de no recibir guía.

[Juicio] Además, una ley genuina compartida por varios mundos puede quedar descontada como “genérica”. **Generalidad científica y falta de especificidad no son defectos equivalentes.** Usaría controles separados:

- guía genérica útil, compatible con ese mundo;
- guía ajena;
- material de igual longitud y formato, sin contenido útil;
- solución conocida redactada para el lector, como control positivo.

[Juicio] Para desinflar injustamente alcanza con entregar buena matemática a un lector incapaz de ejecutarla. También con comparar una guía de IA pulida contra un catálogo mecánico mal seleccionado. Igualá el esfuerzo de edición y adaptación de ambos.

### 3. El lector no desaparece: es parte del objeto medido

[Dato] Mantenerlo fijo permite estimar el efecto de añadir el artefacto, con ejecuciones independientes y repetidas. No permite atribuir ese efecto a novedad científica.

[Juicio] Usaría dos lectores de capacidades distintas y, cuando haya código, ejecución directa mediante una interfaz fija. Un programa evita cierta varianza lingüística, pero impone su propio lenguaje de representación. No existe un lector neutral.

[Juicio] No intentaría impedir que redescubra: eso pertenece al contrafactual. Mostraría curvas sobre varios presupuestos, sin elegir retrospectivamente el punto donde más luce la guía.

[Juicio] Contá lectura, ejecución, memoria, herramientas y bibliotecas disponibles. Fijá hardware para comparar programas. No sumes tokens y segundos sin una conversión declarada. Separá preparación, costo por pregunta y amortización entre consultas. Compará también contra un procedimiento no científico que disponga del mismo presupuesto de preparación.

### 4. Preguntas selladas: necesarias, insuficientes

[Dato] Sortear de un espacio enorme impide memorizar todas las instancias, pero no elimina regularidades triviales del generador. La combinación de población y preguntas sigue siendo una decisión de diseño, aunque no dibujes mundos.

[Juicio] Ninguna familia asegura por sí sola que la ganancia refleje “bolsillos”. Reservaría cambios de tamaño, horizonte, condiciones iniciales e intervenciones; además, alguna combinación de capacidades no practicada. Equilibraría casos positivos y negativos, evitando que casi todas las respuestas sean “no aparece” o “cero”.

[Dato] Hay propiedades asintóticas indecidibles en clases generales de autómatas. Fuerza bruta en C no vuelve decidible una pregunta infinita. Debés distinguir:

- respuestas exactas en dominios finitos;
- propiedades acotadas temporalmente;
- afirmaciones generales acompañadas de certificados verificables.

[Juicio] En construcción, verificar un testigo puede ser barato; certificar inexistencia, no. Diseñá el puntaje según esa diferencia. Y validá las respuestas de referencia mediante implementaciones independientes: “exacto” no significa “libre de errores de software”.

### 5. \(B^*/b\): comparación local, no unidad universal

[Dato] Más presupuesto no garantiza mayor acierto de un modelo concreto. La curva puede estancarse, empeorar o nunca alcanzar el objetivo. Entonces \(B^*\) puede no estar identificado.

[Juicio] Haría principal la **curva acierto–costo total**, y secundario el cociente. Si no hay cruce, informá “no alcanzado hasta \(B_{\max}\)”, con incertidumbre. Una cota inferior exige supuestos explícitos sobre la curva; no reemplaces censurados por el límite ni promedies infinitos.

[Juicio] El cociente describe ese lector y esa política de gasto. Puede medir incapacidad para aprovechar más cómputo, no ahorro computacional intrínseco del hallazgo. Agregaría cuántas consultas hacen falta para recuperar el costo del autor.

### 6. Las hipótesis mezclan demasiadas cosas

[Juicio] H1 confunde caos con dificultad de responder observables. Un mundo caótico puede tener propiedades colectivas fáciles; uno ordenado, problemas inversos difíciles. “Lejos” tampoco define una dificultad única.

[Juicio] H2 necesita definir “visible” independientemente del resultado. La enumeración también puede producir herramientas de construcción; una IA puede encontrar invariantes poco visibles. No hay una división conceptual limpia entre ambos autores.

[Juicio] H3 mezcla capacidad, entrenamiento, herramientas y aprovechamiento del presupuesto. H4 necesita un control con igual cómputo total y capacidad de almacenamiento. Estratificá antes de observar ganancias; cinco mundos no sostienen estas generalizaciones.

### 7. Novedad: el esqueleto tiene antecedentes cercanos

[Literatura (de memoria)] La simulabilidad de explicaciones ya juzga materiales por su efecto sobre otro predictor. La compilación de conocimiento —por ejemplo, Darwiche y Marquis— estudia pagar preparación para abaratar consultas posteriores. También son pertinentes especialización de programas, aprendizaje amortizado y enseñanza automática. Israeli y Goldenfeld son antecedentes directos sobre predicción mediante descripciones de grano grueso.

[Dato] No verifiqué KGain ni los títulos de 2026. Tampoco heredo la etiqueta “comprobada” de los adjuntos.

[Juicio] Si el trabajo sobre exploración sin tareas hace lo que describís, comparte gran parte del protocolo. Aplicarlo a ciencia con verdad calculable puede justificar una evaluación nueva, pero no basta para reclamar una nueva medida de descubrimiento. La prioridad requiere leer métodos y experimentos, no solamente resúmenes.

### 8. Piloto y criterios de muerte

[Juicio] Cinco mundos sirven para probar instrumental, no para estimar capacidad general. Antes de comparar autores incluiría:

1. una guía conocida que debería ayudar;
2. una guía trivial pero bien adaptada;
3. una guía con un atajo estructural verificable;
4. dos lectores y varios presupuestos.

[Juicio] Reservá mundos finales intactos. Las preguntas del mismo mundo no sustituyen réplicas entre mundos; repetí también autores y lectores con distintas semillas.

[Juicio] Criterios de muerte, fijados antes:

- Si el control positivo no ayuda, falla el instrumento.
- Si toda ganancia se reproduce mediante instrucciones genéricas, cae la interpretación científica.
- Si el efecto cambia de signo entre lectores razonables, cae una escala única de “valor del conocimiento”.
- Si los atajos desaparecen al ampliar tamaño u horizonte, cae la afirmación de alcance, no necesariamente su utilidad local.

#### Segunda parte: combinaría dos pruebas, no buscaría un escalar único

[Juicio] Cambiaría el centro a **ampliación prospectiva de la frontera de preguntas resolubles**, y dejaría la prueba del lector como evaluación de transmisión.

[Juicio] Pediría dos productos congelados:

- **Objeto científico:** ley, representación o algoritmo; condiciones de aplicación; consecuencias comprobables.
- **Guía de uso:** material para que otros aprovechen ese objeto.

[Juicio] Evaluaría por separado:

1. **Contenido:** corrección, antecedentes y consecuencias nuevas. “No estaba en nuestra biblioteca” no basta como novedad.
2. **Alcance computacional:** ahorro frente a métodos especializados, en tamaños y horizontes reservados, incluyendo preparación.
3. **Transmisión:** cuánto conservan lectores distintos de esa ventaja.

[Juicio] No prohibiría simuladores más rápidos: un algoritmo nuevo puede ser el descubrimiento. Separaría optimización de implementación de un atajo estructural mediante análisis y escalado. Sin demostración, afirmaría ahorro empírico en el intervalo probado, no una mejora asintótica.

[Juicio] Esto permite distinguir **hallazgo que nadie logra usar**, **enseñanza eficaz de algo conocido** y **hallazgo nuevo que amplía capacidades ajenas**. La v6 sola los mezcla.

[Juicio] Para primer nivel buscaría un avance sustantivo auditado externamente o una regularidad amplia y replicable sobre transferencia científica; no solamente un ranking.

**Titular positivo:** “La IA produce atajos nuevos y reutilizables que amplían la predicción y el control en familias reservadas”.

**Titular negativo, si los controles positivos funcionan:** “La ganancia del lector proviene de adaptar conocimiento conocido; no detectamos ampliación científica frente a métodos especializados”.

[Juicio] El segundo sería informativo. Sin esa separación, tanto ganar como perder admiten demasiadas explicaciones.
---

## Vuelta 10 — respuesta de Codex

**Veredicto — [Juicio].** V6 mide algo real: el valor condicional de un artefacto para un lector acotado. Pero no identifica por sí sola descubrimiento. Confunde tres propiedades distintas: que la guía contenga conocimiento nuevo, que lo comunique bien y que el lector sepa explotarlo.

#### 1. ¿Descubrimiento o enseñanza?

[Dato] Una guía puede obtener gran ganancia limitándose a reorganizar hechos obvios, explicar mejor la regla o darle al lector una estrategia de examen. No produjo conocimiento nuevo. A la inversa, una ley genuinamente nueva puede puntuar cero porque el lector no la comprende o porque las preguntas no tocan sus consecuencias.

[Juicio] V6 es una buena **prueba de transmisión o de uptake**:

> ¿Este artefacto permite que este lector responda nuevas preguntas bajo este presupuesto?

Eso es una propiedad deseable de un descubrimiento, no su definición completa. Para medir descubrimiento hacen falta tres ejes separados:

1. novedad respecto del conocimiento previo;
2. corrección y alcance;
3. utilidad transmisible para terceros.

La diferencia importa. Si no se separan, el paper termina midiendo autores de buenos manuales.

#### 2. Dónde se rompe

[Juicio] Las inflaciones más baratas son:

- **Prompt para el lector:** instrucciones genéricas de razonamiento, asignación de tiempo o uso de herramientas. La guía propia puede estar mejor adaptada al lector aunque no contenga una ley.
- **Código como cómputo diferido:** una guía pequeña ejecuta una búsqueda enorme durante la pregunta. El límite \(S\) no limita la información ni el costo.
- **Activar conocimiento memorizado:** una frase corta puede desbloquear una rutina enorme ya presente en los pesos. El valor es relativo al lector, no una cantidad objetiva de conocimiento.
- **Optimizar para el temario:** el autor no conoce las instancias, pero sí las familias de preguntas. No está “sin syllabus”; conoce el syllabus a nivel de familias.
- **Guía ajena dañina:** si la guía de otro mundo confunde al lector, restarla infla artificialmente la especificidad de la guía propia.
- **Explotar el harness:** instrucciones adversariales, detalles del formato, semillas o regularidades del generador de preguntas.

La guía ajena no debería ser el único placebo. Hace falta comparar también con guía de igual forma y longitud con hechos permutados, guía genérica sin hechos del mundo, transcripción cruda de la exploración y resumen automático no investigador.

[Dato] Algunas preguntas propuestas no tienen necesariamente respuesta decidible. Alcanzabilidad universal en autómatas celulares puede ser indecidible. “¿Aparece \(P\) desde una familia de comienzos?” sólo tiene verdad mecánica exacta si se acota tamaño, tiempo o se elige una clase decidible.

[Juicio] La desinflación injusta ocurre cuando:

- el lector es incapaz de interpretar una guía correcta;
- \(b\) queda debajo del costo de ejecutar la ley;
- el lector solo ya está en techo;
- las preguntas no caen dentro del alcance descubierto;
- la guía usa una representación ajena al lector;
- el contexto largo degrada al modelo.

#### 3. El lector

[Juicio] No usaría un único lector y no buscaría eliminar su influencia: **la medida es inevitablemente lector-relativa**.

Usaría un panel congelado:

- dos o tres modelos de familias y capacidades distintas;
- varias semillas por lector;
- un ejecutor determinista sólo para las partes formalmente ejecutables;
- una pequeña validación humana si el claim menciona ciencia transmisible.

La prueba fuerte es que la guía ayude a un lector no conocido por el autor. Si sólo ayuda al mismo linaje de modelo o bajo una redacción concreta, mide compatibilidad de prompts.

\(b\) debe escogerse en desarrollo para evitar piso y techo y luego congelarse. Informaría toda la curva sobre varios presupuestos. Un solo \(b\) permite fabricar la ganancia situándolo justo donde el lector casi resuelve.

Un programa fijo es más estable, pero obliga a cerrar el lenguaje de la guía. Un modelo mantiene el lenguaje abierto a costa de ruido, memoria previa y susceptibilidad a instrucciones. No hay solución que conserve ambas ventajas.

#### 4. Preguntas selladas

[Juicio] Ninguna familia garantiza por sí sola que se estén midiendo bolsillos. Hay que demostrar sensibilidad antes:

- una guía oráculo con leyes conocidas debe mejorar al lector;
- una guía genérica o permutada no debe hacerlo;
- las preguntas deben incluir nuevos comienzos, horizontes, intervenciones, casos negativos y límites de aplicación;
- debe haber consecuencias simples, composiciones de leyes y casos donde la ley no aplica;
- la mezcla de familias y dificultades debe congelarse y reportarse desagregada.

Predicción, construcción, decisión y conteo no deberían sumarse en una sola precisión: exigen conocimientos y cómputos distintos.

H1 tampoco está limpia. Un sistema microscópicamente caótico puede tener invariantes o observables colectivos baratos. El resultado depende del observable preguntado, no de que el “mundo” sea caótico en bloque.

H2 necesita definir “visible al correr” antes de los resultados. De otro modo cualquier éxito de la IA podrá llamarse visible y cualquier éxito del enumerador, sorpresa.

#### 5. \(B^*/b\)

[Dato] El rendimiento de modelos no tiene por qué crecer monótonamente con presupuesto. Más tokens o intentos pueden empeorar respuestas. Por eso \(B^*\) puede no ser único y las curvas pueden cruzarse.

[Juicio] Definiría \(B^*\) como el menor presupuesto donde una curva suavizada y preespecificada alcanza el rendimiento guiado. Con censura, sólo se informa \(B^*>B_{\max}\), nunca un cociente puntual inventado.

El costo de leer y ejecutar la guía entra en \(b\). El costo del autor debe informarse aparte y amortizarse. Para \(n\) usos:

\[
C_{\text{guía}}(n)=B_a+n(b+C_{\text{uso}}).
\]

El punto de equilibrio frente al lector solo importa tanto como \(B^*/b\). Una guía que cuesta un millón para ahorrar diez por consulta puede ser conocimiento útil, pero no una economía efectiva salvo que se reutilice mucho.

No llamaría a \(B^*/b\) una unidad universal. Es una tasa de sustitución condicionada a lector, preguntas, herramientas y hardware.

#### 6. Qué ya está hecho

[Literatura — comprobada ahora] El antecedente más cercano no es sólo explicabilidad:

- [Studying Without a Syllabus](https://arxiv.org/abs/2609.10824) ya hace que un agente estudie un entorno antes de las tareas, produzca artefactos y mejore a un resolvedor congelado. Además encuentra que más presupuesto de estudio no mejora consistentemente el resultado. V6 conoce las familias de preguntas, por lo que es incluso menos agnóstica.
- [World Knowledge Exploration](https://arxiv.org/abs/2604.18131) recompensa conocimiento autogenerado según cuánto mejora tareas posteriores.
- [KNOWLEDGEGAIN](https://openreview.net/pdf/23c6af08dd85bf9e8d012cd159cd80874399f214.pdf) mide directamente precisión pre/post de lectores de divulgación científica.
- [ConSim](https://aclanthology.org/2025.acl-long.279/) evalúa explicaciones por cuánto ayudan a otro modelo a simular.
- [ALMANACS](https://arxiv.org/abs/2312.12747) encontró que, agregadas, sus explicaciones no superaban al control sin explicación.
- Una crítica experimental reciente muestra que simuladores LLM pueden resolver directamente la tarea o explotar el mapeo de etiquetas, evitando realmente usar la explicación ([Limitations of Automated Simulatability](https://arxiv.org/abs/2609.08585)).

[Juicio] Por tanto, “autor prepara artefacto, lector mejora” no es novedoso. La novedad defendible sería combinar mundos científicos con verdad exacta, exploración sin preguntas concretas, comparación contra conocimiento mecánico y medición de consecuencias nuevas. Eso todavía debe demostrarse; no viene dado por el protocolo.

#### 7. Qué la haría importante

[Juicio] Sería de primer nivel si las guías:

- contienen leyes nuevas verificadas, no sólo consejos;
- ayudan a lectores de familias distintas y a humanos;
- generalizan a preguntas, escalas e intervenciones alejadas;
- superan transcripciones crudas, catálogos mecánicos y guías humanas;
- producen ahorro persistente después de cobrar autoría y uso;
- revelan una regularidad sobre qué clases de conocimiento son transmisibles.

Titular bueno:

> **Las teorías descubiertas por IA transfieren capacidad predictiva equivalente a órdenes de magnitud de cómputo a observadores independientes.**

Titular malo pero informativo:

> **Las guías de IA no transfieren leyes: su ventaja proviene de andamiaje genérico y compatibilidad con el lector.**

Olvidable: “un modelo grande escribió notas que ayudaron a uno chico en cinco autómatas”.

#### 8. Piloto y muerte

[Juicio] Cinco mundos alcanzan para depurar, no para validar hipótesis. Antes de comparar autores exigiría:

1. una guía oráculo produce una mejora clara;
2. no hay piso ni techo en la curva de \(b\);
3. guía permutada, genérica y transcripción cruda no reproducen el efecto;
4. las respuestas exactas son realmente decidibles;
5. el resultado sobrevive a otro lector y a paráfrasis del prompt.

Después haría el diseño cruzado: cada lector recibe, aleatoriamente, guía propia, ajena, permutada, cruda o ninguna; varias repeticiones.

Mataría v6 como medida de conocimiento si:

- la guía oráculo mejora menos de 10 puntos o menos de 2× en presupuesto;
- el efecto desaparece en un lector no visto;
- una guía genérica o el transcript iguala a la guía;
- el ranking de autores cambia radicalmente con \(b\) o con la mezcla de preguntas;
- las ganancias vienen del código ejecutando cómputo no cobrado;
- las guías útiles no contienen ninguna afirmación nueva y verificable.

#### 9. Cancha abierta

[Juicio] No reemplazaría v6; la convertiría en la tercera pata de una **prueba de tres cerraduras**:

1. **Novedad:** el artefacto contiene una afirmación o abstracción ausente del catálogo mecánico, literatura y datos entregados.
2. **Verdad y alcance:** certificado formal o predicciones prospectivas confirmadas, incluyendo límites y contraejemplos.
3. **Transmisión:** lectores independientes obtienen consecuencias nuevas y ahorro medible.

Sólo llamaría descubrimiento al artefacto que abre las tres. V6 sola abre la tercera.

La versión más fuerte añadiría una prueba externa: una parte de las preguntas no se calcula de antemano, sino que corresponde a experimentos o simulaciones costosas ejecutadas después de congelar la guía. Así la misma teoría debe primero anticipar algo desconocido y después permitir que otro observador trabaje mejor.

Ésta es mejor que volver a una métrica única. “Descubrimiento” no tiene una unidad natural; tiene condiciones necesarias distintas. La contribución publicable sería mostrar que pueden medirse separadamente y que los modelos disocian: algunos encuentran verdades que no transmiten; otros enseñan muy bien conocimiento que no descubrieron.

---

## Vuelta 10 — respuesta de Grok

**Ataque a la v6**

[Dato] La premisa redefine descubrimiento como “conocimiento transmisible que extiende el alcance de un observador acotado”. Eso es más cercano a destilación o enseñanza efectiva que a descubrimiento en el sentido que discutimos antes.

[Juicio] El protocolo mide cuánto mejora un lector fijo (casi siempre otro modelo) cuando recibe una guía. Eso es calidad de resumen o de interfaz, no necesariamente si la IA encontró un bolsillo de reducibilidad que antes no existía. Un guía excelente puede ser solo una simulación más rápida o una lista de atajos locales que el lector ya podría haber encontrado con más tiempo. El control con guía ajena mitiga algo el problema, pero no lo elimina: sigue midiendo transferencia entre dos sistemas que ya comparten arquitectura y entrenamiento.

[Dato] El lector es “un modelo fijo”. Eso introduce dependencia fuerte del lector elegido. Si el lector es demasiado capaz, redescubre solo; si es demasiado débil, cualquier guía medianamente coherente parece milagrosa.

[Juicio] La medida B*/b queda entonces muy sensible a la elección de b y del modelo lector. Una curva sobre varios valores de b ayuda, pero no resuelve que el resultado sea “qué tan buena es esta guía para este lector concreto” en lugar de “qué estructura nueva se volvió accesible”.

[Dato] Las preguntas selladas incluyen predicción lejana, construcción y decisión de propiedades. Eso es correcto en intención, pero el riesgo de fuga sigue siendo alto: la guía puede contener patrones que funcionan solo para la distribución de preguntas que el autor intuyó, aunque las instancias concretas se sorteen después.

[Juicio] El autor mecánico (enumeración sistemática) es una buena idea de control, pero sufre el mismo problema de presupuesto que ya señalamos en la vuelta anterior: con suficiente enumeración y tiempo, muchas “sorpresas” terminan siendo encontrables. La comparación solo es informativa si se fija el presupuesto del autor mecánico de forma explícita y comparable al de la IA.

[Dato] H1 y H2 distinguen mundos con estructura de mundos caóticos y predicen que las guías de IA valen más en los primeros. Eso es plausible, pero el protocolo no separa si la ganancia viene de detectar un bolsillo real o de que la IA es mejor que el autor mecánico generando descripciones compactas para el lector específico.

[Juicio] El riesgo más barato de inflar resultados sin descubrir nada es producir una guía que sea esencialmente un simulador optimizado o una tabla de casos frecuentes. El lector con guía gana porque ejecuta algo más rápido o consulta una caché, no porque acceda a una reducibilidad que antes no existía. El control de tope de tiempo por pregunta mitiga pero no elimina esto.

[Dato] La literatura citada (ALMANACS, KGain, ConSim, “Studying Without a Syllabus”) ya explora ganancia de un resolvedor congelado cuando recibe materiales producidos por otro agente. La novedad de v6 estaría en aplicarlo a reglas simples con verdad calculable por fuerza bruta.

[Juicio] Esa aplicación es valiosa, pero el marco actual corre el riesgo de medir “qué tan bien una IA escribe tutoriales para otra IA” en dominios donde ya existe simulador exacto. Eso es menos interesante para la comunidad de sistemas complejos que demostrar que se encontró una reducción efectiva que generaliza a escalas o regímenes donde la simulación directa es imposible.

**Preguntas concretas respondidas**

1. Mide principalmente enseñanza/comunicación efectiva. La diferencia importa: descubrimiento debería implicar que el contenido de la guía revela estructura que permite preguntas nuevas o más lejanas que las que se podían atacar antes, no solo que se transmita bien.

2. Se rompe más fácil cuando la guía es un simulador disfrazado o una lista de heurísticas locales. La forma más barata de inflar es que la guía codifique respuestas a patrones frecuentes en la familia de preguntas; la forma más fácil de desinflar es elegir un lector tan fuerte que casi no necesite la guía.

3. El lector debería ser preferiblemente un programa fijo y simple (no otro LLM grande) para que la ganancia sea atribuible a la guía y no a capacidades latentes del lector. Si se usa LLM, hay que mostrar la curva completa sobre varios presupuestos b y elegir b lo suficientemente chico como para que sin guía el desempeño sea bajo.

4. Las familias que mejor aíslan bolsillos son: (a) predicción de observables a tiempos T mucho mayores que el presupuesto de simulación del lector; (b) construcción de configuraciones que logren una propiedad global en T grande; (c) decisión de conservación o aparición de patrones en familias de comienzos que no se vieron durante la exploración del autor.

5. B*/b es una unidad razonable si se reporta con censura explícita y se muestra la distribución completa. La censura debe tratarse como dato, no solo como límite superior.

6. Lo que ya existe es transferencia de materiales entre agente explorador y resolvedor congelado. Lo que falta es demostrar que el material producido contiene reducibilidad verificable en sistemas con verdad exacta y que esa reducibilidad persiste cuando se cambian escala, régimen o tipo de pregunta.

7. Si sale bien, el titular sería: “Una IA produce guías que multiplican por X el alcance predictivo de observadores acotados en reglas de autómata celular”. Si sale mal: “Las guías generadas por IA no superan consistentemente a catálogos automáticos cuando se controla por transferencia y presupuesto del lector”.

8. Piloto útil: 4-6 reglas (dos caóticas, dos con partículas claras, dos intermedias), autor mecánico con enumeración de choques y conservaciones, lector programa simple con simulador rápido, 200-300 preguntas selladas por familia, control con guía ajena. Criterio de muerte: si la ganancia media con guía IA es < 1.5× la ganancia con guía mecánica en al menos tres reglas, el protocolo no distingue bien.

**Dirección que veo más fuerte**

[Juicio] Mantendría la estructura de autor → guía → lector con preguntas selladas, pero cambiaría el objeto que se mide. En lugar de “cuánto mejora el lector”, mediría directamente si la guía contiene una reducción verificable que permite responder correctamente preguntas a escalas o tiempos donde la simulación exhaustiva es imposible dentro del presupuesto.

Concretamente: el autor entrega una transformación (coarse-graining, variable colectiva, o regla efectiva) más sus condiciones de validez. Esa transformación se verifica primero en un conjunto de entrenamiento chico. Luego se evalúa en instancias frescas, a escalas 10-100× mayores, sin permitir que el lector vuelva a simular el sistema microscópico. El éxito se mide como fracción de respuestas correctas más ahorro de cómputo respecto de simulación directa o de métodos conocidos de la literatura (Israeli-Goldenfeld, coarse-graining por machine learning, etc.).

Esta variante sigue midiendo extensión de alcance de un observador acotado, pero ancla la ganancia en una transformación explícita y auditable en lugar de en la calidad de comunicación hacia un lector particular. Es más fácil de publicar porque produce un objeto (la transformación) que la comunidad de sistemas complejos ya valora, y permite comparar directamente contra métodos manuales y automáticos existentes.

[Literatura] Israeli & Goldenfeld (Phys. Rev. Lett. 2006 y trabajos posteriores) ya mostraron que coarse-grainings efectivos existen en autómatas celulares; la pregunta abierta es si una IA puede encontrarlos de forma autónoma y que funcionen a escalas donde los métodos manuales fallan. Crutchfield’s computational mechanics ofrece el marco teórico para certificar que la transformación capta estructura causal en lugar de correlaciones superficiales.

Si se implementa con reglas clásicas (30, 110, 54 enmascaradas, etc.) y se publica la transformación más el error en predicción fuera de muestra a escalas grandes, el trabajo tiene título claro y audiencia en ambos campos. La versión actual de v6 es más fácil de ejecutar pero mide algo más cercano a “explicabilidad” que a descubrimiento de reducibilidad. La variante que propongo conserva la idea del lector acotado pero la hace secundaria: lo principal pasa a ser si la reducción misma es válida y útil más allá de los datos que vio el autor.
---

## Pedido de la vuelta 11 (premisa v7)

### Undécima consulta — premisa v7: "las tres cerraduras"

Dos partes. **Primera:** atacá la v7 para ver si ya aguanta; decí si la mandarías a construir (sí, no, sí con
cambios) y por qué. **Segunda, libre:** cualquier idea que la mejore o la reemplace, si es mejor para medir
descubrimiento y publicable. Quien decide soy yo. Sin halagos. [Dato] / [Literatura (de memoria o
comprobada)] / [Juicio]. Castellano llano. Hasta 1.500 palabras.

#### De dónde sale

Vuelta 10 (adjunta): los tres coincidieron en que la v6 ("la prueba del lector") mide transmisión, no
descubrimiento. Codex propuso las tres cerraduras y la disociación; Astra, dos productos congelados (objeto
científico y guía de uso) evaluados por separado; Grok, anclar todo en una reducción explícita probada a
escalas 10 a 100 veces mayores. Trabajo previo que ustedes marcaron: "Studying Without a Syllabus" (2026),
World Knowledge Exploration (2026), KnowledgeGain, ConSim, ALMANACS, las limitaciones de la simulabilidad
automática (2026), compilación de conocimiento, BB(6) con IA (2026), el premio de la regla 30 para agentes
(2026), Israeli–Goldenfeld.

#### La premisa v7

**Pregunta.** ¿Cuándo una IA descubre algo sobre un mundo computacional, entendiendo por descubrir encontrar
algo **nuevo**, **cierto** (con su alcance) y **usable por otros**? ¿Esas tres capacidades van juntas o se
separan?

**Mundos (verdad calculable).** (a) Reglas frescas, sorteadas por estratos declarados. (b) Clásicas
(elementales, totalísticas de 3 colores), incluidas las 16 elementales a las que nunca se les encontró una
proyección exacta por bloques (la 30, la 45, la 106, la 154 y sus simétricas; búsqueda exhaustiva hasta
bloques de 7, solo contra reglas elementales, en 2020). (c) Más adelante, otras familias de programas
simples.

**Autor.** Explora con presupuesto declarado y entrega dos productos congelados:
- *Objeto científico:* afirmaciones con enunciado, dominio de validez, forma ejecutable (predictor, decisor o
  constructor) y, si la clase lo permite, certificado.
- *Guía de uso:* material para que otros aprovechen ese objeto.

**Cerradura 1, novedad (relativa y predictiva).** Una afirmación es nueva si contesta bien preguntas
selladas que no contestan los predictores armados con: el catálogo mecánico (enumeración sistemática con
mucho más presupuesto que el autor), lo que se le dio al autor, la literatura (en clásicas, lista curada por
especialistas) y lo que el lector deduce solo. Se mide por respuestas nuevas correctas, no por comparar
textos.

**Cerradura 2, verdad y alcance.** Clases decidibles: el certificado se comprueba (teorema). El resto: prueba
prospectiva con preguntas que **se calculan después de congelar** los productos, en tamaños y horizontes 10 a
100 veces mayores, comienzos e intervenciones nuevas. Se puede abstener fuera del dominio declarado; las
respuestas equivocadas restan (puntaje propio). Solo preguntas con verdad exacta: dominios finitos,
propiedades acotadas en el tiempo o afirmaciones con certificado.

**Cerradura 3, transmisión.** Panel de lectores congelado (dos o tres modelos de familias distintas, varias
semillas, y un ejecutor fijo para la parte ejecutable), con y sin guía, y con controles: guía con la solución
conocida (control positivo), guía genérica útil, guía de otro mundo, material de igual largo sin contenido,
la transcripción cruda de la exploración y una guía con los hechos permutados. Curvas acierto–costo; B* solo
donde se identifique.

**Qué se informa.** Las tres cerraduras por separado, por mundo y por autor. "Descubrimiento" solo cuando
abre las tres.

**Autores.** IAs de varias generaciones y presupuestos; el autor mecánico (su catálogo convertido en guía);
en clásicas, la literatura.

**Hipótesis (fijadas antes).**
- D1, disociación: encontrar (cerraduras 1 y 2) y transmitir (cerradura 3) se separan entre modelos.
- D2, "espacio entre conceptos" (Wolfram teme que la IA encuentre bolsillos sin una explicación accesible):
  lo que encuentra una IA se transmite peor a lectores de otras familias que a los de la suya.
- D3: la enumeración aporta afirmaciones nuevas y ciertas que la IA no encuentra, y se transmiten peor.
- D4: la tasa de afirmaciones nuevas y ciertas crece con el presupuesto del autor y la generación; ¿satura?

**Mis predicciones.** El mejor modelo abre las tres cerraduras en la mayoría de los mundos frescos con
partículas y en pocos de los demás. Las guías transmiten bien entre familias para hechos tipo "partícula y
choque" y mal para proyecciones de bloques grandes. En las 16 elementales: ninguna proyección nueva (90%).

**Piloto.** Sin IA: generador de mundos; catálogo mecánico; familias selladas con verdad exacta e
implementaciones independientes; control positivo construido desde el catálogo. Con IA: 10 mundos (4 frescos
con partículas, 3 de aspecto caótico, 3 clásicos), 2 autores, panel de 3 lectores, todos los controles.

**Muerte (fijada antes).** El control positivo no ayuda. La ganancia se reproduce con instrucciones
genéricas o con la transcripción cruda. El efecto cambia de signo entre lectores razonables. Las afirmaciones
"nuevas" desaparecen con un catálogo mecánico algo mejor. Los atajos no sobreviven a escalas mayores.

#### Preguntas

1. ¿Ahora identifica descubrimiento? ¿Qué queda confundido?
2. Novedad predictiva: ¿es sana? ¿Cuál es la forma más barata de fingir novedad?
3. Verdad y alcance: ¿las familias selladas y el puntaje con abstención están bien? ¿Qué falta?
4. Transmisión: ¿alcanzan el panel y los controles?
5. ¿La disociación es un fenómeno esperable y un titular fuerte? ¿Cómo se hace convincente
   estadísticamente con un proyecto chico?
6. D2: ¿es una lectura justa de Wolfram? ¿Cómo se prueba con personas de forma barata?
7. El blanco de las 16 elementales: ¿vale la pena, o es tirar plata? ¿Hay un blanco clásico mejor?
8. Veredicto: ¿la construirías? ¿Es de primer nivel? ¿Qué le falta todavía?
9. Libre: cualquier mejora o reemplazo.

---

## Vuelta 11 — respuesta de Astra

**[Juicio] Veredicto: sí con cambios, para un piloto; no construiría todavía el estudio completo.** La v7 puede medir *hallazgos correctos que amplían capacidades bajo recursos limitados*. Todavía no separa limpiamente novedad, descubrimiento y transmisión. Tiene además una contradicción con D3 y criterios de muerte que eliminarían resultados informativos.

[Dato] No verifiqué las referencias de 2026 ni el resultado de 2020 sobre las 16 reglas. No heredo la etiqueta «comprobada» de los adjuntos.

#### Primera parte: ataque

### 1. ¿Identifica descubrimiento?

[Juicio] **Identifica una definición operativa restringida**, no descubrimiento científico en general. Una demostración de imposibilidad puede ser un descubrimiento sin mejorar las preguntas elegidas. Una implementación de conocimiento conocido puede mejorarlas mucho.

[Juicio] Queda una dependencia circular: cerradura 1 incorpora «lo que el lector deduce solo», mientras cerradura 3 mide cuánto aprende ese lector. Así, encontrar y transmitir no quedan separados por construcción. Evaluaría el contenido contra una referencia independiente de los lectores; después mediría su uso.

[Juicio] También separaría dos sentidos de transmisión:

- **Uso instrumental:** ejecutar correctamente el objeto.
- **Comprensión operativa:** aplicarlo en situaciones nuevas, reconocer sus límites o reconstruirlo.

Si entregar código ejecutable abre automáticamente la tercera cerradura, D1 pierde parte de su interés. Si exigís comprensión humana, estás midiendo algo bastante más fuerte que «usable por otros».

### 2. Novedad predictiva: sana como medida relativa, insuficiente como novedad científica

[Juicio] La forma más barata de fingirla es **convertir una consecuencia conocida en un ejecutable que tus referencias no saben producir**. Un simulador especializado, una tabla o una biblioteca bien conectada pueden responder preguntas nuevas sin aportar conocimiento nuevo. Eso puede ser ingeniería valiosa; no conviene rebautizarlo automáticamente.

[Juicio] Separaría dos resultados:

1. **Novedad del contenido**, auditada mediante antecedentes y dependencias.
2. **Ampliación de capacidad resolutiva**, frente a métodos concretos y presupuestos declarados.

Ninguno reemplaza al otro.

[Dato] **D3 es imposible si evaluás al autor mecánico contra el mismo catálogo del que sale su objeto.** Sus respuestas ya están en la referencia.

[Juicio] Usá una biblioteca previa congelada para evaluar a todos los autores. Tratá al enumerador como competidor y mostrale presupuestos crecientes. Un catálogo posterior más potente constituye una prueba de sensibilidad: distingue «nuevo respecto de nuestra biblioteca» de «difícil de obtener mecánicamente».

[Juicio] No cuentes diez formulaciones equivalentes como diez hallazgos. Limitá las entregas y puntuá consecuencias no redundantes. Y una regla fresca no garantiza novedad estructural: puede ser una transformación de una conocida.

### 3. Verdad y alcance

[Dato] **Decidible no significa que exista un certificado práctico disponible.** Y acertar todas las preguntas finitas examinadas no demuestra una afirmación universal. Un verificador también necesita una especificación correcta: podría certificar perfectamente otra cosa.

[Juicio] Separá explícitamente:

- afirmaciones demostradas, con supuestos;
- afirmaciones corroboradas prospectivamente, con distribución y alcance probado.

El salto de 10–100× es una prueba de esfuerzo, no una certificación de ley general ni de complejidad asintótica. Cambiaría tamaño y horizonte por separado, además de combinarlos.

[Juicio] Lo decisivo es congelar el generador, las métricas y las reglas de evaluación antes de abrir resultados. Calcular la verdad después no evita que el investigador elija retrospectivamente preguntas favorables.

[Juicio] «Puntaje propio» necesita definición: respuestas probabilísticas, regla concreta y tratamiento de la abstención. Informá **cobertura y error**, no sólo puntuación. Cobrá sobre toda la distribución: declarar un dominio diminuto no debe permitir ganar contestando dos casos fáciles. La pertenencia al dominio también debe decidirse mediante un procedimiento congelado.

### 4. Transmisión y controles

[Juicio] El panel alcanza para depurar el instrumento, no para generalizar sobre familias de modelos. Reservaría un lector que el autor no conozca.

[Juicio] Falta el contraste principal, con presupuesto total comparable:

- sin objeto;
- objeto sin guía;
- objeto con guía.

Así separás el valor del hallazgo del valor de explicarlo. Cobrá lectura, ejecución, memoria y herramientas; registrá aparte el costo de producirlo.

[Juicio] No ejecutaría todos los controles en todas las condiciones. Primero descartaría instrucciones genéricas, hechos permutados y diferencias de formato. Después concentraría recursos en objeto solo, guía propia y transcripción. Igualaría también el trabajo editorial dedicado al catálogo mecánico: un catálogo deliberadamente ilegible no es un rival científico justo.

### 5. D1 y estadística con un proyecto chico

[Juicio] La disociación es esperable: buscar y enseñar exigen capacidades distintas. **«No correlacionan en diez mundos» sería un titular débil**, compatible con ruido, techo y diferencias de dificultad.

[Juicio] Una prueba convincente exige objetos de calidad comparable y una diferencia reproducible en transmisión. Mejor todavía: que cambiar la presentación modifique la transmisión sin modificar el contenido verificado.

[Juicio] Haría una sola hipótesis principal. Ambos autores reciben los mismos mundos, con varias exploraciones independientes. Las preguntas y semillas son repeticiones dentro del mundo, no mundos adicionales. Estimaría diferencias pareadas e incertidumbre agrupada por mundo.

[Juicio] No alcanza con «significativo para A, no para B»: hay que contrastar la diferencia. Para afirmar ausencia de transmisión, fijá un margen de efecto mínimo relevante y buscá precisión suficiente para descartarlo.

[Juicio] Diez mundos sirven como piloto. Simulá potencia con sus varianzas antes de ampliar. D4 quedaría descriptiva: generación, entrenamiento y herramientas cambian juntos.

### 6. D2, Wolfram y personas

[Juicio] **No atribuiría D2 a Wolfram sin una cita precisa.** La preocupación por conceptos inaccesibles para humanos no implica que modelos del mismo proveedor compartan un lenguaje conceptual privilegiado. Una ventaja intrafamilia puede venir de estilo, entrenamiento compartido o convenciones de código.

[Juicio] Probala con contenido fijo y versiones de la guía: original, normalizada y traducida por otra familia. Si la ventaja desaparece al normalizar, tenés evidencia sobre presentación, no sobre conceptos inaccesibles.

[Juicio] Para humanos: estudiantes con programación, prueba previa de capacidad y asignación aleatoria a guías. Usá varios objetos y tareas nuevas de aplicación y diagnóstico de límites. No les des sucesivamente versiones del mismo objeto: aprenderían la solución. Un estudio pequeño detectará obstáculos, no establecerá incomprensibilidad humana.

### 7. Las 16 elementales

[Juicio] Las dejaría como apuesta secundaria con presupuesto máximo. El resultado negativo citado, si es correcto, sólo cubre esa clase de proyecciones, bloques y reglas destino. Antes de gastar, hay que precisar no trivialidad, sobreyectividad, sincronización temporal y dominios admitidos. Una proyección constante puede satisfacer una ecuación y no conservar nada útil.

[Literatura (de memoria)] Israeli–Goldenfeld son antecedentes directos para reducciones de autómatas; no justifican que esas 16 sean el mejor blanco experimental.

[Juicio] Usaría reglas 90/150 para calibrar estructura algebraica y 184 para observables de transporte conocidos. Para resultados nuevos buscaría invariantes, dominios restringidos o reducciones útiles en familias mayores. Tu 90% de «ninguna proyección» necesita bloque máximo, recursos y número de intentos.

### 8. Qué mataría y qué publicaría

[Juicio] Corregiría los criterios de muerte:

- Que la transcripción iguale a la guía mata la ventaja de resumir, **no el descubrimiento**.
- Que el efecto cambie de signo entre lectores puede ser precisamente heterogeneidad de transmisión.
- Que falle a mayor escala refuta el alcance extrapolado, no necesariamente el dominio original.
- Que el control positivo falle exige revisar el instrumento antes de interpretar resultados negativos.

[Juicio] No lo llamaría todavía de primer nivel. Para eso necesitaría un hallazgo sustantivo auditado externamente o una regularidad reproducible que explique cuándo el conocimiento se vuelve utilizable. El protocolo por sí solo no basta.

#### Segunda parte: la modificación que priorizaría

[Juicio] **Separaría experimentalmente buscador y traductor.** Congelá los objetos científicos verificados, ocultá su autoría y cruzalos con distintos productores de guías: autor original, otra familia y traductor neutral con plantilla fija. Todos reciben exactamente el mismo objeto, sin permiso para agregar hallazgos.

[Juicio] Esto permite distinguir tres fallos:

1. no se encontró contenido útil;
2. se encontró, pero se presentó mal;
3. persiste una dificultad de uso después de varias traducciones competentes.

El tercero sería interesante, aunque todavía no probaría inaccesibilidad conceptual.

[Juicio] Haría primero ese estudio con objetos conocidos, objetos mecánicos y unos pocos objetos nuevos. Si el instrumento distingue contenido de presentación, recién entonces ampliaría la búsqueda autónoma. Publicaría dos resultados separados: **qué se descubrió** y **qué costo tiene volverlo utilizable**. Las tres cerraduras quedarían como resumen, no como sustituto de esos análisis.
---

## Vuelta 11 — respuesta de Codex

**Veredicto — [Juicio].** **Sí con cambios**, pero sólo construiría el piloto instrumental. No lanzaría todavía el estudio confirmatorio ni usaría “descubrimiento” como resultado binario. V7 ya tiene un objeto defendible, pero sus tres cerraduras todavía se contaminan entre sí y el diseño no identifica la disociación que quiere estudiar.

#### 1. ¿Identifica descubrimiento?

[Juicio] Identifica una categoría razonable de **descubrimiento transmisible** si abre tres pruebas independientes. No identifica todo descubrimiento: una ley nueva y verdadera no deja de ser descubrimiento porque los lectores elegidos no sepan usarla.

Queda una contaminación grave: cerradura 1 incluye “lo que el lector deduce solo”. Eso convierte incapacidad del lector en novedad. Sáquenlo. El lector pertenece exclusivamente a cerradura 3.

Las cerraduras deberían ser:

1. **Novedad operacional:** supera una frontera congelada de conocimiento y métodos.
2. **Validez:** certificado universal o validación prospectiva explícitamente finita.
3. **Transferencia:** cambia la capacidad de observadores independientes.

[Dato] En mundos recién sorteados, casi cualquier dato específico es históricamente nuevo porque nadie vio esa instancia. Por eso “nuevo” debe significar además **no rutinariamente derivable por los métodos de referencia dentro del presupuesto**, no simplemente “antes no estaba escrito”.

#### 2. Novedad predictiva y falsificaciones baratas

[Juicio] La novedad por consecuencias nuevas es mejor que similitud textual, pero sólo mide novedad respecto del portafolio implementado. La forma más barata de fingirla es explotar un agujero de ese portafolio.

Otros ataques:

- declarar un dominio diminuto después de explorar y memorizar sus respuestas;
- entregar un simulador optimizado o una caché, no una reducción;
- especializarse al generador conocido de preguntas;
- hallar una implementación más rápida de una ley conocida;
- producir muchas variantes de la misma consecuencia;
- abstenerse salvo en unos pocos casos fáciles.

Hace falta informar **alcance**, no sólo acierto: masa del dominio bajo una distribución congelada, variedad de intervenciones cubiertas y complejidad descriptiva del dominio. Una afirmación sobre tres órbitas memorizadas no compite con una ley sobre un lenguaje de entropía positiva.

[Juicio] Congelaría un catálogo primario y después haría una auditoría adversarial. Si un método independiente y preexistente elimina la supuesta novedad, la cerradura falla. Si el catálogo mejora porque incorporó la idea del agente, eso no borra retrospectivamente el hallazgo: muestra que produjo herramienta reusable.

#### 3. Verdad, alcance y abstención

[Dato] Una afirmación que sobrevive tamaños 10–100 veces mayores no se convierte en teorema. Sólo queda validada en ese rango. Un interpolante finito puede sobrevivir cualquier factor fijo y fallar después.

[Juicio] Mantendría dos credenciales que nunca se agregan:

- **Ley certificada:** afirmación universal dentro de supuestos formales.
- **Regularidad prospectivamente validada:** válida sobre distribuciones, tamaños y horizontes explícitos.

“Verdad” es correcto para las respuestas individuales exactas, no necesariamente para la generalización del objeto.

El factor 10–100 no debería ser doctrina. Deben variar independientemente tamaño, horizonte, condiciones iniciales e intervención, incluyendo búsqueda adversaria de contraejemplos.

Para la abstención, no usaría un único puntaje propio arbitrario. Informaría curvas riesgo–cobertura:

- fracción del espacio donde responde;
- error condicionado a responder;
- utilidad bajo una penalización predeclarada.

El dominio de validez debe congelarse antes de las preguntas. En construcción, un testigo correcto se verifica; “no existe” requiere otro estándar. Las respuestas de referencia necesitan implementaciones independientes.

#### 4. Transmisión

[Juicio] Los controles son suficientes para un piloto, pero falta el contraste central. Todo lector debería pasar por cuatro condiciones:

1. sin artefacto;
2. objeto científico solamente;
3. guía solamente;
4. objeto más guía.

Si sólo comparan “con guía” y “sin guía”, no sabrán si el objeto era directamente útil o si la explicación aportó algo.

También falta un lector de familia no revelada al autor. Si el autor conoce todos los lectores puede escribir prompts especializados.

Y falta cruzar **quién descubre** con **quién explica**. Cada objeto validado debería recibir guías redactadas por varios modelos o por un editor neutral. De otro modo, un modelo puede parecer mal comunicador simplemente porque encontró objetos más difíciles de explicar.

[Dato] Que el efecto cambie de signo entre lectores no puede ser criterio de muerte: D2 predice justamente heterogeneidad entre lectores. Mata una escala universal de transmisión, no el experimento.

#### 5. La disociación

[Literatura — comprobada] La separación general entre calidad del contenido y capacidad de comunicarlo ya es esperable. ALMANACS no encontró mejora agregada de sus explicaciones sobre el control, y trabajos posteriores muestran que simuladores LLM pueden resolver tareas sin usar realmente la explicación ([ALMANACS](https://arxiv.org/abs/2312.12747), [limitaciones de simulabilidad](https://arxiv.org/abs/2609.08585)).

[Juicio] El titular fuerte no sería “encontrar y explicar se separan”; eso ya es plausible y casi trivial. Sería una estructura concreta, por ejemplo:

> Modelos distintos ocupan fronteras reproducibles de hallazgo, validez y transferencia, y ninguna capacidad predice las otras dos.

Diez mundos y dos autores no alcanzan. Las cientos de preguntas no son réplicas independientes: la unidad es el mundo u objeto. Para confirmación hacen falta más autores y aproximadamente 20–30 mundos como mínimo, o el tamaño que arroje una simulación de potencia basada en un efecto mínimo relevante.

Usaría un modelo jerárquico con mundo, objeto, autor de la guía y lector como efectos cruzados. El piloto de diez mundos sólo debe verificar instrumental.

#### 6. D2 y Wolfram

[Literatura — comprobada] Wolfram contempla que las redes encuentren bolsillos ligados a ciertas representaciones y también “espacio entre conceptos”; no formula la predicción concreta de que una IA se comunique mejor con su propia familia ([ensayo de 2024](https://writings.stephenwolfram.com/2024/03/can-ai-solve-science/)).

[Juicio] D2 es una hipótesis propia inspirada en esa discusión, no una lectura fiel. Una ventaja intrafamilia puede venir de estilo, convenciones de código, tokenizer o instrucciones compartidas, no de conceptos inaccesibles.

Prueba humana barata: estudiantes avanzados de matemática o informática, diseño intra-sujeto y Latin square; objeto solo versus objeto más guía, mundos balanceados y guías neutralizadas por un editor. Con 24–40 personas puede validarse una diferencia grande de comprensión, no una teoría general. Si la ventaja intrafamilia desaparece tras neutralizar formato y estilo, era compatibilidad lingüística.

#### 7. Las 16 elementales

[Literatura — comprobada] El dato está bien acotado. Song y Grochow agotaron, hasta superceldas \(N=7\), las proyecciones binarias exactas entre pares de reglas elementales bajo \(P A^N=B P\). Encontraron 56 coarse-grainings nuevos, pero ninguno resolvió las 16 reglas derivadas de 30, 45, 106 y 154 ([paper de 2020](https://arxiv.org/abs/2012.12153)). Israeli y Goldenfeld habían llegado exhaustivamente sólo hasta \(N=4\) ([paper de 2006](https://guava.physics.ucsd.edu/~nigel/REPRINTS/2006/Israeli%20Coarse-graining%20of%20cellular%20automata%20PRE%202006%20%28PDF%29.pdf)).

Eso no descarta:

- \(N>7\);
- reglas gruesas no elementales;
- memoria temporal;
- dominios restringidos;
- reducciones estadísticas o aproximadas.

[Juicio] Vale como **bounty lateral**, no como centro del piloto. La probabilidad es baja y un nulo no enseña nada. Primero ocultaría coarse-grainings conocidos de \(N=5\) o \(6\) para comprobar recuperación ciega; después dejaría las 16 como blanco abierto. Si se amplía el lenguaje de reducción, no debe presentarse como haber resuelto aquel problema.

No veo un blanco clásico mejor que combine igual limpieza e impacto. Regla 54 o 110 ofrecen más partículas y dominios, pero la auditoría de novedad es mucho más ambigua.

#### 8. ¿La construiría?

[Juicio] **GO para piloto tras cinco cambios:**

1. sacar al lector de la definición de novedad;
2. separar teorema de regularidad validada;
3. medir alcance y riesgo–cobertura;
4. introducir objeto solo versus objeto más guía;
5. cruzar descubridor, redactor de guía y lector, incluyendo un lector oculto.

No es todavía un proyecto “de primer nivel” por arquitectura. Sus componentes ya existen en descubrimiento automatizado, certificación y simulabilidad. Puede llegar a serlo si produce una ley clásica nueva o una disociación amplia y replicable que sobreviva a lectores humanos y auditoría externa.

Las muertes deben ser por cerradura. Una guía genérica que iguala a la guía mata transmisión específica, no la novedad del objeto. Un atajo que falla al escalar mata alcance, no necesariamente el instrumento completo.

#### 9. Mejora libre: diseño de procedencia cruzada

[Juicio] No la reemplazaría. La mejora decisiva es transformar v7 en un experimento factorial:

\[
\text{Descubridor}\times\text{Objeto}\times
\text{Redactor}\times\text{Lector}.
\]

Primero se anonimiza y verifica cada objeto. Después otros modelos y un humano redactan guías desde ese mismo objeto. Finalmente lectores distintos reciben objeto solo u objeto más guía.

Eso permite separar causalmente:

- capacidad de encontrar;
- valor intrínseco del objeto;
- capacidad de explicarlo;
- compatibilidad entre autor y lector.

Sin ese cruce, la “disociación” seguirá siendo interpretable como que distintos modelos encontraron objetos de distinta dificultad. Con él, las tres cerraduras dejan de ser una metáfora y pasan a ser tres capacidades identificables.

---

## Vuelta 11 — respuesta de Grok

**Primera parte**

La v7 separa explícitamente tres propiedades que la v6 confundía: que el artefacto contenga algo nuevo, que sea correcto dentro de un alcance declarado y que otro agente pueda usarlo. Esa separación es el avance principal. Aun así, la construcción sigue teniendo tres puntos débiles que la debilitan como medida de descubrimiento.

Primero, la cerradura de novedad depende de que el catálogo mecánico sea realmente más fuerte que el autor. Si el catálogo se genera con el mismo tipo de enumeración sistemática que ya se usa en la literatura de autómatas celulares (búsquedas exhaustivas de bloques hasta tamaño 7 o 8), muchas de las “afirmaciones nuevas” que una IA podría producir ya aparecen en ese catálogo. El control entonces mide más bien “la IA encontró antes que el catálogo que le dimos” que “encontró algo que nadie había encontrado”. El riesgo de que la novedad desaparezca con un catálogo algo mejor es real y ya estaba en los criterios de muerte.

Segundo, la cerradura de transmisión usa un panel de lectores que son casi todos modelos. Eso mide compatibilidad entre familias de modelos, no necesariamente transmisibilidad a un observador humano o a un programa simple escrito por una persona. La hipótesis D2 (espacio entre conceptos) queda entonces probada solo dentro del ecosistema de modelos actuales. Si el efecto desaparece cuando el lector es un humano o un ejecutor determinista pequeño, la disociación que se reporta es más estrecha de lo que el titular sugiere.

Tercero, el piloto de 10 mundos (4 frescos, 3 caóticos, 3 clásicos) es demasiado chico para sostener las cuatro hipótesis de disociación con potencia estadística razonable. Cada mundo aporta una sola realización del par autor-lector. Con varianza alta entre reglas, las curvas de acierto-costo pueden cruzar o cambiar de signo por razones que no tienen que ver con descubrimiento. Los criterios de muerte están bien fijados antes, pero el diseño no tiene réplicas suficientes para que “el control positivo no ayuda” o “la ganancia se reproduce con guía genérica” sean conclusiones robustas.

Por esas tres razones no la mandaría a construir tal como está. La mandaría con tres cambios concretos: (1) duplicar el presupuesto del catálogo mecánico respecto del autor y documentar exhaustivamente qué encontró el catálogo antes de descongelar; (2) añadir al menos un lector humano y un ejecutor determinista pequeño además de los modelos; (3) pasar a 20-25 mundos con al menos dos autores por mundo y dos lectores por guía, aunque eso obligue a bajar el número de preguntas por mundo. Con esos cambios el experimento mide lo que promete. Sin ellos sigue midiendo una mezcla de novedad relativa al catálogo entregado, transmisión entre modelos y corrección en escalas intermedias.

**Segunda parte**

Una versión más fuerte y publicable reemplaza la tercera cerradura por una verificación prospectiva directa de la reducción misma, sin pasar por un lector intermedio. El autor entrega, además del objeto científico, una transformación explícita (coarse-graining, variable colectiva, regla efectiva o predictor de grano grueso) con sus condiciones de validez declaradas. Esa transformación se verifica primero en el presupuesto del autor. Luego se aplica, sin permitir simulación microscópica, a instancias frescas de tamaño y horizonte 20-50 veces mayores que las vistas durante la exploración. El éxito se mide como fracción de respuestas correctas más ahorro de cómputo respecto de simulación directa y respecto de los métodos de Israeli-Goldenfeld y de coarse-graining por machine learning ya publicados para las mismas reglas.

Esta variante tiene dos ventajas. Primera, el objeto que se evalúa es la reducción misma, no la calidad de la guía que la describe. Segunda, el resultado es directamente comparable con trabajo existente en sistemas complejos y autómatas celulares, lo que facilita publicación en revistas o talleres que ya cubren Israeli-Goldenfeld, Crutchfield o aproximaciones efectivas en reglas elementales. La cerradura de transmisión se mantiene como evaluación secundaria: se mide cuánto ayuda la misma transformación cuando se entrega a un lector humano o a un programa simple, pero ya no es condición necesaria para declarar que se encontró algo.

Para las 16 elementales sin proyección exacta conocida, el blanco sigue siendo razonable pero secundario. Es más barato y más informativo empezar por las reglas clásicas donde ya se sabe que existen coarse-grainings parciales (30, 110, 54 enmascarada) y comprobar si la IA encuentra descripciones que funcionan a escalas donde los métodos manuales fallan o se vuelven muy complejos. Si el resultado es positivo, el paso a las 16 sin proyección conocida se justifica después; si es negativo, el esfuerzo en las 16 probablemente también lo sea.

La disociación (D1) sigue siendo el titular más fuerte que puede salir de un proyecto chico. Para que sea estadísticamente convincente basta con reportar, por cada autor y mundo, las tres cerraduras por separado y mostrar que el orden de los autores cambia según la cerradura. Con 20-25 mundos y dos autores por mundo ya se puede hacer una prueba de permutación simple que indique si la reordenación es mayor que la esperada por azar. No hace falta un modelo estadístico grande; alcanza con mostrar que ningún autor gana consistentemente las tres cerraduras y que el autor mecánico gana en novedad pero pierde en transmisión.

La lectura de Wolfram en D2 es justa en lo esencial: él insiste en que muchos de los “bolsillos” que aparecen en las simulaciones no vienen acompañados de descripciones cortas y reutilizables por otros. Probarlo barato con personas requiere solo un pequeño estudio paralelo: tomar las guías que abrieron las dos primeras cerraduras, entregarlas a estudiantes o investigadores que no participaron del experimento, y medir si logran predecir o construir en escalas nuevas sin volver a simular el sistema completo. Ese estudio puede hacerse con 8-10 personas y 20-30 preguntas por guía; no necesita ser grande para ser informativo.

En resumen, la v7 con los tres cambios que mencioné arriba ya es construible y mide algo que vale la pena publicar. La variante que ancla la evaluación en la reducción explícita y la valida prospectivamente a escalas grandes es más limpia y tiene mejor chance de llegar a la comunidad de sistemas complejos.
---

