# Estado atual — Collatz

Última atualização: 2026-07-13

## Onde estamos

Levantamento inicial da literatura concluído (ver `literature/00-index.md`).
Sete hipóteses testadas (H-001 a H-007). **Resultado central do projeto**:
recordistas reais de stopping time nunca são ≡2 mod 3 (exceto o caso trivial
n=2) — confirmado empiricamente com dados oficiais (H-004, n=148,
p<10^-13) e depois **provado algebricamente** (H-007): existe sempre um número
menor que domina qualquer candidato ≡2 mod 3, exceto quando esse número menor
colapsaria em 1.

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

- `H-004` — recordistas reais de stopping time (não outliers locais). **Achado
  principal do projeto até agora**: entre os 148 recordistas reais oficiais
  (OEIS A006877/Roosendaal, de n=1 até ~1.47×10^19), 85 são ≡0 mod 3, 62 são
  ≡1 mod 3, e **apenas 1 é ≡2 mod 3** (esperado uniforme: ~49 cada). O único
  caso ≡2 é n=2 (trivial/borda) — excluindo-o, **0 de 147** recordistas
  restantes são ≡2 mod 3. p=5.2×10^-14 (mod 3), 3.2×10^-19 (mod 9), 1.8×10^-22
  (mod 27), todos com amostra válida. **Explicação mecanicista completa em
  H-007** (ver abaixo). Ver `hypotheses/H-004-true-record-holders.md` e
  `experiments/E-004-true-record-holders/README.md`.
  **Nota de integridade**: a análise original usava uma lista de 57
  recordistas reconstruída de memória, com 4 valores incorretos — corrigido
  usando a sequência oficial completa (ver `CORRECTION.md` no experimento).
  O código de busca de recordistas em si sempre esteve correto (validado
  termo a termo contra a fonte oficial).
- `H-007` — **prova** de por que recordistas nunca são ≡2 mod 3 (exceto n=2).
  Teorema: para todo N≡2 mod 3 com N>2, M=(2N−1)/3 é inteiro ímpar menor que N
  cuja órbita passa por N exatamente 2 passos depois (M→2N→N), logo
  total_stopping_time(M) = total_stopping_time(N)+2 — N nunca pode ser
  recordista. N=2 é a única exceção porque M colapsaria em 1 (estado
  terminal, fora da recursão normal). Verificado sem exceção em 333.332 casos
  até 1M. Fecha completamente o achado de H-004 — deixa de ser um padrão
  empírico sem explicação e passa a ser teorema provado. Ver
  `hypotheses/H-007-why-record-holders-avoid-2-mod-3.md`.
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
- `H-004` (autocorrelação interna, parte da hipótese) — sinal inicial não
  sobreviveu ao controle de confounder de comprimento de órbita — não
  suportada. (A parte mod-3 de H-004 é o principal achado confirmado do
  projeto, ver "Hipóteses confirmadas" acima.)
- `H-006` — viés mod-3 replicado via "top-K por valor bruto" em vez de
  recordistas estritos. Não suportada como formulada (nenhum viés no top-K
  bruto), mas o diagnóstico foi valioso: top-K bruto e recordista estrito são
  populações diferentes, e isso ajudou a descobrir o erro de transcrição
  corrigido em H-004. Ver `hypotheses/H-006-top-k-stopping-time-mod3.md`.

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
- 2026-07-13: **lição de integridade importante** — uma lista de recordistas
  usada para caracterizar H-004 foi digitada de memória em vez de vinda da
  saída real do script, e continha 4 valores incorretos que distorceram a
  conclusão inicial. Corrigido usando a sequência oficial (OEIS A006877). O
  código em si estava correto o tempo todo. Lição documentada em
  `protocols/new-experiment.md`: nunca reconstruir dados de memória — sempre
  usar a saída real ou uma fonte externa salva no repositório.
- 2026-07-13: com dados corrigidos, o achado mod-3 de H-004 ficou **mais
  forte**, não mais fraco (n=148 em vez de 57, p<10^-13 em três módulos).
- 2026-07-13: **achado de H-004 completamente explicado** — H-007 prova
  algebricamente (não só estatisticamente) por que recordistas nunca são ≡2
  mod 3. Descoberto ao pesquisar a literatura: essa exclusão já era usada como
  otimização conhecida em buscadores de "delay records" (repositório
  cuda-collatz), mas sem prova publicada facilmente acessível — derivamos a
  prova nós mesmos.
- 2026-07-13: **outro bug pego a tempo** — uma função "acelerada"
  (`total_steps_only`) assume implicitamente que a entrada é sempre ímpar;
  chamá-la com um número par dá resultado errado sem avisar. Nunca afetou os
  scans principais (sempre iteravam só sobre ímpares), mas pegou uma
  verificação ad-hoc de surpresa. Lição documentada em
  `protocols/new-experiment.md`.

## Próximos passos

Oito hipóteses testadas (H-001 a H-008). O achado central do projeto — por que
recordistas evitam resíduo 2 mod 3 — está **completamente resolvido** (H-007:
prova + verificação). Tentei generalizar a técnica para explicar a ausência da
classe 4 mod 9 (H-008) e **não consegui** — busquei o menor M dominante para
vários N≡4 mod9 e não há relação algébrica curta e fixa (M varia sem padrão,
frequentemente é só um recordista genérico como 27). Deixado como questão
aberta, não forcei uma explicação sem sustentação. Candidatas para a próxima
sessão (escolher com o diretor científico):

1. Tentar uma técnica diferente (cadeia de mais de 2 passos, ou argumento
   não-construtivo) para a classe 4 mod 9 — ou aceitar que pode não ser um
   fato permanente, só válido no intervalo já calculado (~1.47×10^19).
2. Considerar formalizar H-005 e H-007 (teoremas curtos, já provados e
   verificados) em Lean/SageMath se o projeto crescer nessa direção (fora de
   escopo por enquanto, ver `ROADMAP.md`).
3. Voltar à literatura mais ampla (`literature/approaches-2adic-ergodic.md`)
   com a técnica de H-007 em mãos — pode haver outras "exclusões fáceis"
   similares ainda não catalogadas, sem precisar generalizar especificamente
   para mod 9.
4. Deixar a linha mod-3/9 descansar e escolher um ângulo totalmente diferente
   da literatura (ex: verificar a aditividade de ciclos, ou revisitar as
   abordagens 2-ádicas de forma mais profunda).
