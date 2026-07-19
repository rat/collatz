# E-092 — Verification of Koyuncu et al. (2026), item 071

Related hypothesis: [`H-092-koyuncu-2026-review.md`](../../hypotheses/H-092-koyuncu-2026-review.md)

## What was done

Verification of Lemma 1 (exact formula for n from the parity code)
against real Collatz trajectories via exact `Fraction` arithmetic, and
reproduction of the paper's central experiment (regression
log(mean)~k for each length L=10..30, n≤100,000).

## Result

Lemma 1 matches exactly in every tested case. Table 1 of the paper
reproduced almost byte-for-byte (slopes identical to the 4th decimal
place for L=10,11,12). No error found. See H-092 for the full analysis,
including a nuance not discussed by the paper (observed slope ~2% more
negative than the "naive" value −log 6).

## Reproduce

```
python3 experiment.py
```
