# E-038 — Search for nonlinear structure (MI) beyond H-025

Related hypothesis: [`H-038-nonlinear-mi-embedding-search.md`](../../hypotheses/H-038-nonlinear-mi-embedding-search.md)

## What was tested

Honest generalization of "Project PHI" (an external AI idea, rich
embedding + structure search): is there **nonlinear** dependence
(mutual information, not Pearson-style correlation) between rich
features of n (Hamming weight, residues mod5/7/9/11, bit windows) and
of m=(3n+1)/2^a, conditioning on fixed a, beyond what H-025 (linear
bit-by-bit correlation) already tested and refuted?

## Files

- `experiment.py`: main search — MI between 7 features of n × 6
  features of m (including the second valuation a2), conditioned on
  a∈{1,...,6}, compared against a shuffle null (15 shuffles).
- `control_check.py`: mechanism check — (1) confirms
  `popcount(m)==popcount(3n+1)` exactly; (2) compares the real Collatz
  MI against synthetic control transforms (5n+1, 7n+3, 9n+5, and the
  family 2^k+1 for k=1..6).

## Result

Found a real, very robust dependence (z-score up to ~2448) between the
Hamming weight of n and of m, and between bit windows and the second
valuation a2 — something H-025 (bit-by-bit only) would not have
captured.

**But the control experiment shows this is generic, not
Collatz-specific**: replacing 3n+1 with 5n+1, 7n+3, or 9n+5 (unrelated
to Collatz), the SAME class of dependence appears (nonzero MI, far
above the null). Mechanism: `popcount(m)` is always exactly
`popcount(3n+1)` (dividing by 2^a only removes trailing zeros), and the
dependence between `popcount(n)` and `popcount(3n+1)` is a classic
carry-propagation property of multiplication by an odd number plus
addition — the same mechanism class H-025 already identified, just seen
from a different angle (aggregate statistic instead of bit pairs).

## Reproduce

```
python3 experiment.py [N_SAMPLES]     # main search (~20s for N=400000)
python3 control_check.py              # mechanism check (~3s)
```

## Status of H-038

**Refuted as new structure** — a real finding, but with a mechanism
identified and confirmed as generic to binary arithmetic, not specific
to Collatz. Extends H-025 (different method, same underlying
conclusion), doesn't contradict it.
