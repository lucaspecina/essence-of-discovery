<!--
Informe de la búsqueda bibliográfica del 16-nov-2026 (nueve lectores y un redactor, todos Claude).
Las notas crudas de cada lector (unas 1,15 MB, con todas las citas y marcas de lectura) quedan solo en la
máquina de Lucas, en scratch/deep-research/research_notes/, que no se sube al repo.
Límite principal: el cupo de búsquedas web de la sesión se agotó a mitad del trabajo; las líneas sin buscar
están en la sección "El cupo de búsquedas se agotó...". Nada de esto se corrió ni se recalculó.
-->

# Medir descubrimiento exige contar atajos verificables

Medir sin jueces el descubrimiento en el sentido de Wolfram es posible, pero ninguno de los trabajos revisados lo hace todavía. Juntando la evidencia de las nueve notas, la medida tiene tres cuentas. La primera es un certificado finito, que una máquina chequea, de que existe un bolsillo de reducibilidad: un granulado grueso que conmuta con la regla, una ley de conservación, un dominio con sus partículas, una fórmula de salto o un teorema que el núcleo de Lean vuelve a chequear. La segunda es cuánto cómputo ahorra ese atajo frente a simular paso a paso. La tercera es cuánta búsqueda costó hallarlo frente al mejor rival clásico afinado, con el mismo presupuesto y contando los intentos fallidos. Las piezas existen por separado: el verificador del Premio Rule 30, la tabla de conmutación de Israeli y Goldenfeld, la prueba de BB(5) en Coq, rivales como L*/TTT o la búsqueda exhaustiva de proyecciones, y la contabilidad de costos de COCO. Pero en lo leído no aparece ningún trabajo que las combine. Ninguno informa el tamaño del atajo, la novedad la juzgan personas y casi ninguna comparación iguala el cómputo en dólares o FLOPs. Wolfram aporta la pregunta y la tesis: hay «an infinite number of pockets of computational reducibility», y la IA sirve cuando alcanza con un «“80%”». Pero la apoya en experimentos chicos juzgados a ojo, aunque varias de sus afirmaciones se pueden convertir en pruebas con una cuenta. La foto de noviembre de 2026 muestra el hueco. El Premio Rule 30 para agentes juntó 366 entregas parciales verificadas en Lean y ningún premio. DeepMind encontró 11 aceleraciones nuevas en BB(6) sin informar costo ni rival. La guía de IA le gana al azar, pero frente a rivales clásicos afinados la ventaja se achica o desaparece. La comunidad de Life ya descubre con verificación mecánica y crédito por prioridad, sobre unas 3,4×10^14 sopas, y no registra ningún resultado atribuido a una IA. Alcance: nueve notas de una sola sesión, con unas 114 búsquedas web propias. El cupo compartido de búsquedas se agotó a mitad de camino y varias líneas no se buscaron; la lista está en la penúltima sección.

**Cómo leer las marcas.** Cada cita dice entre corchetes cómo leyó la fuente quien escribió la nota de origen. Las nueve notas usan leyendas distintas; acá se unifican así:

| Marca en este informe | Equivale en las notas a | Qué significa |
|---|---|---|
| [entero] | FULL, full, D, completa, ENTERO | texto principal leído completo |
| [parcial] | PART, part, P, pdf-sección, en parte | secciones relevantes de un texto completo |
| [resumen] | ABS, abs, abstract, ABSTRACT | solo el resumen oficial |
| [extracto] | X, tool, fetch-extracto, FETCH-EXTRACT | página bajada entera, pero leída a través del resumen de una herramienta, que puede truncar o parafrasear |
| [snippet] | S, snip, snippet | solo el fragmento que mostró el buscador |
| [2ª mano] | 2ND, 2ª, SECOND-HAND | citado por otra fuente y no comprobado |
| [memoria] | MEMORY, memoria | sabido de antes; no verificado en la sesión |

No se vieron las figuras de los ensayos de Wolfram y no se recalculó ningún número suyo. Las páginas de LifeWiki y del foro de Life se leyeron en el espejo conwaylife.njohnston.ca, que sirve el mismo contenido, porque conwaylife.com bloquea a los programas.

## Wolfram plantea la pregunta con experimentos chicos juzgados a ojo

