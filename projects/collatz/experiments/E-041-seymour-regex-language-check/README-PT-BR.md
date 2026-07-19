# E-041 — Verificação do paper #005 (Seymour, "A Regular Expression Language for the Collatz Graph")

Hipótese relacionada: [`H-041-seymour-regex-language-review.md`](../../hypotheses/H-041-seymour-regex-language-review.md)

## O que foi testado

Paper explicitamente rotulado "working paper", que separa claramente
resultados **provados** de resultados **conjecturados**. Testamos os
três resultados centrais alegados como provados:

- **Proposição 3.1** (aritmética do circuito Steiner via mapa natural
  C): confirmada em 20.000 casos aleatórios, sem exceção.
- **Teorema 3.6** (comprimento da corrida "7 mod 8" = v₂(n+1)−2):
  confirmado em 50.000 casos aleatórios, sem exceção.
- **Corolário 2.2** (exit ping-pong mod 24, alegando 11 se t par e 23
  se t ímpar): **erro sistemático encontrado**. Quando t é par, bate
  100% (24.815/24.815). Quando t é ímpar, o valor real é **sempre 11**
  (25.185/25.185), nunca 23 como o paper afirma.

## Diagnóstico

A prova do Corolário 2.2 alega que a transformação t↦(3t+1)/2
"preserva a paridade de t" quando t é ímpar — isso é falso em geral
(ex: t=1→t'=2, par; t=5→t'=8, par; a paridade de t' depende de t mod4,
não da paridade de t). O valor correto parece ser simplesmente
S^ℓ(n)≡11 (mod24) sempre, independente da paridade de t.

## Avaliação

Diferente do item 004 (H-040), este é um erro **pequeno e contido**:
o Corolário 2.2 nem aparece na lista "What is proved" da conclusão do
próprio paper (só mod-8 taxonomy, decomposição Prop 3.1, Teorema 3.6,
universo mod-24 e fundamentos de grafos são listados lá) — sugerindo
que o autor já trata isso como material mais preliminar/secundário.
A Conjectura 5.1 (a caracterização via regex, o resultado central do
paper) é honestamente apresentada como conjectura, não como prova —
dado que já verificamos a matriz de transição equivalente (Teorema 2.1
do paper #004), essa conjectura parece bem fundamentada e
provavelmente segue quase diretamente da estrutura já confirmada,
embora não a tenhamos provado formalmente nós mesmos.

## Reproduzir

`python3 experiment.py` (~0,15s)

## Status

Revisão concluída: dois resultados centrais confirmados corretos, um
erro pequeno e sistemático encontrado numa corolário secundário,
conjectura central tratada honestamente como conjectura pelo próprio
autor.
