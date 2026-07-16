#!/usr/bin/env python3
"""
E-090 (extensao 2026-07-16) - responde as 3 perguntas deixadas em aberto
por H-090:

  1. A correlacao log-log entre 3^m*mu_m(r) e G(v) medido converge a 1,0
     conforme m cresce, ou estabiliza abaixo disso?
  2. E proporcionalidade exata (constante c universal por residuo) ou so
     tendencia geral com residuo sistematico nao explicado?
  3. (tratada em experiment_bridge.py / consulta ao Fable) - ha uma ponte
     teorica real entre a recursao de Tao (orbita direta) e a densidade
     da arvore reversa, ou e so coincidencia algebrica das duas equacoes?

Reutiliza a infraestrutura ja validada de experiment.py (syrac_distribution,
syrac_distribution_float, measure_G, build_tree_count_dfs).

Reproduzir: python3 experiment_extended.py
"""
import math
import random
import statistics

from experiment import (
    syrac_distribution_float,
    measure_G,
    sample_odd_with_residue,
    log_log_correlation,
)


def measure_mean_G_by_residue_adaptive(m, n_samples_per_residue, seed=1):
    """Como measure_mean_G_by_residue, mas escolhe a janela de magnitude
    adaptativamente para garantir mod_k=3^m << faixa de busca (evita
    desperdicio de tentativas em sample_odd_with_residue para m grande)."""
    rng = random.Random(seed)
    mod_k = 3 ** m
    log_mod_k = math.log10(mod_k)
    log_mag_lo = max(5.0, log_mod_k + 0.3)
    log_mag_hi = log_mag_lo + 1.0

    results = {}
    for r in range(mod_k):
        if r % 3 == 0:
            continue
        logs = []
        for _ in range(n_samples_per_residue):
            v = sample_odd_with_residue(rng, mod_k, r, log_mag_lo, log_mag_hi)
            if v is None:
                continue
            n_max = v * 20
            G = measure_G(v, n_max)
            if G is not None and G > 0:
                logs.append(math.log10(G))
        if logs:
            mean_log = sum(logs) / len(logs)
            results[r] = 10 ** mean_log
    return results, (log_mag_lo, log_mag_hi)


def residual_dispersion(m, mean_G, mu):
    """Para cada residuo r, calcula log10(G_medio(r)) - log10(3^m*mu(r))
    (o residuo depois de explicar G por mu). Retorna (mean, std, n) desse
    residuo em log10 - dispersao baixa e decrescente com m => mu explica
    G cada vez melhor (tendendo a proporcionalidade exata); dispersao que
    nao cai => componente real nao explicado por mu."""
    mod_k = 3 ** m
    diffs = []
    for r in mean_G:
        if mu.get(r, 0) <= 0:
            continue
        pred = mod_k * mu[r]
        diffs.append(math.log10(mean_G[r]) - math.log10(pred))
    if len(diffs) < 5:
        return None, None, len(diffs)
    return statistics.mean(diffs), statistics.pstdev(diffs), len(diffs)


def main():
    print("=== Extensao H-090: correlacao e dispersao residual vs. m ===\n")
    print(f"{'m':>3} {'mod_k':>8} {'n_res':>6} {'corr':>8} {'resid_mean':>11} {'resid_std':>10}")

    n_per_residue_by_m = {
        2: 2000, 3: 1000, 4: 500, 5: 300, 6: 150,
        7: 80, 8: 40, 9: 20, 10: 10, 11: 6, 12: 3,
    }

    rows = []
    for m in range(2, 13):
        n_per_residue = n_per_residue_by_m.get(m, 3)
        mu = syrac_distribution_float(m, a_max=64)
        mean_G, (lo, hi) = measure_mean_G_by_residue_adaptive(m, n_per_residue, seed=42)

        common_r = [r for r in mean_G if r % 3 != 0 and mu.get(r, 0) > 0]
        mod_k = 3 ** m
        xs = [mod_k * mu[r] for r in common_r]
        ys = [mean_G[r] for r in common_r]
        corr = log_log_correlation(xs, ys) if len(xs) >= 5 else None

        rmean, rstd, rn = residual_dispersion(m, mean_G, mu)

        rows.append((m, mod_k, len(common_r), corr, rmean, rstd, lo, hi))
        corr_s = f"{corr:.4f}" if corr is not None else "n/a"
        rmean_s = f"{rmean:.4f}" if rmean is not None else "n/a"
        rstd_s = f"{rstd:.4f}" if rstd is not None else "n/a"
        print(f"{m:>3} {mod_k:>8} {len(common_r):>6} {corr_s:>8} {rmean_s:>11} {rstd_s:>10}  (log_mag [{lo:.2f},{hi:.2f}])")

    print("\n=== Interpretacao ===")
    print("corr -> 1.0 conforme m cresce?  resid_std -> 0 conforme m cresce?")
    return rows


if __name__ == "__main__":
    main()
