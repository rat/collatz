#!/usr/bin/env python3
"""
E-025 - Testa H-025: existe uma correlacao linear (GF(2)/Pearson) entre um
bit individual de n e um bit individual de m = (3n+1)/2^a (proximo impar),
NAO explicada pela determinacao 2-adica trivial de baixa ordem?

Metodologia tipo "criptoanalise linear": mede o bias (correlacao +-1) entre
bit_i(n) e bit_j(m) para todos os pares (i,j) numa janela, sobre uma amostra
grande de n impares aleatorios, SEM condicionar em a (a varia por amostra,
como acontece de fato na dinamica). Um bias grande fora da banda trivial de
baixa ordem seria um invariante linear genuino e novo.

Reproduzir: python3 experiment.py [N_SAMPLES] [WINDOW] [BIT_LENGTH]
"""
import sys
import numpy as np


def accel_step_vec(n):
    """m = (3n+1) removendo todos os fatores de 2; retorna (m, a)."""
    t = 3 * n + 1
    a = np.zeros_like(t)
    m = t.copy()
    for shift in (32, 16, 8, 4, 2, 1):
        mask = (m & np.int64((1 << shift) - 1)) == 0
        a = a + mask.astype(np.int64) * shift
        m = np.where(mask, m >> shift, m)
    return m, a


def main():
    n_samples = int(sys.argv[1]) if len(sys.argv) > 1 else 2_000_000
    window = int(sys.argv[2]) if len(sys.argv) > 2 else 24
    bit_length = int(sys.argv[3]) if len(sys.argv) > 3 else 50

    rng = np.random.default_rng(42)
    n = (rng.integers(0, 2 ** (bit_length - 1), size=n_samples, dtype=np.int64) << 1) | 1

    m, a = accel_step_vec(n)

    print(f"N={n_samples}, window={window} bits, bit_length={bit_length}")
    print(f"a: media={a.mean():.4f} (esperado 2.0), var={a.var():.4f} (esperado 2.0)")
    print()

    idx = np.arange(window)
    Bn = ((n[:, None] >> idx) & 1).astype(np.float64) * 2 - 1  # (N, W) em +-1
    Bm = ((m[:, None] >> idx) & 1).astype(np.float64) * 2 - 1  # (N, W) em +-1

    bias = (Bn.T @ Bm) / n_samples  # (W, W), bias[i,j] = corr(bit_i(n), bit_j(m))

    se = 1.0 / np.sqrt(n_samples)
    z_threshold = 5.0
    sig_threshold = z_threshold * se

    print(f"erro padrao esperado sob ruido puro = {se:.5f}")
    print(f"limiar de significancia (|z|>{z_threshold}) => |bias| > {sig_threshold:.5f}")
    print()

    print("Maiores |bias| fora da diagonal principal (|i-j|>3), ordenados:")
    entries = []
    for i in range(window):
        for j in range(window):
            if abs(i - j) > 3:
                entries.append((abs(bias[i, j]), i, j, bias[i, j]))
    entries.sort(reverse=True)
    for absb, i, j, b in entries[:15]:
        z = b / se
        flag = "  <-- SIGNIFICATIVO" if absb > sig_threshold else ""
        print(f"  bit_{i}(n) vs bit_{j}(m): bias={b:+.5f}  z={z:+.1f}{flag}")

    print()
    print("Banda diagonal/proxima (|i-j|<=3), mostrando decaimento com i:")
    for i in range(min(window, 15)):
        row = "  ".join(f"{bias[i, j]:+.3f}" for j in range(max(0, i - 3), min(window, i + 4)))
        print(f"  i={i:2d}: {row}")


if __name__ == "__main__":
    main()
