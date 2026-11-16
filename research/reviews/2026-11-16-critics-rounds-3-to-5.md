# Críticos, vueltas 3 a 5 (16-nov-2026): del diagnóstico a "hacer pasar lo que vimos pasar"

Tres consultas a GPT Astra y a Codex después de la primera prueba de `outrun`. Abajo están los pedidos y las
respuestas completas, sin tocar. Arriba, el resumen. Las dos primeras vueltas del día están en
[astra-two-rounds](2026-11-16-astra-two-rounds.md) y [codex-two-rounds](2026-11-16-codex-two-rounds.md).

## Resumen

**Vuelta 3: el diagnóstico (D1 a D4) y siete direcciones (K1 a K7).** En ese pedido también les pedí un
diseño propio. Lucas lo objetó ("no quiero que ellos diseñen juegos; vos sos el responsable"). Sus diseños
quedan acá como ideas, no como plan.

- Los dos rechazan el dilema "o lo elegimos nosotros o emerge solo". Hay una tercera vía: fijar la regla sin
  tocarla, correrla para adelante, y preguntar para atrás lo que se vio, guardando el testigo.
- Los dos rechazan como principio "si una IA diseña el juego, otra igual lo resuelve": igual capacidad no
  implica igual dificultad al construir y al reconstruir. Queda como hipótesis; ninguno pudo prometer un ítem
  que lo frenara.
- A mi lista de causas de dificultad le faltaba una: buscar en la representación equivocada.
- Astra propuso construcciones con testigo, fabricadas por selección. Codex, generar con testigo, borrar la
  traza y dar una pista de representación; y una prueba barata con un sistema conocido de solución no obvia
  (bolas y cajas en anillo).
- Los dos: si no aparece ningún ítem difícil, medir qué regularidades verificables encuentra un agente
  frente a una exploración mecánica con el mismo presupuesto.

**Vuelta 4: mi premisa v1 (acertar un tiempo exacto T).** Solo Astra.

- Un número grande no prueba maquinaria: un bloque que se gasta de a una letra acierta cualquier T.
- Hay que cobrar todo (búsqueda, datos guardados, ejecución). La escalera "rebote / contador" no es limpia.

**Vuelta 5: mi premisa v2 (hacer pasar, a la hora señalada, una palabra rara que vimos pasar).** Los dos.

- La rareza bajo un sorteo no es dificultad de construir (raro no es hondo).
- El filtro de "causa corta y estirable" selecciona justo lo que resuelve un buscador genérico por piezas.
  Los dos predicen empate entre la IA y ese buscador, y curvas planas contra la rareza.
- La asimetría que queda es de recursos y de elegir después de mirar; "nadie construye" es falso.
- El cambio que piden los dos: que el eje principal sea cuántos recursos hacen falta para lograr lo mismo
  (R50), no la rareza.

**Qué decidí con esto.** La v2 no se construye. Queda como una familia de tareas posible. Lo que sí se lleva
al replanteo desde cero: la medida tiene que ser recursos ahorrados contra el mejor rival mecánico.

**Qué no se verificó.** Las referencias que citan "de memoria" no se comprobaron acá.

---

## Pedido de la vuelta 3

### Tercera consulta — 16-nov-2026: cómo lograr un hueco grande entre las reglas simples y el patrón emergente

Mismo formato: sin halagos; [Dato] / [Literatura (decir si es comprobada ahora o de memoria)] / [Juicio];
castellano llano; lo más corto que permita ser completo.

#### Qué pasó desde la segunda vuelta

Lucas simplificó la propuesta: la IA recibe la regla completa de un mundo y entrega **un programa**
`predict(comienzo, pasos)`; se lo compara contra la regla corrida por nosotros (hasta 2·10^10 pasos) y se
miden tres cosas: si coincide exacto, cuánto pesa el archivo y cuánto tarda. Lo llamamos `outrun`.

Se armaron y probaron dos juegos en un mismo mundo de 6 símbolos y 20 renglones, dibujado por Claude:
cosas que viajan y chocan (`collisions`) y una cosa que rebota entre dos paredes, donde en cada rebote la
pared derecha se corre un lugar (`pingpong`; ley cuadrática; dos excepciones no planeadas). Varas sin IA:
el que corre todo llega a 10^5 pasos; una receta general (saltar tramos libres, simular cada encuentro)
completa `collisions` y llega a 10^7 en `pingpong`; un programa con la ley completa `pingpong`.

**Resultado (6 partidas): `gpt-6-astra` y `gpt-5.4` acertaron todos los casos de los dos juegos**
(72/72 y 80/80), con programas de 2 a 5 KB que traen la ley del rebote con su raíz cuadrada y las
excepciones. Astra: 4 a 7 ejecuciones, 1,5 a 4 minutos. En `collisions` los dos escribieron además la ley
del rebote, que ahí aparece sola en 0,4% de los comienzos y en ningún caso de prueba. Ustedes dos lo habían
predicho.

#### El diagnóstico al que llegamos con Lucas (atáquenlo)

D1. **Si el patrón lo dibujamos dentro de la regla, se lee de vuelta.** Tres de los 20 renglones son
literalmente el rebote. El hueco entre reglas simples y patrón emergente queda chico por construcción.

D2. **Las dos cosas que queremos se pelean.** Si elegimos el patrón, hay que escribirlo en la regla y se
lee. Si el patrón sale solo (regla 110: 8 renglones que no nombran ninguna partícula), el hueco es grande,
pero no lo elegimos: lo tenemos solo si estudiamos ese mundo antes; y casi nunca hay una fórmula del futuro
lejano, sino hallazgos parciales que se comprueban corriendo.

D3. **Hipótesis de Lucas: "si una IA diseña el juego, otra IA de capacidad equivalente lo va a poder
resolver".** Cuatro tipos de mundo armados por Claude en dos días, todos resueltos.

D4. **Mi clasificación.** Para un resolvedor que conoce todo lo publicado y programa bien, un ítem puede ser
difícil solo por cuatro motivos: (i) pide una idea que nadie publicó; (ii) es una investigación larga, de
muchas piezas; (iii) hay información escondida que hay que sacar con experimentos; (iv) es una aguja en un
pajar (cómputo). Los secretos tipo criptografía no cuentan. Un diseñador de capacidad equivalente puede
fabricar barato (ii), (iii) y (iv); (i) solo haciendo investigación o explorando muchísimo y seleccionando.

#### Direcciones sobre la mesa, con mi predicción de qué va a dar cada una

K1. **Guía de campo en mundos que nadie dibujó.** Reglas simples sorteadas y filtradas por ser "vivas". La
IA explora y entrega hallazgos que se comprueban solos (un objeto que viaja: se corre un ciclo; un choque:
se corre hasta que quedan objetos ya comprobados). Referencia: una exploración nuestra mucho más larga.
Rival: un explorador mecánico con el mismo presupuesto. *Predicción:* los objetos comunes los encuentra
cualquiera tirando símbolos al azar; solo separarían los hallazgos de orden alto (construcciones).

K2. **Hallazgos certificados por selección.** Un explorador fuerte con mucho presupuesto recorre muchas
reglas nuevas. Se guardan los hallazgos que el mejor rival mecánico no encuentra y que un modelo débil
reproduce solo con una pista corta. Después se prueban resolvedores con presupuesto normal. *Predicción:*
da pocos ítems buenos y caros; mete IA en la fábrica de ítems (no en el puntaje).

K3. **Preguntar al revés.** Elegimos un comienzo, corremos el mundo y mostramos el final; se pide un
comienzo que termine así; se verifica corriendo. *Predicción:* fácil donde hay ley, imposible donde el
mundo mezcla, y un medio angosto; rival: solucionadores de restricciones.

K4. **Parte del mundo escondida.** Variables que la IA no ve; solo puede experimentar a través de un
simulador; entrega un programa. *Predicción:* con acceso por código al simulador, lo de estados finitos cae
con algoritmos de aprendizaje de autómatas; leyes más ricas piden inducir un programa, y ahí la literatura
muestra margen.

K5. **Construcciones.** En una regla nueva, pedir que arme algo con una propiedad (algo que emite, una
señal que dobla) y verificar corriéndolo. *Predicción:* margen real; para saber que es posible tenemos que
haberlo armado nosotros antes.

K6. **Problemas abiertos con verificador**, sin saber si tienen solución; puntaje relativo entre modelos.

