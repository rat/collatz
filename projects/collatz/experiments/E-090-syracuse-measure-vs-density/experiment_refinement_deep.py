#!/usr/bin/env python3
"""
E-090/H-091 (2026-07-16, parte 6) - versao "recursos nao sao problema"
do teste de refinamento pedido pelo diretor cientifico: sera que o
resid_std do Teste A (H-091 Parte 2) estabiliza num plato conforme M
cresce, ou continua caindo (evidencia de que a exatidao pode valer no
limite)?

Melhorias sobre a versao anterior (experiment_pervalue.py):
1. mu_M calculado com syrac_fast.py (vetorizado numpy, ~30-50x mais
   rapido) - permite M ate 18 em minutos em vez de nunca terminar.
2. G(v) calculado em paralelo (multiprocessing, todos os cores) -
   permite headroom MUITO mais alto (1.000.000x) numa amostra grande
   (30.000 v's) em tempo de execucao razoavel.
3. Amostra 10x maior que o teste anterior (30.000 vs 2.997 v's) -
   reduz o erro-padrao da regressao proporcionalmente a 1/sqrt(n).
4. Reextende tambem o teste B (convergencia pareada) ate headroom=
   1.000.000, numa sub-amostra.

Reproduzir: python3 experiment_refinement_deep.py
"""
import math
import random
import statistics
import time
from multiprocessing import Pool

from experiment_headroom import measure_G_headroom
from syrac_fast import syrac_distribution_np


def sample_random_odd(rng, log_lo, log_hi):
    while True:
        mag = int(10 ** rng.uniform(log_lo, log_hi))
        v = mag | 1
        if v % 3 != 0:
            return v


def _worker(args):
    v, mult = args
    return v, measure_G_headroom(v, mult)


def compute_G_parallel(vs, mult, n_workers=16):
    with Pool(n_workers) as pool:
        results = pool.map(_worker, [(v, mult) for v in vs], chunksize=max(1, len(vs) // (n_workers * 4)))
    return {v: G for v, G in results if G is not None and G > 0}


def linreg(xs, ys):
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / n
    varx = sum((x - mx) ** 2 for x in xs) / n
    vary = sum((y - my) ** 2 for y in ys) / n
    b = cov / varx if varx > 0 else None
    a = my - b * mx if b is not None else None
    corr = cov / math.sqrt(varx * vary) if varx > 0 and vary > 0 else None
    resid = [y - (a + b * x) for x, y in zip(xs, ys)] if b is not None else []
    return {"b": b, "a": a, "corr": corr, "resid_std": statistics.pstdev(resid) if resid else None, "n": n}


def test_A_refinement_deep(vs, G_by_v, M_list, a_max=64):
    print("=== Teste A (aprofundado): resid_std estabiliza num plato conforme M cresce? ===\n")
    print(f"{'M':>3} {'b':>8} {'intercepto':>11} {'resid_std':>10} {'corr':>8} {'t_mu_build':>10}")
    results = []
    for M in M_list:
        t0 = time.time()
        mu = syrac_distribution_np(M, a_max=a_max)
        t_mu = time.time() - t0
        mod_k = 3 ** M
        xs, ys = [], []
        for v, G in G_by_v.items():
            r = v % mod_k
            if r % 3 == 0 or mu[r] <= 0:
                continue
            xs.append(math.log10(mod_k * mu[r]))
            ys.append(math.log10(G))
        fit = linreg(xs, ys)
        results.append((M, fit))
        print(f"{M:>3} {fit['b']:8.4f} {fit['a']:11.4f} {fit['resid_std']:10.4f} {fit['corr']:8.4f} {t_mu:10.1f}s  (n={fit['n']})")
    return results


def test_B_paired_headroom_deep(vs, headrooms):
    print("\n=== Teste B (aprofundado): G(v) converge conforme headroom cresce ate 1.000.000x? ===\n")
    G_by_h = {}
    for h in headrooms:
        t0 = time.time()
        G_by_h[h] = compute_G_parallel(vs, h)
        print(f"  headroom={h:>8}: {len(G_by_h[h])} v's medidos em {time.time()-t0:.1f}s")

    print(f"\n{'H1->H2':>18} {'mean(Delta) dex':>16} {'std(Delta) dex':>15} {'n':>6}")
    for h1, h2 in zip(headrooms, headrooms[1:]):
        deltas = []
        for v in vs:
            if v in G_by_h[h1] and v in G_by_h[h2]:
                deltas.append(math.log10(G_by_h[h2][v]) - math.log10(G_by_h[h1][v]))
        if deltas:
            print(f"{h1:>7}->{h2:<9} {statistics.mean(deltas):16.5f} {statistics.pstdev(deltas):15.5f} {len(deltas):>6}")
    return G_by_h


def main():
    t_start = time.time()
    rng = random.Random(2026)

    # --- Teste B estendido (subamostra, ate headroom=1e6) ---
    N_V_B = 5000
    vs_b = list(dict.fromkeys(sample_random_odd(rng, 6.0, 8.0) for _ in range(N_V_B)))
    print(f"Teste B: {len(vs_b)} v's distintos (log10 v em [6,8))")
    headrooms_b = [200, 2000, 20000, 100000, 1000000]
    test_B_paired_headroom_deep(vs_b, headrooms_b)

    # --- Teste A aprofundado (amostra grande, headroom=1e6) ---
    N_V_A = 30000
    vs_a = list(dict.fromkeys(sample_random_odd(rng, 6.0, 8.0) for _ in range(N_V_A)))
    print(f"\nTeste A: {len(vs_a)} v's distintos (log10 v em [6,8)), headroom=1.000.000")
    t0 = time.time()
    G_by_v = compute_G_parallel(vs_a, 1_000_000)
    print(f"  G(v) computado para {len(G_by_v)} v's em {time.time()-t0:.1f}s\n")

    M_list = [4, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    test_A_refinement_deep(list(G_by_v.keys()), G_by_v, M_list)

    print(f"\nTempo total: {time.time()-t_start:.1f}s")


if __name__ == "__main__":
    main()
