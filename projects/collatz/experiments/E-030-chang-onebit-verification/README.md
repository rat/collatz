# E-030 — Independent verification of Chang's paper (2026)

Related hypothesis: [`H-030-chang-onebit-mixing-verification.md`](../../hypotheses/H-030-chang-onebit-mixing-verification.md)

Paper: [Edward Y. Chang, "A Structural Reduction of the Collatz
Conjecture to One-Bit Orbit Mixing"](https://arxiv.org/abs/2603.25753)
(2026).

## What was tested

Independent computational verification of three central results from
the paper (Lemma 4.1, Theorem 4.2 "Map Balance", the bit-4 mechanism),
followed by two extensions: orbits larger than those tested in the
paper, and the set of 148 real stopping-time record holders (data
already used in E-004).

## Our own bugs found and fixed

Two bugs in the verification (not in the paper): (1) I forgot to
restrict the bit-4 test to the condition k=(n−1)/8 odd; (2) I applied
Lemma 4.1's mod-8 test to the wrong value (n instead of T(n)). Both
fixed before reporting any result — the final version gives zero
failures.

## Result

All three results verified without exception (Lemma 4.1: 50k cases;
Map Balance: K=5..15 exact; bit-4: 12.5k cases). The extension with the
148 real record holders showed a deviation of ~0.61 (vs. 0.5 expected)
over 9064 observations — but this is **pseudo-replication** (record
holders' orbits collide with each other, directly confirmed: 8/45
pairs among the top 10 record holders share tail values within a
500-step window) and, even discounting that, the deviation matches
exactly what the paper's own Table 2 already shows for large generic
orbits (individual orbit deviations of ±10-25%) — not a new finding
nor counter-evidence.

Reproduce: `python3 experiment.py`.

## Status of H-030

**Confirmed** (successful verification of the external paper) with an
honest extension that did not overclaim an apparently large but
methodologically confounded deviation.
