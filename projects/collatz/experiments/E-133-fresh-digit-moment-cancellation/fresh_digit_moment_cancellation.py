#!/usr/bin/env python3
"""Does a MOMENT/FOURIER functional of the fresh-digit joint law cancel,
where total variation and mutual information do not?

E-120/H-150 (paper: thm:fresh-digit-coupling) prove that for a fixed
sibling pair the fresh-digit blocks are maximally coupled:
TV = 1-3^-s, I = s*log(3). E-129 then showed that averaging the joint
law over the natural branching measure on the sibling gap
(P(Delta=2k)=3*4^-k, from E-108) does not move TV or mutual
information toward the product law either.

Neither statistic is what the second-moment programme of the paper
actually consumes. Section 9 of main.tex ("The correct, non-circular
reformulation") writes the relevant quantity as

    Cov  proportional to  sum_{xi != 0} S_1(xi) * conj(S_2(xi)),

with the SAME frequency xi in both factors. That is a diagonal slice of
the bivariate spectrum of the pair, equivalently a character functional
of the DIFFERENCE of the two leaves:

    D(xi) := E[ e_{3^s}( xi * (X - Y) ) ].

Under the product law D(xi) = 0 for every xi != 0, because both
marginals are uniform. This script measures D(xi) for the true joint
law, for a single fixed gap and after aggregating over the branching
measure on Delta, and compares against TV computed on the same objects.

Sections:

  A  fixed pair: full bivariate spectrum, its support line, and the
     diagonal slice. Predicate and direct summation cross-checked.
  B  aggregation over the branching measure on Delta.
  C  non-uniform free parameter: the exact identity
     D(xi) = phase * muhat(xi*(1-m)) and the resulting energy relation
     to thm:multiscale-parseval.
  D  a moment functional that does NOT cancel (per-digit covariance),
     so the choice of functional is doing real work.
  E  verification on actual integers that prop:fixed-pair's affine form
     w_i(v_0 + 3^D t) = w_i(v_0) + 2^{A_i} t is real, not idealized.

Run:

    python3 fresh_digit_moment_cancellation.py
"""

import argparse

import math

import numpy as np


# ----------------------------------------------------------------------
# the fixed-pair model
# ----------------------------------------------------------------------


