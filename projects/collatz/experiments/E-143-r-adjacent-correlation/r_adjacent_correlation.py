#!/usr/bin/env python3
"""E-143 (H-176): is R_ell(k) correlated with R_ell(A(k))?

H-176 asked whether H-166's convex-combination identity (R_ell is a
window average of R_{ell-1} along the A-orbit) explains the
decorrelation E-132 measured for a DIFFERENT quantity (the joint tail
of N/W at consecutive units). The hypothesis's own stated counter-
argument: overlapping-window averages classically correlate nearby
points, not decorrelate them, so if that holds here the lead dies fast.

It does. Corr(R_ell(k), R_ell(A(k))) is positive (0.40 to 0.55,
increasing and flattening with ell), against ~0 for a random shuffle
of the same values. Persisted here as a formal experiment (2026-08-10,
after a critique round flagged that the sole evidence behind a
`fechada-refutada` verdict had only lived in hypothesis-file prose, not
as a runnable script) rather than left in the session scratchpad.
"""

import sys
import os

import numpy as np

sys.path.insert(
    0,
    os.path.join(os.path.dirname(os.path.abspath(__file__)),
                  "..", "E-134-weyl-sum-pair-anticoncentration"),
)
from cascade_factor_bound import float_levels  # noqa: E402


def R_along_orbit(mu, mu_prev, ell):
    """R_ell(y(k)) for k=0..3^(ell-1)-1, via the t0=1 branch
    representative y=(3k+1)*inverse(2) mod 3^ell (same construction
    verified independently in H-176 and reused in E-142)."""
    mod = 3 ** ell
    mod_prev = 3 ** (ell - 1)
    inv2 = pow(2, -1, mod)
    ks = np.arange(mod_prev)
    z = (3 * ks + 1) % mod
    y = (z * inv2) % mod
    assert np.all(y % 3 != 0)
    Ny = mu[y] * mod
    Nprev = mu_prev[y % mod_prev] * mod_prev
    return Ny / Nprev


def main(maxlevel=14, seed=0):
    rng = np.random.default_rng(seed)
    print(f"{'ell':>3} {'corr(R(k),R(A(k)))':>20} {'corr(R,shuffled)':>18} "
          f"{'min(R)':>10} {'max(R)':>10}")
    for level, mu, mu_prev in float_levels(maxlevel):
        if level < 4:
            continue
        R = R_along_orbit(mu, mu_prev, level)
        modp = 3 ** (level - 1)
        Ak = (4 * np.arange(modp) + 1) % modp
        R_next = R[Ak]
        corr = np.corrcoef(R, R_next)[0, 1]
        shuffled = rng.permutation(R)
        corr_shuffled = np.corrcoef(R, shuffled)[0, 1]
        print(f"{level:3d} {corr:20.4f} {corr_shuffled:18.4f} "
              f"{R.min():10.5f} {R.max():10.4f}")


if __name__ == "__main__":
    main()
