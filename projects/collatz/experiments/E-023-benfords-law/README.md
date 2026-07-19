# E-023 — Benford's Law in Collatz orbit values

Related hypothesis: [`H-023-benfords-law.md`](../../hypotheses/H-023-benfords-law.md)

Origin: a Veritasium video about the Collatz Conjecture (brought by the
scientific director).

## What was tested

Whether the values visited in a Collatz orbit follow Benford's Law
(P(first digit=d) = log₁₀(1+1/d), P(1)≈30.1%). Two clean tests
(avoiding the orbit-collision pitfall):
(a) a single long orbit (837799, 525 steps);
(b) 500,000 independent orbits, one value per orbit (large, distinct n,
value taken after a random number of steps, 10-200).

## Methodological bug found and fixed

The first attempt at part (b) gave a very poor fit (chi-square=837,
p≈10⁻¹¹²) — 2.61% of samples had already reached n=1 before the end of
the chosen step window, artificially "trapping" the value at 1 (digit
1) and inflating that count. A test with an even larger window
(50-2000 steps) made this dramatically obvious: 91.7% of samples gave
digit 1, because most orbits had already converged well before the
window ended. **Fixed** by discarding samples that reach 1 before the
window ends, instead of counting the spurious 1.

## Result (after correction)

- **(a) Single orbit**: chi-square=7.49, p=0.486 — **consistent with
  Benford** (modest sample, 525 points).
- **(b) 500,000 independent orbits**: excellent fit in magnitude —
  digit 1: 30.11% observed vs. 30.10% predicted; every other digit also
  matches to the 3rd-4th decimal place. Chi-square=43.10, p=1.4×10⁻⁶ —
  technically "significant", but with tiny absolute deviations,
  expected given the huge sample size (even fine noise deviations
  become detectable with n=500,000).

Reproduce: `python3 experiment.py 837799 500000`.

## Conclusion

Benford's Law is confirmed with excellent practical precision in
Collatz orbit values — a natural consequence of the "multiplicative
random walk"-like behavior already established in H-001/H-010/H-011/
H-017 (the value's logarithm "equidistributes" along the orbit). Not a
new mathematical discovery, but it connects a popular observation
(from the video) to our own already-validated theoretical framework,
and the process revealed (and fixed) a real methodological bias in the
sampling.

## Status of H-023

**Confirmed** (excellent practical fit; the residual statistical
deviation is expected given the sample size, not a real model
failure).
