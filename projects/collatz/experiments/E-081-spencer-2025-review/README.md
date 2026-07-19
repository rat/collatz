# E-081 — Review of Spencer, "Finite Block Exhaustion and Rooted Occupancy..." (2025)

Related hypothesis: [`H-081-spencer-2025-review.md`](../../hypotheses/H-081-spencer-2025-review.md)

**FULL-PROOF CLAIM — REFUTED.**

## What was done

Constructs the same reverse tree as H-018/E-018, with a sophisticated
combinatorial apparatus (a ternary counter of residue classes mod
2·3^J). Claims to prove that every primitive residue class is
"occupied" at every finite scale, and concludes (Theorem 15.3) that
every odd integer has a finite reverse address.

## The logical hole

"Residue class occupied" (a statement about residues, abstract
objects) does not imply "a specific integer is reached" — the paper
never connects the two. We confirmed this concretely: we built the real
tree up to depth 6 and 8 and showed that 27's residue class is
occupied, but by representatives far larger (on the order of
10⁶-10⁸), never 27 itself.

## Result

Not a valid proof — the same error anatomy as item 109
(Getachew/H-079), via a different route. See H-081 for the full
analysis.

## Reproduce

```
python3 experiment.py
```
