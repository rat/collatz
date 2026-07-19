# E-089 — Corrected retest of H-026 (does larger K help predict G(v)?)

Related hypothesis: [`H-089-h026-corrected-K-does-help.md`](../../hypotheses/H-089-h026-corrected-K-does-help.md)

## What was done

The original H-026 concluded that fixing more base-3 digits (larger K)
does not reduce the divergence of the finite-memory approximation. The
Fable model showed by direct arithmetic that this conclusion was
contaminated by the same trivial magnitude term D(v)≈C/v identified in
H-086 — H-026 never tested the right variable (G(v)=D(v)·v). We
reimplemented the test measuring the **spread** of log₁₀(G) within
fixed, controlled magnitude windows, with multiple independent residue
chains.

## Bug found and fixed along the way

A first attempt used magnitude windows too narrow for large K — the
mod 3^K spacing exceeded the window width, forcing the sampling to
repeat the same v (spurious zero variance). Fixed by checking that the
window contains enough distinct values before sampling, and using
wider windows.

## Result

The spread of log₁₀(G) drops monotonically with K: 0.2352 (K=2) →
0.1748 (K=4) → 0.1444 (K=6) → 0.0936 (K=8) — consistent across the 3
tested magnitude windows. **Larger K reduces the uncertainty about
G(v)** — the opposite of H-026's original conclusion. See H-089 for the
full analysis.

## Reproduce

```
python3 experiment.py
```
