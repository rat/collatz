#!/usr/bin/env python3
"""E-141 (H-162): where does the path-index-averaged pairing S_1(xi)
conj(S_2(xi)) sit, by conductor, at fixed v?

H-159/E-133 show the diagonal coefficient D(xi) = E[e(xi(X-Y))] of a
sibling pair cancels above conductor 3^(1+v3(k)) (k = Delta/2) once
averaged over the FREE ARITHMETIC PARAMETER t. H-162 asks whether the
SAME localization by conductor holds for the different average O1
actually needs: over PATH INDICES within each subtree, at a single
FIXED v (no t to average over).

This reuses E-140's S_1(xi), S_2(xi) (real branch weights, fixed v,
full weighted enumeration of the sibling subtrees below v, vectorised
with per-level residue deduplication) and adds a conductor breakdown:
group xi != 0 by conductor 3^r (r = ell - v3(xi), the standard
graduation of H-154/H-155/E-133), and report where
sum_{xi: cond(xi)=3^r} S_1(xi)*conj(S_2(xi)) concentrates, against the
E-133 prediction r = 1 + v3(k), k = (a2-a1)/2.

The S_i functions and the correctness check that fast enumeration
matches slow brute-force enumeration are copied verbatim from E-140
(not re-derived), since that check is the expensive part to get right
and E-140 already paid for it.
"""

import argparse
import math

import numpy as np


def predecessor(v, a, allow_multiple_of_three=False):
    num = (1 << a) * v - 1
    if num % 3 != 0:
        return None
    w = num // 3
    if w <= 0 or w % 2 == 0:
        return None
    if w % 3 == 0 and not allow_multiple_of_three:
        return None
    return w


def admissible_first_steps(v, n, max_a=200):
    """The n smallest admissible first-step exponents at v."""
    found = []
    for a in range(1, max_a + 1):
        if predecessor(v, a) is not None:
            found.append(a)
            if len(found) == n:
                return found
    raise RuntimeError(f"fewer than {n} admissible first steps at v={v}")


def enumerate_subtree_slow(root, depth, max_exp):
    live = [(root, 1.0)]
    for _ in range(depth):
        nxt = []
        for w, wt in live:
            for a in range(1, max_exp + 1):
                child = predecessor(w, a)
                if child is not None:
                    nxt.append((child, wt * 2.0 ** (-a)))
        live = nxt
    return live


def enumerate_subtree_fast(root, depth, ell, max_exp):
    m_final = 3 ** ell
    if depth == 0:
        hist = np.zeros(m_final, dtype=np.float64)
        hist[root % m_final] += 1.0
        return hist
    m_start = 3 ** (ell + depth)
    res = np.array([root % m_start], dtype=np.int64)
    wt = np.array([1.0], dtype=np.float64)
    m_cur = m_start
    for _ in range(depth):
        m_next = m_cur // 3
        new_res_parts, new_wt_parts = [], []
        for a in range(1, max_exp + 1):
            pow2a = pow(2, a, m_cur)
            num = (pow2a * res - 1) % m_cur
            divisible = num % 3 == 0
            if not np.any(divisible):
                continue
            child = num[divisible] // 3
            child_ok = child % 3 != 0
            if not np.any(child_ok):
                continue
            new_res_parts.append(child[child_ok])
            new_wt_parts.append(wt[divisible][child_ok] * (2.0 ** (-a)))
        if not new_res_parts:
            res = np.array([], dtype=np.int64)
            wt = np.array([], dtype=np.float64)
            m_cur = m_next
            break
        res = np.concatenate(new_res_parts)
        wt = np.concatenate(new_wt_parts)
        uniq, inv = np.unique(res, return_inverse=True)
        wt = np.bincount(inv, weights=wt, minlength=uniq.size)
        res = uniq
        m_cur = m_next
    assert m_cur == m_final, (m_cur, m_final)
    hist = np.zeros(m_final, dtype=np.float64)
    if res.size:
        np.add.at(hist, res % m_final, wt)
    return hist


def character_sum_from_hist(hist):
    return np.conj(np.fft.fft(hist))


def _check_fast_matches_slow():
    for root, depth, ell, max_exp in [(1, 3, 3, 10), (5, 4, 4, 8)]:
        slow = enumerate_subtree_slow(root, depth, max_exp)
        mod = 3 ** ell
        hist_slow = np.zeros(mod, dtype=np.float64)
        for leaf, w in slow:
            hist_slow[leaf % mod] += w
        hist_fast = enumerate_subtree_fast(root, depth, ell, max_exp)
        err = float(np.max(np.abs(hist_slow - hist_fast)))
        if err > 1e-9:
            raise RuntimeError(f"fast/slow mismatch root={root}: {err:.3e}")


_check_fast_matches_slow()


def v3(n):
    n = abs(int(n))
    if n == 0:
        return 10 ** 9
    k = 0
    while n % 3 == 0:
        n //= 3
        k += 1
    return k


def conductor_exponent(xi, ell):
    """r such that cond(xi) = 3^r, xi != 0 mod 3^ell: r = ell - v3(xi)."""
    return ell - v3(xi)


