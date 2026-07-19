# E-012 — Predecessores de potências de 2

Hipótese relacionada: [`H-012-powers-of-2-predecessor-structure.md`](../../hypotheses/H-012-powers-of-2-predecessor-structure.md)

## Origem

Observação do diretor científico explorando a árvore reversa de Collatz:
potências de 2 como 32 e 64 parecem se comportar diferente — algumas só são
alcançadas pela cadeia trivial de duplicação, outras têm um ramo extra.

## O que foi verificado

2^k tem um predecessor ímpar genuíno (via 3m+1=2^k) se e somente se k é par,
e nesse caso o predecessor é exatamente Σ_{i=0}^{k/2−1} 4^i (sempre ímpar).
Prova completa em `hypotheses/H-012-powers-of-2-predecessor-structure.md`.

## Resultado

Verificado sem exceção para k=1 até 60. Reproduzir: `python3 experiment.py 60`.

## Status

**Confirmada.** Explica exatamente a observação original: 2^5=32 (k ímpar)
não tem predecessor ímpar — só é alcançado duplicando 16 — enquanto 2^6=64
(k par) tem o predecessor ímpar 21 (3·21+1=64), um ramo extra na árvore.
