#!/usr/bin/env python3
"""
E-133: the l^2 budget available to O4 (Regime 3 of the three-precision
frame), measured directly on the Syracuse law mu_ell.

Three quantities, all exact up to double-precision rounding:

  K_ell   = 3^ell * sum_x mu_ell(x)^2            (collision mass, E-100)
  E_ell   = sum over primitive xi of |muhat_ell(xi)|^2
            (primitive energy; H-155 says E_ell = K_ell - K_(ell-1),
             H-154 gives an equivalent fresh-fibre form)
  sup_ell = max over primitive xi of |muhat_ell(xi)|

Reported:
  (a) cross-check of the three expressions for E_ell;
  (b) the fraction (K_r - 1) / (K_ell - 1) of the total primitive l^2
      mass carried by conductors at most 3^r, which is the share of the
      problem covered by the sublinear-precision theorem;
  (c) sup_ell and the RMS primitive coefficient, both rescaled by
      3^(ell/2), the square-root-cancellation scale.

The law mu_ell is built with the exact recursion of E-100 (validated
there bin by bin against direct Monte Carlo at ell = 3, 4).

Nothing here decides an asymptotic question. K_ell is nondecreasing
(H-138), so a finite range of levels cannot separate convergence from
divergence; see H-140.
"""
import numpy as np


def solve_level(p_prev, ell, s_max=100):
    """Law of Syrac mod 3^ell from the law mod 3^(ell-1) (E-100 recursion)."""
    mod = 3 ** ell
    period = 2 * (mod // 3)
    nu = np.zeros(mod)
    nu[1 + 3 * np.arange(len(p_prev))] = p_prev
    orbit = np.empty(period, dtype=np.int64)
    orbit[0] = 1
    for k in range(1, period):
        orbit[k] = (orbit[k - 1] * 2) % mod
    n_k = nu[orbit]
    x = np.zeros(period)
    for s in range(s_max):
        w = 0.5 ** (s + 1)
        if w == 0.0:
            break
        x += w * np.roll(n_k, -(s + 1))
    p = np.zeros(mod)
    p[orbit] = x
    return p


def primitive_energy_fft(p):
    ph = np.fft.fft(p)
    total = float(np.sum(np.abs(ph) ** 2))
    coarse = float(np.sum(np.abs(ph[::3]) ** 2))
    mod = len(p)
    mask = np.ones(mod, dtype=bool)
    mask[::3] = False
    idx = np.flatnonzero(mask)
    j = int(idx[np.argmax(np.abs(ph[idx]))])
    return total - coarse, total, float(np.abs(ph[j])), j


def primitive_energy_fibre(p, ell):
    """H-154: 3^(ell-1) * sum_b [(x0-x1)^2 + (x1-x2)^2 + (x2-x0)^2]."""
    m = 3 ** (ell - 1)
    x0, x1, x2 = p[0:m], p[m:2 * m], p[2 * m:3 * m]
    return float(m * np.sum((x0 - x1) ** 2 + (x1 - x2) ** 2 + (x2 - x0) ** 2))


def main(lmax=15):
    p = np.zeros(3)
    p[1] = 1 / 3
    p[2] = 2 / 3

    K = {}
    E = {}
    sup = {}
    argmax = {}
    err_fft = 0.0
    err_fibre = 0.0

    E0, tot, s0, j0 = primitive_energy_fft(p)
    K[1], sup[1], argmax[1] = tot, s0, j0

    print("(a) primitive energy, three expressions")
    print(f"{'ell':>3} {'K_ell':>11} {'K_l-K_(l-1)':>13} {'FFT':>13} {'fibres':>13}")
    for ell in range(2, lmax + 1):
        p = solve_level(p, ell)
        Ef, tot, s, j = primitive_energy_fft(p)
        K[ell], sup[ell], argmax[ell] = tot, s, j
        Ediff = K[ell] - K[ell - 1]
        Efib = primitive_energy_fibre(p, ell)
        E[ell] = Ediff
        err_fft = max(err_fft, abs(Ediff - Ef))
        err_fibre = max(err_fibre, abs(Ediff - Efib))
        print(f"{ell:>3} {K[ell]:11.6f} {Ediff:13.8f} {Ef:13.8f} {Efib:13.8f}")
    print(f"max |K_l-K_(l-1) - FFT|    = {err_fft:.3e}")
    print(f"max |K_l-K_(l-1) - fibres| = {err_fibre:.3e}")

    print("\n(b) share of primitive l^2 mass in conductors at most 3^r")
    print(f"{'ell':>4} {'r':>4} {'(K_r-1)/(K_ell-1)':>19} {'K_ell-K_r':>11}")
    for ell in [8, 10, 12, 14]:
        if ell > lmax:
            continue
        for r in sorted({1, 2, 3, int(round(ell ** 0.5)), ell // 2}):
            if r >= ell:
                continue
            print(f"{ell:>4} {r:>4} {(K[r]-1)/(K[ell]-1):19.5f} "
                  f"{K[ell]-K[r]:11.5f}")

    print("\n(c) primitive coefficients against the 3^(-ell/2) scale")
    print("    a uniform square-root bound would need sup_l/sup_(l-1) <= "
          "3^(-1/2) = 0.57735")
    print(f"{'ell':>3} {'E_ell':>10} {'rms*3^(l/2)':>12} {'sup*3^(l/2)':>12} "
          f"{'sup/rms':>9} {'sup_l/sup_(l-1)':>16} {'argmax xi':>10}")
    for ell in range(2, lmax + 1):
        rms = (E[ell] / (2 * 3 ** (ell - 1))) ** 0.5
        scale = 3.0 ** (ell / 2)
        print(f"{ell:>3} {E[ell]:10.6f} {rms*scale:12.5f} {sup[ell]*scale:12.5f} "
              f"{sup[ell]/rms:9.2f} {sup[ell]/sup[ell-1]:16.5f} "
              f"{argmax[ell]:>10}")


if __name__ == "__main__":
    main()
