#!/usr/bin/env python3
"""
H-111 - producao do experimento de controle de 3 bracos (especificacao
completa do Fable, ver experiment_synthetic_core.py e H-111.md).

Braco 1: sintetico i.i.d. (rho=0) - controle positivo, espera-se
colapso de variancia residual com profundidade g.
Braco 2: sintetico com acoplamento de conteudo entre subarvores irmas
(rho ajustavel) - controle negativo, espera-se piso crescente com rho.
Braco 3: arvore aritmetica real (measure_G_headroom), REMEDIDA em
mult=2000 (nao reusa os dados antigos de mult=20000 de
experiment_deep_pairs*.py - Fable foi explicito que a comparacao entre
bracos exige o MESMO mult nos tres).

Conversao de profundidade: g = m - 2 (ver docstring de
experiment_synthetic_core.py para a derivacao).

Reproduzir: python3 experiment_control_arms.py [etapa]
etapas: braco1, braco3, forma, tudo (default)
"""
import math
import random
import statistics
import sys
import time

from experiment_headroom import measure_G_headroom
from experiment_synthetic_core import run_synth_pairs_with_ci

MULT = 2000
M_GRID = [8, 11, 14, 17, 20, 23, 26, 29]
G_GRID = [m - 2 for m in M_GRID]

# janelas de magnitude de v1 por m, mesmo criterio de experiment_deep_pairs*.py
# (v1 >> 3^m para manter diferenca relativa alvo ~1% controlavel)
LOG_WINDOWS = {
    8: (12.5, 13.5), 11: (12.5, 13.5), 14: (12.5, 13.5),
    17: (12.5, 13.5), 20: (12.5, 13.5), 23: (12.5, 13.5),
    26: (14.3, 15.3), 29: (15.8, 16.8),
}
TARGET_REL_DIFF = 0.01


def sample_pair_real(rng, m, log_lo, log_hi):
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


def measure_delta_real(v1, v2, mult):
    G1 = measure_G_headroom(v1, mult)
    G2 = measure_G_headroom(v2, mult)
    if G1 is None or G2 is None or G1 <= 0 or G2 <= 0:
        return None
    return math.log10(G2) - math.log10(G1)


def run_real_for_m(m, n_pairs, mult, seed):
    log_lo, log_hi = LOG_WINDOWS[m]
    rng = random.Random(seed)
    deltas = []
    for _ in range(n_pairs):
        v1, v2 = sample_pair_real(rng, m, log_lo, log_hi)
        d = measure_delta_real(v1, v2, mult)
        if d is not None:
            deltas.append(d)
    if len(deltas) < 10:
        return None
    resid_var = statistics.pvariance(deltas) / 2
    return {"resid_var": resid_var, "n": len(deltas)}


def bootstrap_ci_from_deltas(deltas, n_boot=1000, seed=0):
    rng = random.Random(seed)
    n = len(deltas)
    boots = []
    for _ in range(n_boot):
        sample = [deltas[rng.randrange(n)] for _ in range(n)]
        boots.append(statistics.pvariance(sample) / 2)
    boots.sort()
    return boots[int(0.025 * n_boot)], boots[int(0.975 * n_boot) - 1]


def run_real_for_m_with_ci(m, n_pairs, mult, seed):
    log_lo, log_hi = LOG_WINDOWS[m]
    rng = random.Random(seed)
    deltas = []
    for _ in range(n_pairs):
        v1, v2 = sample_pair_real(rng, m, log_lo, log_hi)
        d = measure_delta_real(v1, v2, mult)
        if d is not None:
            deltas.append(d)
    if len(deltas) < 10:
        return None
    resid_var = statistics.pvariance(deltas) / 2
    lo, hi = bootstrap_ci_from_deltas(deltas, seed=seed + 1)
    return {"resid_var": resid_var, "ci_lo": lo, "ci_hi": hi, "n": len(deltas), "deltas": deltas}


def stage_braco1(n_pairs=2000):
    print(f"=== Braco 1 (sintetico i.i.d., rho=0) - grade completa, mult={MULT} ===", flush=True)
    t0 = time.time()
    results = {}
    for m, g in zip(M_GRID, G_GRID):
        res = run_synth_pairs_with_ci(g=g, mult=MULT, rho=0.0, n_pairs=n_pairs, seed=3000 + m)
        results[m] = res
        print(f"  [{time.time()-t0:6.1f}s] m={m:>3} g={g:>3}  resid_var={res['resid_var']:.5f}  "
              f"IC95=[{res['ci_lo']:.5f},{res['ci_hi']:.5f}]  n={res['n']}  frac_sat={res['frac_sat']:.3f}",
              flush=True)
    return results


def stage_braco3(n_pairs=2000):
    print(f"=== Braco 3 (arvore real, remedida) - grade completa, mult={MULT} ===", flush=True)
    t0 = time.time()
    results = {}
    for m in M_GRID:
        res = run_real_for_m_with_ci(m, n_pairs=n_pairs, mult=MULT, seed=4000 + m)
        results[m] = res
        print(f"  [{time.time()-t0:6.1f}s] m={m:>3}  resid_var={res['resid_var']:.5f}  "
              f"IC95=[{res['ci_lo']:.5f},{res['ci_hi']:.5f}]  n={res['n']}", flush=True)
    return results


