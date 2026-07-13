# Estado atual — Collatz

Última atualização: 2026-07-13

## Onde estamos

Levantamento inicial da literatura concluído (ver `literature/00-index.md`). Ainda
não há hipóteses formais nem experimentos.

## O que o levantamento estabeleceu

- Não existe prova aceita. Resultado mais forte e rigoroso: Tao (2019) — quase
  todas as órbitas atingem valores quase limitados (afirmação de densidade, não a
  conjectura completa).
- Verificação computacional sem contraexemplo até 2^71 (Barina, 2025).
- Três famílias de abordagem mapeadas: 2-ádica/ergódica, estocástica/heurística
  (Kontorovich–Lagarias), e "provas" completas não verificadas (tratar com
  ceticismo — ver `literature/unverified-proof-claims.md`).
- Obstáculo estrutural comum a todas: nenhum método conhecido certifica que o
  conjunto residual de "sobreviventes" é vazio. Qualquer hipótese nova deveria
  endereçar isso explicitamente ou já nasce redundante com tentativas anteriores.
- Existe um paper metodológico direto sobre colaboração humano-LLM neste problema
  (`literature/resources-and-tools.md`) — reforça que toda hipótese/experimento
  aqui precisa de verificação clara, não "a IA disse que funciona".

## Hipóteses abertas

(nenhuma ainda — ver `protocols/new-hypothesis.md`)

## Ideias descartadas

(nenhuma ainda)

## Descobertas recentes

- 2026-07-13: levantamento de literatura inicial (5 notas temáticas em
  `literature/`), cobrindo estado da arte, abordagens conhecidas e recursos de
  referência (bibliografias de Lagarias, projeto ccchallenge.org).

## Próximos passos

1. A partir do levantamento, escolher 1-2 ângulos concretos de exploração para a
   primeira hipótese formal (ex: alguma variação nos modelos estocásticos, ou
   verificação computacional de um caso específico ainda não coberto).
2. Abrir a primeira hipótese seguindo `protocols/new-hypothesis.md`.
