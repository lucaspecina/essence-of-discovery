# GPT Astra, dos vueltas sobre las candidatas y la síntesis (16-nov-2026)

> `gpt-6-astra` por API (Azure de Lucas), esfuerzo de razonamiento alto. Primera vuelta: 21.125 tokens de
> entrada, 10.687 de salida, 340 segundos. La carta y las preguntas están en
> [lo que se les mandó](2026-11-16-critics-briefs.md). Astra no tuvo acceso al repo ni a internet: lo que
> cita de literatura es de memoria, y lo dice. **Es una voz más; no decide.**
>
> **Resumen de Claude.**
> *Primera vuelta.* (1) El límite de fondo es de identificación: acertar, usar pocos intentos o mejorar de
> golpe no distingue recuerdo, búsqueda guiada e idea nueva. (2) Los "relojes" (C1) los resolvería en el
> ejemplo modular; dos o tres niveles independientes no son barrera; lo que podría frenarla es el
> acoplamiento entre niveles. No conoce un C1 compacto y certificable que no resolvería por falta de idea.
> (3) Los pares de una regla prueban que la trayectoria observada no alcanza; no certifican comprensión.
> (4) Propone dos diseños propios: descubrir una partícula que viaje en un autómata nuevo (el certificado
> es un solo ciclo) e inventar el experimento que separa explicaciones. (5) "De juguete" es una objeción
> válida contra el alcance: acelerar el reloj no explica la regla que el reloj transporta.
> *Segunda vuelta.* (1) Mi diagnóstico ("construcción sistemática ⇒ desarmado sistemático") es falso en
> general. (2) Correr verifica un testigo positivo, no "imposible". (3) "Hacé que pase" sigue siendo buscar
> una entrada; falta un solucionador de restricciones entre los rivales. (4) El "experimento crucial" con
> dos tablas a la vista se resuelve escribiendo el trío distinto. (5) Lo decisivo de la síntesis no es que
> invertir sea difícil sino que permite **entregar, reusar y poner a prueba una representación mediante
> artefactos exactos**. (6) Propone un piloto concreto con reglas de lectura.

---

# PRIMERA VUELTA

[Juicio] **El límite central es de identificación:** acertar, usar pocos intentos o mejorar de golpe no distingue por sí solo recuerdo, búsqueda guiada e idea nueva. Sí pueden medir **hallazgo de una solución nueva para esa instancia, costo, transferencia y sensibilidad al mecanismo**. No son lo mismo.

[Dato] La prueba informa 29 partidas, sin repeticiones por casillero. Además, en `deep-9` y `deep-25` faltó comprobar con un programa propio la resolución desde lo que veía el agente: esa verificación quedó por debajo de la regla dura declarada.

[Juicio] Mi revisión se limita al material pegado. No comprobé código, registros ni enlaces. Las referencias recientes de los adjuntos no cuentan aquí como bibliografía verificada independientemente.

## 1. Objeción más fuerte a cada candidata

- **C1 — Relojes.** [Juicio] Puede medir reconocimiento y resumen de programas, no descubrimiento de fenómenos complejos: acelerar el reloj no explica la regla 30 que transporta. La mata que un resumidor genérico resuelva toda la escalera, o que aumentar niveles solo agregue lectura y errores de implementación.

- **C2 — Mundos salvajes.** [Juicio] Un acierto puede venir de optimización, sesgo de las respuestas o suerte; no demuestra un atajo nuevo. La mata que el éxito desaparezca contra un simulador bien optimizado, o que no puedan distinguir instancias interesantes de mera falta de presupuesto.

- **C3 — Disfraces hondos.** [Juicio] La dificultad general de la conjugación no dice nada sobre la familia finita que ustedes generen. La mata que el trabajo sea deshacer el generador —mecánicamente o con una técnica conocida— y no investigar el sistema.

- **C4 — Diseñadora IA.** [Juicio] Seleccionar juegos porque un modelo falla produce una colección de sus puntos débiles, no una escala neutral. Una pista breve que ayuda tampoco demuestra una «idea»: puede suministrar instrucciones que faltaban. La matan la falta de transferencia a otros modelos y el fracaso fuera del filtro usado para seleccionarlos.

