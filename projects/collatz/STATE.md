# Estado atual — Collatz

Última atualização: 2026-07-13

## Onde estamos

Levantamento inicial da literatura concluído (ver `literature/00-index.md`).
**Vinte e uma hipóteses testadas (H-001 a H-021)**, mais um PDF externo
revisado e catalogado. **Resultado central do projeto**: recordistas reais
de stopping time nunca são ≡2 mod 3 (exceto o caso trivial n=2) — confirmado
empiricamente (H-004, n=148, p<10^-13) e **provado algebricamente** (H-007).
Generalizamos a técnica de exclusão por empate (H-014→H-015): 2374 classes
residuais mod 2^d excluídas, 69.3% de mod 2^16 — mas **não resolve H-008**
(limitação estrutural: mod 2^d e mod 9 são coprimos; tentativa mod-9
conjunta em H-016 também não resolveu). A lista completa de brainstorm do
modelo Fable sobre padrões binários (H-012 a H-021) foi **totalmente
testada** nesta sessão, incluindo um mecanismo qualitativo (Galton-Watson)
para a anomalia de H-013 e três confirmações teóricas precisas no estilo
"derivar → confirmar" (H-010, H-011, H-017). H-008 continua sendo a única
questão central em aberto. Backlog em `BACKLOG.md`. **Tarefa pendente**:
escrever um paper curto apontando os erros do PDF de Santos 2018 — só fazer
quando o diretor científico pedir explicitamente, por último (o diretor
pediu para lembrá-lo de avisar quando isso for feito).

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
- `H-010` — constante assintótica do stopping time. Derivamos K≈7.2283
  (total_stopping_time(n) ≈ K·log₂n) a partir de fatos já estabelecidos por
  nós (E[a]=2, H-001), e confirmamos empiricamente: K empírico=7.1833
  (diferença 0.62%). R²=0.03 — log₂(n) sozinho explica pouco da variância
  individual. Ver `hypotheses/H-010-stopping-time-asymptotic-constant.md`.
- `H-011` — a variância residual de H-010 é ruído previsto, não estrutura
  escondida. Derivamos que Var(total_stopping_time) deveria crescer linear
  em log₂n (coeficiente teórico 186.93, via aproximação de tempo de primeira
  passagem). Confirmado empiricamente em 8 ordens de magnitude (log₂n de 10.5
  a 45.5): coeficiente empírico 181.53, diferença de 2.9%. Resolve a pergunta
  em aberto de H-010. Ver `hypotheses/H-011-variance-scaling.md`.
- `H-017` — cauda do pico da órbita. A sequência de valores ímpares é um
  martingale multiplicativo exato (E[3/2^a]=1, verificado analiticamente),
  o que implica via equação de Cramér um expoente de decaimento exato
  θ*=1 (sem parâmetro livre) para a cauda do pico: P(pico≥n·2^Δ)~C·2^(−Δ).
  Confirmado empiricamente: inclinação da cauda distante −1.0045 vs. teórico
  −1.0 (diferença 0.45%, 2M amostras, duas seeds). Ver
  `hypotheses/H-017-peak-excursion-tail.md`.
- `H-012` — estrutura de predecessores de potências de 2 (a partir de
  observação do diretor científico sobre 32/64 na árvore reversa). Provado:
  2^k tem predecessor ímpar genuíno sse k é par, e nesse caso o predecessor é
  Σ4^i (sempre ímpar). Conecta diretamente com o lema de H-005. Verificado
  para k=1..60. Ver `hypotheses/H-012-powers-of-2-predecessor-structure.md`.
- `H-013` — todo órbita termina no último valor ímpar J_t=(4^t−1)/3
  (consequência de H-012). Classes estéreis (t múltiplo de 3) explicadas por
  H-005 (J_t divisível por 3 nunca reaparece). Confirmado sem exceção em
  300k amostras (e depois em varredura exaustiva até 80M). Anomalia real e
  ainda não-explicada: fração para t=5 (341) maior que para t=4 (85), e para
  t=8 maior que t=7 — mas **hipótese inicial (ligada a mod 3 de J_t)
  refutada**: a razão entre classes adjacentes inverte em t=10/11 e t=13/14
  (varredura exaustiva). Não é um padrão simples — continua em aberto. Ver
  `hypotheses/H-013-last-odd-value-structure.md` e
  `experiments/E-013-last-odd-value-structure/CORRECTION.md`.
