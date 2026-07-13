#!/usr/bin/env python3
"""
E-001 - Testa H-001: independencia entre valuacoes 2-adicas consecutivas
na orbita acelerada de Collatz T(n) = (3n+1) / 2^a(n), onde a(n) e a maior
potencia de 2 que divide 3n+1.

Controle metodologico importante: toda orbita termina numa cauda universal e
deterministica (...->8->4->2->1), identica para todas as orbitas. Se agregarmos
pares (a_i, a_{i+1}) de TODAS as posicoes de TODAS as orbitas sem cuidado, essa
cauda compartilhada contamina a estatistica com uma correlacao espuria que nada
tem a ver com a pergunta real (independencia no regime "generico", n grande).
Por isso o script reporta os resultados COM e SEM um filtro de threshold que
descarta pares onde o valor de n na orbita ja caiu abaixo de um piso minimo.

Usa somente a biblioteca padrao (sem numpy/scipy, nao disponiveis no ambiente).
Reproduzir: python3 experiment.py [N_ORBITS] [THRESHOLD] [MAX_VALUATION_BUCKET]
"""
import sys
import math
import time


def orbit_steps(n, max_steps=100_000):
    """Retorna lista de (n_antes_do_passo, a) para cada passo ate a orbita atingir 1."""
    steps = []
    while n != 1:
        n_before = n
        m = 3 * n + 1
        a = 0
        while m % 2 == 0:
            m //= 2
            a += 1
        steps.append((n_before, a))
        n = m
        if len(steps) > max_steps:
            raise RuntimeError(f"orbita nao convergiu em {max_steps} passos (n inicial={n_before})")
    return steps


def chi_square_pvalue(x, k):
    """Aproximacao de Wilson-Hilferty para p-valor (cauda superior) de chi-quadrado."""
    if k <= 0:
        return float("nan")
    z = ((x / k) ** (1 / 3) - (1 - 2 / (9 * k))) / math.sqrt(2 / (9 * k))
    return 0.5 * math.erfc(z / math.sqrt(2))


def normal_pvalue_two_sided(z):
    return math.erfc(abs(z) / math.sqrt(2))


def analyze(pairs, bucket_max, label):
    """pairs: lista de (a_i, a_{i+1}). Roda correlacao de Pearson + qui-quadrado."""
    n_pairs = len(pairs)
    if n_pairs < 100:
        print(f"[{label}] amostra insuficiente ({n_pairs} pares), pulando.")
        return

    def bucket(a):
        return a if a < bucket_max else bucket_max

    sum_x = sum_y = sum_x2 = sum_y2 = sum_xy = 0.0
    pair_counts = {}
    marginal_counts = {}

    for a_i, a_j in pairs:
        sum_x += a_i
        sum_y += a_j
        sum_x2 += a_i * a_i
        sum_y2 += a_j * a_j
        sum_xy += a_i * a_j
        key = (bucket(a_i), bucket(a_j))
        pair_counts[key] = pair_counts.get(key, 0) + 1
        marginal_counts[bucket(a_i)] = marginal_counts.get(bucket(a_i), 0) + 1

    mean_x = sum_x / n_pairs
    mean_y = sum_y / n_pairs
    cov = sum_xy / n_pairs - mean_x * mean_y
    var_x = sum_x2 / n_pairs - mean_x * mean_x
    var_y = sum_y2 / n_pairs - mean_y * mean_y
    r = cov / math.sqrt(var_x * var_y)

    z_fisher = math.atanh(max(min(r, 0.999999), -0.999999)) * math.sqrt(n_pairs - 3)
    p_corr = normal_pvalue_two_sided(z_fisher)

    buckets = sorted(marginal_counts.keys())
    row_totals = {b: 0 for b in buckets}
    col_totals = {b: 0 for b in buckets}
    for (bi, bj), c in pair_counts.items():
        row_totals[bi] = row_totals.get(bi, 0) + c
        col_totals[bj] = col_totals.get(bj, 0) + c

    chi2 = 0.0
    for bi in buckets:
        for bj in buckets:
            observed = pair_counts.get((bi, bj), 0)
            expected = row_totals.get(bi, 0) * col_totals.get(bj, 0) / n_pairs
            if expected > 0:
                chi2 += (observed - expected) ** 2 / expected
    dof = (len(buckets) - 1) ** 2
    p_chi2 = chi_square_pvalue(chi2, dof) if dof > 0 else float("nan")

    print(f"--- {label} (n_pares={n_pairs}) ---")
    print(f"  correlacao de Pearson r = {r:.5f}  (z-Fisher={z_fisher:.2f}, p={p_corr:.3e})")
    print(f"  qui-quadrado = {chi2:.1f}  (dof={dof}, p~={p_chi2:.3e})")
    if p_corr < 0.01 or (dof > 0 and p_chi2 < 0.01):
        print("  => dependencia estatisticamente significativa nesta amostra.")
    else:
        print("  => nenhuma dependencia estatisticamente significativa detectada.")
    print()


def main():
    n_orbits = int(sys.argv[1]) if len(sys.argv) > 1 else 200_000
    threshold = int(sys.argv[2]) if len(sys.argv) > 2 else 10_000
    bucket_max = int(sys.argv[3]) if len(sys.argv) > 3 else 8

    t0 = time.time()

    all_pairs = []       # todas as posicoes de todas as orbitas (sem filtro)
    filtered_pairs = []   # so pares onde n_before(a_i) >= threshold
    marginal_all = {}
    max_orbit_len = 0

    for n in range(1, 2 * n_orbits, 2):
        steps = orbit_steps(n)
        max_orbit_len = max(max_orbit_len, len(steps))

        for n_before, a in steps:
            marginal_all[a] = marginal_all.get(a, 0) + 1

        for (n_i, a_i), (n_j, a_j) in zip(steps, steps[1:]):
            all_pairs.append((a_i, a_j))
            if n_i >= threshold:
                filtered_pairs.append((a_i, a_j))

    elapsed = time.time() - t0

    print(f"n_orbits (n impares iniciais) = {n_orbits}, faixa n inicial: 1..{2 * n_orbits - 1}")
    print(f"threshold (piso de n para o filtro) = {threshold}")
    print(f"tamanho maximo de orbita observado = {max_orbit_len}")
    print(f"tempo de execucao = {elapsed:.1f}s")
    print()

    print("--- marginal de a, sem filtro (checagem: deve ~ 2^-k) ---")
    total = sum(marginal_all.values())
    for k in sorted(marginal_all):
        obs = marginal_all[k] / total
        theo = 2 ** -k
        print(f"  a={k}: observado={obs:.4f}  teorico=2^-{k}={theo:.4f}")
    print()

    analyze(all_pairs, bucket_max, "SEM FILTRO (inclui cauda universal perto de 1)")
    analyze(filtered_pairs, bucket_max, f"COM FILTRO (n_i >= {threshold}, regime generico)")


if __name__ == "__main__":
    main()
