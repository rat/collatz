# E-082 — Revisão de Kayadibi, "Exact and Delayed Descent in Accelerated Odd Collatz Spines" (2026)

Hipótese relacionada: [`H-082-kayadibi-2025-review.md`](../../hypotheses/H-082-kayadibi-2025-review.md)

## O que foi feito

Não é alegação de prova (o próprio texto diz explicitamente que não
prova a conjectura). Verificamos as quatro identidades algébricas
centrais sobre "spines de resistência modular" S_m={n≡−1 mod 2^m}: a
identidade de persistência, a fórmula de saída, o limiar de valuação
que certifica descenso exato, e o lema de valuação de deslocamento para
o complemento não-certificado.

## Resultado

Todas as quatro identidades confirmadas sem exceção (3016+377+184+244
casos). Estatísticas empíricas do paper (excesso de descenso médio/
mediano/máximo) reproduzidas em escala menor, consistentes
qualitativamente. Ver H-082 para o veredito completo.

## Reproduzir

```
python3 experiment.py
```
