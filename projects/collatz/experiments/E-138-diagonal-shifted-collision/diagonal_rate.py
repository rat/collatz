#!/usr/bin/env python3
"""Shifted-collision decomposition of the qx+1 collision mass, and the q/3 rate.

Write mu_(q,ell) for the Syracuse law of parameter q with geometric weight
P(a)=2^-a, and

    K_(q,ell) = q^ell sum_x mu_(q,ell)(x)^2.

With F_ell = 2^-a (1 + q F_(ell-1)) mod q^ell and Y = 1 + q F_(ell-1) mod q^ell,
two independent copies collide iff Y' = 2^(a'-a) Y.  Since a, a' are iid
geometric on {1,2,...}, P[a'-a=s] = 2^-|s| / 3, so

    K_(q,ell) = (q/3) sum_(s in Z) 2^-|s| H_(ell-1)(s),
    H_(ell-1)(s) = q^(ell-1) P[Y' = 2^s Y mod q^ell] >= 0,
    H_(ell-1)(0) = K_(q,ell-1).

Every term is a probability times a positive constant, so dropping all s != 0
gives the unconditional rate

    K_(q,ell) >= (q/3) K_(q,ell-1).

This script checks the identity and the rate directly against the law, for
prime and composite odd q.  It uses no orbit hypothesis: the law is built by
the plain convolution mu_ell(y) = sum_(a>=1) 2^-a nu(2^a y), so the maximal
lifting condition v_q(2^d-1)=1 of H-157 is never invoked.
"""

import argparse

import numpy as np


def solve_level(previous, q, level, cutoff=120):
    """Law of F_ell mod q^ell from the law of F_(ell-1) mod q^(ell-1)."""
    modulus = q**level
    nu = np.zeros(modulus)
    nu[(1 + q * np.arange(len(previous))) % modulus] = previous
    index = np.arange(modulus)
    law = np.zeros(modulus)
    power = 1
    for shift in range(1, cutoff + 1):
        power = (2 * power) % modulus
        weight = 2.0**-shift
        if weight == 0.0:
            break
        law += weight * nu[(power * index) % modulus]
    if abs(law.sum() - 1.0) > 1e-12:
        raise AssertionError((q, level, law.sum()))
    return law


def shifted_profile(previous, q, level, max_shift):
    """H_(ell-1)(s) = q^(ell-1) P[Y' = 2^s Y mod q^ell] for s = 0..max_shift."""
    modulus = q**level
    nu = np.zeros(modulus)
    nu[(1 + q * np.arange(len(previous))) % modulus] = previous
    index = np.arange(modulus)
    profile = np.zeros(max_shift + 1)
    power = 1
    for shift in range(max_shift + 1):
        if shift:
            power = (2 * power) % modulus
        profile[shift] = q ** (level - 1) * float(np.dot(nu, nu[(power * index) % modulus]))
    return profile


def collision(law, q, level):
    return q**level * float(np.sum(law**2))


def order_of_two(q):
    value, order = 1, 0
    while True:
        value = (2 * value) % q
        order += 1
        if value == 1:
            return order
        if order > q:
            raise AssertionError(q)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--values", type=int, nargs="+",
                        default=[3, 5, 7, 9, 11, 13, 15, 21, 25])
    parser.add_argument("--max-modulus", type=int, default=2_000_000)
    parser.add_argument("--max-shift", type=int, default=60)
    args = parser.parse_args()

    worst = np.inf
    for q in args.values:
        if q % 2 == 0 or q < 3:
            raise SystemExit(f"q must be odd and at least 3, got {q}")
        d = order_of_two(q)
        c157 = q * (2**d - 1) / (3.0 * (2**d + 1))
        note = f"  H-157 c_(q,d)={c157:.6f} with d={d}"
        print(f"q={q}  rate q/3={q / 3.0:.6f}{note}")
        previous = np.array([1.0])
        previous_K = 1.0
        level = 1
        while q ** (level + 1) <= args.max_modulus:
            profile = shifted_profile(previous, q, level, args.max_shift)
            current = solve_level(previous, q, level)
            K = collision(current, q, level)
            identity = (q / 3.0) * (profile[0] + 2.0 * sum(
                2.0**-s * profile[s] for s in range(1, len(profile))))
            if level == 1:
                # base case: F_0 = 0, so Y = 1 and H_0(s) = [d divides s]
                closed = (q / 3.0) * (2**d + 1) / (2**d - 1)
                if abs(K - closed) > 1e-9 * closed:
                    raise AssertionError(("base case", q, K, closed))
                print(f"   base  K_(q,1)={K:.6f} matches (q/3)(2^d+1)/(2^d-1)"
                      f"={closed:.6f};  K_(q,0)=1")
            ratio = K / previous_K
            worst = min(worst, ratio - q / 3.0)
            flag = "" if ratio >= q / 3.0 - 1e-9 else "   <-- RATE VIOLATION"
            print(f"   ell={level:2d}  K={K:13.6f}  K/K_prev={ratio:10.6f}"
                  f"  identity_err={abs(K - identity):.3e}{flag}")
            previous, previous_K = current, K
            level += 1
        print()
    print(f"smallest observed (K_ell/K_(ell-1) - q/3) = {worst:.6e}")


if __name__ == "__main__":
    main()
