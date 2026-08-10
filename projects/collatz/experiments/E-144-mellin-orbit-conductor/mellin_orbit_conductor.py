#!/usr/bin/env python3
"""E-144 (H-175): the Mellin/orbit-time transform of N_ell, decomposed
by orbit conductor.

H-175's "tentativa 2" established that the Mellin/orbit-time transform
of N_ell (the object H-161's Weyl section actually uses: N_ell(y(k_t))
reordered by orbit time t under A(k)=4k+1) is genuinely different from
the ordinary additive Fourier transform of N_ell that E-137 measures
(sup and rms ratios between the two do not track a single scale
factor).

This script takes the next step: group the Mellin frequencies m by
ORBIT CONDUCTOR 3^r, r := (ell-1) - v3(m) (the exact analogue, in
orbit-time space, of the conductor graduation H-154/H-155/E-137 use in
additive space), and report energy/sup per class.

Correctness: reuses `float_levels` from
E-134-weyl-sum-pair-anticoncentration/cascade_factor_bound.py
unmodified. The orbit-time sequence construction (t0=1 branch) is the
same one independently verified in H-172/E-143 against float_levels'
own recorded min-N values, and the Plancherel identity
(sum|hat(m)|^2 = M*sum(seq^2)) was checked to 2e-16 in H-175's
"tentativa 2" using the same construction; not re-checked here since
nothing about the construction changed, only the grouping by r.
"""

import os
import sys

import numpy as np

sys.path.insert(
    0,
    os.path.join(os.path.dirname(os.path.abspath(__file__)),
                  "..", "E-134-weyl-sum-pair-anticoncentration"),
)
from cascade_factor_bound import float_levels  # noqa: E402


def orbit_time_sequence(mu, mu_prev, ell):
    """N_ell(y(k_t)) ordered by orbit time t under A(k)=4k+1 mod
    3^(ell-1), y via the t0=1 branch representative."""
    mod = 3 ** ell
    mod_prev = 3 ** (ell - 1)
    inv2 = pow(2, -1, mod)
    N_full = mu * mod
    k = 0
    seq = np.empty(mod_prev, dtype=np.float64)
    for t in range(mod_prev):
        z = (3 * k + 1) % mod
        y = (z * inv2) % mod
        seq[t] = N_full[y]
        k = (4 * k + 1) % mod_prev
    return seq


def v3(n):
    n = abs(int(n))
    if n == 0:
        return 10 ** 9
    k = 0
    while n % 3 == 0:
        n //= 3
        k += 1
    return k


def conductor_breakdown(mu, mu_prev, ell):
    seq = orbit_time_sequence(mu, mu_prev, ell)
    M = len(seq)
    hat = np.fft.fft(seq)
    m = np.arange(M)
    maxr = ell - 1
    rows = []
    for r in range(1, maxr + 1):
        cond_of_m = np.array([(ell - 1) - v3(int(mm)) if mm != 0 else -1
                               for mm in m])
        mask = cond_of_m == r
        if not mask.any():
            continue
        energy_r = float(np.sum(np.abs(hat[mask]) ** 2))
        sup_r = float(np.max(np.abs(hat[mask])))
        count = int(mask.sum())
        rows.append((r, count, energy_r, sup_r, sup_r / np.sqrt(3.0 ** r)))
    total_energy = float(np.sum(np.abs(hat[1:]) ** 2))
    return rows, total_energy


def main(maxlevel=12):
    for level, mu, mu_prev in float_levels(maxlevel):
        if level < 6:
            continue
        rows, total_energy = conductor_breakdown(mu, mu_prev, level)
        M = 3 ** (level - 1)
        print(f"ell={level} M={M} total_energy(r>=1)={total_energy:.2f}")
        print(f"{'r':>3} {'count':>8} {'energy':>16} {'sup':>14} "
              f"{'sup/sqrt(3^r)':>14}")
        for r, count, energy_r, sup_r, scaled in rows:
            print(f"{r:3d} {count:8d} {energy_r:16.2f} {sup_r:14.2f} "
                  f"{scaled:14.4f}")
        sum_rows = sum(row[2] for row in rows)
        err = abs(sum_rows - total_energy) / total_energy
        print(f"  self-consistency: sum of per-conductor energies vs "
              f"total, rel err = {err:.2e}")
        print()


if __name__ == "__main__":
    main()
