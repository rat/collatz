# E-078 — Revisão de Wei Ren, "Reduced Collatz dynamics is periodical..." (2025)

Hipótese relacionada: [`H-078-wei-ren-2025-review.md`](../../hypotheses/H-078-wei-ren-2025-review.md)

## O que foi feito

Verificamos o "Period Theorem" central do paper (item 108): se a
"dinâmica reduzida" d_r(x) (sequência de operações I/O até o primeiro
iterado abaixo de x) existe, então d_r(x+2^L)=d_r(x), onde L é o
comprimento da sequência. Também verificamos a extensão (Corollary
3.24) e a caracterização de forma do apêndice (Form Corollary).

## Resultado

Tudo confirmado sem exceção: exemplos do próprio paper, Period Theorem
(499 casos), Corollary 3.24 (245 casos), Form Corollary (999 casos, nas
duas partes). Confirmamos também que o teorema é condicional (só vale
para x cuja dinâmica reduzida já existe) e não fecha a conjectura — algo
que o próprio autor reconhece explicitamente na conclusão. Ver H-078
para o veredito completo.

## Reproduzir

```
python3 experiment.py
```
