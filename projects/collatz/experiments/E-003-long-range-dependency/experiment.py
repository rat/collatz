#!/usr/bin/env python3
"""
E-003 - Testa H-003: existe dependencia entre a_1 e a_{1+k} para lags k > 1?

Reaproveita o desenho limpo validado em E-001 (amostra fresca de n grandes e
distintos por lag, para evitar colisao de orbitas / pseudo-replicacao - ver
protocols/new-experiment.md).

Reproduzir: python3 experiment.py [K] [MAX_LAG] [LOW] [HIGH] [SEED_BASE]
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


def test_lag(k_lag, k_samples, low, high, seed):
    rng = random.Random(seed)
    starts = set()
    while len(starts) < k_samples:
        n = rng.randrange(low // 2, high // 2) * 2 + 1
        starts.add(n)

    pairs = []
    visited = set()
    collisions = 0
    for n in starts:
        cur = n
        a_first = None
        a_last = None
        for step_idx in range(1, k_lag + 2):
            cur, a = step(cur)
            if cur in visited:
                collisions += 1
            visited.add(cur)
            if step_idx == 1:
                a_first = a
            if step_idx == k_lag + 1:
                a_last = a
        pairs.append((a_first, a_last))

    n_pairs = len(pairs)
    bucket_max = 8

    def bucket(a):
        return a if a < bucket_max else bucket_max

    sum_x = sum_y = sum_x2 = sum_y2 = sum_xy = 0.0
    pair_counts = {}
    marginal_counts = {}
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

    return {
        "lag": k_lag, "n_pairs": n_pairs, "collisions": collisions,
        "r": r, "p_corr": p_corr, "chi2": chi2, "dof": dof, "p_chi2": p_chi2,
    }


def main():
    k_samples = int(sys.argv[1]) if len(sys.argv) > 1 else 200_000
    max_lag = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    low = int(sys.argv[3]) if len(sys.argv) > 3 else 10 ** 9
    high = int(sys.argv[4]) if len(sys.argv) > 4 else 10 ** 12
    seed_base = int(sys.argv[5]) if len(sys.argv) > 5 else 1000

    print(f"K={k_samples} amostras por lag, faixa n em [{low}, {high}]")
    print()
    print(f"{'lag':>4} {'n_pares':>9} {'colisoes':>9} {'Pearson r':>10} {'p(corr)':>12} {'chi2':>9} {'dof':>4} {'p(chi2)':>12}  veredito")
    for k_lag in range(1, max_lag + 1):
        res = test_lag(k_lag, k_samples, low, high, seed_base + k_lag)
        sig = res["p_corr"] < 0.01 or res["p_chi2"] < 0.01
        veredito = "DEPENDENCIA" if sig else "independencia ok"
        print(f"{res['lag']:>4} {res['n_pairs']:>9} {res['collisions']:>9} "
              f"{res['r']:>10.5f} {res['p_corr']:>12.3e} "
              f"{res['chi2']:>9.1f} {res['dof']:>4} {res['p_chi2']:>12.3e}  {veredito}")


if __name__ == "__main__":
    main()
