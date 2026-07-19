# E-096 — Refutação da alegação de prova de Roif (2026), item 050

Hipótese relacionada: [`H-096-roif-2026-review.md`](../../hypotheses/H-096-roif-2026-review.md)

## O que foi feito

O paper fecha o "gap ergódico" (o conjunto excepcional de densidade
zero do Teorema de Tao 2022) afirmando que "densidade zero implica
conjunto vazio" (Lemma 4.3). Este experimento demonstra numericamente
que isso é falso via dois contraexemplos clássicos e elementares:
quadrados perfeitos e potências de 2 — ambos infinitos, ambos com
densidade tendendo a zero.

## Resultado

Densidade dos quadrados perfeitos cai de 10⁻¹ (N=10²) a 10⁻⁶ (N=10¹²);
densidade das potências de 2 cai a 4×10⁻¹¹ (N=10¹²) — em ambos os
casos o conjunto é obviamente infinito. Refuta diretamente a Lemma 4.3
do paper, que é o único mecanismo usado para fechar o conjunto
excepcional de Tao e completar a "prova".

## Reproduzir

```
python3 experiment.py
```
