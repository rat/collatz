#!/usr/bin/env python3
"""Exact transfer operator on affine states, and a failed subinvariance certificate.

Let T_ell(u,v) = 3^ell P[F'_ell = u F_ell + v mod 3^ell], u a unit.  Writing
F = 2^-a (1 + 3 Ftil) with a geometric on {1,2,...} gives, exactly,

    T_ell(u,v) = 3 sum_(a,a'>=1)  2^-(a+a')  T_(ell-1)(w, (w + v 2^a' - 1)/3),
    w = u 2^(a'-a),  summed over the pairs with 3 | (w + v 2^a' - 1),

with T_0 = 1 on every state.  The operator does not depend on the level, which
is what makes a level-uniform lower bound on T_ell(4,1) = G_ell(1) conceivable.

Part 1 validates the recursion in exact rational arithmetic at levels 1, 2, 3
against the law itself.

Part 2 tests the obvious certificate: a function h of (u,v) mod 3^k with
0 <= h <= 1 and (Th)(u,v) >= h(u,v) for every lift.  Such an h would give
T_ell >= h for all ell by induction from T_0 = 1.  The largest such h is the
limit of h <- min(h, T_* h) started from 1, where T_* takes the minimum over
lifts.  The iteration collapses to 0 geometrically for k = 1 and k = 2, so no
certificate of this shape exists at those resolutions.  Reported as a negative
result.
"""

import argparse
from fractions import Fraction as Fr


def syracuse_law(level):
    """mu_ell on Z/3^ell as exact Fractions."""
    modulus = 3**level
    if level == 0:
        return [Fr(1)]
    previous = syracuse_law(level - 1)
    nu = [Fr(0)] * modulus
    for x, p in enumerate(previous):
        nu[(1 + 3 * x) % modulus] = p
    period = 2 * (modulus // 3)
    orbit = [1] * period
    for k in range(1, period):
        orbit[k] = (orbit[k - 1] * 2) % modulus
    along = [nu[y] for y in orbit]
    law = [Fr(0)] * modulus
    for k in range(period):
        total = Fr(0)
        for s in range(1, period + 1):
            total += Fr(1, 2**s) * along[(k + s) % period]
        law[orbit[k]] = total / (1 - Fr(1, 2**period))
    return law


def T_direct(law, level, u, v):
    modulus = 3**level
    total = Fr(0)
    for x in range(modulus):
        if law[x]:
            total += law[x] * law[(u * x + v) % modulus]
    return modulus * total


def states(k):
    modulus = 3**k
    return [(u, v) for u in range(modulus) if u % 3 for v in range(modulus)]


def apply_operator(h, k, u, v):
    """(Th)(u,v), h a function of (u,v) mod 3^k, argument given mod 3^(k+1)."""
    lifted = 3 ** (k + 1)
    coarse = 3**k
    period = 2 * coarse                      # period of 2^t mod 3^(k+1)
    inverse_two = pow(2, -1, lifted)
    normal = 1 - Fr(1, 2**period)
    weight = {r: Fr(1, 2**r) / normal for r in range(1, period + 1)}
    total = Fr(0)
    for a in range(1, period + 1):
        inv_a = pow(inverse_two, a, lifted)
        for ap in range(1, period + 1):
            two_ap = pow(2, ap, lifted)
            w = (u * two_ap % lifted) * inv_a % lifted
            numerator = (w + v * two_ap - 1) % lifted
            if numerator % 3:
                continue
            total += weight[a] * weight[ap] * h[(w % coarse, (numerator // 3) % coarse)]
    return 3 * total


def coarse_step(h, k):
    """T_* h: for each coarse state, the minimum of (Th) over its lifts."""
    coarse = 3**k
    lifted = 3 ** (k + 1)
    out = {}
    for u in range(lifted):
        if u % 3 == 0:
            continue
        for v in range(lifted):
            value = apply_operator(h, k, u, v)
            key = (u % coarse, v % coarse)
            if key not in out or value < out[key]:
                out[key] = value
    return out


def validate():
    laws = {level: syracuse_law(level) for level in (1, 2, 3)}
    checks = [
        (1, {s: Fr(1) for s in states(1)}, 1),
        (1, {s: T_direct(laws[1], 1, *s) for s in states(1)}, 2),
        (2, {s: T_direct(laws[2], 2, *s) for s in states(2)}, 3),
    ]
    for k, h, level in checks:
        lifted = 3 ** (k + 1)
        for u in range(lifted):
            if u % 3 == 0:
                continue
            for v in range(lifted):
                got = apply_operator(h, k, u, v)
                want = T_direct(laws[level], level, u, v)
                if got != want:
                    raise AssertionError(("recursion mismatch", level, u, v, got, want))
        print(f"T_{level} reproduced from T_{level - 1} by the operator: exact match")
    print("T_1(4,1) =", T_direct(laws[1], 1, 4, 1),
          " T_2(4,1) =", T_direct(laws[2], 2, 4, 1),
          " T_3(4,1) =", T_direct(laws[3], 3, 4, 1))
    violations = [
        (u, v) for u in range(9) if u % 3 for v in range(9)
        if T_direct(laws[2], 2, u, v) < T_direct(laws[1], 1, u % 3, v % 3)
    ]
    print(f"states (mod 9) where T_2 < T_1: {len(violations)} of 54 "
          "(so plain monotonicity in ell is false state by state)")


def certificate(k, rounds):
    space = states(k)
    h = {s: Fr(1) for s in space}
    target = (4 % 3**k, 1 % 3**k)
    for n in range(1, rounds + 1):
        stepped = coarse_step(h, k)
        new = {s: min(h[s], stepped[s]) for s in space}
        if new == h:
            print(f"k={k}: fixed point reached at round {n}, h(4,1)={float(h[target]):.6f}")
            return
        h = new
        print(f"k={k} round {n:2d}: min h = {float(min(h.values())):.8f}   "
              f"h(4,1) = {float(h[target]):.8f}")
    print(f"k={k}: no fixed point after {rounds} rounds, h is collapsing to zero")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rounds", type=int, default=12)
    parser.add_argument("--resolutions", type=int, nargs="+", default=[1, 2])
    args = parser.parse_args()
    validate()
    print()
    for k in args.resolutions:
        certificate(k, args.rounds)
        print()


if __name__ == "__main__":
    main()
