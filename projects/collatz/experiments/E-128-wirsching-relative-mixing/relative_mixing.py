#!/usr/bin/env python3
"""Exact finite-level diagnostics for Wirsching relative mixing."""

import argparse
import importlib.util
from math import isqrt
from pathlib import Path

import numpy as np


def load_functions():
    path = (
        Path(__file__).parents[1]
        / "E-115-wirsching-microcanonical-multiplicity"
        / "microcanonical_multiplicity.py"
    )
    spec = importlib.util.spec_from_file_location("microcanonical", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.extend, module.bounded_composition_counts


def report(table, ell, offset):
    cost = ell + offset * isqrt(ell)
    units = np.arange(3**ell) % 3 != 0
    row = table[cost, units].astype(np.float64)
    total = float(row.sum())
    count = row.size
    if total == 0:
        print(f"ell={ell:2d} offset={offset:+d} k={cost:2d} empty_row=True")
        return
    ratios = count * row / total
    tv = 0.5 * float(np.mean(np.abs(ratios - 1.0)))
    collision = float(np.mean(ratios**2))
    quantiles = np.quantile(ratios, [0.5, 0.9, 0.99])
    all_units = np.flatnonzero(units)
    class_one = float(row[all_units % 3 == 1].sum() / total)
    class_two = float(row[all_units % 3 == 2].sum() / total)
    coarse_tv = abs(class_one - 0.5)
    print(
        f"ell={ell:2d} offset={offset:+d} k={cost:2d} "
        f"support={np.count_nonzero(row)/count:.9f} "
        f"min_ratio={ratios.min():.6g} max_ratio={ratios.max():.6g} "
        f"sup_defect={np.max(np.abs(ratios-1)):.6g} tv={tv:.6g} "
        f"collision={collision:.6g} mod3=({class_one:.6g},{class_two:.6g}) "
        f"coarse_tv={coarse_tv:.6g} q50={quantiles[0]:.6g} "
        f"q90={quantiles[1]:.6g} q99={quantiles[2]:.6g}"
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-level", type=int, default=12)
    parser.add_argument("--offsets", type=int, nargs="+", default=[-1, 0, 1])
    args = parser.parse_args()

    extend, bounded_counts = load_functions()
    radius = max(abs(value) for value in args.offsets)
    cost_max = args.max_level + radius * isqrt(args.max_level) + 2
    table = np.zeros((cost_max + 1, 1), dtype=np.int64)
    table[0, 0] = 1
    for ell in range(1, args.max_level + 1):
        table = extend(table, ell, cost_max)
        totals = table.sum(axis=1)
        expected = np.array(bounded_counts(ell, cost_max), dtype=np.int64)
        if not np.array_equal(totals, expected):
            raise AssertionError((ell, "composition total mismatch"))
        for offset in args.offsets:
            cost = ell + offset * isqrt(ell)
            if 0 <= cost <= cost_max:
                report(table, ell, offset)


if __name__ == "__main__":
    main()
