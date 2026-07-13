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

## 2. Distribuição de stopping times

Já exaustivamente estudada na literatura clássica (heurística de passeio
aleatório, Kontorovich-Lagarias — ver `literature/approaches-stochastic-heuristic.md`),
mas o diretor científico ainda considera um ponto de interesse. Candidato
para uma sessão futura: comparar nossa própria distribuição empírica de
stopping times (já temos o código de E-002/E-004) contra a previsão teórica
precisa da heurística, não só qualitativamente.

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