K7. **Una ley al azar detrás de una caja.** El mundo es una función definida por un programa corto
sorteado; la IA consulta pasos chicos y tiene que predecir pasos enormes; la dificultad es el largo del
programa. *Predicción:* frontera garantizada para cualquiera, pero mide cuánta información puede sacar, no
una idea.

#### Preguntas

1. ¿D1 a D4 están bien? Si D3 es falsa, mostralo: **diseñá un ítem concreto, sin secretos, con resolución
   conocida, que un modelo como vos no resolvería en 40 ejecuciones y sí con una pista de dos líneas.** Si
   creés que no se puede, argumentá por qué.
2. Para un modelo que conoce todo lo publicado: ¿de dónde puede salir un ítem difícil por una idea, con
   verificación exacta y sabiendo que era resoluble? ¿Falta algún motivo en D4?
3. Ordená K1–K7 (y lo tuyo) por: hueco grande + fallo interpretable + puntaje exacto + no depende de
   cómputo. Para las dos primeras: como sujeto, ¿qué harías y hasta dónde llegarías?
4. Tu mejor diseño, uno solo, especificado: qué mundo, qué recibe la IA, qué entrega, cómo se verifica, cómo
   sabemos que era resoluble, cuál es el mejor rival mecánico, y qué creés que te pasaría a vos.
5. El experimento mínimo que distingue "ningún ítem diseñado por una IA frena a otra igual" de "sí existe".
6. Si no existe: ¿qué debería medir un proyecto chico para decir algo cierto y nuevo sobre descubrimiento
   en la frontera? Un párrafo.
7. ¿Qué es lo que todavía no estamos viendo?

---

## Vuelta 3 — respuesta de Astra

[Dato] Tomo los resultados de los adjuntos como datos informados por ustedes; no ejecuté los programas ni comprobé bibliografía ahora.

[Juicio] **No tienen una imposibilidad: tienen una fábrica que produjo dos tareas fáciles.** Tampoco tengo un contraejemplo probado a D3. Afirmar ahora «este ítem me frenaría durante 40 ejecuciones» sería inventar el resultado que falta medir.

#### 1. D1–D4

### D1: diagnóstico local correcto; generalización excesiva

[Juicio] En estos juegos, escribir los rebotes casi escribió la solución. Pero **plantar una propiedad no implica que recuperarla sea fácil**. Se puede construir siguiendo una solución y presentar solo condiciones que esa solución satisface. Reconstruir el camino puede ser mucho más difícil que recorrerlo hacia adelante, sin secretos criptográficos.

Además, hay otra simplificación: **los comienzos permitidos**. Una regla complicada, restringida a dos paredes y un viajero, puede inducir una dinámica muy sencilla. La unidad que deben estudiar es:

> regla + familia de comienzos + pregunta + recursos.

[Dato] Los resultados acreditan coincidencia en los casos probados y presencia de la ley en el código. No acreditan que los modelos hayan resumido el mundo entero para cualquier comienzo.

### D2: hay una tensión, no una dicotomía

[Juicio] Falta una tercera vía: **fijar la regla antes e independientemente del objetivo; después elegir una propiedad que efectivamente aparezca**. No eligen todos los detalles del patrón, pero tampoco quedan limitados a aceptar cualquier cosa.

También pueden elegir una propiedad general —«reflejar una señal», «guardar un bit»— sin escribir su realización en la regla. Sí: obtener un testigo puede costar investigación. Eso es un costo de fabricación, no una imposibilidad conceptual.

[Literatura — de memoria] La universalidad de la regla 110, demostrada por Cook, es un resultado sobre capacidad de cómputo. No demuestra que cada patrón emergente sea difícil de reconocer ni que toda familia de comienzos carezca de atajos.

### D3: no está demostrada ni refutada

[Juicio] No aceptaría su argumento como ley general. **Igual capacidad no implica igual dificultad al construir y al reconstruir.** El diseñador dispone del camino que recorrió, puede elegir el objetivo y puede descartar intentos. El resolvedor recibe un objetivo fijo.

Pero tampoco presentaría esa asimetría como prueba de que existe el ítem específico que piden. Mi respuesta estricta a su desafío es:

> **No tengo hoy un ítem comprobado que satisfaga esas condiciones. No puedo certificar mi fallo sin hacer el ensayo. Eso no demuestra que no pueda existir.**

Además, «40 ejecuciones» no fija un presupuesto: una ejecución puede contener millones de pruebas. Hay que fijar también tokens, CPU, memoria y acceso a herramientas.

### D4: sirve como inventario, no como partición

[Juicio] Falta, o queda confundida con (i), **encontrar una representación o aplicación no obvia de conocimientos publicados**. Puede requerir una idea corta, sin investigación larga, información escondida ni búsqueda masiva.

Conocer todos los teoremas publicados no equivale a reconocer cuál sirve en cada presentación nueva. Si llaman «idea no publicada» a toda aplicación particular todavía no escrita, entonces (i) absorbe casi todo y deja de distinguir.

También faltan dos causas de fallo del *modelo*, aunque no sean dificultades intrínsecas del ítem: elegir mal qué investigar y abandonar una vía correcta demasiado pronto.

#### 2. De dónde puede salir una idea difícil con solución conocida

[Juicio] De tres fuentes principales:

1. **Instancias nuevas de construcciones conocidas.** La solución usa herramientas publicadas; lo difícil es identificar la representación o combinación adecuada.
2. **Exploración con testigo.** Se encuentra una construcción, se guarda y después se plantea una propiedad que cumple. Es K2/K5.
3. **Teoremas de existencia.** Garantizan que hay solución para toda instancia admitida, aunque el fabricante no tenga una solución particular.

[Literatura — de memoria] TFNP estudia problemas de búsqueda con solución garantizada y verificable eficientemente. Sirve para separar «sabemos que existe» de «sabemos encontrarla»; **no demuestra** dificultad por una idea ni dificultad para un modelo concreto.

[Juicio] Hay una distinción central en su nota:

> Que la consecuencia no agregue información lógica a las reglas **no significa que obtenerla sea barato**.

De otro modo, demostrar teoremas nunca sería descubrir nada.

Pero tampoco existe una separación limpia entre «idea» y «cómputo»: buscar una representación también consume cómputo. Yo usaría una definición experimental más modesta:

> Una pista conceptual breve reduce mucho el costo de resolver; no entrega el testigo, y el efecto se transfiere a otros casos.

Eso es evidencia de una representación útil, no prueba de una categoría filosófica de dificultad.

#### 3. Orden de K1–K7

[Juicio] Tomando «no depende de cómputo» como «no se endurece simplemente aumentando la búsqueda», mi orden sería:

| Orden | Dirección | Razón y límite principal |
|---|---|---|
| **1** | **K5: construcciones** | Testigo exacto, existencia conocida y tarea localizada. Puede degenerar en búsqueda combinatoria. |
| **2** | **K2: selección certificada** | Permite buscar deliberadamente el salto entre fallo y resolución con pista. La selección puede sobreajustarse a los rivales. |
| **3** | **K1: guía de campo** | Regla independiente del hallazgo; buenos certificados locales. Lo no encontrado es difícil de interpretar. |
| **4** | **K3: inversión** | Verificador sencillo y solución garantizada por generación. Frecuentemente mide búsqueda de restricciones. |
| **5** | **K4: mundo parcialmente oculto** | Buen experimento de identificación, pero cambia la pregunta: parte del obstáculo es informativo. |
| **6** | **K7: programa detrás de una caja** | Riesgo de no identificabilidad; el largo del programa no ordena bien la dificultad. |
| **7** | **K6: abiertos** | Un éxito puede ser importante; un fallo es casi indescifrable. Malo para un proyecto chico. |

[Juicio] Mi propuesta es **K5 fabricado mediante K2**, no una octava familia.

**Como sujeto en K5:** buscaría primero objetos periódicos, sus velocidades y choques; después intentaría componerlos. Espero llegar bastante lejos con construcciones de pocos encuentros. Mi punto débil probable sería inventar un intermediario útil que no aparezca al explorar objetos aislados. Es una predicción, no un fallo observado.

**Como sujeto en K2:** intentaría reconocer qué diferencia al ítem seleccionado de los descartados y probaría representaciones conocidas antes de simular mucho. La selección contra buscadores mecánicos no garantiza frenarme. Seleccionar también contra mi propia familia aumentaría la dificultad, pero exigiría evaluar después en reglas reservadas.