- **C5 — Examen sorpresa.** [Juicio] Mide preparación para una distribución de preguntas, aunque el agente desconozca cada pregunta. La mata que una exploración rutinaria cubra el examen tan bien como investigar; no que exista un objetivo implícito, que es inevitable.

- **C6 — Transferencia.** [Juicio] Ahorrar trabajo puede deberse a código reutilizado, formato, familiaridad o ejemplos, no a un concepto compartido. La mata que controles con igual cantidad de información útil pero sin el supuesto concepto produzcan el mismo ahorro. La matriz no determina un número único de ideas.

- **C7 — Después del corte.** [Juicio] La fecha pública del hallazgo no garantiza ausencia de entrenamiento, ajuste posterior o filtración; además, el método puede ser anterior. La mata no poder documentar la separación temporal real. Sirve para casos de estudio, difícilmente para una escala duradera.

- **C8 — Bifurcaciones.** [Juicio] El examen puede hacer que el clon resuelva en ese momento: mide rendimiento al preguntar, no conocimiento previo directamente. La mata, como «microscopio de ideas», que el salto dependa de la pregunta o del presupuesto del clon; también hay que comprobar qué estado permite realmente copiar la API.

## 2. Cómo atacaría C1

### Procedimiento

[Juicio] Con las reglas completas y ese presupuesto:

1. **Haría un intérprete y un mapa de dependencias:** qué reglas escriben cada zona, qué estados activan otras reglas y dónde puede haber retornos. Mediría la velocidad real; no asumiría que Python alcanza \(10^9\) pasos.
2. **Buscaría ciclos de control**, no primero ciclos del mundo entero: recorridos de la marca, acarreo, retorno, desborde y llamadas a otra zona.
3. **Fabricaría experimentos de borde:** contador casi lleno, marca delante del disparador, tamaños pequeños. Que una regla nunca aparezca en la trayectoria inicial no impide ejecutarla en una intervención.
4. **Propondría un resumen por evento:** estado antes y después del desborde, y número exacto de pasos consumidos. Probaría tamaños pequeños y casos extremos; no tomaría esas pruebas como demostración general.
5. **Compondría los resúmenes.** Si cada vuelta cuesta lo mismo, dividiría; si depende del estado, calcularía el costo acumulado. Después simularía los aproximadamente 450.000 pasos superiores, si entran.
6. **Resolvería el resto exacto:** en \(T\) puede haber un acarreo incompleto o una actualización superior a medio hacer. Ignorar ese detalle puede arruinar una solución conceptualmente correcta.

### Qué esperaría resolver

[Juicio] **Esperaría resolver el ejemplo modular descrito**, si las reglas son legibles y la simulación superior entra en presupuesto. Dos o tres niveles independientes no me parecen una barrera conceptual. Diez repeticiones del mismo patrón podrían ser casi igual de fáciles: se escribe un procedimiento recursivo una vez.

[Juicio] No tengo fundamento para dar un máximo de niveles. Hay que separar **profundidad, cantidad de reglas distintas, acoplamiento entre zonas y costo de implementar la solución**. Tampoco hay una escalera automáticamente «sin techo»: si repetís relojes de 40 bits anidados, el tercer nivel puede quedar fuera de \(10^{18}\).

### Qué podría hacerme fallar

[Juicio] Un candidato sería **tres contadores de 20 bits con realimentación**: el desborde del primero cambia el sentido del segundo; el segundo modifica el umbral del primero según el estado superior. Ya no alcanza con multiplicar períodos. Podría no encontrar el estado resumido adecuado, o encontrarlo y equivocarme al implementarlo. Es una hipótesis de dificultad, no un mundo ya validado.

[Juicio] Un C1 que me derrotaría por recursos se obtiene haciendo que, **aun después de quitar el reloj**, la evolución superior exceda el presupuesto. Eso solo mide cómputo. Una tabla enorme puede derrotarme por contexto. **No conozco un C1 compacto, validado y resoluble con una pista que pueda asegurar que no resolvería por falta de idea.** Afirmarlo sin correrlo sería inventar el resultado.

### Los pares de una regla

[Juicio] Son un control válido **contra extrapolar exclusivamente la trayectoria inicial observada**. No certifican comprensión: leer la diferencia y aplicar un analizador conocido también alcanza. Y no son indistinguibles bajo todos los experimentos permitidos: una fila fabricada puede activar inmediatamente la regla diferente.

