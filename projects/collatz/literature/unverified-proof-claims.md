# Alegações de prova completa — catálogo cético

## Por que este arquivo existe

A Conjectura de Collatz está aberta há quase 90 anos e atrai um volume incomum de
"provas" publicadas em periódicos de baixo rigor de revisão por pares, preprints não
revisados e sites pessoais. **Nenhuma foi aceita pela comunidade matemática.** Regra
prática: se uma fonte alega ter uma prova completa e definitiva, o padrão de
evidência para acreditar é altíssimo (publicação em periódico de matemática de
primeira linha + verificação por especialistas independentes) — presunção inicial é
de que a prova tem um furo, geralmente em algum ponto exatamente onde o "obstáculo
estrutural" (ver `overview-and-known-results.md`) apareceria.

## Alegações encontradas no levantamento (não verificadas, tratar com ceticismo)

- "A Proof of the Collatz Conjecture via Thermodynamic Entropy Decay, Modular
  Arithmetic, and 2-Adic Analysis" — Journal of Mathematics Research (CCSE), 2025.
  Periódico sem reputação estabelecida em matemática pura.
- "A 2-adic Algebraic Proof of the Collatz Conjecture via Finite State Automaton
  Analysis" — preprint no Figshare (não é veículo de publicação com revisão por
  pares).
- "A Proof of the Collatz Conjecture via Boundedness and Cycle Uniqueness" —
  preprint em Preprints.org (idem, sem revisão por pares).
- "Unfolding the Collatz Tree: An Indirect Structural Proof" — Eyob Solomon
  Getachew, Taylor & Francis ("Research in Mathematics"), periódico de escopo
  genérico (não especializado em matemática pura), 2025. **PDF arquivado em
  2026-07-15** via busca EBSCO/ScienceDirect (`literature/papers/INDEX.md` item
  109, `109_Unfolding-Collatz-Tree-Structural-Proof.pdf`) — constrói uma árvore
  reversa explícita e alega provar ausência de ciclos não-triviais e
  alcançabilidade finita à raiz, tecnicamente próximo do que fizemos em H-018
  deste projeto. **Ainda não lido/analisado** — candidato natural para revisão
  quando pedido, dado que já temos ferramental (E-018) para checar as alegações
  sobre a estrutura da árvore reversa diretamente.
- Site pessoal "Phil Seawolf — Unified Fields Theory 1" alegando solução — sinal
  claro de trabalho fora do padrão acadêmico, sem revisão alguma.
- **"Proving the Collatz Conjecture with Binaries Numbers"** — Olinto de Oliveira
  Santos, *Pure and Applied Mathematics Journal* 7(5), 2018 (Science Publishing
  Group — editora de baixíssimo rigor de revisão, sem reputação em matemática
  pura). Recebida do usuário em 2026-07-13 (arquivo local
  `/home/rat/Downloads/pamj.20180705.12.pdf`), lida e analisada integralmente.
  **Falha identificada com precisão**: o artigo introduz uma notação binária
  ("movimentos", "reduções fortes") equivalente à nossa própria noção de
  sequência de valuações 2-ádicas (H-001/H-003), sem nada estruturalmente novo.
  O núcleo da "prova" (Seção 2.6) pega um K>30 hipotético, **assume uma
  sequência fixa e específica de passos** (2 movimentos crescentes + 3
  decrescentes com divisores escolhidos à mão) e mostra algebricamente que,
  *para essa sequência particular*, K diminui — depois generaliza
  ilegitimamente essa conclusão para todo K>30. Nunca prova que sequências
  "adversárias" de passos crescentes não podem ser arbitrariamente longas —
  exatamente o obstáculo estrutural que nenhum método conhecido resolve (ver
  acima). Na Seção 2.9 o próprio autor mostra a órbita "fantástica" de n=129
  sem provar rigorosamente que termina, apenas afirma isso por gesto na
  Conclusão. **Veredito: não é uma prova válida.**
