#!/usr/bin/env python3
"""Certifies the inter-level cascade factor bound for the Syracuse law.

Write N_ell(u) = 3^ell mu_ell(u) and, for u a unit mod 3^ell,

    R_ell(u) := N_ell(u) / N_(ell-1)(u mod 3^(ell-1)).

F4 (the pushforward identity) says the three children of every u average
to the parent, so R has mean 1 over each sibling triple and min_u R <= 1.

The claim this script certifies is the opposite side: R_ell is a convex
combination of R_(ell-1) values, hence

    min_u R_ell(u) >= min_v R_(ell-1)(v),

so min R is nondecreasing in ell. Combined with the pointwise factoring
N_ell(u) = N_(ell-1)(u mod 3^(ell-1)) * R_ell(u), a min R computed at any
single level L bounds every later level:

    3^ell c_ell = min_u N_ell(u) >= C_L * (min R_L)^ell
    ==> limsup beta_eff <= 1 + log(1 / min R_L) / log 3.

Proof of the convex-combination step (see H-161 for the writeup). F1 gives
N_ell(y) = 3 * 2^-t0(y) * W_ell(k0(y)) with
W_ell(k) = sum_{j>=0} 4^-j N_(ell-1)(A^j k), A(k) = 4k+1 mod 3^(ell-1).
t0 depends only on y mod 3 and k0(y mod 3^(ell-1)) = k0(y) mod 3^(ell-2),
so the 3*2^-t0 factors cancel in the ratio:

    R_ell(y) = W_ell(k) / W_(ell-1)(k mod 3^(ell-2)),  k = k0(y).

A is given by an integer formula, so A^j k mod 3^(ell-2) = A^j(k mod
3^(ell-2)) for every j: numerator and denominator run over the SAME index
j with the SAME weights 4^-j. Substituting N_(ell-1)(A^j k) =
N_(ell-2)(A^j k') * R_(ell-1)(A^j k) exhibits R_ell(k) as an average of
R_(ell-1)(A^j k) with weights 4^-j N_(ell-2)(A^j k') / W_(ell-1)(k') >= 0
summing to 1. Weights vanish exactly where R_(ell-1) is undefined (non-unit
positions, where N is identically zero), so no 0/0 term enters.

Modes:

  --exact L     exact rational arithmetic (integer numerators over a
                common denominator), levels 2..L. This is the certified
                number; nothing depends on floating point.
  --float L     float64 measurement, levels 2..L, to show where the
                method saturates. Also cross-checks min N against the
                values E-127 recorded independently.
"""

import argparse
import math
import time
from fractions import Fraction

import numpy as np


# ---------------------------------------------------------------- exact


