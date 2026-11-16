# Propuesta (16-nov-2026): que la IA entregue un programa que resuma el mundo, y compararlo con la realidad

**Estado: aprobada por Lucas para una primera prueba real con dos juegos.** Nombre de trabajo del juego:
`outrun` ("ganarle a la cuenta"). Reemplaza a la
[propuesta de la guía de campo](2026-11-16-field-guide-executable-catalog.md), que era lo mismo con más
piezas. La forma simple es de Lucas.

## 0. En cinco líneas

1. Ayer le pedíamos a la IA **una respuesta** sobre un futuro lejísimo. Para conocer nosotros esa respuesta
   hacía falta una fórmula, así que solo podíamos armar mundos con fórmulas conocidas, y el mejor modelo las
   encontró en un minuto.
2. Ahora le pedimos **un programa**: "poné cualquier comienzo y cualquier cantidad de pasos, y decí cómo
   queda el mundo".
3. Lo corregimos comparándolo **contra la realidad**: corremos la regla de verdad y miramos si coincide,
   letra por letra, en casos que la IA no vio.
4. Para que no haga trampa medimos además **cuánto pesa** el programa y **cuánto tarda**. Un resumen de
   verdad es chico y rápido a la vez.
5. El patrón del mundo lo creamos nosotros, así que sabemos que hay algo para descubrir y cuál es el mejor
   resumen posible.

## 1. De dónde venimos

Los juegos son siempre del mismo tipo, el de Wolfram: una fila de casillas, cada una con un símbolo, y una
regla que dice cómo cambia cada casilla mirando a sus dos vecinas. (A eso se le dice "autómata celular".)

En el juego anterior, `jump-ahead`, la pregunta era: "¿qué símbolo hay en estas seis casillas en el paso un
trillón?". Paso por paso no se llega, así que para contestar hay que encontrar una forma de saltar.

Eso tenía dos problemas, y los dos salieron a la luz en la [primera prueba](../../experiments/2026-11-16-mixing-ladder/reading.md):

- **Para corregir, nosotros teníamos que conocer la respuesta del paso un trillón.** Y solo la conocemos si
  debajo del mundo hay una fórmula. Entonces todos nuestros mundos tenían debajo una cuenta conocida (una
  suma), con los nombres cambiados. El mejor modelo la reconoció en uno o dos minutos.
- **Una respuesta no dice cómo se llegó.** "La casilla 12 tiene una B" puede salir de entender, de probar
  cosas o de suerte.

## 2. La idea

En vez de pedir una respuesta, pedir un **programa**. La consigna para la IA es:

> "Dame un programa donde yo pongo cualquier comienzo y cualquier cantidad de pasos, y sale cómo queda el
> mundo."

Ese programa, si es bueno, es un **resumen** del mundo: dice qué va a pasar sin hacer todos los pasos. Es
lo que Wolfram llama descubrir. En su charla de la cumbre de ARC (octubre de 2026): "can we jump ahead? Can
we figure out what's going to happen in a sort of reduced way?".

Y para corregirlo no hace falta saber nada de antemano: **se corre la regla de verdad y se compara**. La
regla siempre la podemos correr nosotros.

## 3. Un ejemplo completo, con un mundo de juguete

Este mundo lo armé y lo corrí el 16-nov para explicar la idea. No es uno de los juegos.

Tiene cinco símbolos (el punto es casilla vacía) y una regla de diez renglones, del tipo "si a mi izquierda
hay vacío, yo soy `a` y a mi derecha hay `b`, paso a vacío". Todo lo que la regla no nombra da vacío.

**Lo primero que se ve al correrlo: hay cosas que viajan.** Si pongo `a b`:

```
paso 0:  . a b . . . . .
paso 1:  . . b a . . . .
paso 2:  . . . a b . . .
paso 3:  . . . . b a . .
```

Ese par se corre un lugar a la derecha en cada paso. En la regla no dice "hay algo que viaja": se ve al
correrla. Hay otra cosa, una `c` sola, que viaja hacia la izquierda.

**Lo segundo: cuando dos cosas se encuentran, pasa algo.**

```
paso 0:  . a b . . . c . .
paso 1:  . . b a . c . . .
paso 2:  . . . a d . . . .
paso 3:  . . . . d . . . .
```

Chocaron y quedó una `d` quieta. Si arrancan una casilla más lejos, desaparecen las dos.

**Ahora el juego.** La pregunta es: "el par arranca en tal casilla, la `c` en tal otra; ¿cómo queda la fila
después de tantos pasos?". Armé mil casos al azar, corrí la regla de verdad en los mil, y comparé contra
tres programas:

```
programa que sabe...                                    acierta
1. que las cosas viajan                                   310 de 1.000
2. además: a distancia 3, 7, 11... queda una d            803 de 1.000
3. además: a distancia 5, 9, 13... queda una letra sola   994 de 1.000
```

