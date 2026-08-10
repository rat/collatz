#!/usr/bin/env python3
"""E-140 (H-163): the cheap first test the hypothesis itself prescribes
-- AND, added after an independent critique caught a real error, the
control that shows the original test does not measure what it claims to.

H-163 asks whether the bilinear pairing

    Cov(xi) ~ sum_{xi != 0} S_1(xi) * conj(S_2(xi))

between two sibling subtrees of the reverse Syracuse tree (q=3), rooted
at a common fixed v, shows phase cancellation. S_i(xi) is the character
sum over admissible depth-D continuations below sibling i, weighted by
the real branch weight prod_j 2^{-a_j} (Geom(2)-style weight, not
renormalized), evaluated at the leaf's residue mod 3^ell.

"Siblings" are the two smallest admissible first-step exponents at v.
Their gap alpha_2-alpha_1 is USUALLY 2 (only one parity of `a` clears
the mod-3 divisibility test at a fixed v), but not always: the further
exclusion w%3==0 can skip a candidate, so some roots give a larger gap
(v=17 gives alpha_1=1, alpha_2=5, gap 4). Do not assume gap=2 for every
root without checking `first_admissible_pair`'s actual return value.

FINDING (2026-08-10, after an independent critic's controls, reproduced
here independently, see `control_dilation_median` /
`control_unrelated_root` and H-163's closure): the ratio_CS /
ratio_RP quantities below do NOT measure phase cancellation between
siblings. By Parseval, `measured = m*<h1,h2> - m1*m2` (m=3^ell, h_i the
weighted residue histogram, m_i its total mass). CORRECTION (second
critique round: the first version of this note wrongly called h1, h2
"sparse"): the supports are FULL (every residue coprime to 3, verified
with `(h>0).sum()`: 4374/6561 at ell=8, 354294/531441 at ell=12, same
support size for both siblings). What is small is the PARTICIPATION
RATIO (m_i^2/||h_i||_2^2, an effective-atom count, ~11-85 in the cases
measured), a different statistic from support size. The unrenormalized
branch weight concentrates most of the mass onto a handful of "heavy"
residues within the full support, and the two siblings' heavy residues
rarely coincide: measured `m*<h1,h2>/(m1*m2)` runs 0.03-0.5 in the
cases checked (not ~0; v=17,ell=4 is an exception at 5.8), enough that
`measured` is usually dominated by `-m1*m2` without needing a
sparse-support argument. Two controls below (random frequency dilation
of h2, median of 5 draws; an unrelated, far-away root's subtree in
place of sibling 2) cover the same range as the real siblings at every
depth tested, in two cells by a wide margin in the direction that
strengthens this conclusion -- the numbers carry no sibling-specific
information. Kept as part of the permanent record (not deleted)
because the failure mode is itself worth having on file: a decision
rule whose "no signal" branch is structurally unreachable (see H-163)
does not decide anything just because it lands on the other branch.

Decision rule that was pre-registered in H-163 before first running
this (now known to have been unfalsifiable, kept here verbatim for the
record):

  1. measured near the trivial Cauchy-Schwarz budget sqrt(E_1*E_2):
     no cancellation, the route dies with a number.
  2. measured near or below the random-phase estimate
     sqrt(sum_xi |S_1|^2 |S_2|^2): phase cancellation is present, and
     the next question is rate/uniformity in ell.

The enumeration is exact (no path is dropped for depths tested here;
`max_exp` only truncates the exponent range: results are stable to
within about 1% between max_exp=14 and max_exp=20, not bit-identical,
checked before relying on max_exp=14 as the default) but is vectorised
over full levels with numpy instead of walking individual Python path
objects, tracking residues at higher modulus 3^(ell+remaining) so each
division by 3 in the reverse step stays exact (no wraparound), only
losing precision at the rate the recursion actually loses it.
Cross-checked below against a small brute-force enumeration using the
individual-path method (kept as `enumerate_subtree_slow`, the original,
obviously-correct version) before trusting the fast path on anything
reported.
"""

import argparse
import math

import numpy as np


def predecessor(v, a, allow_multiple_of_three=False):
    """The Syracuse predecessor w with (3w+1)/2^a = v, when it exists.
    Verbatim from E-133 section E (already validated there)."""
    num = (1 << a) * v - 1
    if num % 3 != 0:
        return None
    w = num // 3
    if w <= 0 or w % 2 == 0:
        return None
    if w % 3 == 0 and not allow_multiple_of_three:
        return None
    return w


def first_admissible_pair(v, max_a=200):
    """The two smallest admissible first-step exponents at v."""
    found = []
    for a in range(1, max_a + 1):
        if predecessor(v, a) is not None:
            found.append(a)
            if len(found) == 2:
                return found
    raise RuntimeError(f"fewer than 2 admissible first steps at v={v} "
                        f"within max_a={max_a}")


