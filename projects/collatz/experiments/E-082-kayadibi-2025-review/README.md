# E-082 — Review of Kayadibi, "Exact and Delayed Descent in Accelerated Odd Collatz Spines" (2026)

Related hypothesis: [`H-082-kayadibi-2025-review.md`](../../hypotheses/H-082-kayadibi-2025-review.md)

## What was done

Not a proof claim (the text itself explicitly says it does not prove
the conjecture). We verified the four central algebraic identities
about "modular resistance spines" S_m={n≡−1 mod 2^m}: the persistence
identity, the exit formula, the valuation threshold certifying exact
descent, and the shift-valuation lemma for the uncertified complement.

## Result

All four identities confirmed without exception (3016+377+184+244
cases). The paper's empirical statistics (mean/median/max descent
excess) reproduced at a smaller scale, qualitatively consistent. See
H-082 for the full verdict.

## Reproduce

```
python3 experiment.py
```
