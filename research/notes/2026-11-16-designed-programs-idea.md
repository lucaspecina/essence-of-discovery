# Nota: juegos con un programa diseñado debajo (idea guardada, sin probar)

16-nov-2026. Salió de la charla con Lucas después de la primera prueba con IAs. Lucas pidió guardarla
como interesante. **Nada de esto está construido ni corrido con un modelo.**

## De dónde sale

En la [primera prueba](../../experiments/2026-11-16-mixing-ladder/reading.md) lo que había debajo de cada
juego era siempre lo mismo: una suma de las tres vecinas, con los nombres de los símbolos cambiados. Para
ese tipo existe un método único que resuelve todos los casos, y `gpt-6-astra` lo aplicó (25 a 112 segundos
por juego). Pasar de 5 símbolos a 25 no le costó nada.

## La idea

Elegir nosotros **qué hace la fila a la larga**, escribirlo como un procedimiento, y recién después
escribir las reglas que lo cumplen. Las reglas se entregan a la vista, sin renombrar nada. Lo único que no
está escrito en ningún lado es qué terminan haciendo.

**Ejemplo chico (verificado con cuentas, versión simplificada).** Una fila de casillas con 0 y 1 y una
marca parada en una casilla. Tres reglas:

- si la marca está sobre un 1, lo cambia a 0 y pasa a la casilla de la izquierda;
- si está sobre un 0, lo cambia a 1 y vuelve a la punta derecha;
- las casillas sin marca no cambian.

Con eso la fila cuenta en binario: 0000, 0001, 0010, 0011, 0100... Como sabemos que cuenta, sabemos la fila
de cualquier paso sin correrla: hacer `n` sumas lleva `2n − (cantidad de unos de n)` pasos. La fórmula
coincide con la cuenta paso por paso en los pasos 0 a 2.999, en el millón y en el 3.000.007. En el paso
10^18 la cuenta va por 500.000.000.000.000.013.

**Ejemplo de dos partes (no armado).** La fila partida en dos zonas. La derecha cuenta como arriba. Cada
vez que se llena y vuelve a cero, la marca cruza a la izquierda y multiplica por 3 el número que hay ahí.

## Tres cosas que esta forma de armar permite y las anteriores no

1. **Un fenómeno que todavía no pasó.** Con 40 casillas a la derecha, la primera multiplicación ocurre
   cerca del paso 2 billones. La IA, con su computadora, llega a unos miles de millones. Las reglas que
   multiplican están a la vista pero no se usan nunca en lo que ella puede correr. Para contestar por el
   paso 10^18 (unas 450.000 multiplicaciones después) tiene que predecir algo que no vio ocurrir: cuándo
   pasa, qué hace, cuántas veces.
2. **Pares que solo se distinguen entendiendo.** Dos juegos iguales salvo en una regla (en uno multiplica
   por 3; en el otro, por 3 y suma 1). En todo lo que la IA puede correr son idénticos; en el paso 10^18
   son distintos. Solo acierta los dos quien entendió esa regla.
3. **Niveles.** Un tercer fenómeno que recién aparece después de muchas multiplicaciones, y un cuarto.
   La medida sería hasta qué nivel predice bien cada modelo.

Se puede automatizar: las piezas (contar, multiplicar, copiar) y las formas de conectarlas se arman una
vez; después un programa sortea combinaciones, escribe las reglas, calcula la respuesta y la comprueba
contra la cuenta paso por paso.

## La objeción de Lucas

"Son cosas muy de juguete: siempre sumas, multiplicaciones, cambios básicos. No es que va a averiguar
sistemas complejos como los de Wolfram con reglas arbitrarias."

Lo que es cierto de la objeción: todo sale de piezas que nosotros entendemos; en estos juegos nunca hay
algo que no sepamos.

Una salida posible, **sin verificar**: lo que nosotros conocemos por diseño no tiene que ser una fórmula
del fenómeno de arriba; alcanza con conocer el *reloj* escondido. Si la zona izquierda avanza un paso de
una regla cualquiera (por ejemplo una regla sorteada, o la regla 30) cada vez que la derecha da una vuelta,
en el paso 10^18 esa regla dio unos 450.000 pasos, y eso se calcula corriéndola. El fenómeno de arriba
puede ser entonces un sistema arbitrario, en cámara lenta.

## Lo que no se sabe

- Si `gpt-6-astra` lo resuelve. Puede leer las reglas que nunca se usaron y razonar sobre ellas, o armar a
  mano una fila a punto de dar la vuelta y mirar qué pasa.
- Si alguien ya lo hizo. Hice 8 búsquedas generales el 16-nov (resúmenes, nada a texto completo) y no
  apareció este diseño; no busqué todavía lo específico (fenómeno no observado, pares de una regla).
- Si lo que mide es descubrimiento o paciencia para leer reglas.

## Idea descartada el mismo día (queda anotada)

"Reglas que nadie diseñó, con la respuesta calculada en una computadora mucho más grande que la de la IA."
Ya estaba escrita en la [propuesta del 15-nov](../proposals/2026-11-15-discovery-as-finding-a-shortcut.md)
como "mundos salvajes" (§5.5), con un antecedente de 2011 (Zenil y otros). La objeción de Lucas: es lo de
DeepMind en versión barata y no deja elegir el fenómeno. La probé sin querer en chico en la primera prueba
(tres juegos de tabla sorteada): `gpt-6-astra` resolvió dos contando más rápido, sin encontrar nada.
