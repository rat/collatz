# E-033 — Extending Chang's (2026) open problem with longer orbits

Related hypothesis: [`H-033-chang-bit4-longorbit-extension.md`](../../hypotheses/H-033-chang-bit4-longorbit-extension.md)

## What was tested

Chang's paper (H-030) leaves open: does every orbit visit 9 and 25 (mod
32) with sufficient balance along the end-of-burst in the ≡1 mod8
channel? He tested up to n0=10⁹ with a few dozen observations per
orbit. Here we track the balance individually along the 8 largest real
record holders (878-920 steps, 131-134 observations each — 3× more
than the original paper's best case).

## Result

The deviation persists (0.54-0.64, not 0.5), with no sign of
convergence even with more data. Consistent with H-021/H-030 (record
holders have longer ascent runs by selection) and with Chang's own
acknowledgment that individual orbits deviate ±10-25%. Does not resolve
nor contradict his open problem — the exact δ_max was not derived here.

Reproduce: `python3 experiment.py`.

## Status of H-033

**Confirmed** as an honest empirical extension — new data at larger
scale, without overclaiming about the original open problem.
