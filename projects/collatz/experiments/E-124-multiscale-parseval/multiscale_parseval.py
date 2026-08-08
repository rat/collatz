#!/usr/bin/env python3
"""Checks K_ell-K_(ell-1) = primitive Fourier energy."""

import argparse
import importlib.util
from pathlib import Path

import numpy as np


def load_syracuse_solver():
    path = (
        Path(__file__).parents[1]
        / "E-100-syracuse-collision-mass-k-ell"
        / "experiment_k_ell.py"
    )
    spec = importlib.util.spec_from_file_location("e100_solver", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.solve_level


def primitive_energy(law):
    transform = np.fft.fft(law)
    primitive = np.arange(len(law)) % 3 != 0
    return float(np.sum(np.abs(transform[primitive]) ** 2))


def collision(law):
    return len(law) * float(np.sum(law**2))


def random_refinement(previous, rng):
    old_modulus = len(previous)
    current = np.zeros(3 * old_modulus)
    weights = rng.dirichlet(np.ones(3), size=old_modulus)
    for digit in range(3):
        current[digit * old_modulus : (digit + 1) * old_modulus] = (
            previous * weights[:, digit]
        )
    assert np.max(
        np.abs(
            current[:old_modulus]
            + current[old_modulus : 2 * old_modulus]
            + current[2 * old_modulus :]
            - previous
        )
    ) < 1e-15
    return current


def check_sequence(laws, name, tolerance=3e-10):
    previous_collision = 1.0
    cumulative = 1.0
    for level, law in enumerate(laws, start=1):
        current_collision = collision(law)
        energy = primitive_energy(law)
        increment_error = abs(
            current_collision - previous_collision - energy
        )
        cumulative += energy
        telescoping_error = abs(current_collision - cumulative)
        if max(increment_error, telescoping_error) > tolerance:
            raise AssertionError(
                (name, level, increment_error, telescoping_error)
            )
        print(
            f"{name} ell={level:2d} K={current_collision:.12g} "
            f"E_prim={energy:.12g} increment_error={increment_error:.3e} "
            f"telescoping_error={telescoping_error:.3e}"
        )
        previous_collision = current_collision


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-level", type=int, default=12)
    parser.add_argument("--seed", type=int, default=155)
    args = parser.parse_args()

    solve_level = load_syracuse_solver()
    syracuse = np.zeros(3)
    syracuse[1] = 1.0 / 3.0
    syracuse[2] = 2.0 / 3.0
    syracuse_laws = [syracuse]
    for level in range(2, args.max_level + 1):
        syracuse = solve_level(syracuse, level)
        syracuse_laws.append(syracuse)
    check_sequence(syracuse_laws, "syracuse")

    rng = np.random.default_rng(args.seed)
    random_laws = []
    random_law = np.array([1.0])
    for _ in range(args.max_level):
        random_law = random_refinement(random_law, rng)
        random_laws.append(random_law)
    check_sequence(random_laws, "random")


if __name__ == "__main__":
    main()
