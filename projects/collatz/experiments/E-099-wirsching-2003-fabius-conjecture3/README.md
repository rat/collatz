# E-099 — Certified test of Wirsching's (2003) Conjecture 3 via exact moments of φ

Related hypothesis: [`H-125-wirsching-2003-functional-equation-fabius-atomic-function.md`](../../hypotheses/H-125-wirsching-2003-functional-equation-fabius-atomic-function.md)

## What was done

A numerical test with CERTIFIED (not heuristic) error of Wirsching's
(2003) Conjecture 3 — the most concrete piece of a chain of 3
conjectures reducing to positive density of 3n+1 predecessors. The
central object, φ (the invariant density of the W₃ averaging operator,
which turns out to be the base-3 analogue of Rvachev's Fabius
function/"atomic function"), has EXACT RATIONAL moments via
self-similarity (X=d(2U+X)/3) — allowing φ to be evaluated at
extreme-tail points (x~ℓ·3⁻ℓ) without iterating the W₃ operator and
without loss of precision, via a reduction using iterated
antiderivatives.

## Result

Run up to ℓ=500 (CLT window, u∈[−2,2]): the decisive ratio
L_ℓ=3^(1−ℓ)φ(3x_ℓ)/φ(x_ℓ) converges to the predicted value 2/3 with a
deficit of (0.580±0.001)/ℓ — a coefficient independently reproduced by
Berg-Krüppel's (1998) own φ₀ asymptotics. ln(φ/φ₀) converges to a
finite limit L=−0.619±0.001(statistical)±0.015(functional form), i.e.
c=e^L≈0.54 (honest interval 0.53-0.55). Strong uniformity across the
CLT window (dispersion <10⁻⁴ at ℓ=500, versus an individual variation
of ~100 units in ln φ). No visible log-periodic modulation.
**Conjecture 3 numerically SUPPORTED** — but it's the most concrete tip
of a chain of 3 conjectures; Conjectures 1 and 2 (above it) remain open
and are untouched by this test. See H-125 for the full analysis.

## Files

- `experiment_conjecture3.py` — main script: exact moments, reduction
  by antiderivatives, φ₀ via Berg-Krüppel asymptotics (symbolic
  constants α,β,γ,δ,ε), validation (φ(1/2)=3/2 exact, odd central
  moments=0), sweep up to ℓ=300.
- Extension to ℓ∈{350,400,450,500} (6+ decimals, out-of-sample test
  against the tail models fit at ℓ≤300) run inline, not persisted as a
  separate script — see H-125 for the numbers.

## Reproduce

```
python3 experiment_conjecture3.py
```

Cost: moments(310)~18s, moments(510)~5min (grows ~N^4-5). Don't raise
N_MAX without need — ℓ~1000+ would require tens of minutes to hours.