def per_conductor_pairing(S1, S2, ell):
    """sum_{xi: cond=3^r} S1(xi) conj(S2(xi)) for r=1..ell, xi != 0."""
    xi = np.arange(1, len(S1))
    r_of_xi = np.array([conductor_exponent(int(x), ell) for x in xi])
    prod = S1[1:] * np.conj(S2[1:])
    out = {}
    for r in range(1, ell + 1):
        mask = r_of_xi == r
        out[r] = complex(np.sum(prod[mask])) if np.any(mask) else 0j
    return out


def _conductor_fractions(S1, S2, ell, predicted_r):
    by_r = per_conductor_pairing(S1, S2, ell)
    total = sum(by_r.values())
    mags = {rr: abs(val) for rr, val in by_r.items()}
    total_mag = sum(mags.values())
    at_pred = mags.get(predicted_r, 0.0)
    above_pred = sum(v_ for rr, v_ in mags.items() if rr > predicted_r)
    frac_at = at_pred / total_mag if total_mag > 0 else float("nan")
    frac_above = above_pred / total_mag if total_mag > 0 else float("nan")
    dominant_r = max(mags, key=mags.get) if mags else None
    return total, frac_at, frac_above, dominant_r


def run_one(v, rank_pair, depth, ell, max_exp, control=False, seed=0):
    """rank_pair=(i,j): use the i-th and j-th smallest admissible first
    steps (1-indexed) as the two siblings, so gaps other than the
    minimal Delta=2 (k=1) can be probed too.

    control=True (added 2026-08-10, after the E-140/H-163 critique):
    replaces sibling 2's histogram with a random-unit dilation of
    itself (same control that showed E-140's base measurement carries
    no sibling-specific information) before computing the same
    conductor-fraction statistic, so the two can be compared directly.
    """
    i, j = rank_pair
    steps = admissible_first_steps(v, max(i, j))
    a1, a2 = steps[i - 1], steps[j - 1]
    k = (a2 - a1) // 2
    predicted_r = 1 + v3(k)
    w1 = predecessor(v, a1)
    w2 = predecessor(v, a2)
    hist1 = enumerate_subtree_fast(w1, depth - 1, ell, max_exp)
    hist2 = enumerate_subtree_fast(w2, depth - 1, ell, max_exp)
    S1 = character_sum_from_hist(hist1)
    S2 = character_sum_from_hist(hist2)
    total, frac_at, frac_above, dominant_r = _conductor_fractions(
        S1, S2, ell, predicted_r)
    out = dict(v=v, a1=a1, a2=a2, k=k, predicted_r=predicted_r,
               depth=depth, ell=ell, total=total, frac_at=frac_at,
               frac_above=frac_above, dominant_r=dominant_r)
    if control:
        mod = 3 ** ell
        rng = np.random.default_rng(seed)
        u = int(rng.integers(1, mod))
        while u % 3 == 0:
            u = int(rng.integers(1, mod))
        hist2_dilated = np.zeros(mod, dtype=np.float64)
        idx = (np.arange(mod) * u) % mod
        np.add.at(hist2_dilated, idx, hist2)
        S2c = character_sum_from_hist(hist2_dilated)
        _, frac_at_c, frac_above_c, _ = _conductor_fractions(
            S1, S2c, ell, predicted_r)
        out.update(frac_at_control=frac_at_c, frac_above_control=frac_above_c)
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--roots", type=int, nargs="+",
                        default=[1, 5, 7, 11, 17, 25])
    parser.add_argument("--depths", type=int, nargs="+", default=[6, 8, 10])
    parser.add_argument("--rank-pairs", type=str, nargs="+",
                        default=["1,2", "1,3", "2,3"],
                        help="which admissible-first-step ranks to pair, "
                             "e.g. 1,2 for the two closest siblings "
                             "(k=1, predicted r=1)")
    parser.add_argument("--max-exp", type=int, default=14)
    parser.add_argument("--control", action="store_true",
                         help="also compute the dilation control per row")
    args = parser.parse_args()

    rank_pairs = [tuple(int(x) for x in rp.split(",")) for rp in args.rank_pairs]

    header = ("v    a1  a2  k  pred_r  depth  ell  dominant_r  "
              "|total|      frac_at_pred_r   frac_above_pred_r")
    if args.control:
        header += "   frac_at_control   frac_above_control"
    print(header)
    for v in args.roots:
        for rp in rank_pairs:
            for depth in args.depths:
                ell = depth
                r = run_one(v, rp, depth, ell, args.max_exp,
                            control=args.control, seed=depth * 1000 + v)
                line = (f"{r['v']:<4d} {r['a1']:3d} {r['a2']:3d} {r['k']:2d} "
                        f"{r['predicted_r']:6d} {r['depth']:5d} {r['ell']:4d} "
                        f"{str(r['dominant_r']):>10s} {abs(r['total']):11.5e} "
                        f"{r['frac_at']:17.4f} {r['frac_above']:18.4f}")
                if args.control:
                    line += (f"   {r['frac_at_control']:15.4f}   "
                             f"{r['frac_above_control']:18.4f}")
                print(line)


if __name__ == "__main__":
    main()