El ejemplo de manual es la regla 30. Es una regla de ocho casos que, a partir de una sola celda negra, produce una columna central que parece azar. Wolfram llama irreducibilidad computacional a que no haya forma de saber qué pasa sin hacer casi tantos pasos de cómputo como el propio sistema: «there can be no way to predict how the system will behave except by going through almost as many steps of computation as the evolution of the system itself» ([NKS p. 739](https://www.wolframscience.com/nks/p739--computational-irreducibility/) [parcial]). La tesis que sostiene desde 2023 tiene dos mitades. La negativa: «if we want to “solve everything” we’ll inevitably be confronted with computational irreducibility, and there just won’t be any way—with AI or otherwise—to shortcut just simulating the system step by step». La positiva, que es la que define qué es descubrir: «whenever there’s overall computational irreducibility, there are also an infinite number of pockets of computational reducibility. In other words, there are always certain aspects of a system about which things can be said using limited computational effort». La pregunta sobre la IA queda planteada en el mismo ensayo: «whether the AI can successfully find and exploit pockets of computational reducibility» ([Can AI Solve Science?](https://writings.stephenwolfram.com/2024/03/can-ai-solve-science/) [entero]). Su respuesta de 2024 tiene tres partes. La IA sirve «if an approximate (“80%”) answer is good enough». Su potencial de descubrimiento «pales in comparison» con el del cómputo explícito. Y lo interesante no se descubre: «There’s no abstract notion of “interestingness” that an AI or anything can “go out and discover” ahead of our choices».

**Las pruebas de ese ensayo son trece experimentos chicos, casi todos juzgados mirando las salidas.** Algunos ejemplos:

- Un autoencoder convolucional de 59 capas y unos 800.000 parámetros, entrenado con 32 millones de ejemplos de un autómata de 64 celdas, acierta cuando el comportamiento es simple y queda «“vaguely right”» cuando es complejo.
- Un espacio de rasgos «almost managed to automatically discover the four classes» de autómatas.
- Una red que guía la búsqueda en un sistema multicamino llega «in slightly more steps than the true shortest path».
- La evolución de reglas para que un patrón muera justo a los 50 pasos se traba con 3 colores y avanza con 4.
- La enumeración de alcanos muestra que, con 11 carbonos, faltan en las listas estándar al menos 42 de 159.

Ninguno trae tasas de acierto. Tampoco usan herramientas, comparan contra un rival ni miden costo ([CASS](https://writings.stephenwolfram.com/2024/03/can-ai-solve-science/) [entero]). La nota sobre trabajos cercanos no encontró que alguna de esas propuestas se convirtiera en un banco de pruebas en 2024. El propio Wolfram avisa que sus conclusiones son provisorias: «I won’t be at all surprised if experiments that haven’t worked well for me could be dramatically improved by future such innovations, conceivably even changing my “big-picture” conclusions from them». Su vara de comparación es la enumeración exhaustiva, que llama «the only “truly unbiased” approach». Así encontró la regla 30 en 1981, la máquina de Turing universal de 2 estados y 3 colores y el axioma único de la lógica.

Entre 2024 y 2026 los experimentos crecen en tamaño pero no cambian de tipo.

- **Evolución.** En su modelo mínimo, el genotipo es la regla de un autómata y la aptitud es cuántos pasos vive el patrón. Wolfram enumera las 2.147.483.648 reglas de dos colores y rango 2: unas 75 millones tienen vida finita y la más larga dura 308 pasos. El camino adaptativo hacia ese máximo es angosto: pasa por él 1.260 de 606.081 caminos. Con metas exactas o ralas, la búsqueda adaptativa falla donde la exhaustiva encuentra ([evolución, may. 2024](https://writings.stephenwolfram.com/2024/05/why-does-biological-evolution-work-a-minimal-model-for-biological-evolution-and-other-adaptive-processes/) [entero]; [evolución, dic. 2024](https://writings.stephenwolfram.com/2024/12/foundations-of-biological-evolution-more-results-more-surprises/) [entero]).
- **P vs NP.** Enumera todas las máquinas de Turing de hasta 4 estados y 2 colores, que son 4.294.967.296. Llama irreducibles, dentro de cada clase de tamaño, a las funciones que calcula una sola máquina. Admite que antes «we haven’t had a way to rigorously say that we’re seeing computational irreducibility in any particular case». La nota registra que esa irreducibilidad es relativa a la clase: una función «irreducible» con 3 estados la calcula una máquina de 4 estados en tiempo constante 7 ([P vs NP, ene. 2026](https://writings.stephenwolfram.com/2026/01/p-vs-np-and-the-difficulty-of-computation-a-ruliological-approach/) [entero]).
- **Juegos entre programas.** Pone a jugar todas las estrategias de programas chicos contra todas, y deja una regla de método que vale para cualquier evaluación: «It seemed very unscientific to have just looked at programs people happened to have submitted for the tournament. Why not instead systematically enumerate all possible programs and see what happens?» ([juegos, jun. 2026](https://writings.stephenwolfram.com/2026/06/games-between-programs-the-ruliology-of-competition/) [entero]).
- **Modelos de lenguaje.** Sus experimentos con ellos son anécdotas sin protocolo. En el ensayo sobre bugs escribe: «Using an LLM able to validate steps by calling a proof assistant, we can eventually generate a proof for our machine 445 example from above». No dice qué modelo usó, cuántos intentos hizo ni cuánto costó ([bugs, jul. 2026](https://writings.stephenwolfram.com/2026/07/towards-a-theory-of-bugs-the-ruliology-of-the-unexpected/) [entero]). En el ensayo sobre pruebas formales, varios LLM fallan al explicar la prueba de su axioma, también sin nombres ni números ([prueba, ene. 2025](https://writings.stephenwolfram.com/2025/01/who-can-understand-the-proof-a-window-on-formalized-mathematics/) [entero]).
- **El tono de 2026.** Cambia: la IA pasa a ser «unquestionably useful, sometimes very useful» para minar la literatura. La desconfianza se muda a la autoformalización: «an AI will tell me “I did it; look, the proof checks out!” But, actually, in some sense it cheated» ([matemática pura, sep. 2026](https://writings.stephenwolfram.com/2026/09/whats-the-future-for-pure-math-research-in-the-age-of-ai/) [entero]).

La lista de afirmaciones comprobables no es de Wolfram: la armó quien escribió la nota, y Wolfram dice varias de ellas con cautela. Aun así, al menos siete se pueden poner a prueba con una cuenta, sin jueces:

| Afirmación y fuente | Prueba con una cuenta | Qué la refutaría |
|---|---|---|
| No hay atajo «with AI or otherwise» en un proceso irreducible ([CASS](https://writings.stephenwolfram.com/2024/03/can-ai-solve-science/) [entero]) | Pedir el estado exacto en el paso t y medir el cómputo usado contra el de simular | Acertar el estado lejano gastando menos que la simulación |
| Sin herramientas, los LLM fallan más cuanto más larga es la cadena ([FT26](https://writings.stephenwolfram.com/2026/02/making-wolfram-tech-available-as-a-foundation-tool-for-llm-systems/) [entero]; MATH26) | Tasa de error contra largo de la cadena | Que el error no crezca con el largo |
| «to “reverse engineer the pattern” to find the rules can require even more computation» ([Observer Theory](https://writings.stephenwolfram.com/2023/12/observer-theory/) [entero]) | Comparar el costo de inferir la regla con el de generar el patrón, en reglas sorteadas | Que inferir resulte típicamente más barato |
| Un generador de mutaciones acotado «ve» el paisaje como aleatorio (evolución, may. 2024) | Contar evaluaciones hasta la meta: generador aprendido contra mutación al azar | Un generador aprendido mucho mejor que el azar |
| Con metas ralas, la búsqueda adaptativa falla donde la enumeración encuentra (evolución, may. 2024) | Contar evaluaciones hasta la meta con búsqueda exhaustiva, adaptativa y con un agente | Que la adaptativa o el agente lleguen con menos evaluaciones |
| Copiar el criterio humano de interés «doesn’t really work» (MATH26) | Predecir qué teoremas reciben nombre y comparar con el criterio «no derivable de los anteriores» | Un modelo que lo prediga mejor que ese criterio |
| El ganador de una competencia no se anticipa sin correrla ([juegos](https://writings.stephenwolfram.com/2026/06/games-between-programs-the-ruliology-of-competition/) [entero]) | Predecir el orden final antes de correr el torneo completo | Una predicción acertada sin correrlo |

Wolfram mismo da un criterio de interés que se puede contar, y que choca con su afirmación de que lo interesante no se descubre. En una lista ordenada de teoremas, «Most theorems in the list will be derivable from earlier ones. But a few will not. And these turn out to be basically exactly the ones that are typically given names» ([CASS](https://writings.stephenwolfram.com/2024/03/can-ai-solve-science/) [parcial, según la nota de filosofía]). En 2026 lo repite: los interesantes son «the simplest theorems that “give new information”» (MATH26 [entero]). La nota distingue dos patas en su argumento. Una es de principio: la irreducibilidad impide el atajo general. La otra es empírica: sus redes chicas fallan. La segunda es la que él declara provisoria. Además, su definición estrecha de IA en 2024 deja afuera a los sistemas que corren programas, que en 2025 y 2026 pasan a ser el caso central. En la parte C de la nota, 8 búsquedas no encontraron ninguna crítica arbitrada de 2024 a 2026 que discuta de frente estas tesis. El único trabajo externo que las pone a prueba es LifeGPT, que concluye: «LifeGPT is not, in fact, exactly replicating the Life algorithm, but is instead approximating it in an extremely effective, while occasionally fallible, manner» ([arXiv:2409.12182](https://arxiv.org/abs/2409.12182) [parcial: los párrafos que mencionan a Wolfram]).

## Los bolsillos de reducibilidad tienen forma de certificado finito

Un ejemplo concreto hace visible el objeto. Si se mira la regla 146, que parece caótica, en bloques de 3 celdas y cada bloque se reduce a un solo bit (1 si el bloque es «111», 0 si no), la versión gruesa sigue exactamente la regla 128, que es trivial. Israeli y Goldenfeld formalizan esto así: un tamaño de supercelda N, una proyección P de bloques de N celdas a un alfabeto más chico y una regla B tales que proyectar y después correr B da lo mismo que correr la regla original N pasos y después proyectar. Verificarlo es comparar una tabla finita sobre todos los bloques de 3N celdas, 2^(3N) entradas (con N=7, unos 2,1 millones). Con ese criterio granularon 240 de las 256 reglas elementales. Quedaron afuera la 30, la 45, la 106, la 154 y sus simétricas: «We don't know if our inability to coarse-grain these 16 rules comes from limited computing power or from something deeper» ([PRL 2004, nlin/0309047](https://arxiv.org/abs/nlin/0309047) [entero]; [PRE 2006, nlin/0508033](https://arxiv.org/abs/nlin/0508033) [entero]).

Song y Grochow cambiaron la búsqueda por un backtracking tipo DPLL. Con él encontraron en una laptop todos los granulados entre reglas elementales hasta N=7, que por fuerza bruta llevarían «≈ 10^27 years». Encontraron 56 granulados nuevos. Siguen sin granulado 20 reglas: las 16, más [37, 91] y [164, 218]. El problema queda «in the complexity class NEXP. It would be interesting to know whether it is NEXP-complete» ([arXiv:2012.12153](https://arxiv.org/abs/2012.12153) [entero]).

Hay un dato que cambia la lectura, con una salvedad: sale de un cómputo propio de la nota, sin IA y no publicado. Según ese cómputo, las 16 reglas sin granulado son exactamente las elementales sobreyectivas no afines. Toda regla no sobreyectiva tiene una palabra «Jardín del Edén», que nunca aparece después de un paso, de largo 9 o menos, y eso permite granularla trivialmente a la regla 0. Así le pasa a la 110 con «01010», como ya mostraban Israeli y Goldenfeld, que para esa regla escriben: «At every scale we achieved a constant reduction in the computational effort». **Existir no es valer.** Un puntaje de granulados necesita un criterio de no trivialidad escrito antes de mirar.

**Leyes de conservación.** Una ley de conservación aditiva es una función sobre bloques cuya suma sobre la fila no cambia de un paso al siguiente. Con un rango fijo, chequearla es álgebra lineal finita: es la ecuación de continuidad discreta de Hattori y Takesue ([Fukś 2005, nlin/0502037](https://arxiv.org/abs/nlin/0502037) [entero]). NKS da, para bloques de largo 1 a 10, la cantidad de reglas elementales que tienen alguna ley: {5, 38, 66, 88, 102, 108, 108, 114, 118, 118}. Agrega que «Rules that show complicated behavior usually do not seem to have conserved quantities, and this is true for example of rules 30, 90 and 110, at least up to blocks of length 10» ([NKS 1022f](https://wolframscience.com/nksonline/page-1022f/) [parcial, extracto]). Un cómputo propio de la nota reproduce esa serie y extiende la ausencia de leyes hasta rango 12 para seis reglas. Pero usa aritmética de punto flotante, y la propia nota avisa que no es una prueba exacta. En general el problema es indecidible y tiene un borde abierto: «whether a (one-dimensional) cellular automaton has any non-trivial local conservation law is undecidable ... It is an interesting open problem whether the latter undecidability statement remains true when restricted to the class of reversible (or surjective) cellular automata» ([Kari y Taati, arXiv:1311.2319](https://arxiv.org/abs/1311.2319) [parcial]). Para la regla 30 hay un cierre en Lean del 25-oct-2026, aportado por un participante «with OpenAI Codex»: «For every positive window width, integer densities conserved by four Rule30 steps on all closed overlapping-word walks are exactly constants plus shift coboundaries» ([lean/README del kit](https://github.com/WolframInstitute/Rule30PrizeKit/tree/main/lean) [parcial]).

**Dominios y partículas.** Un dominio regular es un lenguaje regular que la regla devuelve a sí mismo; las partículas son los defectos que se mueven entre dominios. Verificar un dominio propuesto es exacto y decidible: se pasa el autómata por el transductor de la regla, se minimiza y se comparan autómatas. Encontrarlo se automatiza con «guess and check» sobre autómatas enumerados por tamaño. Hay catálogos para la regla 18 y para la 54, con cuatro partículas y sus reacciones. De la 110, que tiene un dominio de período espacial 14 y temporal 7, dicen: «Exactly how, though, remains an open problem» ([Rupe y Crutchfield, arXiv:1801.00515](https://arxiv.org/abs/1801.00515) [parcial]). Para la 30, el kit registra que «the 12 × 3 ether has no wall of any width» ([lean/README](https://github.com/WolframInstitute/Rule30PrizeKit/tree/main/lean) [parcial]).

**Atajos.** Lo probado forma una escalera:

- En las reglas aditivas se puede saltar adelante: se predicen «in O(t) serial time or O(log t) parallel time», y las cuasi-lineales en profundidad O(log² t) ([Moore 1997, patt-sol/9701008](https://arxiv.org/abs/patt-sol/9701008) [parcial]).
- La 110 tiene una barrera: «predicting t timesteps of a Rule 110 computation is P-complete» ([Neary y Woods, arXiv:1110.2230](https://arxiv.org/abs/1110.2230) [parcial]).
- La 30 no tiene nada probado en ningún sentido. Las versiones del Problema 3 en complejidad de circuitos están «beyond current lower-bound techniques» ([CATALOG del kit](https://github.com/WolframInstitute/Rule30PrizeKit/blob/main/equivalents/CATALOG.md) [parcial]).
- La definición formal de Zwirn y Delahaye dice que predecir es «to be able to find the result it computes faster than the machine itself». También deja el problema abierto: «An open problem is now to prove that explicit objects are really CIR. Possible candidates are: ... Rule 30, Rule 110» ([arXiv:1111.4121](https://arxiv.org/abs/1111.4121) [entero]).
- En máquinas de Turing chicas, de 3.414 algoritmos solo 122 tenían una versión más rápida, con una aceleración media de 1,23×: «Actually no essential speed-up was witnessed at all» ([Joosten, Soler-Toscano y Zenil, arXiv:1102.5389](https://arxiv.org/abs/1102.5389) [parcial]).

**Certificados formales.** El kit del Premio Rule 30 usa Lean 4.35.0. Trae 210 módulos de la biblioteca `Ruliology` y 107 de `Rule30Equivalents`; de 54 formas equivalentes del Problema 1, 52 están probadas. Lo que se sabe del problema:

- «Problem 1 is open. Everything here is a partial result.»
- No hay período P ≤ 4096 con transitorio ≤ 8192.
- El caso del período 2 se reduce a un enunciado llamado Q01, abierto, que está probado para todo arranque de ancho ≤ 52.

El kit también registra una barrera: «Rules 90, 150 and 210 share every structural fact used so far, yet their center columns are eventually constant (`Rule30Realization`) ... A new idea has to use something that rule 30 has and those rules lack» ([skill.md](https://www.wolframcloud.com/obj/rule-30-prize/Agents/skill.md) [entero]). El verificador vuelve a pasar cada declaración por el núcleo. Lo hace porque «A file can add a theorem without type checking it (`set_option debug.skipKernelTC true`), and an axiom check then reports nothing wrong» ([README del kit](https://github.com/WolframInstitute/Rule30PrizeKit) [entero]). BB(5) es el modelo clásico sin IA: S(5) = 47.176.870 probado en Coq, con la enumeración reducida a 181.385.789 máquinas, y «AI-based code completion was not used in Coq-BB5» ([bbchallenge, arXiv:2509.12337](https://arxiv.org/abs/2509.12337) [parcial]).

| Objeto | Qué chequea una máquina, sin IA | Costo de encontrarlo | Estado en reglas famosas |
|---|---|---|---|
| Granulado grueso | Conmutación en una tabla de 2^(3N) bloques | Búsqueda tipo SAT; problema en NEXP | 240/256 granuladas; 30, 45, 106 y 154 sin granulado hasta N=7 |
| Ley de conservación aditiva | Ecuación de continuidad de Hattori–Takesue a rango fijo | Sistema lineal por rango; indecidible si se piden todos los rangos | 30, 90 y 110 sin leyes hasta rango 10; la 30, cerrada en Lean (2026) |
| Dominio y partículas | Transductor de la regla, minimización y comparación de autómatas | Adivinar y chequear sobre autómatas enumerados | Catálogos para la 18 y la 54; la 110, abierta |
| Salto hacia adelante | Fórmula o circuito comparado contra la simulación | Sin método general | Aditivas: O(log t) en paralelo; 110: P-completa; 30: nada probado |
| Teorema formal | Replay en el núcleo, enunciado oficial y lista blanca de axiomas | El de la prueba | 30: Q01 abierto; BB(5) cerrado en Coq |

La nota de objetos exactos deja seis instancias abiertas y bien planteadas:

1. Un granulado no constante de la 30, 45, 106 o 154, o una prueba de que no existe.
2. Si el problema de granulado es NEXP-completo.
3. Leyes de conservación de rango mayor que 10 a 12 para la 110, 54, 45, 106 y 154, y la decidibilidad del problema para reglas sobreyectivas o reversibles.
4. Cómo sale la complejidad de la 110 de su dominio de 14 estados.
5. Los tres problemas del Premio Rule 30 y sus intermedios, como Q01.
6. Probar que la 30 o la 110 son irreducibles en el sentido formal.

Una respuesta positiva en los puntos 1 y 3 se certifica con una tabla finita. Una negativa exige una prueba que valga para todo N o para todo rango.

## Bancos y sistemas cuentan aciertos y dejan afuera el atajo

La nota del panorama revisó unos 20 bancos de pruebas. Solo una parte usa mundos totalmente sintéticos y puntaje exacto sin juez: InductionBench, KoLMogorov Test, CellARC, el autómata oculto, ARC-AGI-3 y OEIS Open, y con matices CodeARC y Gravity-Bench. Los de leyes físicas meten un modelo en el puntaje. NewtonBench, por ejemplo, decide la equivalencia de ecuaciones con un juez LLM que coincide en un 98,3% con expertos sobre 120 pares ([arXiv:2510.07172](https://arxiv.org/abs/2510.07172) [parcial]). Los resultados van de casi cero a la saturación:

- **InductionBench:** los puntajes de o1-mini y o3-mini quedan «at or near zero» ([arXiv:2502.15823](https://arxiv.org/abs/2502.15823) [parcial, copia local]).
- **ARC-AGI-3:** es el único cuyo puntaje es una eficiencia, en acciones contra las de un humano. Al lanzarse, los modelos de frontera sacaban menos del 1%. Al 16-nov-2026, la tabla oficial muestra 81,2% para Claude Fable 5.2, con 21.900 USD de costo ([paper](https://arxiv.org/abs/2603.24621) [parcial]; [tabla](https://arcprize.org/leaderboard) [extracto]).
- **OEIS Open** puntúa con el núcleo de Lean sobre 492 conjeturas abiertas reales y encuentra que «Solve rates rise roughly linearly in log-spend, on the order of ten percentage points per tenfold increase» ([arXiv:2608.11941](https://arxiv.org/abs/2608.11941) [entero]).
- **Autómata oculto:** es el más parecido en diseño a lo que hace falta, porque compara las consultas del agente con las del algoritmo clásico TTT. Pero el objeto es chico y su algoritmo óptimo se conoce ([arXiv:2606.16576](https://arxiv.org/abs/2606.16576) [entero]).

**El KoLMogorov Test es lo más cercano a un puntaje de descubrimiento sin IA, y muestra la trampa principal.** El puntaje es el programa más corto que reproduce exactamente una secuencia. GPT-4o no reproduce el 40% de las secuencias naturales. En datos naturales, más del 95% de los aciertos son repeticiones literales de la entrada. Y los autores no cuentan el tiempo: «In our experiments, we do not consider the runtime compute of programs execution» ([arXiv:2503.13992](https://arxiv.org/abs/2503.13992) [entero]). Sin tiempo, un programa corto que vuelve a simular se ve igual que un atajo verdadero. Pasa también con OMNIS, que recupera un programa de 74,5 bits para la regla 30 y aclara que «makes no claim about the rule's behavior over infinite time» ([arXiv:2606.13799](https://arxiv.org/abs/2606.13799) [parcial; cuerpo entero]).

Los sistemas con resultados nuevos verificados miden un sí o un no por instancia, o un puntaje contra un evaluador fijo.

- **FunSearch** halló un cap set de 512 en n=8. Lo logró en solo 4 de 140 corridas. Sus autores ponen el límite así: «works best for problems having the following characteristics: (1) availability of an efficient evaluator; (2) a 'rich' scoring feedback ... (3) ability to provide a skeleton» ([Nature](https://www.nature.com/articles/s41586-023-06924-6) [entero: cuerpo y Methods]).
- **AlphaEvolve** igualó cerca del 75% de más de 50 problemas y mejoró cerca del 20%, entre ellos el rango 48 para matrices complejas de 4×4 ([arXiv:2506.13131](https://arxiv.org/abs/2506.13131) [entero, §1-6, copia local]). El informe de 67 problemas admite que hubo un «cheating phenomenon» frente al verificador y que, «for problems where genuinely new, deep insights are required to make progress, AlphaEvolve is likely not the right tool to use» ([arXiv:2511.02864](https://arxiv.org/abs/2511.02864) [entero, §1-5, copia local]).
- **BB(6) (DeepMind).** Una tubería con Gemini 3.1 Pro y Lean encontró y probó 11 aceleraciones nuevas y 15 redescubrimientos. La novedad se decidió a mano contra la wiki y el Discord de la comunidad. No informa costo ni compara contra un rival sin IA. Los autores dicen: «we acknowledge that our current approach is not entirely open-ended. Specifically, our system currently accelerates machines exhibiting Collatz-like functions» ([arXiv:2610.22603](https://arxiv.org/abs/2610.22603) [entero]).
- **Station.** Es de los pocos que corre un rival con el mismo presupuesto: OpenEvolve, con 8.000 minutos de tiempo de evaluador. Pero ese rival es otra IA, no el mejor método sin el truco ([arXiv:2608.23691](https://arxiv.org/abs/2608.23691) [parcial]).
- **ASAL** está en el extremo opuesto a un puntaje sin jueces. Usa CLIP o DINOv2 como juez de novedad, y los autores reconocen que la formulación «outsources the subjectivity of measuring open-endedness to the construction of the representation function, which embodies the observer» ([arXiv:2412.17799](https://arxiv.org/abs/2412.17799) [entero, copia local]).

**El Premio Rule 30 para agentes es el único programa del entorno de Wolfram que acepta entregas verificadas de IA, y mide probar enunciados, no encontrar bolsillos.** Fechas del arranque: el repositorio del kit se creó el 16-oct-2026, la primera entrega pública es del 20-oct, Wolfram lo anunció en X el 22-oct (leído a través de un espejo [extracto]) y el 23-oct apareció un aviso en el ensayo de 2019. Cómo funciona:

- El agente manda un cuaderno con una prueba en Lean.
- La máquina reconstruye la prueba en un sandbox, la vuelve a pasar por el núcleo y compara el enunciado con el oficial.
- Después, personas ponen etiquetas.
- En los resultados parciales y en el Problema 3, «the statement is the submitter's own; a person judges what it means». El Problema 3 no tiene enunciado oficial en Lean.

Hay un tope de 30 entregas por hora y 100 por día por cuenta ([Agents](https://www.wolframcloud.com/obj/rule-30-prize/Agents/) [entero]; [skill.md](https://www.wolframcloud.com/obj/rule-30-prize/Agents/skill.md) [entero]). En la copia del 16-nov-2026 (20:15 UTC), contada con un script, hay:

- 366 entregas: 286 del Problema 1, 57 del 2 y 23 del 3, todas parciales;
- 363 Lean Verified, 339 Human Verified, 315 Kit Contribution y 0 Prize Claimed;
- un solo grupo, que declara el agente «Gemini 3 Pro (Google)», con 240 entregas (66%), y tres grupos que suman el 90%.

Fuente: [submissions.json](https://www.wolframcloud.com/obj/rule-30-prize/Agents/submissions.json) [entero, procesado con un script]. Los organizadores ya avisan saturación: «much of what agents find has been found already, and a submission that repeats one, or adds one more case of it, adds nothing». Y también: más palabras excluidas por certificados finitos «are no longer worth a submission: the catalog and the list hold many» ([skill.md](https://www.wolframcloud.com/obj/rule-30-prize/Agents/skill.md) [entero]). La nota lo lee así: no hay denominador (ni intentos fallidos, ni costo, ni rival sin LLM, por ejemplo SAT o búsqueda de certificados), y con esa concentración las cuentas miden esfuerzo, no capacidad.

| Trabajo | Verificador | Rival sin IA | Costo informado | Quién juzga la novedad | Mide el tamaño del atajo |
|---|---|---|---|---|---|
| BB(6), DeepMind | Lean | No | No | Personas (wiki, Discord) | No; solo incentiva «< 15 rules» |
| Premio Rule 30 para agentes | Replay en el núcleo de Lean | No | No | Personas (etiquetas) | No |
| KoLMogorov Test | Salida idéntica | gzip | No; tope de 5 s | — | Bits, sin tiempo |
| FunSearch / AlphaEvolve | Función evaluate() | FunSearch: mutación al azar; AlphaEvolve: no | Anécdotas | La literatura | No |
| Israeli–Goldenfeld | Conmutación exacta | Su propia búsqueda exhaustiva | No | — | Reducción de alfabeto y tamaño N |
| Autómata oculto | Equivalencia exacta | L*/TTT | Consultas, tokens, USD | — | No aplica |
| ASAL | CLIP / DINOv2 (una IA) | — | — | Una IA | No |
| OEIS Open | Núcleo de Lean | — | USD | Conjeturas abiertas reales | No |
| BB(5), bbchallenge | Coq | Es el rival clásico | — | — | Clase de certificado |

Lo que ningún trabajo leído mide queda acotado por lo que se buscó. La nota del panorama define «nadie» como «no lo encontré en 30 búsquedas + 51 lecturas + el resumen previo». Con esa salvedad, la lista es:

- leyes emergentes en reglas nunca estudiadas, con puntaje exacto;
- un rival clásico optimizado, que solo usan el autómata oculto y los códigos cuánticos;
- búsqueda ahorrada a igual cómputo, sobre muchos descubrimientos;
- atajos medidos por tiempo de ejecución;
- novedad decidida de forma mecánica;
- denominadores, que solo publican AlphaProof Nexus, OEIS Open, Aletheia y BB(6), este último sin costo;
- una tasa de trampas comparable entre sistemas;
- la varianza entre corridas;
- cuánto pesa el prompt.

La nota sobre trabajos cercanos llega a lo mismo después de leer doce trabajos: ninguno informa un factor de aceleración ni cuánto adelante se puede saltar, y ninguno prueba sistemas cuya regularidad no se haya nombrado antes.

## La guía de IA le gana al azar y se achica frente a rivales afinados

La advertencia de la nota de búsqueda ahorrada vale para toda esta sección: casi ninguna comparación iguala el cómputo total, en FLOPs o en dólares. Lo habitual es igualar candidatos, llamadas al oráculo o tiempo por problema, o comparar contra un número publicado por otro sin volver a correrlo. Con esa salvedad, el patrón es nítido. Contra el azar o contra heurísticas fijas, la guía de IA gana, a veces por órdenes de magnitud en cantidad de candidatos. Contra el mejor rival clásico afinado, la ventaja se achica mucho o desaparece en la mayoría de los casos.

**FunSearch es el único de su familia con un brazo sin LLM.** En su suplemento, la mutación aleatoria de programas no pasa de una meseta: «Even after leaving 'Random' generate more than 50 million programs, none of the runs were able to surpass −240 and reached a plateau». FunSearch, en cambio, llega con unos 2×10^6 programas. Eso da una ventaja de más de 25× en programas, que es una cota inferior y no un ahorro de cómputo ([Nature, suplemento](https://www.nature.com/articles/s41586-023-06924-6) [parcial: suplemento A.1–A.5]). AlphaEvolve no publica cuántas muestras usó, ni cuánto cómputo, ni un brazo sin LLM. Sus ablaciones dicen solo que «each of the components is responsible for a significant improvement» ([arXiv:2506.13131](https://arxiv.org/abs/2506.13131) [parcial]). Cuando otros afinaron rivales clásicos, varios récords cayeron en semanas:

- Xpress y SCIP superaron su empaquetado de 32 círculos, 2,93957 contra 2,93794 ([Berthold, arXiv:2605.04850](https://arxiv.org/abs/2605.04850) [parcial]).
- En multiplicación de matrices, los grafos de volteo encontraron por otro camino todas sus mejoras: «all the improvements we found starting from one of AlphaEvolve's schemes was also found in some other way» ([Kauers y Wood, arXiv:2510.19787](https://arxiv.org/abs/2510.19787) [parcial]).
- Un equipo humano dio un esquema de 48 multiplicaciones con coeficientes racionales ([Dumas, Pernet y Sedoglavic, arXiv:2506.13242](https://arxiv.org/abs/2506.13242) [resumen]).

Las ablaciones de 2025 y 2026 se contradicen, y la nota registra la contradicción sin arbitrarla.

- **Gideoni, Risi y Gal**, con 20 USD por problema, encuentran que el muestreo secuencial iguala o supera a ShinkaEvolve en 6 de 9 problemas y a AlphaEvolve en 4 de 9. Concluyen que «the search space matters far more than the exact search algorithm» ([arXiv:2602.16805](https://arxiv.org/abs/2602.16805) [entero]).
- **Zhang et al.** encuentran lo contrario: «(1+1)-EPS with 500 query budgets can outperform standalone LLM with 10,000 query budgets…» ([arXiv:2407.10873](https://arxiv.org/abs/2407.10873) [parcial]).
- **Códigos cuánticos «bicicleta».** Un algoritmo genético llega a una suma de k de 1.037 con 14.000 evaluaciones, y el LLM a 704 con unas 213.000. Pero solo el LLM llega a distancia 6 o más ([arXiv:2606.02418](https://arxiv.org/abs/2606.02418) [parcial]).

| Dominio | Con IA | Rival | Quién gana | Cómo se igualó | Fuente |
|---|---|---|---|---|---|
| Cap set / I(15,10) | FunSearch, ~2×10^6 programas | Mutación al azar, >5×10^7, en meseta | IA | Programas | [Nature](https://www.nature.com/articles/s41586-023-06924-6) [parcial] |
| Geometría IMO-AG-30 | AlphaGeometry, 25/30 | DD+AR con heurísticas: 18; con el método de Wu en una laptop: 21 | IA, por 4 | Rival afinado después | [Trinh](https://www.nature.com/articles/s41586-023-06747-5) [parcial]; [Sinha](https://arxiv.org/abs/2404.06405) [entero] |
| Selección de premisas | Magnushammer, 59,5% | Sledgehammer, 38,3% | IA | Mismo presupuesto | [arXiv:2303.04488](https://arxiv.org/abs/2303.04488) [parcial] |
| Síntesis SyGuS | LLM ∪ A*, 80,1% | cvc5, 68,1% | IA | 600 s | [arXiv:2403.03997](https://arxiv.org/abs/2403.03997) [parcial] |
| Grafos sin 4-ciclos | PatternBoost, 91 | Búsqueda local, 89 | IA | 50M búsquedas locales | [arXiv:2411.00566](https://arxiv.org/abs/2411.00566) [parcial] |
| Grafos extremales | AlphaZero | Tabú, 32 × 7 días | Empate en 41; tabú +1 en 6 | Hasta meseta | [arXiv:2311.03583](https://arxiv.org/abs/2311.03583) [parcial] |
| Ubicación en chips | AlphaChip, 19.068–21.507 CPU-h | Recocido simulado, 896 CPU-h | Clásico en 6/9 | Recursos | [arXiv:2302.11014](https://arxiv.org/abs/2302.11014) [parcial] |
| Cristales | MatterGen, 3,0% | Intercambio iónico, 9,2% | Clásico | 500 candidatos, DFT | [arXiv:2501.02144](https://arxiv.org/abs/2501.02144) [parcial] |
| Heurísticas | LLM, 10.000 evaluaciones | (1+1)-EPS, 10.000 | Ninguno consistente | Evaluaciones | [arXiv:2407.10873](https://arxiv.org/abs/2407.10873) [parcial] |

La lectura de la nota es que la ventaja se sostiene donde el rival no tiene una buena guía propia: en espacios de programas y de pruebas, la selección de premisas y la síntesis ganan con presupuesto igualado. Desaparece donde el verificador es barato y existe una búsqueda local rápida. Mehrabian lo dice sin vueltas: «introducing learning did not yield improvements», porque «for this problem, natural, fast, and strong local search algorithms exist». En Busy Beaver, los deciders clásicos eliminan más del 99,999% de las máquinas, y la IA entra solo en la cola de unas mil que quedan. Ninguna fuente da el costo de esa etapa ([arXiv:2509.12337](https://arxiv.org/abs/2509.12337) [parcial]; [arXiv:2610.22603](https://arxiv.org/abs/2610.22603) [entero]).

Medir el valor de una idea en cómputo equivalente tiene antecedentes viejos y una definición moderna frágil.

- **Newell, Shaw y Simon (1958)** ya daban el ahorro neto del costo de la propia heurística: los filtros del Logic Theorist «reduced the amount of search required to find the solution by a factor of [...] 2.7. When the cost of the additional testing is taken into account, the net saving in total problem-solving effort after allowing for this testing was 2.3» ([RAND P-1320](https://www.rand.org/content/dam/rand/pubs/papers/2008/P1320.pdf) [parcial, con OCR propio]).
- **OOPS** midió cuánto ayuda lo aprendido antes: el programa final tiene probabilidad 9,3×10^−11 con el resolvedor previo y 4,5×10^−14 sin él, es decir, «speeding up the search by a factor of 1000 or so» ([Schmidhuber, cs/0207097](https://arxiv.org/pdf/cs/0207097) [parcial]).
- **Epoch** define una «ganancia de cómputo equivalente», que mide «how much additional training compute would be needed to improve performance by the same amount as the enhancement». Pero sus autores avisan que en agentes «the CEG is not meaningful» ([arXiv:2312.07413](https://arxiv.org/abs/2312.07413) [parcial]).

La nota no encontró ningún estudio que mida el valor de una idea de IA en fuerza bruta equivalente. Infiere que eso exige la curva completa del rival: si el rival nunca llega, solo hay cotas inferiores. Sobre el escalamiento, el éxito crece log-lineal con el gasto y con las muestras, y varias corridas cortas le ganan a una larga. Un ejemplo: en el autómata oculto, DeepSeek pasa del 3,1% con el 100% del presupuesto de referencia al 55,6% con el 200% ([arXiv:2606.16576](https://arxiv.org/abs/2606.16576) [entero]). Hay una contradicción abierta sobre el tamaño del modelo. FunSearch dice que el método es «not too sensitive to the exact choice of LLM» ([Nature](https://www.nature.com/articles/s41586-023-06924-6) [parcial]). AlphaEvolve, en cambio, rinde mejor cuanto mejor es el modelo base.

## La comunidad de Life ya mide descubrimiento sin jueces, y en lo leído la IA no figura

El Juego de la Vida tiene la línea de base humana más madura. Catagolue es un censo voluntario, iniciado el 20-feb-2015, de en qué terminan sopas aleatorias de 16×16. Al 16-nov-2026, el censo asimétrico (C1) lleva 339.736.943.207.988 sopas y 7.421.511.702.997.913 objetos ([censo C1](https://catagolue.hatsya.com/census/b3s23/C1) [extracto]), con 557.080 tipos distintos ([estadísticas](https://catagolue.hatsya.com/statistics) [parcial]). Sumando todas las simetrías, a febrero de 2026 eran más de 2,7×10^15 sopas ([LifeWiki, Catagolue, copia de Wayback del 6-nov-2026](https://web.archive.org/web/20261106144128/https://conwaylife.com/wiki/Catagolue) [entero]).

La verificación es mecánica. Cada objeto tiene un código canónico. El servidor comprueba que el objeto se comporte como dice su código. Los envíos pasan pruebas estadísticas y verificación por pares. Y cada aparición se puede regenerar desde un identificador de sopa. El crédito es por prioridad: «Users are credited for discoveries if they find one of the first 20 occurrences of an interesting object». Las frecuencias abarcan unos 15 órdenes de magnitud. El bloque aparece unas 6,7 veces por sopa; el loafer, 2 veces en todo el censo, una vez cada 1,7×10^14 sopas, y eso que una persona ya lo había encontrado en 2013 sin censo ([Loafer](https://conwaylife.njohnston.ca/wiki/Loafer) [extracto]). La nota infiere que la búsqueda por sopas no llega, en la práctica, a nada más raro que una vez cada unas 10^14 sopas.

La historia muestra regímenes, tiempos largos y casi ninguna cifra de cómputo. Hasta los años 80 se trabajaba a mano. Desde fines de los 80 hubo programas de búsqueda hechos a medida. Después vino la ingeniería a gran escala sobre componentes hallados por búsqueda, y desde 2015 los censos masivos, junto con SAT y la búsqueda de catalizadores. Algunos hitos:

- **Sir Robin (2018).** El primer knightship elemental llegó 48 años después de la pregunta. SAT completó un patrón parcial hecho por una persona ([Sir Robin](https://conwaylife.njohnston.ca/wiki/Sir_Robin) [extracto]).
- **Omniperiodicidad (julio de 2023).** Los últimos doce períodos se buscaron entre 2000 y 2023 ([arXiv:2312.02799](https://arxiv.org/abs/2312.02799) [entero]).
- **Omninave (14-sep-2026).** Una construcción humana que da naves de toda velocidad estrictamente por debajo del límite ([Omniship](https://conwaylife.njohnston.ca/wiki/Omniship) [extracto]).
- **Síntesis con planeadores.** Todas las still lifes de hasta 23 celdas se pueden armar solo con planeadores (cerrado en diciembre de 2025), y la frontera avanza alrededor de una celda cada 12 a 18 meses. Todo lo que se puede sintetizar cabe en 15 planeadores o menos. Y existe una still life que no se puede sintetizar, de 153 celdas (27-sep-2026), así que el umbral queda entre 24 y 153 celdas, una pregunta abierta que se verifica de forma exacta ([Glider synthesis](https://conwaylife.njohnston.ca/wiki/Glider_synthesis) [extracto]).
- **Cifras de cómputo.** Casi no hay. La nave c/5 de 1996 llevó «38 cpu-weeks» ([Eppstein, cs/0004003](https://arxiv.org/abs/cs/0004003) [extracto]). La prueba de que todo fénix finito tiene período 2 resolvió con SAT una caja de 26.912 variables ([cp4space](https://cp4space.hatsya.com/2024/01/20/every-finite-phoenix-has-period-2/) [extracto]). La nota no encontró ninguna cifra total de horas de CPU o GPU de Catagolue.

Los propios practicantes describen el azar del proceso: «each result of a catalyst-based search is a roll of the dice: there is no way of specifying in advance which period you would like to find», y «Soup searches are essentially the only method we have of finding small, volatile, high-period oscillators» ([arXiv:2312.02799](https://arxiv.org/abs/2312.02799) [entero]).

Qué cuenta como descubrimiento también está escrito. Según los criterios de LifeWiki, un patrón merece página si es histórico, si es un récord, si es el primero de su tipo o si «Its discovery answered an open question about Life or a similar cellular automaton» ([Notability](https://conwaylife.njohnston.ca/wiki/LifeWiki:Notability) [extracto]). El gusto cambia con el tiempo: «in the past, LCM oscillators were considered 'too boring to count'» ([arXiv:2312.02799](https://arxiv.org/abs/2312.02799) [entero]). Otras reglas se exploran con la misma maquinaria: hay 20.644 reglas censadas al 2-jun-2026, casi todas con censos chicos, y un premio anual al descubrimiento del año en otras reglas ([LifeWiki, Catagolue](https://web.archive.org/web/20261106144128/https://conwaylife.com/wiki/Catagolue) [entero]).

Sobre la IA, la nota dice: «I found no community-recognised Life result attributed to an AI or LLM agent». La búsqueda de noticias de IA de 2025 y 2026 sobre autómatas quedó bloqueada por el cupo. En el foro, los modelos inventan objetos y estadísticas desde 2023. En octubre de 2026, un usuario resumió: «Claude is definitely better at CA than I thought it would be, but it is clear it is imperfect» ([foro](https://conwaylife.njohnston.ca/forums/viewtopic.php?p=233402) [parcial]). El único aporte concreto registrado es de 2026: un LLM escribió un script de fuerza bruta, una persona lo corrió y apareció un contraejemplo chico a una conjetura ([foro](https://conwaylife.njohnston.ca/forums/viewtopic.php?p=232398) [extracto]). Un moderador de LifeWiki y del foro explicó en 2024 por qué: «Game of Life problems seem to be highly resistant to neural-net types of solutions», ya que «there aren't any reliably recognizable features that can distinguish a spaceship from a non-spaceship» ([Hacker News](https://news.ycombinator.com/item?id=40131597) [parcial]). Para una evaluación, la línea de base humana deja cuatro rasgos: verificar es barato comparado con encontrar; el tiempo hasta un descubrimiento tiene cola pesada, de días a décadas; los hitos recientes mezclan búsqueda automática con ingeniería humana; y los problemas abiertos ya vienen en un formato que una máquina puede chequear.

## Las definiciones sin juez existen, pero todas fijan un observador o el tiempo

La filosofía clásica no da una cuenta numérica del acto de descubrir. Popper y Reichenbach lo excluyen a propósito. La enciclopedia de Stanford define el descubrimiento de forma amplia: «Scientific discovery is the process or product of successful scientific inquiry» ([SEP, Scientific Discovery](https://plato.stanford.edu/entries/scientific-discovery/) [entero]). Lo que sí se cuantificó son derivados.

- **Novedad heurística de Zahar.** Un hecho es nuevo si «it is not predicted by any of the programme's rivals and b) either it is not already known or if it is already known, the hard core of the programme was not devised to explain it» ([SEP, Lakatos](https://plato.stanford.edu/entries/lakatos/) [parcial]). En la práctica es un control de contaminación, dicho en 1973.
- **Teoría formal del aprendizaje.** Descubrir es converger a la verdad, y la eficiencia se cuenta en cambios de opinión ([SEP, Formal Learning Theory](https://plato.stanford.edu/entries/learning-formal/) [parcial]).
- **Cercanía a la verdad.** Las medidas de cuán cerca quedó una teoría dependen del lenguaje en que se escriben ([SEP, Truthlikeness](https://plato.stanford.edu/entries/truthlikeness/) [parcial]). La nota infiere que un puntaje binario y exacto esquiva esa objeción.

Las críticas al descubrimiento por máquina de los años 80 y 90 apuntan a quién eligió la representación. De BACON escriben: «BACON, in short, works only in a world of hand-picked, prestructured data» ([Chalmers, French y Hofstadter](https://consc.net/papers/highlevel.pdf) [parcial]). El éxito de AM venía de cómo estaba escrito: «it is, in part, the density of worthwhile math concepts as represented in Lisp that is the crucial factor» ([Lenat y Brown, AAAI-83](https://cdn.aaai.org/AAAI/1983/AAAI83-059.pdf) [entero]). Graffiti y HR ya tenían filtros contables, como guardar una conjetura solo si no se sigue de las anteriores ([Colton, Bundy y Walsh](https://cgi.cse.unsw.edu.au/~tw/IJHCS00.pdf) [parcial]). Es la misma idea que el criterio de Wolfram para los teoremas que reciben nombre.

Las medidas de inteligencia meten al observador de forma explícita.

- **Chollet** define la dificultad de generalización como un cociente de entropías condicionales ([arXiv:1911.01547](https://arxiv.org/abs/1911.01547) [parcial]).
- **Legg y Hutter** suman sobre entornos pesados por complejidad de Kolmogorov, que no es computable y depende de la máquina de referencia. Además rechazan meter el costo: «We consider the addition of resource limitations to the definition of intelligence to be either superfluous, or wrong» ([arXiv:0712.3329](https://arxiv.org/abs/0712.3329) [parcial]).
- **Hughes et al.** definen lo abierto respecto de un observador fijo: «a system is open-ended if and only if the sequence of artifacts it produces is both novel and learnable» ([arXiv:2406.04268](https://arxiv.org/abs/2406.04268) [parcial]).
- **Epiplexity** (Finzi et al., 2026) es la más cercana a Wolfram: mide la estructura que extrae un observador acotado en tiempo. La regla 30 tiene «maximal time-bounded entropy that is produced but no epiplexity», mientras que la 54 tiene mucha ([arXiv:2601.03220](https://arxiv.org/abs/2601.03220) [parcial]).
- **ARC** llegó al mismo punto que Newell y Simon: «it is thus no longer possible to assign a score to an approach, but only to the combination of an approach plus a compute budget» ([ARC Prize 2024](https://arxiv.org/abs/2412.04604) [parcial]).

La teoría de la información algorítmica da la tasa de cambio que necesita una medida de atajos.

- **Levin** define Kt como el largo del programa más el logaritmo de su tiempo ([Filan, Hutter y Leike, arXiv:1604.03343](https://arxiv.org/pdf/1604.03343) [parcial]). Su búsqueda universal cuesta del orden de 2^(largo)·tiempo, una constante exponencial que solo se vuelve práctica con un prior fuerte. OOPS probó 93.994.568.009 prefijos y corrió 678.634.413.962 pasos en cuatro días ([cs/0207097](https://arxiv.org/pdf/cs/0207097) [parcial]).
- **Bennett** da la definición de valor que mejor encaja con Wolfram: «the value of a message is the amount of mathematical or other work plausibly done by its originator, which its receiver is saved from having to repeat» ([Bennett 1988](https://web.archive.org/web/2016/http://researcher.watson.ibm.com/researcher/files/us-bennetc/UTMX.pdf) [parcial]).
- **Schmidhuber** fija el tipo de cambio entre bits y tiempo: «compression by one bit is worth as much as runtime reduction by a factor of 2». Y lo liga al descubrimiento: «An unusually large compression breakthrough deserves the name discovery» ([arXiv:0812.4360](https://arxiv.org/pdf/0812.4360) [parcial]).
- **Los premios de compresión** muestran el límite práctico. La FAQ del Hutter Prize lo admite: «even if we reach K(x), we will never know whether we have done so» ([FAQ](http://prize.hutter1.net/hfaq.htm) [entero, preguntas elegidas]).
- **Delétang et al.** muestran que no cobrar el modelo distorsiona el puntaje: Chinchilla 70B comprime enwik9 al 8,3% en bruto y al 14.008,3% si se cuentan sus pesos ([arXiv:2309.10668](https://arxiv.org/pdf/2309.10668) [parcial]).

Hay tres propuestas de 2026, todas preprints:

- **Pass** define el valor como cuánto más fácil se vuelve obtener un artefacto, y él mismo marca el problema: «a random string may have high production difficulty while having no substantive value». Su autor declara haber usado mucho ChatGPT y Claude ([arXiv:2608.16438](https://arxiv.org/pdf/2608.16438) [parcial]).
- **El C-test ONE** liga la dificultad a Kt: «A linear increase in the number of Kt bits corresponds to an exponential growth of search compute» ([arXiv:2610.14005](https://arxiv.org/pdf/2610.14005) [parcial]).
- **OMNIS** prueba una cota: «each bit of structural knowledge... removes at most one bit of search» ([arXiv:2606.13799](https://arxiv.org/pdf/2606.13799) [parcial]).

Achille y Soatto resumen por qué el tiempo es obligatorio: «Without time penalties, optimal inference can be achieved brute-force without any learning or insight» ([arXiv:2510.12066](https://arxiv.org/pdf/2510.12066) [parcial]).

La inferencia más útil de estas notas es que la línea divisoria es **tiempo sí o tiempo no**. Las definiciones de largo de descripción sin tiempo (Solomonoff, Legg y Hutter, Chollet, la compresión básica) no ven la diferencia que le importa a Wolfram: la regla 30 tiene una descripción cortísima y aun así no deja saltar adelante. La nota de información algorítmica lo formaliza con una cota: Kt(x_n) ≤ |R| + K(n) + log2 T(n) + O(1). Una regla irreducible simple parece entonces fácil de describir, y lo irreducible solo encarece la predicción. De ahí sale una regla de diseño: el puntaje tiene que separar el costo de describir del costo de predecir el estado lejano.

Todas las tasas que aparecen en las fuentes son la misma: un bit vale un factor dos de tiempo. Está en Kt, en el cociente de Solomonoff, en la compresión con tiempo de Schmidhuber, en Pass, en OMNIS y en Hernández-Orallo. Entonces una idea se puede medir como el logaritmo en base 2 del costo sin ella menos el logaritmo del costo con ella, siempre para un buscador declarado. El factor de unas 1000 veces de OOPS equivale a unos 10 bits, y el 2,3 neto de 1958 a algo más de un bit. Sobre la irreducibilidad formal, la nota no encontró ningún teorema publicado que la ligue con la profundidad lógica o con Kt, y ningún objeto explícito está probado irreducible ([Zwirn y Delahaye](https://arxiv.org/abs/1111.4121) [entero]).

La distinción entre aplicar un tipo de regularidad conocido y encontrar un tipo nuevo solo se volvió operativa respecto de una biblioteca fija. DreamCoder lo explica así: «Library learning decreases depth at the expense of breadth» ([arXiv:2006.08381](https://arxiv.org/abs/2006.08381) [parcial]). ARC-AGI-3 lo aplica como test: dos entornos son del mismo tipo si un solo programa los resuelve siendo «at least 50% shorter than the concatenation of two independent solution programs» ([arXiv:2603.24621](https://arxiv.org/abs/2603.24621) [parcial]).

## Un paper de primer nivel tiene que sobrevivir a los anuncios que ya cayeron

Los casos escépticos documentados caen por tres vías, y cada una pide un control distinto: el resultado ya estaba en la literatura, el verificador tenía un agujero o los datos no eran confiables.

**Ya estaba en la literatura.**
- El anuncio de soluciones de GPT-5 a diez problemas de Erdős (octubre de 2025) resultó ser literatura existente, y los posts se borraron ([The Decoder](https://the-decoder.com/leading-openai-researcher-announced-a-gpt-5-math-breakthrough-that-never-happened/) [entero; las fuentes primarias no se vieron]).
- La auditoría del AI Scientist encontró que marcó como novedosas las diez ideas generadas, entre ellas el «micro-batching for SGD». También halló números incorrectos o alucinados en 4 de 7 manuscritos, y lo comparó con «an unmotivated undergraduate student rushing to meet a deadline» ([Beel, Kan y Baumgart, arXiv:2502.14297](https://arxiv.org/html/2502.14297v3) [entero, cuerpo]).
- El 24% de las propuestas de investigación hechas por IA eran paráfrasis o préstamos sin atribución ([Gupta y Pruthi, arXiv:2502.16487](https://arxiv.org/html/2502.16487v3) [parcial]).
- De diez compuestos de GNoME elegidos al azar, los diez tenían una estructura identificable en ICSD: «we have yet to find any strikingly novel compounds» ([Cheetham y Seshadri](https://pmc.ncbi.nlm.nih.gov/articles/PMC11044265/) [parcial]).

**El verificador tenía un agujero.**
- El CUDA Engineer de Sakana tenía «exploits in the evaluation code». Corregido, la aceleración mediana pasó de 1,13× a 0,82× ([TechCrunch](https://techcrunch.com/2025/02/21/sakana-walks-back-claims-that-its-ai-can-dramatically-speed-up-model-training/) [entero]; [EvoEngineer, A.8](https://arxiv.org/html/2510.03760) [parcial]).
- En SWE-Bench+, filtrar los parches tramposos baja la tasa de resolución de 12,47% a 3,97% ([arXiv:2410.06992](https://arxiv.org/abs/2410.06992) [resumen]).

**Los datos no eran confiables.**
- El MIT retiró un preprint porque «has no confidence in the provenance, reliability or validity of the data» ([MIT](https://economics.mit.edu/news/assuring-accurate-research-record) [entero]).

Para descubrimiento importa además que verificar no es fácil para los modelos. Encontrar contraejemplos a envíos incorrectos funciona en menos del 9% de los casos, y los autores advierten que la verificación «can sometimes be harder for models than solving the problem correctly» ([REFUTE, arXiv:2502.19414](https://arxiv.org/html/2502.19414) [parcial]).

Los estándares de método vienen sobre todo de la optimización de caja negra.

- **COCO** cuenta como tiempo el número de evaluaciones. Su aRT incluye las corridas fallidas, y su regla es que «the fixed-target approach is superior to the fixed-budget approach», porque da una escala de razón ([arXiv:1605.03560](https://ar5iv.labs.arxiv.org/html/1605.03560) [entero]).
- **El protocolo experimental de COCO** exige declarar cuánto se afinó cada algoritmo y dice: «Algorithms are only comparable up to the smallest budget given to any of them» ([arXiv:1603.08776](https://ar5iv.labs.arxiv.org/html/1603.08776) [entero]).
- **Bartz-Beielstein et al.**: «comparisons of tuned versus untuned algorithms are not fair and should be avoided» ([arXiv:2007.03488](https://ar5iv.labs.arxiv.org/html/2007.03488) [parcial]).
- **El costo por éxito** de Erol et al. es la misma cuenta que el aRT. Avisan que un adivinador al azar puede parecer el más barato, y piden excluirlo y exigir que el modelo acierte en k intentos seguidos (pass^k) ([arXiv:2504.13359](https://arxiv.org/html/2504.13359v2) [parcial]).
- **Kapoor et al.** muestran que tres líneas de base simples no difieren del mejor agente complejo, a un costo que puede ser casi cien veces menor, y advierten: «Accuracy alone cannot identify progress because it can be improved by scientifically meaningless methods such as retrying» ([arXiv:2407.01502](https://arxiv.org/html/2407.01502) [entero, cuerpo]).
- **La estadística mínima** también está escrita. Para detectar tres puntos de diferencia con 80% de potencia hacen falta unas 1.000 preguntas, con errores agrupados y comparaciones pareadas ([Miller, arXiv:2411.00640](https://arxiv.org/html/2411.00640) [parcial]).
- **La revisión de 445 bancos** encontró que solo el 16,0% usa incertidumbre o estadística ([Bean et al., arXiv:2511.04703](https://arxiv.org/html/2511.04703) [entero]).
- **La convocatoria de NeurIPS 2026** pide que cada envío diga «what claims it supports, under what assumptions, and what limitations apply» ([CfP 2026](https://neurips.cc/Conferences/2026/CallForEvaluationsDatasets) [entero]).
- **La crítica estadística al gráfico de METR** recuerda que las corridas repetidas no son independientes: se observa un 83% de vectores unánimes donde un modelo independiente predice un 60%. Hay que agrupar los intervalos por tarea ([Nguyen y Fithian, arXiv:2610.12466](https://arxiv.org/abs/2610.12466) [entero]).

Los bancos influyentes comparten rasgos: una tarea de significado obvio, verificación exacta, ítems privados o generados por procedimiento, una línea de base humana medida, mucho margen al lanzarse y un solo número. SWE-bench sacaba 1,96% al lanzarse ([resumen](https://arxiv.org/abs/2310.06770)). La contracara es ARC-AGI-1: en 2020, el 49% de su evaluación privada lo resolvió al menos un equipo con «variations of brute-force program search», y por eso ARC-AGI-2 se diseñó «to minimize susceptibility to naive or computationally intensive brute-force program search techniques, since such tasks provide no signal» ([arXiv:2505.11831](https://arxiv.org/html/2505.11831) [parcial]). La nota de métodos infiere que en descubrimiento la fuerza bruta no es ruido que haya que esconder sino el rival a vencer, y que la contabilidad de COCO registra una búsqueda larga como un costo, no como un fracaso ni como un éxito gratis.

La objeción de que es «un juguete» se responde con evidencia, no con fe. Un modelo mínimo vale si comparte la clase de universalidad del sistema, y eso es discutido ([SEP, Models in Science](https://plato.stanford.edu/entries/models-science/) [parcial]). Para descubrimiento hay además un precedente de escalera de pistas. En el benchmark del speedrun, sin pistas ningún agente recupera ni el 20% de la aceleración humana, y con todas llegan a cerca del 46% ([Zhao et al., arXiv:2506.22419](https://arxiv.org/html/2506.22419) [parcial]).

## Tres cuentas que hoy viven separadas alcanzan para una medida publicable

Lo que sigue es una inferencia de este informe, armada con piezas que las notas documentan. No es un diseño probado. La medida responde a la pregunta de Wolfram sin puntuar el interés, que él mismo considera una elección humana. Puntúa en cambio si el atajo existe, cuánto adelante deja saltar y cuánto costó encontrarlo.

| Cuenta | Qué mide | Unidad | Pieza que ya existe | Riesgo documentado |
|---|---|---|---|---|
| Existencia | Si el objeto propuesto es exacto | Sí o no, decidido por una máquina | Replay en Lean del kit del Premio Rule 30; conmutación de Israeli–Goldenfeld; transductor de dominios; ecuación de Hattori–Takesue; Coq-BB5 | `skipKernelTC`, hipótesis vacías, granulados triviales a la regla 0 |
| Valor | Cuánto cómputo ahorra para predecir el paso t | Bits: log2(costo de simular) − log2(costo con el atajo); orden de complejidad | Valor de Bennett; compresión con tiempo de Schmidhuber; O(log t) de Moore frente a O(t²) | Programas cortos que vuelven a simular (KoLMogorov Test); dependencia de la máquina |
| Costo de hallarlo | Recurso hasta el primer certificado, contando las fallas | Evaluaciones, tokens, USD; aRT o costo por éxito | COCO; L*/TTT; búsqueda exhaustiva de proyecciones; SAT; OMNIS | Rival sin afinar; presupuestos desiguales; prompts que traen el objetivo |
| Controles | Que no sea memoria ni trampa | — | Mundos sorteados después del corte de entrenamiento; el par 30 frente a 90/150/210; las 16 reglas sobreyectivas no afines | Novedad juzgada a mano; concentración de entregas |

El banco de ítems ya existe, con controles incluidos. Las 16 reglas elementales sobreyectivas no afines son ítems difíciles en los que no hay granulado trivial. La barrera de la regla 30 frente a la 90, la 150 y la 210 es un par de control ya probado en Lean. El dominio de 14 estados de la 110 es un objeto exacto que todavía no tiene explicación. Y los problemas abiertos de Life ya vienen en formato verificable por máquina. Falta lo que ninguna fuente hace: un ítem sin bolsillo conocido, para medir si el sistema sabe decir «acá no hay nada», y un criterio de no trivialidad escrito antes de mirar.

## El cupo de búsquedas se agotó y estas líneas quedaron sin buscar

El buscador web de la sesión tenía un cupo compartido entre todos los agentes, informado como de 200 búsquedas, y se agotó mientras se escribían las notas. Las nueve notas declaran unas 114 búsquedas propias (30, 18, 15, 11, 10, 9, 9, 8 y 4) y unas 16 rechazadas. Siete de los nueve lectores se toparon con el corte, y después solo bajaron URLs que ya conocían. Hay dos excepciones. La nota sobre trabajos cercanos hizo solo 4 búsquedas y atribuye sus huecos a alcance o tiempo, no al cupo. Y uno de los lectores del material de Wolfram fue cortado por límite de uso, sin que se sepa cuántas búsquedas había hecho. Las líneas que quedaron sin buscar, o que no se pudieron cerrar, son estas:

| Línea | Nota de origen | Qué queda en duda |
|---|---|---|
| Trabajos posteriores a Song y Grochow (por ejemplo, SAT con N ≥ 8); el algoritmo de Magiera y Dzwinel | Objetos exactos | Si alguien ya granuló la 30, 45, 106 o 154 a escalas mayores |
| Hanson–Crutchfield 1992 y 1997; defectos de Pivato; Eloranta–Nummelin; catálogos de planeadores de la 110 (Cook 2004; Martínez et al.) | Objetos exactos | La lista exacta de partículas de la 110 |
| Formalizaciones generales de autómatas en Mathlib, Coq o Isabelle; listas de problemas abiertos de autómatas elementales | Objetos exactos | Si hay bibliotecas reutilizables fuera del kit del Premio Rule 30 |
| Noticias de IA de 2025 y 2026 sobre problemas de autómatas; posts sobre LLM en el subforo de otras reglas | Life | Si hubo algún aporte de IA reconocido fuera de lo leído |
| La búsqueda «LLM, atajo, simular un autómata, reducibilidad computacional»; game-of-life-bench | Panorama de bancos | Si existe un banco de atajos que no apareció |
| Bancos OEIS con LLM; MDL en ARC-AGI-2 y 3; quienes citan al KoLMogorov Test en 2025 y 2026; críticas nuevas a CTM/BDM; búsqueda de Levin después de 1997; Antunes et al. 2006; parte II de Zwirn–Delahaye | Información algorítmica | Si ya hay un puntaje de compresión que cuente el tiempo |
| Langley et al. 1987; Simon 1973; Ritchie 2007; Wiggins 2006; Jordanous; informe de ARC Prize 2025 y cuerpo de ARC-AGI-2; posiciones de 2025 y 2026 sobre redescubrimiento; Stitch, LILO y otras bibliotecas; comparaciones publicadas de Wolfram con filósofos | Filosofía | La vara original de BACON y si alguien ya hizo esta comparación |
| LLaMEA/BLADE; programación genética en scheduling; LLM con optimización bayesiana en materiales; ENIGMA/Deepire; NeuroBack; DreamCoder; AlphaProof y Ramsey 2026; CodeEvolve, DeepEvolve y AlphaResearch | Búsqueda ahorrada | Más comparaciones de IA contra un rival afinado |
| Crítica a la «rediscovery» del AI co-scientist (febrero de 2025); Agents4Science 2025; revisiones hechas por IA en ICLR 2026; citas alucinadas en NeurIPS 2025; el episodio FrontierMath/o3; desmentidos y aportes genuinos de 2026; «Signal and Noise»; varianza entre semillas (Meta, 2024); el paper de 2025 sobre líneas de base humanas; perfiles Dolan–Moré y Moré–Wild (solo snippets) | Métodos y escépticos | El lado escéptico de 2026 y la estadística de varianza |

## Conclusión

La verificación no es el cuello de botella. Ya hay verificadores exactos y baratos comparados con encontrar: el replay en el núcleo de Lean, las tablas de conmutación, el transductor de dominios, el censo reproducible de Life. Lo que falta son dos números que ninguna fuente leída informa: cuánto cómputo ahorra el atajo encontrado y cuánto costó encontrarlo frente al mejor rival sin el truco, afinado y con el mismo presupuesto. La objeción de Wolfram sobre el interés no bloquea la medida. Alcanza con puntuar existencia, alcance y costo y dejar el interés afuera; su propio criterio de «no derivable de lo anterior» ofrece además un sustituto contable. La evidencia sobre ahorro de búsqueda sugiere que el resultado de una evaluación así no va a ser «la IA gana» o «la IA pierde». Va a depender de si el rival clásico tiene guía propia: la IA rinde en espacios de programas y de pruebas, y no aporta donde una búsqueda local rápida ya llega.

Este informe tiene límites. Se apoya en nueve notas de una sola sesión, con el cupo de búsquedas agotado a mitad de camino. Muchas fuentes se leyeron en parte, de resumen o a través de una herramienta. Los números de Wolfram no se recalcularon. Los cómputos propios de las notas (sobreyectividad, leyes de conservación hasta rango 12) no están publicados, y el segundo usa punto flotante. Los conteos del Premio Rule 30 salen de una sola foto del día, sin abrir ningún ensayo entregado. Cada «no se encontró» vale solo dentro de las búsquedas que se declaran. La medida de tres cuentas es una inferencia, no un resultado.

## Pendientes

1. Correr las búsquedas de la tabla anterior cuando haya cupo. Empezar por los trabajos posteriores a Song y Grochow, las partículas de la 110 y los bancos OEIS con LLM, porque pueden cambiar qué está abierto.
2. Rehacer con aritmética exacta el cómputo propio de leyes de conservación hasta rango 12, y publicar o descartar el de sobreyectividad que explica el 240/16.
3. Abrir una muestra de los ensayos entregados al Premio Rule 30 y contar cuántos tocan factores, conservación o dominios, y cuántos son variantes de un mismo método.
4. Leer enteros los textos que quedaron en resumen o en extracto y que sostienen afirmaciones de este informe: el KoLMogorov Test según la nota de métodos, LLM-SRBench, la tabla de ARC-AGI-3 y las páginas de LifeWiki.
5. Antes de cualquier diseño, decidir con el responsable del proyecto si se mide con una tanda mínima cuánto cuesta el rival clásico (búsqueda exhaustiva de proyecciones, Hattori–Takesue) en reglas sorteadas. Nada de esto se corrió.