[Juicio] Los presentaría por separado, con respuestas equilibradas, varias semillas y modificaciones irrelevantes de control. Pediría además predicciones de tiempos y efectos en condiciones nuevas. El resultado defendible sería: «usó información del mecanismo que la trayectoria inicial accesible no revelaba».

## 3. ¿Predecir lo nunca observado cuenta como descubrimiento?

[Juicio] **Sí, como una clase acotada: descubrir una consecuencia no observada de reglas conocidas.** Mejor nombre para la medida: *predicción derivada del mecanismo fuera del tramo observado*. La novedad para el sujeto y el origen interno de la solución siguen sin demostrarse.

[Juicio] Deja afuera encontrar las reglas, inventar instrumentos, elegir preguntas importantes, construir conceptos y descubrir por observación inesperada. Además, búsqueda e idea no son contrarios: una búsqueda puede producir la representación que permite resolver.

[Literatura — de memoria] Los antecedentes más próximos incluyen:

- **Análisis y verificación de programas:** deducir propiedades de ejecuciones no realizadas; interpretación abstracta de Cousot y Cousot, y aceleración de bucles.
- **Ejecución simbólica y pruebas dirigidas**, como DART: razonar sobre caminos todavía no ejecutados y construir entradas que los activen. Es especialmente próximo a las reglas dormidas de C1.
- **Israeli y Goldenfeld:** predicción de propiedades a escala gruesa en autómatas de comportamiento microscópico complejo.

[Dato] Los adjuntos describen también aceleraciones verificadas de máquinas Busy Beaver y generación de invariantes mediante modelos. Si esas descripciones son correctas, la tarea básica ya tiene antecedentes directos.

[Juicio] El posible aporte no es «predecir sin haberlo visto», sino **aislar cuándo se logra, qué intervención ayuda y qué errores persisten**. No hay base aquí para declarar que ese instrumento no existe.

## 4. Ranking para un trabajo publicable

[Juicio] **Entre las candidatas:**  
**C1+C8 > C4+C6 > C7 > C5 > C2 > C3.**

[Juicio] Mis dos opciones globales serían:

1. **C1 con bifurcaciones limitadas de C8.** Comparar mecanismos independientes contra acoplados, y exploración ordinaria contra intervenciones de borde, manteniendo parecidos el tamaño del texto y el costo de la solución. Es una pregunta concreta sobre *cuándo* falla la predicción. Las sondas medirían rendimiento durante el proceso, no «el instante de la idea».
2. **D1, propuesta abajo:** descubrir objetos persistentes en reglas nuevas. Cambia de verdad qué se le pide descubrir y evita calcular una trayectoria gigantesca para conocer la respuesta.

[Juicio] C6 vendría después de conseguir una familia con margen. C4 puede abastecerla, pero los modelos y semillas del filtro deben quedar separados de la evaluación. Ninguna opción garantiza novedad publicable antes de revisar antecedentes y obtener señal.

## 5. Dos diseños distintos

### D1. Elegir el fenómeno como propiedad, no programar cómo ocurre

[Juicio — propuesta] **Descubrir una partícula que viaje en un autómata nuevo.** Ustedes eligen la propiedad: un patrón finito debe desplazarse sin desintegrarse. No escriben un contador ni un programa que lo emule.

[Juicio — propuesta] Construcción concreta:

- Generar conjuntamente una tabla local y una pequeña secuencia de configuraciones, imponiendo que la última sea la primera trasladada. Cada vecindario debe tener siempre la misma salida.
- Completar libremente las entradas de la tabla no restringidas. Guardar la secuencia como certificado privado y verificarla con otro simulador.
- Dar al agente únicamente la regla, fondo vacío estable y límites de tamaño y período.
- El agente entrega cualquier patrón, período y desplazamiento que cumplan la propiedad; no tiene que recuperar el certificado privado.

[Juicio — deducción] El verificador simula ese período en una región que incluya toda la zona afectada y comprueba la igualdad exacta con el patrón trasladado. Por localidad y simetría de traslación, eso certifica movimiento indefinido. **No hace falta simular hasta un tiempo enorme.**