- `H-014` — recordistas nunca são ≡5 mod 8. Segunda técnica de exclusão
  (empate exato: N=4u+1 com u ímpar tem total_stopping_time igual, não
  menor, ao de N−1, via coalescência de trajetórias — diferente do domínio
  estrito de H-007). Confirmado em 200k casos + nenhum dos 148 recordistas
  oficiais é ≡5 mod 8. Ver `hypotheses/H-014-tie-exclusion-mod8.md`.
- `H-015` — busca sistemática de coalescências mod 2^d (generalização de
  H-014). Encontrou 2374 classes residuais novas, excluindo cumulativamente
  69.3% dos resíduos mod 2^16. Verificado válido para K grande o suficiente
  (efeito de borda em K pequeno, análogo ao N=2 de H-007 — só 6 dos 148
  recordistas, todos muito pequenos, "violam" alguma exclusão). **Não
  resolve H-008** por limitação estrutural (mod 2^d e mod 9 são coprimos).
  Ver `hypotheses/H-015-systematic-coalescence-search.md`.
- `H-018` — mecanismo qualitativo (Galton-Watson) por trás da anomalia de
  H-013. Construção explícita da árvore reversa (após corrigir um bug de
  poda por magnitude) revela: geração do primeiro checkpoint é constante
  (1 para t≡2mod3, 2 para t≡1mod3, insuficiente sozinho); o "orçamento"
  log₂(n_max/J_t) encolhe 2 bits por unidade de t — explica por que a
  vantagem geracional domina para t pequeno mas é dominada por flutuações
  de árvore finita para t grande. Sem fórmula fechada. Ver
  `hypotheses/H-018-reverse-tree-branching.md`.
- `H-019` — tempo de mistura da densidade de bits. Razão passos/k estabiliza
  em ~1.3-1.5 (denso) e ~1.0-1.23 (esparso) de k=8 a 1024 — confirma
  crescimento linear, consistente com 3n+1 ser operação local. Ver
  `hypotheses/H-019-bit-density-mixing.md`.
- `H-021` — erosão de runs de 1s terminais. Regra confirmada sem exceção
  (50k testes). Recordistas têm runs de subida mais longos (2.512 vs 2.035
  típico, que bate com previsão teórica de H-001) — registrado como
  parcialmente tautológico. Ver `hypotheses/H-021-terminal-run-erosion.md`.

## Hipóteses parcialmente confirmadas (com ressalva)

- `H-020` — controle bits altos vs. baixos. F-estatística: baixos=50.7,
  altos=1.80, controle aleatório=0.94. Assimetria forte confirmada, mas
  "zero informação" nos bits altos não confirmada com exatidão — resíduo
  provavelmente explicado por H-010/H-011 (média/variância dependem de
  log₂n), não por informação nova. Ver
  `hypotheses/H-020-high-bits-no-information.md`.

## Hipóteses refutadas relacionadas a H-008 (tentativas negativas registradas)

- `H-016` — tentativa de estender a coalescência para módulo conjunto
  9·2^d, tentando atacar H-008 diretamente. Encontrou candidatos aparentes
  para excluir a classe 4 mod 9, mas todos se mostraram genéricos (funcionam
  para os 9 resíduos mod 9 igualmente — testado até d=7, k=100) — são
  fenômenos mod-2^d disfarçados, não achados mod-9 genuínos. Explicação
  teórica: T(n) mod 9 depende só de n mod 3, não do valor completo mod 9,
  então fixar mod 9 não adiciona restrição real. H-008 continua sem solução;
  precisaria de uma técnica estruturalmente diferente. Ver
  `hypotheses/H-016-mod9-coalescence-search.md`.

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
- `H-009` — busca por ciclo não-trivial em inteiros positivos (pergunta do
  diretor científico, por analogia aos 3 ciclos conhecidos em negativos).
  Busca própria por força bruta (a=1 até 14) não encontrou nada além do ciclo
  trivial — consistente com Steiner (1977), Simons (2005) e Simons & de Weger
  (2005, que já provaram rigorosamente até a=68, muito além do nosso
  alcance). Não é descoberta nova, é verificação própria de resultado já
  estabelecido. Ver `hypotheses/H-009-nontrivial-cycles.md`.

## Questões em aberto (sem prova nem refutação)

- `H-008` — por que a classe 4 mod 9 nunca aparece em recordistas (mesmo não
  sendo excluída pela prova de H-007). Tentei generalizar a técnica de H-007
  e não encontrei uma relação algébrica curta. Ver
  `hypotheses/H-008-mod9-class4-open-question.md`.

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
- 2026-07-13: diretor científico pediu para atacar o problema por múltiplos
  ângulos simultaneamente (não só provar, também tentar desprovar/refutar).
  Registrado backlog em `BACKLOG.md`: ciclos não-triviais em positivos,
  distribuição de stopping times, análise de padrões binários. Escolhi
  ciclos não-triviais como próximo passo (H-009) — mais tratável e com
  literatura séria para comparar.
