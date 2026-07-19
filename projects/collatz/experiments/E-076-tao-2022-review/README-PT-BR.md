# E-076 — Revisão de Tao, "Almost all orbits of the Collatz map attain almost bounded values" (2022)

Hipótese relacionada: [`H-076-tao-2022-review.md`](../../hypotheses/H-076-tao-2022-review.md)

## O que foi feito

Não uma "caça a erros" (paper de Terence Tao, revisado por pares num
periódico de primeira linha) — verificação disciplinada dos exemplos
numéricos e identidades explícitas concretas que o texto apresenta:
exemplos do mapa de Siracusa, a identidade Col_min(N)=Syr_min(N/2^v2(N)),
e a distribuição exata de Syrac(ℤ/3ℤ) e Syrac(ℤ/9ℤ) via reimplementação
independente da fórmula recursiva do Lemma 1.12.

## Resultado

Tudo confirmado sem exceção, incluindo reprodução exata (aritmética de
frações, não ponto flutuante) de 12 valores de probabilidade racionais
não-triviais (ex: 8/63, 22/63) que o texto apresenta como resultado da
fórmula recursiva. Ver H-076 para o veredito completo.

## Reproduzir

```
python3 experiment.py
```