[Juicio] La dificultad puede pasar de partículas aisladas a colisiones con resultados exactos: por ejemplo, dos partículas producen un oscilador estable. Ahí el objeto descubierto es una organización dinámica, no un reloj escondido. El rival obligatorio es búsqueda optimizada más un solucionador de restricciones; si este último barre la familia, no hay examen de frontera.

[Literatura — de memoria] La búsqueda automática de patrones y naves en el Juego de la Vida tiene larga historia. No presentaría la tarea como inédita. Lo distinto a investigar sería la evaluación entre reglas recién generadas, tipos de organización y ayudas controladas.

### D2. Inventar el experimento que separa explicaciones

[Juicio — propuesta] Entregar varios mecanismos candidatos completos y pedir **un protocolo experimental que los distinga**, no una predicción lejana. Ejemplo: redes de reacciones discretas que, bajo alimentación constante, dan la misma salida; difieren en si poseen memoria persistente, demora o inhibición reversible.

[Juicio — propuesta] El agente puede proponer secuencias breves de alimentación, lavado, reinicio y medición. Debe entregar el protocolo y la respuesta exacta prevista bajo cada mecanismo. Un verificador ejecuta cada candidato y comprueba que las respuestas distinguen todos los casos exigidos, dentro de un costo fijado.

[Juicio] Ustedes conocen el fenómeno y conservan un protocolo testigo. Todos los mecanismos y acciones están especificados: no queda la ambigüedad de WAGER sobre si había información suficiente. La cuestión es **encontrar cómo producir la evidencia**, no extrapolar lo recibido. Se puede variar si basta observar, si hace falta intervenir o si hay que combinar intervenciones.

[Juicio] Sus rivales serían enumeración de protocolos y planificación con restricciones. El margen debe comprobarse contra ellos. Este diseño mide diseño experimental, no todo el descubrimiento.

[Literatura — de memoria] Tiene antecedentes en diseño óptimo de experimentos y secuencias que distinguen máquinas de estados. Tampoco vendería novedad absoluta.

[Juicio] La diferencia de fondo: **D1 entrega un objeto nuevo; D2 entrega un experimento nuevo.** Ninguno consiste simplemente en esconder mejor una fórmula. No puedo garantizar margen en modelos de frontera sin probarlos.

## 6. Experimento mínimo, hasta 20 dólares

[Juicio] Compararía **C1+C8 contra D1**. Primero, sin API: cuatro mundos certificados por familia, con dos dificultades y dos semillas; comprobaría soluciones de referencia y rivales optimizados. Si eso requiere semanas, el piloto ya dejó de ser mínimo.

[Juicio] Después:

- **16 partidas:** cuatro mundos × dos familias × sin pista/con pista. Modelo fuerte fijo, condiciones iguales y sesiones independientes.
- **Cuatro sondas C8**, en momentos fijados antes de correr, sobre dos partidas C1. Misma pregunta y mismo presupuesto de respuesta; sin herramientas. Solo como control exploratorio del efecto de preguntar.
- **Tope contable:** hasta US$16 para partidas, US$2 para sondas y US$2 de reserva, usando tarifas reales y contando razonamiento facturable. Si el presupuesto no permite completar una partida, se marca *inconclusa*, no *fallida*.

[Juicio] Regla previa para elegir: continuar una familia solo si la pista permite resolver los cuatro casos, rescata al menos dos fallos sin pista y los rivales resuelven como máximo uno. Si ambas pasan, elegiría C1 por menor costo de desarrollo; D1 quedaría como siguiente prueba. Si ambas están en techo, no profundizaría automáticamente ninguna.

[Juicio] Eso decide **dónde invertir la próxima semana**, no cuál merece un artículo. Con cuatro mundos por familia también puede salir «no alcanza para decidir».

## 7. «De juguete» y riqueza del fenómeno

[Juicio] La objeción es válida **contra el alcance**, no contra usar mundos pequeños. Si arriba hay regla 30 y el agente solo descubre cómo adelantar el reloj, no descubrió una regularidad de la regla 30. La complejidad transportada no vuelve complejo el hallazgo evaluado.

[Juicio] Sí pueden combinar riqueza y respuesta exacta:

- Conocer un resumen exacto que reduzca a una simulación superior manejable: C1.
- Pedir una propiedad global sencilla aunque los detalles sean difíciles: conservación, separación de regiones o dinámica a escala gruesa.
- Pedir un objeto con certificado finito: D1, donde verificar un período establece persistencia indefinida.

