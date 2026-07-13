#!/usr/bin/env python3
"""
E-011 - Testa H-011: a variancia de total_stopping_time(n) cresce linearmente
em log2(n), com coeficiente ~186.93 (derivado da heuristica de passeio
aleatorio com deriva, via aproximacao de tempo de primeira passagem), nao
quadraticamente - ou seja, a variancia residual de H-010 e ruido previsto,
nao estrutura escondida.

Amostra varios "niveis" de log2(n) (de magnitudes bem diferentes, usando
inteiros grandes - Python lida com isso nativamente) e mede a variancia
empirica de total_stopping_time dentro de cada nivel.

Reproduzir: python3 experiment.py [K_POR_NIVEL] [SEED]
"""
import sys
import math
import random


def total_steps(n):
    total = 0
    while n != 1:
        m = 3 * n + 1
        a = 0
        while m % 2 == 0:
            m //= 2
            a += 1
        total += 1 + a
        n = m
    return total


def main():
    k_per_level = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 42
    rng = random.Random(seed)

    levels = [10, 15, 20, 25, 30, 35, 40, 45]

    log2_3 = math.log2(3)
    mu = log2_3 - 2.0
    var_a = 2.0
    c = 1 + log2_3
    coef_teorico = c ** 2 * var_a / abs(mu) ** 3

    print(f"K por nivel = {k_per_level}")
    print(f"coeficiente teorico (Var ~ coef * log2(n)) = {coef_teorico:.2f}")
    print()
    print(f"{'log2(n) alvo':>12} {'media':>10} {'variancia':>12} {'var/log2n':>10} {'K empirico (media/log2n)':>26}")

    results = []
    for level in levels:
        low = 2 ** level
        high = 2 ** (level + 1)
        samples = []
        for _ in range(k_per_level):
            n = rng.randrange(low // 2, high // 2) * 2 + 1
            samples.append(total_steps(n))

        mean_ts = sum(samples) / len(samples)
        var_ts = sum((x - mean_ts) ** 2 for x in samples) / (len(samples) - 1)
        log2n_mid = level + 0.5  # aprox. representativo do nivel [2^level, 2^(level+1))

        results.append((log2n_mid, mean_ts, var_ts))
        print(f"{log2n_mid:>12.1f} {mean_ts:>10.2f} {var_ts:>12.2f} {var_ts/log2n_mid:>10.2f} {mean_ts/log2n_mid:>26.3f}")

    # regressao: variancia ~ coef * log2(n), sem intercepto (forcado por 0, ja que Var(0)=0 faz sentido)
    sum_xy = sum(x * v for x, _, v in results)
    sum_xx = sum(x * x for x, _, _ in results)
    coef_empirico = sum_xy / sum_xx

    print()
    print(f"coeficiente empirico (regressao Var ~ coef*log2n, sem intercepto) = {coef_empirico:.2f}")
    print(f"coeficiente teorico = {coef_teorico:.2f}")
    print(f"diferenca relativa = {abs(coef_empirico - coef_teorico) / coef_teorico * 100:.1f}%")


if __name__ == "__main__":
    main()
