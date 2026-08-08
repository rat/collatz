#!/usr/bin/env python3
"""Check logarithmic collision renormalization for several odd primes."""

import argparse

import numpy as np


def multiplicative_order_two(q):
    value = 1
    for order in range(1, q):
        value = (2 * value) % q
        if value == 1:
            return order
    raise AssertionError(q)


def solve_level(previous, q, level, cutoff=120):
    modulus = q**level
    order = multiplicative_order_two(q) * q ** (level - 1)
    nu = np.zeros(modulus)
    nu[1 + q * np.arange(len(previous))] = previous

    orbit = np.empty(order, dtype=np.int64)
    orbit[0] = 1
    for index in range(1, order):
        orbit[index] = (2 * orbit[index - 1]) % modulus
    if len(np.unique(orbit)) != order:
        raise AssertionError((q, level, "wrong lifted order"))

    along_orbit = nu[orbit]
    masses = np.zeros(order)
    for shift in range(1, cutoff + 1):
        masses += (2.0**-shift) * np.roll(along_orbit, -shift)
    law = np.zeros(modulus)
    law[orbit] = masses
    if abs(law.sum() - 1.0) > 2e-14:
        raise AssertionError((q, level, law.sum()))
    return law


def logarithmic_order(previous, q, d):
    size = len(previous)
    lifted_modulus = q * size
    values = np.empty(size, dtype=np.int64)
    power = 1
    step = pow(2, d, lifted_modulus)
    for index in range(size):
        values[index] = ((power - 1) // q) % size
        power = (step * power) % lifted_modulus
    if len(np.unique(values)) != size:
        raise AssertionError((q, size, "logarithmic map is not bijective"))
    return previous[values]


def spectral_collision(previous, q, d):
    ordered = logarithmic_order(previous, q, d)
    size = len(ordered)
    angle = 2.0 * np.pi * np.arange(size) / size
    numerator = q * (4**d - 1) / 3.0
    denominator = 4**d + 1 - 2 ** (d + 1) * np.cos(angle)
    transform = np.fft.fft(ordered)
    return float(np.sum(numerator / denominator * np.abs(transform) ** 2))


def collision(law, q, level):
    return q**level * float(np.sum(law**2))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--primes", type=int, nargs="+", default=[3, 5, 7, 11, 13, 17, 19])
    parser.add_argument("--max-level", type=int, default=5)
    args = parser.parse_args()

    for q in args.primes:
        d = multiplicative_order_two(q)
        if pow(2, d, q * q) == 1:
            raise AssertionError((q, "exceptional order lift"))
        previous = np.array([1.0])
        for level in range(1, args.max_level + 1):
            current = solve_level(previous, q, level)
            direct = collision(current, q, level)
            spectral = spectral_collision(previous, q, d)
            error = abs(direct - spectral)
            if error > 3e-10 * max(1.0, direct):
                raise AssertionError((q, d, level, direct, spectral, error))
            print(
                f"q={q:2d} d={d:2d} ell={level} K_direct={direct:.12g} "
                f"K_spectral={spectral:.12g} error={error:.3e}"
            )
            previous = current


if __name__ == "__main__":
    main()
