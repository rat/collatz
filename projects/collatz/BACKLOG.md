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

## 3. Análise de padrões em representação binária — EM ANDAMENTO

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
  coprimos, então essa técnica nunca poderia dizer nada sobre mod 9 — H-008
  precisaria de uma técnica mod-3^b separada (ex: generalizar H-005 para mod
  9), ainda não tentada com sucesso. A versão de profundidade 8-10 tratando
  mod 2 e mod 3 conjuntamente (ideia original do Fable) segue como
  possibilidade mais ambiciosa para o futuro, se alguém quiser retomar.
- Investigar a anomalia p₅>p₄ de H-013 (talvez ligada ao resíduo mod 3 de
  cada J_t afetando a estrutura da árvore reversa).
- Cauda geométrica do pico da órbita (martingale, E[3/2^a]=1 exatamente) —
  previsão sem parâmetro livre, no estilo H-010/H-011 mas para o máximo em
  vez da média/variância do tempo.
- Tempo de mistura da densidade de bits (popcount) partindo de extremos —
  primeira estatística global de bits do projeto, não redutível a mod 2^k.
- Controle metodológico: confirmar que bits ALTOS de n não carregam
  informação sobre stopping time (só os baixos, via Terras) — protege contra
  a armadilha tautológica de H-002.
- Runs de 1s terminais e erosão determinística — mecanismo binário por trás
  das "subidas", risco tautológico a declarar explicitamente se testado.

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
