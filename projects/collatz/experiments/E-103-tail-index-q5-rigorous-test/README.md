# E-103 — Tail index of W_v for q=5 (Tail-Index Conjecture, paper §3.3)

Related hypothesis: [`H-109-generalized-qx1-pressure-equation-exact-closed-form.md`](../../hypotheses/H-109-generalized-qx1-pressure-equation-exact-closed-form.md)
See also: [`H-129-q-adic-pole-analog-seymour.md`](../../hypotheses/H-129-q-adic-pole-analog-seymour.md) (a parallel front, different theoretical framing)

## What was done

After fixing paper §3 (annealed pressure equation + freezing
transition) and downgrading the martingale's tail index for q≥5 to a
Conjecture with no solid empirical support (the original H-109/H-113
measurement, Hill with 600 roots, had already been flagged as
statistically non-confirmatory), the scientific director successively
requested more robust tests, with explicit authorization to use
computation time and the Fable freely. The investigation went through
three rounds, each more rigorous than the last:

**Round 1** — a more careful Hill/Zipf test (`experiment_tail_index_q5.py`):
an 8x larger sample (5000 vs 600 roots), 4 headrooms, bootstrap. The
initial result seemed "encouraging" (close to predicted at the 5%
fraction).

**Round 2** — a full battery of 4 estimators (`full_battery.py`):
Gabaix-Ibragimov regression, bias-corrected Hill (Huisman et al.), GPD
MLE with threshold-stability sweep, and Clauset-Shalizi-Newman + Vuong
test against lognormal. Revealed that Round 1 had been overly
optimistic — see "Result" below.

**Round 3** — an EXACT test via population moment (`exact_moment_test.py`):
instead of a statistical estimator over a sample of roots, uses the
exact DP `Z_k(θ;u)` (already validated in the freezing tests) over the
COMPLETE population of residues mod 5^k. Decisive in principle (no
sampling noise), but limited by reachable depth (k≤11 due to memory).

**Discarded before Round 3** — an idea for calibration via a random-phase
i.i.d. tree (`stage0_iid_power_check.ABANDONED.py`) was abandoned for
two reasons: (1) circular (its index falls out algebraically from the
already-proven annealed pressure identity, at the point already known
to always be frozen — it cannot fail by construction); (2) raw node
count explodes combinatorially under i.i.d. phase (headroom=100: real
tree=42 nodes, synthetic>200000 nodes) — see the file for details.

## Round 2 Result (full battery) — a mixed picture

**Stability across headrooms**: excellent for Huisman (bias-corrected
Hill), which sits at ~1.61 across all 4 headroom levels, bootstrap CI
≈[1.48; 1.77] — comfortably covers the predicted 1.536.

**But**: the threshold-stability sweep (GPD) shows no clean plateau
near the predicted ξ (0.651) — ξ̂(u) decreases from ~0.58 to ~0.45 as
the threshold rises, with no stabilization. And the Vuong test favors
the **lognormal** alternative over the power law, with significance
(p≈0.03), in 3 of the 4 tested headroom levels.

Consulted the Fable to interpret: the 4 estimators, when read by the
tail depth each one summarizes, agree with each other on the SHAPE of
the curve — the apparent local index rises smoothly from ~1.3 (wide
window) to ~2.2 (narrow window), crossing the predicted value near the
10% window. In other words, the earlier "hits" were a window artifact,
not confirmation — a concave curve like this would "confirm" almost any
value between 1.3 and 2.2 at some depth. Fable's verdict: downgrade
from "encouraging" to "inconclusive".

## Round 3 Result (exact moment) — inconclusive, reason identified

Sanity check: M_k(1.0)=1.0 exactly at every k (forced by the
already-proven annealed pressure identity — confirms the
implementation).

For the tail index: M_k(p) saturates (decreasing increments) for
p≤1.6 and diverges (increasing increments) for p≥1.7 — which would
place the real index ABOVE the predicted 1.536 if taken at face value.

