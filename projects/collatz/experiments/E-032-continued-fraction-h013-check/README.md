# E-032 — Continued fractions of log₂(3) vs. the H-013 anomaly

Related hypothesis: [`H-032-continued-fraction-h013-check.md`](../../hypotheses/H-032-continued-fraction-h013-check.md)

## What was tested

Whether the quality of log₂(3)'s rational approximation (measured
classically via continued-fraction convergents, the tool used in
cycle-length bounds — Simons & de Weger) explains the t points where
the H-013/H-018 density anomaly occurs (t=4/5, 7/8 anomaly; 10/11,
13/14 inversion).

## Result

No correlation. Pairs of the same type (two anomalies, or two
inversions) show opposite patterns in the distance of t·log₂(3) to the
nearest integer — if there were a real mechanism, they should agree.

Reproduce: `python3 experiment.py`.

## Status of H-032

**Refuted** — an honest negative result for a well-motivated idea (a
real connection between log₂(3) and H-018's mechanism, but one that
doesn't hold up empirically in this form). Consistent with H-024: the
obstruction is 3-adic (residues), not Archimedean (numerical
closeness) — different precision categories.
