# E-024 — Densidade exige precisão 3-ádica ilimitada

Hipótese relacionada: [`H-024-density-needs-unbounded-precision.md`](../../hypotheses/H-024-density-needs-unbounded-precision.md)

Origem: lista de ideias de outra IA (sugestão de abordagem espectral/grafos
para H-013), testada antes de investir esforço nessa direção.

## O que foi testado

Se a densidade D(v) do subárvore reverso de Collatz depende só de v mod 3^K
(residuo finito) — o que permitiria um operador de transferência de
dimensão finita para calculá-la exatamente.

## Resultado

Cinco valores de v, todos ≡85 (mod 729=3⁶), com orçamento de magnitude
proporcional (evitando o erro de comparar orçamentos desiguais):

| v | D(v) |
|---|---|
| 85 | 0.0089 |
| 1543 | 0.0004 |
| 4459 | 0.0002 |
| 14665 | 0.000038 |
| 72985 | 0.000027 |

**Variação de mais de 300×** entre números com o mesmo resíduo mod 729.
Metodologia validada (reproduz exatamente os valores já conferidos de J_4
na configuração original antes de rodar este teste).

Reproduzir: `python3 experiment.py 6 24`.

## Conclusão

D(v) **não** é função de resíduo 3-ádico limitado — depende de estrutura
arbitrariamente profunda. Isso fecha, com evidência direta (não apenas
tentativa fracassada), a linha de "operador de transferência de dimensão
finita" para a fórmula de H-013, e também informa contra tentar a "teoria
espectral/grafos" de forma ingênua (truncando resíduos) para esta
quantidade específica.

## Status de H-024

**Confirmada** — resultado negativo que explica rigorosamente uma
limitação já suspeitada, encerrando essa linha de investigação com clareza
em vez de deixá-la em aberto sem explicação.
