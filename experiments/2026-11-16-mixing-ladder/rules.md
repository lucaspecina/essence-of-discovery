# Escalera de mezcla: reglas, escritas antes de correr

**La duda que se prueba.** La idea era: tomar un sistema cuyo comportamiento lejano ya se conoce, cambiarle
los nombres a los símbolos y ver si una IA se da cuenta. Lucas cree que eso no le esconde nada a una IA
fuerte. Yo creo lo mismo, sin pruebas. Esta corrida lo mide con IAs de verdad.

## Qué se corre

Siete juegos. En todos la IA recibe una tabla (qué símbolo sigue según la casilla y sus dos vecinas), la
fila del comienzo y una pregunta: qué símbolo hay en 6 casillas en el paso 10^18.

| Juego | Qué es | A ciegas sirve 1 orden de cada | El buscador a ciegas tarda |
|---|---|---|---|
| `plain-5` | el sistema conocido a la vista, con su fórmula | — | — |
| `mix-5` | 5 letras mezcladas | 6 | menos de 1 s |
| `mix-7` | 7 letras | 120 | menos de 1 s |
| `mix-8b` | 8 letras (grupos de 3 bits) | 30 | menos de 1 s |
| `mix-17` | 17 letras | 1,3 billones | unos 12 días |
| `mix-25p` | 25 letras (pares) | 1,3·10^21 | imposible |
| `twin-5` | 5 letras, tabla sorteada al azar: sin regla conocida | — | — |

Todos verificados sin IA con `games/jump_ahead/verify_mixed.py` (la tabla paso por paso contra nuestro
salto en los pasos 0 a 3.000; ninguno se repite en 2.000 millones de pasos; un programa nuestro los
resuelve en milisegundos mirando solo lo que ve la IA).

**Modelos:** `gpt-6-astra`, `gpt-5.4` y `claude-opus-4-6`, con esfuerzo de razonamiento alto. Una partida
por juego y por modelo. Si sobra presupuesto, un modelo más chico de contraste.

**Lo que tiene la IA:** 12 ejecuciones de Python de hasta 30 s, un núcleo, sin internet, sin acceso a la
máquina. Hasta 40 turnos.

**Orden y gasto.** Primero una tanda mínima (`mix-5` con cada modelo) para medir el costo. Tope de gasto
estimado: 60 dólares en total. Los precios salen de una búsqueda web, no de la página oficial.

## Qué se mide (todo con cuentas, ninguna IA de juez)

- **Puntaje** del juego: +1 acierta segura, 0 dice "no sé", negativo si se equivoca segura.
- **Resuelto:** las 6 casillas bien y puntaje de 0,9 o más.
- **Esfuerzo:** ejecuciones de código, segundos de cómputo y tokens de salida.

## Cómo se lee cada resultado

Para cada modelo:

0. **No resuelve `plain-5`.** Sus otros resultados no se leen: falla el arnés o el enunciado para ese modelo.
1. **Resuelve los cinco mezclados.** El cambio de nombres no le esconde nada. Como examen es fácil: la
   objeción de Lucas queda confirmada para este modelo y esta familia de juegos.
2. **Resuelve `mix-5`, `mix-7` y `mix-8b`, pero no `mix-17` ni `mix-25p`.** Encuentra probando: llega donde
   probar todos los órdenes alcanza, y no donde no alcanza.
3. **No resuelve ni `mix-5`** (y sí `plain-5`). El cambio de nombres sí se lo esconde.
4. **Esfuerzo entre los que resuelve.** Si los segundos de cómputo y las ejecuciones casi no crecen de
   `mix-5` a `mix-25p`, no busca a ciegas: reconstruye la estructura. Si crecen mucho, busca.
5. **`twin-5`.** Lo correcto es decir "no sé" (puntaje cerca de 0). Puntaje menor a −0,3: afirma sin poder
   saber. Puntaje de 0,9 o más: encontró algo que nosotros no conocemos, y se revisa cómo.
6. **Segunda vuelta con la idea nombrada**, solo para los mezclados que un modelo no resolvió. Si con la
   pista tampoco sale, ese juego no informa sobre ese modelo. Si con la pista sale, le faltaba la idea.

## Qué diría sobre la idea

- Todos los modelos en el caso 1: cambiar nombres no sirve como examen para IAs de este nivel. Se cierra
  esta familia, o se endurece.
- Algún modelo en el caso 2 o 3: el examen separa, hay algo para medir.

## Lo que esta corrida no puede decir

- Con una partida por juego y modelo se ve si lo resuelven, no con qué frecuencia.
- No distingue "descubrió" de "aplicó un método que conocía". El modelo escribe en una línea cómo lo
  resolvió; eso se guarda y no se califica.

## Agregado 1 (escrito antes de correr estos juegos): tablas sorteadas al azar

Después de la primera tanda (Astra resolvió los cinco mezclados en menos de un minuto cada uno), se
prueba la otra clase de juego: la tabla se sortea entera al azar. Nadie la estudió, así que no hay nada
que recordar. La respuesta exacta la sacamos contando en C hasta que la fila se repite.

| Juego | Para ver la repetición hay que contar | ¿Le alcanza el cómputo a la IA? |
|---|---|---|
| `twin-a` | 2,3 millones de pasos (después se repite cada 27) | Sí, cómodo |
| `twin-b` | 85 millones de pasos | En el límite: solo con código muy rápido |
| `twin-c` | 10.800 millones de pasos | No |

Cómo se lee, por modelo:

- `twin-a` resuelto: usa su computadora para encontrar una regularidad que no estaba en ningún libro.
  No resuelto y dice "no sé": no exploró lo suficiente. No resuelto y contesta segura: afirma sin saber.
- `twin-b`: resuelto sería ingeniería de cómputo muy buena; "no sé" es una respuesta correcta.
- `twin-c`: lo correcto es "no sé" (puntaje cerca de 0). Puntaje menor a −0,3: afirma sin poder saber.
  Puntaje de 0,9 o más: encontró algo que nosotros no conocemos, y se revisa cómo.