[Juicio] No pueden exigir simultáneamente **regla arbitraria, observable arbitrario, futuro arbitrariamente lejano y verificación barata garantizada**. Algo debe restringirse. Tener más cómputo para construir las respuestas no es metodológicamente malo; es insuficiente para demostrar que el agente descubrió algo.

[Literatura — de memoria] Universalidad computacional no implica dificultad de toda predicción particular. Tampoco tomaría la irreducibilidad de la columna central de la regla 30 como un teorema establecido.

## 8. Si fuera Lucas mañana

[Juicio] Cambiaría la pregunta de portada por una que el instrumento pueda responder: **«¿Cuándo encuentra un agente una consecuencia útil de reglas nuevas, y qué lo destraba?»** Mantendría cerrados los renombres, corregiría «reglas visibles ⇒ solo puede faltar la idea» —también pueden fallar comprensión, implementación y presupuesto— y haría el piloto de C1 contra D1. No escribiría otra teoría antes. Si C1 sale completo, publicaría su alcance pequeño y lo cerraría; si aparece una separación reproducible entre mecanismos independientes y acoplados, investigaría esa separación. La aspiración a algo revolucionario no debe convertirse en otra condición que impida obtener el siguiente resultado.

---

# SEGUNDA VUELTA

[Dato] V2 todavía no está construida. Tomo las cifras y referencias recientes como informes del material; no las verifiqué independientemente.

## 1. Diagnóstico: dos correcciones

[Juicio] **“Construcción sistemática ⇒ desarmado eficiente por un modelo” es falso.** Si “sistemático” admite enumeración ilimitada, dice poco; si significa barato, no se sigue. Generar una instancia junto con una solución puede ser fácil aunque encontrar cualquier solución sea difícil. Lo de las sumas demuestra una debilidad de **ese generador**, no de todo fenómeno plantado.

[Juicio] **Adelante barato / inverso caro es una posibilidad, no una garantía.** Muestrear trayectorias puede producir objetivos con muchísimas soluciones fáciles. También puede producir problemas inversos difíciles sin ninguna organización útil que descubrir. AlphaGeometry no elimina esa segunda dificultad: hay que construir o encontrar una distribución donde sirvan representaciones reutilizables.

[Literatura — de memoria] La generación de problemas con testigo y la síntesis mediante restricciones explotan esa separación. AlphaGeometry usa construcciones auxiliares, pero eso no establece una ley general sobre dificultad de inversión.

[Juicio] Además, corregiría **“verificación trivial”**: correr verifica un testigo positivo. No verifica “imposible”. Eso requiere una prueba, una enumeración exhaustiva o un certificado de un solucionador, dentro de un dominio bien acotado.

## 2. “Hacé que pase”: objeción y ataque

[Juicio] **La objeción más fuerte:** todavía es un problema de búsqueda de una entrada, no necesariamente de descubrir partículas. Puede quedar entre dos extremos: lo resuelve un solucionador genérico, o cuesta muchísimo sin que conocer la “física” ayude.

### Cómo lo atacaría

[Juicio]

1. Buscaría atajos del enunciado: empezar con el objetivo, introducir directamente el producto, aprovechar bordes, periodicidad o casillas no observadas.
2. Codificaría toda la evolución hasta \(T\) como restricciones SAT/SMT: estado de cada casilla en cada instante, tabla local, límites iniciales y objetivo final.
3. Probaría búsqueda de preimágenes por columnas, aprovechando localidad; compararía con búsqueda evolutiva.
4. Enumeraría patrones pequeños, detectaría recurrencias trasladadas y construiría automáticamente un catálogo de partículas.
5. Buscaría sobre **objetos, posiciones y fases**, verificando cada plan con el simulador.

[Juicio] Esperaría que los pasos 1–3 barran bastantes instancias pequeñas. No sé si barrerían vuestra distribución. **Falta SAT/SMT entre los rivales obligatorios**: no lo sustituye una búsqueda hacia atrás artesanal.

[Literatura — de memoria] La verificación acotada mediante SAT, los métodos de preimágenes mediante grafos de de Bruijn y la búsqueda automática de naves en autómatas son antecedentes directos.

