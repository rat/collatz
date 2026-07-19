# E-052 — Verification of paper #010 (Ruiz Castillo, "Residual Central Limit Theorem")

## Goal

Verify "Teorema Central del Límite Residual de Ruiz Castillo para la
dinámica acelerada de la Conjetura de Collatz" (Juan Carlos Ruiz
Castillo, 29 pages). The third paper by this author reviewed in the
collection (the first was item 001/H-039, the second item 008/H-050).
Proposes a Central Limit Theorem for the fluctuations of the "residual
debt" L_k(n) = k·log₂(3) − A_k(n) — the same elementary quantity as
always (standard logarithmic drift), now through the lens of
convergence in distribution.

**Central finding from the read**: the main result is formally labeled
"Conjecture 4.2" (not "Theorem") in the BODY of the paper, despite the
TITLE saying "Theorem" — the author himself honestly lists 5
unestablished hypotheses (existence of a residual Gibbs measure,
ergodicity, an adequate function space, spectral gap of the residual
transfer operator, positive residual variance) on which the result
depends, and never proves or constructs them. The paper's own
conclusion explicitly states: "Este marco no demuestra la Conjetura de
Collatz" (This framework does not prove the Collatz Conjecture).

## What we did

**Part 1 — algebraic identities proven in the paper's body**
(elementary, correct): Theorem 2.3 (L_k(n) = −S_k(φ), a direct
rewriting of the definition) and Proposition 2.5 (Var(L_k)=Var(−S_k φ),
trivial) — tested on 27 values of n × 5 values of k, 0 failures.

**Part 2 — a testable empirical consequence of "Conjecture 4.2"**:
since the conjecture's technical hypotheses (residual Gibbs measure,
spectral gap) are never constructed in the paper, we directly tested
the observable PREDICTION — asymptotic normality of
Z_k = (L_k(n) − k·m_RC)/√k, with m_RC = log₂(3)−2 — on REAL Collatz
trajectories (not an abstract i.i.d. model), for k = 5, 20, 50, 100,
300.

## Integrity note: sampling bug fixed before reporting

The first version sampled n uniformly from `range(3, 10**15, 2)` for
every k, requiring (via `require_no_fixed_point=True`) that the
trajectory not reach the fixed point n=1 before completing k steps. The
average length of a Syracuse trajectory for n of ~50 bits is
log₂(n)/(2−log₂3) ≈ 120 steps; for k=300 (~4.9 standard deviations
above the mean) the rejection rate got so close to 100% that the retry
loop never completed — the background process got stuck for 17 minutes
with no progress. Fixed by scaling the sampling range with k: the
number of bits of n is chosen so that the EXPECTED trajectory length is
~3k+50, guaranteeing a high acceptance rate even for k=300 (full run in
~5 seconds after the fix). A cap on attempts (`max_attempts`) was also
added, raising an explicit error instead of running indefinitely, in
case the rejection rate becomes unexpectedly high again in the future.

## Result

**No real mathematical error found.** Part 1 confirms the algebraic
identities (trivial rewrites of definitions). Part 2 shows that Z_k's
empirical moments converge exactly as a standard Gaussian would predict
as k grows:

| k   | mean Z_k | var Z_k | skewness | kurtosis |
|-----|-----------|---------|------------|---------|
| 5   | -0.0201   | 2.0163  | -0.9590    | 4.3795  |
| 20  | 0.0037    | 1.9703  | -0.4592    | 3.3472  |
| 50  | 0.0081    | 1.9882  | -0.2916    | 3.1821  |
| 100 | 0.0070    | 1.9680  | -0.2366    | 3.0770  |
| 300 | -0.0031   | 1.9832  | -0.1002    | 2.9843  |

Variance stabilizes near 2 (= σ²_RC = Var(a_j), already established in
H-001/H-011), skewness → 0 and kurtosis → 3 as k grows — i.e., the
conjecture's PREDICTION is **empirically plausible on real data**, even
though the technical hypotheses that would support it are never
constructed or proven in this paper. This is the first real numerical
verification of this prediction (the paper itself contains none).

**"Theorem" vs. "Conjecture" labeling**: consistent with the pattern of
partial honesty already seen in the other reviewed Ruiz Castillo papers
(H-039, H-050) — elementary correctness in what is actually proven, no
numerical verification of its own, but the author is honest in labeling
the central result as conjectural in the body of the text.

**Citation pattern**: ~20 references, all self-citations by Ruiz
Castillo himself — confirms the pattern already seen in H-039/H-050 of
applying, one at a time, a different classical concept (drift,
pressure, bounds, dimension, entropy, Gibbs measures, variational
principle, transfer operator, spectral theory, CLT, large deviations)
to the SAME quantity L_k(n).

See `hypotheses/H-052-ruiz-castillo-clt-review.md`.

## How to run

```
/home/rat/.venv/bin/python3 experiment.py
```
