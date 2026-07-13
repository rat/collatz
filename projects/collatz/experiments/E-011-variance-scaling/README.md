# E-011 — A variância de H-010 é ruído previsto, não estrutura escondida

Hipótese relacionada: [`H-011-variance-scaling.md`](../../hypotheses/H-011-variance-scaling.md)

## O que foi testado

H-010 achou R²=0.03 (log₂n explica pouco da variância individual de
total_stopping_time). Derivamos a previsão teórica de que
Var(total_stopping_time(n)) ≈ 186.93·log₂(n) — crescimento **linear** em
log₂(n), não quadrático — usando a aproximação de tempo de primeira passagem
de um passeio aleatório com deriva (distribuição Gaussiana Inversa),
combinando Var(a)=2 (H-001) com a relação exata entre passos-padrão e
deriva-log₂ por passo acelerado.

## Resultado

Amostramos ~5.000 números por "nível" de magnitude (log₂n ≈ 10.5, 15.5, ...,
45.5 — de 2^10 a 2^46, usando inteiros grandes nativos do Python) e medimos a
variância empírica de total_stopping_time dentro de cada nível:

| log₂(n) | média | variância | var/log₂n |
|---|---|---|---|
| 10.5 | 82.4 | 1969 | 187.5 |
| 15.5 | 115.6 | 2685 | 173.2 |
| 20.5 | 152.5 | 3557 | 173.5 |
| 25.5 | 188.9 | 4765 | 186.9 |
| 30.5 | 223.1 | 5345 | 175.2 |
| 35.5 | 261.5 | 6705 | 188.9 |
| 40.5 | 297.6 | 7208 | 178.0 |
| 45.5 | 333.6 | 8341 | 183.3 |

Regressão (variância ~ coef·log₂n, sem intercepto): **coeficiente empírico =
181.53** vs. **teórico = 186.93** — diferença de apenas **2.9%**.

Reproduzir: `python3 experiment.py 5000 7`

## Conclusão

A variância cresce **linearmente** em log₂(n) (não quadraticamente), com o
coeficiente previsto pela teoria batendo dentro de 3% dos dados. Isso
resolve a pergunta em aberto de H-010: **o R² baixo não é evidência de
estrutura escondida** — é exatamente o comportamento que a heurística de
passeio aleatório prevê. Como a média cresce linear em log₂n mas o desvio
padrão cresce só como √(log₂n), a razão sinal-ruído (desvio/média) diminui
lentamente conforme n cresce — mas para as magnitudes testadas (log₂n ~
10-45), ainda é grande o suficiente (~35-45% da média) para produzir um R²
pequeno numa regressão simples, sem que isso implique nada de novo escondido.

## Status de H-011

**Confirmada** (coeficiente empírico dentro de 2.9% do teórico, em 8 ordens
de magnitude diferentes de n).
