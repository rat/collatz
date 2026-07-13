# Estado atual — Collatz

Última atualização: 2026-07-13

## Onde estamos

Levantamento inicial da literatura concluído (ver `literature/00-index.md`).
Cinco hipóteses testadas (H-001 a H-005) — ver resultados abaixo. As três
candidatas de próximo passo pedidas pelo diretor científico foram todas
executadas nesta rodada.

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

## Hipóteses confirmadas

- `H-005` — lema: T(n) mod 3 é determinado inteiramente pela paridade de a(n)
  (a valuação 2-ádica do passo), nunca pelo resíduo de n mod 3. Prova algébrica
  curta + verificação computacional sem exceção em 777.748 passos (ver
  `experiments/E-005-mod3-valuation-parity/`). Consequência derivada e também
  confirmada: entre termos subsequentes de qualquer órbita, resíduo mod 3 nunca
  é 0, e a proporção 1 vs 2 é 1:2 (não 1:1) — confirmado com 33.47% vs 33.33%
  previsto. Primeira peça de estrutura **exata** (não estatística) do projeto.
  Não explica o achado de H-004 (esse é sobre o número inicial da órbita, não
  sobre termos subsequentes) — continua em aberto. Ver
  `hypotheses/H-005-mod3-valuation-parity-lemma.md`.

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

Cinco hipóteses testadas (H-001 a H-005). As três candidatas pedidas pelo
diretor científico foram todas executadas: extensão de H-001 (H-003, refutada),
recordistas reais (H-004, achado promissor + autocorrelação descartada), e
ângulo 2-ádico/ergódico (H-005, lema confirmado). Nenhuma pendência aberta no
momento — candidatas para a próxima sessão (escolher com o diretor científico):

1. Investigar por que os números **iniciais** de recordistas evitam resíduo 2
   mod 3 (achado de H-004) — H-005 explica termos subsequentes de uma órbita,
   mas não o número inicial. Precisaria de mais recordistas reais (fonte
   externa tipo Roosendaal, já que escanear além de 50M em Python puro é caro)
   ou uma ideia teórica diferente.
2. Generalizar o lema de H-005 para outros módulos além de 3 (ex: mod 9, mod
   27) — pode revelar mais estrutura exata reutilizável.
3. Considerar formalizar alguma dessas descobertas em Lean/SageMath se o
   projeto crescer nessa direção (fora de escopo por enquanto, ver
   `ROADMAP.md`).
