# E-080 — Revisão de Barina, "Improved verification limit..." (2025)

Hipótese relacionada: [`H-080-barina-2025-verification-review.md`](../../hypotheses/H-080-barina-2025-verification-review.md)

## O que foi feito

Continuação direta do paper de 2020 do mesmo autor (item 105, já
verificado em E-075 — equações centrais idênticas). Esta revisão foca
no que é novo: o mecanismo do sieve 3^k. Simulamos diretamente (busca
exaustiva, não só reprodução de números) para confirmar que 100% dos
números ≡2 (mod 3) são elimináveis pelo sieve 3¹, e 0% dos outros
resíduos — bate exatamente com o percentual citado (33,33%).

## Resultado

Nenhum erro encontrado. Timeline de verificação e ordem dos 5 novos
path records também confirmados. Ver H-080 para o veredito completo.

## Reproduzir

```
python3 experiment.py
```
