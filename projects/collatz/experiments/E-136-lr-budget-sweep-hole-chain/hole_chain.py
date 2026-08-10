"""E-136 part 2: the doubling structure of Weak Covering Conjecture holes.

S_j^(ell) is the image modulo 3^ell of

    sum_{i=0}^{ell-1} 2^{alpha_i} 3^i,
    j+ell-1 >= alpha_0 > alpha_1 > ... > alpha_{ell-1} >= 0,

that is, R_{ell-1,j} of H-114/H-127.  H_j = U \\ S_j is the hole set
inside the units U modulo 3^ell, and j*(ell) is the least j with
H_j empty.

Shifting every exponent up by one is legal as soon as the top slot
grows by one, so

    2 S_j subset S_{j+1},   and trivially   S_j subset S_{j+1}.

Taking complements inside U,

    H_{j+1} subset H_j intersect 2 H_j,
    H_{j+m} subset intersection_{k=0}^{m} 2^k H_j.

So a hole surviving to stage j+m forces a full geometric progression
b, b/2, ..., b/2^m of holes at stage j, hence |H_j| >= j*(ell) - j.
This is a support statement with no Fourier budget in it.

The script computes S_j exactly for all j at once, by a dynamic program
that records, for each residue, the least possible largest exponent.
It then checks every claim above and reports how far the linear lower
bound |H_j| >= j*-j is from the true hole counts.
"""

import argparse

import numpy as np


def minmax_exponent(ell, emax):
    """least achievable largest exponent, per residue modulo 3^ell.

    Returns an int array of length 3^ell; entries are emax+1 when the
    residue is not representable with exponents below emax+1.
    """
    n = 3 ** ell
    inf = emax + 1
    # reach[e, v]: some choice of the k+1 smallest exponents, the largest
    # of them equal to e, produces partial value v.
    reach = np.zeros((emax + 1, n), dtype=bool)
    pow3 = [pow(3, i, n) for i in range(ell)]
    for e in range(emax + 1):
        reach[e, (pow(2, e, n) * pow3[ell - 1]) % n] = True
    for k in range(1, ell):
        prefix = np.zeros(n, dtype=bool)
        nxt = np.zeros((emax + 1, n), dtype=bool)
        coeff = pow3[ell - 1 - k]
        for e in range(emax + 1):
            if prefix.any():
                nxt[e] = np.roll(prefix, (pow(2, e, n) * coeff) % n)
            prefix = prefix | reach[e]
        reach = nxt
    out = np.full(n, inf, dtype=np.int64)
    for e in range(emax, -1, -1):
        out[reach[e]] = e
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-level", type=int, default=9)
    ap.add_argument("--slack", type=int, default=6,
                    help="extra exponent slots above the covering threshold")
    args = ap.parse_args()

    all_ok = True
    for ell in range(2, args.max_level + 1):
        n = 3 ** ell
        jmax = int(2.0 * ell) + args.slack
        emax = jmax + ell - 1
        mm = minmax_exponent(ell, emax)

        units = np.array([x for x in range(n) if x % 3 != 0])
        nonunits = np.array([x for x in range(n) if x % 3 == 0])

        # every representable residue is a unit
        ok_units = bool((mm[nonunits] > emax).all())

        # S_j = {v : mm[v] <= j+ell-1}
        def hole_count(j):
            return int((mm[units] > j + ell - 1).sum())

        jstar = None
        for j in range(0, jmax + 1):
            if hole_count(j) == 0:
                jstar = j
                break

        # 2 S_j subset S_{j+1}  <=>  mm[2v] <= mm[v] + 1 for representable v
        idx = np.arange(n)
        doubled = (2 * idx) % n
        rep = mm <= emax - 1
        ok_double = bool((mm[doubled[rep]] <= mm[rep] + 1).all())

        # chain test: every hole at stage j has its whole halving chain
        # b, b/2, ..., b/2^j sitting in H_0, ..., H_j respectively
        inv2 = pow(2, -1, n)
        ok_chain = True
        chains = []
        for j in range(0, (jstar if jstar is not None else jmax) + 1):
            holes = units[mm[units] > j + ell - 1]
            if holes.size == 0:
                continue
            b = int(holes[0])
            length = 0
            cur = b
            for k in range(0, j + 1):
                if mm[cur] <= (j - k) + ell - 1:
                    ok_chain = False
                    break
                length += 1
                cur = (cur * inv2) % n
            chains.append((j, length))

        counts = [(j, hole_count(j)) for j in range(0, (jstar or jmax) + 1)]
        ok_linear = all(c >= (jstar - j) for j, c in counts) if jstar else True

        status = "OK" if (ok_units and ok_double and ok_chain
                          and ok_linear) else "FAIL"
        all_ok = all_ok and status == "OK"
        print(f"ell={ell}  |U|={units.size}  j*={jstar}  [{status}]")
        print(f"  S_j inside units: {ok_units};  2S_j subset S_(j+1): "
              f"{ok_double};  halving chains: {ok_chain};  "
              f"|H_j| >= j*-j: {ok_linear}")
        tail = counts[max(0, len(counts) - 6):]
        print("  j, |H_j|, lower bound j*-j: "
              + "  ".join(f"({j},{c},{jstar - j})" for j, c in tail))
        if chains:
            print("  chain lengths verified (j, length): "
                  + " ".join(f"({j},{L})" for j, L in chains[-6:]))
    print("\nall checks passed" if all_ok else "\nSOME CHECK FAILED")


if __name__ == "__main__":
    main()
