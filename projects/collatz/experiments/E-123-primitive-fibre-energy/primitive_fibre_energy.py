#!/usr/bin/env python3
"""Checks the primitive Fourier energy identity from H-154."""

import argparse

import numpy as np


def fourier(values):
    return np.fft.fft(values)


def fibre_energy(values, level):
    old_modulus = 3 ** (level - 1)
    children = np.vstack(
        [values[offset * old_modulus : (offset + 1) * old_modulus] for offset in range(3)]
    )
    x0, x1, x2 = children
    return old_modulus * np.sum(
        (x0 - x1) ** 2 + (x1 - x2) ** 2 + (x2 - x0) ** 2
    )


def check(values, level, tolerance=2e-9):
    transform = fourier(values)
    primitive = np.arange(len(values)) % 3 != 0
    spectral = float(np.sum(np.abs(transform[primitive]) ** 2))
    fibres = float(fibre_energy(values, level))
    error = abs(spectral - fibres)
    if error > tolerance * max(1.0, spectral, fibres):
        raise AssertionError((level, spectral, fibres, error))
    return spectral, fibres, error


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-level", type=int, default=8)
    parser.add_argument("--seed", type=int, default=154)
    args = parser.parse_args()
    rng = np.random.default_rng(args.seed)

    for level in range(1, args.max_level + 1):
        modulus = 3**level
        counts = rng.integers(0, 20, size=modulus, dtype=np.int64)
        if counts.sum() == 0:
            counts[0] = 1
        law = counts / counts.sum()
        spectral, fibres, error = check(law, level)

        old = rng.random(3 ** (level - 1))
        old /= old.sum()
        lifted = np.tile(old / 3.0, 3)
        lifted_spectral, _, lifted_error = check(lifted, level)
        maximum = float(np.max(np.abs(fourier(law)[np.arange(modulus) % 3 != 0])))
        if any(
            not np.array_equal(
                counts[: modulus // 3],
                counts[offset * modulus // 3 : (offset + 1) * modulus // 3],
            )
            for offset in (1, 2)
        ):
            assert maximum + 1e-12 >= 1.0 / counts.sum()

        print(
            f"ell={level:2d} random_energy={spectral:.12g} "
            f"identity_error={error:.3e} lifted_energy={lifted_spectral:.3e} "
            f"lifted_error={lifted_error:.3e}"
        )


if __name__ == "__main__":
    main()
