#!/usr/bin/env python3
"""Decompose the worst-cylinder mass c_ell by cost band (H-158 step 3).

The Tao memoryless recursion mu_ell(y) = 1/2 nu(2y) + 1/2 mu_ell(2y),
unrolled to a geometric tail, gives

    mu_ell(y) = sum_{s=0}^{tail-1} 2^-(s+1) * nu(2^-(s+1) y mod 3^ell).

Term s is the contribution from paths that take exactly s+1 extra
doubling steps before landing in the previous level's law nu. This is
the natural cost coordinate available without running the exponential
min-cost DP (E-111's reachable_w), which is exactly what E-127 already
avoids running at these levels.

The 2^-(s+1) prefactor decays geometrically for every residue, so a
plain cumulative-fraction count is not informative by itself: it would
saturate quickly no matter which residue is examined. The informative
comparison is against a control: this script reports the same
statistic for the minimum-mass residue (E-127's argmin, i.e. c_ell),
the maximum-mass residue, and a residue of median mass, at the same
level. The three differ sharply: the maximum-mass residue is
essentially a single term (s=0 alone already exceeds 90% of its
total), while the minimum-mass residue needs contributions from
several cost bands to reach the same cumulative fractions. That
contrast, not the absolute s values, is the finding.
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


def level_terms(previous, level, tail):
    """Term[s, position] for every position on the multiply-by-2 orbit,
    and the orbit itself. distribution is the full mu_ell (returned
    so the caller can feed it back in as next level's `previous`,
    exactly as weighted_bridge.scan_weighted does)."""
    modulus = 3**level
    period = 2 * 3 ** (level - 1)
    nu = np.zeros(modulus, dtype=np.float64)
    nu[1 + 3 * np.arange(previous.size)] = previous

    orbit = np.empty(period, dtype=np.int64)
    orbit[0] = 1
    for k in range(1, period):
        orbit[k] = (2 * orbit[k - 1]) % modulus
    along = nu[orbit]

    values = np.zeros(period, dtype=np.float64)
    terms = np.zeros((tail, period), dtype=np.float64)
    for s in range(tail):
        term = 2.0 ** (-(s + 1)) * np.roll(along, -(s + 1))
        terms[s] = term
        values += term

    distribution = np.zeros(modulus, dtype=np.float64)
    distribution[orbit] = values
    return distribution, orbit, values, terms


def summarize(term_series, total):
    cumulative = np.cumsum(term_series)
    fractions = {}
    for target in (0.5, 0.9, 0.99):
        threshold = target * total
        reached = np.flatnonzero(cumulative >= threshold)
        fractions[target] = int(reached[0]) if reached.size else -1
    return fractions


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-level", type=int, default=15)
    parser.add_argument("--tail", type=int, default=120)
    args = parser.parse_args()

    next_distribution = load_next_distribution()
    previous = np.array([1.0])
    print(
        "ell which value s_for_50pct s_for_90pct s_for_99pct"
    )
    for level in range(1, args.max_level + 1):
        distribution, orbit, values, terms = level_terms(
            previous, level, args.tail
        )
        units_mask = (orbit % 3) != 0
        unit_positions = np.flatnonzero(units_mask)

        min_pos = unit_positions[np.argmin(values[unit_positions])]
        max_pos = unit_positions[np.argmax(values[unit_positions])]
        order = np.argsort(values[unit_positions])
        median_pos = unit_positions[order[len(order) // 2]]

        for name, pos in (("min", min_pos), ("median", median_pos), ("max", max_pos)):
            total = values[pos]
            fractions = summarize(terms[:, pos], total)
            print(
                f"{level:3d} {name:6s} {total:.6e} "
                f"{fractions[0.5]:11d} {fractions[0.9]:11d} "
                f"{fractions[0.99]:11d}"
            )
        previous = next_distribution(previous, level)

    print()
    print(
        "s indexes 'extra doubling steps before the previous level's "
        "law'. Descriptive only, at the levels tested; not a claim "
        "about the min-cost DP's cost variable or an asymptotic trend."
    )


if __name__ == "__main__":
    main()