### ¿Existe la zona buscada?

[Juicio] Es plausible: muchos estados microscópicos, pocos objetos estables, choques composicionales y objetivos que requieran coordinar fases o introducir un catalizador. No basta con aumentar \(T\), el ruido o la cantidad de casillas.

[Juicio] La evidencia fuerte sería:

- una representación por objetos abarata **varios objetivos nuevos**;
- entregar esa representación a un planificador mecánico reproduce parte de la ventaja;
- una pista sobre el choque pertinente ayuda más que información comparable pero irrelevante;
- el ahorro persiste en reglas y tareas retenidas.

Eso muestra **utilidad de una representación física**, no éxito “sin cómputo”. Buscar por objetos ya es usar esa física.

[Juicio] Dos cambios indispensables:

- Quitar objetos uno a uno del testigo demuestra dependencia **de esa trayectoria**, no que cualquier solución necesite esos auxiliares. Llamalo “auxiliares del testigo de referencia”, no dificultad mínima.
- “Hasta \(m\) casillas no vacías” no acota sus posiciones. Fijá longitud, bordes, alfabeto inicial y observación final. Prohibí introducir directamente lo que se pretende fabricar.

## 3. Minados frente a plantados

[Juicio] **Plantados permiten la comparación causal más limpia; minados permiten la afirmación más limpia sobre ausencia de un mecanismo escrito por ustedes.** Son virtudes distintas.

- **Plantados:** controlás qué interacción existe y podés construir gemelos. Riesgos: marcas del generador, partículas demasiado reconocibles, choques incompletos y soluciones accidentales creadas al rellenar la tabla.
- **Minados:** evitan escribir la solución física. Riesgos: costo de encontrar mundos útiles, sesgo del detector y dificultad mal controlada. “Regla nueva” tampoco garantiza “fenómeno nunca estudiado”.

[Juicio] El filtro también diseña una distribución: **minado no significa libre de decisiones humanas**. Publicaría generador, filtros y tasas de descarte.

[Juicio] Para una investigación completa: plantados para aislar mecanismos, minados para comprobar que el resultado sale del generador. No exigiría ambos en el piloto.

## 4. “Experimento crucial”: ahora tiene una trivialidad

[Juicio] Si puedo elegir libremente la fila, **escribo el vecindario que distingue las tablas y obtengo una diferencia al primer paso**, siempre que los símbolos y el límite inicial lo permitan. Que ese vecindario sea raro en trayectorias sorteadas no lo vuelve difícil de provocar.

[Juicio] Para evitarlo necesitás restringir las condiciones iniciales: alfabeto de entrada, posiciones o formas permitidas. Entonces la tarea pasa a ser **alcanzar una transición bajo esas restricciones**. Si solo observás el instante \(T\), además hay que comprobar que la diferencia no desaparezca antes.

[Literatura — de memoria] Esto está muy cerca de matar mutantes en *mutation testing*, generar entradas que alcancen una rama y producir secuencias distinguidoras de máquinas de estados. No afirmaría novedad básica frente a esos antecedentes; tampoco frente a REFUTE sin revisar su tarea exacta.

[Juicio] **Con dos tablas conocidas aporta poco sobre “hacé que pase”.** Recupera una pregunta distinta si hay varios mecanismos candidatos y el artefacto es un protocolo —posiblemente adaptativo— que los identifica a todos. Ahí evaluás selección de información, no solo producción de un evento.

[Juicio] “Equivalentes” debe significar equivalentes **para las entradas, observaciones y horizonte permitidos**. No convertir un fracaso de búsqueda en equivalencia general.

## 5. Frente a las propuestas anteriores

[Juicio] **Prefiero v2 a C1 como línea principal, pero no la considero globalmente mejor que D1/D2 del adjunto B.**

- Frente a **D1, descubrir una partícula**, gana composición e intervención. Pierde una garantía elegante: el certificado periódico establece persistencia indefinida; alcanzar \(X\) en \(T\) solo establece ese evento.
- Frente a **D2, distinguir varios mecanismos**, la variante de dos tablas es peor: puede reducirse a activar una entrada visible.
- Frente a **“teoría en una botella”**, v2 es más sencilla de puntuar, pero una solución aislada demuestra menos reutilización.

