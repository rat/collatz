#!/usr/bin/env python3
"""Verify the exact affine-orbit reformulation of the memoryless recursion
(H-158 step-4 attempt, H-161).

The verified recursion is mu_ell(y) = 1/2 nu(2y) + 1/2 mu_ell(2y) (forward,
increasing powers of 2). Unrolling gives mu_ell(y) = sum_{t>=1} 2^-t
nu(2^t y mod 3^ell), nonzero only at t with 2^t y == 1 (mod 3) (nu is
supported on z==1 mod 3). Those t share a fixed parity t0(y) in {1,2},
and t -> t+2 sends z=2^t y to 4z. Writing z=1+3k, this is the affine map

    A(k) = 4k+1 (mod 3^(ell-1))

which turns out to be a single cycle of length 3^(ell-1) covering all of
Z/3^(ell-1)Z (4 has order exactly 3^(ell-1) mod 3^ell). This gives

    mu_ell(y) = 2^-t0(y) * sum_j 4^-j * mu_(ell-1)(A^j(k0(y)))
    c_ell = (1/4) * min_k G(k),  G(k) = sum_j 4^-j mu_(ell-1)(A^j(k))

This script checks both identities directly against the reference
recursion in E-111's weighted_bridge.py, independently of any script
used during the consultation that first proposed this reformulation.
"""

import argparse
import importlib.util
from pathlib import Path

import numpy as np


def load_next_distribution():
    path = (
        Path(__file__).parents[1]
        / "E-111-weighted-wcc-beta-bridge"
        / "weighted_bridge.py"
    )
    spec = importlib.util.spec_from_file_location("weighted_bridge", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.next_distribution


def affine_orbit_is_full_cycle(prev_modulus):
    seen = set()
    k = 0
    for _ in range(prev_modulus):
        seen.add(k)
        k = (4 * k + 1) % prev_modulus
    return len(seen) == prev_modulus and k == 0


def t0_and_k0(y, modulus):
    z = y % modulus
    for t in (1, 2):
        z = (2 * z) % modulus
        if z % 3 == 1:
            return t, (z - 1) // 3
    raise AssertionError((y, modulus))


def orbit_reconstruction(y, ell, mu_prev, terms=400):
    modulus = 3**ell
    prev_modulus = 3 ** (ell - 1)
    t0, k0 = t0_and_k0(y, modulus)
    total = 0.0
    k = k0
    for j in range(min(terms, prev_modulus)):
        total += 4.0 ** (-j) * mu_prev[k]
        k = (4 * k + 1) % prev_modulus
    correction = 1.0 / (1.0 - 4.0 ** (-prev_modulus)) if prev_modulus < 500 else 1.0
    return 2.0 ** (-t0) * total * correction


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-level", type=int, default=8)
    args = parser.parse_args()

    next_distribution = load_next_distribution()
    previous = np.array([1.0])
    levels = [previous]
    for level in range(1, args.max_level + 1):
        previous = next_distribution(previous, level)
        levels.append(previous)

    print("ell cycle_full pointwise_max_reldiff c_ell_direct c_ell_orbit_formula")
    for ell in range(2, args.max_level + 1):
        prev_modulus = 3 ** (ell - 1)
        modulus = 3**ell
        mu_prev = levels[ell - 1]
        mu_ell = levels[ell]

        full_cycle = affine_orbit_is_full_cycle(prev_modulus)

        max_reldiff = 0.0
        sample_ys = [y for y in range(1, min(modulus, 2000)) if y % 3 != 0]
        for y in sample_ys:
            direct = mu_ell[y]
            recon = orbit_reconstruction(y, ell, mu_prev)
            reldiff = abs(direct - recon) / max(direct, 1e-300)
            max_reldiff = max(max_reldiff, reldiff)

        orb = np.empty(prev_modulus, dtype=np.int64)
        k = 0
        for i in range(prev_modulus):
            orb[i] = k
            k = (4 * k + 1) % prev_modulus
        v = mu_prev[orb]
        window = np.zeros(prev_modulus)
        for j in range(min(400, prev_modulus)):
            window += 4.0 ** (-j) * np.roll(v, -j)
        correction = 1.0 / (1.0 - 4.0 ** (-prev_modulus)) if prev_modulus < 500 else 1.0
        c_ell_orbit = 0.25 * window.min() * correction

        units = np.arange(modulus)
        units = units[units % 3 != 0]
        c_ell_direct = float(mu_ell[units].min())

        print(
            f"{ell:3d} {str(full_cycle):>5s} {max_reldiff:.3e} "
            f"{c_ell_direct:.12e} {c_ell_orbit:.12e}"
        )


if __name__ == "__main__":
    main()