def exact_levels(maxlevel):
    """Yield (level, num, D, num_prev, D_prev) with mu_level(u) = num[u]/D
    exactly, num indexed by residue mod 3^level.

    mu_level(y) = sum_{t>=1} 2^-t nu(2^t y) along the 2-power cycle of
    length P = 2*3^(level-1), which closes exactly as
    S[i] / (2^P - 1) with S[i] = sum_{t=1}^{P} 2^(P-t) nu[(i+t) mod P].
    S is filled by the exact backward relation
    S[i-1] = 2^(P-1) nu[i] + (S[i] - nu[i]) / 2 (the halving is exact).
    """
    num_prev, D_prev = [1], 1          # mu_0(0) = 1
    for level in range(1, maxlevel + 1):
        mod = 3 ** level
        P = 2 * 3 ** (level - 1)
        orbit = [0] * P
        y = 1
        for i in range(P):
            orbit[i] = y
            y = (2 * y) % mod
        nu = [0] * P
        for i in range(P):
            o = orbit[i]
            if o % 3 == 1:
                nu[i] = num_prev[(o - 1) // 3]
        acc = 0
        for t in range(1, P + 1):
            acc += nu[t % P] << (P - t)
        S = [0] * P
        S[0] = acc
        top = 1 << (P - 1)
        i = 0
        for _ in range(P - 1):
            prev = (i - 1) % P
            S[prev] = top * nu[i] + ((S[i] - nu[i]) >> 1)
            i = prev
        D = D_prev * ((1 << P) - 1)
        num = [0] * mod
        for i in range(P):
            num[orbit[i]] = S[i]
        assert sum(num) == D, f"level {level}: total mass is not 1"
        yield level, num, D, num_prev, D_prev
        num_prev, D_prev = num, D


def run_exact(maxlevel):
    print("EXACT rational arithmetic (no floating point anywhere)")
    print(" ell   min R_ell (exact)        decimal        beta bound   secs")
    prev_min = None
    for level, num, D, num_prev, D_prev in exact_levels(maxlevel):
        if level == 1:
            assert Fraction(num[1], D) == Fraction(1, 3)
            assert Fraction(num[2], D) == Fraction(2, 3)
            print("   1   mu_1 = (0, 1/3, 2/3) confirmed exactly")
            continue
        start = time.time()
        mod_prev = 3 ** (level - 1)
        factor = (1 << (2 * 3 ** (level - 1))) - 1   # D / D_prev
        # R(y) = 3*num[y] / (factor * num_prev[y mod 3^(level-1)])
        best_p = best_q = None
        for y in range(3 ** level):
            if y % 3 == 0:
                continue
            p = 3 * num[y]
            q = factor * num_prev[y % mod_prev]
            if best_p is None or p * best_q < best_p * q:
                best_p, best_q = p, q
        rmin = Fraction(best_p, best_q)
        assert rmin <= 1, "min R > 1 contradicts the mean-one pushforward"
        if prev_min is not None:
            assert rmin >= prev_min, f"monotonicity FAILS at level {level}"
        prev_min = rmin
        bits = rmin.denominator.bit_length()
        shown = str(rmin) if bits <= 40 else f"{bits}-bit ratio"
        print(
            f"{level:4d}   {shown:22s}  {float(rmin):.12f}"
            f"   {1 + math.log(1/float(rmin))/math.log(3):.6f}"
            f"   {time.time()-start:5.1f}"
        )
    print()
    print(
        f"Certified: limsup beta_eff <= "
        f"{1 + math.log(1/float(prev_min))/math.log(3):.6f}  (from level {maxlevel})"
    )


# ---------------------------------------------------------------- float


def circ_geom_half(nu):
    """T[i] = sum_{t>=1} 2^-t nu[(i+t) mod M] by binary doubling.
    Every operation adds or scales nonnegative numbers, so there is no
    cancellation; the relative error is O(log M * eps) per level."""
    M = len(nu)
    cur = 0.5 * np.roll(nu, -1)
    cur_len, res_len = 1, 0
    res = np.zeros(M)
    m = M
    while m:
        if m & 1:
            w = 2.0 ** (-res_len) if res_len < 1070 else 0.0
            res = res + w * np.roll(cur, -res_len)
            res_len += cur_len
        m >>= 1
        if m:
            w = 2.0 ** (-cur_len) if cur_len < 1070 else 0.0
            cur = cur + w * np.roll(cur, -cur_len)
            cur_len *= 2
    if M < 200:
        res = res / (1.0 - 2.0 ** (-M))
    return res


def float_levels(maxlevel):
    mu_prev = np.array([1.0])
    for level in range(1, maxlevel + 1):
        mod = 3 ** level
        period = 2 * 3 ** (level - 1)
        orbit = np.empty(period, dtype=np.int64)
        y = 1
        for i in range(period):
            orbit[i] = y
            y = (2 * y) % mod
        nu = np.zeros(period)
        um = (orbit % 3) == 1
        nu[um] = mu_prev[(orbit[um] - 1) // 3]
        vals = circ_geom_half(nu)
        mu = np.zeros(mod)
        mu[orbit] = vals
        yield level, mu, mu_prev
        mu_prev = mu


# values E-127 recorded independently, used as a cross-check
E127_MIN_N = {12: 0.0529150, 13: 0.0500995, 14: 0.0469172, 15: 0.0441133,
              16: 0.0429289, 17: 0.0417504, 18: 0.0404242}


def run_float(maxlevel):
    print("float64 measurement (saturation of the method)")
    print(" ell    min R        max R      min N      minN/prev   beta bound  E-127")
    prev_min = None
    prev_minN = None
    for level, mu, mu_prev in float_levels(maxlevel):
        if level == 1:
            prev_minN = 1.0
            continue
        N = mu * 3 ** level
        Np = mu_prev * 3 ** (level - 1)
        units = (np.arange(3 ** level) % 3) != 0
        R = N[units] / np.tile(Np, 3)[units]
        # martingale/F4 check, free of charge
        f4 = np.abs(N.reshape(3, 3 ** (level - 1)).mean(axis=0) - Np).max()
        assert f4 < 1e-10, f"F4 fails at level {level}: {f4}"
        rmin, rmax = R.min(), R.max()
        minN = N[units].min()
        if prev_min is not None and rmin < prev_min - 1e-12:
            raise AssertionError(f"monotonicity fails at level {level}")
        cross = ""
        if level in E127_MIN_N:
            cross = "match" if abs(minN - E127_MIN_N[level]) < 5e-7 else "MISMATCH"
        print(
            f"{level:4d}  {rmin:.8f}  {rmax:.8f}  {minN:.6f}"
            f"   {minN/prev_minN:.5f}    {1+math.log(1/rmin)/math.log(3):.6f}  {cross}"
        )
        prev_min, prev_minN = rmin, minN
        del N, R
    print()
    print(
        "The 'minN/prev' column is the ratio the truth achieves; the proved"
        "\nper-level factor is min R. The gap between them is the whole"
        "\ndistance between this bound and beta_eff -> 1."
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--exact", type=int, default=0, help="max level, exact arithmetic")
    ap.add_argument("--float", dest="flt", type=int, default=0, help="max level, float64")
    args = ap.parse_args()
    if not args.exact and not args.flt:
        args.exact, args.flt = 8, 12
    if args.exact:
        run_exact(args.exact)
        print()
    if args.flt:
        run_float(args.flt)


if __name__ == "__main__":
    main()