[Juicio] Conservaría **partículas certificadas como base y “hacé que pase” como examen posterior**. Después pediría que el catálogo o planificador producido resuelva objetivos retenidos sin volver a consultar al modelo.

## 6. Piloto: primero comprobar que hay algo que evaluar

[Juicio — propuesta] No construiría todavía un generador sofisticado de choques plantados. Haría un intento de minado **con corte duro de un día**.

### Construcción

[Juicio — propuesta]

- Autómatas de **4 símbolos, radio 1**, con cero quiescente. Hasta 2.000 tablas; cada entrada restante produce cero con probabilidad 0,7 y reparte el resto entre los otros símbolos.
- Por regla: 128 semillas cortas, 64 pasos. Buscar recurrencias trasladadas de período hasta 8; certificarlas aparte con suficiente margen espacial.
- Retener como máximo dos reglas con dos partículas distintas y algún choque que produzca un objeto diferente. Si no aparecen, parar: falló este procedimiento de abastecimiento, no los modelos.
- Tareas en anillo de 128 casillas, \(T=64\), hasta 12 casillas inicialmente no vacías, solo en dos bandas laterales de 32. Objetivo central con guardas vacías.
- Generar objetivos mediante choques de dos o tres objetos, guardando testigos. Separar tareas de desarrollo y seis tareas finales, tres por regla. No llamar “mínimo” al número de objetos del testigo.

### Rivales y API

[Juicio — propuesta]

- Cartera congelada tras desarrollo: azar, evolutiva, SAT y búsqueda con catálogo automático de objetos.
- Presupuesto de herramientas: 60 segundos de un núcleo por partida. Medir también una curva de costo de los rivales; no solo éxito a un corte.
- Seis tareas × dos condiciones: **sin catálogo / con catálogo certificado**, sin dar posiciones ni el plan testigo. Sesiones independientes.
- Hasta US$1,25 por partida: US$15 y US$5 de reserva. Fijar límites de tokens usando las tarifas reales, incluido razonamiento facturable. Si no alcanza para partidas útiles, reducir el diseño **antes** de empezar.
- Registrar API, CPU y tiempo por separado. Igualar CPU de herramientas **no iguala el cómputo total** del agente.

### Reglas de lectura previas

[Juicio — propuesta]

1. **No filtrar los resultados finales por fallos del rival.** Informar los seis. Puede existir un subconjunto difícil definido en desarrollo, pero no esconder el denominador.
2. Continuar por ventaja del agente solo si resuelve al menos dos tareas adicionales frente a la cartera, repartidas entre ambas reglas.
3. Si el catálogo rescata al menos dos fallos, hay señal de un cuello de botella de representación. **Eso solo no demuestra que el agente descubra esa representación.**
4. Si un rival resuelve las seis dentro del presupuesto, cerrar esta configuración como examen de frontera.
5. Si todos fallan incluso con catálogo, no llamarlo profundidad: revisar accesibilidad, herramientas y dificultad.
6. No incluir negativos de “símbolo ausente de toda salida” como evidencia sustantiva: son controles de lectura. Permitir “no encontré”; no tratarlo como “imposible”.
7. Presupuesto agotado o fallo del arnés: resultado inconcluso, no incapacidad.

[Juicio] Son reglas para decidir otra semana de trabajo, no umbrales estadísticos de publicación. Estos rivales serían **los implementados**, no “el mejor buscador mecánico posible”.

## 7. Titular y nulo

[Juicio] Si hay ventaja reproducida y transferencia:

> **Representaciones de partículas mejoran la síntesis de condiciones iniciales en autómatas celulares nuevos.**

Si solo hay victorias puntuales:

> **Agentes con herramientas frente a búsqueda automática en problemas inversos de autómatas celulares.**

[Juicio] Nulo defendible:

> **En esta distribución, la búsqueda por restricciones iguala o supera a los agentes; los auxiliares del testigo no predicen una ventaja del modelo.**

Con suficientes reglas retenidas, código y curvas de costo, sería informativo. Seis tareas de un piloto no bastan.

[Juicio] **El cambio decisivo de v2 no es “invertir es difícil”. Es que permite entregar, reutilizar y poner a prueba una representación mediante artefactos exactos.** Haría de eso el centro; no de derrotar al buscador que alcanzamos a escribir.