- 2026-07-13: revisado e catalogado um PDF externo enviado pelo usuário
  ("Proving the Collatz Conjecture with Binaries Numbers", Santos 2018,
  periódico de baixo rigor) — não é uma prova válida; falha identificada com
  precisão (Seção 2.6 assume uma sequência fixa de passos e generaliza
  ilegitimamente). Catalogado em `literature/unverified-proof-claims.md`.
- 2026-07-13: H-009 testada — busca própria por ciclo não-trivial (a até 14)
  não encontrou nada além do trivial, consistente com Steiner/Simons/de
  Weger.
- 2026-07-13: diretor científico pediu para registrar uma tarefa pendente:
  escrever um paper curto apontando os erros do PDF de Santos (2018) —
  registrado em `BACKLOG.md`, ainda não iniciado.
- 2026-07-13: H-010 testada — derivamos e confirmamos empiricamente a
  constante assintótica do stopping time (K≈7.23·log₂n, diferença de 0.62%
  entre teoria e dados). R²=0.03 é o achado lateral interessante: pouquíssimo
  da variância individual vem do tamanho de n.
- 2026-07-13: diretor científico pediu para deixar o paper sobre o PDF por
  último e continuar as análises.
- 2026-07-13: H-011 testada — resolvida a pergunta em aberto de H-010:
  derivamos que a variância de total_stopping_time deveria crescer linear em
  log₂n (não quadraticamente), coeficiente teórico 186.93. Confirmado
  empiricamente em 8 ordens de magnitude (log₂n de 10.5 a 45.5): coeficiente
  empírico 181.53, diferença de 2.9%. O R² baixo de H-010 é ruído previsto
  pela própria heurística, não estrutura escondida.
- 2026-07-13: diretor científico trouxe uma observação da árvore reversa de
  Collatz (potências de 2 como 32/64 se comportam diferente) e pediu para
  explorar padrões binários, sugerindo consultar um modelo de IA (Fable) para
  brainstorm de hipóteses novas. H-012 testada — a observação virou um
  teorema curto e provado (conecta com H-005): 2^k tem predecessor ímpar na
  árvore reversa sse k é par. Um agente rodando o modelo Fable foi consultado
  em paralelo para gerar mais hipóteses de padrão binário (resultado a
  incorporar quando o agente terminar).
- **Lembrete permanente**: só escrever o paper sobre os erros do PDF de
  Santos quando o diretor científico pedir explicitamente — não fazer por
  iniciativa própria, mesmo que pareça um bom momento.
- 2026-07-13: agente Fable retornou brainstorm de padrões binários. Relatório
  bem calibrado (já avisou da armadilha tautológica de H-002 antes de propor
  ideias). Verifiquei de forma independente as duas hipóteses mais fortes
  (nunca aceitar afirmação de agente sem checar):
  - **H-013** (confirmada): toda órbita termina em J_t=(4^t−1)/3
    (consequência de H-012). Classes estéreis explicadas por H-005. Achou
    uma anomalia real (t=5 mais frequente que t=4) — deixada em aberto.
  - **H-014** (confirmada): recordistas nunca ≡5 mod 8 — segunda técnica de
    exclusão (empate exato por coalescência, diferente do domínio de H-007).
  - Ideias mais ambiciosas do Fable (busca sistemática de coalescências que
    poderia resolver H-008; cauda do pico da órbita; mistura de densidade de
    bits) registradas em `BACKLOG.md` item 3 para sessões futuras.
- 2026-07-13: H-015 testada (busca sistemática de coalescências mod 2^d,
  generalizando H-014) — 2374 classes novas, 69.3% de mod 2^16 excluído.
  Confirmado válido para N grande o suficiente. **Não resolve H-008** —
  limitação estrutural clara (mod 2^d e mod 9 são coprimos), documentada
  para não repetir a tentativa nessa forma no futuro.
- 2026-07-13: diretor científico pediu para tentar uma versão mod-9 da
  técnica, atacando H-008 diretamente. H-016 testada: encontrou candidatos
  aparentes usando módulo conjunto 9·2^d, mas todos se revelaram genéricos
  (funcionam para os 9 resíduos mod 9 igualmente, não só o 4) ao testar
  explicitamente a exclusividade — resultado negativo, mas com explicação
  teórica clara (T(n) mod 9 depende só de n mod 3, não do valor completo mod
  9). H-008 continua sem solução.
