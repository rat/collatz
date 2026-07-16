#!/usr/bin/env python3
"""
E-090/H-091 (2026-07-16, parte 5) - testes decisivos propostos pelo
Fable apos ele apontar que o stress test anterior (experiment_stress.py)
nao era pareado (n_per_residue variava com o headroom, mudando a janela
e a sequencia do RNG - v's diferentes em cada nivel de headroom, o que
inflava o erro-padrao da comparacao entre niveis).

Aqui os testes sao feitos POR v individual (G(v) e determinístico dado
v e o headroom - nao ha ruido de medicao por v), evitando totalmente o
problema de pareamento: usamos o MESMO conjunto de v's em todos os
niveis de headroom e em todos os niveis de resolucao M de mu.

Teste A (refinamento): regride log G(v) contra log(3^M*mu_M(v mod 3^M))
por v individual, para M crescente (nao agregado por classe) - se o
excesso de dispersao vem de estrutura de digitos alem de M, deve
encolher conforme M cresce.

Teste B (convergencia pareada entre headrooms): mede Delta(v) =
log G_H2(v) - log G_H1(v) para o MESMO v em headrooms H1<H2 crescentes
geometricamente - se G(v) esta convergindo (existencia do limite de
escala), Delta deve encolher para 0 conforme H1,H2 crescem.

Reproduzir: python3 experiment_pervalue.py
"""
import math
import random
import statistics

from experiment import syrac_distribution_float
from experiment_headroom import measure_G_headroom


def sample_random_odd(rng, log_lo, log_hi):
    while True:
        mag = int(10 ** rng.uniform(log_lo, log_hi))
        v = mag | 1
        if v % 3 != 0:
            return v


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


def test_A_refinement(vs, G_by_v, M_list, a_max=64):
    print("=== Teste A (Fable): refinamento em M explica o excesso de dispersao? ===")
    print("(por v individual, sem agregar por classe - G(v) e' deterministico)\n")
    print(f"{'M':>3} {'b':>8} {'intercepto':>11} {'resid_std':>10} {'corr':>8}")
    for M in M_list:
        mu = syrac_distribution_float(M, a_max=a_max)
        mod_k = 3 ** M
        xs, ys = [], []
        for v in vs:
            r = v % mod_k
            if r % 3 == 0 or mu.get(r, 0) <= 0:
                continue
            xs.append(math.log10(mod_k * mu[r]))
            ys.append(math.log10(G_by_v[v]))
        fit = linreg(xs, ys)
        print(f"{M:>3} {fit['b']:8.4f} {fit['a']:11.4f} {fit['resid_std']:10.4f} {fit['corr']:8.4f}  (n={fit['n']})")
    print()


def test_B_paired_headroom(vs, headrooms):
    print("=== Teste B (Fable): G(v) converge conforme headroom cresce (mesmo v)? ===\n")
    G_by_h = {}
    for h in headrooms:
        G_by_h[h] = {}
        for v in vs:
            G = measure_G_headroom(v, h)
            if G is not None and G > 0:
                G_by_h[h][v] = G

    print(f"{'H1->H2':>15} {'mean(Delta) dex':>16} {'std(Delta) dex':>15} {'n':>6}")
    for h1, h2 in zip(headrooms, headrooms[1:]):
        deltas = []
        for v in vs:
            if v in G_by_h[h1] and v in G_by_h[h2]:
                deltas.append(math.log10(G_by_h[h2][v]) - math.log10(G_by_h[h1][v]))
        if deltas:
            print(f"{h1:>6}->{h2:<6} {statistics.mean(deltas):16.5f} {statistics.pstdev(deltas):15.5f} {len(deltas):>6}")
    print()
    return G_by_h


def main():
    N_V = 3000
    rng = random.Random(123)
    vs = [sample_random_odd(rng, 6.0, 7.0) for _ in range(N_V)]
    vs = list(dict.fromkeys(vs))  # remove duplicatas mantendo ordem
    print(f"Amostrados {len(vs)} v's distintos (log10 v em [6,7))\n")

    headrooms = [200, 2000, 20000, 100000]
    G_by_h = test_B_paired_headroom(vs, headrooms)

    # usa o headroom mais alto (mais preciso) para o teste de refinamento
    best_h = headrooms[-1]
    G_by_v = G_by_h[best_h]
    vs_ok = [v for v in vs if v in G_by_v]
    print(f"Teste A usando headroom={best_h} (mais preciso), n={len(vs_ok)}\n")
    test_A_refinement(vs_ok, G_by_v, M_list=[4, 6, 8, 10, 12, 14])


if __name__ == "__main__":
    main()
