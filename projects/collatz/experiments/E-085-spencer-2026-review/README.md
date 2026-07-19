# E-085 — Review of Spencer, "Rooted Surjectivity from the Invariant E/O Refinement System" (2026)

Related hypothesis: [`H-085-spencer-2026-review.md`](../../hypotheses/H-085-spencer-2026-review.md)

**FULL-PROOF CLAIM — differentiated verdict (not computationally confirmed, not refuted).**

## What was done

Same author as item 022 (already refuted with a counterexample in
H-081) — our initial suspicion was the same error anatomy ("residue
class occupied" ≠ "specific integer reached"). We built the real
reverse tree starting from n=1 (infinite degree: multiple admissible k
per node, unlike item 022's degree-≤2 tree) and tested coverage of
small odd integers with growing computational budget.

## What we found (different from the initial suspicion)

Complete coverage up to 10,000 with adequate budget; the "missing"
ones in smaller-budget rounds **converge exactly to the root** when
followed with no magnitude limit (individually confirmed for several
values) — this is the opposite of the behavior seen in item 022, where
the gap persisted and grew regardless of budget.

**But** we identified a genuine rigor gap in the written proof: Theorem
14.1 argues about the occupancy of residue *classes*, and Theorem 14.2
concludes something stronger about *individual elements* — this
transition isn't explicitly justified in the text.

## Result

Honest verdict: the proof as written has a real logical gap (it isn't a
valid proof as it stands), but the available computational evidence is
consistent with the paper's conclusion, unlike the same author's item
022. See H-085 for the full analysis, including the self-correction of
our initial precedent-based suspicion.

## Reproduce

```
python3 experiment.py
```
