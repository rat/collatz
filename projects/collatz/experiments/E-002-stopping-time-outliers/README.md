# E-002 — Residual structure in stopping-time outliers

Related hypothesis: [`H-002-stopping-time-outliers.md`](../../hypotheses/H-002-stopping-time-outliers.md)

## What was tested

Numbers with abnormally high stopping time for their size ("outliers"
— the top 0.5% by `total_steps(n) / log2(n)` over an interval) were
compared against a typical sample from the same interval on: (a)
residue mod powers of 2 (4 to 64), (b) residue mod powers of 3 (3 to
27), (c) length of the initial run of steps with valuation a_i=1
("run1").

`total_steps` = number of steps of the standard map (n/2 if even, 3n+1
if odd) until reaching 1, computed cheaply from the accelerated orbit.

## Results (n up to 2,000,000, top 0.5% = ~5,000 outliers, tested with 2 seeds)

- **Residue mod 4/8/16/32/64**: huge and extremely significant
  difference (p < 10^-40) between outliers and the typical group.
- **Residue mod 3/9/27**: no significant difference in any tested
  configuration (p always > 0.05, even without correction for multiple
  testing).
- **Initial run of a_i=1**: outliers average ~1.95 initial steps with
  a=1, versus ~1.0 in the typical group — almost double.

## Interpretation — why the mod-2^k signal is NOT a new finding

The residue of n modulo 2^k determines (essentially deterministically)
the first values of the valuation sequence a_1, a_2, ... until their
sum exceeds k — and vice versa. Since an outlier is, by definition, a
number whose initial descent is slow (small valuations over several
consecutive steps), it **necessarily** falls into specific residue
classes mod 2^k. In other words: the mod-2^k residue test is
essentially testing the same thing the outlier definition already
guarantees — it's a tautology encoded another way, not newly
discovered structure.

To verify this, we ran a control: conditioning both groups on the
**same** initial run length (`run1` fixed at 1 or 2), removing the most
obvious explanation. Even so, mod 16/32/64 remained strongly
significant (p < 10^-13) — showing that the tautology isn't limited to
"run1": residue mod 2^k carries information about the *exact* values
of a_2, a_3, ... (not just whether they're 1 or not), and that
information stays mechanically tied to stopping time. That is, the
mod-2^k signal is real, but it is **already-known, expected structure**
(the very definition of stopping time via valuations), not a discovery.

## Genuine result: absence of mod-3^k structure

The residue test mod 3/9/27 **does not have** this deterministic
relationship with the valuation sequence (the "3" in 3n+1 enters
differently from the "2"). The absence of any signal here — including
after conditioning on run1 — is a genuine negative result:
stopping-time outliers don't seem to have any residual signature
modulo powers of 3, in the tested range and scale.

## Status of H-002

**Supported only in the tautological part** (mod-2^k structure,
already expected from the very definition of stopping time) and
**refuted in the more interesting part** (no mod-3^k structure
detected). No evidence of a "new" structural signature in outliers
beyond what the valuation definition already implies.

Possible next extension (not a current priority): test subtler
structures not reducible to residue mod 2^k — e.g., features based on
the full valuation sequence normalized by length, or comparison
against the real record-holders catalogued in the literature
(Roosendaal) instead of outliers defined locally within our sample.
