#!/usr/bin/env python3
"""
Testa a previsao do Fable: G(v) deveria ter cauda de lei de potencia
P(G>x) ~ C(r)*x^{-alpha}, com alpha*=2 EXATO (raiz da equacao espectral
de pressao multitipo ρ(M(alpha))=1, calculada pelo Fable e estavel em
4 niveis de refinamento mod 3^k, k=1..4) - o mesmo expoente para toda
classe residual, so' a constante C(r) variando (o que explicaria a
heterogeneidade de 46x do gap de Jensen como diferenca de CONSTANTE,
nao de expoente).

Testa via estimador de Hill: alpha_hill = 1 / [(1/k) * sum(log(X_(i)/X_(k+1)))]
para as k maiores observacoes ordenadas X_(1)>=X_(2)>=...>=X_(k+1).

Reproduzir: python3 experiment_hill_tail_index.py
"""
import math
import random
import statistics

from experiment_headroom import measure_G_headroom


def hill_estimator(values, k):
    """Estimador de Hill classico para o indice de cauda, usando as k
    maiores observacoes de 'values' (lista de valores positivos)."""
    sorted_vals = sorted(values, reverse=True)
    if k >= len(sorted_vals):
        k = len(sorted_vals) - 1
    xk1 = sorted_vals[k]  # X_(k+1)
    if xk1 <= 0:
        return None
    logs = [math.log(sorted_vals[i] / xk1) for i in range(k)]
    mean_log = sum(logs) / k
    if mean_log <= 0:
        return None
    return 1.0 / mean_log


def sample_G_values(n, log_lo, log_hi, seed):
    rng = random.Random(seed)
    vals = []
    for _ in range(n):
        mag = 10 ** rng.uniform(log_lo, log_hi)
        v = int(mag) | 1
        if v % 3 == 0:
            continue
        G = measure_G_headroom(v, 20000)
        if G is not None and G > 0:
            vals.append(G)
    return vals


def sample_G_in_class(n, mod_k, target_r, log_lo, log_hi, seed):
    rng = random.Random(seed)
    vals = []
    tries = 0
    while len(vals) < n and tries < n * 200:
        tries += 1
        mag = 10 ** rng.uniform(log_lo, log_hi)
        base = int(mag)
        v = (base // mod_k) * mod_k + target_r
        if v < base:
            v += mod_k
        if v % 2 == 1 and v % 3 != 0:
            G = measure_G_headroom(v, 20000)
            if G is not None and G > 0:
                vals.append(G)
    return vals


def main():
    print("=== Teste do indice de cauda de Hill (previsao do Fable: alpha*=2 exato) ===\n")

    print("--- Amostra global (v aleatorio, sem condicionar residuo) ---")
    n_global = 20000
    vals = sample_G_values(n_global, 5.0, 7.0, seed=555)
    print(f"n={len(vals)} amostras")
    for frac in [0.01, 0.02, 0.05, 0.10]:
        k = int(len(vals) * frac)
        alpha = hill_estimator(vals, k)
        print(f"  k={k} (top {frac*100:.0f}%): alpha_hill = {alpha:.4f}" if alpha else f"  k={k}: falhou")

    print("\n--- Por classe residual (mod 3^4=81, algumas classes especificas) ---")
    mod_k = 81
    for r in [1, 4, 13, 40, 76]:
        if r % 3 == 0:
            continue
        vals_r = sample_G_in_class(3000, mod_k, r, 6.0, 8.0, seed=1000 + r)
        if len(vals_r) < 100:
            print(f"  r={r}: amostra insuficiente ({len(vals_r)})")
            continue
        k = max(20, int(len(vals_r) * 0.05))
        alpha = hill_estimator(vals_r, k)
        print(f"  r={r}: n={len(vals_r)}  k={k}  alpha_hill={alpha:.4f}" if alpha else f"  r={r}: falhou")


if __name__ == "__main__":
    main()
