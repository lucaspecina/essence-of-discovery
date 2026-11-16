# Críticos, vueltas 6 y 7 (16-nov-2026): el reinicio desde cero

Lucas pidió repensar todo desde cero, con solo dos condiciones: que mida descubrimiento en el sentido de
Wolfram y que sea publicable e impactante. Estas son las dos primeras vueltas después de ese pedido. Abajo,
los pedidos y las respuestas completas de GPT Astra y Codex, sin tocar. Arriba, el resumen.

## Resumen

**Vuelta 6: cinco direcciones desde cero (C1 a C5).** C1 medir cuánto cómputo reemplaza lo que la IA
entiende; C2 leyes que emergen, demostradas (proyecciones exactas, emulaciones); C3 un censo de muchos
programas simples; C4 explicar lo que encontró la evolución; C5 descubrimiento acumulado.

- Los dos eligen, por separado, C2 como el objeto científico más defendible; C1 como contabilidad que
  acompaña; C3 para que el resultado sea general. C4 ya existe como superoptimización. C5 va después.
- Los dos rechazan la tesis "la irreducibilidad acota el retorno de la inteligencia" tal como estaba: no
  encontrar un atajo no prueba que no exista. Lo defendible es la frontera empírica de lo que encuentran
  observadores concretos.
- Un solo eje orden–caos sería un artefacto (la tesis del borde del caos fue reexaminada). Usar varios
  descriptores medidos aparte.
- Astra: para evaluar una ley descubierta no hace falta conocerla antes; se certifica y se mide su utilidad.
  Se pierde medir exhaustividad, no medir descubrimiento.
- Codex propone como dirección general "abstracciones predictivas que dependen del observador": una mirada,
  una dinámica reducida y un decodificador, con una frontera entre error, complejidad y costo. Astra propone
  abstracciones certificadas para verificar software real (más impacto, rivales maduros).

**Vuelta 7: la premisa v3, "leyes con comprobante".** Una ley es una terna de programas (dominio, mirada,
predictor) que la IA entrega con su comprobante; un programa nuestro la comprueba.

- Los dos: v3 es mejor apuesta que C1 sola y que la v2, porque puede producir matemática.
- El agujero central: mezcla teoremas con conjeturas que pasaron pruebas. Tienen que ir separados.
- Formas baratas de inflar: dominios diminutos, miradas constantes, esconder la simulación adentro de la
  mirada o del dominio, tablas guardadas, partir una ley en mil. Hace falta forma canónica por clase y no
  contar leyes.
- Dan definiciones mínimas de alcance, contenido y ahorro, y avisan que ninguna elimina la arbitrariedad.
- El dilema del lenguaje de leyes: abierto, no se puede comparar ni deduplicar; fijo, se vuelve síntesis
  dentro de una gramática, donde SAT gana. La ventaja posible de un agente es elegir la representación.
- "Sin jueces" es falso para novedad e importancia. La precisión de lo afirmado no es una medida nueva.
- Los sistemas criados no prueban nada sobre Wolfram sin controles emparejados.
- En sistemas clásicos, un resultado serio sería, por ejemplo, un factor no trivial nuevo de la regla 30 o
  la 110, o un dominio invariante nuevo con entropía positiva. Pide auditoría de especialistas.

**Qué decidí con esto.** Me quedo con el objeto de la v3, separo teoremas de conjeturas, fijo las clases de
ley y dejo libre su tamaño. La medida principal pasa a ser cuánto cómputo de búsqueda reemplaza la idea, y la
pregunta se ancla en frases textuales de Wolfram (v4, vuelta 8).

**Qué no se verificó.** Las referencias que citan "de memoria" no se comprobaron acá.

---

## Pedido de la vuelta 6 (cinco direcciones desde cero)

### Sexta consulta — volver a cero: cómo medir descubrimiento "según Wolfram" de forma publicable

Tu rol: crítico que piensa el problema conmigo. **No diseñes juegos.** Atacá, compará, decí qué pasaría si se
hace, qué falta y qué no estoy viendo. Sin halagos. Marcá [Dato] / [Literatura (de memoria o comprobada)] /
[Juicio]. Castellano llano. Hasta 1.300 palabras.

#### El reinicio

El dueño del proyecto pidió empezar de cero, sin ninguna de las condiciones anteriores. Quedan solo dos:

1. Tiene que ayudar a medir o evaluar **descubrimiento en el sentido de Wolfram** (la ciencia como
   observadores de cómputo acotado que encuentran bolsillos de reducibilidad en sistemas irreducibles; la
   ruliología; "minar" el universo computacional), aunque no sea con mundos de Wolfram.
2. Tiene que ser **publicable e impactante a nivel mundial**. Una demo o algo chico no sirve.

Todo lo demás está abierto: el tipo de mundo, qué recibe la IA, el formato, y también las reglas anteriores
del proyecto.

#### Lo que ya sabemos (datos propios, pocos)

- Mundos dibujados por nosotros: los dos mejores modelos sacan la ley completa en minutos (6 partidas).
- Sistemas conocidos con los nombres cambiados: resueltos en 25 a 112 segundos (29 partidas).
- Tablas al azar: los modelos dicen "no sé"; ninguna respuesta segura y falsa.
- La v2 ("hacer pasar lo que vimos pasar"): ustedes dos predijeron empate entre la IA y un buscador por
  piezas, y curvas planas contra la rareza; propusieron medir recursos (R50) y no rareza.

#### Mi diagnóstico de fondo

Todo intento de tener "la respuesta" de antemano choca con lo mismo: si la armamos nosotros, se lee; si es
matemática conocida, se reconoce; si es natural, no sabemos qué había para encontrar. Propongo dejar de
preguntar "¿encontró lo que plantamos?" y medir otra cosa.

#### Candidatos (los cinco son míos; atacalos)

**C1. El precio de pensar.** Definición: descubrir = ahorrar cómputo irreducible. Medida: cuántos órdenes de
magnitud de fuerza bruta reemplaza lo que la IA entendió. Cómo: tareas con **precio mecánico exacto** (lo que
cuesta resolverlas enumerando, medido por nosotros con mucho más cómputo; exhaustivo en tamaños chicos), de
tres familias: (a) *predecir* lejos; (b) *provocar* (dar un comienzo, o una regla, que logre un resultado
dado); (c) *probar* (ver C2). Variables: la posición del mundo en el eje orden–caos (actividad de la tabla,
clases de Wolfram), la generación del modelo, el presupuesto de cómputo y el de tokens. Resultados buscados:
(i) ganancia G contra la enumeración ciega y contra un portafolio mecánico congelado; (ii) cómo cambia G a
lo largo del eje orden–caos (¿pico en el borde del caos, cero en el caos?); (iii) cruce en costo total:
cuándo es más barato pensar (tokens) que calcular (CPU); (iv) tendencia entre generaciones de modelos; (v)
cuánto se sustituyen cognición y cómputo. Tesis a probar: **"la irreducibilidad acota el retorno de la
inteligencia en el descubrimiento"**, que es la afirmación de Wolfram hecha medible.

