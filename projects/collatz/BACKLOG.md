# Backlog de linhas de investigação

Ideias registradas para atacar o problema por múltiplos ângulos, conforme
discutido com o diretor científico em 2026-07-13. Nem toda ideia vira
hipótese formal imediatamente — isso aqui é a lista de candidatas.

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
