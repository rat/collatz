#!/usr/bin/env python3
"""
E-013b - Varredura EXAUSTIVA (nao amostragem aleatoria) de todos os n
impares ate um limite, tabulando a distribuicao exata do ultimo valor
impar J_t. Complementa experiment.py (que usa amostragem aleatoria, boa
para t pequeno mas com ruido demais para t grande).

Reproduzir: python3 experiment_exhaustive.py [N_MAX]
"""
import sys
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
    t = 1
    val = 1
    while val < m:
        t += 1
        val = (4 ** t - 1) // 3
    return t if val == m else None


def main():
    n_max = int(sys.argv[1]) if len(sys.argv) > 1 else 20_000_000

    counts = Counter()
    for n in range(3, n_max, 2):
        m = last_odd_before_1(n)
        t = find_t(m)
        counts[t] += 1

    total = sum(counts.values())
    print(f"n_max = {n_max}, total de n analisados (impares) = {total}")
    print()
    for t in sorted(counts):
        j_t = (4 ** t - 1) // 3
        mod3 = j_t % 3
        print(f"  t={t:2d}  J_t={j_t:9d}  mod3={mod3}  contagem={counts[t]:8d}  fracao={counts[t]/total:.6f}")

    print()
    print("--- razao entre pares adjacentes (t=1 mod3, t+1=2 mod3) ---")
    for t in sorted(counts):
        j_mod3_t = ((4 ** t - 1) // 3) % 3
        if j_mod3_t == 1 and (t + 1) in counts:
            razao = counts[t + 1] / counts[t] if counts[t] > 0 else float("inf")
            print(f"  t={t}(mod3=1,c={counts[t]}) vs t={t+1}(mod3=2,c={counts[t+1]}): razao={razao:.3f}")


if __name__ == "__main__":
    main()
