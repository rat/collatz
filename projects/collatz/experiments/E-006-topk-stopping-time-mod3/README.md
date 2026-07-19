# E-006 — Replication attempt with top-K by raw value (not strict record holders)

Related hypothesis: [`H-006-top-k-stopping-time-mod3.md`](../../hypotheses/H-006-top-k-stopping-time-mod3.md)

## What was tested

We tried to increase the statistical power of the H-004 mod-3 finding
by using the top-K numbers by raw stopping time (K=200, 1000) over a
large interval (1M-30M), instead of requiring the strict "record
holder" definition (beats every m < n).

## Result

No mod-3 bias was detected in the raw top-K (~uniform distribution,
32-35% in each class, p > 0.18 in all tests).

## Why this does NOT refute H-004 (important diagnosis)

Investigating the discrepancy, we printed the actual numbers in the
"top-50 by raw value" and compared them to the official strict
record-holder list (OEIS A006877). They are **different populations**:
only 5 of the 50 numbers in the raw top-K are true strict record
holders (e.g. 15733191, 14934241, 11200681, 8400511, 6649279); the rest
are numbers with a coincidentally high stopping time that **never set a
record** (a smaller n had already reached an equal or higher value).

This means E-006 tested a hypothesis related to, but distinct from,
H-004 — "numbers with high stopping time in general" rather than
"numbers that set a new record." The mod-3 bias appears to be specific
to the second notion (strict record holder), not the first. See the
corrected, definitive analysis in
`experiments/E-004-true-record-holders/README.md` (using the complete
official strict-record-holder sequence, n=148), which confirms the
finding with overwhelming statistical strength (p < 10^-13).

## Status of H-006

Not supported as formulated (raw top-K doesn't reproduce the bias) —
but the diagnosis was valuable: it clarified that "strict record
holder" and "raw top-K" are genuinely different populations for this
question, and it helped (indirectly) identify the transcription error
corrected in E-004.
