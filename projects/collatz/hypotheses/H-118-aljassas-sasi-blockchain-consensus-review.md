# H-118 — Aljassas & Sasi, "Performance Evaluation of Proof-of-Work and Collatz Conjecture Consensus Algorithms" (2019): aplicação, sem erros relacionados a Collatz

Status: sem erros (aplicação, sem alegação matemática sobre a conjectura)
Criada em: 2026-07-17
Origem: item 124 do INDEX.md (IEEE 2019).

## Enunciado

Compara desempenho (tempo, deployment, latência) entre Proof-of-Work
tradicional e "Proof-of-Collatz-Conjecture" (PCC) como consenso em
blockchain privada — PCC usa nº de iterações de Collatz (hash anterior
+ transações convertidos em inteiro) até atingir 1 como "prova".
Resultado: PCC ~1000× mais rápido e mais estável que PoW nos testes.

## Avaliação

Nenhum erro matemático relacionado a Collatz. Descrição do mapa correta
em essência, embora vaga (não detalha condição de paridade
explicitamente — compressão de linguagem, não erro conceitual).
Atribuição da ideia "Collatz como PoW" à ref. Bocart (2018,
"Inflation Propensity of Collatz Orbits").

**Nota de engenharia (não erro matemático)**: usar Collatz como puzzle
de PoW carrega risco latente de não-terminação caso a conjectura seja
falsa para algum inteiro derivado de hash+transações — os autores não
discutem esse risco, mas é ressalva de aplicação, não erro sobre a
conjectura em si.

## Relevância para a investigação atual

Nenhuma — aplicação pura (blockchain/consenso), Collatz usado só como
função de custo computacional imprevisível.
