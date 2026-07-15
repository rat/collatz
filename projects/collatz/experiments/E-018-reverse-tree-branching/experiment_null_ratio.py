#!/usr/bin/env python3
"""
E-018e - Null correto para o angulo 1 do brainstorm (o primeiro teste,
experiment_random_roots.py, foi pego pelo advisor como confundido: media
D(w1)/D(w4) e um decaimento DENTRO da mesma raiz, com um parametro livre
"3 posicoes" escolhido a dedo para bater com as observacoes anteriores, e
nao o mesmo objeto que as 9 razoes medidas de H-013, que comparam ENTRE
duas raizes diferentes).

Este script mede o objeto CERTO: D(m')/D(m) para m impar aleatorio (m=1
mod3) e m'=4m+1 - a MESMA relacao exata que liga J_t a J_{t+1}
(verificado algebricamente: 4*(4^t-1)/3+1 = (4^(t+1)-1)/3 = J_{t+1}).
Isso reproduz o mesmo tipo de razao que as 9 medidas de H-013 sem
parametro livre nem confusao dentro/entre-raizes.

Reproduzir: python3 experiment_null_ratio.py [N_AMOSTRAS] [SEED] [BUDGET_BITS]
"""
import sys
import random
import math
from experiment_dfs import build_tree_count_dfs


def sample_root(rng, mag_min, mag_max):
    """m impar, m=1 mod3 (mesma classe do "primeiro do par", como J_t nao-esteril com t=1 mod3)."""
    while True:
        m = rng.randrange(mag_min, mag_max) | 1
        if m % 3 == 1:
            return m


def main():
    n_samples = int(sys.argv[1]) if len(sys.argv) > 1 else 500
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    budget_bits = int(sys.argv[3]) if len(sys.argv) > 3 else 18

    rng = random.Random(seed)
    mag_min, mag_max = 10 ** 5, 10 ** 6

    ratios = []
    failures = 0

    for idx in range(n_samples):
        m = sample_root(rng, mag_min, mag_max)
        m2 = 4 * m + 1
        n_max = m * (2 ** budget_bits)
        search_bound = n_max * 5
        _, d_m, _ = build_tree_count_dfs(m, n_max, search_bound)
        _, d_m2, _ = build_tree_count_dfs(m2, n_max, search_bound)
        if d_m == 0 or d_m2 == 0:
            failures += 1
            continue
        ratios.append(d_m2 / d_m)

    print(f"amostras validas = {len(ratios)} de {n_samples} tentadas ({failures} falhas)")
    logs = sorted(math.log10(r) for r in ratios)
    n = len(logs)
    mean_log = sum(logs) / n
    var_log = sum((x - mean_log) ** 2 for x in logs) / n
    std_log = math.sqrt(var_log)

    print(f"razao D(4m+1)/D(m): min={10**logs[0]:.4g}  max={10**logs[-1]:.4g}")
    print(f"media geometrica = {10**mean_log:.4g}  (log10 medio = {mean_log:.4f})")
    print(f"desvio padrao em log10 = {std_log:.4f} dex")
    print()
    print("--- percentis ---")
    for p in [5, 10, 25, 50, 75, 90, 95]:
        idx = min(n - 1, int(p / 100 * n))
        print(f"  p{p:2d} = {10**logs[idx]:.4g}")

    print()
    print("--- comparacao com os 9 pares J_t medidos ---")
    razoes_jt = [1.594, 5.972, 0.0648, 0.2825, 0.7745, 0.0459, 0.1592, 3.610, 0.1473]
    logs_jt = [math.log10(r) for r in razoes_jt]
    n_jt = len(razoes_jt)
    mean_jt = sum(logs_jt) / n_jt
    var_jt = sum((x - mean_jt) ** 2 for x in logs_jt) / n_jt
    std_jt = math.sqrt(var_jt)
    se_jt = std_jt / math.sqrt(2 * (n_jt - 1))
    print(f"  9 razoes J_t: geomedia={10**mean_jt:.4g}  desvio_log10={std_jt:.4f} dex  (erro padrao do desvio ~{se_jt:.4f} dex, n={n_jt})")
    print(f"  {n} razoes nulas D(4m+1)/D(m): geomedia={10**mean_log:.4g}  desvio_log10={std_log:.4f} dex")


if __name__ == "__main__":
    main()
