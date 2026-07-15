# E-075 — Revisão de Barina, "Convergence verification of the Collatz problem" (2020/2021)

Hipótese relacionada: [`H-075-barina-2020-verification-review.md`](../../hypotheses/H-075-barina-2020-verification-review.md)

## O que foi feito

Verificamos o algoritmo central do paper (item 105) — uma técnica para
evitar a etapa aditiva "+1" trocando entre os domínios n e n+1, usando
só operações multiplicativas. Reimplementamos literalmente as
identidades (Eqs. 4-6) e os dois algoritmos de convergência
(Algorithm 1: glide; Algorithm 2: delay).

## Resultado

Confirmado sem exceção: identidades Eq.4/Eq.5 (200.000 casos), Algorithm
1 convergindo corretamente (999 casos), Algorithm 2 batendo exatamente
com a contagem padrão de delay (5 sementes), fórmula geral Eq.6 (1000
casos aleatórios), e a afirmação textual sobre a média de 4 iterados por
passo do algoritmo (confirmado empiricamente, 4,009 vs 4,0 previsto).
Ver H-075 para o veredito completo.

## Reproduzir

```
python3 experiment.py
```
