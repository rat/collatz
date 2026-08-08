#!/usr/bin/env python3
"""Large-deviation mass below the Weak Covering cost threshold."""

import argparse
import math


def log_add(x, y):
    if x == -math.inf:
        return y
    if y == -math.inf:
        return x
    maximum = max(x, y)
    return maximum + math.log(math.exp(x - maximum) + math.exp(y - maximum))


def log_cost_tail(level, cutoff):
    """Log P(A_1+...+A_level <= cutoff), P(A=m)=2^-m."""
    total = -math.inf
    for cost in range(level, cutoff + 1):
        log_probability = (
            math.lgamma(cost)
            - math.lgamma(level)
            - math.lgamma(cost - level + 1)
            - cost * math.log(2.0)
        )
        total = log_add(total, log_probability)
    return total


def rate(slope):
    return (
        slope * math.log(2.0)
        + (slope - 1.0) * math.log(slope - 1.0)
        - slope * math.log(slope)
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--levels", type=int, nargs="*", default=(20, 50, 100, 200, 500, 1000)
    )
    args = parser.parse_args()
    if abs(math.exp(log_cost_tail(2, 3)) - 0.5) > 1e-14:
        raise RuntimeError("negative-binomial base-case validation failed")
    slope = 1.0 + math.log(3.0, 4.0)
    predicted = rate(slope)
    print(f"slope={slope:.12f} I(slope)={predicted:.12f}")
    print("ell cutoff -log(tail)/ell beta_average")
    for level in args.levels:
        cutoff = math.floor(slope * level)
        log_tail = log_cost_tail(level, cutoff)
        observed = -log_tail / level
        beta_average = 1.0 + observed / math.log(3.0)
        print(f"{level:4d} {cutoff:6d} {observed:.12f} {beta_average:.12f}")


if __name__ == "__main__":
    main()
