# Backlog de linhas de investigação

Ideias registradas para atacar o problema por múltiplos ângulos, conforme
discutido com o diretor científico em 2026-07-13. Nem toda ideia vira
hipótese formal imediatamente — isso aqui é a lista de candidatas.

## 0. Coleção de papers do Google Scholar — LEITURA EM ANDAMENTO (item 001 feito)

Coletados 100 resultados de `scholar.google.com` (busca "Collatz",
ordenado por data) em `literature/papers/INDEX.md` — 15 PDFs baixados
com sucesso, resto sem PDF livre (majoritariamente ResearchGate,
bloqueado por limitação técnica de automação, não necessariamente
pago — ver notas no próprio INDEX.md). Vários papers alegam prova ou
refutação completa da conjectura, candidatos a
`literature/unverified-proof-claims.md`. O diretor científico pede para
ler um por um manualmente, marcando as flags Lido/Corrigido/
Implementado na tabela — **só ler o próximo quando pedido
explicitamente**.

**Item 001 concluído (H-039)**: "Geometría Residual de Ruiz Castillo" —
matemática de base correta mas com fatos triviais repetidos como
resultados maiores, identidade central apresentada inconsistentemente
(derivada no corpo, conjectural só na conclusão), zero conteúdo
numérico, 100% autocitação. Cálculo explícito próprio feito
(P_RC(t)/g_RC(t)/K_RC(t) em forma fechada, singularidade em t=log(2)
encontrada). Nenhuma hipótese nova sobre a conjectura em si. Ver
`hypotheses/H-039-ruiz-castillo-geometria-residual-review.md`. O autor
(Juan Carlos Ruiz Castillo, USAC Guatemala) tem ~19 outros papers na
mesma série na coleção — provavelmente mesma lacuna (sem cálculo
numérico), útil comparar quando lermos os próximos.

## 1. Ciclos não-triviais em inteiros positivos — CONCLUÍDA