**C2. Leyes que emergen, demostradas.** Un bolsillo de reducibilidad como objeto matemático exacto: un
morfismo entre el mundo y un mundo más simple. Dos formas: una mirada borrosa (agrupar casillas y proyectar)
bajo la cual el mundo obedece una regla propia (Israeli–Goldenfeld); o un conjunto de comienzos codificados
en bloques donde el mundo emula a otro más simple (las emulaciones de NKS). Se verifican con una cuenta
finita: son teoremas. Verdad completa por enumeración en tamaños chicos (sabemos todo lo que había);
frontera abierta en tamaños grandes; subproducto posible: resultados nuevos sobre reglas famosas (por
ejemplo, las que Israeli–Goldenfeld no pudieron reducir).

**C3. Hacer ruliología (censo).** Una batería fija y automática sobre miles de programas simples frescos de
varios tipos; mapa de qué es reducible para cada observador; ¿distintas IAs encuentran los mismos bolsillos?
(dependencia del observador); estimar cuánto queda sin encontrar por captura–recaptura.

**C4. Explicar lo que encontró la evolución.** Wolfram (2024) dice que la búsqueda adaptativa (evolución,
entrenamiento) encuentra "bultos de cómputo irreducible" sin explicación narrativa. Criamos reglas o
circuitos con una meta elegida por nosotros (sabemos qué hacen, no cómo) y pedimos a la IA el equivalente
exacto más corto o más rápido. Verificación exhaustiva en dominios finitos.

**C5. Descubrimiento acumulado.** Varias sesiones o agentes que heredan artefactos verificados en un
universo fresco: ¿el conocimiento verificado se acumula y acelera, o se satura?

Mi preferencia hoy: C1 como pregunta central, con las tres familias de tarea (predecir, provocar, probar =
C2) y el muestreo amplio de C3. C4 y C5 como extensiones.

#### Mis predicciones (contradecilas)

- En mundos con estructura de partículas: G contra la enumeración ciega, grande (3 a 6 órdenes); G contra
  el portafolio, cerca de 1.
- En mundos caóticos: G entre 1 y 10 (solo poda).
- Minar reglas (elegir la tabla): si el espacio de reglas es grande, la IA "ingenieriza" una regla y la
  tarea se vuelve trivial; si es chico, G chico.
- Costo total: pensar le gana a la fuerza bruta escrita en C recién por encima de cierto tamaño de
  problema, y solo donde hay estructura.
- Titular más probable: "la IA automatiza la búsqueda experta; el retorno de pensar cae a cero con la
  irreducibilidad".

#### Preguntas

1. Para cada candidato: ¿cómo falla o queda de juguete? ¿Qué resultado lo haría importante y cuál olvidable?
2. C1: ¿"órdenes de magnitud de fuerza bruta reemplazados" es una medida sana? Agujeros: definición del
   rival, contabilidad (tokens contra CPU), amortización, tareas donde el precio mecánico no es exacto.
   ¿Ya existe algo así?
3. ¿La curva a lo largo del eje orden–caos sería un hallazgo o un artefacto (de las tareas, del parámetro,
   del filtro)? ¿Qué eje usarías?
4. C2: ¿los morfismos exactos son un buen formato para "ley emergente"? ¿Qué dejan afuera? ¿Qué rival
   mecánico (por ejemplo SAT) lo vuelve trivial?
5. ¿Qué combinación apostarías para un artículo de primer nivel, y qué le falta para no ser "otro benchmark
   sintético"?
6. ¿Qué vería un revisor escéptico como el agujero principal?
7. Como sujeto: ¿qué harías en C1 y en C2, y dónde fallarías?
8. El piloto mínimo decisivo (primero sin IA, después con IA) y los criterios para matar la idea.
9. ¿Qué dirección que no estoy viendo cumple mejor las dos condiciones? (Una dirección, no un juego.)

---

## Vuelta 6 — respuesta de Astra

[Juicio] Tu diagnóstico exige demasiado: **no necesitás conocer todas las leyes posibles para evaluar una descubierta**. Podés certificarla y medir su utilidad sin conocer el óptimo. Perdés la posibilidad de medir exhaustividad, no la de medir descubrimiento. Tus partidas tampoco justifican concluir que cualquier mundo diseñado será legible.

#### 1. Cómo fallan los cinco candidatos

- **C1 — [Juicio]** Falla si mide cuánto mejora una biblioteca conocida sobre un enumerador deliberadamente torpe. Importante: reducciones reutilizables que cambien el escalado o desplacen algoritmos competitivos. Olvidable: millones de veces más rápido contra fuerza bruta, empate contra software experto. “Ahorrar cómputo irreducible” es una mala definición: lo ahorrado revela que **ese aspecto** era reducible.
- **C2 — [Juicio]** Es el candidato más limpio para certificar resultados, pero puede convertirse en síntesis de mapas pequeños. Importante: familias nuevas de reducciones, con consecuencias predictivas y demostraciones generales. Olvidable: redescubrir proyecciones conocidas o factores que descartan toda información interesante.
- **C3 — [Juicio]** Miles de programas no garantizan diversidad científica. Importante: regularidades robustas entre lenguajes, tamaños y observadores. Olvidable: catálogo de éxitos. Captura–recaptura es especialmente frágil: modelos con conocimientos y puntos ciegos compartidos pueden hacer parecer exhaustivo un censo muy incompleto.
- **C4 — [Juicio]** Compite directamente con síntesis y superoptimización. La evolución puede producir circuitos llenos de redundancias fáciles de limpiar. Importante: simplificar resultados que sobreviven a optimizadores fuertes. Olvidable: quitar código muerto. “Equivalente más corto” requiere demostrar optimalidad; verificar equivalencia no alcanza.
- **C5 — [Juicio]** Puede medir caché, recuperación documental o más cómputo acumulado. Importante: composición de conocimientos que acelere problemas diferentes bajo contabilidad completa. Olvidable: repetir casos cercanos con soluciones guardadas. Necesita separar transferencia de mera reutilización.

#### 2. C1: qué mide realmente G

[Dato] El costo exacto de enumerar es el costo de **un algoritmo**, no el precio intrínseco del problema. Enumerar exhaustivamente tamaños chicos no establece una cota inferior para algoritmos mejores.

[Juicio] G es sano como comparación operacional, no como cantidad de “inteligencia” o “irreducibilidad”. Para \(Q\) usos:

