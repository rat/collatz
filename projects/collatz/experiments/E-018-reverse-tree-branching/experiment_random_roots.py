#!/usr/bin/env python3
"""
E-018d - Angulo 1 do brainstorm (agente rodando Opus, pedido explicito do
diretor cientifico para propor e testar novos angulos sobre a oscilacao de
H-013/H-018): distribuicao empirica da razao de decaimento D(w_1)/D(w_4)
(galhos de mesma fase mod3, 3 posicoes de distancia - Teorema 2 de
experiment_decompose.py) sobre MUITAS raizes impares ALEATORIAS, nao so a
familia J_t.

Motivacao: medimos que a taxa de decaimento entre galhos ferteis da mesma
fase varia 73x (t=13) a 680x (t=10), sem explicacao via t mod9 (a fase em
si). Pergunta: essa faixa e ela mesma tipica de um processo de ramificacao
generico? Reformula "por que este valor especifico" (bloqueado por H-024,
exige precisao 3-adica ilimitada) para "essa oscilacao e surpreendente
dado o que se espera do processo" - respondivel estatisticamente sem
fechar H-024.

Reproduzir: python3 experiment_random_roots.py [N_AMOSTRAS] [SEED] [BUDGET_BITS]
"""
import sys
import random
import math
from experiment_decompose import decompose


def sample_root(rng, mag_min, mag_max):
    """Raiz impar aleatoria, nao-esteril (m%3!=0), em [mag_min, mag_max)."""
    while True:
        m = rng.randrange(mag_min, mag_max) | 1
        if m % 3 != 0:
            return m


def main():
    n_samples = int(sys.argv[1]) if len(sys.argv) > 1 else 500
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    budget_bits = int(sys.argv[3]) if len(sys.argv) > 3 else 18

    rng = random.Random(seed)
    mag_min, mag_max = 10 ** 5, 10 ** 6  # ordem de grandeza comparavel a J_10/J_11

    ratios = []
    n_sterile_w1 = 0
    n_sterile_w4 = 0
    failures = 0

    for idx in range(n_samples):
        m = sample_root(rng, mag_min, mag_max)
        n_max = m * (2 ** budget_bits)
        search_bound = n_max * 5
        total, buckets, w_list = decompose(m, n_max, search_bound)
        if len(w_list) < 4:
            failures += 1
            continue
        d1 = buckets.get(1, 0)
        d4 = buckets.get(4, 0)
        if d1 == 0 or d4 == 0:
            failures += 1
            continue
        if d1 == 1:
            n_sterile_w1 += 1
        if d4 == 1:
            n_sterile_w4 += 1
        # Pelo Teorema 2 (periodicidade mod3 com periodo 3), galho1 e galho4
        # tem a MESMA fase - se um e esteril (w%3==0), o outro tambem e,
        # SEMPRE, dando razao=1 trivialmente (nao carrega informacao sobre
        # decaimento). Guardamos a razao completa (para checagem) mas
        # separamos os casos genuinamente-ferteis para a analise real.
        ratios.append((d1, d4, d1 / d4))

    n_ferteis = sum(1 for d1, d4, r in ratios if d1 > 1)
    print(f"amostras validas = {len(ratios)} de {n_samples} tentadas ({failures} falhas/incompletas)")
    print(f"galho1 esteril em {n_sterile_w1}/{len(ratios)}, galho4 esteril em {n_sterile_w4}/{len(ratios)}")
    print(f"(esperado ~1/3 cada, pelo Teorema 2 - e por periodicidade, sterile(w1)=sterile(w4) SEMPRE juntos)")
    print(f"amostras com fase FERTIL (d1>1, as unicas que carregam informacao real de decaimento) = {n_ferteis}")
    print()

    # análise só nos casos genuinamente férteis (exclui a degenerescência
    # ratio=1 forçada quando a fase e esteril)
    razoes_ferteis = [r for d1, d4, r in ratios if d1 > 1]
    logs = sorted(math.log10(r) for r in razoes_ferteis)
    n = len(logs)
    mean_log = sum(logs) / n
    var_log = sum((x - mean_log) ** 2 for x in logs) / n
    std_log = math.sqrt(var_log)

    print(f"razao D(w1)/D(w4): min={10**logs[0]:.4g}  max={10**logs[-1]:.4g}")
    print(f"media geometrica = {10**mean_log:.4g}  (log10 medio = {mean_log:.4f})")
    print(f"desvio padrao em log10 = {std_log:.4f} dex")
    print()
    print("--- percentis (razao D(w1)/D(w4)) ---")
    for p in [1, 5, 10, 25, 50, 75, 90, 95, 99]:
        idx = min(n - 1, int(p / 100 * n))
        print(f"  p{p:2d} = {10**logs[idx]:.4g}")

    print()
    print("--- histograma (log10 da razao D(w1)/D(w4)) ---")
    lo, hi = logs[0], logs[-1]
    nbins = 20
    width = (hi - lo) / nbins if hi > lo else 1
    bins = [0] * nbins
    for x in logs:
        b = min(nbins - 1, int((x - lo) / width))
        bins[b] += 1
    maxc = max(bins) if bins else 1
    for i, c in enumerate(bins):
        lo_edge = lo + i * width
        print(f"  [{lo_edge:+6.2f}, {lo_edge + width:+6.2f})  {'#' * (c * 60 // maxc)}  ({c})")

    print()
    print("--- comparacao com os 9 pares J_t medidos ---")
    razoes_jt = [1.594, 5.972, 0.0648, 0.2825, 0.7745, 0.0459, 0.1592, 3.610, 0.1473]
    logs_jt = [math.log10(r) for r in razoes_jt]
    mean_jt = sum(logs_jt) / len(logs_jt)
    var_jt = sum((x - mean_jt) ** 2 for x in logs_jt) / len(logs_jt)
    std_jt = math.sqrt(var_jt)
    print(f"  9 razoes J_t: media geometrica={10**mean_jt:.4g}  desvio_log10={std_jt:.4f} dex")
    print(f"  {n} razoes aleatorias (D(w1)/D(w4)): media geometrica={10**mean_log:.4g}  desvio_log10={std_log:.4f} dex")


if __name__ == "__main__":
    main()
