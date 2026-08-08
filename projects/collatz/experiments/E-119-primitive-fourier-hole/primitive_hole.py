#!/usr/bin/env python3
"""Coarse and primitive Fourier coefficients of a one-hole unit law."""

import argparse
import cmath
import math


def coefficient(modulus, support, frequency):
    return sum(
        cmath.exp(2j * math.pi * frequency * value / modulus)
        for value in support
    ) / len(support)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-level", type=int, default=8)
    args = parser.parse_args()
    print("ell units coarse_abs primitive_max expected_primitive lifted_primitive_max")
    for level in range(2, args.max_level + 1):
        modulus = 3**level
        units = [value for value in range(modulus) if value % 3]
        support = units[1:]
        coarse = abs(coefficient(modulus, support, 3 ** (level - 1)))
        primitive = max(
            abs(coefficient(modulus, support, frequency))
            for frequency in range(1, modulus)
            if frequency % 3
        )
        expected = 1.0 / len(support)
        lower_modulus = 3 ** (level - 1)
        lower_units = [value for value in range(lower_modulus) if value % 3]
        lower_support = lower_units[1:]
        lifted = [
            value + digit * lower_modulus
            for value in lower_support
            for digit in range(3)
        ]
        lifted_primitive = max(
            abs(coefficient(modulus, lifted, frequency))
            for frequency in range(1, modulus)
            if frequency % 3
        )
        if abs(primitive - expected) > 1e-11:
            raise RuntimeError(f"primitive identity failed at ell={level}")
        if coarse < 0.5 - 1e-12:
            raise RuntimeError(f"coarse lower bound failed at ell={level}")
        if lifted_primitive > 1e-10:
            raise RuntimeError(f"lifted primitive cancellation failed at ell={level}")
        print(
            f"{level:3d} {len(units):6d} {coarse:.12f} "
            f"{primitive:.12e} {expected:.12e} {lifted_primitive:.12e}"
        )


if __name__ == "__main__":
    main()