Tres cosas para notar:

- **El puntaje es por grados.** Cada pieza del patrón que el programa incorpora sube el número.
- **La comparación encuentra lo que falta.** El programa 2 fallaba siempre a distancia 5, 9, 13... Fui a
  mirar y ahí no desaparecen: queda una letra sola que sigue viajando. Yo no lo sabía: ese mundo lo armé yo
  y esa cosa no la planté. Salió de la regla.
- **No hace falta un formato fijo para describir el patrón.** Adentro del programa puede ir cualquier cosa:
  una ley, una familia de casos, una fórmula. Lo único fijo es la prueba: predecir letras en casos nuevos.

## 4. Las dos trampas, y por qué hacen falta tres medidas

Si solo comparáramos contra la realidad, hay dos programas que aciertan sin haber descubierto nada.

**Trampa 1: correr todo.** Copiar la regla y aplicarla paso por paso. Es un programa cortito, pero tarda
cada vez más cuanto más lejos se le pregunta.

**Trampa 2: guardar las respuestas.** Como la IA puede usar todo el cómputo que quiera mientras investiga,
podría calcular muchos casos y pegar los resultados adentro del programa. Contesta al instante, pero pesa
muchísimo, y fuera de lo que guardó no sabe nada.

| Programa | Tamaño | Tiempo en un paso lejano | ¿Y en uno más lejano? |
|---|---|---|---|
| Corre todo | chico | lento | no llega |
| Respuestas guardadas | enorme | rápido | no lo tiene |
| La ley | chico | rápido | rápido |

Por eso se miden tres cosas, todas con cuentas:

1. **¿Coincide con la realidad?** Comparación exacta, en comienzos y pasos que la IA no vio.
2. **¿Cuánto pesa?** El tamaño del archivo, con un tope.
3. **¿Cuánto tarda, y cómo crece ese tiempo cuando se pregunta más lejos?** Si crece igual que la cantidad
   de pasos, está corriendo todo. Si casi no crece, tiene una ley.

En el mundo de juguete, dos programas que contestan lo mismo:

```
pasos      corre la regla    usa la ley     veces más barato
  1.000        0,008 s       0,000001 s           5.779
 10.000        0,085 s       0,000004 s          21.877
100.000        0,848 s       0,000004 s         195.641
```

Los dos aciertan. Cuanto más lejos se pregunta, más se separan.

**Para encontrar el programa, la IA puede usar el tiempo y el cómputo que quiera** (en la práctica el tope
lo pone la plata). Se anota cuánto gastó, pero lo que se puntúa es el programa que entrega.

## 5. Cómo se arma un juego

1. **Elegimos el patrón.** Qué cosas viven en el mundo y qué pasa cuando se encuentran. Por ejemplo: "hay
   una cosa que viaja a la derecha y una pared; cuando la cosa toca la pared, rebota y la pared se corre un
   lugar".
2. **Escribimos la regla que lo produce.** Se dibuja, fila por fila, lo que tiene que pasar; cada trío de
   vecinas que aparece en el dibujo fija un renglón de la regla. Todo lo que no se dibujó da vacío.
3. **Miramos qué hace de verdad.** Corriendo la regla aparecen cosas que no planeamos (como la letra sola
   del ejemplo). No importa: **la verdad es lo que hace la regla, no lo que quisimos hacer.**
4. **Definimos la familia de comienzos** (por ejemplo: "una cosa viajera y una pared, en cualquier lugar") y
   **las distancias** a las que se va a preguntar: diez pasos, cien, mil... hasta donde nosotros podemos
   correr la regla.
5. **Verificamos sin IA** que el juego tiene sentido, con programas nuestros:
   - uno que corre todo: tiene que acertar cerca y quedarse sin tiempo lejos;
   - uno con la ley: tiene que acertar todo, pesar poco y tardar poco. Ese prueba que el mejor resumen
     existe, y es la vara contra la que se compara a la IA.

## 6. Qué recibe la IA y qué entrega

Recibe: la regla completa; un simulador que la corre paso por paso (para que no pierda tiempo
reescribiéndola); cómo se sortean los comienzos; un programa para comparar su solución contra el simulador;
y las condiciones exactas de la prueba (a qué distancias, con qué tope de tamaño y de tiempo). No hay nada
escondido.

Entrega: un archivo con una función `predict(comienzo, pasos)`.

## 7. Qué números salen

Por cada distancia (10 pasos, 100, 1.000...), cuántos casos acierta dentro del tiempo. Con eso:

- **El horizonte:** hasta qué distancia acierta todo. Un programa que corre todo llega hasta ahí nomás; uno
  con la ley llega al final.
- **El tamaño** del archivo.
- **Cómo crece el tiempo.**

