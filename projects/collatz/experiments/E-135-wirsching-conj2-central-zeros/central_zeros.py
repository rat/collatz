#!/usr/bin/env python3
"""Central-cost zero sets of Wirsching's generators g_ell(k,a).

Wirsching (2003), equation (2.1), defines

    g_0(k,a) = [k = 0][a in Z_3],
    g_(ell+1)(k,a) = sum_{0<=j<2*3^ell} g_ell(k-j, (2^(j+1) a - 1)/3).

Condition (?3) of his Theorem 2 asks for constants delta, mu > 0 and an
index ell_0 such that

    g_ell(k_ell, a) >= mu * gbar_ell(k_ell)

holds for every unit residue a, every ell >= ell_0 and every sequence
(k_ell) with |ell - k_ell| <= delta*sqrt(ell).  The constant sequence
k_ell = ell is admissible for every delta > 0, so a single unit residue
with g_ell(ell,a) = 0 at some level ell >= ell_0 falsifies (?3) at that
level.  If such residues exist at every level, no ell_0 works and (?3)
is false.

This script computes, exactly and for every unit residue modulo 3^ell,
the Boolean support of g_ell(., a) up to a cost ceiling, and reports:

  * the zero set Z_ell = {a unit : g_ell(ell,a) = 0} and its size;
  * the least cost whose support is all units, and its excess over ell;
  * whether the zeros are coherent, that is whether a residue in
    Z_(ell+1) reduces modulo 3^ell into Z_ell.  A coherent chain would
    single out a 3-adic integer that is never centrally reachable.

The forward recursion is the one used in E-115: a residue b modulo
3^(ell-1) carrying cost c contributes cost c+j to the residue
(3b+1) * 2^(-(j+1)) modulo 3^ell.  This is exactly equation (2.1) read
in the opposite direction, and it needs no divisibility test.

Support is packed one bit per cost into an unsigned integer per
residue, so the memory footprint is one word per residue instead of one
byte per (cost, residue) pair.
"""

from __future__ import annotations

import argparse
import time

import numpy as np

CHUNK = 1 << 25


def word_dtype(cost_ceiling: int):
    if cost_ceiling < 32:
        return np.uint32
    if cost_ceiling < 64:
        return np.uint64
    raise ValueError("cost ceiling must be below 64")


def extend(previous: np.ndarray, ell: int, cost_ceiling: int) -> np.ndarray:
    """One level of the recursion on packed support words."""
    modulus = 3**ell
    old_modulus = modulus // 3
    dtype = previous.dtype
    current = np.zeros(modulus, dtype=dtype)
    cap = 2 * old_modulus
    inv2 = pow(2, -1, modulus)
    full = np.array(
        (1 << (cost_ceiling + 1)) - 1 if cost_ceiling < 63 else -1,
        dtype=dtype,
    )
    inverse_power = 1
    for increment in range(min(cost_ceiling, cap - 1) + 1):
        inverse_power = (inverse_power * inv2) % modulus
        shift = np.array(increment, dtype=dtype)
        for start in range(0, old_modulus, CHUNK):
            stop = min(start + CHUNK, old_modulus)
            source = previous[start:stop]
            live = source != 0
            if not live.any():
                continue
            base = np.arange(start, stop, dtype=np.int64)[live]
            targets = ((3 * base + 1) % modulus) * inverse_power % modulus
            current[targets] |= (source[live] << shift) & full
    return current


