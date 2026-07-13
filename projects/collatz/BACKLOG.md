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

## 3. Análise de padrões em representação binária

O PDF revisado (`literature/unverified-proof-claims.md`) tentou isso sem
rigor suficiente. Ainda pode haver valor em uma versão mais cuidadosa: olhar
os bits de n (não só resíduos mod 2^k, que já cobrimos em H-002/H-005) à
procura de invariantes ou padrões estruturais ainda não testados por nós.
Não descartada, mas sem um ângulo concreto definido ainda — precisa de mais
uma ideia específica antes de virar hipótese formal.

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
