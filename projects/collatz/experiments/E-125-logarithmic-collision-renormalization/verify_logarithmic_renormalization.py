#!/usr/bin/env python3
"""Verify the exact collision renormalization in discrete-log order."""

import argparse
import importlib.util
from pathlib import Path

import numpy as np


def load_solver():
    path = (
        Path(__file__).parents[1]
        / "E-100-syracuse-collision-mass-k-ell"
        / "experiment_k_ell.py"
    )
    spec = importlib.util.spec_from_file_location("e100_solver", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.solve_level


def logarithmic_order(previous):
    """Return a_j=mu((4^j-1)/3 mod 3^(ell-1))."""
    modulus = len(previous)
    lifted_modulus = 3 * modulus
    values = np.empty(modulus, dtype=np.int64)
    power = 1
    for j in range(modulus):
        values[j] = ((power - 1) // 3) % modulus
        power = (4 * power) % lifted_modulus
    if len(np.unique(values)) != modulus:
        raise AssertionError("the logarithmic ordering is not bijective")
    return previous[values]


def spectral_collision(previous):
    a = logarithmic_order(previous)
    size = len(a)
    frequencies = 2.0 * np.pi * np.arange(size) / size
    multiplier = 15.0 / (17.0 - 8.0 * np.cos(frequencies))
    transform = np.fft.fft(a)
    contributions = multiplier * np.abs(transform) ** 2
    return float(np.sum(contributions)), float(np.sum(np.abs(transform) ** 2))


def direct_collision(law):
    return len(law) * float(np.sum(law**2))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-level", type=int, default=12)
    parser.add_argument("--random-trials", type=int, default=3)
    parser.add_argument("--seed", type=int, default=156)
    args = parser.parse_args()

    solve_level = load_solver()
    previous = np.zeros(3)
    previous[1] = 1.0 / 3.0
    previous[2] = 2.0 / 3.0

    for level in range(2, args.max_level + 1):
        current = solve_level(previous, level)
        direct = direct_collision(current)
        spectral, parseval_previous = spectral_collision(previous)
        expected_previous = direct_collision(previous)
        error = abs(direct - spectral)
        parseval_error = abs(parseval_previous - expected_previous)
        tolerance = 2e-10 * max(1.0, direct)
        if error > tolerance or parseval_error > tolerance:
            raise AssertionError(
                (level, direct, spectral, error, parseval_error)
            )
        print(
            f"ell={level:2d} K_direct={direct:.12g} "
            f"K_spectral={spectral:.12g} increment={direct-expected_previous:.12g} "
            f"error={error:.3e} parseval_error={parseval_error:.3e}"
        )
        previous = current

    rng = np.random.default_rng(args.seed)
    for level in range(2, min(args.max_level, 8) + 1):
        modulus = 3 ** (level - 1)
        for trial in range(args.random_trials):
            previous = rng.dirichlet(np.ones(modulus))
            current = solve_level(previous, level)
            direct = direct_collision(current)
            spectral, parseval_previous = spectral_collision(previous)
            expected_previous = direct_collision(previous)
            error = abs(direct - spectral)
            parseval_error = abs(parseval_previous - expected_previous)
            tolerance = 2e-10 * max(1.0, direct)
            if error > tolerance or parseval_error > tolerance:
                raise AssertionError(
                    ("random", level, trial, error, parseval_error)
                )
        print(
            f"random ell={level:2d} trials={args.random_trials} "
            "all logarithmic identities passed"
        )


if __name__ == "__main__":
    main()
