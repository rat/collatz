# E-077 — Revisão de Clay, "The Long Search for Collatz Counterexamples" (2023)

Hipótese relacionada: [`H-077-clay-2023-review.md`](../../hypotheses/H-077-clay-2023-review.md)

## O que foi feito

Paper expositivo (não alega prova) sobre exclusão de classes residuais
mod 2^k. Verificamos três fórmulas algébricas explícitas das notas de
rodapé (comprimento de sequência para classes 2k, 4k+1, 16k+3) e a
alegação de que restam 7,4% de altitudes "não domadas" após excluir as
classes citadas mod 32/128/256.

## Resultado

Tudo confirmado exatamente. Uma primeira tentativa de verificar os 7,4%
deu 4,30% — erro próprio (confundi classes mod16 de um estágio do
refinamento com classes mod32 de outro estágio, listadas em partes
diferentes do texto). Corrigido, o cálculo bate exatamente: 19/256 ≈
7,42%. Ver H-077 para o veredito completo.

## Reproduzir

```
python3 experiment.py
```