Para inteiros **negativos**, o mapa de Collatz estendido tem 3 ciclos
conhecidos. Pergunta do diretor: existe um análogo — um ciclo não-trivial
(diferente de 1→4→2→1) para inteiros **positivos**? Esta é, na verdade, a
segunda metade clássica e ainda aberta da conjectura ("nenhum ciclo
não-trivial"), com literatura séria: Steiner (1977), Simons (2005), Simons &
de Weger (2005, sem ciclo até 68 subidas), Eliahou (1993, limite inferior de
comprimento). Testada em H-009/E-009: busca própria por força bruta (a até
14) não encontrou nada além do trivial, consistente com a literatura. Ver
`hypotheses/H-009-nontrivial-cycles.md`.

**Retomada em H-034** (motivada por vídeo informal que redescobriu a mesma
técnica): achado específico do vídeo refutado tecnicamente; H-009
estendido de a=14 para a=16 (janela mais estreita); parede combinatória
das composições quantificada com precisão (bilhões a partir de a≈20),
explicando por que força bruta pura não alcança o a=68 profissional sem
as técnicas de fração contínua deles. Ver
`hypotheses/H-034-video-cycle-equation-followup.md`.

## 2. Distribuição de stopping times — CONCLUÍDA

Já exaustivamente estudada na literatura clássica (heurística de passeio
aleatório, Kontorovich-Lagarias — ver `literature/approaches-stochastic-heuristic.md`),
mas o diretor científico ainda considera um ponto de interesse. Testada em
H-010/E-010: derivamos K≈7.2283 (constante que multiplica log₂(n) no
stopping time médio) a partir de fatos já estabelecidos por nós (H-001,
E[a]=2), e confirmamos empiricamente (K empírico=7.1833, diferença 0.62%).
R² baixo (0.03) levantou a pergunta: estrutura escondida ou ruído previsto?
**Resolvido em H-011/E-011**: a variância cresce linearmente em log₂n (não
quadraticamente), coeficiente teórico 186.93 vs. empírico 181.53 (diferença
2.9%, testado em 8 ordens de magnitude) — é ruído previsto pela própria
heurística, não estrutura nova escondida.

## 3. Análise de padrões em representação binária — CONCLUÍDA (lista do Fable esgotada)

O PDF revisado (`literature/unverified-proof-claims.md`) tentou isso sem
rigor suficiente. Ganhou um ângulo concreto em 2026-07-13: observação do
diretor científico sobre potências de 2 na árvore reversa virou H-012
(provada), e um brainstorm com o modelo Fable (ver prompt e resposta na
sessão de 2026-07-13) gerou mais ideias, das quais duas já foram verificadas
e confirmadas:

- **H-013** (confirmada): todo órbita termina em J_t=(4^t−1)/3 — consequência
  direta de H-012. Classes estéreis (t múltiplo de 3) explicadas por H-005.
  Anomalia real e não-explicada: fração para t=5 é maior que para t=4.
- **H-014** (confirmada): recordistas nunca são ≡5 mod 8 — segunda técnica de
  exclusão (empate exato por coalescência de trajetórias, diferente do
  domínio estrito de H-007).

Ideias do Fable ainda não testadas, candidatas para sessões futuras:

- **Busca sistemática de coalescências — CONCLUÍDA (escopo mod 2^d)**: testada
  em H-015/E-015. Generalizei H-014 (mod 2^d, N vs. N−k) e encontrei 2374
  classes residuais novas, excluindo cumulativamente 69.3% dos resíduos mod
  2^16. Confirmado válido (com ressalva de N grande o suficiente dentro de
  cada classe). **Não resolve H-008**: por construção, mod 2^d e mod 9 são
  coprimos, então essa técnica nunca poderia dizer nada sobre mod 9.
- **Tentativa mod-9 (módulo conjunto 9·2^d) — CONCLUÍDA, negativa**: testada
  em H-016/E-016. Encontrou candidatos aparentes para excluir a classe 4 mod
  9, mas todos se mostraram genéricos (funcionam para os 9 resíduos mod 9
  igualmente, não só o 4) — são fenômenos mod-2^d disfarçados, não
  descobertas mod-9 genuínas. Explicação teórica: T(n) mod 9 depende só de n
  mod 3, não do valor completo mod 9, então fixar mod 9 não adiciona
  restrição real.
- **H-008 RESOLVIDA COMPLETAMENTE (H-022 + H-027)**: relação multiplicativa
  via 2 passos acelerados (H-022) provou a exclusão da metade ímpar de
  N≡4 mod9 (N=18j+13), verificada sem exceção em 100.000 casos — técnica
  genuinamente nova. A metade par (N≡4 mod18) foi fechada depois (H-027):
  acabou sendo um corolário direto de H-007 (um único passo de halving já
  cai em M≡2 mod3), válido na verdade para toda a classe mais ampla
  N≡4 mod6, verificado sem exceção em 500.000 casos — não uma técnica
  nova, só uma linha de álgebra que tinha passado despercebida. Com as
  duas partes, a classe 4 mod9 está completamente excluída de recordistas,
  com prova. Ver `hypotheses/H-022-mod9-multiplicative-exclusion.md` e
  `hypotheses/H-027-mod6-corollary-closes-h008-even-half.md`.
- **Anomalia p₅>p₄ de H-013 — mecanismo qualitativo + convergência numérica
  confirmada (H-018)**: construção explícita da árvore reversa
  (Galton-Watson) revelou competição entre vantagem geracional (constante) e
  orçamento de bits log₂(n_max/J_t) (encolhe 2 bits por unidade de t).
  Escalado depois até n_max=10¹¹ (corrigindo o multiplicador de busca de
  100× para 5×): a razão (10,11) convergiu e estabilizou (0.0655→0.0656),
  confirmando que a inversão é assintótica real, não ruído. Ainda sem
  fórmula fechada para os valores exatos de convergência. Ver
  `hypotheses/H-018-reverse-tree-branching.md`.
- **Cauda geométrica do pico da órbita — CONCLUÍDA**: testada em H-017/E-017.
  Martingale exato (E[3/2^a]=1) implica expoente de Cramér θ*=1 sem
  parâmetro livre. Confirmado empiricamente: inclinação da cauda distante
  −1.0045 vs. teórico −1.0 (diferença 0.45%, 2M amostras). Terceira
  confirmação teórica precisa do projeto no estilo H-010/H-011.
- **Tempo de mistura da densidade de bits — CONCLUÍDA**: testada em
  H-019/E-019. Razão passos-para-misturar/k estabiliza em ~1.3-1.5 (denso) e
  ~1.0-1.23 (esparso) de k=8 a 1024 — confirma crescimento linear (não
  constante), consistente com 3n+1 ser operação local. Constante exata não
  derivada teoricamente (achado qualitativo).
- **Controle bits altos vs. baixos — CONCLUÍDA, com nuance**: testada em
  H-020/E-020. F-estatística: baixos=50.7, altos=1.80, controle
  aleatório=0.94. Assimetria forte confirmada, mas "zero informação" nos
  bits altos NÃO confirmada com exatidão — resíduo provavelmente explicado
  por H-010/H-011 (média e variância dependem de log₂n), não por informação
  nova. Reportado com essa ressalva honesta em vez de superclaim.
- **Runs de 1s terminais e erosão — CONCLUÍDA**: testada em H-021/E-021.
  Regra de erosão (run encolhe 1 por passo, a=1) confirmada sem exceção
  (50k testes). Recordistas têm runs de subida mais longos (média 2.512)
  que típico (2.035, bate com previsão teórica de H-001) — mas registrado
  como parcialmente tautológico, não descoberta nova.

**Lista de brainstorm do Fable esgotada** (2026-07-13) — todas as ideias
(H-A a H-G) foram testadas, produzindo H-012 a H-021 (dez hipóteses no
total a partir de uma única consulta ao modelo).

- **Densidade do subárvore reverso exige precisão 3-ádica ilimitada —
  CONCLUÍDA (H-024)**: motivada por uma de três listas de ideias externas
  revisadas em 2026-07-13 (ver `literature/external-ideas-review.md`), que
  sugeriu abordagem espectral/operador de transferência para H-013. Testei
  computacionalmente antes de investir na construção: D(v) varia >300× entre
  números com o mesmo resíduo mod 3^6, mesmo com orçamento de magnitude
  proporcional. Fecha com clareza por que a derivação fechada de H-013 não
  fechou, e descarta a via de "operador de dimensão finita" (incluindo a
  variante "operador de transferência quântico" sugerida na terceira lista)
  com evidência direta, não apenas por falta de tentativa. Ver
  `hypotheses/H-024-density-needs-unbounded-precision.md`.

## 6. Revisão crítica de quatro listas de ideias externas (outras IAs) — CONCLUÍDA

Quatro listas trazidas pelo diretor científico em 2026-07-13 (10+1 ideias
"gerais", ideias sobre "outras dimensões"/Koopman, 15 ideias especulativas de
matemática avançada, e uma quarta lista "corrigida" após crítica à terceira).
Avaliação completa registrada em `literature/external-ideas-review.md`: a
maioria dos itens já corresponde a algo que já fizemos (rotulado com
nomenclatura diferente) ou é vaga demais para virar hipótese testável sem
uma ponte concreta com a estrutura combinatória real do Collatz.

Da quarta lista, testei a ideia mais barata e imediatamente acionável
(busca de invariantes lineares em bits, estilo criptoanálise linear) como
**H-025** (refutada, com mecanismo totalmente identificado — toda
correlação bit-a-bit observada se reduz ao valor exato de a, já conhecido,
e ao bias clássico de carry em adição binária). Ver
`hypotheses/H-025-linear-bit-correlations.md`.

- **Taxa de divergência de aproximações de memória 3-ádica finita —
  CONCLUÍDA COM RESSALVA (H-026)**: testei se K maior (mais dígitos
  3-ádicos conhecidos) atrasa a divergência de D(v) em relação à
  aproximação de resíduo. Resultado: comparando na mesma magnitude de v
  (não no mesmo multiplicador), a divergência fica na mesma ordem de
  grandeza para K=4,6,8 — sem evidência de que resíduo mais profundo ajude.
  Sinal real mas baseado em medição única por ponto (quantidade já
  conhecida como muito errática); promediar sobre múltiplos resíduos é o
  próximo passo se retomado. Ver
  `hypotheses/H-026-divergence-rate-independent-of-K.md`.

- **Consolidação via CRT da família de exclusão — CONCLUÍDA (H-028)**:
  combinei H-007+H-014+H-022+H-027 mod 72 (=lcm(8,9)). Resultado: 45 de 72
  resíduos (62,5%) provavelmente excluídos de conter recordistas, zero
  violações contra os 148 recordistas reais conhecidos. Candidato mais
  forte do projeto a nota/paper curto, se decidido formalizar. Ver
  `hypotheses/H-028-crt-exclusion-family-consolidated.md`.

Candidatos ainda não implementados, por ordem de prioridade sugerida:
1. Ângulo de estratégia adversarial de máxima subida, conectando com a
   literatura de limites inferiores em ciclos (Simons & de Weger, Eliahou)
   — potencial nova via para H-009 (ciclos não-triviais).
2. Incorporar H-015 (mod 2^d sistemático, 2374 classes) à consolidação de
   H-028 — deixado de fora por ser lista grande, não fórmula fechada.

- **Varredura sistemática de primos não testados — CONCLUÍDA (H-031)**:
  testei mod 5,7,11,13,17,19,23 e potências maiores de 3 (27,81) contra
  os 148 recordistas reais, buscando exclusão nova além de 2 e 3. Nenhuma
  encontrada — os poucos candidatos em mod81 são consistentes com ruído
  estatístico (calculado via Poisson antes de descartar). Reforça que a
  família de exclusão conhecida está completa nos moduli pequenos. Ver
  `hypotheses/H-031-prime-modulus-scan.md`.

**Koopman operator/DMD vetorial — DESCARTADO (não apenas "em espera")**:
ao finalmente formular a afirmação falsificável específica pedida (prever
resíduos/bits de m a partir de resíduos/bits de n via um mapa linear
ajustado por regressão/DMD), percebi que essa é exatamente a mesma
pergunta que H-025 já respondeu por outro método (busca direta de
correlação linear): a resposta esperada é "nenhuma estrutura linear além
da trivial (explicada pela valuação a)", já confirmada por H-025 e
consistente com a independência confirmada em H-001/H-003. Implementar o
DMD só para redescobrir isso seria trabalho caro por confirmação
previsível — exatamente o tipo de atividade que o loop deveria evitar
fabricar. Descartado como redundante, não como "não testável" (distinção
importante: não é vago, é previsível).

- **Frações contínuas de log₂3 vs anomalia de H-013 — CONCLUÍDA COM
  REFUTAÇÃO (H-032)**: testado e descartado, sem correlação. Ver
  `hypotheses/H-032-continued-fraction-h013-check.md`.

- **Extensão do problema aberto de Chang (bit-4) com recordistas maiores
  — CONCLUÍDA (H-033)**: desvio persiste, consistente com H-021/H-030,
  não resolve nem contradiz o problema aberto original. Ver
  `hypotheses/H-033-chang-bit4-longorbit-extension.md`.

- **Categoria de H-024 vs Conjectura 10.4 de Pratiher — CONCLUÍDA
  COM REFUTAÇÃO, mas esclarecedora (H-035)**: D(v) (por-nó) e Freq_r(N)
  de Pratiher (média de conjunto) são objetos categoricamente diferentes;
  H-024 não se aplica diretamente. Ver
  `hypotheses/H-035-pratiher-q3-vs-h024-category-check.md`.

- **Colisão de literatura: a "obstrução de precisão" já é o resultado
  central de um survey de 216 páginas (H-036)**: ao tentar sintetizar
  H-013/H-018/H-024/H-025/H-026/H-030/H-032 como um achado próprio,
  descobri que a narrativa geral já é o Teorema 13.1 ("Paradigm
  Exhaustion") de Chang (2026, arXiv:2603.11066) — survey-pai do paper
  usado em H-030. Recalibrado com honestidade. Ver
  `hypotheses/H-036-literature-collision-precision-narrative.md`.

- **Provável erro de rotulagem off-by-one na Conjectura 10.4 de Pratiher
  — ACHADO IMPORTANTE (H-037)**: ao investigar se α≈0,9762 seria
  derivável por equidistribuição, um argumento de paridade (mecanismo de
  H-012) mostrou que a forma dominante relatada por Pratiher (expoente
  ímpar) é matematicamente impossível como classe de massa positiva.
  Verificação computacional: correspondência EXATA entre os números
  relatados e os corretos, sob rótulos deslocados em 1 posição no ciclo
  de 6 formas. Validado cruzado contra nossos próprios dados de H-013.
  Números do paper parecem certos; atribuição de forma parece errada.
  Decisão sobre comunicar isso ao autor é do diretor científico. Ver
  `hypotheses/H-037-pratiher-form-off-by-one.md`.

- **Busca de estrutura não-linear (MI) além de H-025 — CONCLUÍDA COM
  REFUTAÇÃO, mecanismo confirmado (H-038)**: testando a generalização
  não-linear de "Project PHI"/campo vetorial Δ(n) (outra resposta da
  mesma IA externa), achei dependência real (peso de Hamming, janelas
  de bits vs segunda valuação) que H-025 (só linear) não capturaria.
  Experimento de controle (substituir 3n+1 por 5n+1, 7n+3, 9n+5)
  confirma que é genérico de aritmética de carry, não específico do
  Collatz — estende H-025, não o contradiz. Ver
  `hypotheses/H-038-nonlinear-mi-embedding-search.md`.

## 4. Verificação de alegações de prova externas

Processo contínuo — toda alegação de prova recebida (ex: PDFs, links) deve
ser lida e catalogada em `literature/unverified-proof-claims.md`, seguindo o
padrão já estabelecido.

## 5. Escrever um paper curto apontando os erros do PDF de Santos (2018) — PENDENTE

Pedido do diretor científico em 2026-07-13. Transformar a análise já feita em
`literature/unverified-proof-claims.md` (o furo lógico na Seção 2.6: assume
uma sequência fixa de passos para K>30 e generaliza ilegitimamente) num
manuscrito curto e formal — algo publicável como nota/comentário crítico, não
apenas uma entrada de catálogo interna. Estrutura sugerida:
1. Resumo da alegação do artigo original.
2. Reconstrução formal do argumento da Seção 2.6.
3. Contra-exemplo ou demonstração explícita do gap lógico (por que a
   generalização de "um K específico" para "todo K" não se sustenta — falta
   de limite sobre sequências adversárias de movimentos crescentes).
4. Conexão com o "obstáculo estrutural" que nenhuma tentativa de prova
   conhecida resolve (`literature/overview-and-known-results.md`).
Ainda não iniciado — próxima sessão pode começar por aqui se o diretor
científico priorizar.

## 7. Escrever um paper curto apontando o erro de rotulagem de Pratiher (2026) — PENDENTE

Pedido do diretor científico em 2026-07-13, mesmo padrão do item 5
("anote para quando terminar, assim como o outro, fazer um paper
mostrando o erro"). Transformar a análise já feita em H-037/E-037 num
manuscrito curto: (1) resumo da Conjectura 10.4 de Pratiher (α≈0,9762
para a forma dominante 'a'); (2) argumento de paridade mostrando que a
forma relatada é impossível como classe de massa positiva (mesmo
mecanismo do nosso H-012); (3) verificação computacional com
correspondência exata sob deslocamento de rótulo de 1 posição; (4)
avaliação cuidadosa — números corretos, rótulo errado, sem acesso ao
código-fonte dele para apontar a causa exata. Ainda não iniciado. Só
escrever quando o diretor científico pedir explicitamente, por último
— junto com o item 5 (ver memória `feedback_santos_pdf_paper_timing.md`
no sistema de memória do Claude).

## 8. Escrever um paper cumulativo de críticas aos papers da coleção do Google Scholar — PENDENTE, ABERTO (cresce a cada item lido)

Pedido do diretor científico em 2026-07-14 ("salve como mencionei para
nosso paper futuro de críticas aos papers atuais"), mesmo padrão de
timing dos itens 5 e 7 (só escrever quando pedido explicitamente, por
último), mas **diferente em natureza**: não é um único achado fechado —
é cumulativo, crescendo a cada paper da coleção (`literature/papers/INDEX.md`)
que lemos e corrigimos um por um. Material já acumulado:

- **Item 001 (H-039)**: Ruiz Castillo, "Geometría Residual..." — mesmo
  fato trivial repetido 4x como resultado maior; identidade central
  apresentada como derivada no corpo mas conjectural só na conclusão;
  zero conteúdo numérico (única figura explicitamente "conceptual");
  100% autocitação nas 13 referências (zero literatura de Collatz ou
  de formalismo termodinâmico clássico).

- **Item 004 (H-040) — achado importante**: Seymour, "Steiner Sentence
  Length Distribution" — paper bem melhor (cita literatura real,
  valida empiricamente, alega verificação formal em Lean 4/Mathlib sem
  `sorry`), mas o **teorema principal parece incorreto**: reimplementação
  independente + contraexemplo de aritmética exata (n=68567) mostram que
  a distribuição real é (1/2)^k — exatamente o modelo "ingênuo" que o
  paper argumenta estar errado — não 3^(k-1)/4^k como afirmado. Erro
  provável: conflação entre a matriz de transição de UM passo de
  Syracuse (correta) e a transição entrada-a-entrada entre PALAVRAS
  consecutivas (que exige 2+ passos para as classes 3 e 7). Não temos
  acesso ao código Lean para confirmar onde a formalização diverge da
  definição em prosa.

- **Item 005 (H-041)**: Seymour, "A Regular Expression Language for the
  Collatz Graph" — mesmo autor do item 004, mas de boa prática
  epistêmica: explicitamente rotulado "working paper", separa
  claramente provado de conjecturado. Dois resultados centrais
  confirmados corretos (Proposição 3.1, Teorema 3.6). Um erro pequeno
  e sistemático encontrado no Corolário 2.2 (afirma alternância
  11/23 mod24 conforme paridade de t; na verdade é sempre 11) — mas
  esse corolário nem consta na lista "What is proved" da própria
  conclusão do paper, calibrando a gravidade como baixa. A conjectura
  central (caracterização via regex) é tratada honestamente como
  conjectura, não como prova.

- **Item 014 (H-042) — sem erros, ponto de calibração positivo**:
  Williams, "A Coordinate System for Collatz Dynamics" (Univ. of
  Southampton, arXiv:2607.01718). Qualidade acadêmica claramente
  superior: literatura extensa e genuína, código público, declaração
  honesta de uso de IA (Claude Opus 4.8, com verificação humana
  integral), agradecimento a um colega por revisão que já pegou um
  erro menor antes da publicação. Os dois teoremas centrais (dinâmica
  diagonal, linhas livres de primos) foram confirmados corretos, sem
  exceção. Útil para a crítica cumulativa como contraponto: nem todo
  paper da coleção tem problemas.

Continuar adicionando aqui (ou num arquivo dedicado, se a lista crescer
muito) conforme processarmos os próximos itens da coleção. Ver memória
`feedback_santos_pdf_paper_timing.md`.