def stage_forma(n_pairs=1000):
    print(f"=== Rodada de forma (braco 2) - rho grosseiro x grade completa, mult={MULT} ===", flush=True)
    t0 = time.time()
    rhos = [0.0, 0.1, 0.4, 1.0]
    results = {}
    for rho in rhos:
        for m, g in zip(M_GRID, G_GRID):
            res = run_synth_pairs_with_ci(g=g, mult=MULT, rho=rho, n_pairs=n_pairs, seed=5000 + m + int(rho * 1000))
            results[(rho, m)] = res
            print(f"  [{time.time()-t0:6.1f}s] rho={rho:.1f} m={m:>3} g={g:>3}  "
                  f"resid_var={res['resid_var']:.5f}  IC95=[{res['ci_lo']:.5f},{res['ci_hi']:.5f}]  "
                  f"n={res['n']}  frac_sat={res['frac_sat']:.3f}", flush=True)
    return results


SLOPE_M_GRID = [11, 14, 17, 20]
SLOPE_RHOS = [0.0, 0.05, 0.1, 0.2]
EXCESS_M_GRID = [14, 17, 20]  # m=8,11 excluidos (Fable: null mal casado em g raso)


def bootstrap_excess_ci(deltas_synth, deltas_real, n_boot=2000, seed=0):
    """IC do excesso (var_real-var_synth) via bootstrap casado por seed
    (mesma sequencia de indices de reamostragem usada nos dois lados a
    cada iteracao b, conforme especificado pelo Fable)."""
    rng = random.Random(seed)
    n_s, n_r = len(deltas_synth), len(deltas_real)
    boots = []
    for _ in range(n_boot):
        idx_s = [rng.randrange(n_s) for _ in range(n_s)]
        idx_r = [rng.randrange(n_r) for _ in range(n_r)]
        var_s = statistics.pvariance([deltas_synth[i] for i in idx_s]) / 2
        var_r = statistics.pvariance([deltas_real[i] for i in idx_r]) / 2
        boots.append(var_r - var_s)
    boots.sort()
    point = statistics.pvariance(deltas_real) / 2 - statistics.pvariance(deltas_synth) / 2
    lo = boots[int(0.025 * n_boot)]
    hi = boots[int(0.975 * n_boot) - 1]
    return point, lo, hi


def stage_slope(n_pairs=4000):
    """Rodada de slope: rho pequeno (0,0.05,0.1,0.2) x m={11,14,17,20},
    n=4000/ponto, mult=2000 - especificacao exata do Fable apos
    descobrir contaminacao por saturacao na rodada de forma original
    (rho alto + m profundo e' intratavel E desnecessario; so o slope
    perto de rho=0 importa para o limite de rho_eff)."""
    print(f"=== Rodada de slope: rho pequeno x m={SLOPE_M_GRID}, n={n_pairs}, mult={MULT} ===", flush=True)
    t0 = time.time()
    synth_results = {}
    for rho in SLOPE_RHOS:
        for m in SLOPE_M_GRID:
            g = m - 2
            res = run_synth_pairs_with_ci(g=g, mult=MULT, rho=rho, n_pairs=n_pairs,
                                           seed=6000 + m + int(rho * 10000))
            synth_results[(rho, m)] = res
            print(f"  [{time.time()-t0:6.1f}s] SYNTH rho={rho:.2f} m={m:>3}  "
                  f"var={res['resid_var']:.5f}  IC95=[{res['ci_lo']:.5f},{res['ci_hi']:.5f}]  "
                  f"n={res['n']}  frac_sat={res['frac_sat']:.3f}", flush=True)

    print(f"\n=== Braco 3 (real) remedido para o mesmo n={n_pairs}, m={SLOPE_M_GRID} ===", flush=True)
    real_results = {}
    for m in SLOPE_M_GRID:
        res = run_real_for_m_with_ci(m, n_pairs=n_pairs, mult=MULT, seed=7000 + m)
        real_results[m] = res
        print(f"  [{time.time()-t0:6.1f}s] REAL  m={m:>3}  var={res['resid_var']:.5f}  "
              f"IC95=[{res['ci_lo']:.5f},{res['ci_hi']:.5f}]  n={res['n']}", flush=True)

    print("\n=== Slope dVar/drho perto de rho=0 (regressao linear simples) ===", flush=True)
    slopes = {}
    for m in SLOPE_M_GRID:
        xs = SLOPE_RHOS
        ys = [synth_results[(rho, m)]["resid_var"] for rho in SLOPE_RHOS]
        n = len(xs)
        mx = sum(xs) / n
        my = sum(ys) / n
        cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
        varx = sum((x - mx) ** 2 for x in xs)
        slope = cov / varx
        slopes[m] = slope
        print(f"  m={m:>3}: pontos={list(zip(xs,[round(y,5) for y in ys]))}  slope={slope:.5f}", flush=True)

    print("\n=== Excesso (real-sintetico rho=0) via bootstrap casado, e limite de rho_eff ===", flush=True)
    for m in EXCESS_M_GRID:
        deltas_synth = synth_results[(0.0, m)]["deltas"]
        deltas_real = real_results[m]["deltas"]
        point, lo, hi = bootstrap_excess_ci(deltas_synth, deltas_real, seed=8000 + m)
        slope = slopes[m]
        rho_eff_upper = hi / slope if slope > 0 else float("inf")
        print(f"  m={m:>3}: excesso={point:+.5f}  IC95=[{lo:+.5f},{hi:+.5f}]  "
              f"slope={slope:.5f}  rho_eff_upper95={rho_eff_upper:.4f}", flush=True)

    print(f"\n=== Slope/excesso concluido em {time.time()-t0:.1f}s ===")


if __name__ == "__main__":
    stage = sys.argv[1] if len(sys.argv) > 1 else "tudo"
    if stage in ("braco1", "tudo"):
        stage_braco1()
    if stage in ("braco3", "tudo"):
        stage_braco3()
    if stage in ("forma",):
        stage_forma()
    if stage in ("slope", "tudo"):
        stage_slope()
