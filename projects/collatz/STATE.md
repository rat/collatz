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

- `H-002` — estrutura residual em outliers de stopping time. Planejada, ainda não
  executada (ver `hypotheses/H-002-stopping-time-outliers.md`).

## Hipóteses refutadas

- `H-001` — independência entre valuações 2-ádicas consecutivas (a_1, a_2) na
  órbita acelerada. Testada em `experiments/E-001-parity-independence/`: com
  desenho experimental correto (amostras independentes, sem colisão de órbitas),
  independência **não foi rejeitada** — consistente com o modelo i.i.d. padrão da
  literatura e com o teorema de Terras/Everett. Ver detalhes em
  `hypotheses/H-001-parity-independence.md`.

## Descobertas recentes

- 2026-07-13: levantamento de literatura inicial (5 notas temáticas em
  `literature/`), cobrindo estado da arte, abordagens conhecidas e recursos de
  referência (bibliografias de Lagarias, projeto ccchallenge.org).
- 2026-07-13: **lição metodológica importante** — órbitas de Collatz colidem, e
  agregar estatísticas por posição-em-órbita ao longo de múltiplas trajetórias
  causa pseudo-replicação severa (o mesmo trecho de caminho é contado várias
  vezes), inflando artificialmente significância estatística. Documentado em
  `protocols/new-experiment.md` como armadilha conhecida para todo experimento
  futuro que agregue múltiplas órbitas.
- 2026-07-13: H-001 testada e refutada na forma simples (ver acima).

## Próximos passos

1. Definir o próximo ângulo de pesquisa: executar H-002 (outliers de stopping
   time), ou explorar uma forma mais ambiciosa de H-001 (dependência de longo
   alcance entre a_i e a_{i+k} para k>1, ou dependência condicionada a estrutura
   residual) — já tendo em mãos ferramentas e cuidados metodológicos validados.
2. Ao abrir novo experimento, aplicar desde o início o cuidado de amostragem
   independente descrito em `protocols/new-experiment.md`.
