# Trabajo previo: tres búsquedas del 16-nov-2026

Tres lectores secundarios (agentes de búsqueda) trabajaron en paralelo, cada uno con una pregunta. En total
unas 150 búsquedas y unas 120 páginas abiertas. **Casi todo es resumen o lectura a través de una
herramienta que resume; ningún paper se leyó entero.** Los números no se cotejaron contra las tablas de los
PDF. "No encontré" no es "no existe". Yo (Claude) no abrí ninguna de estas fuentes: esto es de segunda mano.

Marcas de lectura: **[abs]** solo el resumen · **[txt]** texto completo vía herramienta que resume ·
**[pdf]** leído directo · **[2ª]** solo lo que mostró el buscador · **[M]** de memoria del modelo.

## En diez líneas

1. No apareció nadie que mida a un agente con **eventos fuera de su presupuesto de cómputo** ni con mundos
   de **varias escalas de tiempo** con la regla a la vista.
2. No aparecieron **gemelos que difieran solo en reglas que nunca se usan** en lo observable. Lo más cercano:
   pares de programas equivalentes o no (EquiBench).
3. No apareció un banco hecho con **regularidades que se rompen tarde**, ni uno construido sobre invariantes
   o imposibilidad, ni uno sin juez que plante ideas "generando hacia adelante" fuera de la geometría.
4. Con agentes sobre sistemas **armados a propósito** y verdad conocida, solo hay un caso y es con redes
   neuronales (AgenticInterpBench). Sobre autómatas, máquinas de Turing o máquinas virtuales chicas: nada.
5. **Dónde hay margen medido en la frontera (2026):** encontrar estructura escondida interactuando (autómata
   oculto de 8–9 estados: 57,5%; DiG-bench 50/70; DiscoverPhysics, la mitad de 22 mundos) y construir un
   testigo no obvio (ingeniería inversa a escala real: 31,5%).
6. **Dónde no:** FrontierMath nivel 4 (88% en junio); ExplorationBench (89%); invariantes de ciclos (ya
   sabido).
7. Conductas ya nombradas que nos tocan: con intérprete de código, los modelos **toman un chequeo empírico
   por garantía universal** en 54,3% de las soluciones de alto riesgo revisadas (Fatahi Bayat et al.); entre
   8% y 44% de las respuestas dadas por buenas salen de búsqueda, enumeración o adivinanza (Ren et al.). Las
   dos mediciones usan un LLM de juez.
8. La opción de abstenerse cambia todo: ofrecer "es azar" llevó el acierto de 26,8% a 78,0% (Idola
   Tribus); permitir abstención bajó de 96% a 16% los falsos "mejoró" (Placebo).
9. ARC-AGI-4 no tiene formato publicado. El plan anterior, de segunda mano: puntuar si una herramienta o
   notación que la IA inventa acelera los problemas siguientes.
10. Mecanismo más trasplantable: el de AlphaGeometry. Generar hacia adelante al azar, rastrear hacia atrás, y
    contar **lo que la solución usa y el enunciado no menciona**. Esa es su definición mecánica de "la idea".

## A. Sistemas con verdad conocida, analizados por agentes (52 búsquedas)

