# E-041 — Verification of paper #005 (Seymour, "A Regular Expression Language for the Collatz Graph")

Related hypothesis: [`H-041-seymour-regex-language-review.md`](../../hypotheses/H-041-seymour-regex-language-review.md)

## What was tested

A paper explicitly labeled "working paper", which clearly separates
**proven** results from **conjectured** ones. We tested the three
central results claimed as proven:

- **Proposition 3.1** (Steiner-circuit arithmetic via the natural map
  C): confirmed in 20,000 random cases, no exceptions.
- **Theorem 3.6** (length of the "7 mod 8" run = v₂(n+1)−2): confirmed
  in 50,000 random cases, no exceptions.
- **Corollary 2.2** (exit ping-pong mod 24, claiming 11 if t even and
  23 if t odd): **systematic error found**. When t is even, it matches
  100% (24,815/24,815). When t is odd, the real value is **always 11**
  (25,185/25,185), never 23 as the paper claims.

## Diagnosis

Corollary 2.2's proof claims the transformation t↦(3t+1)/2 "preserves
the parity of t" when t is odd — this is false in general (e.g. t=1→
t'=2, even; t=5→t'=8, even; t''s parity depends on t mod4, not on t's
parity). The correct value appears to simply be S^ℓ(n)≡11 (mod24)
always, regardless of t's parity.

## Assessment

Unlike item 004 (H-040), this is a **small, contained** error:
Corollary 2.2 doesn't even appear in the paper's own "What is proved"
list in the conclusion (only the mod-8 taxonomy, Prop 3.1's
decomposition, Theorem 3.6, the mod-24 universe, and graph foundations
are listed there) — suggesting the author already treats it as more
preliminary/secondary material. Conjecture 5.1 (the regex
characterization, the paper's central result) is honestly presented as
a conjecture, not a proof — given we already verified the equivalent
transition matrix (Theorem 2.1 of paper #004), this conjecture seems
well-founded and likely follows almost directly from the
already-confirmed structure, though we haven't formally proven it
ourselves.

## Reproduce

`python3 experiment.py` (~0.15s)

## Status

Review complete: two central results confirmed correct, one small,
systematic error found in a secondary corollary, central conjecture
honestly treated as a conjecture by the author himself.
