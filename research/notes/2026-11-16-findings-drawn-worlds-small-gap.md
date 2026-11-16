# Hallazgos del 15 y 16 de noviembre: lo que aprendimos probando de verdad

Nota de trabajo. Junta lo que salió de dos días de pruebas con modelos y de la charla con Lucas. Cada
hallazgo dice con qué se apoya y qué límite tiene. Nada de esto es un resultado publicable todavía: son
pocas partidas, dos modelos y mundos chicos.

## Qué se probó

Dos formas de preguntar y cuatro tipos de mundo, todos armados por Claude:

| Experimento | Qué se le pide a la IA | Mundos | Resultado |
|---|---|---|---|
| [Escalera de mezcla](../../experiments/2026-11-16-mixing-ladder/reading.md) (29 partidas) | Una respuesta: qué hay en 6 casillas en el paso 10^18 | Una suma con los símbolos renombrados; lo mismo en dos capas; tablas al azar | `gpt-6-astra` resolvió todo lo que tenía estructura, en 25 a 112 segundos |
| [Primeros dos juegos de outrun](../../experiments/2026-11-16-outrun-first-two-games/reading.md) (6 partidas) | Un programa que prediga el mundo; se compara contra la regla corrida | Cosas que viajan y chocan; una cosa que rebota entre dos paredes | `gpt-6-astra` y `gpt-5.4` acertaron todos los casos |

## Los hallazgos

**1. Si el patrón lo dibujamos nosotros dentro de la regla, se lee de vuelta.**
Para tener un rebote, lo dibujé y anoté cada trío del dibujo como un renglón de la regla. Tres de los 20
renglones son, literalmente, el rebote: `(. b d) -> c`, `(b d .) -> e`, `(e . .) -> d`. Leer la regla es
leer el dibujo. El hueco entre las reglas simples y el patrón emergente queda chico por construcción.
*Apoyo:* las 6 partidas de outrun; los programas entregados traen la ley del rebote con su raíz cuadrada.
*Límite:* vale para mundos chicos dibujados así. No dice nada de mundos donde el patrón no se dibujó.

**2. Las dos cosas que queríamos se pelean** (formulación de Lucas, 16-nov).
- Si **elegimos nosotros** el patrón, hay que escribirlo en la regla, y entonces se lee. Hueco chico.
- Si el patrón **sale solo**, como en las reglas de Wolfram, el hueco es grande, pero no lo elegimos. La
  regla 110 son 8 renglones que no nombran ninguna partícula; las que aparecen al correrla llevó años
  catalogarlas.
En el segundo caso, nosotros tenemos el resultado solo si estudiamos ese mundo antes, con más tiempo que
la IA. Y casi nunca hay una fórmula del futuro lejano: hay hallazgos parciales (algo que viaja, qué pasa
cuando dos cosas chocan), que se comprueban corriendo.

**3. "Si una IA diseña el juego, otra IA de capacidad equivalente lo va a poder resolver"** (hipótesis de
Lucas, 16-nov).
*Apoyo:* cuatro tipos de mundo armados por Claude en dos días, todos resueltos por `gpt-6-astra`; dos de
ellos también por `gpt-5.4`. Los dos críticos lo habían predicho antes de correr. Claude no pudo proponer
un mundo con resolución conocida que creyera fuera del alcance de Astra por una razón de fondo.
*Estado:* apoyada, no probada. La refutaría un solo juego con resolución conocida que el mejor modelo no
resuelva y que sí resuelva cuando se le nombra la idea.
*Excepciones que no cuentan:* un secreto escondido (por ejemplo, un número cuyo producto se muestra y
cuyos factores no); ahí no hay idea que valga. Y el puro tamaño.

**4. Con todo a la vista no hay nada escondido.**
La IA recibe las reglas simples y nosotros guardamos la regla emergente. Pero la emergente es una
consecuencia de las simples: no es información aparte. Nosotros llegamos a ella por un camino (armar las
simples partiendo de ella) y la IA por otro (mirar qué hacen las simples). Cuando armar es transparente,
los dos caminos son igual de cortos.
*Dos ideas sin probar para que haya algo escondido de verdad:* esconder parte del mundo (la IA solo puede
experimentar) y preguntar al revés (elegir un comienzo, correr el mundo, mostrar el final y pedir el
comienzo; comprobar es correr, buscar es otra cosa).

**5. La forma de medir "programa contra realidad" funciona.**
La IA entrega un programa; se lo compara contra la regla corrida por nosotros; se miden tres cosas: si
coincide, cuánto pesa y cuánto tarda. Da puntaje por grados (un modelo chico sacó 16 de 72), separa "corre
todo" de "tiene la ley", no necesita que sepamos nada de antemano y cuesta entre 0,50 y 2,50 dólares por
partida. Queda como instrumento, sirva para el mundo que sirva.

**6. Hay recetas generales que resumen sin entender el mundo en particular.**
"Saltar los tramos en que nada se toca y hacer cada encuentro paso por paso" sacó puntaje completo en el
juego simple. "Correr hasta que la fila se repita" resuelve cualquier mundo chico que dé vueltas. Un puntaje
alto no prueba que se encontró el patrón que plantamos: hay que medir siempre contra esas recetas.

**7. Los mundos hacen cosas que nadie dibujó, y los modelos las encuentran.**
En el mundo de juguete apareció una letra sola que sigue viajando; en el de las paredes, dos comienzos en
los que una pared desaparece; y en el juego simple, la situación del rebote aparece sola en 4 de cada 1.000
comienzos. Ninguna estaba planeada. Los dos modelos encontraron las excepciones (7 de 7) y escribieron la ley
del rebote en el juego donde no hacía falta.

**8. No hubo ninguna respuesta segura y equivocada en las 29 partidas del primer experimento**, y en las
tablas al azar sin estructura los modelos dijeron "no sé". Las trampas (patrones que se rompen tarde) siguen
sin probarse.

## Lo que falló en el proceso

- Los dos críticos y la propia propuesta del 15-nov decían que los mundos plantados iban a salir fáciles.
  Se anotó como un riesgo y se construyó igual, sin decirle antes a Lucas, en concreto, por qué iba a pasar.
- De la primera prueba se sacó una lección chica ("las sumas tienen receta") en vez de la general ("lo que
  se escribe en la regla se lee de vuelta").
- Una idea ("verdad calculada con una computadora más grande") se propuso como nueva cuando ya estaba en la
  propuesta del repo, y se descartó en un mensaje.

## Preguntas abiertas

1. ¿Existe un juego con resolución conocida, armado sin secretos, que el mejor modelo no resuelva y que sí
   resuelva con la idea nombrada? Si no existe, los juegos diseñados no miden descubrimiento en la frontera.
2. En mundos donde el patrón sale solo: ¿qué se le pide a la IA, y cómo sabemos que lo que no encontró
   estaba para encontrar?
3. ¿Qué queremos decir con "descubrir" para un modelo que conoce todo lo publicado? Posibles: encontrar algo
   que nadie publicó; llevar adelante una investigación larga; sacar información escondida con
   experimentos; buscar mejor que un buscador a ciegas.
