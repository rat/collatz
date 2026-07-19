# E-028 — Consolidation of the exclusion family via CRT

Related hypothesis: [`H-028-crt-exclusion-family-consolidated.md`](../../hypotheses/H-028-crt-exclusion-family-consolidated.md)

Origin: a suggestion from the advisor — the consolidated family of
exclusion theorems (H-007, H-014, H-022, H-027) is the most realistic
candidate for a "publishable" result from the project so far, more so
than any single hypothesis or the speculative spectral directions.

## What was tested

Combining, via CRT, the four proven exclusion rules (mod3, mod6, mod8,
mod9) into a single characterization mod 72, and validating it against
the 148 known real record holders (OEIS A006877).

## Result

45 of 72 residues mod 72 (62.5%) are likely excluded. Zero violations
against the 148 real record holders. 18 of the 27 allowed residues
actually appear in the sample.

Reproduce: `python3 experiment.py` (uses E-004's data file).

## Status of H-028

**Confirmed** — an arithmetic consolidation (CRT is elementary), no new
mathematics beyond the combination, but a clean result validated 100%
against real data.