Lectura: si la IA llega más lejos que nuestro programa que corre todo, resumió algo. Si llega tan lejos como
nuestro programa con la ley, encontró el resumen entero. Lo del medio dice cuánto, y los casos que falla
dicen qué pieza le falta.

## 8. Límites y riesgos (sin vueltas)

- **Puede salir todo fácil.** En mundos con una ley sencilla, el mejor modelo probablemente la encuentra (es
  lo que mostró la primera prueba). Por eso el primer experimento tiene un juego simple y uno más complejo,
  y por eso el puntaje es por grados.
- **Hay recetas generales que resumen sin entender el mundo en particular.** Por ejemplo: "corré hasta que
  la fila se repita y después saltá de a vueltas enteras", o "saltá los tramos donde las cosas viajan solas
  y simulá solo los choques". Son resúmenes válidos, pero no descubren el patrón que plantamos. El juego
  complejo está armado para que esas recetas no alcancen (el mundo no se repite y los choques son cada vez
  más).
- **Solo comparamos hasta donde nosotros podemos correr la regla.** No hay "paso un trillón": la distancia
  máxima es la que una máquina normal alcanza en un minuto.
- **Acertar muchos casos no es una demostración.** Un programa puede acertar mil y fallar el mil uno.
- **El tiempo se mide en una máquina, con ruido.** Por eso las distancias van de a diez veces: lo que
  importa es el salto, no el milisegundo.
- **No mide si "se le ocurrió una idea".** Mide si convirtió lo que exploró en un resumen cierto, chico y
  rápido. Los dos críticos externos insistieron en no llamarlo más que eso.

## 9. En qué se parece a lo que ya existe

Buscado el 16-nov; solo resúmenes. Detalle en el
[registro de trabajo previo](../readings/2026-11-16-prior-work-three-searches.md), sección D.

| Trabajo | Qué hace | Diferencia |
|---|---|---|
| Test de Kolmogorov (Meta, ICLR 2025, [arXiv:2503.13992](https://arxiv.org/abs/2503.13992)) | La IA escribe el programa más corto que reproduce una tira de datos | Mide solo tamaño; no hay regla ni futuro |
| Zenil y otros 2011 ([arXiv:1104.3421](https://arxiv.org/abs/1104.3421)) | "Ganarle a la cuenta" en todas las máquinas de Turing chicas, con un buscador de fórmulas | Sin IAs |
| Cuaderno de Wolfram, "Limits of Language Model Computation" | Le da a un modelo la regla y le pide el paso N | El modelo contesta de cabeza, sin programa |
| DeepMind ([arXiv:2610.22603](https://arxiv.org/abs/2610.22603)) | Una IA encuentra resúmenes verificados de máquinas tipo Wolfram | Demostraciones formales; máquinas que nadie diseñó; 26 casos |
| Sucesiones de OEIS ([arXiv:2411.04372](https://arxiv.org/abs/2411.04372)) | Código correcto y eficiente "sin tablas" para sucesiones de números | No hay mundo ni regla |

No apareció el paquete junto: regla a la vista + programa entregado + comparación contra la regla corrida +
tamaño y tiempo. "No apareció" no es "no existe".

## 10. Qué pasó con las otras ideas del día

- **Guía de campo** (lista de afirmaciones + un planificador que la usa): era este mismo centro, más
  complicado. Los dos críticos habían señalado como lo más sólido que la IA entregue algo que se corre y se
  compara. Queda como registro.
- **Fenómenos que todavía no ocurrieron** ("relojes"): [nota guardada](../notes/2026-11-16-designed-programs-idea.md).
  El juego complejo de la primera prueba usa una idea de esa familia: un mundo cuyo futuro lejano sigue una
  ley que no se ve corriendo poco.
- **Críticas completas:** [Astra](../reviews/2026-11-16-astra-two-rounds.md) y
  [Codex](../reviews/2026-11-16-codex-two-rounds.md).

## 11. Primer paso

Dos juegos en el mismo mundo (una misma regla), con comienzos de distinta dificultad:

- **Simple:** cosas que viajan, chocan una o dos veces y se separan.
- **Más complejo:** una cosa atrapada entre dos paredes, que rebota; en cada rebote una pared se corre un
  lugar, así que cada vuelta tarda un poco más que la anterior. El futuro lejano sigue una ley que hay que
  encontrar.

Se verifican sin IA, se escriben las reglas de lectura, y se prueban con modelos reales midiendo el costo
en la primera partida. Todo queda en `games/outrun/` y en `experiments/`.

## 12. Lo que no se verificó

- Que los dos juegos se puedan armar como están descritos acá: al escribir esto todavía no están hechos.
- Que el mejor modelo no resuelva los dos enseguida.
- El trabajo previo: resúmenes, no textos completos.
- Los números del mundo de juguete son de corridas mías del 16-nov, hechas en una carpeta temporal; el
  mundo de juguete no está en el repo.