def sibling_fresh_map(delta, coarse, fresh):
    """Return (m, g) such that the fresh block Y of the second leaf is
    Y = (m*X + g) mod 3^fresh, where X is the fresh block of the first.

    Built from exactly the arithmetic of E-120: the second leaf is
    y = 2^delta * x + (2^delta-1)/3, both leaves are then reduced modulo
    3^(coarse+fresh) and their coarse classes modulo 3^coarse removed.
    Requires delta even, which is what the q=3 tree produces (E-108).
    """
    if delta % 2 != 0:
        raise ValueError("the arithmetic construction needs even delta")
    modulus = 3 ** (coarse + fresh)
    coarse_modulus = 3**coarse
    block = 3**fresh
    multiplier = pow(2, delta, modulus)
    shift = (2**delta - 1) // 3
    x0 = 1
    y0 = (multiplier * x0 + shift) % coarse_modulus
    g = (((multiplier * x0 + shift) % modulus - y0) // coarse_modulus) % block
    return multiplier % block, g


def joint_matrix(m, g, fresh):
    """Joint law of (X, Y) with X uniform and Y = m*X+g mod 3^fresh."""
    block = 3**fresh
    joint = np.zeros((block, block))
    for x in range(block):
        joint[x, (m * x + g) % block] += 1.0 / block
    return joint


def check_matches_e120(delta, coarse, fresh):
    """The (m, g) reduction must reproduce E-120's explicit loop."""
    modulus = 3 ** (coarse + fresh)
    coarse_modulus = 3**coarse
    block = 3**fresh
    multiplier = pow(2, delta, modulus)
    shift = (2**delta - 1) // 3
    x0 = 1
    y0 = (multiplier * x0 + shift) % coarse_modulus
    m, g = sibling_fresh_map(delta, coarse, fresh)
    for x_block in range(block):
        x = x0 + coarse_modulus * x_block
        y = (multiplier * x + shift) % modulus
        if y % coarse_modulus != y0:
            raise RuntimeError("coarse affine class changed")
        y_block = ((y - y0) // coarse_modulus) % block
        if y_block != (m * x_block + g) % block:
            raise RuntimeError("reduction disagrees with E-120")
    return True


# ----------------------------------------------------------------------
# the functionals
# ----------------------------------------------------------------------


def diagonal_direct(m, g, fresh, law=None):
    """D(xi) = E[e_{3^s}(xi*(X-Y))] by direct summation over X."""
    block = 3**fresh
    if law is None:
        law = np.full(block, 1.0 / block)
    x = np.arange(block)
    diff = (x - (m * x + g)) % block
    out = np.zeros(block, dtype=complex)
    for xi in range(block):
        out[xi] = np.sum(law * np.exp(2j * math.pi * xi * diff / block))
    return out


def diagonal_predicted(m, g, fresh):
    """Closed form for uniform X: D(xi) is a root of unity when
    3^s divides xi*(1-m), and exactly zero otherwise."""
    block = 3**fresh
    xi = np.arange(block)
    resonant = (xi * ((1 - m) % block)) % block == 0
    phase = np.exp(-2j * math.pi * xi * g / block)
    return np.where(resonant, phase, 0.0)


def bivariate_spectrum(joint):
    """Phi(xi, eta) = E[e_{3^s}(xi*X + eta*Y)]. The joint is real, so the
    positive-sign transform is the conjugate of numpy's convention."""
    return np.conj(np.fft.fft2(joint))


def tv_and_mi(joint):
    mx = joint.sum(axis=1)
    my = joint.sum(axis=0)
    product = np.outer(mx, my)
    tv = 0.5 * float(np.abs(joint - product).sum())
    pos = joint > 0
    mi = float(np.sum(joint[pos] * np.log(joint[pos] / product[pos])))
    return tv, mi


def v3(n):
    n = abs(int(n))
    if n == 0:
        return math.inf
    k = 0
    while n % 3 == 0:
        n //= 3
        k += 1
    return k


def primitive_mask(fresh):
    xi = np.arange(3**fresh)
    return xi % 3 != 0


def delta_weight(k, k_max):
    """P(Delta=2k) = 3*4^-k (E-108), renormalized over k=1..k_max."""
    raw = [3.0 * 4.0 ** (-j) for j in range(1, k_max + 1)]
    return raw[k - 1] / sum(raw)


# ----------------------------------------------------------------------
# section A
# ----------------------------------------------------------------------


def section_a(coarse, max_fresh, deltas):
    print("=" * 72)
    print("A. Fixed sibling pair: bivariate spectrum and its diagonal slice")
    print("=" * 72)
    print()
    print("Phi(xi,eta) = E[e(xi X + eta Y)]. Under the product law it is")
    print("zero off (0,0). Here it is unimodular on the whole line")
    print("xi + eta*m = 0 mod 3^s, which is the 'line of resonant")
    print("frequencies' of prop:fixed-pair. The question is what that line")
    print("leaves on the diagonal eta = -xi that the second moment reads.")
    print()
    header = (
        "delta coarse fresh v3(1-2^d) supp(Phi) offzero_energy "
        "res_diag res_prim max|D|prim      TV"
    )
    print(header)
    for delta in deltas:
        for fresh in range(1, max_fresh + 1):
            check_matches_e120(delta, coarse, fresh)
            m, g = sibling_fresh_map(delta, coarse, fresh)
            block = 3**fresh
            joint = joint_matrix(m, g, fresh)
            phi = bivariate_spectrum(joint)
            support = int(np.sum(np.abs(phi) > 1e-9))
            energy = float(np.sum(np.abs(phi) ** 2)) - 1.0
            direct = diagonal_direct(m, g, fresh)
            pred = diagonal_predicted(m, g, fresh)
            if np.max(np.abs(direct - pred)) > 1e-10:
                raise RuntimeError("predicate and direct summation disagree")
            prim = primitive_mask(fresh)
            res_diag = int(np.sum(np.abs(direct) > 1e-9)) - 1
            res_prim = int(np.sum(np.abs(direct[prim]) > 1e-9))
            max_prim = float(np.max(np.abs(direct[prim]))) if prim.any() else 0.0
            tv, _ = tv_and_mi(joint)
            print(
                f"{delta:5d} {coarse:6d} {fresh:5d} "
                f"{v3(1 - 2**delta):9d} {support:9d} {energy:14.6f} "
                f"{res_diag:8d} {res_prim:8d} {max_prim:11.3e} {tv:9.6f}"
            )
    print()
    print("supp(Phi) equals 3^fresh at every row: the bivariate spectrum is")
    print("carried by one line of full modulus, so off-zero energy is")
    print("3^fresh - 1 and TV stays at 1-3^-fresh. res_diag counts the")
    print("nonzero diagonal coefficients with xi != 0, res_prim how many of")
    print("those sit at a primitive frequency.")


def section_a_odd_check(fresh_list):
    print()
    print("Bookkeeping check with an odd gap (not produced by the q=3 tree,")
    print("used only to exercise the valuation algebra): v3(1-2^delta)=0, so")
    print("D(xi) must vanish for every xi != 0, at every scale.")
    for fresh in fresh_list:
        block = 3**fresh
        for delta in (1, 3, 5):
            m = pow(2, delta, block)
            g = 7 % block
            direct = diagonal_direct(m, g, fresh)
            worst = float(np.max(np.abs(direct[1:])))
            print(
                f"  fresh={fresh} delta={delta} v3(1-2^delta)="
                f"{v3(1 - 2**delta)} max_{{xi!=0}}|D(xi)|={worst:.3e}"
            )


# ----------------------------------------------------------------------
# section B
# ----------------------------------------------------------------------


def aggregate_diagonal(coarse, fresh, k_max):
    block = 3**fresh
    total = np.zeros(block, dtype=complex)
    for k in range(1, k_max + 1):
        m, g = sibling_fresh_map(2 * k, coarse, fresh)
        total += delta_weight(k, k_max) * diagonal_predicted(m, g, fresh)
    return total


def aggregate_joint(coarse, fresh, k_max):
    block = 3**fresh
    joint = np.zeros((block, block))
    for k in range(1, k_max + 1):
        m, g = sibling_fresh_map(2 * k, coarse, fresh)
        joint += delta_weight(k, k_max) * joint_matrix(m, g, fresh)
    return joint


def section_b(coarse, max_fresh, k_max_list, tv_k_max):
    print()
    print("=" * 72)
    print("B. Aggregation over the branching measure P(Delta=2k)=3*4^-k")
    print("=" * 72)
    print()
    print("Same weight E-129 used for its TV aggregation, so the two")
    print("columns below describe the same aggregated ensemble.")
    print()
    print(
        "fresh k_max max|Dagg|prim  primitive_diag_energy  bound_4^(1-3^(s-1))"
        "   aggTV(k_max=%d)" % tv_k_max
    )
    for fresh in range(1, max_fresh + 1):
        prim = primitive_mask(fresh)
        agg_joint = aggregate_joint(coarse, fresh, tv_k_max)
        agg_tv, _ = tv_and_mi(agg_joint)
        bound = 4.0 ** (1 - 3 ** (fresh - 1))
        for k_max in k_max_list:
            dagg = aggregate_diagonal(coarse, fresh, k_max)
            worst = float(np.max(np.abs(dagg[prim])))
            energy = float(np.sum(np.abs(dagg[prim]) ** 2))
            print(
                f"{fresh:5d} {k_max:5d} {worst:14.6e} {energy:22.6e} "
                f"{bound:20.6e} {agg_tv:15.6f}"
            )
    print()
    print("The resonant gaps are exactly those with v3(k) >= fresh-1, whose")
    print("total branching weight is at most 4^(1-3^(fresh-1)). k_max must")
    print("exceed 3^(fresh-1) for any of them to be inside the truncation,")
    print("which is why the small-k_max rows report exact zeros.")


def section_b_conductor(coarse, max_fresh, k_list):
    print()
    print("Where the diagonal resonance actually sits, by gap:")
    print()
    print("k  v3(k) delta  conductor_of_surviving_diagonal_modes  weight")
    for k in k_list:
        j = 1 + v3(k)
        cond = 3**j
        print(
            f"{k:2d} {v3(k):5d} {2*k:5d} {cond:38d} "
            f"{3.0 * 4.0 ** (-k):.6e}"
        )
    print()
    print("The whole diagonal resonance of a pair with gap 2k lives at")
    print("conductor 3^(1+v3(k)). For the typical gap that is conductor 3,")
    print("one single coarse mode, which is the mode O1 already removes.")
    print("Verification that nothing survives above the conductor:")
    for fresh in range(1, max_fresh + 1):
        for k in k_list:
            m, g = sibling_fresh_map(2 * k, coarse, fresh)
            direct = diagonal_direct(m, g, fresh)
            j = 1 + v3(k)
            xi = np.arange(3**fresh)
            above = np.array([v3(x) < fresh - j if x else False for x in xi])
            worst = float(np.max(np.abs(direct[above]))) if above.any() else 0.0
            print(
                f"  fresh={fresh} k={k}: max|D(xi)| over xi with conductor "
                f"above 3^{j} = {worst:.3e}"
            )


# ----------------------------------------------------------------------
# section C
# ----------------------------------------------------------------------


def primitive_energy(law, level):
    """E_r of thm:multiscale-parseval for the projection of `law` to
    level `r`: sum over 3 not dividing xi of |muhat_r(xi)|^2."""
    block = 3**level
    projected = law.reshape(-1, block).sum(axis=0) if law.size != block else law
    hat = np.conj(np.fft.fft(projected))
    xi = np.arange(block)
    return float(np.sum(np.abs(hat[xi % 3 != 0]) ** 2))


def section_c(coarse, fresh_list, k_list, seed):
    print()
    print("=" * 72)
    print("C. Non-uniform free parameter: exact identity and the link to")
    print("   thm:multiscale-parseval")
    print("=" * 72)
    print()
    print("For any law mu of the free parameter X, not only the uniform")
    print("one, X-Y = (1-m)X - g gives")
    print("    D(xi) = e(-xi g / 3^s) * muhat(xi*(1-m)).")
    print("So the same-frequency pair correlation at scale s equals a")
    print("MARGINAL coefficient of the free parameter at the coarser scale")
    print("s - j, where j = v3(1-2^delta) = 1 + v3(k). Summing over")
    print("primitive xi this should give exactly 3^j * E_(s-j)(mu), with")
    print("E_r as defined in thm:multiscale-parseval.")
    print()
    rng = np.random.default_rng(seed)
    print("fresh k  j  identity_err   sum_prim|D|^2      3^j*E_(s-j)(mu)"
          "   rel_err")
    for fresh in fresh_list:
        block = 3**fresh
        law = rng.random(block) + 0.05
        law /= law.sum()
        for k in k_list:
            j = 1 + v3(k)
            if j >= fresh:
                continue
            m, g = sibling_fresh_map(2 * k, coarse, fresh)
            direct = diagonal_direct(m, g, fresh, law)
            xi = np.arange(block)
            hat = np.conj(np.fft.fft(law))
            closed = np.exp(-2j * math.pi * xi * g / block) * hat[
                (xi * ((1 - m) % block)) % block
            ]
            err = float(np.max(np.abs(direct - closed)))
            prim = primitive_mask(fresh)
            lhs = float(np.sum(np.abs(direct[prim]) ** 2))
            rhs = 3**j * primitive_energy(law, fresh - j)
            rel = abs(lhs - rhs) / max(rhs, 1e-300)
            print(
                f"{fresh:5d} {k:2d} {j:2d} {err:13.3e} {lhs:18.10f} "
                f"{rhs:18.10f} {rel:9.2e}"
            )
    print()
    print("The identity is exact, so the pair functional inherits whatever")
    print("decay the free parameter's own spectrum has, one scale coarser.")
    print("Summing over s, the transfer of the L2 criterion of")
    print("thm:multiscale-parseval is term by term, with no independence")
    print("assumption anywhere.")


def section_c_domain(coarse, fresh_list, k_list):
    print()
    print("The law the tree actually supplies. Section E below shows that a")
    print("real leaf pair forces the free parameter to avoid one class of t")
    print("mod 3 per leaf, so mu is uniform on a union of classes mod 3.")
    print("For such a law muhat vanishes off the multiples of 3^(s-1), so")
    print("E_r(mu)=0 for every r >= 2 and the identity of the previous table")
    print("predicts exact vanishing of the primitive diagonal at every")
    print("scale s >= j+2, with the whole residual sitting at s = j+1.")
    print()
    print("fresh k  j  |support mod 3|  sum_prim|D|^2   3^j*E_(s-j)(mu)")
    for fresh in fresh_list:
        block = 3**fresh
        for keep in ((0, 1), (1,)):
            law = np.zeros(block)
            for x in range(block):
                if x % 3 in keep:
                    law[x] = 1.0
            law /= law.sum()
            for k in k_list:
                j = 1 + v3(k)
                if j >= fresh:
                    continue
                m, g = sibling_fresh_map(2 * k, coarse, fresh)
                direct = diagonal_direct(m, g, fresh, law)
                prim = primitive_mask(fresh)
                lhs = float(np.sum(np.abs(direct[prim]) ** 2))
                rhs = 3**j * primitive_energy(law, fresh - j)
                print(
                    f"{fresh:5d} {k:2d} {j:2d} {len(keep):15d} "
                    f"{lhs:16.10f} {rhs:17.10f}"
                )


# ----------------------------------------------------------------------
# section D
# ----------------------------------------------------------------------


def section_d(coarse, max_fresh, k_max):
    print()
    print("=" * 72)
    print("D. A moment functional that does not cancel")
    print("=" * 72)
    print()
    print("Not every low-order statistic behaves like the character sum of")
    print("the difference. The covariance of the j-th base-3 digits of the")
    print("two leaves stays away from zero, aggregated or not, so the")
    print("cancellation in A to C is a property of this particular")
    print("functional and not of the joint law being nearly a product.")
    print()
    print("fresh digit  Cov(single delta=2)  Cov(aggregated over Delta)")
    for fresh in range(1, max_fresh + 1):
        block = 3**fresh
        m1, g1 = sibling_fresh_map(2, coarse, fresh)
        single = joint_matrix(m1, g1, fresh)
        agg = aggregate_joint(coarse, fresh, k_max)
        x = np.arange(block)
        for d in range(fresh):
            dx = (x // 3**d) % 3
            row = []
            for joint in (single, agg):
                mean_x = float(np.sum(joint.sum(axis=1) * dx))
                mean_y = float(np.sum(joint.sum(axis=0) * dx))
                cov = float(
                    np.sum(joint * np.outer(dx, dx)) - mean_x * mean_y
                )
                row.append(cov)
            print(f"{fresh:5d} {d:5d}  {row[0]:19.6f}  {row[1]:25.6f}")


# ----------------------------------------------------------------------
# section E
# ----------------------------------------------------------------------


def predecessor(v, a, allow_multiple_of_three=False):
    """The Syracuse predecessor w with (3w+1)/2^a = v, when it exists."""
    num = (1 << a) * v - 1
    if num % 3 != 0:
        return None
    w = num // 3
    if w <= 0 or w % 2 == 0:
        return None
    if w % 3 == 0 and not allow_multiple_of_three:
        return None
    return w


def lift_path(v, exps, strict_leaf=True):
    """Leaf of the path. With strict_leaf=False the coprime-to-3 condition
    is dropped at the last step only, which isolates the pure affine
    arithmetic from the tree's domain condition on leaves."""
    w = v
    last = len(exps) - 1
    for i, a in enumerate(exps):
        w = predecessor(w, a, allow_multiple_of_three=(i == last
                                                       and not strict_leaf))
        if w is None:
            return None
    return w


def enumerate_paths(v, depth, max_exp, limit):
    """All admissible exponent sequences of the given depth, truncated."""
    live = [(v, [])]
    for _ in range(depth):
        nxt = []
        for w, exps in live:
            for a in range(1, max_exp + 1):
                child = predecessor(w, a)
                if child is not None:
                    nxt.append((child, exps + [a]))
        live = nxt[:limit]
        if not live:
            return []
    return live


def empirical_diagonal(diff, block):
    """max over primitive xi of |mean_t e(xi*diff_t / block)|."""
    worst = 0.0
    for xi in range(1, block):
        if xi % 3 == 0:
            continue
        worst = max(
            worst, abs(np.mean(np.exp(2j * math.pi * xi * diff / block)))
        )
    return worst


def section_e():
    print()
    print("=" * 72)
    print("E. The affine form of prop:fixed-pair, checked on real integers")
    print("=" * 72)
    print()
    print("Claim under test: with v = v0 + 3^D t, an admissible depth-D")
    print("exponent sequence stays admissible and its leaf satisfies")
    print("w(v) = w(v0) + 2^A t exactly, with A the sum of the exponents.")
    print()
    print("One correction the run forced, and it is not cosmetic. A leaf of")
    print("the Syracuse tree must be coprime to 3, and w(v0)+2^A t runs")
    print("through all three classes mod 3 as t varies, so one class of t")
    print("is inadmissible for each leaf. Intermediate vertices are not")
    print("affected: they shift by 2^{A_i} * 3^{D-i} t, which is 0 mod 3.")
    print("So the free parameter of a real leaf pair is uniform on a union")
    print("of classes mod 3, and not on all of Z/3^s. Both cases are")
    print("measured below.")
    print()
    depth = 5
    checked = 0
    for v0 in (1, 5, 7, 11, 17, 25):
        found = enumerate_paths(v0, depth, 8, 400)
        pair = None
        for i in range(len(found)):
            for j2 in range(i + 1, len(found)):
                if sum(found[i][1]) != sum(found[j2][1]):
                    pair = (found[i][1], found[j2][1])
                    break
            if pair:
                break
        if pair is None:
            continue
        p1, p2 = pair
        a1, a2 = sum(p1), sum(p2)
        w1_0 = lift_path(v0, p1, strict_leaf=False)
        w2_0 = lift_path(v0, p2, strict_leaf=False)
        ok = True
        for t in range(1, 200):
            v = v0 + 3**depth * t
            w1 = lift_path(v, p1, strict_leaf=False)
            w2 = lift_path(v, p2, strict_leaf=False)
            if w1 is None or w2 is None:
                ok = False
                break
            if w1 != w1_0 + (1 << a1) * t or w2 != w2_0 + (1 << a2) * t:
                ok = False
                break
        delta = a2 - a1
        print(
            f"  v0={v0:3d} A1={a1:3d} A2={a2:3d} delta={delta:4d} "
            f"even={delta % 2 == 0} affine_form_holds={ok} "
            f"j=v3(2^|delta|-1)={v3(2 ** abs(delta) - 1)}"
        )
        checked += 1
        if not ok:
            raise RuntimeError("affine form failed on real integers")
        for fresh in (2, 3, 4):
            block = 3**fresh
            xs, ys, adm = [], [], []
            for t in range(block):
                v = v0 + 3**depth * t
                w1 = lift_path(v, p1, strict_leaf=False)
                w2 = lift_path(v, p2, strict_leaf=False)
                xs.append(w1 % block)
                ys.append(w2 % block)
                adm.append(w1 % 3 != 0 and w2 % 3 != 0)
            xs = np.array(xs)
            ys = np.array(ys)
            adm = np.array(adm)
            diff = (xs - ys) % block
            all_t = empirical_diagonal(diff, block)
            leaves_t = empirical_diagonal(diff[adm], block)
            print(
                f"        fresh={fresh}: max primitive |D| over all t = "
                f"{all_t:.3e}; over admissible t only = {leaves_t:.3e} "
                f"({int(adm.sum())}/{block} values of t)"
            )
    if checked == 0:
        raise RuntimeError("no admissible pair of paths found")


# ----------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--coarse", type=int, default=2)
    parser.add_argument("--max-fresh", type=int, default=5)
    parser.add_argument("--deltas", type=int, nargs="+", default=[2, 4, 6, 18])
    parser.add_argument("--k-max-list", type=int, nargs="+",
                        default=[16, 90, 300])
    parser.add_argument("--tv-k-max", type=int, default=16)
    parser.add_argument("--seed", type=int, default=20260809)
    args = parser.parse_args()

    section_a(args.coarse, args.max_fresh, args.deltas)
    section_a_odd_check([2, 4])
    section_b(args.coarse, args.max_fresh, args.k_max_list, args.tv_k_max)
    section_b_conductor(args.coarse, min(args.max_fresh, 4), [1, 2, 3, 9])
    section_c(args.coarse, list(range(2, args.max_fresh + 1)), [1, 2, 3, 9],
              args.seed)
    section_c_domain(args.coarse, list(range(2, args.max_fresh + 1)),
                     [1, 3, 9])
    section_d(args.coarse, min(args.max_fresh, 3), args.tv_k_max)
    section_e()


if __name__ == "__main__":
    main()
