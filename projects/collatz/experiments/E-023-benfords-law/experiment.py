#!/usr/bin/env python3
"""
E-023 - Testa H-023: os valores de uma orbita de Collatz seguem a Lei de
Benford (P(primeiro digito=d) = log10(1+1/d))?

Dois testes limpos (evitando a armadilha de colisao de orbitas):
(a) uma UNICA orbita longa - sem risco de colisao, e uma trajetoria so.
(b) MUITAS orbitas independentes, UM valor por orbita (amostra grande e
    esparsa de n, como em E-001) - sem colisao por construcao.

Reproduzir: python3 experiment.py [N_LONGO] [K_AMOSTRAS]
"""
import sys
import math
import random


def first_digit(n):
    s = str(n)
    return int(s[0])


def benford_p(d):
    return math.log10(1 + 1 / d)


def chi_square_gof(counts, expected_fracs, n_total):
    chi2 = 0.0
    for d in range(1, 10):
        observed = counts.get(d, 0)
        expected = expected_fracs[d] * n_total
        chi2 += (observed - expected) ** 2 / expected
    return chi2


def chi_square_pvalue(x, k):
    if k <= 0:
        return float("nan")
    z = ((x / k) ** (1 / 3) - (1 - 2 / (9 * k))) / math.sqrt(2 / (9 * k))
    return 0.5 * math.erfc(z / math.sqrt(2))


def print_comparison(counts, n_total, label):
    print(f"--- {label} (n={n_total}) ---")
    print(f"{'digito':>7} {'observado':>10} {'benford':>10}")
    for d in range(1, 10):
        obs_frac = counts.get(d, 0) / n_total
        print(f"{d:>7} {obs_frac:>10.4f} {benford_p(d):>10.4f}")
    expected_fracs = {d: benford_p(d) for d in range(1, 10)}
    chi2 = chi_square_gof(counts, expected_fracs, n_total)
    p = chi_square_pvalue(chi2, 8)
    print(f"qui-quadrado = {chi2:.2f}  dof=8  p={p:.3e}")
    print()


def main():
    n_longo = int(sys.argv[1]) if len(sys.argv) > 1 else 837799
    k_amostras = int(sys.argv[2]) if len(sys.argv) > 2 else 500_000

    # (a) uma unica orbita longa
    counts_a = {}
    n = n_longo
    total_a = 0
    while n != 1:
        counts_a[first_digit(n)] = counts_a.get(first_digit(n), 0) + 1
        total_a += 1
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    counts_a[first_digit(1)] = counts_a.get(first_digit(1), 0) + 1
    total_a += 1

    print_comparison(counts_a, total_a, f"orbita unica (n0={n_longo})")

    # (b) muitas orbitas independentes, um valor por orbita (apos K passos padrao).
    # CUIDADO: se steps_to_take exceder o total_stopping_time real de n0, a orbita
    # ja chegou em 1 e fica "presa" la, inflando artificialmente o digito 1.
    # Descartamos essas amostras em vez de contar o 1 espurio.
    rng = random.Random(42)
    counts_b = {}
    low, high = 10 ** 9, 10 ** 12
    descartadas = 0
    coletadas = 0
    while coletadas < k_amostras:
        n0 = rng.randrange(low // 2, high // 2) * 2 + 1
        steps_to_take = rng.randint(10, 200)
        n = n0
        chegou_em_1 = False
        for _ in range(steps_to_take):
            if n == 1:
                chegou_em_1 = True
                break
            n = n // 2 if n % 2 == 0 else 3 * n + 1
        if chegou_em_1:
            descartadas += 1
            continue
        counts_b[first_digit(n)] = counts_b.get(first_digit(n), 0) + 1
        coletadas += 1

    print(f"(descartadas {descartadas} amostras que atingiram n=1 antes do fim da janela)")
    print_comparison(counts_b, k_amostras, "muitas orbitas independentes (1 valor cada, corrigido)")


if __name__ == "__main__":
    main()
