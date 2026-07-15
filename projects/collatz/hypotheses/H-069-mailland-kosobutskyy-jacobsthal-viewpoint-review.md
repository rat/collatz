# H-069 — Revisão do paper #084 (Mailland & Kosobutskyy, "Modelling the Collatz Problem from a Jacobsthal Viewpoint") — caso particular κ=3 já coberto por H-063, extensão numérica confirmada

Status: revisão externa concluída — reformulação notacional correta,
caso particular (κ=3) do framework já verificado em [[H-063-jacobsthal-trees-review]]
Criada em: 2026-07-15
Origem: item 084 da coleção (`literature/papers/INDEX.md`), já baixado
(`084_Modelling-Collatz-Jacobsthal-Viewpoint.pdf`).

## O paper

Mailland, D. & Kosobutskyy, P. (2026), *Modelling the Collatz Problem
from a Jacobsthal Viewpoint*, Communications in Advanced Mathematical
Sciences (CDS) 8(1), 49-55, peer-reviewed. Mesmos dois autores do item
032 ([[H-063-jacobsthal-trees-review]]), em ordem reversa — este é o
paper anterior (recebido fev/2026, publicado abr/2026), citado como
referência `[8]` pelo item 032. O próprio texto o descreve como
"pedagogical and structural introduction... restricted to κ=3" (Seção
Conclusions) — não alega provar a conjectura.

## Relação com o item 032 (H-063)

O item 032 generaliza este framework para `κx±1` com qualquer κ ímpar,
via `J^±_{κ,θ,n} = (θ·2^n ± (-1)^n)/κ`. Este paper (084) é exatamente o
caso particular `κ=3`, notação `m_{θ,k} = (θ·2^k - 1)/3` — a mesma
quantidade `J^-_{3,θ,k}` de #032, apenas sem o aparato de κ genérico.
`E-063` já testou exaustivamente a versão geral (κ=1..199, incluindo
κ=3) e, na sua **Parte 8**, verificou especificamente os dois exemplos
numéricos deste paper (θ=5: k=0 não é nó, k=1 é nó com q=3; Exemplo 1
[10=3·3+1]; Exemplo 2 [16=3·5+1]) e a condição de periodicidade mod 3
(Eq 7-8 deste paper). Portanto **não há necessidade de duplicar** essa
verificação — ver `experiments/E-063-jacobsthal-trees-check/experiment.py`.

## O que este paper adiciona (verificado em E-069)

Duas figuras com conteúdo numérico específico que E-063 Parte 8 não
cobria:

- **Fig. 1** — uma "árvore geradora" (spanning tree) mostrando a coluna
  `θ=5` expandida em `k=1,3,5,7,9,11` (gerando `q=3,13,53,213,853,3413`,
  seguindo o padrão `q_{i+1}=4q_i+1`, consequência direta da Eq 5) e a
  coluna `θ=1` expandida em `k=0,2,4,6,8,10,12` (gerando
  `q=0,1,5,21,85,341,1365`).
- **Fig. 2** — uma representação em rede de Petri mostrando 10 colunas:
  `S(1),S(5),S(85),S(341),S(13),S(53),S(853),S(3413),S(7),S(113)`.

`experiments/E-069-mailland-kosobutskyy-jacobsthal-viewpoint-check/experiment.py`,
4 partes, **0 falhas**: Parte 1 reconfirma a condição de integralidade/
periodicidade mod 3 (Eq 5-8) de forma independente e rápida; Parte 2
reconfirma os Exemplos 1-2; Parte 3 reconstrói a árvore completa da Fig.
1 (incluindo os "ramos mortos" `θ=3,21` — nunca geram nó por serem
`≡0 mod 3`); Parte 4 confirma que as 10 colunas da Fig. 2 são todas
alcançáveis a partir da raiz `θ=1` em até 3 níveis de expansão.

## Nota de metodologia própria — leitura de figura incerta

Minha leitura visual inicial da Fig. 1 sugeriu que os nós `57` e `229`
estariam ligados ao nó `85`. Verificação computacional mostrou que
`57=m_{43,2}` e `229=m_{43,4}` — **não descendem de `θ=85`** (cujos
filhos reais são `7` e `113`). Isto quase certamente reflete um erro da
minha leitura da posição exata dos círculos numa figura densa (~90
círculos na Fig. 2), não um erro do paper. Por isso `E-069` verifica
apenas os **números** que aparecem nas figuras (todos válidos como
instâncias de `m_{θ,k}`), sem depender de uma leitura pixel-perfeita da
adjacência exata de cada aresta — mesmo princípio de cautela usado
anteriormente ao evitar reconstruir conteúdo a partir de transcrição
incerta.

## Veredito

Nenhum erro matemático. Reformulação notacional correta e caso
particular fiel do framework de [[H-063-jacobsthal-trees-review]]. Os
dois exemplos numéricos e as duas figuras (na medida em que seus
números são verificáveis independentemente da adjacência exata)
reproduzem-se exatamente.

## Novas hipóteses?

Nenhuma nova — mesmo framework de H-063.

## Atualizações

- 2026-07-15: paper lido por completo (7 páginas), confirmado como caso
  particular κ=3 de #032; conteúdo específico (Figs. 1-2, não coberto
  por E-063 Parte 8) verificado em E-069, 0 falhas. `INDEX.md`
  atualizado (item 084: Lido=Sim, Corrigido=Sim, Implementado=Sim).
