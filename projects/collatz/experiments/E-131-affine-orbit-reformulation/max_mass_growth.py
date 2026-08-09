#!/usr/bin/env python3
"""Growth rate of the maximum point mass M_ell = max_u mu_ell(u).

Needed to assess H-161's direction (B) ("beta_eff -> 1 implies no long
deficient arc"): that direction's proof sketch bounds the tail of the
window sum G(k) beyond an observed short arc using max_u N_(ell-1)(u)
(N_ell(u) := 3^ell mu_ell(u)). A one-line induction on the recursion
mu_ell(y) = 1/2 nu(2y) + 1/2 mu_ell(2y) gives M_ell <= (2/3) M_(ell-1)
(only half the terms, by parity, contribute at most M_(ell-1) each,
worst-case phase), hence M_ell <= (2/3)^ell, i.e. N_max <= 2^ell always.
This script checks that bound and measures the actual growth rate,
which turns out to be much closer to (3/2)^ell than to 2^ell -- still
exponential, just with a better base than the a priori bound.
"""

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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-level", type=int, default=16)
    args = parser.parse_args()

    next_distribution = load_next_distribution()
    previous = np.array([1.0])
    prev_n_max = None
    print("ell  M_ell           bound_(2/3)^ell  N_max=3^ell*M_ell  "
          "ratio_to_previous  log(N_max)/ell")
    for ell in range(1, args.max_level + 1):
        previous = next_distribution(previous, ell)
        M = float(previous.max())
        bound = (2.0 / 3.0) ** ell
        n_max = 3.0**ell * M
        ratio = n_max / prev_n_max if prev_n_max else float("nan")
        if M > bound * (1 + 1e-9):
            raise AssertionError((ell, M, bound))
        print(
            f"{ell:3d}  {M:.10e}  {bound:.10e}  {n_max:14.4f}  "
            f"{ratio:10.4f}  {math.log(n_max) / ell:.5f}"
        )
        prev_n_max = n_max


if __name__ == "__main__":
    main()