- **"Collatz-Thwaites-Ulam-Hasse-Syracuse-Kakutani (CTUHSK) Theorem:
  Convergence of Collatz (3n+1) Sequence to the Trivial Cycle Proved"** —
  Dr.(Prof.) Keshava Prasad Halemane, professor aposentado (NITK Surathkal),
  pesquisador independente, preprint em engrxiv.org, 35 páginas. Item 016 da
  coleção do Google Scholar, lido e analisado integralmente em 2026-07-14
  (arquivo local `literature/papers/016_CTUHSK-Theorem.pdf`). **Falha
  identificada com precisão** (ver `hypotheses/H-043-ctuhsk-halemane-proof-flaw.md`
  e `experiments/E-043-ctuhsk-cycle-proof-check/`): o paper constrói uma
  reformulação notacional da árvore reversa de Collatz padrão (Binary-
  Exponential-Ladders, operadores D#/U#), nada estruturalmente novo. A
  "condição necessária" da prova é tautológica (mostra que o conjunto
  *definido* como quem alcança o ciclo trivial de fato alcança o ciclo
  trivial). A "condição suficiente" — que excluiria ciclos extras e cadeias
  divergentes, carregando todo o peso real da prova — tem um furo decisivo:
  o argumento de redução ao absurdo (Seção 10.2.1) assume que o predecessor
  de um elemento mínimo de um ciclo hipotético é dado pela fórmula do paper
  com o expoente v=1 especificamente, quando na verdade essa fórmula tem
  infinitas soluções válidas (uma por expoente ímpar v=1,3,5,7,...) — e
  apenas v=1 dá um valor menor (violando a minimalidade assumida); todo
  v≥3 dá um valor maior, sem gerar contradição alguma. O paper nunca
  justifica por que o predecessor real dentro do ciclo hipotético teria que
  ser exatamente o de v=1. Confirmado computacionalmente que isso é um
  padrão algébrico geral, não um acidente do exemplo numérico escolhido
  (k=2, BEL(7)/BEL(11)) pelo próprio paper. **Veredito: não é uma prova
  válida.**

- **"Structural Analysis, Dynamic Density Sieve, and Logarithmic
  Contraction of Collatz Sequences"** — Abdullah Mohammed, Kafr
  El-Sheikh University, Egito. Item 011 da coleção do Google Scholar,
  lido e analisado integralmente em 2026-07-14 (arquivo local
  `literature/papers/011_Structural-Analysis-Density-Sieve-Logarithmic-Contraction.pdf`).
  **Falha identificada com precisão** (ver
  `hypotheses/H-045-mohammed-density-sieve-baker-flaw.md` e
  `experiments/E-045-mohammed-density-sieve-baker-check/`): sieve de
  densidade geométrica e exclusão de 1-ciclos corretos (mas não-novos —
  E[M]=2 já é nosso H-001/H-011). O furo está na tentativa de usar o
  Teorema de Baker (formas lineares em logaritmos) para excluir ciclos
  não-triviais: a equação de ciclo do próprio paper força M/P→log₂(3)≈1,585
  para um ciclo real (elementos grandes), mas o paper substitui M≈2P — a
  expectativa ERGÓDICA/MÉDIA de um número ímpar genérico, não a restrição
  de um ciclo autoconsistente — produzindo uma checagem vazia que não
  restringe nada. Mesmo método usado de verdade por Simons & de Weger
  (2005) com constantes de Baker explícitas, mas que não fecha para todo
  P com as constantes efetivas conhecidas. **Veredito: não é uma prova
  válida.**

## Como usar isso no laboratório

- Ao encontrar uma nova alegação de "prova completa", adicione uma linha aqui com
  título, veículo e por que é ou não confiável — não é preciso ler a demonstração
  inteira para registrar o veículo e o nível de ceticismo apropriado.
- Se uma alegação vier de um veículo de primeira linha (Annals of Mathematics,
  Inventiones, Duke Math Journal, ou anúncio de um matemático estabelecido com
  preprint amplamente discutido por especialistas), aí sim vale dedicar tempo a
  entender o argumento em detalhe.
