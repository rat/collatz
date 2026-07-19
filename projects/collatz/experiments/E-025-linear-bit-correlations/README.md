# E-025 — Search for linear invariants between bits of n and bits of m

Related hypothesis: [`H-025-linear-bit-correlations.md`](../../hypotheses/H-025-linear-bit-correlations.md)

Origin: item #9 from a fourth list of external ideas — search for
linear invariants (GF(2)/Z) in binary representations.

## What was tested

Linear-cryptanalysis-style correlation (bias) between `bit_i(n)` and
`bit_j(m)`, where m is the accelerated orbit's next odd number, for
every pair within a bit window, without conditioning on the value of a
(which varies per sample).

## Dependencies

Requires `numpy` (not installed in the system environment; installed
in the venv `/home/rat/.venv` during this session). Run with:
`/home/rat/.venv/bin/python3 experiment.py [N_SAMPLES] [WINDOW] [BIT_LENGTH]`

## Result

An apparent signal (~0.02, highly significant, z>28) at a fixed offset
(bit_i(n) vs bit_{i-4}(m)) that seemed not to decay with i — a
candidate for a genuine invariant. Diagnosis: conditioning on each
fixed value of a separately, the signal only appears when a=4
(bias~0.33), and its probability-weighted contribution (1/16)
reproduces exactly the aggregate value (0.0625×0.33≈0.0206). Mechanism:
when a=k, m=(3n+1)/2^k exactly — a trivial algebraic shift, and the
residual correlation is just the classic carry-propagation bias in
binary addition (3n+1=2n+n), short-range (confirmed null beyond i=1
when a=1 is fixed).

## Conclusion

No new linear invariant found. Every observed correlation is explained
by (1) the exact value of a (already known) and (2) the classic
binary-addition carry bias, with no new information about Collatz
structure. A clean negative result, with the mechanism identified.
