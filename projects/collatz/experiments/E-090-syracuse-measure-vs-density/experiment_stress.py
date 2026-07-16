#!/usr/bin/env python3
"""
E-090/H-091 (stress test 2026-07-16, parte 4) - antes de aceitar o
veredito de H-091 ("expoente converge a ~1,00 exato, headroom 200-2000
basta"), testa se isso e um limite genuino ou so um patamar de
passagem:

  1. Aumenta o headroom bem alem de 2000 (20000, 100000) - se b
     continuar se aproximando de 1,00 (ou ficar estavel), reforca a
     conclusao; se continuar se afastando ou nao estabilizar, H-091
     foi otimista demais.
  2. Reporta resid_std (dispersao residual) diretamente, nao so corr/b
     - "b~1,00" com resid_std ainda grande seria proporcionalidade "na
     media" mas com dispersao real remanescente, nao "exata" de fato.

Reproduzir: python3 experiment_stress.py
"""
import math
import random
import statistics

from experiment import syrac_distribution_float, sample_odd_with_residue
from experiment_headroom import measure_G_headroom, window_for_mod_k


def arithmetic_mean_G_by_residue(m, mult, residues, n_per_residue, seed):
    mod_k = 3 ** m
    log_lo, log_hi = window_for_mod_k(mod_k, min_distinct=max(50, n_per_residue * 3))
    rng = random.Random(seed)
    out = {}
    for r in residues:
        vals = []
        for _ in range(n_per_residue):
            v = sample_odd_with_residue(rng, mod_k, r, log_lo, log_hi)
            if v is None:
                continue
            G = measure_G_headroom(v, mult)
            if G is not None and G > 0:
                vals.append(G)
        if vals:
            out[r] = statistics.mean(vals)
    return out


def fit_and_dispersion(m, mult, n_residues_sample, n_per_residue, seed=42):
    mod_k = 3 ** m
    mu = syrac_distribution_float(m, a_max=64)
    all_r = [r for r in range(mod_k) if r % 3 != 0]
    rng0 = random.Random(7)
    sample_r = rng0.sample(all_r, min(n_residues_sample, len(all_r)))

    mean_G = arithmetic_mean_G_by_residue(m, mult, sample_r, n_per_residue, seed)
    common_r = [r for r in sample_r if mu.get(r, 0) > 0 and r in mean_G]
    if len(common_r) < 5:
        return None

    xs = [math.log10(mod_k * mu[r]) for r in common_r]
    ys = [math.log10(mean_G[r]) for r in common_r]
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / n
    varx = sum((x - mx) ** 2 for x in xs) / n
    vary = sum((y - my) ** 2 for y in ys) / n
    b = cov / varx
    corr = cov / math.sqrt(varx * vary) if varx > 0 and vary > 0 else None
    a = my - b * mx
    resid = [y - (a + b * x) for x, y in zip(xs, ys)]
    resid_std = statistics.pstdev(resid)
    # dispersao com b FIXO em 1.0 (proporcionalidade estrita, sem ajustar expoente)
    a1 = my - mx
    resid_b1 = [y - (a1 + x) for x, y in zip(xs, ys)]
    resid_std_b1 = statistics.pstdev(resid_b1)
    return corr, b, resid_std, resid_std_b1, n


def main():
    print("=== Stress test H-091: o expoente/dispersao realmente convergem, ou so passam por 1,00? ===\n")

    plan = [
        # (mult, m, n_residues_sample, n_per_residue)
        (200,    8, 400, 30),
        (200,   12, 400, 30),
        (2000,   8, 400, 20),
        (2000,  12, 400, 20),
        (20000,  8, 300, 15),
        (20000, 12, 300, 15),
        (100000, 8, 200, 8),
        (100000, 12, 200, 8),
    ]

    print(f"{'mult':>8} {'m':>3} {'corr':>8} {'b':>8} {'resid_std(b_livre)':>19} {'resid_std(b=1)':>15}")
    for mult, m, n_res, n_pr in plan:
        result = fit_and_dispersion(m, mult, n_res, n_pr)
        if result is None:
            print(f"{mult:>8} {m:>3}  dados insuficientes")
            continue
        corr, b, rstd, rstd_b1, n = result
        print(f"{mult:>8} {m:>3} {corr:8.4f} {b:8.4f} {rstd:19.4f} {rstd_b1:15.4f}  (n_res={n})")


if __name__ == "__main__":
    main()
