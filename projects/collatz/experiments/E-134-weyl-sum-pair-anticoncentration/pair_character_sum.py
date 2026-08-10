#!/usr/bin/env python3
"""The 3-adic Weyl-sum program for H-161's pair inequality, carried to the
point where it stalls.

Setup. At level n the affine orbit is A(k) = 4k+1 mod 3^n, which in the
coordinate z = 1+3k is plain multiplication by 4 on the cyclic group
G = {z = 1 mod 3} inside (Z/3^(n+1))^*, |G| = 3^n. The orbit time is the
3-adic discrete logarithm base 4,

    tau(z) = log(z)/log(4)   (both 3-adic logs converge on G),

so A becomes tau -> tau+1 and the characters of G are exactly the Weyl
phases chi_m(z) = e(m tau(z)/3^n).

F2 says every consecutive-unit pair reduces to a pair of W values one
level down, at arguments related by an explicit affine map. In z
coordinates those maps are (derived here, verified below):

    Type (1,2):  b = 2a+1        <=>  sigma1(z) = 2z+2
    Type (2,1):  a''' = 32b+17   <=>  sigma2(z) = 32z+20

Both send G to G bijectively. The pair question is whether the level set
{V <= x} decorrelates from its sigma-preimage, and the sketched program
was to prove that from bounds on the mixed Weyl sums

    T(m,n) = sum_{z in G} chi_m(z) chi_n(sigma z).

This script does two things.

1. Verifies F2 numerically (independently, against laws built from
   scratch) and confirms the two z-coordinate maps.

2. Evaluates T(m,n) exhaustively for small n and tests the 3-adic
   stationary-phase prediction. Writing z = 1+3a and lambda = log/3, the
   phase is F(a) = m~ lambda(1+3a) + n~ lambda(sigma(1+3a)) with
   m~ = m/lambda(4). For sigma1, F'(a) = m~/(1+3a) + n~/(2+3a), so
   F'(a) = 0 mod 3 forces 2m~+n~ = 0 mod 3; for sigma2,
   F'(a) = m~/(1+3a) + 8 n~/(13+24a), forcing m~+2n~ = 0 mod 3. With no
   critical point the sum vanishes identically. Since lambda(4) is a
   3-adic unit the criteria read the same in m,n:

    T1(m,n) = 0 unless 2m+n = 0 (mod 3)
    T2(m,n) = 0 unless m+2n = 0 (mod 3)

   and the surviving sums should show square-root cancellation.

What this does NOT give is recorded in the README: T(m,n)/|G| is the
matrix of composition with a bijection of G written in the character
basis, hence unitary, so no bound on T alone can beat the trivial one.
"""

import argparse
import math

import numpy as np


def circ_geom_half(nu):
    M = len(nu)
    cur = 0.5 * np.roll(nu, -1)
    cur_len, res_len = 1, 0
    res = np.zeros(M)
    m = M
    while m:
        if m & 1:
            w = 2.0 ** (-res_len) if res_len < 1070 else 0.0
            res = res + w * np.roll(cur, -res_len)
            res_len += cur_len
        m >>= 1
        if m:
            w = 2.0 ** (-cur_len) if cur_len < 1070 else 0.0
            cur = cur + w * np.roll(cur, -cur_len)
            cur_len *= 2
    if M < 200:
        res = res / (1.0 - 2.0 ** (-M))
    return res


