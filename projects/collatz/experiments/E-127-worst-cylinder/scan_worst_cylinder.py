#!/usr/bin/env python3
"""Extend the worst-cylinder scan without running the cost DP."""

import argparse
import importlib.util
import math
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


def discrete_log_two(value, modulus):
    period = 2 * (modulus // 3)
    current = 1
    for exponent in range(period):
        if current == value:
            return exponent
        current = (2 * current) % modulus
    raise AssertionError((value, modulus))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-level", type=int, default=15)
    args = parser.parse_args()

    next_distribution = load_next_distribution()
    law = np.array([1.0])
    rows = []
    print(
        "ell c_ell beta_eff normalized argmin log2_argmin "
        "same_parent loss_over_log_ell"
    )
    previous_argmin = None
    for level in range(1, args.max_level + 1):
        law = next_distribution(law, level)
        modulus = 3**level
        units = np.flatnonzero(np.arange(modulus) % 3 != 0)
        probabilities = law[units]
        position = int(np.argmin(probabilities))
        minimum = float(probabilities[position])
        argmin = int(units[position])
        normalized = modulus * minimum
        beta = -math.log(minimum) / (level * math.log(3))
        log_index = discrete_log_two(argmin, modulus)
        same_parent = (
            previous_argmin is not None
            and argmin % (modulus // 3) == previous_argmin
        )
        loss_over_log = (
            -math.log(normalized) / math.log(level) if level > 1 else 0.0
        )
        print(
            f"{level:2d} {minimum:.14e} {beta:.9f} {normalized:.9e} "
            f"{argmin:8d} {log_index:8d} {str(same_parent):>5s} "
            f"{loss_over_log:.6f}"
        )
        rows.append((level, normalized))
        previous_argmin = argmin

    fit_rows = [(ell, value) for ell, value in rows if ell >= 6]
    x = np.log([ell for ell, _ in fit_rows])
    y = np.log([value for _, value in fit_rows])
    slope, intercept = np.polyfit(x, y, 1)
    print(
        "diagnostic power fit on ell>=6: "
        f"3^ell*c_ell ~= exp({intercept:.6f})*ell^({slope:.6f})"
    )
    print("The fit is descriptive finite-level evidence, not an asymptotic claim.")


if __name__ == "__main__":
    main()
