# E-090 — Syracuse measure μ in ℤ₃ vs. residual density G(v)

Related hypothesis: [`H-090-syracuse-measure-explains-density-residual.md`](../../hypotheses/H-090-syracuse-measure-explains-density-residual.md)

## What was done

The Fable proposed (and helped validate the mathematical setup before
implementing) that G(v)=D(v)·v — D(v)'s 3-adic residual after removing
the trivial magnitude term (H-086) — is well approximated by the local
density of a measure μ on ℤ₃, defined by the same recursion as Tao's
(2022) Lemma 1.12 for the variable Syrac(ℤ/3ⁿℤ), already implemented
and verified in this project in E-076.

We reused that implementation, wrote a floating-point-truncated version
to scale to larger m (validated against the exact version, error ~0),
and compared 3^m·μ_m(r) against the geometric mean of G(v) measured
computationally for v's with residue r mod 3^m, controlled magnitude.

## Result

Strong log-log correlation, growing with m: 0.916 (m=2) → 0.969 (m=3)
→ 0.980 (m=4), stable across 5 independent seeds (0.947-0.988 for m=3,
0.968-0.981 for m=4). The Fable's conjecture is confirmed with real
evidence. See H-090 for the full analysis.

## Reproduce

```
python3 experiment.py
```

## Three-arm control experiment (H-111, 2026-07-17)

Quantitatively calibrates H-110's endogeny barrier: arm 1
(`experiment_synthetic_core.py`) simulates the tree under the null
hypothesis of fresh, independent 3-adic digits between subtrees; arm 2
(same file, `rho` parameter) adds adjustable content coupling between
sibling subtrees; arm 3 (`experiment_control_arms.py`, reuses
`measure_G_headroom`) re-measures the real arithmetic tree at the same
`mult` as the synthetic arms. `experiment_synthetic_dp_oracle.py` is an
exact dynamic-programming oracle to validate the simulator's
criticality (E[G|type]) without Monte Carlo.

Result: no positive arithmetic coupling detected between arm 1 and arm
3; bound ρ_eff≲0.06 (95% CI, m=20). See H-111 for the complete
documentation, including a self-correction by the Fable in the
theoretical criticality derivation (found by the validation checklist,
not an implementation bug).

```
python3 experiment_synthetic_core.py          # validation checklist
python3 experiment_control_arms.py braco1     # arm 1, full grid (literal CLI arg, do not translate)
python3 experiment_control_arms.py braco3     # arm 3, re-measured (literal CLI arg, do not translate)
python3 experiment_control_arms.py slope      # slope + excess bootstrap (final result)
```
