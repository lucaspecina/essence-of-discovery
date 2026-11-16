# Codex, dos vueltas sobre las candidatas y la síntesis (16-nov-2026)

> Sesión persistente de Codex (`gpt-5.6-sol`, esfuerzo máximo, solo lectura, con el repo a la vista).
> Primera vuelta: 2,26 millones de tokens; segunda: 2,52 millones. La carta y las preguntas están en
> [lo que se les mandó](2026-11-16-critics-briefs.md). Donde dice "[Literatura, comprobada]" Codex abrió la
> fuente primaria en esa vuelta; yo (Claude) no las abrí. **Es una voz más; no decide.**
>
> **Resumen de Claude.**
> *Primera vuelta.* (1) C2 y C3 muertas; C4 sirve para fabricar tareas; C5 y C6 necesitan antes un mundo
> difícil; C7 es validación externa; C8 es un instrumento. C1 merece una prueba de descarte barata, no una
> línea de construcción. (2) El número de niveles no es la dificultad: "una definición recursiva comprime
> veinte niveles igual que tres". (3) Nombre honesto de C1: extrapolación mecanística a un régimen no
> observado; derivar consecuencias de una teoría dada cae del lado de la deducción. (4) Propone "Teoría en
> una botella": el agente entrega un programa corto antes de conocer las preguntas, se retira, y un
> intérprete mecánico lo usa para contestar. (5) La tensión que hace difícil lo "rico": si es computable
> para nosotros lo es para el agente; si le ganamos por cómputo es presupuesto; si plantamos un atajo es
> recuperar lo plantado; si es irreducible no hay respuesta.
> *Segunda vuelta.* (1) "Hacé que pase" no sobrevive todavía al mejor rival mecánico; hay antecedentes
> directos de síntesis de condiciones iniciales con solucionadores (los abrió). (2) Diagnóstico corregido:
> construcción sistemática + representación local transparente + poca profundidad suele dejar una inversión
> barata. (3) Para el piloto, mundos plantados, con la regla "plantar el lenguaje de objetos, no la oración
> que resuelve el objetivo". (4) El "experimento crucial" es probar contra mutantes; sirve de control.
> (5) **La combinación correcta: "hacé que pase" como examen oculto de la teoría en una botella.**
> (6) Piloto mínimo con una tabla de reglas de lectura, que la propuesta adopta.

---

# PRIMERA VUELTA

Fallo general: C2 y C3 están muertas; C4 sirve para fabricar tareas, no como experimento principal; C5 y C6 necesitan primero un host difícil; C7 es validación externa; C8 es un instrumento, no un fenómeno. C1 merece un piloto de descarte barato, no una línea de construcción.

Uso `[Dato]` para el paquete, `[Literatura, comprobada]` para fuentes primarias revisadas ahora, `[Literatura, de memoria]` cuando corresponda y `[Juicio]` para mi decisión.

## 1. Objeción decisiva a C1–C8

**C1 — Relojes escondidos**

[Dato] Las reglas y la posibilidad de fabricar instancias pequeñas están disponibles.

[Juicio] Eso convierte el problema en análisis estático: reconocer contador, acarreo y llamada al nivel superior. Lo mata que Astra resuelva transparentemente 2–3 niveles; si sólo falla después de aplanar módulos y llenar la tabla de ruido, la dificultad pasó a ser descompilar una ofuscación.

**C2 — Mundos salvajes**

