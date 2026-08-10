#!/usr/bin/env python3
"""Quantitative part of Wirsching's condition (?3).

Condition (?3) has two independent halves.  The first is support: every
unit residue must satisfy g_ell(k,a) > 0.  The second is quantitative:
the ratio

    R_ell(k) = min_a g_ell(k,a) / gbar_ell(k),
    gbar_ell(k) = (sum_a g_ell(k,a)) / (2*3^(ell-1)),

must stay above a fixed mu > 0.  `central_zeros.py` handles the first
half.  This script handles the second, using exact integer counts from
the same forward recursion.

Costs are reported at k = ell (the centre of Wirsching's window, where
the support is still incomplete on every level reached here) and at the
first cost whose support is complete, which through ell = 18 is ell + 5.
The point of the second column is that support and positivity are
different obstructions: R_ell can decay to zero even after the support
has filled in, and no analytic statement about the limiting operator
W_3 can see either half.

The row sum is checked at every level against the independent count of
bounded compositions of k with capacities 2, 6, 18, ..., 2*3^(ell-1),
which is Wirsching's identity 2*3^(ell-1)*gbar_ell(k).
"""

from __future__ import annotations

import argparse
import time
from math import isqrt

import numpy as np


def bounded_composition_counts(ell: int, k_max: int) -> np.ndarray:
    """Number of (j_1,...,j_ell) with 0 <= j_i < 2*3^(i-1) and sum = k."""
    counts = np.zeros(k_max + 1, dtype=object)
    counts[0] = 1
    for index in range(1, ell + 1):
        cap = 2 * 3 ** (index - 1)
        prefix = np.zeros(k_max + 2, dtype=object)
        running = 0
        for cost in range(k_max + 1):
            running += counts[cost]
            prefix[cost + 1] = running
        updated = np.zeros(k_max + 1, dtype=object)
        for cost in range(k_max + 1):
            low = max(0, cost - cap + 1)
            updated[cost] = prefix[cost + 1] - prefix[low]
        counts = updated
    return counts


def extend(previous: np.ndarray, ell: int, k_max: int) -> np.ndarray:
    modulus = 3**ell
    old_modulus = modulus // 3
    current = np.zeros((k_max + 1, modulus), dtype=np.int64)
    residues = np.arange(old_modulus, dtype=np.int64)
    cap = 2 * old_modulus
    inv2 = pow(2, -1, modulus)
    inverse_power = 1
    for increment in range(min(k_max, cap - 1) + 1):
        inverse_power = (inverse_power * inv2) % modulus
        targets = ((3 * residues + 1) % modulus) * inverse_power % modulus
        for old_cost in range(k_max - increment + 1):
            current[old_cost + increment, targets] += previous[old_cost]
    return current


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-ell", type=int, default=14)
    parser.add_argument("--offsets", type=int, nargs="+",
                        default=[0, 4, 5, 6, 7, 8, 10, 12],
                        help="reported costs are ell + offset")
    parser.add_argument("--sqrt-multiples", type=int, nargs="+",
                        default=[1, 2, 3],
                        help="extra columns at ell + u*isqrt(ell)")
    parser.add_argument("--fixed-residues", type=int, nargs="+",
                        default=[1, 2, 4, 5, 7, 8, 10, 11],
                        help="small integers a tracked separately; "
                             "Theorem 1 only consumes integer a")
    parser.add_argument("--fixed-offset", type=int, default=0,
                        help="cost offset used for the fixed-residue column")
    parser.add_argument("--random-fixed", type=int, default=0,
                        help="add this many random integers below "
                             "--random-bound to the tracked set")
    parser.add_argument("--random-bound", type=int, default=3**8)
    parser.add_argument("--seed", type=int, default=20260809)
    args = parser.parse_args()

    tracked = list(args.fixed_residues)
    if args.random_fixed:
        rng = np.random.default_rng(args.seed)
        pool = np.arange(1, args.random_bound)
        pool = pool[pool % 3 != 0]
        extra = rng.choice(pool, size=args.random_fixed, replace=False)
        tracked = sorted(set(tracked) | {int(v) for v in extra})

    offsets = sorted(args.offsets)
    multiples = args.sqrt_multiples
    k_max = args.max_ell + max(
        offsets[-1], max(multiples) * isqrt(args.max_ell)
    )
    table = np.zeros((k_max + 1, 1), dtype=np.int64)
    table[0, 0] = 1

    print("min_a g_ell(ell+d, a) / gbar_ell(ell+d); "
          "a dash marks an incomplete support")
    header = ("ell " + " ".join(f"   d={d:<+3d}" for d in offsets)
              + "  |" + " ".join(f"  d={u}rt " for u in multiples)
              + f"  || min over {len(tracked)} fixed integers"
              + f" at d={args.fixed_offset:+d}")
    print(header)
    print("-" * len(header))

    for ell in range(1, args.max_ell + 1):
        started = time.time()
        table = extend(table, ell, k_max)
        modulus = 3**ell
        unit = np.tile(np.array([False, True, True]), modulus // 3)
        n_units = int(unit.sum())

        reference = bounded_composition_counts(ell, k_max)
        fields = []
        columns = list(offsets) + [None] + [u * isqrt(ell) for u in multiples]
        for offset in columns:
            if offset is None:
                fields.append(" |")
                continue
            cost = ell + offset
            if cost > k_max:
                fields.append("      .")
                continue
            row = table[cost][unit]
            total = int(row.sum())
            if total != int(reference[cost]):
                raise AssertionError(
                    f"row total mismatch ell={ell} k={cost}: "
                    f"{total} != {int(reference[cost])}"
                )
            mean = total / n_units
            smallest = int(row.min())
            if smallest == 0:
                fields.append("      -")
            else:
                fields.append(f"{smallest / mean:7.4f}")

        cost = ell + args.fixed_offset
        if 0 <= cost <= k_max:
            mean = int(reference[cost]) / n_units
            picks = [a for a in tracked if a % 3 and a < modulus]
            values = [int(table[cost, a]) for a in picks]
            worst = min(values) / mean if picks and mean else float("nan")
            report = f"  || {worst:8.4f} ({len(picks):3d})"
        else:
            report = "  ||        ."

        print(f"{ell:3d} " + " ".join(fields) + report
              + f"   [{time.time() - started:6.1f}s]", flush=True)


if __name__ == "__main__":
    main()
