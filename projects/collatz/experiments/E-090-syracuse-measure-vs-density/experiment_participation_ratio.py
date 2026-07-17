#!/usr/bin/env python3
"""
Implementa a quantidade local correta proposta pelo Fable para explicar
a heterogeneidade de 46x no gap de Jensen (H-099), depois de refutar a
formulacao original da IA externa ("expoente de Kesten local") e
confirmar a previsao correta (H-104: expoente de cauda universal
alpha*=2).

Derivacao (verificada independentemente): se G|r = soma_folhas
peso_i * G_generico_i, com G_generico i.i.d. (aproximacao de campo
medio), entao:

  Var(G|r) = S2(r) * Var(G_generico)

onde S2(r) = soma_folhas peso_i^2 (a soma dos PESOS AO QUADRADO da
arvore-prefixo deterministica da classe r, truncada em profundidade m).
S1(r) = soma_folhas peso_i (a mesma arvore, pesos lineares) e' a mesma
quantidade que 3^m*mu_m(r) ja calculada em outro lugar deste projeto.

A razao de participacao PR(r) = S1(r)^2/S2(r) e' o "numero efetivo de
folhas independentes" contribuindo. Previsao do Fable: o gap de Jensen
por classe deve ser decrescente em PR(r) (ou, equivalentemente,
crescente em S2(r)/S1(r)^2 = 1/PR(r)).

Reproduzir: python3 experiment_participation_ratio.py
"""
import math
import random
import statistics

import numpy as np

from syrac_fast import syrac_distribution_np
from experiment_headroom import measure_G_headroom
from experiment import sample_odd_with_residue


def window_for_mod_k(mod_k, min_distinct=200, log_lo_base=6.0):
    log_lo = log_lo_base
    while (10 ** (log_lo + 1.0) - 10 ** log_lo) / mod_k < min_distinct:
        log_lo += 1.0
    return log_lo, log_lo + 1.0


def compute_S1_S2(m, a_max=64):
    """Recursao identica a syrac_distribution_np, mas SEM renormalizar
    (soma bruta de pesos, nao distribuicao de probabilidade), com peso
    3*2^-a por passo (identidade combinatoria exata da arvore reversa),
    calculando S1 (pesos lineares) e S2 (pesos ao quadrado) em paralelo."""
    S1 = np.array([1.0])
    S2 = np.array([1.0])
    for level in range(m):
        modulus = 3 ** (level + 1)
        x = np.arange(modulus, dtype=np.int64)
        new_S1 = np.zeros(modulus, dtype=np.float64)
        new_S2 = np.zeros(modulus, dtype=np.float64)
        mod3 = x % 3
        mask_r1 = mod3 == 1
        mask_r2 = mod3 == 2
        xs_r1 = x[mask_r1]
        xs_r2 = x[mask_r2]
        for a in range(1, a_max + 1):
            xs = xs_r1 if a % 2 == 0 else xs_r2
            if xs.size == 0:
                continue
            pow2a = pow(2, a, modulus)
            z = (pow2a * xs) % modulus
            y = (z - 1) // 3
            w = 3.0 * 2.0 ** (-a)
            new_S1[xs] += w * S1[y]
            new_S2[xs] += (w ** 2) * S2[y]
        S1, S2 = new_S1, new_S2
    return S1, S2


def sanity_check_S1_proportional_to_mu(m):
    print(f"=== Checagem: S1_m(x) e' proporcional a mu_m(x)? (m={m}) ===")
    mu = syrac_distribution_np(m)
    S1, S2 = compute_S1_S2(m)
    ratios = [S1[x] / mu[x] for x in range(len(mu)) if mu[x] > 0 and x % 3 != 0]
    print(f"  razao S1/mu: media={statistics.mean(ratios):.6f}  desvio={statistics.pstdev(ratios):.2e}")
    print("  (desvio pequeno relativo a media confirma proporcionalidade exata)\n")
    return S1, S2


def measure_jensen_gap(m, residues, n_per_class, mult, seed):
    mod_k = 3 ** m
    log_lo, log_hi = window_for_mod_k(mod_k, min_distinct=max(50, n_per_class * 3))
    rng = random.Random(seed)
    gaps = {}
    for r in residues:
        vals = []
        for _ in range(n_per_class):
            v = sample_odd_with_residue(rng, mod_k, r, log_lo, log_hi)
            if v is None:
                continue
            G = measure_G_headroom(v, mult)
            if G is not None and G > 0:
                vals.append(G)
        if len(vals) < 20:
            continue
        mean_G = statistics.mean(vals)
        mean_logG = statistics.mean(math.log(g) for g in vals)
        gap = math.log(mean_G) - mean_logG
        gaps[r] = gap
    return gaps


def main():
    M = 8
    S1, S2 = sanity_check_S1_proportional_to_mu(M)

    mod_k = 3 ** M
    all_r = [r for r in range(mod_k) if r % 3 != 0 and S1[r] > 0]
    rng0 = random.Random(42)
    sample_r = rng0.sample(all_r, min(300, len(all_r)))

    print(f"Calculando PR(r) = S1(r)^2/S2(r) para {len(sample_r)} classes (m={M})...")
    pr = {r: (S1[r] ** 2 / S2[r]) for r in sample_r}

    print(f"Medindo gap de Jensen para as mesmas {len(sample_r)} classes (headroom=2000, 150 amostras/classe)...")
    gaps = measure_jensen_gap(M, sample_r, n_per_class=150, mult=2000, seed=2026)

    common = [r for r in sample_r if r in gaps]
    print(f"\n{len(common)} classes com dados validos em ambos.\n")

    log_pr = [math.log(pr[r]) for r in common]
    gap_vals = [gaps[r] for r in common]

    n = len(common)
    mx = sum(log_pr) / n
    my = sum(gap_vals) / n
    cov = sum((x - mx) * (y - my) for x, y in zip(log_pr, gap_vals)) / n
    varx = sum((x - mx) ** 2 for x in log_pr) / n
    vary = sum((y - my) ** 2 for y in gap_vals) / n
    slope = cov / varx if varx > 0 else None
    corr = cov / math.sqrt(varx * vary) if varx > 0 and vary > 0 else None

    print(f"Regressao gap(r) ~ log(PR(r)):")
    print(f"  slope = {slope:.4f}")
    print(f"  corr = {corr:.4f}")
    print("\n(Previsao do Fable: slope negativo -- PR maior (arvore mais 'espalhada')")
    print(" deveria corresponder a gap de Jensen menor (distribuicao mais concentrada).)")

    print(f"\nEstatisticas de PR(r): min={min(pr.values()):.3f} max={max(pr.values()):.3f} "
          f"media={statistics.mean(pr.values()):.3f}")
    print(f"Estatisticas de gap(r): min={min(gap_vals):.4f} max={max(gap_vals):.4f}")


if __name__ == "__main__":
    main()
