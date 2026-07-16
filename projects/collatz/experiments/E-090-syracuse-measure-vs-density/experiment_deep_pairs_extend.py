#!/usr/bin/env python3
"""
Extensao de experiment_deep_pairs.py para m=26 e m=29 (v1 ajustado por
m para manter a diferenca relativa alvo, já que 3^m cresce e exige v1
maior). Reaproveita os resultados de m=8..23 já obtidos (hardcoded
abaixo) e ajusta os modelos com todos os 8 pontos.
"""
import math
import random
import statistics

from experiment_headroom import measure_G_headroom

MULT = 20000
TARGET_REL_DIFF = 0.01


def sample_pair(rng, m, log_lo, log_hi):
    pow3m = 3 ** m
    while True:
        mag = 10 ** rng.uniform(log_lo, log_hi)
        v1 = int(mag) | 1
        if v1 % 3 == 0:
            continue
        t_target = max(1, round(TARGET_REL_DIFF * v1 / pow3m))
        t = t_target if t_target % 2 == 0 else t_target + 1
        if t == 0:
            t = 2
        v2 = v1 + t * pow3m
        if v2 % 2 == 1 and v2 % 3 != 0:
            return v1, v2


def measure_delta(v1, v2, mult):
    G1 = measure_G_headroom(v1, mult)
    G2 = measure_G_headroom(v2, mult)
    if G1 is None or G2 is None or G1 <= 0 or G2 <= 0:
        return None
    return math.log10(G2) - math.log10(G1)


def run_for_m(m, n_pairs, log_lo, log_hi, seed):
    rng = random.Random(seed)
    deltas = []
    rel_diffs = []
    for _ in range(n_pairs):
        v1, v2 = sample_pair(rng, m, log_lo, log_hi)
        d = measure_delta(v1, v2, MULT)
        if d is not None:
            deltas.append(d)
            rel_diffs.append((v2 - v1) / v1)
    var_delta = statistics.pvariance(deltas)
    residual_var = var_delta / 2
    residual_std = math.sqrt(residual_var)
    return residual_std, residual_var, statistics.mean(rel_diffs), len(deltas)


PREVIOUS = {
    8: 0.032717, 11: 0.020145, 14: 0.015156,
    17: 0.011269, 20: 0.007393, 23: 0.005077,
}


def main():
    print("=== Extensao: m=26 e m=29 ===\n")
    extended = dict(PREVIOUS)
    for m, (log_lo, log_hi) in [(26, (14.3, 15.3)), (29, (15.8, 16.8))]:
        resid_std, resid_var, mean_rel_diff, n = run_for_m(m, 500, log_lo, log_hi, seed=200 + m)
        extended[m] = resid_var
        print(f"m={m:>3}  resid_std={resid_std:.4f}  resid_var={resid_var:.6f}  "
              f"diff_rel_media={mean_rel_diff*100:.3f}%  n={n}")

    ms = sorted(extended)
    variances = [extended[m] for m in ms]
    print("\n=== Todos os pontos (m, resid_var) ===")
    for m, v in zip(ms, variances):
        print(f"  m={m:>3}  var={v:.6f}  std={math.sqrt(v):.4f}")

    from experiment_deep_pairs import fit_models
    print("\n=== Ajuste de modelos com todos os 8 pontos ===")
    best = fit_models(ms, variances)
    for name, vals in best.items():
        print(f"  {name}: params={vals[:-1]}  SSE={vals[-1]:.8f}")


if __name__ == "__main__":
    main()
