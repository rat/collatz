#!/usr/bin/env python3
"""
E-006 - Testa H-006: o vies mod-3 encontrado em H-004 (recordistas estritos,
n=57) se confirma com mais poder estatistico usando os top-K numeros por
stopping time total (K bem maior que 57), num intervalo grande?

Usa heap para manter os top-K sem guardar todos os valores escaneados
(economiza memoria para limites grandes).

Reproduzir: python3 experiment.py [LIMIT] [K] [SEED]
"""
import sys
import math
import random
import heapq


def total_steps_only(n):
    total_steps = 0
    while n != 1:
        m = 3 * n + 1
        while m % 2 == 0:
            m //= 2
            total_steps += 1
        total_steps += 1
        n = m
    return total_steps


def chi_square_pvalue(x, k):
    if k <= 0:
        return float("nan")
    z = ((x / k) ** (1 / 3) - (1 - 2 / (9 * k))) / math.sqrt(2 / (9 * k))
    return 0.5 * math.erfc(z / math.sqrt(2))


def homogeneity_chi2(group_a_residues, group_b_residues, modulus):
    counts_a = [0] * modulus
    counts_b = [0] * modulus
    for r in group_a_residues:
        counts_a[r] += 1
    for r in group_b_residues:
        counts_b[r] += 1
    n_a, n_b = len(group_a_residues), len(group_b_residues)
    n_total = n_a + n_b
    chi2 = 0.0
    min_expected = float("inf")
    for c in range(modulus):
        col_total = counts_a[c] + counts_b[c]
        if col_total == 0:
            min_expected = 0
            continue
        expected_a = n_a * col_total / n_total
        expected_b = n_b * col_total / n_total
        min_expected = min(min_expected, expected_a, expected_b)
        if expected_a > 0:
            chi2 += (counts_a[c] - expected_a) ** 2 / expected_a
        if expected_b > 0:
            chi2 += (counts_b[c] - expected_b) ** 2 / expected_b
    dof = modulus - 1
    p = chi_square_pvalue(chi2, dof) if dof > 0 else float("nan")
    return chi2, dof, p, min_expected >= 5


def main():
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 30_000_000
    k_top = int(sys.argv[2]) if len(sys.argv) > 2 else 1000
    seed = int(sys.argv[3]) if len(sys.argv) > 3 else 42
    rng = random.Random(seed)

    # heap minimo de tamanho k_top guardando os maiores total_steps vistos
    heap = []  # (total_steps, n)
    for n in range(1, limit, 2):
        ts = total_steps_only(n)
        if len(heap) < k_top:
            heapq.heappush(heap, (ts, n))
        elif ts > heap[0][0]:
            heapq.heapreplace(heap, (ts, n))

    top_k = [n for ts, n in heap]
    top_k_steps = sorted((ts for ts, n in heap), reverse=True)

    print(f"limite = {limit}, K = {k_top}")
    print(f"stopping time minimo no top-K = {top_k_steps[-1]}, maximo = {top_k_steps[0]}")
    print()

    top_k_set = set(top_k)
    typical_pool = []
    while len(typical_pool) < k_top * 10:
        n = rng.randrange(1, limit) | 1
        if n not in top_k_set:
            typical_pool.append(n)

    print("=== residuo: top-K vs amostra tipica ===")
    for modulus in [3, 9, 27, 4, 8, 5, 7]:
        res_top = [n % modulus for n in top_k]
        res_typ = [n % modulus for n in typical_pool]
        chi2, dof, p, valido = homogeneity_chi2(res_top, res_typ, modulus)
        if not valido:
            print(f"  mod {modulus:3d}: AMOSTRA INSUFICIENTE (celula esperada < 5) - resultado nao confiavel")
            continue
        sig = "***" if p < 0.01 else ("*" if p < 0.05 else "")
        print(f"  mod {modulus:3d}: chi2={chi2:8.2f} dof={dof:3d} p={p:.3e} {sig}")

    print()
    print("=== distribuicao detalhada mod 3 do top-K ===")
    from collections import Counter
    c3 = Counter(n % 3 for n in top_k)
    for r in [0, 1, 2]:
        frac = c3.get(r, 0) / len(top_k)
        print(f"  residuo {r} mod 3: {c3.get(r, 0)} ({frac:.4f})  -- esperado sob uniforme = {1/3:.4f}")


if __name__ == "__main__":
    main()