def laws(maxlevel):
    out = {}
    mu_prev = np.array([1.0])
    for level in range(1, maxlevel + 1):
        mod = 3 ** level
        period = 2 * 3 ** (level - 1)
        orbit = np.empty(period, dtype=np.int64)
        y = 1
        for i in range(period):
            orbit[i] = y
            y = (2 * y) % mod
        nu = np.zeros(period)
        um = (orbit % 3) == 1
        nu[um] = mu_prev[(orbit[um] - 1) // 3]
        mu = np.zeros(mod)
        mu[orbit] = circ_geom_half(nu)
        out[level] = mu
        mu_prev = mu
    return out


def W_along_orbit(N_prev, level):
    """W(k) = sum_{j>=0} 4^-j N_prev(A^j k) on Z/3^level, exact geometric
    closure on the single A-cycle."""
    M = 3 ** level
    orbit = np.empty(M, dtype=np.int64)
    k = 0
    for i in range(M):
        orbit[i] = k
        k = (4 * k + 1) % M
    vals = N_prev[orbit]
    res = np.zeros(M)
    cur = vals.copy()
    cur_len, res_len = 1, 0
    m = M
    while m:
        if m & 1:
            w = 4.0 ** (-res_len) if res_len < 530 else 0.0
            res = res + w * np.roll(cur, -res_len)
            res_len += cur_len
        m >>= 1
        if m:
            w = 4.0 ** (-cur_len) if cur_len < 530 else 0.0
            cur = cur + w * np.roll(cur, -cur_len)
            cur_len *= 2
    if M < 200:
        res = res / (1.0 - 4.0 ** (-M))
    out = np.zeros(M)
    out[orbit] = res
    return out


def check_f2(maxlevel=8):
    """Re-verify F2 from scratch, and the z-coordinate form of both maps."""
    mu = laws(maxlevel)
    N = {lev: mu[lev] * 3 ** lev for lev in mu}
    print("F2 re-verification (independent rebuild, Rule 8c)")
    for n in range(3, maxlevel + 1):
        Mn, Mp = 3 ** n, 3 ** (n - 1)
        Wp = W_along_orbit(N[n - 1], n - 1)      # W'' on Z/3^(n-1)
        k = np.arange(Mn)
        t1 = k % 3 == 1
        t2 = k % 3 == 2
        a = ((4 * k - 1) // 3) % Mp
        b = ((2 * k - 1) // 3) % Mp
        e1 = np.abs(N[n][t1] - 0.75 * Wp[a[t1]]).max()      # F1, phase 1
        e2 = np.abs(N[n][t2] - 1.5 * Wp[b[t2]]).max()       # F1, phase 2
        # Type (1,2): k = 1 mod 3 paired with A(k)
        kk = k[t1]
        Ak = (4 * kk + 1) % Mn
        aa = ((4 * kk - 1) // 3) % Mp
        bb = ((2 * Ak - 1) // 3) % Mp
        e3 = int(np.abs(bb - (2 * aa + 1) % Mp).max())      # b = 2a+1
        # Type (2,1): k = 2 mod 3 paired with A^2(k)
        kp = k[t2]
        A2k = (16 * kp + 5) % Mn
        b2 = ((2 * kp - 1) // 3) % Mp
        a3 = ((4 * A2k - 1) // 3) % Mp
        e4 = int(np.abs(a3 - (32 * b2 + 17) % Mp).max())    # a''' = 32b+17
        # z coordinates: z_b = 2 z_a + 2 and z_a''' = 32 z_b + 20 mod 3^n
        za, zb = (1 + 3 * aa) % Mn, (1 + 3 * bb) % Mn
        e5 = int(np.abs(zb - (2 * za + 2) % Mn).max())
        zb2, za3 = (1 + 3 * b2) % Mn, (1 + 3 * a3) % Mn
        e6 = int(np.abs(za3 - (32 * zb2 + 20) % Mn).max())
        print(
            f"  n={n:2d}  F1 phase1 {e1:.2e}  phase2 {e2:.2e}   "
            f"b=2a+1 {e3}   a'''=32b+17 {e4}   "
            f"z: 2z+2 {e5}   32z+20 {e6}"
        )


def val3(a, cap):
    """3-adic valuation, capped; val3(0) = cap."""
    r = np.zeros(a.shape, dtype=np.int64)
    b = np.where(a == 0, 3 ** cap, a)
    for _ in range(cap):
        hit = (b % 3) == 0
        r += hit
        b = np.where(hit, b // 3, b)
    return r


def weyl(n, alpha, beta, label):
    """Exhaustive T(m,n) for sigma(z) = alpha*z + beta on
    G = {z = 1 mod 3} subset Z/3^(n+1), |G| = 3^n."""
    q = 3 ** (n + 1)
    M = 3 ** n
    # tau via the cycle of 4: tau(4^j mod q) = j
    tau = {}
    z = 1
    for j in range(M):
        tau[z] = j
        z = (4 * z) % q
    assert len(tau) == M, "4 does not generate G"
    s = np.empty(M, dtype=np.int64)
    z = 1
    for j in range(M):
        s[j] = tau[(alpha * z + beta) % q]
        z = (4 * z) % q
    assert len(set(s.tolist())) == M, "sigma is not a bijection of G"
    Q = np.zeros((M, M))
    Q[np.arange(M), s] = 1.0
    T = np.fft.fft2(Q)          # T[m,n] = sum_j e(-(m j + n s(j))/M)
    mm, nn = np.meshgrid(np.arange(M), np.arange(M), indexing="ij")
    if label == "sigma1":
        crit = (2 * mm + nn) % 3 == 0
    else:
        crit = (mm + 2 * nn) % 3 == 0
    absT = np.abs(T)
    off = absT[~crit].max()
    # size law: |T(m,n)| <= 3^((n+1+v)/2) with v = v_3(gcd(m,n)).
    # A frequency divisible by 3^v collapses the sum to 3^v copies of a
    # sum mod 3^(n-v), giving 3^v * 3^((n-v+1)/2) = 3^((n+v+1)/2).
    v = np.minimum(val3(mm, n), val3(nn, n))
    nonzero = (mm != 0) | (nn != 0)
    bound = 3.0 ** ((n + 1 + v) / 2.0)
    slack = (absT[nonzero] / bound[nonzero]).max()
    nz = absT[crit & nonzero]
    print(
        f"  {label} n={n:2d} |G|={M:6d}: max|T| off-criterion {off:.3e}"
        f"   max|T|/3^((n+1+v)/2) {slack:.6f}"
        f"   max|T| primitive {absT[nonzero & (v == 0)].max():9.4f}"
        f" (3^((n+1)/2)={3.0**((n+1)/2):9.4f})"
        f"   #nonzero {int((absT > 1e-8).sum()):7d}"
        f" (criterion allows {int(crit.sum()):7d})"
    )
    return off, slack


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--f2-level", type=int, default=8)
    ap.add_argument("--weyl-levels", type=int, nargs="+", default=[2, 3, 4, 5, 6])
    args = ap.parse_args()

    check_f2(args.f2_level)
    print()
    print("Mixed Weyl sums T(m,n) = sum_z chi_m(z) chi_n(sigma z)")
    print("stationary phase predicts T = 0 off the criterion")
    worst, worst_slack = 0.0, 0.0
    for n in args.weyl_levels:
        for alpha, beta, label in ((2, 2, "sigma1"), (32, 20, "sigma2")):
            off, slack = weyl(n, alpha, beta, label)
            worst = max(worst, off)
            worst_slack = max(worst_slack, slack)
    print()
    print(f"largest violation of the vanishing criterion anywhere: {worst:.3e}")
    print(
        f"largest |T| / 3^((n+1+v3(gcd(m,n)))/2) anywhere: {worst_slack:.6f}"
        "  (<= 1 means the size law holds, = 1 means it is attained)"
    )
    print(
        "\nThe phase is therefore as non-degenerate as a phase can be:"
        "\nsquare-root cancellation at every primitive frequency, and the"
        "\nonly larger sums are the arithmetically forced ones at"
        "\nfrequencies divisible by a power of 3. Whatever blocks the pair"
        "\ninequality, it is not a failure of equidistribution of sigma."
    )


if __name__ == "__main__":
    main()
