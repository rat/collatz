# E-037 — Verification of Pratiher's (2026) Conjecture 10.4

Related hypothesis: [`H-037-pratiher-form-off-by-one.md`](../../hypotheses/H-037-pratiher-form-off-by-one.md)

## What was tested

Original goal: verify whether Freq_a(N) (the asymptotic fraction of
{1,...,N} whose orbit first reaches a power of 2 ≡8 mod9, "form 𝔞" in
Pratiher's notation) converges to α≈0.9762 as the paper claims
(Conjecture 10.4), and whether this value is derivable via
equidistribution/transfer-operator methods.

Implementation: for each n∈[1,N], simulates the direct (not
accelerated) Collatz trajectory until finding the first power of 2
(checked via the bit trick `n & (n-1) == 0`), extracts the exponent M,
and classifies `M mod 6` per Pratiher's own table (Theorem 4.3: 0↔𝔡,
1↔𝔠, 2↔𝔟, 3↔𝔞, 4↔𝔣, 5↔𝔢). Memoizes via trajectory convergence (multiple
n share a tail).

## Result

**The numerical distribution matches Pratiher's table (Observation
10.2) almost exactly — but under the WRONG labels.**

| N | my dominant form (M even) | Pratiher reports |
|---|---|---|
| 10^6 | 𝔣 = 0.976082 | Freq_a(10^6) — not listed in the paper, but the trend matches |
| 10^7 | 𝔣 = 0.9761136 | Freq_a(10^7) = 0.97611 |
| 10^7 | 𝔟 = 0.0238808 | Freq_c(10^7) = 0.02388 |

All 6 forms match **exactly** under a cyclic shift of 1 position in the
correspondence (M mod6 ↔ letter): the value Pratiher reports for form X
is, number for number (including in the rare tails: 4, 4, 4, 44 at
10^7), what this script computes for the form at
M ≡ (X's M + 1) mod 6. See `hypotheses/H-037...md` for the full
correspondence table and the theoretical argument (parity, identical to
H-012's mechanism) proving that the REAL dominant form must have M
even — never odd, as the paper's Table 10.2 claims.

Additional (exact, not just numerical) verification: the 3 "tail" forms
with M odd (the only ones that can come from n ALREADY being a power of
2 with an odd exponent, since no non-trivial trajectory can enter an
odd exponent) have an EXACT count of 4 each at N=10^7 — matching exactly
the theoretical count of odd-exponent powers of 2 ≤10^7 distributed by
residue mod6 (12 odd exponents ≤23, 4 in each mod6 class). See the
"Exact verification" section in H-037.md.

## Reproduce

`/home/rat/.venv/bin/python3 experiment.py [N]` (with no argument, runs
N=10,100,...,10^7 in sequence; ~8s for N=10^7 single-threaded with
memoization).

## Status of H-037

**The original question refuted** (that isn't actually what motivated
the investigation — the question "can α be derived via
equidistribution" was left hanging), but **something more concrete was
found**: very strong evidence (exact, not approximate, correspondence
across all 6 classes) of an off-by-one labeling error in Pratiher's
paper — the numbers (0.9762 / 0.0238) are correct, the assignment of
which "form" carries which number is shifted by 1 position in the
6-cycle.
