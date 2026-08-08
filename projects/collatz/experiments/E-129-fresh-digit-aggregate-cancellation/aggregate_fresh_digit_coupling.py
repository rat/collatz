#!/usr/bin/env python3
"""Does the fresh-digit coupling of E-120 cancel after aggregating over
the natural branching weight on the sibling gap Delta, or does it
survive aggregation?

H-150/E-120 prove that for any FIXED sibling gap delta, the joint law
of the next `fresh` base-3 digits of two sibling coordinates is
maximally coupled: TV(joint, product of marginals) = 1-3^-fresh,
independent of delta. That refutes pairwise independence for any
single pair. H-159 needs a different, weaker target: whether the
dependence measured against the AGGREGATE joint law, mixed over the
actual branching measure on delta (E-108's P(Delta=2k)=3*4^-k), shrinks
toward zero as fresh and the truncation depth grow, or whether it is
bounded away from zero, which would obstruct any i.i.d.-tail transfer
by aggregation alone.

This script computes that aggregate joint exactly (finite sums, no
sampling) and reports its TV distance and mutual information against
the product of its own marginals, for a range of fresh depths and
truncation levels of the delta sum.
"""

import argparse
from fractions import Fraction

import numpy as np


def delta_weight(k, k_max):
    """P(Delta=2k) = 3*4^-k (E-108), renormalized over k=1..k_max."""
    raw = [3.0 * 4.0 ** (-j) for j in range(1, k_max + 1)]
    total = sum(raw)
    return raw[k - 1] / total


def single_delta_joint(delta, coarse, fresh):
    """Joint law of (next `fresh` digits of x, next `fresh` digits of
    y) for the fixed affine sibling relation of gap `delta`, exactly as
    in E-120's check(). Fixes x0=1; verified separately (see README)
    that TV and mutual information do not depend on which unit residue
    x0 mod 3^coarse is chosen, so this is the correct conditional law,
    not an artifact of one arbitrary representative."""
    modulus = 3 ** (coarse + fresh)
    coarse_modulus = 3**coarse
    block_size = 3**fresh
    multiplier = pow(2, delta, modulus)
    shift = (2**delta - 1) // 3
    x0 = 1
    y0 = (multiplier * x0 + shift) % coarse_modulus
    joint = np.zeros((block_size, block_size), dtype=np.float64)
    for x_block in range(block_size):
        x = x0 + coarse_modulus * x_block
        y = (multiplier * x + shift) % modulus
        if y % coarse_modulus != y0:
            raise RuntimeError("coarse affine class changed")
        y_block = ((y - y0) // coarse_modulus) % block_size
        joint[x_block, y_block] += 1.0 / block_size
    return joint


def aggregate_joint(coarse, fresh, k_max):
    block_size = 3**fresh
    joint = np.zeros((block_size, block_size), dtype=np.float64)
    for k in range(1, k_max + 1):
        delta = 2 * k
        weight = delta_weight(k, k_max)
        joint += weight * single_delta_joint(delta, coarse, fresh)
    return joint


def tv_and_mi(joint):
    marginal_x = joint.sum(axis=1)
    marginal_y = joint.sum(axis=0)
    product = np.outer(marginal_x, marginal_y)
    tv = 0.5 * float(np.abs(joint - product).sum())
    positive = joint > 0
    mutual_information = float(
        np.sum(joint[positive] * np.log(joint[positive] / product[positive]))
    )
    return tv, mutual_information, float(marginal_x.max() - marginal_x.min())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--coarse", type=int, default=1)
    parser.add_argument("--max-fresh", type=int, default=6)
    parser.add_argument("--k-max-list", type=int, nargs="+", default=[3, 6, 10, 16])
    args = parser.parse_args()

    print("coarse fresh k_max TV mutual_information marginal_deviation "
          "single_delta_TV single_delta_MI")
    for fresh in range(1, args.max_fresh + 1):
        single = single_delta_joint(2, args.coarse, fresh)
        single_tv, single_mi, _ = tv_and_mi(single)
        for k_max in args.k_max_list:
            joint = aggregate_joint(args.coarse, fresh, k_max)
            tv, mi, marginal_dev = tv_and_mi(joint)
            print(
                f"{args.coarse:6d} {fresh:5d} {k_max:5d} "
                f"{tv:.12f} {mi:.12f} {marginal_dev:.3e} "
                f"{single_tv:.12f} {single_mi:.12f}"
            )

    print()
    print("Reference (E-108): P(Delta=2k)=3*4^-k, tail past k_max is "
          "3*(1/4)^k_max/(1-1/4) of the untruncated total, so larger "
          "k_max only refines the weighting, it does not change which "
          "regime the aggregate falls into.")


if __name__ == "__main__":
    main()
