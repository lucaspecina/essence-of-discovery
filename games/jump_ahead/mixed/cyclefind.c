/* Cuenta larga en C, para lo que no tiene regla de resultado.
 *
 * Uso:
 *   cyclefind brent   MAXSTEPS < problema     -> "CYCLE mu lambda"  o  "NONE maxsteps"
 *   cyclefind advance STEPS    < problema     -> la fila después de STEPS pasos
 *
 * El problema, por la entrada estándar: q n, después los q^3 valores de la tabla
 * (índice l*q*q + c*q + r), después los n valores de la fila del comienzo.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

static int q, n;
static uint8_t *table;

static inline void step(const uint8_t *s, uint8_t *out) {
    int qq = q * q;
    out[0] = table[s[n - 1] * qq + s[0] * q + s[1]];
    for (int i = 1; i < n - 1; i++) out[i] = table[s[i - 1] * qq + s[i] * q + s[i + 1]];
    out[n - 1] = table[s[n - 2] * qq + s[n - 1] * q + s[0]];
}

int main(int argc, char **argv) {
    if (argc != 3) { fprintf(stderr, "uso: cyclefind brent|advance N\n"); return 2; }
    unsigned long long limit = strtoull(argv[2], NULL, 10);
    if (scanf("%d %d", &q, &n) != 2) return 2;
    table = malloc((size_t)q * q * q);
    for (long i = 0; i < (long)q * q * q; i++) { int v; if (scanf("%d", &v) != 1) return 2; table[i] = (uint8_t)v; }
    uint8_t *start = malloc(n), *a = malloc(n), *b = malloc(n), *tmp = malloc(n);
    for (int i = 0; i < n; i++) { int v; if (scanf("%d", &v) != 1) return 2; start[i] = (uint8_t)v; }

    if (strcmp(argv[1], "advance") == 0) {
        memcpy(a, start, n);
        for (unsigned long long t = 0; t < limit; t++) { step(a, tmp); memcpy(a, tmp, n); }
        for (int i = 0; i < n; i++) printf("%d%s", a[i], i + 1 < n ? " " : "\n");
        return 0;
    }

    /* Brent: encuentra el largo del ciclo (lambda) y después dónde empieza (mu). */
    unsigned long long power = 1, lam = 1, steps = 0;
    memcpy(a, start, n);                 /* tortuga */
    step(start, b); steps++;             /* liebre  */
    while (memcmp(a, b, n) != 0) {
        if (power == lam) { memcpy(a, b, n); power *= 2; lam = 0; }
        step(b, tmp); memcpy(b, tmp, n); lam++; steps++;
        if (steps > limit) { printf("NONE %llu\n", limit); return 0; }
    }
    memcpy(a, start, n); memcpy(b, start, n);
    for (unsigned long long i = 0; i < lam; i++) { step(b, tmp); memcpy(b, tmp, n); }
    unsigned long long mu = 0;
    while (memcmp(a, b, n) != 0) {
        step(a, tmp); memcpy(a, tmp, n);
        step(b, tmp); memcpy(b, tmp, n);
        mu++;
    }
    printf("CYCLE %llu %llu\n", mu, lam);
    return 0;
}
