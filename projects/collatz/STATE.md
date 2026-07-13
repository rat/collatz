# Estado atual — Collatz

Última atualização: 2026-07-13

## Onde estamos

Levantamento inicial da literatura concluído (ver `literature/00-index.md`). H-001
e H-002 testadas — ver resultados abaixo.

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

(nenhuma no momento — ver "Próximos passos" para candidatas)

## Hipóteses refutadas / parcialmente refutadas

- `H-001` — independência entre valuações 2-ádicas consecutivas (a_1, a_2) na
  órbita acelerada. Testada em `experiments/E-001-parity-independence/`: com
  desenho experimental correto (amostras independentes, sem colisão de órbitas),
  independência **não foi rejeitada** — consistente com o modelo i.i.d. padrão da
  literatura e com o teorema de Terras/Everett. Ver detalhes em
  `hypotheses/H-001-parity-independence.md`.
- `H-002` — estrutura residual em outliers de stopping time. Testada em
  `experiments/E-002-stopping-time-outliers/` (n até 2M, top 0.5%, 2 seeds).
  Resíduo mod 2^k mostra diferença enorme, mas é **tautológico** (decorre
  mecanicamente da definição de stopping time via sequência de valuações, não é
  estrutura nova). Resíduo mod 3^k **não mostrou nenhum sinal** — resultado
  negativo genuíno. Hipótese parcialmente refutada: nenhuma estrutura "nova"
  encontrada. Ver `hypotheses/H-002-stopping-time-outliers.md`.
- `H-003` — dependência de longo alcance entre valuações (lags 1-6). Testada em
  `experiments/E-003-long-range-dependency/`: nenhuma dependência significativa
  em nenhum lag (500k amostras cada, todos p > 0.2). Reforça a suposição i.i.d.
  padrão para além do lag 1. Hipótese refutada. Ver
  `hypotheses/H-003-long-range-dependency.md`.
- `H-004` — recordistas reais de stopping time (não outliers locais). Testada em
  `experiments/E-004-true-record-holders/` (recordistas reais até 20-50M,
  validados contra a literatura). Autocorrelação interna: sinal inicial não
  sobreviveu ao controle de confounder de comprimento de órbita — não suportada.
  **Achado promissor** (não tautológico, diferente de H-002): recordistas mostram
  forte sub-representação da classe residual 2 mod 3 (2 de 57, esperado ~19),
  robusto a duas seeds (p~10^-6 a 10^-8) — amostra ainda pequena, candidato para
  investigação futura. Ver `hypotheses/H-004-true-record-holders.md`.

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
- 2026-07-13: H-002 testada. Achado metodológico irmão do de H-001: um sinal
  aparentemente forte (mod-2^k) pode ser tautológico em vez de uma descoberta —
  residuo mod 2^k é quase-determinístico em função da sequência de valuações, que
  é a própria definição de outlier. Sempre verificar se um sinal "óbvio" não é só
  a definição reformulada antes de comemorar.

## Próximos passos

Quatro hipóteses testadas (H-001 a H-004). Três com resultado
negativo/tautológico. H-004 rendeu o primeiro achado genuinamente promissor do
projeto: recordistas reais raramente são ≡2 mod 3 (ver acima). Diretor
científico pediu para testar todas as candidatas, ordem livre:

1. **Pendente**: explorar a família 2-ádica/ergódica da literatura
   (`literature/approaches-2adic-ergodic.md`) como ângulo diferente, já que os
   ataques via estatística simples (H-001/002/003) se esgotaram sem achado novo.
2. Extensão possível (não iniciada): tentar confirmar o sinal mod-3 de H-004 com
   mais recordistas — precisaria de fonte externa tipo tabela Roosendaal, já que
   escanear muito além de 50M em Python puro fica caro computacionalmente.
