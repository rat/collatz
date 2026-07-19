# E-070 — Verification of paper #099 (Lodders, "Selection Rules and Channel Structure in a Base-Octave Model of Collatz Dynamics") — PROOF CLAIM

Related hypothesis: [`H-070-lodders-base-octave-review.md`](../../hypotheses/H-070-lodders-base-octave-review.md)

## Paper

Lodders, K. (2026). *Selection Rules and Channel Structure in a
Base–Octave Model of Collatz Dynamics*. arXiv:2604.20181, 60 pages
(not peer-reviewed). Local PDF:
`literature/papers/099_Selection-Rules-Channel-Structure-Base-Octave.pdf`
(filename with swapped numbering on download — the content is item
099's; item 098 has no free PDF, see `INDEX.md`).

## Verdict

**NOT a valid proof.** The paper reformulates Collatz in a
"base-octave model" (h=B+8(A-1)), derives 16 transition rules between 8
base classes (Section 5), and identifies class B=7 (with even octave
index A) as the only channel able to sustain persistent growth. Up to
here, correct — verified. The paper then claims (Theorem 9.6.8) that
every Collatz trajectory is confined to the terminal basin {1,2} — a
**full-proof claim** — supported by Corollary 9.6.7 (the octave index
A, at the entry of successive base-7 persistence episodes, must
strictly decrease), which is in turn supported by an exhaustive
enumeration of "22 return paths" in a 128-state system (Appendix A2).

**Corollary 9.6.7 is false.** The paper's own example, cited in the
Introduction (n=27, "requires substantially more steps than
neighboring values"), already violates it: its base-7 persistence
episodes have v2(A_entry) = 2, 1, 3, 1 — the jump from 1 to 3 directly
contradicts "must strictly decrease". At scale (N up to 500,000), 56.7%
of all successive-episode pairs violate the claim — not a rare edge
case.

## What was tested

1. Base-octave encoding and the accelerated map, validated against the
   paper's own example (trajectory of h1=7, page 22) and Table 2.
2. The 16 selection rules (Section 5, Cases 1-4) — 31,992 (B,A) pairs
   tested, 0 failures.
3. Proposition 8.4 (persistence-episode length ≤ v2(A_entry)) —
   515,342 episodes tested, 0 failures.
4. **Corollary 9.6.7** (main result) — falsified with the paper's own
   example (n=27, n=31) and at scale (988,476 episode pairs tested,
   560,682 failures).

## How to reproduce

```
python3 experiment.py
```

No dependencies beyond the stdlib. Runs in under 2 minutes.