def enumerate_subtree_slow(root, depth, max_exp):
    """Reference implementation: individual Python path objects, no
    numpy vectorisation. Used only to cross-check the fast version."""
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
    """Weighted residue histogram of leaves mod 3^ell after `depth`
    admissible reverse steps below `root`, computed level by level with
    numpy, tracking each residue at modulus 3^(ell+remaining) so the
    division by 3 inside `predecessor` never loses information it
    should not lose.

    Returns hist: float64 array of length 3^ell, hist[r] = total
    branch weight of paths landing on residue r.
    """
    m_final = 3 ** ell
    if depth == 0:
        hist = np.zeros(m_final, dtype=np.float64)
        hist[root % m_final] += 1.0
        return hist

    m_start = 3 ** (ell + depth)
    res = np.array([root % m_start], dtype=np.int64)
    wt = np.array([1.0], dtype=np.float64)
    m_cur = m_start
    for step in range(depth):
        m_next = m_cur // 3
        new_res_parts = []
        new_wt_parts = []
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
        # Deduplicate every level, not just at the end: without this the
        # intermediate arrays grow with the raw branching factor
        # (unbounded in depth) instead of being capped near 3^(ell+
        # remaining), which is what actually happened the first time
        # this was tried at depth>=16 (>20GB resident before it was
        # killed). Two different admissible paths can land on the same
        # residue at the same intermediate modulus; merging their
        # weight here is exact, not an approximation.
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
    """S(xi) for xi=0..len(hist)-1, from a weighted residue histogram.
    S(xi) = sum_r hist[r]*e(xi*r/mod) is the +2j*pi-convention DFT,
    the conjugate of numpy's fft convention."""
    return np.conj(np.fft.fft(hist))


def _check_fast_matches_slow():
    """Correctness gate (must pass before anything below is trusted):
    fast (vectorised, higher-modulus) enumeration must reproduce the
    slow (individual Python path) enumeration exactly, on cases small
    enough to run both."""
    for root, depth, ell, max_exp in [(1, 3, 3, 10), (5, 4, 4, 8),
                                       (7, 3, 5, 12)]:
        slow = enumerate_subtree_slow(root, depth, max_exp)
        mod = 3 ** ell
        hist_slow = np.zeros(mod, dtype=np.float64)
        for leaf, w in slow:
            hist_slow[leaf % mod] += w
        hist_fast = enumerate_subtree_fast(root, depth, ell, max_exp)
        err = float(np.max(np.abs(hist_slow - hist_fast)))
        if err > 1e-9:
            raise RuntimeError(
                f"fast/slow mismatch at root={root} depth={depth} "
                f"ell={ell}: max err {err:.3e}")
        s_slow = character_sum_from_hist(hist_slow)
        s_fast = character_sum_from_hist(hist_fast)
        if float(np.max(np.abs(s_slow - s_fast))) > 1e-7:
            raise RuntimeError("character sums disagree after hist match")


_check_fast_matches_slow()


def _ratios_from_hists(hist1, hist2):
    """The ratio_CS / ratio_RP pair, from two arbitrary weighted
    residue histograms of the same length. Not sibling-specific; used
    both for the real measurement and for the two controls below."""
    S1 = character_sum_from_hist(hist1)
    S2 = character_sum_from_hist(hist2)
    S1n, S2n = S1[1:], S2[1:]
    measured = complex(np.sum(S1n * np.conj(S2n)))
    E1 = float(np.sum(np.abs(S1n) ** 2))
    E2 = float(np.sum(np.abs(S2n) ** 2))
    cs_budget = math.sqrt(E1 * E2)
    random_phase = math.sqrt(float(np.sum(np.abs(S1n) ** 2 * np.abs(S2n) ** 2)))
    ratio_cs = abs(measured) / cs_budget if cs_budget > 0 else float("nan")
    ratio_rp = abs(measured) / random_phase if random_phase > 0 else float("nan")
    return abs(measured), cs_budget, random_phase, ratio_cs, ratio_rp


def control_dilation(hist2, ell, seed):
    """Control B: dilate hist2's support by a random unit u mod 3^ell
    (a bijection of the residues, preserves every norm of hist2
    exactly, destroys any arithmetic relation to hist1)."""
    mod = 3 ** ell
    rng = np.random.default_rng(seed)
    u = int(rng.integers(1, mod))
    while u % 3 == 0:
        u = int(rng.integers(1, mod))
    dilated = np.zeros(mod, dtype=np.float64)
    idx = (np.arange(mod) * u) % mod
    np.add.at(dilated, idx, hist2)
    return dilated


