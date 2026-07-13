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
- "Unfolding the Collatz Tree: An Indirect Structural Proof" — Taylor & Francis,
  periódico de escopo genérico (não especializado em matemática pura), 2025.
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

## Como usar isso no laboratório

- Ao encontrar uma nova alegação de "prova completa", adicione uma linha aqui com
  título, veículo e por que é ou não confiável — não é preciso ler a demonstração
  inteira para registrar o veículo e o nível de ceticismo apropriado.
- Se uma alegação vier de um veículo de primeira linha (Annals of Mathematics,
  Inventiones, Duke Math Journal, ou anúncio de um matemático estabelecido com
  preprint amplamente discutido por especialistas), aí sim vale dedicar tempo a
  entender o argumento em detalhe.
