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

This script measures ratio(x, ell) := pair(x) / E[d(phase_a)*d(phase_b)]
at a threshold that shrinks with ell (exp(-eps*ell)), which is required
for the comparison to mean anything across levels -- see E-131's README
for why a fixed threshold is the wrong test here too.

The two positions of every consecutive-unit pair have DIFFERENT
marginals: F1 (see H-161) gives N = (3/2)*W(k0) at phase 2 (t0=1) and
N = (3/4)*W(k0) at phase 1 (t0=2), and the contracted unit sequence
strictly alternates phase 1, 2, 1, 2, ... So the correct independence
baseline is d1(x)*d2(x) (each phase's own marginal), not a single
pooled d(x)^2. An earlier version of this script used the pooled
baseline; caught via Rule 11b escalation before being trusted (the
pooled version understates the true independence baseline whenever the
tail is steep, since AM-GM makes d1*d2 < ((d1+d2)/2)^2 for any d1!=d2,
inflating the apparent anti-clustering signal). The corrected version
here computes d1(x) and d2(x) separately, verifies the free identity
d1(x) = d2(2*x) (implied by F1) as a bookkeeping check, and reports
ratio against the correct product baseline.
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


def affine_orbit_units_with_phase(mu_ell, level):
    """Returns (normalized N, orbit position mod 3 in {1,2}) for units
    only, in orbit order. The two phases have DIFFERENT marginals: F1
    gives N = (3/2)*W(k0) at phase 2 (t0=1) and N = (3/4)*W(k0) at
    phase 1 (t0=2), so pooling both phases into one marginal before
    comparing against the joint tail is wrong -- it compares the joint
    tail against a mixture of two different distributions rather than
    against the product of each pair member's own marginal."""
    modulus = 3**level
    orbit = np.empty(modulus, dtype=np.int64)
    k = 0
    for i in range(modulus):
        orbit[i] = k
        k = (4 * k + 1) % modulus
    normalized = mu_ell[orbit] * modulus
    phase = orbit % 3
    units_mask = phase != 0
    return normalized[units_mask], phase[units_mask]


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
    print(
        " ell   x           d1(x)       d2(2x)      [F1 check]  "
        "pair(x)     ratio=pair/(d1*d2)   implied_theta"
    )
    for level in args.levels:
        n_units, phase = affine_orbit_units_with_phase(laws[level], level)
        # phase==1 positions have t0=2 (N=(3/4)W), phase==2 have t0=1
        # (N=(3/2)W); consecutive units in the contracted sequence
        # always alternate 1,2,1,2,... in some rotation, so pair_a
        # and pair_b are always different phases.
        pair_a = n_units[:-1]
        pair_b = n_units[1:]
        phase_a = phase[:-1]
        phase_b = phase[1:]

        x = math.exp(-args.eps * level)
        n1 = n_units[phase == 1]
        n2 = n_units[phase == 2]
        d1 = float((n1 <= x).mean())
        d2 = float((n2 <= x).mean())
        d2_at_2x = float((n2 <= 2 * x).mean())

        below_a = pair_a <= x
        below_b = pair_b <= x
        r = float((below_a & below_b).mean())

        # per-pair marginals: whichever phase each member actually is
        d_a = np.where(phase_a == 1, d1, d2)
        d_b = np.where(phase_b == 1, d1, d2)
        indep = float(np.mean(d_a * d_b))
        ratio = r / indep if indep > 0 else float("nan")
        hits = r * len(pair_a)
        theta = (
            2 + math.log(ratio) / math.log(max(d1, 1e-300))
            if 0 < ratio < 1
            else float("nan")
        )
        print(
            f"{level:4d}  {x:.4e}  {d1:.4e}  {d2_at_2x:.4e}  "
            f"{'OK' if abs(d1-d2_at_2x) < 1e-9 else 'MISMATCH':>10s}  "
            f"{r:.4e}  {ratio:20.5f}  {theta:.3f}"
        )

        # Split by pair type: (1,2) = phase_a==1 (k==1 mod 3, adjacent
        # affine step A(k)); (2,1) = phase_a==2 (k==2 mod 3, skips the
        # non-unit via A^2). Both compared against the SAME product
        # baseline d1*d2 (the type doesn't change each member's own
        # marginal).
        for label, mask in (("(1,2)", phase_a == 1), ("(2,1)", phase_a == 2)):
            r_t = float((below_a[mask] & below_b[mask]).mean())
            ratio_t = r_t / (d1 * d2) if d1 * d2 > 0 else float("nan")
            hits_t = r_t * mask.sum()
            print(
                f"        type {label}: pair(x)={r_t:.4e}  "
                f"ratio={ratio_t:.5f}  hits={hits_t:.1f}"
            )

    print()
    print(
        "d1(x) and d2(2x) must match exactly (F1: phase-2 units carry "
        "N=(3/2)W, phase-1 units carry N=(3/4)W, so P(phase-1 N<=x) = "
        "P(W<=4x/3) = P(phase-2 N<=2x)). This is a free correctness "
        "check on the phase bookkeeping, not a new claim."
    )
    print(
        "ratio = pair(x) / E[d(phase_a)*d(phase_b)] is the correct "
        "independence baseline: each pair member compared against ITS "
        "OWN phase's marginal, not a pooled one. A ratio near 1 means "
        "the two positions are close to independent; well below 1 "
        "means real negative dependence beyond what the phase "
        "asymmetry alone explains."
    )


if __name__ == "__main__":
    main()
