# De WAGER a jump-ahead: qué cambió y qué sigue igual

Para saber de dónde venimos. La formulación es de Lucas (15-nov-2026).

## Lo que sigue igual

El espíritu es el mismo desde SREG y WAGER:

- Nosotros sabemos la respuesta.
- La IA tiene que encontrarla.
- La calificamos con una cuenta, sin otra IA de juez.

Lo que buscamos tampoco cambió: **medir si una IA descubre.**

## Antes: una regla de generación escondida

En WAGER había una **regla de generación** que la IA no veía. Esa regla producía datos. La IA recibía los
datos y tenía que adivinar la regla.

El problema era armar el juego:

- Había que diseñar la regla, y eso ya era difícil.
- Además, los datos tenían que traer la información necesaria para poder descubrirla. Eso obligaba a
  decidir cuántos datos dar, con qué presupuesto y con cuánto ruido.
- Y la idea nueva tenía que convenir. Una vez la explicación simple ya sacaba 0,986: cambiarla no pagaba.

Con tantas perillas, cuando la IA fallaba no se podía aislar el motivo. Podían faltarle datos, podía
haber ruido, podía no convenirle cambiar, o podía no ocurrírsele. No había forma de saber si "no saltó".

## Ahora: dos reglas, y la primera va a la vista

En jump-ahead hay dos reglas:

- **La regla de generación.** Dice cómo avanza el sistema un paso. Es simple y **la IA la ve entera**.
- **La regla de resultado.** Dice qué pasa lejos sin recorrer los pasos del medio. Es lo que la IA tiene
  que encontrar.

La regla de resultado no es algo que agregamos. Es una consecuencia de la regla de generación, que ya está
ahí aunque no se vea. Por eso también se la puede llamar **patrón emergente**: sale de la regla simple.

| | WAGER | jump-ahead |
|---|---|---|
| Qué ve la IA | Datos | La regla de generación, completa |
| Qué tiene que encontrar | La regla de generación | La regla de resultado |
| Qué la limita | Cantidad de datos, ruido, presupuesto | Solo cuánto puede calcular |
| Si falla, por qué puede ser | Datos, ruido, incentivo, o no se le ocurrió | No la encontró |
| Cómo sabemos la respuesta | La regla la escribimos nosotros | La regla de resultado la conocemos de antemano |

Dicho corto: **lo escondido subió un escalón.** Antes era la regla que genera. Ahora es lo que esa regla
produce a la larga.

Y los datos dejaron de ser un problema: como la IA tiene la regla, genera todos los que quiera.

## Tres precisiones, para no engañarnos

1. **No toda regla de generación tiene regla de resultado.** Para algunas, hasta donde se sabe, no hay
   otra que calcular paso por paso. Por eso el juego incluye casos sin premio: ahí lo correcto es decir
   "no sé".
2. **No medimos exactamente lo mismo que antes.** En WAGER el "salto" era cambiar la forma de la
   explicación cuando los datos lo pedían. Acá es encontrar la regla de resultado. Son parientes, no
   idénticos.
3. **Queda un control heredado.** Si la IA no la encuentra ni cuando le nombramos la idea, el juego está
   mal armado y no hay que culparla.

## Cómo se llama esto en otros lados

La **regla de resultado** es lo mismo que:

- el **atajo**, en nuestra [guía](guide.md);
- una **aceleración**, en el trabajo de DeepMind;
- un **bolsillo de reducibilidad**, en palabras de Wolfram.
