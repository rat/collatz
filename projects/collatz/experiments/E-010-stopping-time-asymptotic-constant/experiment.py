#!/usr/bin/env python3
"""
E-010 - Testa H-010: total_stopping_time(n) ~ K * log2(n), com
K = 3 / (2 - log2(3)) ~= 7.2283 derivado da heuristica de passeio aleatorio
(E[a]=2, ver H-001). Ajusta regressao linear simples nos dados reais e
compara o coeficiente empirico com o teorico.

Reproduzir: python3 experiment.py [N_MAX_IMPAR]
"""
import sys
import math


def total_steps(n):
    total = 0
    while n != 1:
        m = 3 * n + 1
        a = 0
        while m % 2 == 0:
            m //= 2
            a += 1
        total += 1 + a
        n = m
    return total


def main():
    n_max = int(sys.argv[1]) if len(sys.argv) > 1 else 2_000_000

    xs = []  # log2(n)
    ys = []  # total_stopping_time(n)

    for n in range(3, n_max, 2):
        xs.append(math.log2(n))
        ys.append(total_steps(n))

    n_pts = len(xs)
    mean_x = sum(xs) / n_pts
    mean_y = sum(ys) / n_pts
    sxx = sum((x - mean_x) ** 2 for x in xs)
    sxy = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys))
    K_empirico = sxy / sxx
    intercept = mean_y - K_empirico * mean_x

    residuals = [y - (K_empirico * x + intercept) for x, y in zip(xs, ys)]
    resid_std = math.sqrt(sum(r * r for r in residuals) / (n_pts - 2))

    # R^2
    ss_tot = sum((y - mean_y) ** 2 for y in ys)
    ss_res = sum(r * r for r in residuals)
    r2 = 1 - ss_res / ss_tot

    log2_3 = math.log2(3)
    K_teorico = 3 / (2 - log2_3)

    print(f"n amostrados (impares, 3 ate {n_max}) = {n_pts}")
    print()
    print(f"K teorico  = {K_teorico:.4f}  (derivado de E[a]=2, H-001)")
    print(f"K empirico = {K_empirico:.4f}  (regressao linear total_steps ~ K*log2(n)+b)")
    print(f"diferenca relativa = {abs(K_empirico - K_teorico) / K_teorico * 100:.2f}%")
    print(f"intercepto = {intercept:.3f}")
    print(f"R^2 = {r2:.4f}")
    print(f"desvio padrao dos residuos = {resid_std:.3f}")
    print()

    # tendencia do desvio padrao dos residuos com log2(n): dividir amostra em blocos
    print("--- desvio padrao dos residuos por faixa de log2(n) (checar se cresce) ---")
    n_blocks = 5
    sorted_pairs = sorted(zip(xs, residuals))
    block_size = n_pts // n_blocks
    for b in range(n_blocks):
        block = sorted_pairs[b * block_size: (b + 1) * block_size if b < n_blocks - 1 else n_pts]
        block_resid = [r for _, r in block]
        block_x = [x for x, _ in block]
        mean_block_x = sum(block_x) / len(block_x)
        std_block = math.sqrt(sum(r * r for r in block_resid) / len(block_resid))
        print(f"  log2(n) ~ {mean_block_x:.1f}: desvio padrao residuo = {std_block:.3f}  (n={len(block)})")


if __name__ == "__main__":
    main()