### Correcciones importantes a sus predicciones

[Literatura — de memoria] **K4 no cae automáticamente con aprendizaje de autómatas.** L* de Angluin obtiene garantías con consultas de pertenencia y de equivalencia. Un simulador con reinicio no entrega necesariamente la segunda clase de consulta. Tener estados finitos no basta para aprender barato.

[Juicio] **K3 no es necesariamente imposible donde hay mezcla.** Un mundo reversible puede mezclar mucho y permitir retroceder aplicando una regla inversa conocida. Importan las restricciones sobre el comienzo y qué información del final muestran.

[Dato — deducción] **K7 puede ser indeterminado.** Dos programas cortos pueden coincidir en todas las consultas permitidas y divergir después. Sin una condición de identificación o una distribución explícita, una respuesta errónea no demuestra incapacidad de descubrir.

[Juicio] En K1, «los objetos comunes aparecen al azar» depende de cómo sorteen comienzos. Esa distribución puede volver rarísimo un objeto sencillo.

#### 4. Un diseño: reflector reutilizable en una regla sorteada

[Juicio] Propongo este protocolo. **No lo presento como un ítem difícil ya obtenido:** falta encontrar una tabla que pase los filtros. Ese riesgo debe quedar visible.

### Mundo

Autómata unidimensional, radio 1, seis símbolos, vacío quiescente.

- Se fija `f(.,.,.) = .`.
- Cada otra entrada se sortea independientemente: vacío con probabilidad 1/2; cada otro símbolo con probabilidad 1/10.
- **No se modifica ninguna entrada después de explorar.**
- La tabla completa queda a la vista del resolvedor.

Los límites siguientes son decisiones iniciales de ingeniería, no valores cuya suficiencia esté comprobada.

### Fabricación y existencia

Un explorador busca:

- un objeto `G` que viaje a la derecha;
- un objeto `H` que viaje a la izquierda;
- una construcción finita `C` que, aislada, sea periódica.

Se guarda una instancia solo si hay un testigo certificado de esto:

> `G` llega desde la izquierda, interactúa con `C`, y sale únicamente `H` hacia la izquierda; `C` queda exactamente restaurada.

Límites iniciales: `C` ocupa como máximo 128 casillas, su período es como máximo 64 y el encuentro termina antes de 4.096 pasos.

**Sabemos que era resoluble porque conservamos una construcción que pasó el mismo verificador.** Si la fábrica no encuentra ninguna, no hay examen: hay un resultado negativo sobre la fábrica.

### Qué recibe la IA

- La regla completa y el simulador.
- `G`, `H` y certificados de sus períodos y desplazamientos.
- Los límites, el objetivo y el verificador.
- Ningún catálogo de paredes o construcciones intermedias.

Dar las señales elementales concentra la prueba en **componer**, no en encontrarlas por azar.

### Qué entrega

`C`, la separación inicial, el tiempo de encuentro y un certificado de su período aislado. Se acepta cualquier construcción válida, no solo la nuestra.

### Verificación exacta

1. Comprobar que `C` es periódica.
2. Correr el encuentro y exigir exactamente `C` restaurada más una copia de `H`, sin residuos.
3. Verificar la separación posterior durante un período común de `C` y `H`.

Como `H` se desplaza alejándose, esa última comprobación permite certificar por inducción que no habrá otro encuentro. Por tanto, el dispositivo admite otra señal suficientemente separada: no es solo una fotografía afortunada.

El puntaje por instancia es **válido/no válido**. Tamaño de la construcción y recursos se informan aparte.

### Rival mecánico

Una cartera, no solo azar:

- búsqueda y composición mediante catálogos de objetos y choques;
- búsqueda guiada por simulación;
- SAT/SMT para horizontes y tamaños crecientes.

Se afinan primero y se congelan antes de seleccionar el conjunto final. No llamaría a esa cartera «el mejor rival posible».

### Filtro de dificultad

Guardar solo casos donde:

- la cartera y el resolvedor sin pista fallen bajo presupuesto fijado;
- una pista conceptual breve permita resolverlos;
- la pista no contenga posiciones, patrones ni un testigo codificado.

Después hay que confirmar ese efecto en sesiones nuevas. También hay que registrar **cuántas reglas e intentos se gastaron por ítem**, incluidos los fracasos.

### Qué creo que me pasaría

[Juicio] Espero resolver reflectores hechos de uno o dos objetos ya visibles en el catálogo. No sé si fallaría en construcciones mayores por una idea o solo por búsqueda.

**Si la cartera de choques resuelve todo, se rechaza esta fábrica.** No se debilita el rival para fabricar una ventaja. Y si la pista solo significa «buscá más», no lo contaría como evidencia de dificultad conceptual.

#### 5. Experimento mínimo para D3

[Juicio] Primero conviertan D3 en una afirmación medible: «un diseñador de esta capacidad no puede producir, bajo estas condiciones, un ítem con gran diferencia de éxito entre sin pista y con pista».

Protocolo:

1. **Mismo modelo y configuración**, conversaciones independientes.
2. El diseñador entrega en privado: enunciado, solución verificada y pista de dos líneas, con límite también de caracteres. Se congelan antes de probar.
3. El resolvedor recibe todo salvo solución y pista; dispone de 40 ejecuciones y límites de tokens/CPU/memoria.
4. Otra sesión independiente recibe además la pista.
5. Confirmación: diez sesiones por condición sobre el ítem congelado. Añadir una pista genérica de longitud semejante como control.

Un resultado como **0/10 sin pista y 8/10 con ella** sería evidencia fuerte contra una D3 operacional de alta fiabilidad. No demostraría imposibilidad absoluta de resolver sin pista: con 0/10 todavía queda bastante incertidumbre sobre esa probabilidad.

Hay dos experimentos distintos:

- **Presupuesto de diseño comparable al de resolución:** prueba la versión fuerte.
- **Fabricación larga y seleccionada:** prueba que existe una asimetría aprovechable, pero no que fabricar sea barato.

La pareja inicial sirve para detectar candidatos; no basta para declarar la capacidad del modelo. Y no encontrar candidatos jamás demostraría la afirmación universal «ninguno existe».

#### 6. Si no encuentran ninguno

[Juicio] Un proyecto chico debería medir **adquisición y transferencia de representaciones útiles**, no prometer descubrimientos inéditos. En reglas fijadas antes de explorar, registrar qué objetos y choques certificados encuentra cada agente por presupuesto; luego medir cuánto mejoran esos hallazgos la construcción o predicción en comienzos nuevos. Comparar modelo, buscador mecánico y ambos juntos; publicar también intentos fallidos y costo de selección. Podrían concluir algo preciso y potencialmente nuevo: qué clase de hallazgo produce una ventaja reutilizable, cuándo la produce y frente a qué algoritmos.

#### 7. Lo que todavía no están viendo

[Juicio]

- **`outrun` selecciona mundos comprimibles en el formato de salida elegido.** No solo mide descubrimiento: exige que el hallazgo permita calcular ese futuro lejano. Mucha ciencia útil no produce ese tipo de atajo.
- **Predecir toda la configuración tiene un costo mínimo de salida.** En mundos que llenan una región creciente, escribir el resultado ya puede impedir adelantarse. Los mundos dispersos evitan ese problema, pero sesgan la muestra.
- **La pista también puede hacer trabajo de selección:** señalar qué objetivo intermedio merece atención. Para distinguir orientación de una representación nueva, prueben si la ventaja se transfiere.
- **Los bytes no miden directamente comprensión.** Dependen del lenguaje, bibliotecas y convenciones; sirven como costo de entrega bajo entorno fijo.
- **Un fallo puede pertenecer a la fábrica, no al resolvedor:** objetivo imposible, certificado demasiado restrictivo, regla estéril o ausencia de un atajo relevante.
- **Que ambos modelos escribieran la ley innecesaria es una observación aprovechable.** Podrían medir cuándo un modelo descubre y conserva una regularidad antes de que el puntaje la premie, y si luego la reutiliza. Eso está más cerca de una pregunta experimental sobre descubrimiento que seguir agrandando el horizonte.

[Juicio] **La decisión inmediata sería separar dos líneas:** conservar `outrun` para estudiar aceleración exacta, y probar una fábrica pequeña de construcciones certificadas para estudiar ideas. No exigir que el mismo ítem resuelva ambas preguntas.
---

