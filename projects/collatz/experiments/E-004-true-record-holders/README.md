# E-004 — True stopping-time record holders

Related hypothesis: [`H-004-true-record-holders.md`](../../hypotheses/H-004-true-record-holders.md)

> **⚠️ Correction (2026-07-13)**: the original version of this
> experiment used a partially incorrect list of record holders (typed
> from memory instead of coming from the script's actual output — see
> [`CORRECTION.md`](CORRECTION.md)). The record-holder search code
> (`experiment.py`) was correct; the error was only in the list used
> afterward for the mod-3/mod-9 characterization. The analysis below
> uses the official, complete sequence (OEIS A006877, 148 terms,
> Roosendaal source) and **replaces** the earlier conclusion — the
> finding got stronger, not weaker, with correct data.

## What was tested

True record holders (n such that total_stopping_time(n) exceeds every
m < n) and their residual structure mod 3 / mod 9 / mod 27, using the
official, complete Roosendaal/OEIS A006877 sequence (148 terms, from
n=1 up to ~1.47×10^19 — far beyond what can be scanned in plain Python
in this environment). Data file: `oeis_A006877_record_holders.txt`.
Reproduce: `python3 experiment_v2_oeis_verified.py`.

We also separately tested (b) internal lag-1 autocorrelation of each
record holder's orbit (see its own section below) — this part was not
affected by the transcription error, since it used the real scan (up
to 20-50M) directly.

## Result (a) — residue, with correct and complete data

| modulus | classes with 0 occurrences | chi2 | dof | p |
|---|---|---|---|---|
| 3  | none | 76.39  | 2  | 5.2×10⁻¹⁴ |
| 9  | {4, 5, 8} | 118.11 | 8  | 3.2×10⁻¹⁹ |
| 27 | {4,5,8,11,13,14,17,20,22,23,26} | 174.54 | 26 | 1.8×10⁻²² |

Distribution mod 3: **85 record holders ≡0, 62 ≡1, only 1 ≡2**
(expected uniform: ~49.3 each). The single ≡2 mod 3 case is **n=2** — a
trivial record holder (1-step orbit). **Excluding this edge case, 0 of
the remaining 147 record holders are ≡2 mod 3.**

At mod 9, classes 4, 5, and 8 (all ≡2 mod 3) never occur — consistent
with the mod-3 finding. At mod 27, 11 of the 27 classes never occur.

### Why this isn't tautological

As discussed in H-005 (`experiments/E-005-mod3-valuation-parity/`),
there is a proven lemma linking the residue mod 3 of **subsequent
terms** of an orbit to the parity of that step's valuation — but this
lemma doesn't apply to an orbit's **starting** number (there is no
"previous step" for it). The bias found here is about the starting
number (the record holder itself), so H-005 doesn't automatically
explain it. It remains a genuine, very well-verified empirical pattern,
but without a complete mechanistic explanation yet.

### What we ruled out along the way (important not to repeat)

We tried replicating this finding using "top-K by raw stopping-time
value" instead of strict record holders
(`experiments/E-006-topk-stopping-time-mod3/`) and did not see the same
bias. Investigating why, we found these are **different populations**:
many numbers in the "raw top-K" never set any record (they just happen
to have a high value). This doesn't refute the finding — it just shows
that "strict record holder" is a more restrictive, special notion than
"among the highest values," and the mod-3 bias appears to be specific
to strict record holders.

## Result (b) — internal autocorrelation, with confounder control

(This part was not affected by the transcription error.)

First round (uncontrolled): record holders had mean lag-1
autocorrelation 0.076-0.106, typical 0.038-0.046, "significant"
difference (p ~0.001-0.0001).

We identified a confounder: record holders have systematically longer
orbits (mean 149 steps vs 73 for the filtered typical group), and the
sample autocorrelation estimator has a known bias depending on series
length (~-1/(L-1) for short i.i.d. series). Controlling via regression
adjusted on the typical group, the record holders' mean residual
dropped to 0.023 (p=0.053) — **not significant** at the project's 0.01
cutoff. The "naive" difference was mostly explained by the short
sample-length bias.

## Status of H-004

- Internal autocorrelation: **not supported** (doesn't survive
  confounder control).
- **Residual mod-3/9/27 structure of record holders: strong, robust
  finding**, now verified with complete official data (n=148, p <
  10⁻¹³ across every tested modulus). Still no complete mechanistic
  explanation — a genuine candidate for future theoretical
  investigation.
