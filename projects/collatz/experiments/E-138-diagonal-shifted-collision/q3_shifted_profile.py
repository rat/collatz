#!/usr/bin/env python3
"""q=3: the increment E_ell as a nonnegative combination of shifted collisions.

For q=3 the diagonal rate q/3 equals 1, so the shifted-collision identity only
reproduces the monotonicity already recorded in H-155 and H-140.  The content
here is the explicit form of the increment.  With
G_(ell-1)(r) = 3^(ell-1) P[Y' = 4^r Y mod 3^ell]  (Y = 1 + 3 F_(ell-1)),

    K_ell = sum_(r in Z) 4^-|r| G_(ell-1)(r),      G_(ell-1)(0) = K_(ell-1),
    E_ell = K_ell - K_(ell-1) = 2 sum_(r>=1) 4^-r G_(ell-1)(r) >= (1/2) G_(ell-1)(1).

G_(ell-1)(1) is the affine shifted collision T_(ell-1)(4,1), where

    T_ell(u,v) = 3^ell P[F'_ell = u F_ell + v mod 3^ell] = E_x[N(x) N(ux+v)],
    N = 3^ell mu_ell.

The script prints the profile G(r), checks the identity against the direct
collision mass, and reports min over all affine states (u,v) of T_ell(u,v).
"""

import argparse

import numpy as np


def solve_level(previous, level, cutoff=120):
    modulus = 3**level
    nu = np.zeros(modulus)
    nu[(1 + 3 * np.arange(len(previous))) % modulus] = previous
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
        raise AssertionError((level, law.sum()))
    return law


def shifted_profile(previous, level, max_shift):
    """G_(ell-1)(r) for r = 0..max_shift."""
    modulus = 3**level
    nu = np.zeros(modulus)
    nu[(1 + 3 * np.arange(len(previous))) % modulus] = previous
    index = np.arange(modulus)
    profile = np.zeros(max_shift + 1)
    power = 1
    for r in range(max_shift + 1):
        if r:
            power = (4 * power) % modulus
        profile[r] = 3 ** (level - 1) * float(np.dot(nu, nu[(power * index) % modulus]))
    return profile


def min_affine_state(law, level):
    """min over units u and all v of T_ell(u,v), by FFT cross-correlation."""
    modulus = 3**level
    index = np.arange(modulus)
    transform = np.fft.rfft(law)
    best, best_state = np.inf, None
    for u in range(1, modulus):
        if u % 3 == 0:
            continue
        shifted = law[(pow(u, -1, modulus) * index) % modulus]
        correlation = np.fft.irfft(np.conj(np.fft.rfft(shifted)) * transform, n=modulus)
        v = int(np.argmin(correlation))
        if correlation[v] < best:
            best, best_state = float(correlation[v]), (u, v)
    return modulus * best, best_state


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-level", type=int, default=14)
    parser.add_argument("--min-state-level", type=int, default=8,
                        help="levels up to which the affine-state minimum is scanned")
    args = parser.parse_args()

    previous = np.array([1.0])
    previous_K = 1.0
    print("ell   K_ell      E_ell     ident_err   G(1)      G(2)      G(3)"
          "     lower=G(1)/2   min_(u,v) T_ell")
    for level in range(1, args.max_level + 1):
        profile = shifted_profile(previous, level, 40)
        current = solve_level(previous, level)
        K = 3**level * float(np.sum(current**2))
        identity = profile[0] + 2.0 * sum(4.0**-r * profile[r]
                                          for r in range(1, len(profile)))
        increment = K - previous_K
        if increment < -1e-12:
            raise AssertionError(("increment negative", level, increment))
        if 0.5 * profile[1] > increment + 1e-12:
            raise AssertionError(("G(1)/2 exceeds increment", level))
        state_line = ""
        if level <= args.min_state_level:
            value, state = min_affine_state(current, level)
            state_line = f"   {value:.6f} at {state}"
        print(f"{level:3d} {K:10.6f} {increment:9.6f}  {abs(K - identity):.2e}  "
              f"{profile[1]:8.5f}  {profile[2]:8.5f}  {profile[3]:8.5f}"
              f"     {0.5 * profile[1]:.6f}{state_line}")
        previous, previous_K = current, K


if __name__ == "__main__":
    main()