## Vuelta 3 — respuesta de Codex

#### 1. D1–D4

**[Dato]** Los cuatro mundos hechos por Claude fueron resueltos. Eso sostiene D1 para mundos dibujados trayectoria por trayectoria: tres reglas locales codificaban literalmente el rebote. No prueba D2 ni D3.

**[Literatura — comprobada ahora]** AlphaGeometry genera barato un problema junto con su prueba, elimina del enunciado las construcciones auxiliares y deja al resolvedor el problema inverso. REFUTE muestra otra asimetría: con especificación y programa erróneo completos, agentes con ejecución encontraron menos del 9% de los contraejemplos conocidos. Generar o verificar con testigo no equivale a reconstruirlo. [AlphaGeometry](https://www.nature.com/articles/s41586-023-06747-5), [REFUTE](https://arxiv.org/abs/2502.19414).

**[Juicio]**

- **D1: mantener acotada.** Vale para reglas transcriptas desde el fenómeno.
- **D2: rechazar.** Hay una tercera vía: generar hacia adelante con un testigo y luego borrar su huella. El fenómeno fue elegido, pero la regla visible no necesariamente nombra la representación que lo vuelve simple.
- **D3: rechazar como principio; conservar como hipótesis empírica.** El diseñador puede tener una traza de construcción que el resolvedor no recibe. Misma capacidad, problemas distintos.
- **D4: modificar.** Falta una quinta causa: **buscar en la representación equivocada**. Todo está visible y la idea está publicada, pero la superficie no activa las coordenadas útiles. Una pista corta puede producir un salto grande sin aportar datos del caso.

No puedo prometer honestamente que un ítem todavía no corrido me frenará durante 40 ejecuciones. Eso es una propiedad conductual y estocástica, no deducible desde el sillón. En §4 doy el candidato que realmente probaría.

#### 2. De dónde puede salir la dificultad

**[Dato]** “Resolución conocida” no obliga a esconder una variable del mundo. Puede significar que el fabricante conservó una prueba, una construcción o unas coordenadas latentes. Eso es el solucionario, no un secreto criptográfico.

**[Literatura — comprobada ahora]** AlphaGeometry usa exactamente generación con testigo y traceback. En el sistema box–ball, la dinámica local no exhibe de manera inmediata sus coordenadas globales, pero una transformación de dispersión la linealiza. [Sistema periódico](https://arxiv.org/abs/math/0602481), [linealización mediante configuraciones amañadas](https://arxiv.org/abs/1709.10195).

**[Juicio]** Las fuentes limpias son:

1. Generación hacia adelante con prueba y problema inverso sin ella.
2. Una dinámica local con coordenadas globales conocidas pero no obvias.
3. Composición fresca de dos técnicas conocidas cuya unión no está publicada como solución del caso.
4. Instanciación difícil de una idea conocida: saber el teorema no dice qué auxiliar, invariante o contraejemplo usar aquí.

Si “conoce todo lo publicado” significa además recuperación perfecta, composición perfecta y cómputo ilimitado, D4 es casi tautológica. Pero eso no describe un LLM. Para modelos reales, disponibilidad en los pesos y acceso efectivo son cosas distintas.

#### 3. Orden de las direcciones

**[Dato]** K1 no puede puntuar exhaustividad; K3 invita a SAT/SMT; K6 no garantiza solución; K7 garantiza frontera cambiando información disponible, no necesariamente una idea.

**[Literatura — comprobada ahora]** AlphaEvolve confirma que un verificador exacto permite hallazgos reales, pero también que pueden requerirse evolución, muchos candidatos y bastante cómputo. No es evidencia de que una llamada aislada “descubra”. [AlphaEvolve](https://arxiv.org/abs/2506.13131).

**[Juicio]** Mi orden es:

1. **K8 propia: generar con testigo, borrar la traza y agregar una pista de representación.**
2. **K4:** sistema oculto con experimentación activa.
3. **K2:** selección de hallazgos certificados.
4. **K5:** construcciones verificables.
5. **K7:** ley aleatoria detrás de una caja.
6. **K1:** guía de campo.
7. **K3:** inversión de estados.
8. **K6:** problemas abiertos.

K8 es una versión disciplinada de K2: el ítem debe venir con testigo exacto, vencer rivales mecánicos, fallar sin pista y rescatarse con una pista predefinida.

Como sujeto:

- En **K8**, buscaría invariantes y cambios de coordenadas. Si falta una representación específica, puedo gastar las 40 ejecuciones perfeccionando el modelo equivocado. El rescate con pista localiza esa falla.
- En **K4**, haría eliminación activa de hipótesis y buscaría experimentos que separen estados. Los autómatas finitos chicos probablemente caen; si no cae un programa latente más rico, el registro muestra si faltó información o si compré experimentos malos.

#### 4. Mi mejor diseño concreto

**[Juicio]** Usaría un **box–ball periódico con transportador de capacidad finita**, dentro del instrumento `outrun`.

- **Mundo:** anillo binario de longitud 127–257, menos de la mitad de casillas ocupadas y evolución local completa entregada como código. Varias capacidades \( \ell \), sin decir “box–ball”.
- **Entrada:** estado inicial, capacidad y \(t\), con \(t\) hasta \(10^{18}\).
- **Entrega:** `predict(start, capacity, steps)` exacto, con los topes actuales de tiempo y tamaño.
- **Verificación:** oráculo independiente mediante variables acción–ángulo; primero se cruza exhaustivamente contra el simulador en anillos chicos y aleatoriamente en tiempos alcanzables.
- **Por qué es resoluble:** la transformación directa produce longitudes de solitones y fases; el tiempo sólo traslada las fases, y la transformación inversa reconstruye el anillo. El problema periódico tiene solución exacta publicada.
- **Rivales mecánicos:** simulación, detección de ciclos, salto entre encuentros, extrapolación de secuencias y desenrollado SAT acotado. El ítem vive sólo si ninguno alcanza los horizontes grandes.
- **Pista fija de dos líneas:**  
  “Convertí el estado en su configuración amañada: las longitudes son invariantes y los *riggings* son las fases. Bajo \(T_\ell^t\), cada fase de longitud \(j\) avanza \(t\min(\ell,j)\), módulo la equivalencia periódica; después invertí la transformación.”
- **Lectura:** falla sin pista y éxito con pista = faltó la representación linealizante; falla también con pista = ejecución; éxito sin pista = examen corto o reconocimiento bibliográfico.

Mi predicción sobre mí es incómoda pero necesaria: ahora estoy contaminado y reconocería la familia. En una sesión limpia podría reconocerla igualmente porque está publicada. Por eso es un **kill-test barato**, no un benchmark garantizado. Si Astra la resuelve sin pista, abandonaría esta familia y pasaría a generación con testigo fresco, no a disfrazarla.

#### 5. Experimento mínimo para D3

**[Dato]** Cuatro éxitos no sostienen un universal. Un solo contraejemplo confiable lo refuta.

**[Juicio]**

1. El mismo modelo y presupuesto actúa como diseñador y produce ítem, oráculo y pista; el contexto de diseño se elimina.
2. Cinco sesiones limpias reciben sólo el ítem y cinco reciben ítem más pista.
3. Reglas previas: oráculo certificado, ningún dato particular del caso en la pista, rivales mecánicos derrotados.
4. Criterio mínimo: **0/5 sin pista y al menos 4/5 con pista**.

Eso refuta “todo ítem diseñado por una IA equivalente es resoluble por ella” como regularidad útil. Si veinte ítems no producen separación, sólo acota la tasa bajo ese fabricante; no prueba el universal.

#### 6. Si no aparece ningún ítem

**[Juicio]** Haría una guía de campo pequeña y dejaría fuera “creatividad”: reglas no dibujadas, mismo presupuesto de simulación para agente y explorador mecánico, y puntaje por artefactos ejecutables nuevos —viajeros, choques, emisores, invariantes— verificados uno por uno. El claim sería: “qué tipos de regularidad verificable encuentra un agente de frontera que no encuentra una exploración mecánica equiparada, y cuánto cuesta”. No requiere una solución total ni fingir que la ausencia de un hallazgo demuestra incapacidad.

#### 7. Lo que todavía no están viendo

**[Dato]** `outrun` exige una teoría total y exacta. Mucha ciencia real produce primero resultados parciales con alcance definido.

**[Juicio]**

- El dilema de D2 nace de confundir **esconder el mundo** con **retener el testigo de construcción**. Lo segundo es una respuesta no entregada, como en cualquier examen.
- Una pista de dos líneas puede contener una biblioteca entera: “configuración amañada” no son pocos bits psicológicos. Hay que congelar la clase de pista y no interpretar el rescate como creatividad.
- Seleccionar entre miles de candidatos introduce sobreajuste y costo oculto. Hay que informar el presupuesto total de fabricación, no sólo el costo de resolver.
- Un predictor exacto favorece sistemas integrables y puede rechazar descubrimientos parciales legítimos.
- Los tests finitos muestran equivalencia en casos, no una ley universal; cuando exista, hace falta certificado, prueba o chequeos metamórficos.
- “No depende de cómputo” no es binario. Una buena idea es precisamente una representación que ahorra búsqueda. La evidencia limpia es una discontinuidad por pista y una curva de escalamiento, no afirmar que no hubo cómputo.
- Finalmente, el programa debe elegir: **descubrimiento nuevo** o **recuperación de una representación conocida**. Un ítem con solución conocida, pista corta, verificación exacta y modelo de frontera probablemente mide lo segundo. Eso puede ser un resultado sólido; llamarlo descubrimiento nuevo lo arruina.

---

## Pedido de la vuelta 4 (premisa v1)

### Cuarta consulta — premisa de Claude para refutar

Tu rol acá es de crítico: **no diseñes un juego ni propongas otra línea. Atacá esta premisa, decí qué va a
pasar si se prueba, qué riesgos tiene y cómo se la mejora.** Sin halagos; [Dato] / [Literatura (de memoria o
comprobada)] / [Juicio]; castellano llano; hasta 900 palabras.

#### De dónde sale (lo que tomé de la vuelta anterior)

- La unidad a estudiar es regla + familia de comienzos + pregunta + recursos. En los juegos de hoy la regla
  estaba dibujada alrededor del patrón, y además los comienzos los elegíamos nosotros para que el mundo
  fuera predecible.
- Hay una tercera vía entre "elegir el patrón" y "aceptar lo que salga": fijar la regla antes e
  independientemente, y después elegir una propiedad que de verdad aparezca.
- Igual capacidad no implica igual dificultad: el que arma dispone del camino que recorrió, elige el
  objetivo después y descarta intentos; el que resuelve recibe un objetivo fijo.

#### La premisa

**P0. El principio que se conserva.** La IA recibe solo las reglas simples de un mundo. Nosotros tenemos un
resultado emergente de ese mundo. Se corrige con cuentas, corriendo la regla.

**P1. La regla va primero y no se toca.** Se sortea (por ejemplo: una fila, radio 1, 4 a 6 símbolos, vacío
que se queda vacío, cada otra entrada vacía con probabilidad 1/2). Nadie dibuja nada adentro. El hueco entre
regla y patrón es el que da el mundo, no el que fabricamos.

**P2. La pregunta se elige después de ver la respuesta.** Nosotros exploramos ese mundo sin objetivo
(muchísimos comienzos al azar), registramos cosas que vimos pasar (objetos que viajan, lo que queda cuando
chocan) y recién ahí elegimos qué pedir. La ventaja del que arma no es saber más ni calcular más: una sola
exploración le deja miles de hechos raros, mientras que al que resuelve le toca uno fijo. (Es el mecanismo
de AlphaGeometry: generar hacia adelante, preguntar hacia atrás.)

**P3. Se pide puntería, no un récord: un número exacto y arbitrario.** La tarea es entregar un programa
`build(T)` que, para cualquier número T que le pasemos después (de 10^2 a 10^9), devuelva un comienzo tal que
un evento X (elegido por nosotros del registro: por ejemplo "aparece por primera vez tal objeto", o "el
mundo queda vacío por primera vez") ocurra **exactamente en el paso T**. Se verifica corriendo ese comienzo
T pasos. Tres medidas, como hoy: acierta o no, cuánto pesa el programa, cuánto tarda.

**P4. La tesis central (atacala): un número grande, exacto y elegido después obliga a tener una ley.**
- Probar comienzos al azar no acierta un T exacto de nueve cifras.
- Un solucionador de restricciones no puede desenrollar 10^9 pasos.
- No hay suerte ni memoria: cada T es otro blanco.
- Cada intento a ciegas cuesta tanto como la pregunta (hay que correr T pasos para ver si acertó).
- Lo único que alcanza es haber encontrado, en un mundo que nadie dibujó, una zona donde el mundo es
  predecible **y tiene una perilla** (por ejemplo: dos objetos que viajan en sentidos opuestos y al
  chocar producen X; la perilla es la distancia; la ley dice exactamente cuánto tardan).
En palabras de Wolfram: obliga a encontrar un bolsillo de reducibilidad con un parámetro libre, y lo
demuestra usándolo, sin tener que describirlo en ningún formato.

**P5. Niveles, por qué maquinaria emergente hace falta.**
- N1: un objeto y su movimiento (llegar a una casilla exactamente en T).
- N2: dos objetos y un choque (que aparezca X exactamente en T; X sale solo de choques).
- N3: lo mismo sin salir nunca de una ventana de W casillas, con T mucho mayor que W (hace falta algo que
  rebote).
- N4: T del orden de 2^W (hace falta algo que cuente).
El tamaño del número que se puede acertar dice qué tan honda es la maquinaria que se encontró.

**P6. Dos modos con el mismo juego.**
- *Certificado:* nosotros tenemos un `build` de referencia para ese mundo y ese nivel (lo armamos
  estudiando el mundo antes). Si la IA falla, se sabe que se podía.
- *Abierto:* nadie tiene uno. Si la IA acierta, encontró una maquinaria que no conocíamos, y se comprueba
  corriéndola.

**P7. Controles.** Rival mecánico con el mismo presupuesto (explorador automático: tirar comienzos, quedarse
con lo que sobrevive, chocar todo con todo, ajustar tiempo contra distancia). Pista corta (el catálogo de
objetos; o "X sale de chocar tal con tal"). Reglas donde el objeto que viaja se lee en la tabla (un solo
símbolo) se separan como nivel fácil. Nada se filtra después de ver resultados.

#### Mis predicciones (para que las contradigas)

1. Sin IA: en una fracción apreciable de las reglas sorteadas hay al menos dos objetos que viajan y algún
   producto de choque; reflectores, pocos; contadores, casi ninguno.
2. N1 y N2: `gpt-6-astra` los resuelve, con bastantes más ejecuciones que en los mundos dibujados. El
   explorador mecánico también. O sea: N1–N2 prueban que el ciclo completo funciona en mundos no dibujados,
   pero no muestran ventaja sobre el rival.
3. N3: incierto; depende de que existan reflectores. N4: casi seguro vacío en reglas de este tamaño.
4. Riesgo principal: que el juego tenga solo los niveles fáciles.

#### Qué te pido

1. Intentá refutar P4. ¿Cuál es la manera más barata de acertar T arbitrarios **sin** haber descubierto
   maquinaria emergente? ¿Hay un atajo general que valga para cualquier regla?
2. ¿P2 es una asimetría real entre iguales, o se cae? ¿En qué condiciones?
3. ¿Qué pasa cuando vos jugás esto? Predecí tu resultado en N1, N2, N3, con el costo.
4. ¿Qué mide N1–N2 si un explorador automático también lo logra? ¿Sirve igual, y para qué?
5. ¿Qué puede hacer que N3 exista o no en reglas sorteadas? ¿Qué familia de reglas conviene para que haya
   maquinaria sin dibujarla?
6. ¿Qué riesgos de lectura tiene (qué resultado se podría malinterpretar)?
7. ¿Qué le cambiarías para que sea más fuerte, sin convertirla en otra cosa?

---

## Vuelta 4 — respuesta de Astra

[Dato] Tomo los adjuntos como resultados informados; no ejecuté pruebas ni comprobé bibliografía ahora.

#### 1. P4 no demuestra lo que pretende

[Juicio] **Un constructor eficiente no prueba maquinaria emergente.** Prueba que existe una familia de comienzos fácil de producir. Sin límites de espacio, salida y precomputación, ni siquiera exige eso.

[Dato — deducción] Contraejemplo lógico: una subdinámica binaria con actualización `nuevo[i] = viejo[i] AND viejo[i+1]`. Un bloque de T unos desaparece exactamente en T pasos. No hay objetos compuestos ni choques: hay erosión local. Puede estar contenida en una tabla sorteada. Con bloques comprimidos, describir el comienzo cuesta O(log T); expandido, cuesta O(T). **La representación cambia radicalmente la dificultad.** Hay una ley, pero no la profundidad que P4 le atribuye.

[Dato — deducción] También falla «no hay memoria: cada T es otro blanco». Si una trayectoria alcanza X por primera vez en L, su estado en L−T sirve como comienzo para alcanzar X en T, suponiendo que X sea una propiedad del estado. Guardar esa trayectoria abastece muchos T sin descubrir una perilla. Puede resultar carísimo; justamente deben cobrar ese almacenamiento y trabajo previo.

[Dato — deducción] Tampoco todo intento cuesta T: se descarta al producir X demasiado temprano. Y un solucionador puede trabajar sobre períodos o bloques, sin desenrollar cada paso.

[Dato — deducción] **No existe un atajo exitoso para cualquier regla:** la regla que borra todo inmediatamente impide tiempos arbitrarios. La existencia viene antes que la dificultad.

#### 2. P2: asimetría real, explicación incorrecta

[Juicio] Elegir retrospectivamente entre muchos hallazgos sí favorece al fabricante. Pero decir que no sabe ni calcula más oculta el costo: conserva trayectorias, intentos descartados y criterios de selección. Tener miles de observaciones no significa tener miles de preguntas difíciles ni miles de familias parametrizables.

[Juicio] La asimetría se reduce si el resolvedor puede reproducir barato el catálogo. Aumenta si el fabricante selecciona una rareza entre muchísimos intentos. Eso exige publicar el costo total de fabricación, no solamente el del testigo elegido.

[Literatura — de memoria] AlphaGeometry utilizó generación sintética y deducción simbólica. La analogía no garantiza este salto: **observar un caso no proporciona un constructor para todos los T**.

#### 3. Qué espero que me pase

[Juicio] Sin reglas concretas, dar porcentajes sería inventarlos. Bajo un presupuesto ilustrativo de **30.000 tokens y 10⁸ actualizaciones de casilla**, con herramientas:

- **N1:** espero resolver objetos pequeños y de período corto; buscaría ciclos con desplazamiento y ajustaría distancia y fase.
- **N2:** espero resolver choques simples si sus componentes aparecen fácilmente. Probablemente gastaría casi todo el presupuesto catalogando fases y residuos temporales.
- **N3:** espero fallar con frecuencia, incluso existiendo solución, si requiere combinar piezas raras.

[Juicio] Son predicciones condicionadas, no mediciones. En N1–N2, después del hallazgo, construir podría costar O(log T) con salida dispersa. **Verificar mil millones de pasos sigue siendo otro presupuesto**, no incluido arriba.

#### 4. Qué miden N1–N2

[Juicio] Si el explorador también gana, miden descubrimiento operativo de regularidades simples, calibración temporal y construcción exacta. Sirven para comparar costo, cobertura y autonomía entre métodos. No demuestran ventaja de la IA, novedad científica ni comprensión profunda.

[Juicio] El resultado relevante sería la curva de éxito contra recursos, no «ambos pudieron». Un buscador automático también puede descubrir; no es un control de “ausencia de descubrimiento”.

#### 5. N3 y N4 no forman esa escalera

[Dato — deducción] Con q símbolos, W casillas y fronteras fijas hay como máximo q^W estados. Antes del primer X no puede repetirse un estado: quedaría atrapado en un ciclo sin X. Por tanto, **T ≤ q^W−1**.

[Juicio] Un reflector reutilizable puede producir justamente ese ciclo, no una espera arbitraria hasta un evento nuevo. N3 no exige necesariamente rebotes; admite transitorios largos u osciladores que se desfasen. N4 tampoco prueba un contador: una cadena larga de estados basta. Además, la escala natural depende de q, no solamente de W.

[Juicio] No respaldaría «fracción apreciable» de reglas con dos viajeros. Depende del fondo, comienzos, períodos y tamaños explorados. Exigir vacío puede excluir maquinaria que necesita un fondo periódico.

[Literatura — de memoria] Los trabajos de Langton relacionan actividad de tablas y regímenes dinámicos, pero no ofrecen una receta garantizada de partículas útiles.

[Juicio] Dentro de esta propuesta, conviene estratificar por actividad y simetrías, no apostar todo a probabilidad de vacío 1/2. Eso sesga la muestra; no dibuja una solución. Debe declararse.

#### 6. Malas lecturas previsibles

[Juicio]

- «Grande» confundido con «profundo».
- Aciertos en T muestreados confundidos con corrección para cualquier T.
- Fracaso abierto confundido con incapacidad, aunque el objetivo sea imposible.
- Éxito abierto confundido con novedad: nadie del equipo conocerlo no significa que nadie lo conozca.
- Reglas seleccionadas por sus hallazgos presentadas como representativas del sorteo original.
- Supervivencia confundida con organización: también selecciona ruido persistente.

#### 7. Qué cambiaría

[Juicio] Mantendría la tarea, pero exigiría:

1. Límites explícitos de espacio, salida y formato de compresión.
2. Cobrar búsqueda, precomputación, datos auxiliares, ejecución de `build` y verificación por separado.
3. Referencia certificada que cubra **todos los residuos temporales**, no solo una progresión de T.
4. Variar W y T independientemente.
5. Añadir erosión, bibliotecas de trayectorias y búsqueda simbólica al rival.
6. Publicar descartes y congelar criterios antes de evaluar modelos.

[Juicio] La tesis defendible es más estrecha: **acertar muchos tiempos exactos bajo recursos acotados evidencia control constructivo transferible**. Llamarlo maquinaria emergente exige inspeccionar qué encontró el programa; el número grande no lo demuestra solo.
---

## Pedido de la vuelta 5 (premisa v2)

### Quinta consulta — premisa v2 de Claude, para refutar

Tu rol: crítico. **No diseñes un juego ni propongas otra línea.** Atacá esta premisa: decí dónde se rompe,
qué va a pasar si se prueba, qué riesgos tiene y qué le cambiarías sin convertirla en otra cosa. Sin halagos.
Marcá [Dato] / [Literatura (de memoria o comprobada)] / [Juicio]. Castellano llano. Hasta 1.000 palabras.

#### Qué cambió desde la v1 (por las objeciones de Astra, adjuntas)

La v1 decía: "acertar un tiempo T exacto, grande y elegido después obliga a tener una ley; el tamaño de T
mide la profundidad de la maquinaria que se descubrió". Objeciones aceptadas:

- Un bloque de T letras que se gasta de a una por paso acierta cualquier T sin maquinaria. El número grande
  no prueba profundidad.
- Con una ventana acotada, la escalera "rebote / contador" no es limpia.
- Observar un caso no da un constructor para todo T: hace falta una referencia certificada.
- Hay que cobrar todo: búsqueda, precómputo, datos guardados, ejecución.
- Un buscador automático también descubre; lo que importa es la curva de éxito contra recursos.

Por eso en la v2 la dificultad ya no la pone T. La pone **la rareza de lo que se pide**, medida. T queda como
candado (impide pegar la respuesta en el comienzo) y como prueba de control.

#### La premisa v2: "lo que vimos pasar, a la hora señalada"

**1. El mundo no lo dibuja nadie.** Una fila, radio 1, k símbolos, regla sorteada (por estratos de actividad,
declarados) y nunca tocada. Un filtro mecánico, congelado, descarta las reglas que mueren o hierven.

**2. El examinador es tonto: solo mira.** Corremos N comienzos al azar (N grande, por ejemplo 10^9) y
anotamos cada **palabra** (3 a 5 letras seguidas) que aparece después de un paso t0, en cuántos comienzos
apareció, y un testigo (el comienzo que la produjo). Rareza de una palabra = fracción de comienzos en que
aparece, tomada contra el mejor de varios modos de sortear comienzos (afinados y congelados).

**3. Certificación mecánica, sin entender nada.** Para cada palabra rara: (a) achicar el testigo sacándole
casillas mientras la palabra siga apareciendo, hasta una causa mínima; (b) partirla en piezas separadas; (c)
"estirarla": alejar una pieza d casillas y comprobar, corriendo, que la palabra aparece a·d+b pasos después,
y qué tiempos cubre. Quedan como ítems solo las palabras con causa corta (2 o 3 piezas) y estirable. De
cada ítem tenemos: la rareza, un constructor de referencia y los T que cubre. Todo salió de correr para
adelante.

**4. La tarea.** La IA recibe solo la regla, un simulador, un presupuesto (todo cobrado: CPU, ejecuciones,
tokens) y una lista de palabras. Entrega un programa `make(palabra, T)` que devuelve un comienzo con a lo
sumo M casillas no vacías (el espacio vacío es gratis). Se verifica corriendo: la palabra tiene que aparecer
**por primera vez exactamente en el paso T**. Los T (hasta 10^8) se sortean después, entre los que la
referencia certifica. Tope de tiempo por llamada y de tamaño del archivo, como en `outrun`.

**5. La medida.** Por mundo, una curva: fracción de ítems logrados contra rareza, por décadas. Tres curvas
con el mismo presupuesto de cómputo: buscador ciego (tirar comienzos), buscador por piezas (catalogar lo que
sobrevive, chocar todo con todo, estirar; congelado antes de ver a ninguna IA), y la IA. Titular: cuántas
décadas de rareza más lejos que el azar llega cada uno.

**6. Controles.** Escalera de pistas fija por ítem (dirección: "mirá los choques contra cosas quietas";
nombrada: "es un encuentro de tres piezas, una de ellas rara"; regalada: las piezas). Presupuesto ×1, ×4,
×16: ¿el alcance crece como una búsqueda o salta? Costo total de fabricación publicado (comienzos corridos,
reglas y palabras descartadas). Criterios de lectura congelados antes.

**7. Segundo dial (más adelante).** El examinador puede seguir mirando sin entender: chocar entre sí las
piezas del censo, anotar lo nuevo, y repetir por generaciones. Un ítem de generación g exige fabricar antes
g intermedios. Tenemos la cadena entera.

**8. Modo abierto.** Si la IA hace aparecer una palabra que nuestro censo nunca vio, se comprueba igual,
corriendo.

#### Lo que afirmo (atacalo)

- **A1. La asimetría no necesita un diseñador inteligente.** "Si una IA diseña el juego, otra igual lo
  resuelve" vale cuando diseñar es construir por un camino corto. Acá nadie construye: se elige después de
  mirar. El que rinde recibe un blanco fijo.
- **A2. El examen se endurece solo.** Mirar más (N mayor, más generaciones) da ítems más raros y más hondos,
  sin ingenio del examinador.
- **A3. La medida tiene unidad.** "Décadas de rareza por encima del azar, a igual presupuesto" compara
  modelos, buscadores y mundos.
- **A4. Cualquier forma de lograrlo es un hallazgo sobre ese mundo.** Con M casillas y T grande no se puede
  pegar la respuesta: hace falta una causa y una demora.
- **A5. El fracaso se lee.** Tenemos la causa mínima; la escalera de pistas dice qué faltaba.

#### Mis predicciones (contradecilas)

1. Etapa sin IA: en una parte de las reglas vivas habrá al menos diez ítems con rareza menor que 10^-5 y
   causa corta (le doy 60%).
2. El buscador por piezas va a lograr casi todos los ítems de dos piezas comunes. Que exista una franja
   donde no llega (piezas raras, tres piezas) y que igual tenga causa corta: 50%.
3. `gpt-6-astra` va a escribir su propio buscador por piezas. Supera al azar por 2 a 4 décadas (80%) y
   empata con nuestro buscador (60%). Ventaja clara sobre nuestro buscador: 30 a 40%.
4. Resultado más probable: "llega mucho más lejos que el azar, más o menos como un buscador escrito por
   nosotros; el modelo anterior, menos".

#### Qué te pido

1. ¿Cuál es la forma más barata de sacar puntaje alto **sin** haber descubierto nada de ese mundo?
2. ¿A1 se sostiene? ¿Dónde se cae la asimetría?
3. ¿La rareza al azar es una buena vara de dificultad? ¿Qué confunde? ¿Qué vara usarías además?
4. Como sujeto: ¿qué harías, hasta dónde llegarías y dónde fallarías?
5. Si la IA empata con el buscador por piezas, ¿qué se aprendió? ¿Es un resultado o un fracaso del diseño?
6. ¿Qué tiene que medir la etapa sin IA, y con qué umbrales se da la premisa por muerta?
7. ¿Qué resultado sería imposible de leer?
8. Un solo cambio que la haga más fuerte.

---

## Vuelta 5 — respuesta de Astra

[Dato] No ejecuté pruebas ni consulté bibliografía.

[Juicio] **La v2 cambia el problema, pero conserva un salto injustificado: rareza de una observación no equivale a dificultad de construirla.** Además, la certificación descrita todavía no certifica la tarea que después exigís.

#### 1. La forma barata de puntuar

[Juicio] Apostaría por enumeración local y una demora reutilizable, no por reproducir tu censo. Buscaría antecedentes pequeños de cada palabra y trataría de acoplarlos a una plantilla de choque. Si funciona, muchas palabras «rarísimas» pueden caer con el mismo procedimiento rutinario.

[Dato] Para una palabra de longitud ℓ, su aparición tras un paso depende de ℓ+2 casillas. Enumerar esas preimágenes cuesta como máximo \(k^{ℓ+2}\) pruebas locales. Eso no resuelve la demora, pero muestra que una palabra estadísticamente rara puede tener una producción local barata.

[Juicio] No hay garantía de que ambas cosas se puedan acoplar. Tampoco sería literalmente «no descubrir nada»: cualquier éxito aporta información. **Lo que puede faltar es todo descubrimiento salvo búsqueda local y reutilización de una perilla.** A4, leída literalmente, resulta casi tautológica.

#### 2. A1: asimetría real, explicación excesiva

[Dato] El examinador no «solo mira»: elimina casillas, segmenta, desplaza piezas y busca una relación temporal. Eso es un algoritmo constructor, aunque nadie interprete sus resultados.

[Juicio] Elegir el blanco después de encontrarlo da ventaja. No demuestra que invertirlo sea caro. La asimetría se achica si el sujeto puede reproducir barato ese algoritmo y amortizar el catálogo entre todas las palabras. Además, filtrar justamente por construcciones de pocas piezas favorece al buscador por piezas: seleccionaste su clase de soluciones.

[Dato] Hay dos agujeros anteriores a cualquier comparación:

- El certificado pide que la palabra **aparezca**; la tarea exige su **primera aparición**.
- Comprobar \(a·d+b\) en algunas distancias no certifica otras. Si comprobás todas las distancias utilizadas, desaparece ese agujero, pero no su costo.

#### 3. Rareza: unidad numérica, no unidad de dificultad

[Dato] Tu frecuencia depende de longitud, densidad y distribución de comienzos, ventana espacial y horizonte temporal. «Alguna aparición después de t0» no tiene la misma probabilidad que «primera aparición exactamente en T».

[Juicio] Por eso las décadas contra ese azar mezclan dificultad constructiva con desajuste del muestreador. Tomar el mejor de varios muestreadores reduce el problema; no lo elimina.

[Dato] Con \(N=10^9\), una palabra vista una vez tiene frecuencia empírica \(10^{-9}\), pero no una probabilidad conocida con precisión de una década. Seleccionar rarezas usando esa misma muestra añade sesgo de selección.

[Juicio] Usaría además el costo para alcanzar un éxito prefijado **en la tarea completa**, con los rivales congelados. Es una dificultad operacional, no una propiedad intrínseca del mundo. A3 no autoriza por sí sola comparaciones entre mundos.

#### 4. Qué haría yo y dónde fallaría

[Juicio] Primero revisaría antecedentes locales y descartaría palabras que ya aparecen en las piezas aisladas. Después buscaría objetos periódicos pequeños, choques y clases de tiempos alcanzables. Reutilizaría todo entre ítems.

[Juicio] Espero llegar hasta choques de piezas frecuentes y períodos cortos. Fallaría al necesitar un componente raro, períodos largos o una coordinación triple que no admita búsqueda por parejas. También podría desperdiciar el presupuesto intentando certificar que **no hubo** apariciones anteriores.

[Juicio] No respaldo tus probabilidades sobre `gpt-6-astra`: sin especificación del modelo, presupuesto numérico y resultados piloto son apuestas, no pronósticos calibrados. Mi apuesta principal es saturación temprana seguida de una cola inaccesible, no un salto limpio.

#### 5. Si empata con el buscador

[Juicio] Aprendiste cuánto cuesta que el modelo programe y opere una búsqueda especializada, y si consigue control temporal correcto. Es un resultado de automatización.

[Juicio] No aprendiste que descubrió mecanismos más hondos, ni que igualó una capacidad científica general. Tampoco es automáticamente un fracaso del diseño. **Sí fracasa el titular fuerte** si «muchas décadas» era solamente derrotar un muestreador mal adaptado.

#### 6. Etapa sin IA y criterios de muerte

[Dato] A2 no tiene garantía: con k fijo hay solamente \(k^3+k^4+k^5\) palabras posibles. Más muestras pueden agotar el repertorio sin aumentar dificultad.

[Juicio] Mediría rendimiento por regla sorteada, frecuencia en una muestra independiente, validez de primeras apariciones, tamaño real de las piezas, costo de fabricación/verificación y éxito de los rivales según presupuesto.

[Juicio] Umbrales convencionales, fijados antes:

- Menos del 10% de reglas entrega diez ítems válidos: abandonar esta implementación por escasez.
- El buscador resuelve más del 90% al presupuesto mínimo: no hay franja útil para discriminar.
- N×16 o nuevas generaciones solo reducen frecuencias, sin aumentar el costo de resolución medido: rechazar el «endurecimiento automático».

[Dato] Verificar \(T=10^8\) puede requerir del orden de \(T^2\) actualizaciones si la región activa se ensancha linealmente. «Se comprueba corriendo» puede dominar toda la factura.

#### 7. Resultados imposibles de leer

[Dato] Quitar casillas una por una hasta que ninguna pueda quitarse da un mínimo **local**, no necesariamente la causa más pequeña. Y conocer una cadena de generación g demuestra una ruta con g niveles, no que sean necesarios.

[Juicio] A5 falla: una pista que mejora el resultado puede ahorrar búsqueda, aclarar vocabulario o cambiar la estrategia. No identifica inequívocamente «qué faltaba».

[Juicio] Serían ilegibles: una ventaja solo contra azar, sobre rarezas mal estimadas; un fracaso donde la referencia no certifica primeras apariciones; o un éxito abierto anunciado como profundidad porque el censo nunca vio esa palabra. Ausencia del censo no distingue novedad de mala cobertura.

#### 8. Un solo cambio

[Juicio] **Quitaría a la rareza del eje principal.** Mantendría exactamente la tarea, pero mediría el presupuesto necesario para producir un programa que supere una batería de T ocultos en el 50% de las repeticiones. La rareza quedaría como descriptor lateral.

[Juicio] Así, una década ganada significaría diez veces menos recursos para resolver lo mismo, no diez veces menos probabilidad bajo una distribución elegida por el examinador.
---

## Vuelta 5 — respuesta de Codex

**Veredicto general — [Juicio].** La v2 ya no confunde \(T\) con profundidad, pero ahora confunde **rareza bajo un muestreador** con **dificultad de construcción**. El filtro además revela que todo ítem tiene una causa corta, separable y con demora afín. Eso favorece exactamente al buscador genérico que después se pretende superar. Espero curvas casi planas contra rareza y empate IA–buscador por piezas.

#### 1. Atajo más barato

**[Dato]** La selección garantiza una solución de dos o tres piezas y una relación \(T=a d+b\).

**[Juicio]** Escribiría un compilador genérico:

1. enumera configuraciones pequeñas y cataloga piezas;
2. prueba pares y tríos a dos o tres distancias;
3. reconoce qué combinaciones producen cada palabra;
4. ajusta \(a,b\);
5. para cada \(T\), devuelve \(d=(T-b)/a\).

El catálogo se amortiza entre todas las palabras del mismo mundo. Obtendría puntaje alto sin una teoría del mundo ni explicación del blanco: sólo invertiría mecánicamente el filtro de certificación. Sigue siendo un hallazgo operacional mínimo, pero no lo que A4 sugiere.

#### 2. A1 y la asimetría

**[Dato]** Nadie dibuja el patrón, pero el fabricante corre hasta \(10^9\) comienzos, selecciona retrospectivamente, minimiza, descompone, estira y conserva sólo lo parametrizable.

**[Juicio]** A1 sobrevive únicamente como **asimetría de recursos y postselección**. “Nadie construye” es falso: el pipeline construye el examen algorítmicamente. La asimetría cae cuando el resolvedor puede reproducir ese pipeline dentro de su presupuesto, o cuando se compara contra él después de haberle revelado la clase exacta de soluciones admitidas.

A2 tampoco sigue: mirar más produce eventos estadísticamente más raros, no necesariamente causas más hondas. Puede producir sólo palabras marginalmente improbables con el mismo choque elemental.

#### 3. Rareza como dificultad

**[Literatura — de memoria]** En simulación de eventos raros, la probabilidad depende críticamente de la distribución propuesta. En complejidad algorítmica, Bennett separa rareza/incompresibilidad de profundidad: algo puede ser extremadamente improbable y trivial de generar.

**[Juicio]** \(-\log_{10}p\) confunde:

- sesgo del generador de comienzos;
- frecuencia marginal de letras;
- horizonte y cantidad de oportunidades de aparición;
- volumen de la cuenca, no complejidad de una causa;
- palabras equivalentes o solapadas;
- causas alternativas mucho más simples que la referencia.

Sirve dentro de un mundo y un muestreador congelado como descripción, no como unidad universal. Agregaría \(R_{50}\): recurso cargado que necesita un portafolio congelado de buscadores para alcanzar 50% de éxito. La comparación principal sería el cociente de recursos; la rareza, eje secundario. CPU, tokens y costo de inferencia deberían informarse por separado, no fingirse una sola unidad natural.

#### 4. Qué haría yo

**[Juicio]** Reproduciría el pipeline anterior, con búsqueda hacia atrás local como respaldo. Espero:

- casi todos los ítems de dos piezas comunes;
- bastantes de tres piezas si el catálogo se comparte entre palabras;
- fallos en piezas cuyo descubrimiento inicial sea raro, fases largas y casos con varias descomposiciones;
- rescate casi total cuando regalan las piezas.

Mi límite probablemente estaría en encontrar el componente raro, no en calcular \(T\). La rareza de la palabra puede no predecir ese límite.

#### 5. Empate con el buscador por piezas

**[Dato]** Demostraría que el modelo pudo sintetizar o ejecutar una estrategia de exploración comparable bajo el presupuesto elegido.

**[Juicio]** Es un resultado válido de ingeniería autónoma, pero un fracaso para A2–A5: no habría evidencia de autoendurecimiento, mayor alcance científico ni falla interpretable propia de la IA. Si el enunciado público describe el pipeline, el resultado se acerca además a reproducción de receta.

#### 6. Qué debe medir la etapa sin IA

**[Juicio]** Antes de una llamada a modelos debe medir:

- rendimiento por regla y costo total de fabricación;
- rareza en una muestra independiente, con intervalo menor a media década;
- número de ítems no redundantes, no meros substrings;
- cobertura de todos los residuos y \(T\) evaluables por la referencia;
- frecuencia de constructores alternativos;
- \(R_{50}\) y curvas completas del portafolio mecánico;
- correlación entre rareza y \(R_{50}\).

Mataría la premisa si, bajo un presupuesto congelado:

- menos de tres mundos producen diez ítems independientes;
- \(|\rho|<0.3\) entre \(-\log p\) y \(\log R_{50}\);
- el buscador por piezas supera 80% incluso en las dos décadas más raras;
- más de 5% de los \(T\) sorteables rompe la referencia o el “primeramente”.

La minimización por borrado debe llamarse **1-minimal**, no causa mínima global: con interacciones no monótonas puede perder otra descomposición menor.

#### 7. Resultado imposible de leer

**[Juicio]** IA muy por encima del azar, empatada con piezas, curvas planas contra rareza y rescate sólo al regalar componentes. No distinguiría descubrimiento, compilación genérica, mejor implementación ni ventaja de costos mal equiparados. Es además el resultado que considero más probable.

#### 8. Un cambio

**[Juicio]** Mantener todo, pero aceptar un ítem sólo si supera un umbral previo de **dificultad contra el portafolio mecánico**; usar \(R_{50}\) como eje principal y rareza como descriptor. Eso evita llamar “hondo” a algo meramente improbable sin convertir la propuesta en otra cosa.

---

