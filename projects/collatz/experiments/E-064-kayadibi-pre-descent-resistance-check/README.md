# E-064 — Verification of paper #038 (Kayadibi, "A Modular Classification of Pre-Descent Resistance in Accelerated Odd Collatz Dynamics")

Related hypothesis: [`H-064-kayadibi-pre-descent-resistance-review.md`](../../hypotheses/H-064-kayadibi-pre-descent-resistance-review.md)

## Paper

Kayadibi, S.Y. (2026). *A Modular Classification of Pre-Descent
Resistance in Accelerated Odd Collatz Dynamics*. SSRN 6918258. Local
PDF:
`literature/papers/038_Modular-Classification-Pre-Descent-Resistance.pdf`.

The simpler predecessor of paper #015 in this collection (same author,
already reviewed as H-058) — referenced as `[11]` in that paper.

## What was tested

A classification framework for "pre-descent resistance" for the
accelerated odd map `T(n)=(3n+1)/2^v2(3n+1)`. Does not claim to prove
Collatz.

1. Lemma 3.3, Proposition 3.4, Lemma 3.6, Proposition 3.8 — 4 algebraic
   results about the "modular resistance spine" `S_m`.
2. Full computational reproduction at `N=10⁷, L=5000` (identical to the
   paper's own largest experiment).
3. The two extreme cases cited by name (largest τ, largest ρ).
4. Statistics modulo 64 (Section 5.4).
5. Tables 2 and 3 (resistance spine, `m=6..15`, 40 values).

## Result

**0 failures across all 8 parts.** An exact, complete reproduction —
the paper's computational component is 100% deterministic (no random
sampling) and cheap enough (~9s for `N=10⁷`) to reproduce in full, not
just by sampling. All ~50 specific numerical claims checked match
exactly.

## How to reproduce

```
python3 experiment.py [N] [L]
```

Optional arguments: `N` (default 10,000,000) and `L`, the accelerated
step limit (default 5000) — use smaller values (e.g. `100000 2000`)
for a quick sanity/performance test before the full run. No
dependencies beyond the stdlib. Runs in ~10s for `N=10⁷`.