\[
G(Q)=\frac{C_{\text{rival}}(Q)}
{C_{\text{descubrimiento}}+C_{\text{verificación}}+C_{\text{uso}}(Q)}.
\]

Incluí también el preprocesamiento del rival. Publicá tanto ahorro por consulta como punto de amortización. No conviertas tokens en CPU mediante una constante universal: medí dinero, latencia, trabajo computacional y memoria por separado. Distinguí costo marginal de despliegue del costo de crear ambos sistemas.

[Juicio] El portafolio debe congelarse **después** de una preparación competitiva, con ajuste comparable y especialistas pertinentes. Si el costo exacto es inaccesible, informá intervalos o censura por presupuesto; no inventes órdenes de magnitud.

[Juicio] Predecir, provocar y probar tienen complejidades distintas: no agregaría sus G como si fueran una magnitud natural única.

[Literatura (de memoria)] Hay antecedentes en análisis amortizado, selección algorítmica, superoptimización y descubrimiento automático de algoritmos. AlphaTensor y FunSearch conectan búsqueda automatizada con mejoras evaluables. La novedad no sería contar aceleraciones, sino explicar **cuándo aparecen reducciones transferibles**.

#### 3. Orden–caos y tus predicciones

[Juicio] No usaría un eje único. Actividad de tabla, clases de Wolfram, sensibilidad a perturbaciones y compresibilidad miden cosas diferentes. Usaría varios descriptores independientes y mostraría cuánto depende la conclusión de cada uno.

[Dato] Apariencia caótica no implica dificultad predictiva: ciertos sistemas aditivos admiten atajos algebraicos. Una dinámica microscópica difícil puede tener observables colectivos fáciles.

[Juicio] Por eso contradigo “G entre 1 y 10 en caos” y “retorno cero”: dependen del observable y de la precisión exigida. Tampoco compraría tus 3–6 órdenes sin fijar rivales. Permitir elegir reglas puede abrir soluciones degeneradas, pero no vuelve trivial cualquier problema inverso.

[Juicio] Un pico en el borde del caos sería inicialmente sospechoso de selección de tareas. Comparar generaciones tampoco aísla inteligencia: cambian entrenamiento, herramientas y costos.

#### 4. C2: qué certifican los morfismos

[Dato] Una relación como \(\pi F^k=H\pi\) puede verificarse mediante condiciones locales finitas **si** están fijadas la localidad y las convenciones de bloques. Comprobar unos tamaños finitos no demuestra automáticamente el enunciado para todos los tamaños.

[Juicio] Separaría dos objetos: un factor describe una observación cerrada de la dinámica; una emulación sobre comienzos codificados describe un subconjunto especial, no necesariamente estados típicos.

[Juicio] Hay que penalizar proyecciones constantes, alfabetos gigantes y complejidad escondida en codificación o decodificación. Pedí información preservada y utilidad, no solamente conmutatividad. El censo exhaustivo será completo respecto del lenguaje y las cotas elegidas, no de todas las leyes posibles.

[Juicio] Quedan afuera leyes aproximadas, estadísticas, transitorias y válidas casi siempre: buena parte de la ciencia. SAT/SMT y síntesis guiada por contraejemplos son rivales obligatorios; pueden liquidar los tamaños modestos. Eso no vuelve trivial la búsqueda sin cotas.

#### 5. Mi apuesta editorial

[Juicio] Apostaría por **C2 como objeto verificable, C1 como consecuencia y C3 como prueba de generalidad**, no C1 con tres modalidades enormes desde el comienzo.

Para primer nivel falta al menos una contribución sustantiva: matemática nueva, algoritmos competitivos nuevos o una regularidad sobre descubrimiento que sobreviva cambios fuertes de representación y rival. Un benchmark amplio no reemplaza ninguna. Ninguna combinación garantiza impacto mundial.

#### 6. El agujero principal del revisor

[Juicio] “Llaman irreducibles a los casos donde sus métodos fallan y después concluyen que la irreducibilidad limita sus métodos”.

Ese círculo mata la tesis central. Si sustituís irreducibilidad por caos, cambiás el concepto sin resolverlo. Podés establecer límites **empíricos de observadores concretos**; no probar con esas curvas una afirmación general de Wolfram.

#### 7. Qué haría yo como sujeto

[Juicio] En C1 buscaría simetrías, conservación, linealidad, periodicidad y descomposición; después produciría código reutilizable. Mi ventaja probable sería reconocer familias y organizar búsquedas. Fallaría ante estructura inédita sin pistas, y podría confundir regularidad finita con ley.

En C2 propondría proyecciones y codificaciones familiares, delegando búsqueda y certificación al solver. No aceptaría mi explicación verbal como evidencia matemática.

#### 8. Piloto mínimo decisivo

[Juicio] **Primero sin IA:** un formato de certificado, tres tamaños crecientes y comparación entre enumeración, SAT/síntesis y código experto. Auditá degeneraciones, costo de verificar y existencia de reducciones útiles. Si el solver agota rápidamente el espacio admisible, C2 no ofrece margen interesante ahí.

**Después con IA:** presupuesto total comparable, repeticiones independientes, pruebas ocultas en tamaños mayores y amortización sobre usos nuevos.

Mataría esta formulación si:

- toda ganancia desaparece ante el rival competente;
- los certificados solo sirven en el tamaño observado;
- verificar y descubrir consumen el ahorro para cualquier volumen plausible;
- las conclusiones cambian de signo al cambiar representación o descriptor de caos.

Un resultado nulo solo importa si excluye una hipótesis precisa con margen suficiente.

#### 9. Una dirección que falta

[Juicio] **Descubrir abstracciones certificadas para verificar software y protocolos reales.** Ahí hay espacios de estados enormes, observadores acotados y reducciones que permiten responder preguntas antes inaccesibles, sin plantar una ley.

[Literatura (de memoria)] Interpretación abstracta, bisimulación y reducción de modelos ya ofrecen fundamentos y rivales fuertes.

[Juicio] La novedad tendría que ser descubrir automáticamente abstracciones que habiliten verificaciones antes inviables. Cumple mejor la exigencia de impacto que otro universo sintético, aunque cobra un precio: competir contra décadas de herramientas maduras, no contra enumeración ciega.
---

## Vuelta 6 — respuesta de Codex

**Diagnóstico general — [Juicio].** C1 no es todavía una tesis: es una contabilidad. C2 contiene el objeto científico más defendible. C3 puede darle generalidad. C4 ya vive dentro de superoptimización. C5 es una pregunta posterior. La afirmación “la irreducibilidad acota el retorno de la inteligencia” no queda identificada por medir poco ahorro: eso también puede significar que el agente o el portafolio son malos.

