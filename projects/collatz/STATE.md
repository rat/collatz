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

Duas hipóteses testadas, ambas com resultado negativo/tautológico para a pergunta
original. Ainda não encontramos estrutura genuinamente nova. Candidatas para a
próxima hipótese (nenhuma aberta ainda — escolher com o diretor científico):

1. Estender H-001 para dependência de longo alcance (a_i vs a_{i+k}, k>2) ou
   dependência condicionada a alguma variável estrutural — já com o cuidado de
   amostragem independente validado.
2. Repetir E-002 usando recordistas reais catalogados na literatura (Roosendaal)
   em vez de outliers definidos localmente na nossa amostra, e testar
   características que não sejam redutíveis a resíduo mod 2^k (ex: comparar com a
   distribuição completa normalizada da sequência de valuações).
3. Considerar sair do par estocástico/residual e explorar a família 2-ádica/
   ergódica da literatura (`literature/approaches-2adic-ergodic.md`) como próximo
   ângulo, já que os dois primeiros ataques via estatística simples se esgotaram.
