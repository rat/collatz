"""E-136 part 1: the l^r family of annealed Fourier-budget criteria.

Setting (same annealed model as E-101).  Z = sum_{g>=1} w_g e(U_g) with
U_g i.i.d. uniform on [0,1) and geometric weights w_g = p(1-p)^{g-1}.
Z is the annealed per-scale factor of a Fourier coefficient of the
Wirsching law mu_{ell,j}: a frequency of conductor 3^r picks up exactly
r such factors, so |muhat(xi)| ~ |Z|^r in the annealed benchmark.

A hole in the support forces sum_{xi != 0} |muhat(xi)| >= 1.  Holder
with exponent r >= 1 turns that into

    ||muhat||_{l^r(xi != 0)} >= (3^ell - 1)^{1/r - 1}.

Evaluating the left side in the annealed model gives 3^{ell/r} ||Z||_r^ell
(the top conductor shell dominates whenever 3||Z||_r^r > 1), so the
criterion closes if and only if

    ||Z||_r < 1/3.

||Z||_r is nondecreasing in r, and its r -> 0 limit is exp(E log|Z|),
which is the Jensen exponent of E-101.  So r = 1 is the best member of
the family that Holder actually allows, and the Jensen benchmark is a
strict lower bound on every member.

This script measures ||Z||_r, the induced threshold slope gamma_r
(the gamma = 1/p at which ||Z||_r = 1/3), and the exponent deficit
D_r = log 3 / log(1/||Z||_r) at the Wirsching critical slope.

Exact values used as self-checks, no Monte Carlo needed for them:
  ||Z||_2^2 = p/(2-p)                        (phases independent)
  lim_{r->0} ||Z||_r = exp(E log|Z|) = p     for p >= 1/2 (E-101/Jensen)
"""

import argparse
import math

import numpy as np

LOG3 = math.log(3.0)
GAMMA_C = 1.0 + math.log(3.0) / math.log(4.0)  # 1.79248..., c = 0
P_C = 1.0 / GAMMA_C  # 0.55789...


def truncation(p, eps=1e-15):
    """Number of geometric terms whose omitted tail is below eps."""
    return max(4, int(math.ceil(math.log(eps) / math.log1p(-p))))


def sample_abs_Z(p, n, rng, block=200_000):
    """Monte Carlo sample of |Z| for the geometric-weight annealed factor."""
    g = truncation(p)
    w = p * (1.0 - p) ** np.arange(g)
    out = np.empty(n)
    done = 0
    while done < n:
        m = min(block, n - done)
        u = rng.random((m, g))
        z = (w * np.exp(2j * math.pi * u)).sum(axis=1)
        out[done:done + m] = np.abs(z)
        done += m
    return out


def norms(absz, orders):
    """||Z||_r for each r, plus the r -> 0 limit exp(E log|Z|)."""
    res = {}
    safe = np.maximum(absz, 1e-300)
    res[0.0] = math.exp(float(np.mean(np.log(safe))))
    for r in orders:
        res[r] = float(np.mean(absz ** r)) ** (1.0 / r)
    return res


def threshold_gamma(r, rng, n, lo=0.02, hi=0.999):
    """Solve ||Z||_r(p) = 1/3 for p, return gamma = 1/p.

    ||Z||_r is increasing in p, so bisection is well posed.
    """
    if r == 2.0:  # exact: p/(2-p) = 1/9
        return 5.0
    for _ in range(40):
        mid = 0.5 * (lo + hi)
        if r == 0.0:
            val = math.exp(float(np.mean(np.log(
                np.maximum(sample_abs_Z(mid, n, rng), 1e-300)))))
        else:
            val = float(np.mean(sample_abs_Z(mid, n, rng) ** r)) ** (1.0 / r)
        if val < 1.0 / 3.0:
            lo = mid
        else:
            hi = mid
        if hi - lo < 1e-4:
            break
    return 2.0 / (lo + hi)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--samples", type=int, default=4_000_000)
    ap.add_argument("--threshold-samples", type=int, default=400_000)
    ap.add_argument("--seed", type=int, default=20260809)
    args = ap.parse_args()

    rng = np.random.default_rng(args.seed)
    orders = [0.5, 1.0, 1.5, 2.0, 3.0, 4.0]

    print(f"gamma_c = {GAMMA_C:.6f}   p_c = 1/gamma_c = {P_C:.6f}")
    print(f"Monte Carlo samples: {args.samples}\n")

    absz = sample_abs_Z(P_C, args.samples, rng)
    nrm = norms(absz, orders)

    exact2 = math.sqrt(P_C / (2.0 - P_C))
    print("self-checks at p = p_c")
    print(f"  ||Z||_2 exact  sqrt(p/(2-p)) = {exact2:.6f}")
    print(f"  ||Z||_2 MC                   = {nrm[2.0]:.6f}"
          f"   (rel err {abs(nrm[2.0] - exact2) / exact2:.2e})")
    print(f"  r->0 limit exact (Jensen)    = {P_C:.6f}")
    print(f"  r->0 limit MC                = {nrm[0.0]:.6f}"
          f"   (rel err {abs(nrm[0.0] - P_C) / P_C:.2e})")
    print(f"  bracket p <= E|Z| <= ||Z||_2 : "
          f"{P_C:.6f} <= {nrm[1.0]:.6f} <= {exact2:.6f}"
          f"  -> {'OK' if P_C <= nrm[1.0] <= exact2 else 'FAIL'}")

    # ||Z||_r at r = 0 and r = 2 is known in closed form (p and
    # sqrt(p/(2-p))); the gamma threshold is closed form only at r = 2.
    print("\n  r      ||Z||_r    deficit D_r    gamma threshold")
    for r in [0.0] + orders:
        v = nrm[r]
        d = LOG3 / math.log(1.0 / v)
        gt = threshold_gamma(r, rng, args.threshold_samples)
        tag = "  norm exact" if r == 0.0 else ""
        tag = "  norm and threshold exact" if r == 2.0 else tag
        print(f"  {r:<5}  {v:.6f}   {d:.4f}         {gt:.4f}{tag}")

    print("\nmonotonicity of ||Z||_r in r: "
          + ("OK" if all(nrm[a] <= nrm[b] + 1e-6
                         for a, b in zip([0.0] + orders, orders)) else "FAIL"))
    print(f"criterion needs ||Z||_r < 1/3 = {1/3:.6f}; "
          f"smallest value in the family is {nrm[0.0]:.6f}")

    # Lambda(p) below p = 1/2: the Jensen identity Lambda = log(1/p) only
    # holds for p >= 1/2.  Below that, Lambda < log(1/p), so the true
    # r -> 0 inversion point sits above gamma = 3.
    print("\nLambda(p) = E log(1/|Z|) versus the identity log(1/p)")
    print("  p        Lambda(MC)   log(1/p)   gamma=1/p")
    for p in [0.6, 0.5, 0.45, 0.40, 1.0 / 3.0, 0.30, 0.28]:
        a = sample_abs_Z(p, args.threshold_samples, rng)
        lam = float(-np.mean(np.log(np.maximum(a, 1e-300))))
        print(f"  {p:.4f}   {lam:.5f}      {math.log(1/p):.5f}    {1/p:.4f}")
    print(f"  target for inversion: Lambda > log 3 = {LOG3:.5f}")


if __name__ == "__main__":
    main()
