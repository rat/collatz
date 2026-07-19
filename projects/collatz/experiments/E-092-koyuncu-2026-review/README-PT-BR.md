# E-092 — Verificação de Koyuncu et al. (2026), item 071

Hipótese relacionada: [`H-092-koyuncu-2026-review.md`](../../hypotheses/H-092-koyuncu-2026-review.md)

## O que foi feito

Verificação do Lemma 1 (fórmula exata de n a partir do código de
paridade) contra trajetórias reais de Collatz via aritmética `Fraction`
exata, e reprodução do experimento central do paper (regressão
log(média)~k para cada comprimento L=10..30, n≤100.000).

## Resultado

Lemma 1 bate exatamente em todos os casos testados. Tabela 1 do paper
reproduzida quase byte-a-byte (slopes idênticos até a 4ª casa decimal
para L=10,11,12). Nenhum erro encontrado. Ver H-092 para a análise
completa, incluindo uma nuance não discutida pelo paper (slope
observado ~2% mais negativo que o valor "ingênuo" −log 6).

## Reproduzir

```
python3 experiment.py
```