def control_dilation_median(hist1, hist2, ell, base_seed, draws=5):
    """A single random dilation is noisy (checked: the same cell can
    read anywhere from 0.04 to 0.11 across draws). Report the median
    ratio_rp/ratio_cs over `draws` independent dilations, with the
    exact seeds recorded so this is reproducible, not a single
    unrecorded draw (an earlier version of this experiment reported
    one-off interactive numbers that a critic could not reproduce from
    the committed script)."""
    rcs_list, rrp_list = [], []
    for i in range(draws):
        dilated = control_dilation(hist2, ell, base_seed * 100 + i)
        _, _, _, rcs, rrp = _ratios_from_hists(hist1, dilated)
        rcs_list.append(rcs)
        rrp_list.append(rrp)
    return float(np.median(rcs_list)), float(np.median(rrp_list))


def control_unrelated_root(v, depth, ell, max_exp, offset=1000003):
    """Control C: the subtree below the smallest admissible first step
    of a root far away from v, with no sibling relationship to v's own
    subtrees at all."""
    v2 = offset + 6 * v
    a, _ = first_admissible_pair(v2)
    w = predecessor(v2, a)
    return enumerate_subtree_fast(w, depth - 1, ell, max_exp)


def run_one(v, depth, ell, max_exp, with_controls=False, seed=0):
    a1, a2 = first_admissible_pair(v)
    w1 = predecessor(v, a1)
    w2 = predecessor(v, a2)
    hist1 = enumerate_subtree_fast(w1, depth - 1, ell, max_exp)
    hist2 = enumerate_subtree_fast(w2, depth - 1, ell, max_exp)
    measured_abs, cs_budget, random_phase, ratio_cs, ratio_rp = \
        _ratios_from_hists(hist1, hist2)
    n_leaves = int(np.sum(hist1 > 0)) + int(np.sum(hist2 > 0))
    mass1 = float(hist1.sum())
    mass2 = float(hist2.sum())
    out = dict(
        v=v, a1=a1, a2=a2, depth=depth, ell=ell,
        n_leaves=n_leaves, mass1=mass1, mass2=mass2,
        measured_abs=measured_abs, cs_budget=cs_budget,
        random_phase=random_phase, ratio_cs=ratio_cs, ratio_rp=ratio_rp,
    )
    if with_controls:
        rcs_b, rrp_b = control_dilation_median(hist1, hist2, ell, seed,
                                                draws=5)
        hist3 = control_unrelated_root(v, depth, ell, max_exp)
        _, _, _, rcs_c, rrp_c = _ratios_from_hists(hist1, hist3)
        out.update(ratio_rp_control_dilation=rrp_b,
                    ratio_rp_control_unrelated=rrp_c,
                    ratio_cs_control_dilation=rcs_b,
                    ratio_cs_control_unrelated=rcs_c)
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--roots", type=int, nargs="+",
                        default=[1, 5, 7, 11, 17, 25, 35, 49])
    parser.add_argument("--depths", type=int, nargs="+",
                        default=[2, 3, 4, 5, 6, 7, 8, 9, 10])
    parser.add_argument("--max-exp", type=int, default=14)
    parser.add_argument("--controls", action="store_true",
                         help="also compute the dilation and "
                              "unrelated-root controls (H-163's "
                              "closure: these reproduce the real-"
                              "sibling ratios, showing the base "
                              "measurement carries no sibling-specific "
                              "information)")
    args = parser.parse_args()

    if not args.controls:
        print("v    a1  a2  depth  ell  n_leaves    mass1     mass2  "
              "|sum S1 S2*|   CS_budget  rand_phase  ratio_CS  ratio_RP")
        for v in args.roots:
            for depth in args.depths:
                ell = depth
                r = run_one(v, depth, ell, args.max_exp)
                print(f"{r['v']:<4d} {r['a1']:3d} {r['a2']:3d} "
                      f"{r['depth']:5d} {r['ell']:4d} {r['n_leaves']:8d} "
                      f"{r['mass1']:9.6f} {r['mass2']:9.6f} "
                      f"{r['measured_abs']:12.6e} {r['cs_budget']:12.6e} "
                      f"{r['random_phase']:11.6e} {r['ratio_cs']:9.4f} "
                      f"{r['ratio_rp']:9.4f}")
        return

    print("v    ell   ratio_RP(real)   ratio_RP(dilation-control)   "
          "ratio_RP(unrelated-root)")
    for v in args.roots:
        for depth in args.depths:
            ell = depth
            r = run_one(v, depth, ell, args.max_exp, with_controls=True,
                        seed=depth * 1000 + v)
            print(f"{r['v']:<4d} {r['ell']:4d}   {r['ratio_rp']:12.4f}   "
                  f"{r['ratio_rp_control_dilation']:24.4f}   "
                  f"{r['ratio_rp_control_unrelated']:22.4f}")


if __name__ == "__main__":
    main()
