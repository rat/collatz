#!/usr/bin/env python3
"""
Sugestao #5 (terceira rodada de uma IA externa): teoria de valores
extremos (EVT) como validacao do expoente de cauda alpha=2 (H-104)
imune ao problema de que a variancia esta na fronteira da divergencia
justamente em alpha=2 (o que contamina estimadores baseados em
variancia/Jensen).

Se P(G>x) ~ C*x^{-alpha} (cauda regularmente variante, ja confirmado
alpha=2 via estimador de Hill em H-104), entao pelo Teorema de
Fisher-Tippett-Gnedenko o maximo de um bloco de tamanho n, devidamente
normalizado, converge a uma distribuicao de Frechet com parametro de
forma xi=1/alpha=0.5. Consequencia direta e mais simples de testar:
a ESCALA tipica do maximo de blocos de tamanho n cresce como n^{1/alpha}
= n^0.5 - testavel via regressao log-log do maximo tipico (mediana)
contra o tamanho do bloco, sem precisar ajustar a GEV inteira (mas
fazemos isso tambem como checagem secundaria, com scipy).

Reproduzir: python3 experiment_evt_frechet.py
"""
import math
import random
import statistics

import numpy as np
from scipy.stats import genextreme

from experiment_headroom import measure_G_headroom


def generate_sample(n, log_lo, log_hi, mult, seed):
    rng = random.Random(seed)
    vals = []
    for _ in range(n):
        mag = 10 ** rng.uniform(log_lo, log_hi)
        v = int(mag) | 1
        if v % 3 == 0:
            continue
        G = measure_G_headroom(v, mult)
        if G is not None and G > 0:
            vals.append(G)
    return vals


def block_maxima(vals, block_size, rng):
    """Particiona vals (embaralhados) em blocos de tamanho block_size,
    retorna a lista de maximos de cada bloco completo."""
    shuffled = vals[:]
    rng.shuffle(shuffled)
    n_blocks = len(shuffled) // block_size
    maxima = []
    for i in range(n_blocks):
        block = shuffled[i * block_size:(i + 1) * block_size]
        maxima.append(max(block))
    return maxima


def main():
    print("=== Teste EVT: maximo de blocos deveria escalar como n^(1/alpha)=n^0.5 ===\n")

    N_TOTAL = 150000
    print(f"Gerando amostra de {N_TOTAL} valores de G(v)...")
    vals = generate_sample(N_TOTAL, 5.0, 7.0, mult=2000, seed=9999)
    print(f"{len(vals)} valores validos coletados.\n")

    rng = random.Random(1234)
    block_sizes = [10, 20, 50, 100, 200, 500, 1000, 2000]
    print(f"{'n (tamanho bloco)':>18} {'n_blocos':>9} {'mediana(max)':>14} {'media(max)':>12}")
    log_n, log_median = [], []
    for n in block_sizes:
        maxima = block_maxima(vals, n, rng)
        med = statistics.median(maxima)
        mean = statistics.mean(maxima)
        print(f"{n:>18} {len(maxima):>9} {med:>14.3f} {mean:>12.3f}")
        log_n.append(math.log(n))
        log_median.append(math.log(med))

    # regressao log-log simples
    nn = len(log_n)
    mx = sum(log_n) / nn
    my = sum(log_median) / nn
    cov = sum((x - mx) * (y - my) for x, y in zip(log_n, log_median)) / nn
    varx = sum((x - mx) ** 2 for x in log_n) / nn
    slope = cov / varx
    print(f"\nInclinacao log(mediana do maximo) vs log(n): {slope:.4f}")
    print("(previsao teorica para alpha=2: 1/alpha = 0.5000)")

    print("\n=== Ajuste da distribuicao GEV (scipy) aos maximos de blocos (n=200) ===")
    maxima_200 = block_maxima(vals, 200, random.Random(777))
    print(f"n_blocos={len(maxima_200)}")
    c, loc, scale = genextreme.fit(maxima_200)
    xi_scipy = -c  # scipy usa c = -xi na convencao usual de Fisher-Tippett-Gnedenko
    print(f"scipy genextreme.fit: c={c:.4f}  loc={loc:.3f}  scale={scale:.3f}")
    print(f"xi (convencao EVT padrao, xi=-c) = {xi_scipy:.4f}")
    print("(previsao teorica para alpha=2: xi = 1/alpha = 0.5000)")


if __name__ == "__main__":
    main()