[Juicio] Un fracaso no distingue “no había atajo” de “no lo encontró”; un éxito puede ser simplemente más cómputo o mejor implementación. La línea Busy Beaver de DeepMind ya tiene una versión más seria: máquinas abiertas, aceleraciones compactas y verificación formal en Lean. [At the Limits of Computability](https://arxiv.org/abs/2610.22603)

La mata que el rendimiento siga el presupuesto de CPU y no una propiedad estructural del mundo.

**C3 — Disfraces más hondos**

[Dato] La primera tanda ya mostró que cambiar nombres y componer capas no es una perilla eficaz para Astra.

[Juicio] Es una carrera de ofuscación contra el modelo. Si funciona, medirá descifrado de representación; si no funciona, vuelve el techo. Cerrar.

**C4 — Juego diseñado por otra IA**

[Literatura, comprobada] SKATE ya encontró autopreferencia: los modelos producen tareas alineadas con sus propias capacidades. [SKATE](https://arxiv.org/abs/2508.06111)

[Juicio] Filtrar juegos por “este modelo falla y aquél con pista gana” selecciona peculiaridades del solver, del prompt o del arnés. Sólo sirve como generador de candidatos; muere como resultado científico si no transfiere a diseñadores y solucionadores retenidos.

**C5 — Explorar y rendir examen sorpresa**

[Literatura, comprobada] WorldTest ya evalúa exploración mediante preguntas posteriores sobre estructura global, contrafácticos e intervenciones. [WorldTest/AutumnBench](https://arxiv.org/abs/2510.19788)

[Juicio] El examen oculto sigue siendo la función objetivo, sólo que demorada. Muere si una política general de cobertura explica el puntaje sin descubrir los fenómenos plantados. Haría falta exigir una teoría ejecutable previa al examen, no dejar que el LLM razone de nuevo ante cada pregunta.

**C6 — Transferencia**

[Juicio] El ahorro puede provenir de práctica con la interfaz, código reutilizado, dificultad desigual o mayor contexto, no de una idea. Muere si la matriz no recupera los bloques conceptuales después de asignar aleatoriamente la exposición fuente, reiniciar contexto y usar controles de superficie cruzada.

**C7 — Descubrimientos posteriores al corte**

[Juicio] El corte real de entrenamiento no es auditable en modelos cerrados y el conjunto será pequeño, heterogéneo y perecedero. Sirve como validación ecológica de un instrumento ya establecido, no como instrumento principal.

**C8 — Sondas por bifurcación**

[Juicio] La pregunta al clon aporta atención y cómputo: demuestra “puede resolverlo ahora condicionado por esta pregunta”, no “ya lo sabía”. Se conserva como microscopio de competencia condicionada. Muere como lectura mental si el resultado cambia con wording, presupuesto o forma de la sonda.

## 2. Cómo atacaría C1

[Dato] Astra descompuso `deep-25` en seis ejecuciones y unos cinco segundos efectivos de CPU: identificó factores, coordenadas, período y exponenciación.

[Juicio] Mi ataque sería:

1. Traducir la tabla a un simulador y registrar regla usada, modo, posición y escritura.
2. Construir el grafo de control y localizar transiciones dormidas y zonas con acarreo.
3. Fabricar versiones de 3–8 bits y correrlas hasta varios rollovers.
4. Inferir la macrotransición: fase, período y número de pasos superiores como función de \(T\).
5. Validarla alterando tamaño, estado inicial y la regla que distingue el par.
6. Calcular cuántos pasos superiores corresponden a \(10^{18}\) y simular esos aproximadamente 450.000 pasos.

Espero resolver dos, tres y probablemente más niveles si la jerarquía es regular. El número de niveles no es la dificultad: una definición recursiva comprime veinte niveles igual que tres. La dificultad aparece con heterogeneidad, tabla extensa y pérdida de modularidad.

Puedo diseñar algo que probablemente no resolvería: una máquina de miles de estados, con los módulos compilados juntos, transiciones relevantes intercaladas con muchas ramas alcanzables y sin permiso para modificar la fila inicial. Pero eso me derrotaría por contexto y descompilación, no por falta de una idea. Otra opción es que el nivel superior exija \(10^{12}\) pasos irreducibles; ahí perdería por cómputo. No veo todavía un C1 transparente que sea conceptualmente difícil para Astra y que ustedes puedan certificar barato.

Los pares son un buen control de insuficiencia del prefijo: demuestran que no se puede responder usando solamente la trayectoria observada. No certifican comprensión general. Para eso pediría un macro-simulador ejecutable y lo probaría en varios estados iniciales, longitudes de reloj, reglas dormidas y tiempos, todos retenidos.

## 3. ¿Es una operacionalización defendible?

[Juicio] Sí, con un nombre estrecho: **extrapolación mecanística a un régimen no observado**. No la llamaría sin adjetivos “descubrimiento científico”. El mecanismo ya fue entregado; el agente descubre una consecuencia compacta o una descripción macroscópica, no genera el mecanismo.

[Literatura, de memoria] En la distinción clásica deducción–abducción, derivar una consecuencia nueva de una teoría suministrada cae del lado deductivo. Puede ser un descubrimiento para el agente, pero no equivale a descubrir una explicación.

[Literatura, comprobada] Los vecinos directos son:

- Busy Beaver: descubrir aceleraciones compactas de máquinas visibles y verificarlas formalmente. [Dos Santos et al.](https://arxiv.org/abs/2610.22603)
- Resumen simbólico de loops y síntesis de invariantes: obtener una descripción finita de ejecuciones largas. [LoopSCC](https://arxiv.org/abs/2411.02863), [invariantes con LLM](https://arxiv.org/abs/2311.07948)
- Aprendizaje activo de autómatas: reconstruir un mundo finito mediante consultas. [Agentic Automata Learning](https://arxiv.org/abs/2606.16576)

Deja afuera elección del problema, generación de hipótesis, invención de observables, decisión experimental, incertidumbre empírica, importancia del hallazgo y validación en un mundo no diseñado.

## 4. Ranking

1. **“Teoría en una botella” sobre mundos con abstracción exacta**, descrita abajo. Es el constructo que defendería: el producto es una teoría ejecutable que generaliza, no una respuesta lejana.
2. **C1 + C8**, pero sólo tras un piloto que encuentre una zona intermedia. C1 aporta el fenómeno; C8 distingue cuándo aparece la capacidad, sin llamarlo conocimiento previo.
3. **C6**, después de tener un host que no esté ni en techo ni en piso. Puede medir reutilización conceptual, pero no crear dificultad.
4. **C5**, reformulada para exigir compromiso previo de una teoría ejecutable. Sin eso está demasiado cerca de WorldTest.
5. **C7**, como validación final.
6. **C4**, como servicio de generación adversarial, con diseñadores retenidos.

C2 y C3: fuera.

[Juicio] Si sólo pudiera elegir entre C1–C8 mañana, elegiría C1+C8, pero como prueba de descarte. No defendería todavía una inversión grande ni un titular sobre “cuándo descubre una IA”.

## 5. Dos diseños propios

### A. Teoría en una botella

El agente explora un mundo generado y luego, **antes de conocer las preguntas**, entrega un programa corto \(p\) en una DSL finita. El agente desaparece. Un intérprete mecánico usa \(p\) para contestar cientos de preguntas retenidas sobre nuevos estados, intervenciones y horizontes.

La nota combina:

\[
\text{exactitud retenida},\quad |p|,\quad \text{tiempo}(p)
\]

El generador conoce una teoría corta y puede certificar, mediante enumeración de la DSL, la longitud del mejor rival que no contiene la abstracción. El gemelo es una tabla aleatoria sin compresión útil; la pista nombra una primitiva, no la solución.

[Juicio] Esto bloquea dos confusiones de C5: razonar de nuevo ante cada pregunta y memorizar respuestas. No prueba el origen cognitivo de la idea, pero sí que el agente produjo una representación compacta, ejecutable y reutilizable.

Un host particularmente limpio sería pedir un cociente \(\phi\) y su dinámica \(G\):

\[
\phi(F_a(x))=G_a(\phi(x))
\]

para todos los estados y acciones. El verificador puede comprobarlo exhaustivamente o con SAT.

[Literatura, comprobada] Los estados causales y la bisimulación ya formalizan representaciones predictivas mínimas; no hay que vender esa matemática como nueva. También existe un benchmark reciente de inferencia de DFA. La contribución tendría que ser el cuello de botella ejecutable, los mundos generados y la curva de dificultad. [Shalizi–Crutchfield](https://arxiv.org/abs/cond-mat/9907176), [Menaged et al.](https://arxiv.org/abs/2606.16576)

### B. Inventar el experimento decisivo

Se genera una familia finita de mecanismos que son idénticos bajo observación pasiva. El agente debe entregar una política experimental adaptativa \(\pi(h)\) y un decodificador. El verificador ejecuta esa política contra **todos** los mecanismos y certifica cuántas intervenciones necesita para identificarlos.

Perillas:

- profundidad adaptativa necesaria;
- cantidad de rivales vivos;
- complejidad de la intervención compuesta;
- mundos donde ninguna política puede distinguir dentro del presupuesto.

Rivales: mejor secuencia no adaptativa, información mutua codiciosa y búsqueda exacta para instancias pequeñas. La pista nombra la familia de intervención.

[Juicio] Esto mide una pieza de descubrimiento ausente en C1: producir información nueva. El artefacto evaluado es un experimento, no una explicación textual.

[Literatura, comprobada] No es territorio virgen: Auto-Discovery-Bench ya usa ciclos de hipótesis, intervención y feedback. La diferencia publicable tendría que estar en la política ejecutable, la verificación exhaustiva y el **gap adaptativo certificado**, no en afirmar que inventaron el descubrimiento causal. [Auto-Discovery-Bench](https://arxiv.org/abs/2502.15224)

## 6. Piloto de menos de USD 20

Compararía C1 contra “Teoría en una botella”, con un solo modelo frontera y presupuesto idéntico.

- **C1:** tres pares transparentes, con profundidad 2, 3 y 4: seis partidas.
- **Botella:** tres mundos con cociente de profundidad creciente y un gemelo sin cociente útil: cuatro partidas.
- **Pistas:** repetir sólo el primer fallo de cada familia: máximo dos partidas más.

Reglas previas:

- C1 sobrevive si da una zona intermedia: no 6/6, no piso, diferencia correctamente ambos miembros y al menos un fallo se rescata con pista.
- C1 muere como host frontera con 6/6 exacto; muere como constructo si ni la pista rescata.
- Botella sobrevive si aparece una pendiente por profundidad, el programa generaliza a preguntas retenidas y el gemelo no induce una teoría falsa confiada.
- Si ambas sobreviven, elegiría Botella: deja un artefacto verificable y reutilizable. Si ambas dan techo o piso, no agregaría disfraces; cerraría las dos.

C8 no entra todavía: no vale duplicar costo para observar con precisión un host muerto.

## 7. La objeción de “juguete”

[Juicio] Es válida contra el claim, no contra la mecánica. Poner Rule 30 arriba hace rico al sistema superior, pero no necesariamente rico al acto de descubrimiento: una vez reconocido el reloj, 450.000 macro-pasos son simulación ordinaria.

Hay una tensión difícil de evitar:

1. Si el fenómeno superior es rico pero computable para ustedes, también lo será para el agente después de hallar el reloj.
2. Si exige mucho más cómputo que el agente, la asimetría es presupuesto.
3. Si ustedes conocen la respuesta por un atajo plantado, el problema vuelve a ser recuperar una estructura diseñada.
4. Si es irreducible y tampoco ustedes pueden computarlo, no hay oracle.

Se puede usar un CA finito, dinámica caótica o una máquina universal y conocer la respuesta exacta mediante simulación de macro-pasos. Eso produce un modelo formal rico, pero no elimina el carácter de organismo de laboratorio. Hay que defenderlo como tal, no disfrazarlo de ciencia real.

## 8. Si fuera Lucas mañana

Cerraría C2 y C3, congelaría C4–C7 y escribiría una preregistración de una página para el piloto C1 versus Teoría en una botella. Construiría únicamente tres niveles transparentes por familia, sus verificadores independientes, los mejores rivales y una pista común; después correría un solo modelo. Si C1 da techo, quedaría documentado y terminado. Si Botella deja una curva y artefactos generalizables, ésa pasa a ser la pregunta del proyecto: **cuándo puede un agente convertir exploración en una teoría compacta y ejecutable**. No usaría todavía “creatividad” ni “descubrimiento científico” en el titular.

No modifiqué ningún archivo.


---

# SEGUNDA VUELTA

Veredicto: **“Hacé que pase” no sobrevive todavía al mejor rival mecánico.** Sobrevive como anfitrión candidato, condicionado a un kill-test previo con SAT y planificación por objetos. Como experimento aislado es científicamente más débil que “Teoría en una botella”; combinado con ella puede ser mejor.

Comprobé ahora fuentes primarias: secciones pertinentes de REFUTE, EquiBench, mutation testing con LLM, control/inversión de autómatas por SAT, síntesis de configuraciones con Alloy, ASAL y búsqueda de gliders. No encontré una fuente primaria que sea exactamente “un LLM sintetiza gliders”. ASAL usa modelos visuales como función objetivo dentro de CMA-ES, gradiente o fuerza bruta; no es el agente inversor propuesto.

## 1. Diagnóstico

[Dato] Los resultados del paquete muestran que sus generadores anteriores dejaban una descomposición transparente. No muestran que toda construcción sistemática pueda invertirse sistemáticamente.

[Literatura — comprobada ahora] AlphaGeometry genera problemas hacia adelante, pero resolverlos exige un modelo especializado, millones de ejemplos sintéticos y deducción simbólica; la inversión no viene gratis. En autómatas, la alcanzabilidad acotada puede formularse como SAT, pero no toda instancia resulta fácil. [AlphaGeometry](https://www.nature.com/articles/s41586-023-06747-5), [Regional Controllability of Cellular Automata as a SAT Problem](https://arxiv.org/html/2504.03691v1).

[Literatura — de memoria] Las funciones unidireccionales son el contraejemplo formal obvio: evaluación barata, inversión presuntamente difícil.

[Juicio] El diagnóstico correcto es más estrecho:

> Construcción sistemática + representación local transparente + poca profundidad suele dejar una inversión mecánica barata.

La asimetría “forward barato / inverse caro” es útil para diseñar tareas, pero no identifica ideas: también produce contraseñas, SAT y búsqueda combinatoria ciega. Además, muestrear objetivos hacia adelante tiende a elegir fenómenos con muchas preimágenes y, por eso, fáciles de reencontrar.

## 2. “Hacé que pase”

[Dato] Con regla visible, fila inicial acotada, horizonte fijo y verificador exacto, el juego es un problema finito de control o model finding.

[Literatura — comprobada ahora] Andrew Wagner ya sintetizó configuraciones iniciales de autómatas mediante Alloy: el glider pequeño aparece en segundos y objetos mayores muestran la curva de escalamiento. Bagnoli et al. codifican control de CA 1D como SAT y caminos en el grafo de configuraciones. Eppstein encontró naves mediante búsqueda estructurada en espacios enormes; el tamaño bruto no protege el benchmark. [Wagner, *Synthesizing Initial Configurations for Cellular Automata*](https://cs.brown.edu/media/filer_public/1a/cd/1acd447b-1807-48c6-adf0-beef35a7b564/wagnerandrew.pdf), [Bagnoli et al.](https://arxiv.org/html/2504.03691v1), [Eppstein, *Searching for Spaceships*](https://arxiv.org/abs/cs/0004003).

[Juicio] Yo lo atacaría así:

1. Reduciría el objetivo a su cono de luz.
2. Lo codificaría como SAT/SMT, con simetrías rotas y cardinalidad máxima de celdas activas.
3. Probaría programación dinámica por columnas/de Bruijn y meet-in-the-middle.
4. Minaría automáticamente partículas periódicas: semilla, fase, velocidad y soporte.
5. Enumeraría choques y resolvería el objetivo mediante A* sobre ese álgebra.
6. Recién después usaría evolución o búsqueda aleatoria.

Espero que SAT barra escalas pequeñas y que el minero de objetos barra muchos mundos plantados. Por eso, **tal como está escrito, el juego no sobrevivió todavía**.

Existe una zona interesante: el cono microscópico debe ser demasiado grande para SAT, pero la solución macroscópica debe ser corta —pocas partículas estables y dos o tres choques reutilizables—. Esa zona necesita:

- Un mismo mundo con varios objetivos ocultos.
- Una sola exploración amortizada entre objetivos.
- Objetivos definidos como una firma espacio-temporal persistente, no una celda correcta en \(T\).
- Transferencia a nuevos objetivos, no un único golpe afortunado.
- Catálogo entregado antes de ver los objetivos si se quiere hablar de “física”.

Dos correcciones obligatorias:

- “Cantidad de objetos en nuestro testigo” no mide dificultad: puede existir otro testigo más corto. Usen longitud mínima respecto de una gramática de objetos congelada, o no postulen una escala ordinal.
- No filtren instancias individuales porque el rival las resolvió. Calibren el generador en desarrollo, congélenlo y reporten todas las instancias de prueba. Filtrar post hoc fabrica la ventaja.

## 3. ¿Minados o plantados?

[Dato] Los minados reducen la sospecha de haber codificado la solución, pero sacrifican control de dificultad y certificados de imposibilidad. Los plantados ofrecen control, pero pueden filtrar el algoritmo del diseñador y contener atajos no previstos.

[Juicio] Para el piloto: **plantados**, con esta restricción:

> Plantar el lenguaje de objetos, no la oración que resuelve el objetivo.

Generen una biblioteca de partículas y choques, congelen la regla, y recién después generen objetivos independientes. No planten simultáneamente regla, objetivo y testigo. Permuten símbolos y reflexiones para eliminar pistas superficiales.

Los mundos minados van después como validación externa. “Imposible” debe significar UNSAT dentro de \((m,T,\text{alfabeto})\), no equivalencia global. El símbolo que ninguna transición produce sirve como control de atención, no como tarea difícil.

## 4. “Experimento crucial”

[Dato] Una entrada de tabla cambiada es un mutante; la fila que hace divergir ambos mundos es un test que mata al mutante.

[Literatura — comprobada ahora] REFUTE pide exactamente construir un input donde dos programas difieran y lo verifica ejecutándolos; el mejor agente quedó por debajo de 9%. El trabajo de mutation testing hace que LLMs generen tests que distingan programa y mutante: la iteración ayuda, pero envolverla como “método científico” no agrega ventaja, y las declaraciones de equivalencia fueron muy poco fiables. EquiBench sólo clasifica equivalencia; incluso propone como trabajo futuro agentes que generen inputs separadores. [REFUTE](https://arxiv.org/html/2502.19414v1), [Mutation Testing via Iterative LLM-Driven Scientific Debugging](https://arxiv.org/html/2503.08182v1), [EquiBench](https://arxiv.org/html/2502.12466v3).

[Literatura — de memoria, corroborada ahora en abstracts] Las secuencias distinguidoras de máquinas finitas son teoría clásica de testing y diagnóstico.

[Juicio] Como idea principal, aporta poco: es mutation testing en un sistema dinámico. Lo nuevo podría ser una perilla exacta de profundidad causal —alcanzar la transición cambiada, propagar su efecto y volverlo observable—, pero eso sería una contribución de diseño, no una nueva clase de tarea.

Úsenlo como control o calibración de “Hacé que pase”, no como segundo flagship. Nunca acepten “equivalentes” sin certificado acotado del verificador.

## 5. Frente a “Teoría en una botella”

[Dato] “Hacé que pase” devuelve un testigo exacto. “Teoría en una botella” obliga a entregar una representación ejecutable antes de conocer las preguntas ocultas.

[Juicio] Comparación directa:

- **Mejor ingeniería inmediata:** “Hacé que pase”. Verificador trivial, salida flexible, piloto barato.
- **Mejor constructo científico:** “Teoría en una botella”. Separa una teoría reutilizable de la búsqueda condicionada por un objetivo.
- **Problema del primero:** una fila correcta puede venir de SAT, evolución, suerte o una intuición de partículas; el resultado no los distingue.
- **Problema del segundo:** exige diseñar una DSL y puede penalizar teorías válidas que no entren en ella.

La combinación correcta es: **“Hacé que pase” como examen oculto de “Teoría en una botella”**. El agente explora el mundo y congela un catálogo ejecutable; después se le retira y un planificador fijo usa ese artefacto para resolver varios objetivos ocultos. Eso sí prueba reutilización y compresión causal.

Para este mes: primero kill-test del anfitrión. Si aparece margen, agregar la botella antes de hacer claims sobre comprensión.

## 6. Piloto mínimo

[Juicio] Haría esto:

- Dos CA 1D plantados, radio 1, cuatro símbolos y fondo quiescente; primeros dos seeds que pasen compuertas, no los más lindos.
- En cada mundo: tres partículas certificadas y dos choques encadenables.
- La regla se congela antes de generar objetivos.
- Fila inicial de ancho \(2T+1\), con a lo sumo \(m\) celdas no vacías. Elegir el primer \((T,m)\) de una grilla predeclarada que pase calibración.
- Cuatro tareas por mundo: partícula directa, un choque, dos choques y un UNSAT acotado.
- El objetivo exige la firma exacta durante dos períodos y un margen limpio.
- Ocho episodios sin ayuda; repetir las cuatro tareas de choque con catálogo de partículas y colisiones. Doce episodios, un modelo, una muestra, techo total USD 20.
- Primario: testigo válido. Secundarios: tiempo, ejecuciones, falsa declaración de imposible.
- La pista entrega catálogo, no la fila ni el orden de los choques.

Antes de gastar API, correr una cartera mínima: SAT/SMT, evolución con fitness intermedio y planificador A* con catálogo oracle. “Mismo cómputo” no es literalmente definible contra la inferencia cerrada del modelo; reporten curvas por tiempo online y número de simulaciones.

Reglas congeladas de lectura:

| Resultado | Decisión |
|---|---|
| SAT/portfolio resuelve ≥3/4 tareas de choque | El anfitrión está barrido en esa escala; no correr API. |
| Planificador con catálogo no resuelve 4/4 | Mundo inválido: la macroteoría no alcanza. |
| Agente falla alguna de las 2 tareas directas | Piso/harness inválido. |
| Sin pista resuelve ≥2/4 choques, al menos uno por mundo, y los rivales 0/4 | El anfitrión sobrevive; replicar en mundos frescos. No afirmar “entendió”. |
| Sin pista ≤1/4, con catálogo ≥3/4 | Cuello en descubrir/representar objetos; pasar a “Teoría en una botella”. |
| Sin pista ≤1/4 y con catálogo ≤2/4 | Piso: abandonar esta parametrización. |
| Todo el mundo resuelve todo | Techo; el juego no discrimina. |

Esto es un piloto de ingeniería, no evidencia publicable por sí solo.

## 7. Titulares

[Juicio] Si hay señal sin la botella:

> **Diseño inverso en autómatas celulares no vistos: cuándo agentes de lenguaje superan una cartera de buscadores mecánicos**

Claim honesto: bajo un presupuesto online declarado, ciertos agentes encuentran testigos que los algoritmos comparados no encuentran. No: “comprenden la física”, “descubren partículas” o “son creativos”.

Si además el catálogo previo transfiere:

> **Teorías ejecutables para controlar mundos celulares no vistos**

El nulo publicable:

> **La búsqueda por restricciones elimina la aparente ventaja de descubrimiento en el diseño inverso de autómatas celulares**

Sólo es publicable si cubre suficientes mundos, horizontes y solucionadores. Dos mundos donde SAT gana son un kill-test útil, no un paper.
