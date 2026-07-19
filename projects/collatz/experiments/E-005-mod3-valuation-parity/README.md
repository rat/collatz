# E-005 — Lemma: residue mod 3 determined by valuation parity

Related hypothesis: [`H-005-mod3-valuation-parity-lemma.md`](../../hypotheses/H-005-mod3-valuation-parity-lemma.md)

## What was tested

An algebraic (not statistical) lemma: for T(n) = (3n+1)/2^{a(n)}, T(n)
mod 3 depends only on the parity of a(n) — never on the residue of n
mod 3. A short proof is in the hypothesis file. Consequence: a value
divisible by 3 never reappears after the orbit's first odd step.

Prediction derived by combining this lemma with the already-established
geometric distribution of a(n) (H-001): among subsequent terms of any
orbit (excluding the starting number), the ratio of residue 1 vs 2 mod
3 should be 1:2 (not 1:1), and residue 0 should never appear.

## Result

- **(a) Exact algebraic verification**: 0 violations in 777,748
  verified steps (20,000 orbits, 40 steps each) — confirms the
  identity without exception, as expected for a proof verified
  computationally (not a statistical result).
- **(b) Predicted ratio**: residue 1 mod 3 observed in 33.47% of cases
  (predicted 33.33%), residue 2 mod 3 in 66.53% (predicted 66.67%),
  observed 1:2 ratio = 0.5032 (predicted exactly 0.5). Excellent
  agreement.

Reproduce: `python3 experiment.py 20000 40`

## Why this matters

It's the first piece of **exact, proven** structure (not a statistical
correlation) found in the project — it directly connects the H-001
result (geometric distribution of a(n), independence) to mod-3
arithmetic structure, within the "2-adic/ergodic" framework from the
literature (`literature/approaches-2adic-ergodic.md`): the 1:2 ratio is
essentially an equidistribution statement with respect to a
non-uniform measure induced by the dynamics — exactly the kind of
object 2-adic-map ergodic theory studies.

## Relation to H-004 (important, don't confuse)

This lemma explains the behavior of **subsequent** terms within an
orbit — it does not explain why the **starting** numbers that are
stopping-time record holders (H-004) avoid residue 2 mod 3. That
remains an open question. The lemma here is a real, useful piece of
structure, but it doesn't close the H-004 finding.

## Status of H-005

**Confirmed** (algebraic proof + computational verification with no
exceptions).
