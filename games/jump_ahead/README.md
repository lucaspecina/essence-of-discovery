# jump-ahead

**El juego.** La IA ve la regla completa de un sistema simple y recibe una pregunta sobre un futuro
lejísimo (por ejemplo, el paso un trillón). Tiene una computadora chica para experimentar, que no alcanza
para llegar paso por paso. Entrega un programita que contesta rápido y dice cuán segura está. Se corrige
contra la respuesta exacta, sin ninguna IA de juez. Sin atajo es imposible; con atajo es fácil.

**Qué mide.** Si la IA encuentra el atajo y, sobre todo, si lo *ve* o lo *busca*: se esconde el mismo
atajo en pajares cada vez más grandes y se mira cuánto crece su esfuerzo, contra un buscador a ciegas.
También cuántas veces cree ver un atajo que no está (mundos sin atajo y trampas).

La explicación completa, con figuras, está en la [guía](../../docs/guia.md).

## Estado (15-nov-2026)

**Hecho, sin IA:** seis ejemplos de mundos verificados con cuentas. Para reproducirlos:

```
pip install -r requirements.txt
python games/jump_ahead/verificacion.py
```

Corre en segundos y comprueba, entre otras cosas:

- un sistema con atajo donde el paso un trillón se contesta en una fracción de milisegundo;
- un sistema disfrazado (5 símbolos renombrados) donde la prueba estándar deja de ver el atajo, un
  buscador a ciegas lo recupera probando renombres (sirven 20 de 120), y el estado del paso un trillón
  sale en milisegundos; sin el atajo, el sistema recién se repite a los 794.728.597.005.208 pasos;
- una trampa: un dibujo que se repite 118 veces seguidas y a la vuelta siguiente cambia.

**No hecho:** ninguna partida con una IA. No hay todavía generador de mundos, ni computadora de pruebas
para el agente, ni puntaje implementado.

## Lo que sigue (espera el OK de Lucas)

1. Armar unos 12 mini-juegos (con atajo a dos niveles de disfraz, sin atajo, trampas) y verificarlos sin IA.
2. Probar un modelo actual: primero 4 partidas para medir el costo, después unas 48.
3. Leer el resultado contra reglas escritas de antemano:

| Si pasa esto | Quiere decir | Qué se hace |
|---|---|---|
| Resuelve todo, hasta lo más disfrazado | El juego es fácil para los modelos de hoy | Endurecer o cerrar |
| No resuelve ni con la idea nombrada | El juego está mal armado | Arreglar el juego |
| Resuelve, y su esfuerzo crece como el del buscador a ciegas | Busca | Resultado |
| Resuelve, y su esfuerzo casi no crece | Ve (si no era un truco de manual) | Resultado |

## Lo más cercano que hicieron otros

- DeepMind, [arXiv:2610.22603](https://arxiv.org/abs/2610.22603): una IA encuentra atajos verificados en
  máquinas de juguete sin resolver. La manera de mirar la arma un programa de los autores; un solo tipo de
  atajo; no mide cómo los encuentra.
- Han et al., [arXiv:2505.10844](https://arxiv.org/abs/2505.10844), y Hu et al.,
  [arXiv:2602.10329](https://arxiv.org/abs/2602.10329): la pregunta "¿fuerza bruta o algo más fino?", con
  una IA de juez leyendo la solución.
- Invariantes de ciclos con IA y verificador, por ejemplo [arXiv:2508.00419](https://arxiv.org/abs/2508.00419):
  los modelos ya resuelven el banco clásico completo.

Leído de resúmenes y partes, no a texto completo. El detalle y el resto de las fuentes están en el
[documento de la propuesta](../../biblioteca/2026-11-15-reformulacion-descubrir-es-encontrar-un-atajo.md) (§8).
