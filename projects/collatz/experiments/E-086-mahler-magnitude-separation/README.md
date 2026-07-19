# E-086 — Magnitude/residue separation in D(v), testing Fable's critique of H-024

Related hypothesis: [`H-086-density-magnitude-factorization.md`](../../hypotheses/H-086-density-magnitude-factorization.md)

## What was done

The Fable model, consulted for creative ideas about H-013/H-018/
H-024, pointed out that H-024's experimental design (fixing the residue
mod 3⁶, letting magnitude vary freely by ~860×) doesn't separate the
magnitude effect from the residue effect. We tested this directly: we
measured D(v) for many v with the same residue mod 729, varying
magnitude freely, and ran the log-log regression.

## Result

D(v) ≈ C/v almost exactly (log-log regression slope = −0.9971,
R²=0.9991). Removing this term, the "unexplained" variance drops from
~300× (original H-024) to ~1.26× — more than two orders of magnitude of
reduction. H-024's formal conclusion remains correct (no finite K
explains D(v) alone), but the magnitude of the remaining phenomenon is
much more modest than it appeared. See H-086 for the full analysis.

## Reproduce

```
python3 experiment.py
```

Or, to reproduce the specific regression cited in H-086, see the inline
code used in the investigation (measure D(v) for v with fixed residue
mod 729 and log-uniform magnitude between 10² and 10⁷, then regress
log10(D) against log10(v)).