But, analyzing the RATIO between successive increments (not just the
sign): for p≥1.7 this ratio has already relaxed to the asymptotic
geometric regime at k=8-11; for p≤1.6, including the predicted value,
the ratio **is still moving** — the classic signature of "critical
slowing down" near any critical point, not evidence that criticality
lies above 1.6. The known q=5 transient (k^-0.222 decay) drops only
~7% between k=8 and k=11; halving it would require k≈250 — impossible
by exhaustive enumeration (cost 5^k). Extrapolation attempts
(Aitken/Richardson) gave unstable, unreliable values (the transient
appears oscillatory, not simply geometric — breaking the
extrapolator's assumption).

**Final verdict (Fable + our own check)**: inconclusive, not
disconfirming. This method cannot distinguish between the predicted
value sitting just below the real index (consistent with theory) or
well below it (evidence against). Going deeper by exhaustive
enumeration doesn't resolve it — the cost grows exponentially (5^k)
while the transient decays as a slow power law.

## Consolidated verdict (both rounds together)

Neither route confirms the Conjecture for q≥5, neither refutes it.
Both are far more informative than the original under-powered
measurement. The paper's text (main.tex/main-pt-br.tex, §3.3) was
rewritten to reflect this honestly — see the corresponding commit.
More promising paths to resolve this for good, if the line is resumed:
a pre-registered Clauset-Shalizi-Newman-style comparison with a much
larger budget than exhaustive enumeration, explicitly testing against a
log-periodic fit (see the correction below — the "subdominant
spectrum" route was closed by E-105: there is no isolated subdominant
to control).

**Terminology correction (2026-07-19, see H-129/E-105)**: the phrase
"subdominant complex root of the transfer operator", which appeared
here and elsewhere in the project, was wrong. A consultation with the
Fable resolved the correct formalization of the operator (the dual pair
L_α/M_α acting on Z_q) and showed, with exact numerical verification in
E-105, that M_α has spectrum EXACTLY {Λ,0} at any truncation level —
a perfect spectral gap, with no isolated subdominant eigenvalue. The
k^-0.222 transient is not a linear spectral phenomenon — it belongs to
a different, nonlinear layer (see Stage 2 below for what that layer
turned out NOT to be).

## Stage 2 (2026-07-19) — log-periodic hypothesis tested and NOT supported

We raised the hypothesis that the k^-0.222 transient was a
log-periodic lattice effect (branch weights are powers of 2). Before
testing, we consulted the Fable to DERIVE the predicted period (not fit
it to the data — the same trap that already caught the a* result in
H-129).

**Derivation (Fable)**: the multipliers A_a=(5·2^-a)^θ form a
lattice shifted by type (u0 mod 5), with shift
b_i/s=(log₂5−a₀(i))/4 — **irrational**, since log₂5 is irrational (5
is not a power of 2). By the arithmetic/non-arithmetic dichotomy of
implicit renewal theory (Goldie 1991), this is the **non-arithmetic**
case: no asymptotic log-periodic correction should be expected (the
phase rotates by log₂5 per level, irrational, and "washes out" as k
grows — Blackwell's theorem). Two candidate periods would only be
visible as a finite-depth artifact, with expected DECREASING amplitude
in k: θ·log2=0.4512 ("union", all a's) and 4θ·log2=1.8047 ("by-type",
spacing d=ord₅(2)=4), in natural log of x.

**Test** (`stage2_periodogram.py`): pure power-law fit via CSN on the 4
W_v samples (headroom 10⁵-10⁸, n=5000 roots each, already existing from
E-103 Rounds 1-2), residual log(S_emp/S_pred) at t=log(x/xmin),
Lomb-Scargle power measured EXACTLY at the two pre-registered periods
(not chosen after the fact), compared against the background noise
level (a wide grid of periods).

**Result**: at none of the 4 headrooms does the power at the predicted
periods exceed the 95th percentile of the background noise. At the
"union" period (well-powered — 6.7 to 9.7 cycles fit within the data's
range), the power is essentially null (0.003-0.010, mean background
noise ~0.11-0.14). At the "by-type" period, 3 of the 4 headrooms also
give near-zero power; the one nontrivial value (H=10⁸, power=0.1985)
still falls below the p95 (0.263), has only 1.7 cycles within the
data's range (below the recommended minimum), and appears at the
DEEPEST headroom — the opposite of what the theoretical prediction
would say (amplitude should decrease with k, not appear only at the
deepest k). The three facts triangulate to noise, not signal.

**Verdict**: the log-periodic hypothesis was **tested and not
supported** — consistent with the Fable's own theoretical prediction
(non-arithmetic case, no asymptotic log-periodicity expected). This is
a mutual theory+data confirmation, not a favorable coincidence.
A phase-coherence check across headrooms (planned as a structural
guard) had no object to check — there's no amplitude to check phase
on.

**What this does NOT close**: the origin of the k^-0.222 transient
remains open. We have now refuted two candidate mechanisms (isolated
spectral root — E-105; log-periodicity — here). This doesn't "explain"
the transient, it only eliminates two specific explanations. The
numerical origin of the value "0.222" itself remains unlocated in the
project (see the correction in H-109/E-105).

**Complementary check on the k axis** (`stage3_k_axis_check.py`, Round
3 data, k=5..11): the ratio of successive increments of M_k(p) is
MONOTONIC in k, with no sign of oscillation, for the 3 values of p near
the predicted index — corroborates (doesn't prove anew) the absence of
oscillation already established in E-105/Stage 2. An attempt to fit
|ratio(k)−1|~k^-χ to compare against "0.222" was made and DISCARDED
(advisor review): the target "1" is only asymptotically correct exactly
at the critical p, and n=5 smooth/correlated points doesn't support a
reliable standard error (the fitted χ varied from 0.98 to 3.60 across
the 3 tested p's — a sign of underpowering, not a real measurement).
The code stays in the repository for transparency, but the number
should not be cited. Resolving the origin of "0.222" still requires
either locating the original derivation, or extending k beyond the
5^k memory ceiling (a new formulation, not a script tweak) — neither
is an immediate action.

## Stage 4 (2026-07-19) — scale family by residue type: CONFIRMED (but doesn't test κ)

The Fable's collateral prediction (relative weights by type C_i ∝
2^(−a₀(i)θκ), i.e. (2⁻⁴,2⁻³,2⁻¹,2⁻²) for types u0 mod 5 = 1,2,3,4) was
tested, not left for later. I reconstructed the root list (same seed,
without redoing the DFS) to recover each already-collected W_v sample's
type, and compared conditional quantile ratios x_i/x_1
(top30%/20%/10%) against the prediction (C_i/C_1)^(1/κ),
κ=α₊/α₋=1.536290.

**Result**: matches very well (2-9% deviation) across ALL 4 independent
headrooms and 3 tail levels, with notable cross-stability (e.g.
x₃/x₁≈4.06-4.12 across 4 orders of magnitude of headroom — doesn't
look like noise). I consulted the Fable to confirm the translation, and
it revealed a crucial point I had missed: **κ cancels algebraically**
in this ratio — (C_i/C_j)^(1/κ) = 2^((a₀(j)−a₀(i))θ), independent of
κ. That is, this test confirms the **exact scale family
W_i =_d 2^(−a₀(i)θ)·W\*** (the same distribution for every residue
type, only rescaled by θ and a₀) and rejects the "C_i enters linearly"
alternative (would predict x₃/x₁=8; measured 4.06-4.12) — but it
**does not test the tail index κ itself**. Exact scope: confirms θ and
the multi-type decomposition, not κ; and it's exact only in the
idealized model (systematic 2-9% residuals measure where the real tree
diverges from the uniform-i.i.d.-child-residue hypothesis).

## Stage 5 (2026-07-19) — rescaled pool by type: doesn't improve the test of κ

An attempt to use Stage 4's scale family for a cleaner test of κ: I
rescaled the 5000 samples by the predicted factor 2^(a₀(type)θ) and
ran the same battery of 4 estimators (Stage/Round 2) on the rescaled
pool. **No improvement**: Huisman came out at ~1.50 (95% CI
[1.38;1.63], covers 1.536, stable across the 4 headrooms) and
Gabaix-Ibragimov at ~1.57 — consistent with κ=1.536, not confirmatory
(the same pattern as always); GPD still shows no clean threshold
plateau. CSN+Vuong seemed to get worse (lognormal favored with p<0.001
in 3 of the 4 headrooms), but this is an ARTIFACT: in these 3 cases the
KS-optimal x_min fell inside the BODY of the distribution (n_tail~2000,
~40% of the sample, not a tail test). The one headroom with a genuine
tail per CSN (H=10⁵, x_min=95, n_tail=112) gave "indistinguishable"
(p=0.93), not lognormal — evidence that the "lognormal" signal in the
other 3 is a body artifact, not a tail one. Global lognormality is
already ruled out another way: M_k(p) diverges for p≥1.7 (Round 3) —
lognormal has all finite moments, incompatible with a diverging exact
moment.

**Consolidated verdict for Stages 4-5**: a new, real structural finding
(scale family by type), but of limited scope — doesn't resolve nor
approach resolving the Tail-Index Conjecture. κ remains **consistent
with 1.536290, not confirmed**: the same obstacle as always (5000
samples don't reach sufficient tail depth to decide), now with the
precise reason why the quantile-ratio test can't help (it's
κ-invariant by construction).

## Stage 6 (2026-07-19) — 20x larger sample: evidence moves from inconclusive to strongly favorable

Item 3 of the next-steps list, finally executed: 100,000 roots (vs.
5,000 in Rounds 1-2), same 4 headrooms, generated in parallel (12
processes, ~73 min — `stage6_large_sample_generation.py`; V_RANGE
expanded 10x so as not to exhaust the pool of valid roots). Same
battery of 4 estimators (`stage6_large_sample_battery.py`).

**Result, qualitatively different from every previous round**:

- **GPD with a CLEAN threshold plateau for the first time**: ξ stable
  at 0.63-0.68 (predicted 0.6509) across ALL 9 threshold levels and 4
  headrooms — the systematic instability from Round 2/Stage 5 is gone.
- **Huisman very stable**: 1.545 (n/2), 95% CI [1.51;1.58] covering
  1.536290, identical across the 4 headrooms.
- **CSN+Vuong "indistinguishable" at all 4 headrooms** (p=0.13-0.16) —
  the previous round (n=5000) favored lognormal in 3/4 cases; this
  signal no longer appears at n=100,000.

**Two sanity calibrations** (`stage6_calibration_checks.py`, requested
by the advisor before any stronger conclusion):

1. **Synthetic null** (exact pure Pareto, κ=1.536290, n=100,000):
   Huisman gave 1.545/1.538 — nearly identical to the real value
   (1.545/1.503) — confirms Huisman is well-calibrated at this n. GPD
   on the synthetic ALSO shows "instability" at higher thresholds even
   though it's an exact Pareto — the noise seen in the real data is
   within what's expected from sampling chance, not misspecification.
   CSN on the synthetic gave 1.55 with n_tail≈63,000 (nearly the whole
   sample, correct for a pure Pareto); on the real data it gave 1.40
   with n_tail≈7,300 (~7%) — an expected difference (real data has a
   genuine non-power-law body, only the extreme tail is) — the lower
   CSN value on real data looks like a known weakness of the estimator
   under this body+tail structure, not evidence against κ.
2. **Invariance to θ' (rules out circularity)**: predicted κ=1/θ and
   W=count/H^θ looks self-referential. Recomputed W with θ'=0.60
   (deliberately wrong) — every number in the battery came out
   IDENTICAL to those with the real θ. Confirms κ comes from the data,
   not a circular artifact of W's definition.

**Honest verdict**: this is NOT "confirmed" nor "closed". (1) Vuong
went to "indistinguishable", not "power law wins" — removes the
earlier disconfirmation, doesn't confirm over lognormal; (2) W
provably still hasn't converged (median drops monotonically from 2.04
at H=10⁵ to 0.94 at H=10⁸, even with the tail index stable — shape
stabilizes before scale); (3) the spread across estimators
(1.40-1.55) is now calibrated, not just observed — calibrated isn't
the same as decided. But the evidence moves from INCONCLUSIVE to
STRONGLY FAVORABLE for κ=1.536290 — exactly the pattern the paper
itself (§3.3) proposed as necessary ("pre-registered comparison... a
much larger budget"). See H-129 for the full record.

## Files

- `experiment_tail_index_q5.py` — Round 1 (simple Hill/Zipf).
- `results.json` — Round 1 results.
- `full_battery.py` — Round 2 (battery of 4 estimators).
- `stage0_iid_power_check.ABANDONED.py` — a discarded idea, documented.
- `stage1_exact_moment_test.py` — Round 3 (exact population moment).
- `stage1_moment_results.json` — Round 3 results (k=5..11).
- `rerun_save_raw.py` — helper script that reruns Round 1 saving raw
  W_v samples (used to feed Round 2 without redoing the DFS).
- `stage2_periodogram.py` — Stage 2 (pre-registered log-periodic test).
- `stage2_periodogram_results.json` — Stage 2 results (4 headrooms).
- `stage3_k_axis_check.py` — monotonicity check on the k axis (no
  citable fit — see the "Complementary check on the k axis" section
  above).
- `stage4_type_constants_check.py` / `stage4_type_constants_results.json`
  — Stage 4 (scale family by type, confirmed).
- `stage5_rescaled_pool_battery.py` / `stage5_rescaled_pool_results.json`
  — Stage 5 (rescaled pool, doesn't improve the test of κ).
- `stage6_large_sample_generation.py` — Stage 6, generates 100,000
  roots in parallel (saves to `/tmp/tail_index_q5_large_sample.json`,
  not committed — deterministically regenerable, ~73 min, 12
  processes).
- `stage6_large_sample_battery.py` / `stage6_large_sample_battery_results.json`
  — battery of 4 estimators on the large sample (favorable evidence).
- `stage6_calibration_checks.py` / `stage6_calibration_output.txt` —
  synthetic null + invariance to θ' (the two Stage 6 sanity
  calibrations; the script doesn't save JSON, only prints — full
  output preserved in the .txt).

Public mirror (identical code, adapted to be self-contained):
`collatz-endogeny/sec3-pressure-equation/` (`full_battery.py`,
`exact_moment_test.py`).

## Reproduce

```
python3 experiment_tail_index_q5.py    # ~20 min, Round 1
python3 full_battery.py                # ~25 min, Round 2 (needs the raw samples — see rerun_save_raw.py)
python3 stage1_exact_moment_test.py    # ~15 min (k up to 11), uses ~10-15GB RAM at peak
python3 stage2_periodogram.py          # seconds, needs the raw samples (rerun_save_raw.py)
python3 stage3_k_axis_check.py         # seconds, uses stage1_moment_results.json
python3 stage4_type_constants_check.py # ~1 min, reconstructs roots + raw samples
python3 stage5_rescaled_pool_battery.py # ~2 min, same
python3 stage6_large_sample_generation.py # ~73 min (12 processes), 100k roots
python3 stage6_large_sample_battery.py    # ~2 min, uses the output above
python3 stage6_calibration_checks.py      # ~2 min, same
```

## Next steps (if the line is resumed)

1. ~~Analytic control of the transfer operator's subdominant
   spectrum~~ — **closed by E-105**: there's no isolated subdominant
   eigenvalue to control, the linear layer's spectral gap is perfect
   and proven.
2. ~~Test the log-periodic fit against the pure power law~~ —
   **closed by Stage 2 (2026-07-19)**: tested and not supported,
   consistent with the Fable's theoretical derivation (non-arithmetic
   case). See section above.
3. ~~Full statistical battery (pre-registered CSN+Vuong) with a much
   larger sample (10^5+ roots)~~ — **done, Stage 6 (2026-07-19)**:
   100,000 roots, evidence moves from inconclusive to strongly
   favorable for κ=1.536290 (GPD with a clean plateau for the first
   time, Huisman very stable, Vuong stops favoring lognormal). Two
   sanity calibrations (synthetic null, invariance to θ') revealed no
   artifact. NOT confirmation/closure (Vuong is "indistinguishable",
   not "power law wins"; W hasn't converged yet — median drops
   monotonically with headroom). See the "Stage 6" section above and
   H-129 for the full record. To go further: larger headroom (>10⁸)
   would require more DFS time per root, not yet attempted.
4. See H-129 for a parallel theoretical front (ergodic optimization)
   that might give an exact characterization of the freezing without
   relying on numerical estimators.
5. ~~Test the k^-0.222 transient on the axis where it was observed~~ —
   a light check done (`stage3_k_axis_check.py`): no oscillation
   visible in the ratio of M_k(p) increments, k=5..11. Only 5-7 points
   exist because of the real 5^k memory ceiling — can't measure
   amplitude decay with k nor locate "0.222" with this data. **Real
   item that remains, not executed**: locate the original derivation
   of "0.222" (a search, not new computation) or extend k beyond the
   current ceiling (a new formulation, high cost).
6. ~~Falsifiable collateral prediction (weights by residue type)~~ —
   **done, Stage 4 (2026-07-19)**: CONFIRMED (exact scale family by
   type), but shown not to test κ (cancels algebraically). An attempt
   to use this to improve the test of κ (Stage 5) was also made — it
   didn't help. See sections above.
