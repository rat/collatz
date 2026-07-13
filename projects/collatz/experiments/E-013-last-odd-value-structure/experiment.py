#!/usr/bin/env python3
"""
E-013 - Verifica H-013: o ultimo valor impar (>1) de qualquer orbita e
sempre J_t=(4^t-1)/3 para algum t, e tabula a distribuicao de t.

Reproduzir: python3 experiment.py [N_AMOSTRAS] [SEED]
"""
import sys
import random
from collections import Counter


def last_odd_before_1(n):
    prev_odd = None
    while n != 1:
        if n % 2 == 1:
            prev_odd = n
            n = 3 * n + 1
        else:
            n //= 2
    return prev_odd


def find_t(m):
    t = 0
    val = 0  # J_0 = 0, nao usado; comeca t=1
    t = 1
    val = 1  # J_1 = (4^1-1)/3 = 1
    while val < m:
        t += 1
        val = (4 ** t - 1) // 3
    return t if val == m else None


def main():
    n_samples = int(sys.argv[1]) if len(sys.argv) > 1 else 300_000
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 2
    rng = random.Random(seed)

    counts = Counter()
    mismatches = 0
    for _ in range(n_samples):
        n = rng.randrange(3, 10 ** 9) | 1
        m = last_odd_before_1(n)
        t = find_t(m)
        if t is None:
            mismatches += 1
        else:
            counts[t] += 1

    print(f"amostras = {n_samples}, incompativeis com a formula J_t = {mismatches}")
    total = sum(counts.values())
    for t in sorted(counts):
        j_t = (4 ** t - 1) // 3
        esteril = " (esteril: J_t divisivel por 3, explicado por H-005)" if j_t % 3 == 0 else ""
        print(f"  t={t:2d}  J_t={j_t:8d}  contagem={counts[t]:7d}  fracao={counts[t]/total:.4f}{esteril}")

    if mismatches == 0:
        print()
        print("=> Formula confirmada sem excecao.")


if __name__ == "__main__":
    main()