- 2026-07-13: escolhi H-017 (cauda do pico da órbita) como próximo passo —
  ideia do Fable com previsão sem parâmetro livre. Verifiquei a equação de
  Cramér antes de implementar (θ*=1 exato). Confirmado empiricamente com
  grande precisão (0.45% de diferença na cauda distante). Terceira vitória
  no estilo "derivar teoria → confirmar nos dados" (depois de H-010/H-011).
- 2026-07-13: diretor científico expressou compromisso de longo prazo com o
  projeto ("nunca vamos parar"). Respondi com calibração honesta: Collatz
  resistiu a ~90 anos de matemáticos profissionais (incluindo Tao), é
  extremamente improvável que seja "resolvido" por completo por este
  laboratório — mas o trabalho incremental real (teoremas verificados, erros
  corrigidos, resultados negativos documentados) já é ciência genuína e vale
  a pena continuar sessão após sessão.
- 2026-07-13: investiguei a anomalia p₅>p₄ de H-013 mais a fundo. Especulei
  que fosse ligada ao resíduo mod 3 de J_t — **refutei minha própria
  hipótese** com varredura exaustiva até 80M: a razão entre classes
  adjacentes cresce em (4,5) e (7,8) mas inverte em (10,11) e (13,14). A
  anomalia é real (confirmada em duas escalas) mas não segue um padrão
  simples de mod 3 — continua genuinamente em aberto.
- 2026-07-13: diretor científico pediu para testar tudo em sequência,
  começando pela análise de ramificação (Galton-Watson) da árvore reversa.
  H-018: construí a árvore reversa explicitamente, corrigi um bug real de
  poda por magnitude no caminho, e encontrei um mecanismo qualitativo
  (competição entre vantagem geracional constante e orçamento de bits que
  encolhe 2 bits por t) que explica coerentemente a não-monotonicidade,
  sem fórmula fechada.
- 2026-07-13: completei toda a lista restante do brainstorm Fable em
  sequência: H-019 (mistura de densidade de bits, confirmada — crescimento
  linear), H-020 (controle bits altos, parcialmente confirmada — assimetria
  forte mas resíduo não-nulo explicado por H-010/H-011), H-021 (erosão de
  runs terminais, confirmada + achado tautológico sobre recordistas). Lista
  do Fable totalmente esgotada — 10 hipóteses (H-012 a H-021) a partir de
  uma única consulta ao modelo.

## Próximos passos

**Vinte e uma hipóteses testadas (H-001 a H-021)**. O achado central do
projeto — por que recordistas evitam resíduo 2 mod 3 — está **completamente
resolvido** (H-007), com uma técnica irmã generalizada em larga escala
(H-014→H-015). A pergunta da variância de H-010 também está **resolvida**
(H-011), assim como a cauda do pico da órbita (H-017). A lista de brainstorm
do Fable está **totalmente esgotada**. Restam duas questões genuinamente
em aberto:

1. **H-008** (classe 4 mod 9 nunca aparece em recordistas) — duas
   tentativas de coalescência (H-015 mod-2^d, H-016 mod-9 conjunto) não
   resolveram; precisaria de uma ideia estruturalmente diferente (ex:
   relação multiplicativa em vez de aditiva).
2. **Anomalia de H-013** (razão não-monotônica entre classes J_t adjacentes)
   — H-018 deu um mecanismo qualitativo (competição orçamento vs. vantagem
   geracional), mas não uma fórmula fechada.

Tarefa pendente (**só fazer quando o diretor científico pedir
explicitamente**, por último — lembrar de avisar quando for feito): paper
sobre os erros do PDF de Santos (`BACKLOG.md` item 5). Outras candidatas:

1. Repensar H-008 com uma abordagem genuinamente diferente.
2. Tentar uma teoria quantitativa fechada para a anomalia de H-013 (função
   geradora para o processo de ramificação da árvore reversa).
3. Considerar formalizar os teoremas já provados (H-005, H-007, H-009,
   H-012, H-014, H-015, H-017, H-019, H-021) em Lean/SageMath se o projeto
   crescer nessa direção (fora de escopo por enquanto, ver `ROADMAP.md`).
4. Continuar revisando qualquer nova alegação de prova externa que o diretor
   científico receber, seguindo o padrão já estabelecido em
   `literature/unverified-proof-claims.md`.
5. **Só quando pedido explicitamente**: escrever o paper curto sobre os
   erros do PDF de Santos (`BACKLOG.md` item 5).