#### 1. Los cinco candidatos

**C1 — El precio de pensar.**

- Falla si llama “precio mecánico exacto” al costo de enumerar: eso es el costo de un algoritmo, no un límite inferior.
- Es importante si la IA cambia la **ley de escalamiento** —por ejemplo, exponencial a polinómica— en sistemas frescos, y no sólo gana seis órdenes en un tamaño arbitrario.
- Es olvidable si termina como tabla de dólares, tokens y segundos dependiente del hardware.

**C2 — Morfismos exactos.**

- Puede quedar de juguete si sólo encuentra proyecciones constantes, casi identidades o reducciones que SAT enumera.
- Sería importante si produce morfismos nuevos y no triviales en reglas estudiadas, con certificado y reducción real de costo predictivo.
- Es el único candidato cuyo producto puede ser simultáneamente descubrimiento matemático, explicación ejecutable y resultado verificable.

**C3 — Censo.**

- Un atlas de miles de reglas es descriptivo. “Las IAs ven cosas distintas” puede ser una tautología sobre sus algoritmos.
- Sería importante si encuentra leyes de escala que predicen, antes de explorar, qué sistemas admiten qué clase de reducción.
- Captura–recaptura es frágil: la detectabilidad de los hallazgos será extremadamente heterogénea, condición que vuelve no identificable el total faltante. Esto está documentado en la literatura estadística de captura–recaptura. [Artículo primario](https://academic.oup.com/biometrics/article-abstract/59/4/1123/7288615).

**C4 — Explicar evolución.**

- “Equivalente exacto más corto” es superoptimización, no necesariamente explicación.
- En dominios chicos será búsqueda; en dominios grandes, demostrar equivalencia será el cuello.
- STOKE ya busca programas equivalentes más rápidos y AlphaEvolve optimiza programas con evaluadores. Sería importante sólo si encuentra una abstracción transferible o un teorema, no otro circuito menor. [STOKE](https://arxiv.org/abs/1211.0557), [AlphaEvolve](https://arxiv.org/abs/2506.13131).

**C5 — Acumulación.**

- Confunde conocimiento acumulado con más contexto, más cómputo y selección de éxitos.
- Sería importante si una biblioteca verificada reduce el costo de descubrimiento en **mundos nuevos**, frente a controles con igual cantidad de tokens, artefactos aleatorios y registros crudos.
- Como artículo central es prematuro; como segunda etapa, sí.

#### 2. ¿Es sana la medida de C1?

**[Literatura — comprobada]** FunSearch y AlphaEvolve miden mejoras verificadas contra métodos previos; superoptimización mide equivalencia y velocidad. No encontré una unidad aceptada que convierta tokens, inferencia, CPU y búsqueda en “precio de pensar”. [FunSearch](https://www.nature.com/articles/s41586-023-06924-6).

**[Juicio]** Usaría tres cantidades separadas:

1. costo único de descubrir el método;
2. costo marginal por instancia;
3. costo amortizado después de \(n\) usos.

Y reportaría dólares, energía o FLOP, tiempo de pared y actualizaciones del mundo por separado. Los pesos del modelo contienen una inversión de entrenamiento imposible de atribuir; el claim debe limitarse al costo marginal.

La medida fuerte no es “órdenes ahorrados en \(n\)”, sino diferencia entre curvas:

\[
C_{\text{método}}(n)\quad\text{contra}\quad C_{\text{portafolio}}(n).
\]

Sin una cota inferior no se puede hablar de irreducibilidad, sólo de ventaja frente al mejor rival conocido.

#### 3. El eje orden–caos

**[Literatura — comprobada]** La tesis de Langton sobre el borde del caos fue reexaminada por Mitchell, Hraber y Crutchfield; \(\lambda\) no ordena limpiamente capacidad computacional. [Reexamen](https://arxiv.org/abs/adap-org/9303003).

**[Juicio]** Una curva contra clase de Wolfram o actividad será principalmente un artefacto del muestreo. Usaría un espacio, no un eje:

- tasa de entropía: imprevisibilidad producida;
- información mutua/exceso de entropía: estructura almacenada;
- propagación de perturbaciones;
- tiempo de mezcla/transitorio;
- compresibilidad empírica.

Se miden antes y fuera de las tareas. La predicción interesante sería una superficie: poco retorno cuando no hay incertidumbre, poco cuando hay incertidumbre sin estructura reutilizable, máximo cuando coexisten estructura y novedad.

#### 4. C2 como ley emergente

**[Literatura — comprobada]** Israeli–Goldenfeld verifican relaciones del tipo \(P\circ F^N=G\circ P\), encontraron reducciones incluso desde reglas complejas hacia reglas simples y enumeraron todas las proyecciones sólo hasta superceldas pequeñas; el espacio crece brutalmente. [Trabajo completo](https://arxiv.org/abs/nlin/0508033).

**[Juicio]** Es un formato excelente pero angosto. Deja afuera:

- leyes estadísticas o aproximadas;
- invariantes y cantidades conservadas;
- leyes válidas sólo en un dominio de condiciones;
- partículas y coordenadas no locales;
- reducciones con memoria.

SAT puede volver trivial una gramática pequeña; eso no invalida C2, pero obliga a comparar contra SAT, refinamiento de particiones y simetrías. Además hay que excluir proyecciones constantes y puntuar cuánto se pierde, cuánto se conserva y cuánto acelera realmente.

#### 5. Combinación para primer nivel

**[Juicio]** Apostaría a:

- **C2 como producto científico:** nuevas leyes exactas;
- **C1 como contabilidad:** costo y cambio de escalamiento;
- **C3 como marco de muestreo:** qué tan general es el efecto.

El artículo no debe titularse “benchmark de descubrimiento”. Debe presentar un método que produzca resultados matemáticos nuevos, una frontera que los buscadores existentes no alcanzaban y una ley empírica que prediga dónde aparecen. Sin descubrimientos nuevos fuera del propio conjunto de prueba, seguirá siendo sintético.

#### 6. Agujero principal para un revisor

**[Juicio]** La variable independiente “irreducibilidad” no está observada. Fracasar en hallar un atajo no demuestra que no exista; hallar uno demuestra reducibilidad de esa propiedad, no del sistema completo. El claim defendible es sobre la **frontera empírica de reducciones descubribles por observadores acotados**, no sobre un límite fundamental de la inteligencia.

#### 7. Qué haría yo

**[Juicio]** En C1 buscaría primero linealidad, simetrías, invariantes, periodicidad, factorización y representaciones espectrales; luego programaría búsqueda y síntesis. Ganaría donde una de esas bibliotecas aplica y probablemente empataría con el portafolio experto. Fallaría en estructura nueva que exija varios pasos intermedios.

En C2 escribiría la ecuación de conmutación, reduciría por simetrías y usaría refinamiento de particiones y SAT. Espero dominar escalas chicas y fallar cuando explote el alfabeto de superceldas o la reducción correcta esté fuera de la gramática local.

#### 8. Piloto mínimo decisivo

**Sin IA:**

1. Reproducir los resultados conocidos de Israeli–Goldenfeld.
2. Congelar checker, criterio de no trivialidad y portafolio SAT/refinamiento/enumeración.
3. Localizar una escala donde el portafolio resuelva entre 10% y 70%: menos no da positivos; más no deja espacio.
4. Confirmar que los morfismos encontrados producen ahorro predictivo que cambia con el tamaño.

Matar si sólo aparecen proyecciones triviales, si el portafolio agota la frontera o si el certificado no produce ahorro real.

**Con IA:**

- Sistemas retenidos y frescos, mismo acceso a herramientas, varios modelos y presupuestos.
- Resultado primario: certificados válidos fuera del alcance del portafolio, no texto ni tasa de intentos.
- Exigir varios resultados independientes en más de una familia y una mejora de escalamiento o rendimiento reproducible.

Matar si los “descubrimientos” aparecen al darle al portafolio el mismo cómputo adicional, si la IA sólo invoca SAT o si toda ventaja es un factor constante de ingeniería.

#### 9. Dirección faltante

**[Literatura — de memoria]** La mecánica computacional estudia estados causales: la representación mínima suficiente para predecir un proceso.

**[Juicio]** La dirección más fuerte es **descubrimiento automatizado de abstracciones predictivas dependientes del observador**. El objeto no sería solamente un morfismo exacto, sino un codificador, una dinámica reducida y un decodificador, medidos por una frontera entre error predictivo, complejidad descriptiva y costo computacional. C2 sería el extremo de error cero; las leyes estadísticas y naturales entrarían en el resto de la frontera. Esto conecta ruliología, renormalización, modelos de mundo y ciencia real. Para ser mundialmente importante tendría que producir nuevas abstracciones útiles, no sólo una curva más sobre autómatas.

---

## Pedido de la vuelta 7 (premisa v3)

### Séptima consulta — premisa v3: "leyes con comprobante"

Tu rol: crítico. **No diseñes un juego ni propongas otra línea.** Atacá esta premisa, discutí con el otro
crítico (su respuesta de la vuelta anterior va adjunta) y decí qué pasaría si se prueba. Sin halagos. Marcá
[Dato] / [Literatura (de memoria o comprobada)] / [Juicio]. Castellano llano. Hasta 1.300 palabras.

#### Qué tomé de la vuelta 6

- No hace falta conocer las leyes de antemano para evaluar una que se descubre: se certifica y se mide su
  utilidad. Se pierde medir exhaustividad, no medir descubrimiento.
- El objeto defendible son las reducciones exactas (C2). La contabilidad de costos (C1) va como consecuencia:
  curvas de costo contra un rival competente, con tres costos separados. El muestreo amplio (C3) da
  generalidad.
- El objeto general es una abstracción predictiva: una mirada (codificador) y una dinámica reducida, con una
  frontera entre lo que dice y lo que cuesta.
- No afirmar nada sobre "irreducibilidad": hablar de la frontera empírica de reducciones que encuentran
  observadores concretos.
- Hace falta un aporte sustantivo: matemática nueva, o una regularidad robusta sobre dónde aparecen las
  reducciones.

#### La premisa v3

**1. El cambio de fondo: de la clave de respuestas al verificador.** No plantamos nada ni necesitamos saber
la respuesta. La IA trae una ley con su comprobante y un programa nuestro la comprueba. Se aprovecha la
diferencia entre encontrar y verificar.

**2. Qué es una ley (el objeto).** Una manera de saber algo del futuro de un sistema sin correrlo entero,
válida en un conjunto declarado de situaciones. Una terna de programas: un dominio D cerrado bajo la
dinámica F; una mirada φ (qué se predice); un predictor G tal que φ(F^t(x)) = G(φ(x), t) para todo x en D.
Casos: cantidad conservada (G no cambia nada); ley borrosa (φ agrupa casillas y proyecta:
Israeli–Goldenfeld); dominio invariante (un lenguaje regular cerrado donde el sistema se porta simple:
Hanson–Crutchfield); atajo total (φ es todo el estado: `outrun`); emulación (D es la imagen de una
codificación de otro sistema).

**3. Comprobación, en dos niveles siempre declarados.** (a) Prueba finita cuando D, φ y G son locales o
regulares: cuenta exhaustiva de vecindarios, inclusión de lenguajes. (b) Cuando son programas generales:
exhaustivo en tamaños chicos, muestreo grande y búsqueda adversaria de contraejemplos con nuestras
herramientas. Una ley que cae no puntúa y cuenta como afirmación falsa.

**4. Cuánto vale una ley.** Tres medidas: **alcance** (cuánto del espacio de estados cubre D), **contenido**
(cuánta información del futuro entrega φ) y **ahorro** (la curva de costo del predictor contra la mejor
cuenta directa; importa el cambio de escalamiento, no la constante). Se excluye lo trivial (proyección
constante, identidad, lo que ya da el cono de luz) y solo puntúa lo que queda por encima de la frontera de
un **portafolio mecánico congelado**: enumeración, SAT/CEGIS, refinamiento de particiones, invariantes
aditivos por álgebra lineal, detección de ciclos, hashlife, álgebra lineal para reglas aditivas.

**5. Qué se mide de una IA.** Por sistema y por presupuesto (todo cobrado, sin convertir tokens en CPU):
(i) **rendimiento**: la frontera de leyes certificadas que entrega, contra la del portafolio; (ii)
**precisión**: qué fracción de las leyes que afirma sobrevive a la comprobación (tasa de descubrimientos
falsos); (iii) **costo**: de descubrir, de verificar y de usar, con el punto de amortización. En tamaños
chicos el portafolio enumera todo lo que hay dentro de una gramática: ahí también se mide exhaustividad.

**6. Dónde se corre. Tres poblaciones.** (a) Sistemas **clásicos**, muy estudiados (autómatas elementales,
totalísticos de tres colores, Life): cualquier ley certificada que no esté en la literatura es un resultado
nuevo; es la prueba de que el instrumento no es de juguete. (b) Sistemas **frescos**, sorteados, de varios
lenguajes (autómatas, máquinas de Turing, reescritura): evaluación sin contaminación, comparación entre
modelos y generaciones. (c) Sistemas **criados** por búsqueda adaptativa hacia una meta: Wolfram (2024)
afirma que son bultos de cómputo sin explicación; ¿se dejan reducir?

**7. La regularidad que se busca.** Con descriptores medidos antes y fuera de las tareas (tasa de entropía,
información guardada, propagación de perturbaciones, transitorios, compresibilidad): ¿qué predice dónde
aparecen leyes y de qué clase? ¿Vale igual entre lenguajes y entre observadores?

**8. Lo que no se afirma.** Nada sobre irreducibilidad intrínseca ni sobre límites de "la inteligencia".
Sí: la frontera empírica de leyes certificadas que encuentran observadores concretos, y cómo se mueve con
el modelo y con el presupuesto.

#### Afirmaciones (atacalas)

- **B1.** Esto mide descubrimiento en el sentido de Wolfram sin plantar respuestas y sin jueces.
- **B2.** El mismo instrumento sirve de examen (sistemas frescos) y de fábrica de resultados (clásicos).
- **B3.** La precisión de las leyes afirmadas es una medida nueva y útil por sí sola.
- **B4.** Por encima de las gramáticas chicas, donde SAT gana, la búsqueda guiada por hipótesis de un agente
  supera al portafolio: dominios, miradas no locales, leyes con aritmética.
- **B5.** Un piloto chico decide. Sin IA: reproducir Israeli–Goldenfeld y las cantidades conservadas
  conocidas, y ubicar la escala donde el portafolio logra entre 10 y 70%. Con IA: diez sistemas frescos y
  cinco clásicos.

#### Mis predicciones (contradecilas)

1. Sin IA: se reproducen los resultados conocidos; el portafolio domina las proyecciones por bloques hasta
   tamaño 4 (95%).
2. Con IA, en sistemas frescos con estructura: leyes certificadas por encima del portafolio (dominios y
   atajos) en más de la mitad de los sistemas (65%). Precisión de lo afirmado: 60 a 85% en el mejor modelo,
   bastante menos en los anteriores (70%).
3. En clásicos: resultados nuevos pero modestos, por ejemplo proyecciones con superceldas mayores o
   dominios no catalogados (50%). Algo llamativo sobre la regla 30 o la 110: menos de 10%.
4. Riesgo principal: que lo "nuevo" valga poco y que el valor dependa demasiado de cómo se pesen alcance,
   contenido y ahorro.

#### Preguntas

1. ¿Dónde se rompe? ¿Cuál es la forma más barata de inflar el puntaje sin descubrir nada (leyes triviales,
   mil variantes de la misma ley, dominios diminutos)? ¿Cómo se deduplica y se pesa?
2. ¿"Alcance, contenido, ahorro" se pueden medir sin arbitrariedad? Dá la definición mínima de cada una que
   aguante.
3. ¿B4 es creíble? ¿Dónde esperás que un agente le gane de verdad a SAT/CEGIS, y dónde no?
4. Leyes que son programas generales: ¿qué estándar hace que una ley "comprobada" no sea un falso positivo?
5. ¿Qué resultado sobre sistemas clásicos haría que un matemático o un físico de sistemas complejos lo tome
   en serio? ¿Cuáles son los objetivos concretos más plausibles?
6. ¿Qué vería hoy como agujero principal un revisor de primer nivel?
7. La población (c), los sistemas criados: ¿prueba algo sobre la afirmación de Wolfram o es otra tautología?
8. El piloto: ¿qué le cambiarías? Criterios para matar.
9. Veredicto: comparada con C1 sola y con la v2, ¿es mejor apuesta? ¿Qué le falta todavía?

---

## Vuelta 7 — respuesta de Astra

[Juicio] La rotura central es llamar **«certificadas» a dos cosas distintas: teoremas y conjeturas que sobrevivieron pruebas**. Astra separó encontrar de verificar; acepto esa separación, pero no implica que cualquier ley tenga una verificación barata. Codex pidió certificados generales: el nivel 3(b) no los entrega.

#### 1. El comprobante no siempre existe

[Dato] Para programas generales no hay un procedimiento completo que decida siempre la igualdad propuesta. Probar muchos estados, tamaños y tiempos no demuestra una afirmación universal. Una excepción puede aparecer después de cualquier horizonte ensayado.

[Juicio] El estándar mínimo para decir «certificada» es una prueba verificable de cierre de D, terminación sobre las entradas admitidas y ecuación predictiva, bajo supuestos explícitos. Lo demás es «contrastada hasta estas cotas». Agotar el presupuesto de verificación tampoco equivale a refutarla.

[Dato] La localidad permite comprobaciones finitas únicamente cuando un argumento demuestra que esas condiciones implican el resultado para todos los tamaños y tiempos. Además, algunas reducciones por bloques y emulaciones necesitan varios pasos de F por paso reducido: la imagen codificada puede ser invariante bajo Fᵏ, no bajo F.

[Juicio] **B1 exagera:** desaparece el juez de corrección dentro de un formalismo, no los juicios sobre interés, novedad y relevancia. Tampoco queda identificado todo «descubrimiento en el sentido de Wolfram».

#### 2. Inflar valor y deduplicar

[Juicio] El ataque más barato: declarar D como unas pocas órbitas conocidas, guardar sus futuros y presentar una tabla como predictor. Después dividir D, renombrar símbolos y desplazar bloques para fabricar novedades. Otro ataque: esconder la simulación en φ, en decidir pertenencia a D o en la decodificación.

[Dato] Excluir «identidad» contradice incluir `outrun`: un atajo total requiere φ identidad. Lo trivial no es esa mirada, sino no aportar ventaja. Del mismo modo, un dominio de medida pequeña puede contener una familia científicamente importante.

[Juicio] Dentro de clases decidibles, deduplicaría por particiones equivalentes bajo renombrado, simetrías declaradas y extensiones mecánicas; separar un dominio no debería multiplicar hallazgos. Fuera de ellas no existe una deduplicación semántica completa y decidible. Contar programas o certificados queda descartado.

[Juicio] Las definiciones mínimas, para una distribución declarada μₙ de estados de tamaño n, serían:

- **Alcance:** μₙ(Dₙ), como curva en n. No una cifra mezclando tamaños.
- **Contenido:** entropía de φ(Fᵗ(X)), condicionada a X∈Dₙ. Evita premiar bits duplicados; no mide importancia científica.
- **Ahorro:** costo rival dividido por costo de pertenencia, codificación, predicción y entrega efectiva del resultado, para **el mismo observable**, entradas y horizonte. Descubrimiento, almacenamiento y verificación entran en la amortización.

[Juicio] Ninguna elimina arbitrariedad: dependen de distribución, observable y recursos. Una frontera de Pareto evita sumar con pesos, pero no vuelve naturales los ejes. Además, curvas finitas no certifican un cambio asintótico de escalamiento.

#### 3. La precisión no es B3

[Literatura (de memoria)] Síntesis de programas, demostración automática y predicción selectiva ya distinguen corrección, aceptación y cobertura. La fracción de afirmaciones correctas no es nueva por sí sola.

[Dato] Si el comprobador es sólido, las leyes certificadas pasan por construcción. Si sólo hacés pruebas empíricas, medís supervivencia al comprobador, no la verdadera tasa de falsos descubrimientos.

[Juicio] Además, el modelo puede subir su precisión afirmando únicamente una conservación conocida. Hay que leerla junto con cantidad y valor de las afirmaciones. Tu predicción de 60–85% carece de interpretación hasta fijar qué cuenta como afirmación, abstención y fallo. Yo esperaría grandes cambios por instrucciones, no sólo por generación del modelo.

#### 4. B4: ventaja posible, comparación torcida

[Juicio] Esperaría ventaja del agente al reconocer una estructura algebraica, elegir coordenadas no locales o proponer un lema fuera de la gramática. No al recorrer tablas pequeñas ni resolver restricciones locales ya formalizadas.

[Juicio] Pero comparás un agente que puede escribir algoritmos con un portafolio congelado. Ganarle puede significar «faltaba una rutina», no superioridad general de búsqueda hipotética. El rival debe recibir preparación competente y presupuesto comparable.

[Juicio] Discrepo con Codex: que el agente invoque SAT no mata el resultado. Si encuentra una representación que vuelve resoluble el problema, ése puede ser el aporte. Hay que atribuir la ventaja, no exigir aislamiento de herramientas.

[Dato] «Bloques hasta tamaño 4» no fija dificultad: mapas de bloques binarios a binario suman 2¹⁶; de bloques ternarios a ternario, 3⁸¹. Tu 95% no se sostiene sin alfabetos y restricciones.

#### 5. Clásicos: novedad no equivale a resultado sustantivo

[Juicio] **B2 sólo vale técnicamente:** el mismo comprobador puede servir para ambos usos. La novedad bibliográfica necesita otra auditoría; el interés científico, otra argumentación.

[Juicio] Objetivos plausibles: una familia de dominios invariantes descrita uniformemente, una clasificación completa de factores mínimos dentro de cotas relevantes, o una reducción con consecuencias nuevas para transporte, defectos o predicción. Una proyección mayor obtenida levantando otra conocida aporta poco aunque nadie haya publicado esa tabla.

[Juicio] Esperaría más redescubrimientos y extensiones mecánicas que resultados nuevos sustantivos. «Algo llamativo» sobre 30 o 110 es demasiado elástico para asignarle probabilidad.

#### 6. El agujero del revisor

[Juicio] Ahora sería: **«¿Estudian estructura de los sistemas o afinidad entre representaciones, entrenamiento y buscadores?»** Medir descriptores antes no resuelve esa identificación. Entropía, transitorios y compresibilidad dependen del muestreo y de las escalas observadas.

[Dato] Sistemas recién sorteados evitan recuperar esa instancia exacta; no eliminan familiaridad con sus familias y trucos. Cambiar de lenguaje tampoco produce automáticamente poblaciones comparables.

#### 7. Sistemas criados

[Juicio] Sin una cita precisa de Wolfram y una afirmación operacional, no hay tesis refutable. Encontrar una reducción parcial no demuestra que todo el sistema tenga explicación; fracasar tampoco demuestra lo contrario.

[Juicio] La crianza selecciona estructura según su objetivo y representación. Si éstos favorecen invariantes, recuperarlos puede revelar ese sesgo. La población (c) describe qué encontraron estos observadores en esos sistemas; no prueba una tesis general sobre cómputo evolucionado.

#### 8. Piloto: puede matar, no decidir a favor

[Juicio] Separaría desde el inicio certificados y evidencia empírica; congelaría equivalencias y utilidad antes de evaluar; incluiría repeticiones y una auditoría posterior con rivales reforzados. «El portafolio logra 10–70%» necesita denominador: sistemas con algún hallazgo admisible, no leyes desconocidas. Elegir después la escala favorable sesga el examen.

[Dato] Seis éxitos en diez sistemas dan aproximadamente un intervalo binomial del 95% de 31–83%. Diez casos no establecen «más de la mitad».

[Juicio] Mi expectativa: reproducción parcial de conocidos, dominio mecánico en gramáticas chicas y pocas ventajas iniciales del agente; varias desaparecerán al mejorar el rival. Mataría la formulación si:

- la ventaja depende de aceptar pruebas finitas como certificados;
- desaparece cobrando codificación y verificación;
- los éxitos son variantes o dominios sin utilidad;
- cambia de signo con decisiones razonables de representación.

#### 9. Veredicto

[Juicio] Frente a C1 sola, la apuesta tiene un producto identificable; frente a v2, gana precisión del objeto pero introduce una falsa continuidad entre prueba y ensayo. Todavía faltan una noción defendible de utilidad, una comparación no sesgada y un resultado sustantivo. **El verificador no sustituye ninguna de esas tres cosas.**
---

## Vuelta 7 — respuesta de Codex

**Veredicto general — [Juicio].** V3 tiene un objeto científico, pero mezcla dos cosas incompatibles bajo “ley con comprobante”: teoremas certificados y programas que sobrevivieron pruebas. Además, \(D\), \(\phi\) y \(G\) permiten esconder casi toda la computación y fabricar infinitas leyes degeneradas. Espero que SAT domine las gramáticas fijadas, que la IA produzca muchos dominios chicos y conjeturas plausibles, y que aparezcan pocos resultados clásicos realmente nuevos.

#### 1. Inflar el puntaje, deduplicar y pesar

**[Dato]** Las trampas baratas son:

- \(D\) vacío, singleton, una órbita periódica o un lenguaje de entropía casi cero;
- \(\phi\) constante, casi identidad o una ley ya conocida relabelada;
- hacer que decidir pertenencia a \(D\) o calcular \(\phi\) corra secretamente la dinámica;
- guardar trayectorias en \(G\);
- partir una ley en mil subdominios;
- conjugaciones, renombres, potencias temporales y composiciones de la misma reducción.

**[Juicio]** No contaría leyes. Usaría una frontera Pareto de alcance, contenido, ahorro y longitud/costo de \(D,\phi,G\). Cada ley suma sólo la cobertura o información nueva respecto de las anteriores.

Dentro de gramáticas regulares se puede canonicalizar: DFA mínimo para \(D\), transductor mínimo para \(\phi\), símbolos y simetrías normalizados. Para programas generales, equivalencia y deduplicación exactas son indecidibles: ahí no existe un contador limpio. El otro crítico tenía razón sobre penalizar alfabetos gigantes, pero faltó llevarlo hasta esta consecuencia.

#### 2. Definiciones mínimas

Sea \(X_n\sim\mu_n\), con \(\mu_n\) congelada antes.

**Alcance:**

\[
A_n=\Pr_{\mu_n}(X_n\in D).
\]

Para lenguajes regulares agregaría la entropía topológica relativa:

\[
a=\liminf_n\frac{\log |D_n|}{\log |X_n|}.
\]

Así una órbita no parece amplia sólo porque fue elegida cuidadosamente.

**Contenido:**

\[
C_{n,t}=
\frac{H(\phi(F^t(X_n))\mid X_n\in D)}
     {H(F^t(X_n)\mid X_n\in D)}.
\]

Mide cuántos bits variables del futuro entrega, no cuántos bits ocupa el programa.

**Ahorro operacional:**

\[
S_{n,t}=
\frac{C_{\text{portafolio}}(n,t;\phi,D)}
 {C_D+C_\phi+C_G}.
\]

Incluye comprobar \(D\), codificar, predecir y decodificar. Descubrimiento y verificación se agregan sólo al calcular amortización.

**[Juicio]** Sigue dependiendo de \(\mu_n\), del modelo de costos y de qué observable se considera valioso. No hay ponderación no arbitraria. Por eso debe quedar multiobjetivo y mostrar sensibilidad a varias medidas predeclaradas.

#### 3. ¿Es creíble B4?

**[Juicio]** Parcialmente. SAT/CEGIS gana cuando ya están fijados:

- la gramática;
- el tamaño de bloques;
- el alfabeto;
- la forma de \(D\) y \(\phi\).

El agente puede ganar antes: eligiendo representación, proponiendo un dominio no obvio, componiendo transformaciones o inventando un invariante inductivo. Esa es una ventaja de **meta-búsqueda**, no de resolver mejor el SAT.

No compro 65% de sistemas frescos “con estructura”: esa frase permite seleccionar después. En reglas realmente sorteadas espero muchos casos sin ley exacta corta y victorias concentradas en linealidad, conservación y dominios periódicos. El control correcto es agente+solver contra automatización+el mismo solver.

#### 4. Programas generales

**[Literatura — de memoria]** La equivalencia universal de programas generales y muchas propiedades semánticas son indecidibles. Testing adversarial no las convierte en teoremas.

**[Juicio]** Deben existir dos pistas separadas:

1. **Ley certificada:** prueba formal comprobada por un kernel pequeño, certificado SAT/SMT, inducción sobre un autómata o decisión completa dentro de una DSL restringida.
2. **Conjetura resistente:** sobrevivió tamaños chicos, muestreo y búsqueda adversaria.

No pueden compartir el titular, la precisión ni la frontera. “No encontramos contraejemplo” no es “comprobada”. Para dominios finitos, la afirmación sólo vale dentro de ese límite.

#### 5. Qué tomaría en serio en clásicos

**[Literatura — comprobada]** Israeli–Goldenfeld agotaron proyecciones pequeñas y dejaron reglas sin reducir dentro de sus cotas. Hanson–Crutchfield formalizaron dominios regulares y partículas; las leyes de conservación aditivas ya tienen caracterizaciones y pruebas prácticas. [Coarse-graining](https://arxiv.org/abs/nlin/0508033), [dominios](https://csc.ucdavis.edu/~cmg/compmech/pubs/CompMech_of_CATitlePage.html), [conservación](https://arxiv.org/abs/math/0111014).

**[Juicio]** Resultados serios serían:

- un factor no trivial nuevo para regla 30 o 110, con alcance de entropía positiva y reducción estricta de complejidad;
- un dominio regular invariante de entropía positiva, antes desconocido, con dinámica cociente exacta;
- una familia general de reducciones acompañada por un teorema;
- una ley de conservación no cubierta por las clases automatizadas existentes.

Una proyección de 256 símbolos a 255 o un dominio periódico microscópico no alcanza. “No estaba en nuestra búsqueda bibliográfica” tampoco prueba novedad: necesita especialistas, equivalencia matemática e inspección independiente.

#### 6. Agujero principal del revisor

**[Juicio]** El lenguaje de leyes tiene un dilema:

- si queda abierto, los resultados no son comparables, deduplicables ni universalmente verificables;
- si se fija, el trabajo se convierte en síntesis dentro de una gramática.

Éste es hoy el agujero central. El segundo es que “sin jueces” es falso: novedad, importancia y no trivialidad exigen juicio científico. B3 tampoco es nueva por sí sola; precisión se usa en síntesis y demostración automática y se infla absteniéndose. Debe informarse a rendimiento o valor fijo.

#### 7. Sistemas criados

**[Juicio]** No prueban la afirmación general de Wolfram. Como mucho prueban si la búsqueda adaptativa cambia la frontera de reducciones respecto de controles emparejados por tamaño, comportamiento, fitness y costo de generación.

Sin esos controles es tautológico: se optimiza hasta obtener una conducta complicada y luego se declara que la evolución produjo complejidad. También puede ocurrir lo contrario: la evolución deja redundancia y módulos fáciles de comprimir. “Bulto irreducible” sigue sin variable observable.

#### 8. Piloto y condiciones de muerte

**[Juicio]** Cambiaría tres cosas:

1. separar desde el día uno teoremas y conjeturas;
2. atacar las métricas con un catálogo de leyes degeneradas antes de evaluar agentes;
3. usar los clásicos como prueba ciega: ocultar leyes conocidas y comprobar si el instrumento las recupera y ordena correctamente.

Diez frescos y cinco clásicos sólo depuran el aparato; no estiman 65% ni una regularidad entre lenguajes.

Mataría la premisa si:

- las degeneraciones permanecen en la frontera después de cobrar todos los costos;
- el ranking cambia radicalmente con \(\mu_n\);
- el portafolio agota toda gramática con alcance útil;
- ninguna ley formalmente certificada supera al portafolio en una muestra confirmatoria;
- las aparentes ventajas desaparecen al compartir herramientas y presupuesto;
- los resultados clásicos “nuevos” no sobreviven auditoría experta.

Para continuar exigiría varias leyes distintas, en más de un sistema, con certificado, alcance no nulo, ahorro de escalamiento y verificación independiente.

#### 9. Veredicto comparativo

**[Juicio]**

\[
\text{v3} \;>\; \text{C1 sola} \;>\; \text{v2}.
\]

V2 medía construcción inversa sesgada por su fábrica. C1 tenía una contabilidad sin objeto científico. V3 puede producir matemática.

Todavía le faltan cuatro cierres: lenguaje formal de leyes, separación teorema/conjetura, canonicalización contra duplicados y una auditoría externa de novedad e importancia. Sin eso será un generador de afirmaciones interesantes con una métrica negociable, no una medición publicable de descubrimiento.

---

