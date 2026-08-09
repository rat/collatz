#!/usr/bin/env python3
"""Measures the joint lower-tail decoupling exponent for consecutive
units along the A-orbit (H-161's "m=2" question).

H-161 shows that the whole open band in direction (B) of the
beta_eff-vs-arc equivalence reduces to a question about consecutive
pairs of units along the affine orbit A(k)=4k+1 (mod 3^(ell-1)): does

    P(N(k) <= x  AND  N(next unit) <= x) <= C * P(N <= x)^theta

hold for some theta > 1 (theta=2 would be full independence; theta<2
would mean the pair clusters MORE than independence)? If a bound of
this form holds uniformly down to x ~ exp(-c0*ell) for some c0 large
enough, a union bound over all ~3^ell pairs gives an unconditional
bound beta_eff <= 1 + 1/(2*kappa) + o(1) for any kappa < theta/2 - 1/2
(see H-161 for the derivation, independently re-verified).

"Next unit" means the next unit in the CONTRACTED sequence (skipping
non-unit orbit positions, where N is identically 0 and would trivially
satisfy any threshold) -- this is the same contraction fix used in
E-131's deficient_arc_scan.py, needed for the same reason.

This script measures ratio(x, ell) := pair(x)/d(x)^2 (d = single-point
tail) at a threshold that shrinks with ell (exp(-eps*ell)), which is
required for the comparison to mean anything across levels -- see
E-131's README for why a fixed threshold is the wrong test here too.
"""

import argparse
import math

import numpy as np


def next_distribution(previous, level, tail=120):
    """Copied from E-111's weighted_bridge.py (not imported, to keep
    this experiment self-contained; logic unchanged)."""
    modulus = 3**level
    period = 2 * 3 ** (level - 1)
    nu = np.zeros(modulus, dtype=np.float64)
    nu[1 + 3 * np.arange(previous.size)] = previous

    orbit = np.empty(period, dtype=np.int64)
    orbit[0] = 1
    for k in range(1, period):
        orbit[k] = (2 * orbit[k - 1]) % modulus
    along = nu[orbit]

    values = np.zeros(period, dtype=np.float64)
    for s in range(tail):
        values += 2.0 ** (-(s + 1)) * np.roll(along, -(s + 1))

    distribution = np.zeros(modulus, dtype=np.float64)
    distribution[orbit] = values
    return distribution


def affine_orbit_units(mu_ell, level):
    modulus = 3**level
    orbit = np.empty(modulus, dtype=np.int64)
    k = 0
    for i in range(modulus):
        orbit[i] = k
        k = (4 * k + 1) % modulus
    normalized = mu_ell[orbit] * modulus
    units_mask = (orbit % 3) != 0
    return normalized[units_mask]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--levels", type=int, nargs="+", default=[8, 10, 12, 14, 16])
    parser.add_argument("--eps", type=float, default=0.1)
    args = parser.parse_args()

    max_level = max(args.levels)
    previous = np.array([1.0])
    laws = {}
    for level in range(1, max_level + 1):
        previous = next_distribution(previous, level)
        if level in args.levels:
            laws[level] = previous.copy()

    print(f"eps={args.eps} (threshold = exp(-eps*ell))")
    print(" ell   x           d(x)        pair(x)     hits    ratio      "
          "implied_theta")
    for level in args.levels:
        n_units = affine_orbit_units(laws[level], level)
        pair_a = n_units[:-1]
        pair_b = n_units[1:]

        x = math.exp(-args.eps * level)
        d = float((n_units <= x).mean())
        r = float(((pair_a <= x) & (pair_b <= x)).mean())
        indep = d * d
        ratio = r / indep if indep > 0 else float("nan")
        hits = r * len(pair_a)
        theta = 2 + math.log(ratio) / math.log(d) if 0 < ratio and d < 1 else float("nan")
        print(
            f"{level:4d}  {x:.4e}  {d:.4e}  {r:.4e}  {hits:6.1f}  "
            f"{ratio:.5f}  {theta:.3f}"
        )

    print()
    print(
        "If theta is roughly constant across levels, that constant is "
        "the decoupling exponent for the conditional bound in H-161. "
        "If theta visibly GROWS with ell (as observed at eps=0.1: "
        "2.90, 3.13, 3.54, 4.16, 5.26), the joint tail decays faster "
        "than any single fixed power of the marginal tail -- a "
        "stronger anti-clustering signal than the m=2 hypothesis (D) "
        "asked for, though still an empirical observation over a "
        "short range, not a proof of any fixed or growing rate."
    )


if __name__ == "__main__":
    main()
