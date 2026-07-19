# E-051 — Verification of paper #009 (Olgac, "Structural Dualism in Integer Architectures")

## Goal

Verify "Technical Note: Structural Dualism in Integer Architectures"
(Enis Olgac, 3 pages). A short note connecting two earlier claims by
the same author (not included in this collection, cited only as
references [3]/[4], both self-published Zenodo preprints): one about
Collatz ("Canonical Triple-Graph") and another claiming to **prove the
entire Goldbach Conjecture** ("The Proof Beyond Goldbach").

## What we did

The only Collatz-specific content in this note (Definition 2.1,
"Localized Stranger Invariant" — reverse-tree branches rooted at
distinct odd numbers don't overlap) is a **tautology**: a direct
consequence of every positive integer having exactly one odd part (via
unique factorization of powers of 2), not a new result. We confirmed
this computationally for 200,000 integers (0 violations, as expected by
construction).

## Result

The rest of the paper (Theorem 2.2 "Lattice Inversion", Theorem 3.3
"Hard Physical Boundary Fact") is entirely about the **Goldbach**
Conjecture — outside this project's scope (Collatz) — and does not
reach sufficient mathematical rigor to be assessed as a proof: it uses
non-rigorous descriptive language ("physical collision",
"topologically trapped", "retaining wall") without precisely defining
the objects involved.

**This is not a Collatz paper with specific verifiable content** — it's
a short note connecting two extraordinary claims by the same author
through a vague analogy, without real mathematical rigor on either end.

See `hypotheses/H-051-olgac-structural-dualism-review.md`.

## How to run

```
/home/rat/.venv/bin/python3 experiment.py
```
