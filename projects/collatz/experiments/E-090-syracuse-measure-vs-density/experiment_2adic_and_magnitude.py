#!/usr/bin/env python3
"""
Testa as sugestoes #3 (interferencia 2-adica cruzada) e #5 (termo
residual 1/v acumulado) da lista priorizada pelo Fable - ambas com
prior baixo (o argumento estrutural do Fable prediz efeito nulo ou
desprezivel para as duas), mas "quase gratis" e servem de detector
de bug: qualquer sinal >= 0.01 dex e suspeito.

#3: usa os pares (v1, v2) do teste de pares casados (m=17, fixo) e
regride |Delta| (proxy de variancia residual) contra v1 mod 2^K, para
K em {2,3,4,5}.

#5: usa a mesma amostra, particiona por faixa de magnitude de v1 (2
decadas de range) e compara resid_var por faixa - um termo O(1/v)
preveria resid_var ~100x maior na faixa de magnitude mais baixa.

Reproduzir: python3 experiment_2adic_and_magnitude.py
"""
import math
import random
import statistics

from experiment_headroom import measure_G_headroom
from experiment_deep_pairs import sample_pair, measure_delta

M_FIXED = 17
N_PAIRS = 3000


def collect_deltas_with_covariates(m, n_pairs, seed):
    rng = random.Random(seed)
    data = []
    for _ in range(n_pairs):
        v1, v2 = sample_pair(rng, m)
        d = measure_delta(v1, v2, 20000)
        if d is not None:
            data.append((v1, d))
    return data


def test_2adic(data):
    print("=== Teste #3: dependencia 2-adica cruzada ===\n")
    for K in [2, 3, 4, 5]:
        mod_k = 2 ** K
        groups = {r: [] for r in range(mod_k)}
        for v1, d in data:
            groups[v1 % mod_k].append(d ** 2)  # d^2 como proxy de variancia local
        means = {r: statistics.mean(vals) for r, vals in groups.items() if vals}
        overall = statistics.mean(v[1] ** 2 for v in data)
        print(f"  K={K} (mod {mod_k}): variancia geral={overall:.6f}")
        for r in sorted(means):
            n = len(groups[r])
            print(f"    r={r}: var_local={means[r]:.6f}  n={n}  razao_vs_geral={means[r]/overall:.3f}")
        print()


def test_magnitude_split(data):
    print("=== Teste #5: termo residual 1/v acumulado (particao por magnitude) ===\n")
    log_mags = [math.log10(v1) for v1, d in data]
    lo, hi = min(log_mags), max(log_mags)
    mid = (lo + hi) / 2
    low_bin = [d for (v1, d), lm in zip(data, log_mags) if lm < mid]
    high_bin = [d for (v1, d), lm in zip(data, log_mags) if lm >= mid]
    var_low = statistics.pvariance(low_bin) / 2
    var_high = statistics.pvariance(high_bin) / 2
    print(f"  faixa baixa  (log10 v1 < {mid:.2f}): resid_var={var_low:.6f}  n={len(low_bin)}")
    print(f"  faixa alta   (log10 v1 >= {mid:.2f}): resid_var={var_high:.6f}  n={len(high_bin)}")
    print(f"  razao (baixa/alta) = {var_low/var_high:.3f}")
    print("  (um termo O(1/v) preveria razao ~ (10^(hi-mid))^2, ou seja, muito > 1;")
    print("   razao proxima de 1 descarta o termo 1/v como explicacao do residuo)")


def main():
    print(f"Coletando {N_PAIRS} pares em m={M_FIXED}...\n")
    data = collect_deltas_with_covariates(M_FIXED, N_PAIRS, seed=777)
    print(f"{len(data)} pares validos coletados.\n")
    test_2adic(data)
    test_magnitude_split(data)


if __name__ == "__main__":
    main()
