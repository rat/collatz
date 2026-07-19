# E-007 — Proof of why record holders avoid residue 2 mod 3

Related hypothesis: [`H-007-why-record-holders-avoid-2-mod-3.md`](../../hypotheses/H-007-why-record-holders-avoid-2-mod-3.md)

## What was verified

H-007's theorem: for every N ≡ 2 (mod 3) with N > 2, M = (2N−1)/3 is an
odd integer smaller than N whose orbit passes through N exactly 2
steps later (M → 2N → N), so total_stopping_time(M) =
total_stopping_time(N) + 2. This algebraically proves that N can never
be a record holder — M always beats it.

## Technical note — bug found and fixed during verification

The first verification attempt used the `total_steps_only` function
from E-004/E-006, which **implicitly assumes the input is always
odd** (it always held in that context because every previous scan only
iterated over odd numbers — `range(1, limit, 2)`). When testing the
theorem directly with even values of N (e.g. N=8, 14, 20, 26), the
function broke silently (it applied "3n+1" to an even number,
producing a completely wrong orbit — e.g. `total_steps_only(2)`
returned 17 instead of the correct 1). **This does not affect any
earlier result** (E-001 through E-006 never called these functions
with even input), but it is a real pitfall: an "accelerated" function
that assumes the input's parity silently gives a wrong result if used
outside the context it was written for. Fixed by using a generic
`total_stopping_time` function (standard map, no parity assumption)
just for this verification.

## Result

Verified without exception for every N ≡ 2 (mod 3) from 2 to
1,000,000 (333,332 cases, including even and odd N) — stopping-time
difference exactly 2 in 100% of cases, the only exception being the
predicted edge case (N=2, where M would collapse to 1).

Reproduce: `python3 experiment.py 1000000`

## Conclusion

**H-004 is now fully explained, not just statistically confirmed.**
It's not a mysterious correlation — it's a direct, simple algebraic
consequence of the Collatz map's structure. Closes the project's main
open finding so far.

## Status of H-007

**Confirmed** — short algebraic proof + exhaustive computational
verification with no exceptions (outside the predicted edge case).
