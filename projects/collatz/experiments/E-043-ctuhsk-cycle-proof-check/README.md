# E-043 — Verificação da "prova" CTUHSK (paper #016 da coleção)

## Objetivo

Verificar de forma independente a alegação central do paper "Collatz-
Thwaites-Ulam-Hasse-Syracuse-Kakutani (CTUHSK) Theorem: Convergence of
Collatz (3n+1) Sequence to the Trivial Cycle Proved" (KP Bikarnakatte /
Dr. Keshava Prasad Halemane, engrxiv.org preprint, 35 páginas) — que
alega uma prova completa da Conjectura de Collatz.

## Estrutura da "prova" no paper

1. **Condição necessária** (Seção 10.1): mostra que H^s (o componente do
   framework H conectado ao nó-sink BEL(1), i.e. ao ciclo trivial
   {4,2,1}) satisfaz os axiomas de Dedekind-Peano e portanto é
   order-isomórfico a N.
2. **Condição suficiente** (Seção 10.2): argumenta, por redução ao
   absurdo, que não existem ciclos extras (H^∞) nem cadeias divergentes
   (H^&) — ou seja, que H^s = H (domain exhaustion).

## O que fizemos

- Reimplementamos as estruturas básicas do paper (mapa de Syracuse,
  classificação mod 6 dos ímpares, fórmula de predecessores) e
  confirmamos que os fatos estruturais preliminares (Eqn.7, 8, 9) estão
  corretos: multiplicidade de 3 realmente não tem predecessor algum;
  números do tipo (6m-1) realmente têm um predecessor válido
  `(n·2^v - 1)/3` para todo expoente ímpar v.
- Reproduzimos exatamente o exemplo numérico do próprio paper (k=2,
  n=11, predecessor 7 via v=1) e confirmamos a aritmética.
- **Achado central**: para n=11, existem infinitos predecessores válidos
  (um por v ímpar: 7, 29, 117, 469, 1877, ...), mas o paper usa apenas o
  de v=1 para "provar" que um ciclo hipotético contendo 11 como elemento
  mínimo do tipo (6m-1) leva a uma contradição de minimalidade (pois
  7<11). Isso não generaliza: para v≥3, o predecessor é MAIOR que 11
  (29, 117, ...), e portanto não violaria minimalidade alguma. O paper
  nunca argumenta por que o predecessor real, dentro do ciclo/cadeia
  hipotético, teria que ser especificamente o de v=1.
- Confirmamos algebricamente (não só para n=11) que isso é um padrão
  geral: `pred(v=1) = (2n-1)/3 < n` e `pred(v=3) = (8n-1)/3 > n` para
  todo n>0 do tipo (6m-1) — não é uma coincidência do exemplo escolhido
  pelo paper, é uma propriedade algébrica de qualquer n dessa forma.
- Confirmamos que a Seção 10.2.2 (cadeias divergentes H^&) usa "o mesmo
  argumento" (palavras do próprio paper) e sofre exatamente da mesma
  falha (testado com n=5, k=1).

## Resultado

**A "prova" tem um furo lógico decisivo na condição suficiente**, que é
a única parte que carregaria conteúdo matemático real (a condição
necessária é tautológica — H^s é definido como quem alcança o ciclo
trivial). Ver `hypotheses/H-043-ctuhsk-halemane-proof-flaw.md` para a
análise completa.

## Como rodar

```
/home/rat/.venv/bin/python3 experiment.py
```

Sem dependências externas (usa apenas `fractions` da biblioteca padrão).
