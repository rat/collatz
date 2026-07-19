# E-093 — Refutação da alegação de prova de Tynski (2026), item 087

Hipótese relacionada: [`H-093-tynski-2026-review.md`](../../hypotheses/H-093-tynski-2026-review.md)

## O que foi feito

O paper alega provar Collatz via um limite de Lyapunov determinístico
(axioma W6): log₂(n_m) ≤ log₂(n₀) − m·δ + C·√m com C≤5 universal,
verificado numericamente só até n₀≤3×10⁴. Este experimento calcula o
menor C que faz o limite valer em toda a trajetória, para amostras
muito além da faixa testada pelo paper, incluindo recordistas de
atraso conhecidos e sementes adversariais.

## Resultado

C_min já excede 5 pouco além de n₀=10⁴, chegando a 8,34 para
recordistas de atraso conhecidos, sem sinal de estabilizar. Refuta
diretamente a alegação numérica central que sustenta o axioma (W6) —
o mesmo padrão de confundir taxa média com garantia determinística já
catalogado em outras alegações de prova deste projeto (H-045, H-065).

## Reproduzir

```
python3 experiment.py
```
