/* La realidad, corrida rápido: aplica la regla paso por paso, sin ningún atajo.
 *
 * Solo guarda las casillas no vacías. Eso no es un atajo: como el trío (vacía, vacía, vacía) da vacía,
 * una casilla lejos de toda casilla ocupada no puede cambiar. En cada paso se recalculan las casillas
 * ocupadas y sus dos vecinas.
 *
 * Entrada (stdin):
 *   K                       cantidad de símbolos (el 0 es "vacía")
 *   K*K*K números           tabla[l*K*K + c*K + r] = símbolo nuevo
 *   PASOS
 *   N                       casillas ocupadas al empezar
 *   N renglones "pos símbolo", en orden creciente de pos
 * Salida (stdout): N' y después N' renglones "pos símbolo".
 */
#include <stdio.h>
#include <stdlib.h>

typedef struct { long long pos; int sym; } Cell;

int main(void) {
    int K;
    if (scanf("%d", &K) != 1 || K < 2 || K > 16) return 2;
    int table[16 * 16 * 16];
    for (int i = 0; i < K * K * K; i++) if (scanf("%d", &table[i]) != 1) return 2;
    if (table[0] != 0) return 3;                     /* (vacía, vacía, vacía) tiene que dar vacía */
    unsigned long long steps;
    int n;
    if (scanf("%llu %d", &steps, &n) != 2) return 2;
    int cap = 4096;
    if (n > cap / 4) return 4;
    Cell *cur = malloc(sizeof(Cell) * cap), *next = malloc(sizeof(Cell) * cap);
    for (int i = 0; i < n; i++) if (scanf("%lld %d", &cur[i].pos, &cur[i].sym) != 2) return 2;

    for (unsigned long long t = 0; t < steps && n > 0; t++) {
        if (3 * n + 3 > cap) return 5;               /* el mundo creció más de lo que esperamos */
        int m = 0, j = 0;                            /* j: primera casilla ocupada con pos >= q-1 */
        long long last = cur[0].pos - 2;             /* última posición candidata ya calculada */
        for (int i = 0; i < n; i++) {
            for (long long q = cur[i].pos - 1; q <= cur[i].pos + 1; q++) {
                if (q <= last) continue;
                last = q;
                while (j < n && cur[j].pos < q - 1) j++;
                int l = 0, c = 0, r = 0, k = j;
                if (k < n && cur[k].pos == q - 1) { l = cur[k].sym; k++; }
                if (k < n && cur[k].pos == q)     { c = cur[k].sym; k++; }
                if (k < n && cur[k].pos == q + 1) { r = cur[k].sym; }
                int s = table[(l * K + c) * K + r];
                if (s) { next[m].pos = q; next[m].sym = s; m++; }
            }
        }
        Cell *tmp = cur; cur = next; next = tmp;
        n = m;
    }
    printf("%d\n", n);
    for (int i = 0; i < n; i++) printf("%lld %d\n", cur[i].pos, cur[i].sym);
    return 0;
}