def reference_hit(level: int, cost: int, residue: int) -> bool:
    """Independent backward predicate, the one used in E-121."""
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def hit(lv: int, c: int, r: int) -> bool:
        if lv == 0:
            return c == 0
        if c < 0:
            return False
        modulus = 3**lv
        old_modulus = modulus // 3
        cap = 2 * old_modulus
        r %= modulus
        for inc in range(min(c, cap - 1) + 1):
            numerator = pow(2, inc + 1, modulus) * r - 1
            if numerator % 3:
                continue
            if hit(lv - 1, c - inc, (numerator // 3) % old_modulus):
                return True
        return False

    return hit(level, cost, residue)


def audit(support: np.ndarray, ell: int, cost_ceiling: int, samples: int,
          seed: int) -> None:
    """Compare the packed table with the backward predicate."""
    rng = np.random.default_rng(seed)
    modulus = 3**ell
    picks = rng.integers(0, modulus, size=samples)
    for residue in picks:
        residue = int(residue)
        if residue % 3 == 0:
            continue
        word = int(support[residue])
        for cost in range(cost_ceiling + 1):
            got = bool(word >> cost & 1)
            want = reference_hit(ell, cost, residue)
            if got != want:
                raise AssertionError(
                    f"mismatch ell={ell} a={residue} k={cost} "
                    f"packed={got} reference={want}"
                )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-ell", type=int, default=18)
    parser.add_argument("--cost-ceiling", type=int, default=31)
    parser.add_argument("--audit-ell", type=int, default=7,
                        help="levels up to this value are audited against "
                             "the independent backward predicate")
    parser.add_argument("--audit-samples", type=int, default=40)
    parser.add_argument("--witnesses", type=int, default=3,
                        help="coherent zeros re-checked at every level with "
                             "the backward predicate")
    args = parser.parse_args()

    dtype = word_dtype(args.cost_ceiling)
    support = np.zeros(1, dtype=dtype)
    support[0] = 1  # level 0: cost 0 only

    previous_zeros: np.ndarray | None = None
    coherent: np.ndarray | None = None

    print(f"cost ceiling {args.cost_ceiling}, word dtype {dtype.__name__}")
    header = (
        "ell  units        |Z_ell|  frac_zero   first_full  excess  "
        "lifted  coherent"
    )
    print(header)
    print("-" * len(header))

    for ell in range(1, args.max_ell + 1):
        started = time.time()
        support = extend(support, ell, args.cost_ceiling)
        modulus = 3**ell
        if ell <= args.audit_ell:
            audit(support, ell, args.cost_ceiling, args.audit_samples,
                  seed=ell)

        unit = np.tile(np.array([False, True, True]), modulus // 3)
        n_units = int(unit.sum())

        # cost exactly ell
        if args.cost_ceiling < ell:
            print(f"ell={ell}: cost ceiling below ell, stopping")
            break
        central_bit = np.array(1 << ell, dtype=dtype)
        reachable = (support & central_bit) != 0
        zeros = unit & ~reachable
        n_zeros = int(zeros.sum())

        # least cost whose support covers every unit
        first_full = None
        unit_support = support[unit]
        covered = np.bitwise_and.reduce(unit_support)
        del unit_support
        for cost in range(args.cost_ceiling + 1):
            if int(covered) >> cost & 1:
                first_full = cost
                break

        # do level-(ell) zeros reduce into level-(ell-1) zeros?
        lifted = "-"
        coherent_size = "-"
        if previous_zeros is not None:
            idx = np.flatnonzero(zeros)
            if idx.size:
                parents = idx % (modulus // 3)
                lifted = f"{int(previous_zeros[parents].sum())}"
                if coherent is not None:
                    keep = coherent[parents]
                    coherent_new = np.zeros(modulus, dtype=bool)
                    coherent_new[idx[keep]] = True
                    coherent = coherent_new
                    coherent_size = f"{int(coherent.sum())}"
            else:
                lifted = "0"
                coherent = np.zeros(modulus, dtype=bool)
                coherent_size = "0"
        else:
            coherent = zeros.copy()
            coherent_size = f"{n_zeros}"

        previous_zeros = zeros
        witnesses = (
            np.flatnonzero(coherent)[: args.witnesses]
            if coherent is not None
            else np.array([], dtype=np.int64)
        )
        for witness in witnesses:
            witness = int(witness)
            for level in range(1, ell + 1):
                if reference_hit(level, level, witness % 3**level):
                    raise AssertionError(
                        f"claimed coherent zero {witness} mod 3^{ell} is "
                        f"centrally reachable at level {level}"
                    )
        excess = "-" if first_full is None else f"{first_full - ell:+d}"
        print(
            f"{ell:3d} {n_units:12d} {n_zeros:12d} "
            f"{n_zeros / n_units:10.6f}  "
            f"{'none' if first_full is None else first_full:>10} "
            f"{excess:>6}  {lifted:>6}  {coherent_size:>8}"
            f"   [{time.time() - started:6.1f}s]",
            flush=True,
        )


if __name__ == "__main__":
    main()
