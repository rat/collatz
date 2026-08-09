#!/usr/bin/env python3
"""Test H-161's reformulation: does the longest run of consecutive
positions along the A-orbit (A(k)=4k+1 mod 3^(ell-1)) with normalized
mass N_ell(u) <= exp(-eps*ell) grow with ell, stay bounded, or shrink?

A FIXED threshold is the wrong test: the fraction of positions below a
fixed threshold grows with ell on its own, so even an i.i.d. random
arrangement of the same per-level frequencies would show a growing
longest run, purely from more trials. This script uses the threshold
the reformulation actually needs (exp(-eps*ell), which shrinks with
ell) and reports, at every level, the observed longest run against the
random-arrangement baseline log(N)/log(1/p) for that level's own
observed frequency p.

Uses a fast O(M log M) binary-doubling evaluation of the exact
geometric sum defining mu_ell (equivalent to, and cross-checked
against, the direct recursion in E-111's weighted_bridge.py), since
this needs higher levels than the O(M) direct approach comfortably
reaches.
"""

import argparse
import math

import numpy as np


def circ_geom_half(nu):
    """Return T[i] = sum_{t=1}^{M} 2^-t * nu[(i+t) % M], M = len(nu),
    via binary doubling of the shift-and-add operator (T = 0.5*nu
    convolved with the geometric kernel on the cycle Z/M)."""
    M = len(nu)
    cur = 0.5 * np.roll(nu, -1)
    cur_len = 1
    res = np.zeros(M)
    res_len = 0
    m = M
    while m:
        if m & 1:
            weight = 2.0 ** (-res_len) if res_len < 1070 else 0.0
            res = res + weight * np.roll(cur, -res_len)
            res_len += cur_len
        m >>= 1
        if m:
            weight = 2.0 ** (-cur_len) if cur_len < 1070 else 0.0
            cur = cur + weight * np.roll(cur, -cur_len)
            cur_len *= 2
    if M < 200:
        res = res / (1.0 - 2.0 ** (-M))
    return res


def longest_run(mask):
    padded = np.concatenate(([0], mask.view(np.int8), [0]))
    diff = np.diff(padded)
    starts = np.where(diff == 1)[0]
    ends = np.where(diff == -1)[0]
    return int((ends - starts).max()) if len(starts) else 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--min-level", type=int, default=8)
    parser.add_argument("--max-level", type=int, default=18)
    parser.add_argument("--eps-list", type=float, nargs="+", default=[0.1, 0.2])
    args = parser.parse_args()

    mu_prev = np.array([1.0])
    header = " ell | min_N (=3^ell*c_ell)"
    for eps in args.eps_list:
        header += f" | eps={eps}: frac  run  baseline"
    print(header)

    for level in range(1, args.max_level + 1):
        modulus = 3**level
        period = 2 * 3 ** (level - 1)
        orbit_pow2 = np.empty(period, dtype=np.int64)
        y = 1
        for i in range(period):
            orbit_pow2[i] = y
            y = (2 * y) % modulus
        nu = np.zeros(period)
        unit_mask = (orbit_pow2 % 3) == 1
        nu[unit_mask] = mu_prev[(orbit_pow2[unit_mask] - 1) // 3]
        law_along_pow2 = circ_geom_half(nu)
        mu_full = np.zeros(modulus)
        mu_full[orbit_pow2] = law_along_pow2
        mu_prev = mu_full

        if level < args.min_level:
            continue

        affine_period = modulus
        orbit_affine = np.empty(affine_period, dtype=np.int64)
        k = 0
        for i in range(affine_period):
            orbit_affine[i] = k
            k = (4 * k + 1) % affine_period
        normalized = mu_full[orbit_affine] * affine_period
        units_on_orbit = (orbit_affine % 3) != 0

        # A(k) == k+1 (mod 3), so exactly one in every three consecutive
        # orbit positions is a non-unit, where mu is identically 0 and
        # would count as "deficient" for free. Runs must be measured on
        # the CONTRACTED subsequence of unit positions only (in orbit
        # order), matching the population `fraction` is computed over,
        # not on the full orbit where non-units inflate every run by
        # roughly 50% (one free hit per two real ones).
        unit_values = normalized[units_on_orbit]
        n_positions = int(units_on_orbit.sum())

        row = f"{level:4d} | {unit_values.min():.6e}"
        for eps in args.eps_list:
            theta = math.exp(-eps * level)
            below = unit_values <= theta
            fraction = below.mean()
            run = longest_run(below)
            if 0 < fraction < 1:
                baseline = math.log(n_positions) / math.log(1.0 / fraction)
                baseline_str = f"{baseline:7.2f}"
            else:
                baseline_str = "    n/a"
            row += f" | {fraction:.4e} {run:4d} {baseline_str}"
        print(row)


if __name__ == "__main__":
    main()
