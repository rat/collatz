#!/usr/bin/env python3
"""
Alerta do Fable (H-104): com alpha*=2 (expoente de cauda universal
confirmado), E[G^2] esta na fronteira da divergencia - gaps de Jensen
por classe podem ser dominados por poucas observacoes extremas
(ruido de cauda pesada), nao heterogeneidade estrutural real. Antes de
aceitar a correlacao gap~PR de H-105 (-0.58) como solida, testa via
bootstrap por classe: quanto da dispersao de 46x entre classes e'
ruido de estimacao (que um bootstrap revelaria como grande incerteza
por classe) vs sinal real (gap estavel entre reamostragens).

Reproduzir: python3 experiment_bootstrap_gap.py
"""
import math
import random
import statistics

from syrac_fast import syrac_distribution_np
from experiment_headroom import measure_G_headroom
from experiment import sample_odd_with_residue
from experiment_participation_ratio import compute_S1_S2, window_for_mod_k

M = 8
N_PER_CLASS = 150
N_CLASSES = 150
N_BOOTSTRAP = 1000


def collect_raw_samples(m, residues, n_per_class, mult, seed):
    mod_k = 3 ** m
    log_lo, log_hi = window_for_mod_k(mod_k, min_distinct=max(50, n_per_class * 3))
    rng = random.Random(seed)
    raw = {}
    for r in residues:
        vals = []
        for _ in range(n_per_class):
            v = sample_odd_with_residue(rng, mod_k, r, log_lo, log_hi)
            if v is None:
                continue
            G = measure_G_headroom(v, mult)
            if G is not None and G > 0:
                vals.append(G)
        if len(vals) >= 20:
            raw[r] = vals
    return raw


def gap_from_vals(vals):
    mean_G = statistics.mean(vals)
    mean_logG = statistics.mean(math.log(g) for g in vals)
    return math.log(mean_G) - mean_logG


def bootstrap_gap_std(vals, n_bootstrap, seed):
    rng = random.Random(seed)
    n = len(vals)
    gaps = []
    for _ in range(n_bootstrap):
        sample = [vals[rng.randrange(n)] for _ in range(n)]
        gaps.append(gap_from_vals(sample))
    return statistics.mean(gaps), statistics.pstdev(gaps)


def main():
    S1, S2 = compute_S1_S2(M)
    mod_k = 3 ** M
    all_r = [r for r in range(mod_k) if r % 3 != 0 and S1[r] > 0]
    rng0 = random.Random(42)
    sample_r = rng0.sample(all_r, min(N_CLASSES, len(all_r)))

    print(f"Coletando amostras brutas para {len(sample_r)} classes (m={M}, n={N_PER_CLASS}/classe)...")
    raw = collect_raw_samples(M, sample_r, N_PER_CLASS, mult=2000, seed=2026)
    print(f"{len(raw)} classes com dados validos.\n")

    print(f"=== Bootstrap ({N_BOOTSTRAP} reamostragens) por classe ===\n")
    point_gaps = {}
    boot_stds = {}
    for r, vals in raw.items():
        point_gaps[r] = gap_from_vals(vals)
        _, bstd = bootstrap_gap_std(vals, N_BOOTSTRAP, seed=r)
        boot_stds[r] = bstd

    gap_values = list(point_gaps.values())
    boot_std_values = list(boot_stds.values())

    print(f"Dispersao ENTRE classes do gap pontual: min={min(gap_values):.4f} max={max(gap_values):.4f} "
          f"desvio-padrao={statistics.pstdev(gap_values):.4f}")
    print(f"Incerteza de bootstrap DENTRO de cada classe (media dos desvios-padrao bootstrap): "
          f"{statistics.mean(boot_std_values):.4f} (min={min(boot_std_values):.4f} max={max(boot_std_values):.4f})")

    razao = statistics.pstdev(gap_values) / statistics.mean(boot_std_values)
    print(f"\nRazao (dispersao entre classes / incerteza media dentro de classe) = {razao:.3f}")
    print("(Se essa razao for grande (>>1), a heterogeneidade entre classes e' real, nao ruido.")
    print(" Se for proxima de 1, a 'heterogeneidade' pode ser majoritariamente ruido de estimacao.)")

    # correlacao gap~PR usando so' as classes com bootstrap std pequeno o suficiente
    # (excluindo as mais ruidosas, para ver se a correlacao sobrevive)
    pr = {r: (S1[r] ** 2 / S2[r]) for r in raw}
    median_bstd = statistics.median(boot_std_values)
    reliable_r = [r for r in raw if boot_stds[r] <= median_bstd]
    print(f"\n=== Correlacao gap~log(PR) usando so' as {len(reliable_r)} classes mais confiaveis (bootstrap std <= mediana) ===")
    log_pr = [math.log(pr[r]) for r in reliable_r]
    gaps_reliable = [point_gaps[r] for r in reliable_r]
    n = len(reliable_r)
    mx = sum(log_pr) / n
    my = sum(gaps_reliable) / n
    cov = sum((x - mx) * (y - my) for x, y in zip(log_pr, gaps_reliable)) / n
    varx = sum((x - mx) ** 2 for x in log_pr) / n
    vary = sum((y - my) ** 2 for y in gaps_reliable) / n
    corr = cov / math.sqrt(varx * vary) if varx > 0 and vary > 0 else None
    print(f"  corr = {corr:.4f}  (compare com -0.58 usando todas as classes em H-105)")


if __name__ == "__main__":
    main()
