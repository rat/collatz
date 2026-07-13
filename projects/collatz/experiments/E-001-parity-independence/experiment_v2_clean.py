#!/usr/bin/env python3
"""
E-001 v2 - versao corrigida.

Problema identificado na v1 (experiment.py): agregar pares (a_i, a_{i+1}) de TODAS
as posicoes de TODAS as orbitas cria pseudo-replicacao severa. Orbitas de Collatz
colidem (duas trajetorias diferentes que atingem o mesmo valor intermediario
compartilham toda a cauda seguinte identica). Isso quebra a suposicao de amostras
independentes: o mesmo trecho de caminho pode ser contado dezenas de vezes.

Desenho corrigido: amostra K numeros iniciais DISTINTOS e GRANDES, espalhados
aleatoriamente num intervalo enorme, e olha so para os 2 primeiros passos (a_1, a_2)
de cada um. Com numeros iniciais grandes e aleatorios, a probabilidade de duas
trajetorias colidirem em 1-2 passos e desprezivel - cada par (a_1, a_2) e uma
observacao genuinamente independente. Isso testa exatamente a suposicao usada
pelos modelos estocasticos da literatura (Kontorovich-Lagarias): a_1 e a_2 sao
independentes?

Reproduzir: python3 experiment_v2_clean.py [K] [LOW] [HIGH] [SEED]
"""
import sys
import math
import random


def step(n):
    m = 3 * n + 1
    a = 0
    while m % 2 == 0:
        m //= 2
        a += 1
    return m, a


def chi_square_pvalue(x, k):
    if k <= 0:
        return float("nan")
    z = ((x / k) ** (1 / 3) - (1 - 2 / (9 * k))) / math.sqrt(2 / (9 * k))
    return 0.5 * math.erfc(z / math.sqrt(2))


def normal_pvalue_two_sided(z):
    return math.erfc(abs(z) / math.sqrt(2))


def main():
    k_samples = int(sys.argv[1]) if len(sys.argv) > 1 else 200_000
    low = int(sys.argv[2]) if len(sys.argv) > 2 else 10 ** 9
    high = int(sys.argv[3]) if len(sys.argv) > 3 else 10 ** 12
    seed = int(sys.argv[4]) if len(sys.argv) > 4 else 42

    rng = random.Random(seed)

    starts = set()
    while len(starts) < k_samples:
        n = rng.randrange(low // 2, high // 2) * 2 + 1  # forca impar
        starts.add(n)

    pairs = []
    m1_values = set()
    collisions = 0
    for n in starts:
        m1, a1 = step(n)
        if m1 in m1_values:
            collisions += 1
        m1_values.add(m1)
        m2, a2 = step(m1)
        pairs.append((a1, a2))

    print(f"K = {k_samples} numeros iniciais distintos e aleatorios em [{low}, {high}]")
    print(f"seed = {seed}")
    print(f"colisoes detectadas em m1 (deveria ser ~0) = {collisions}")
    print()

    n_pairs = len(pairs)
    sum_x = sum_y = sum_x2 = sum_y2 = sum_xy = 0.0
    pair_counts = {}
    marginal_counts = {}
    bucket_max = 8

    def bucket(a):
        return a if a < bucket_max else bucket_max

    for a1, a2 in pairs:
        sum_x += a1
        sum_y += a2
        sum_x2 += a1 * a1
        sum_y2 += a2 * a2
        sum_xy += a1 * a2
        key = (bucket(a1), bucket(a2))
        pair_counts[key] = pair_counts.get(key, 0) + 1
        marginal_counts[bucket(a1)] = marginal_counts.get(bucket(a1), 0) + 1

    mean_x = sum_x / n_pairs
    mean_y = sum_y / n_pairs
    cov = sum_xy / n_pairs - mean_x * mean_y
    var_x = sum_x2 / n_pairs - mean_x * mean_x
    var_y = sum_y2 / n_pairs - mean_y * mean_y
    r = cov / math.sqrt(var_x * var_y)
    z_fisher = math.atanh(max(min(r, 0.999999), -0.999999)) * math.sqrt(n_pairs - 3)
    p_corr = normal_pvalue_two_sided(z_fisher)

    buckets = sorted(marginal_counts.keys())
    row_totals = {b: 0 for b in buckets}
    col_totals = {b: 0 for b in buckets}
    for (bi, bj), c in pair_counts.items():
        row_totals[bi] += c
        col_totals[bj] += c

    chi2 = 0.0
    for bi in buckets:
        for bj in buckets:
            observed = pair_counts.get((bi, bj), 0)
            expected = row_totals[bi] * col_totals[bj] / n_pairs
            if expected > 0:
                chi2 += (observed - expected) ** 2 / expected
    dof = (len(buckets) - 1) ** 2
    p_chi2 = chi_square_pvalue(chi2, dof)

    print(f"--- teste de independencia entre a_1 e a_2 (n_pares={n_pairs}) ---")
    print(f"  Pearson r = {r:.5f}  (z-Fisher={z_fisher:.2f}, p={p_corr:.3e})")
    print(f"  qui-quadrado = {chi2:.1f}  (dof={dof}, p~={p_chi2:.3e})")
    if p_corr < 0.01 or p_chi2 < 0.01:
        print("  => dependencia estatisticamente significativa detectada.")
    else:
        print("  => independencia NAO rejeitada nesta amostra (consistente com o modelo i.i.d.).")


if __name__ == "__main__":
    main()
