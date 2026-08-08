#!/usr/bin/env python3
"""Exact fresh-digit coupling induced by an affine sibling relation."""

import argparse
import math

import numpy as np


def check(delta, coarse, fresh):
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
    marginal_x = joint.sum(axis=1)
    marginal_y = joint.sum(axis=0)
    product = np.outer(marginal_x, marginal_y)
    tv = 0.5 * float(np.abs(joint - product).sum())
    positive = joint > 0
    mutual_information = float(
        np.sum(joint[positive] * np.log(joint[positive] / product[positive]))
    )
    expected_tv = 1.0 - 1.0 / block_size
    expected_mi = fresh * math.log(3.0)
    if abs(tv - expected_tv) > 1e-12:
        raise RuntimeError("total-variation identity failed")
    if abs(mutual_information - expected_mi) > 1e-12:
        raise RuntimeError("mutual-information identity failed")
    return tv, mutual_information


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-fresh", type=int, default=6)
    args = parser.parse_args()
    print("delta coarse fresh TV mutual_information")
    for delta, coarse in ((2, 1), (4, 2), (8, 3)):
        for fresh in range(1, args.max_fresh + 1):
            tv, mutual_information = check(delta, coarse, fresh)
            print(
                f"{delta:5d} {coarse:6d} {fresh:5d} "
                f"{tv:.12f} {mutual_information:.12f}"
            )


if __name__ == "__main__":
    main()