**"¿Podría un neurocientífico entender un microprocesador?" y seguidores**
- Con agentes de IA sobre un procesador, circuito o programa: no se encontró nada.
- Lueckmann, Jain, Januszewski 2026, [arXiv:2602.04492](https://arxiv.org/abs/2602.04492) [abs]: pez cebra
  simulado con circuito conocido; una búsqueda guiada por LLM arma modelos. Predecir bien no alcanzó para
  recuperar el circuito real.
- Welch et al. 2025, "Could a Neuroscientist Understand a Box of Sand" [2ª]: el analista no es una IA.

**Tracr / InterpBench**
- Khan et al. 2026, AgenticInterpBench, [arXiv:2606.24026](https://arxiv.org/abs/2606.24026) [abs+txt]:
  agentes LLM sobre sistemas compilados desde un programa conocido (RASP → transformer). 84 circuitos, 163
  componentes. Rol exacto de cada componente: 0,67–0,79 según modelo. El circuito ya viene localizado y el
  resto lo puntúa un juez LLM.

**Ingeniería inversa**
- SRE-Bench, Spence et al. 2026, [arXiv:2608.11469](https://arxiv.org/abs/2608.11469) [abs]: 262 binarios
  privados, corrección determinista. Resuelven entero: GPT-5.6-Sol 31,5%, Claude Fable 5.1 26,9%.
- Nishizaka et al., NDSS BAR 2026 [pdf, pp. 1–6]: 24 "crackmes" de 2025; 58–79% por agente. De 8 con máquina
  virtual propia resolvieron 6 escribiendo su emulador. **Fallan con pistas falsas y con lo que se aparta
  de lo estándar, no con código ilegible.**
- CREBench, Chen et al. 2026, [arXiv:2604.03750](https://arxiv.org/abs/2604.03750) [abs]: 432 retos
  criptográficos; GPT-5.4 recupera la clave en 59%.
- Menaged et al. 2026, [arXiv:2606.16576](https://arxiv.org/abs/2606.16576) [txt]: autómata oculto de hasta 9
  estados; el mejor, 57,5% en 8–9 estados. **Saben escribir el algoritmo clásico (L\*) y no lo ejecutan
  bien.** Hasta 50 dólares por partida.
- EsoLang-Bench, Sharma & Chopra 2026, [arXiv:2603.09678](https://arxiv.org/abs/2603.09678) [abs]: programar
  en cinco lenguajes esotéricos, 0–11% contra 100% en Python.

**Comportamiento a largo plazo**
- PetriBench, Koussios et al. 2026, [arXiv:2609.19883](https://arxiv.org/abs/2609.19883) [txt parcial]: redes
  de Petri a la vista, respuesta exacta, dos familias de "horizonte infinito" que no salen simulando. Nivel
  difícil, GPT-5.6 Sol: 69,0% y 92,0%. Aparentemente sin herramientas. Un verificador clásico ya las resuelve.
- Wiki de bbchallenge, Fractran [txt]: Claude Opus 4.6 probó que no paran los 140 pendientes de tamaño 21 y,
  con Lean, 1.997 de 2.003 de tamaño 22.
- Críticas al paper de DeepMind (arXiv:2610.22603): una sola, un repositorio anónimo que dice haber cerrado
  antes 3 de las 11 máquinas "nuevas". No verificado.

**Mundos de varias escalas / eventos fuera del presupuesto:** nada (5 búsquedas). Lo vecino es de regla
escondida y corto plazo: ExplorationBench ([arXiv:2609.30199](https://arxiv.org/abs/2609.30199) [txt]:
mejores 89% y 81%; **el mismo sistema varía hasta 73 puntos entre corridas**), DiscoverPhysics
([arXiv:2605.26087](https://arxiv.org/abs/2605.26087) [abs]), DiG-bench
([arXiv:2608.12593](https://arxiv.org/abs/2608.12593) [abs]).

**Ideas para tomar:** el par de control de PetriBench (la misma pregunta en versión simulable y no
simulable); un rival clásico como vara (contar solo lo que el mejor método sin IA no cierra); dureza por
apartarse de lo estándar y no por ilegibilidad; una sola respuesta comprometida; varias corridas por
instancia.

## B. Inducir contra derivar; falsos descubrimientos (64 búsquedas)

**Patrones que se rompen tarde; simular contra derivar**
- Wolfram, "Towards a Theory of Bugs" (21-jul-2026) [txt]: máquinas de Turing diminutas; una calcula n+1
  para todo n hasta 62 y en 63 da 72. No prueba predicciones de IAs.
- Ganeshan 2026, "Where Induction Runs Out", [arXiv:2608.29411](https://arxiv.org/abs/2608.29411) [abs]: en
  más de 20.000 sucesiones de OEIS, 89,98% de las que ajustan una recurrencia en algún prefijo no ajustan
  ninguna en el largo completo. Tres modelos dudaron en vez de inventar.
- Fatahi Bayat et al., ACL 2026, "From Proof to Program",
  [arXiv:2511.10899](https://arxiv.org/abs/2511.10899) [abs, txt]: 1.679 problemas, 7 modelos. Con
  intérprete de código el modelo "mistakes empirical checks for universal guarantees" en 54,3% de las
  soluciones de alto riesgo revisadas a mano. Juez LLM; solo sobre respuestas correctas.
- Ren et al. 2026, "Right Answer, Wrong Method", [arXiv:2608.02442](https://arxiv.org/abs/2608.02442) [txt]:
  8,2% a 44,1% de las respuestas acreditadas salieron de búsqueda numérica, enumeración o adivinanza de
  patrones. Panel de LLMs.

**Gemelos**
- Wei et al., EquiBench, EMNLP 2025, [arXiv:2502.12466](https://arxiv.org/abs/2502.12466) [txt]: 2.400 pares
  de programas; en una categoría los equivalentes quitan código muerto y los no equivalentes quitan código
  vivo (mejor: 76,2%). Sí/no, sin herramientas.

**Falso descubrimiento contra verdad conocida**
- Suppa & Kopcan, taller NeurIPS 2026, "The Placebo Improvement" [abs]: cambios de código con salida
  idéntica. Claude Opus 4.5 afirmó una mejora en 16% de los casos con abstención permitida y en 96% con
  sí/no forzado.
- Rewolinski et al. 2026, [arXiv:2604.11003](https://arxiv.org/abs/2604.11003) [abs]: conclusión afirmativa
  sin sustento en 6 de 11 conjuntos de datos reales.
- ARIA, "Can an AI Scientist really discover knowledge?" (jun-2026) [pdf, pp. 1–6]: cinco mundos de regla
  escondida, corregidos por un modelo: "We currently do not penalise for incorrect rules".

**Predecir desde el mecanismo**
- Vafa et al., ICML 2025, [arXiv:2507.06952](https://arxiv.org/abs/2507.06952) [abs]: modelos que predicen
  bien órbitas no aplican mecánica newtoniana a tareas nuevas.
- Thimmaiah et al., PLSemanticsBench, ICML 2026, [arXiv:2510.03415](https://arxiv.org/abs/2510.03415) [abs]:
  con las reglas dadas, hasta 90% con la semántica estándar y **40 a 60 puntos menos con la semántica
  cambiada**.

**Abstenerse cuando no hay nada**
- Ishikawa et al., EMNLP Findings 2025, "The Idola Tribus of AI",
  [arXiv:2510.09709](https://arxiv.org/abs/2510.09709) [txt]: 100 series al azar; acierto medio 26,8%;
  ofreciendo "azar" como respuesta, 78,0%. Juez: o3.

**No encontrado:** un banco hecho de regularidades que se rompen tarde; ninguna evaluación que use "grue" o
la novedad de uso; mundos con regla a la vista puntuados más allá de lo simulable (fuera de los que ya
conocíamos); gemelos que difieran solo en reglas nunca disparadas.

**Ideas para tomar:** informar la tasa de afirmaciones nulas junto con la de compromiso y un control
positivo, con protocolo permisivo y forzado; fijar la opción de abstenerse antes de correr; usar un
aprendiz inductivo exacto como rival; sacar trampas enumerando máquinas chicas; redefinir símbolos
familiares para que lo que el modelo "sabe" choque con las reglas dadas.

## C. Maneras nuevas de medir descubrimiento (32 búsquedas)

**ARC-AGI-4.** Sin formato ni puntaje publicados. De segunda mano (36Kr, 16-sep-2026): el plan era currículos
largos donde cada nivel reusa lo anterior, y después invención, quizá puntuada por si una herramienta o
notación creada por la IA acelera lo que sigue. Obstáculo declarado: los inventos no tienen línea de base
humana. ARC-AGI-3 ([arXiv:2603.24621](https://arxiv.org/abs/2603.24621) [txt]): puntaje por nivel =
(acciones humanas / acciones de la IA)², con tope.

**Medir una idea sin juez**
- Patel et al. 2026, [arXiv:2609.28603](https://arxiv.org/abs/2609.28603) [txt]: interés de un teorema =
  líneas de demostración por carácter de enunciado; utilidad = teoremas que lo usan × sus líneas.
- Herrmann & Schmidhuber 2026, [arXiv:2605.14831](https://arxiv.org/abs/2605.14831) [txt]: un avance es una
  caída en el largo del programa más corto cuando crece el tiempo permitido. Solo calculable enumerando.
- MODES, Dolson et al. 2019 [leído]: novedad = componentes nunca vistos cuyo linaje persiste; las partes que
  importan se encuentran apagándolas una por una.
- Horizonte de METR [txt]: tiempo humano por tarea y una curva logística de dos parámetros; el número es
  donde cruza 50%. Sus intervalos son anchos (alrededor de un factor 2 o más).

**Asimetrías entre quien arma y quien resuelve**
- **AlphaGeometry**, Trinh et al. 2024 [txt]: premisas al azar, deducción barata hacia adelante, rastreo
  hacia atrás. 100 millones de teoremas; 9% necesita una construcción auxiliar, definida mecánicamente como
  lo que la demostración usa y de lo que la conclusión no depende. Hace falta la idea: con deducción sola
  salen 14 de 30; con construcciones, 25 de 30.
- Rompecabezas de ajedrez, Feng et al. 2025, [arXiv:2510.23881](https://arxiv.org/abs/2510.23881) [txt]: lo
  contraintuitivo de una jugada = la profundidad de búsqueda a la que el motor llega a su evaluación final.
- Token Games, Henniger & Poesia 2026, [arXiv:2602.17831](https://arxiv.org/abs/2602.17831) [txt]: el
  proponente da un testigo que se comprueba corriendo código. **Lo más difícil resultó ser hashes y
  cifrados: cómputo y memoria, no ideas.**
- SKATE, Gould et al. 2025, [arXiv:2508.06111](https://arxiv.org/abs/2508.06111) [abs]: autopreferencia de
  los modelos al proponer tareas.
- FrontierMath: Open Problems [txt]: un programa verificador por problema. De 50, 5 resueltos por IA.

**Bancos de "descubrimiento científico" y su debilidad**
- ARIA "Albert" 2026 [txt]: correctores LLM, mejor de 3, reglas erróneas sin penalizar.
- DiG-bench [txt]: 70 juegos hechos a mano; un modelo saca 69/70 con las reglas dadas y 18/70 sin ellas.
  Una sola semilla, sin línea de base de fuerza bruta.
- WorldTest, [arXiv:2510.19788](https://arxiv.org/abs/2510.19788) [txt]: 43 mundos escritos a mano, puntaje
  mecánico, personas 0,935.
- NewtonBench, [arXiv:2510.07172](https://arxiv.org/abs/2510.07172) [txt]: ley conocida con 1–2 mutaciones.
  GPT-5: 75,9% en total, 40,3% en lo más difícil. Juez LLM.

**Los cinco mecanismos más trasplantables (según el lector), con su debilidad**
1. Generar hacia adelante, rastrear hacia atrás, contar lo que el enunciado omite (AlphaGeometry). Las ideas
   quedan acotadas por el motor de quien arma.
2. Perilla de "distancia a lo conocido" con lectura de horizonte. Una estructura conocida mutada puede
   pedir solo encontrar el parche.
3. Valor de una idea = ahorro en los problemas siguientes. El costo depende del arnés.
4. Brecha entre un resolvedor superficial y uno profundo como filtro de "pide una idea". Puede ser puro
   cómputo.
5. Duelos proponente–resolvedor con verificación exacta. Medido: colapsa en hashes y constantes memorizadas.
