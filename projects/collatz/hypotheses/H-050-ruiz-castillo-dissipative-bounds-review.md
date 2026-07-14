# H-050 — Revisão do paper #008 (Ruiz Castillo, "Dissipative Bounds and Residual Decomposition") — correto mas elementar, sem verificação numérica

Status: revisão externa concluída — matematicamente correto em tudo
testado, mas conteúdo inteiramente elementar e sem nenhuma verificação
numérica real (mesmo padrão do primeiro paper deste autor, H-039)
Criada em: 2026-07-14
Origem: paper baixado manualmente pelo diretor científico (item 008 da
coleção, `literature/papers/008_Dissipative-Bounds-Ruiz-Castillo.pdf`,
Juan Carlos Ruiz Castillo, University of San Carlos of Guatemala, 44 páginas).

## O paper

"Dissipative Bounds and Ruiz Castillo Residual Decomposition in the
Accelerated Dynamics of the Collatz Conjecture" — segundo paper deste
autor revisado na coleção (o primeiro foi item 001, H-039). Não alega
prova: "The present work does not claim to assert a final proof of the
Collatz Conjecture. Its purpose is to construct a formal architecture
for studying accelerated dynamics."

## O que foi verificado (todos confirmados)

- **Identidade afim exata** U^k(n)=(3^k n+B_k(n))/2^{A_k(n)} e fórmula
  fechada de B_k(n) (Proposições 3.1/3.3): confirmadas exatamente
  (`experiments/E-050-ruiz-castillo-dissipative-bounds-check/`).
- **Decomposição residual** U^k(n)=2^{L_k(n)}n+R_k(n) (Teorema 4.3):
  confirmada.
- **Não-existência de equilíbrio exato** L_k(n)=0 (Proposição 2.14):
  confirmada — consequência trivial de fatoração única (2^{A_k(n)} é
  potência de 2, 3^k é potência de 3, nunca iguais para k≥1).
- **Sensibilidade à ordem da palavra de valuação** (Proposição 5.5):
  confirmado que (1,3) e (3,1) — mesma soma A₂=4 — dão R₂=5/16 e
  R₂=11/16 respectivamente.
- **Cota universal** R_k(n)≤(3/2)^k−1 (Proposição 7.1): confirmada.
- **Critério de descida** (Teorema 8.7): confirmado, com uma nota de
  integridade importante (ver abaixo).

## Nota de integridade: falso positivo corrigido antes de reportar

A primeira tentativa de verificar o Teorema 8.7 usando ponto flutuante
(`2**(k*log2(3)-Ak)`) encontrou 3 "falhas" aparentes, todas em n=1 (o
ponto fixo, onde U^k(1)=1 para todo k — o caso-limite exato da
desigualdade). Investigamos antes de reportar como erro do paper:
recalculando com aritmética exata (`2^{Lk}=3^k/2^{Ak}`, uma fração
exata que evita `log2(3)` em ponto flutuante), as "falhas" desaparecem
— eram um artefato de arredondamento numérico no nosso próprio código
de verificação, bem no limiar onde ambos os lados da desigualdade são
exatamente iguais a n. O teorema do paper está correto; o bug era
nosso, corrigido antes de reportar qualquer coisa como erro.

## Caráter do paper — mesmo padrão do primeiro Ruiz Castillo (H-039)

- **Matemática elementar dressed em terminologia extensa**: a
  "identidade afim exata" é o mesmo "desenrolar" padrão do mapa
  acelerado que aparece (com notação diferente) em Fu-Liu-Wang (H-044,
  Eq.30) e Mohammed (H-045, Eq.40) — a mesma "equação de ciclo" básica.
  As "cotas dissipativas" são séries geométricas elementares. Nenhuma
  proposição/teorema exige mais que indução simples.
- **Zero conteúdo numérico real**: ambas as figuras (1 e 2) são
  explicitamente rotuladas "conceptual... does not represent real
  computational data" — mesmo padrão do H-039 ("zero conteúdo
  numérico, única figura explicitamente conceptual").
- **Alta autocitação**: 4 referências externas reais (Lagarias ×2,
  Wirsching, Tao) contra 12 autocitações do próprio Ruiz Castillo (75%
  — uma melhora frente aos 100% do H-039, mas ainda muito alto). A
  lista de autocitações revela pelo menos mais ~12 papers com títulos
  quase idênticos já escritos pelo mesmo autor sobre a mesma
  "decomposição residual" (ex: "Descending subcylinders and
  dissipative drift...", "Residual drift and average dissipative
  pressure...", "Ergodic interpretation of 2-adic valuations...",
  "Residual walks and dissipative structures...", "Balance between
  ternary growth and binary dissipation...", "Symbolic dynamics and
  dissipative pressure...", "2-adic valuations and residual drift...",
  "Ideal probabilistic model and negative drift...").
- Confirma-se, agora com uma real tese de doutorado citada (ref. [6],
  University of San Carlos of Guatemala) que o autor é um acadêmico
  real, prolífico, não necessariamente crank — mas com um padrão
  editorial de publicar muitos papers curtos com conteúdo
  incrementalmente pequeno sobre a mesma ideia central repetida.

## Implicação para o processamento dos próximos papers Ruiz Castillo

Dado que este é o SEGUNDO paper deste autor com exatamente o mesmo
padrão (matemática elementar correta, terminologia extensa, zero
verificação numérica, alta autocitação), é provável que os demais
papers Ruiz Castillo ainda na fila desta coleção (itens 010, 013, 017,
020) sigam o mesmo padrão. Sinalizado ao diretor científico para
decidir se quer manter o mesmo nível de revisão detalhada para cada um
ou agilizar o processamento dado o padrão já estabelecido.

## Novas hipóteses?

Nenhuma. O mecanismo central (identidade de "desenrolar" o mapa
acelerado) já é conhecido nosso através de outras revisões desta
coleção (H-044, H-045) e da literatura padrão (equação de ciclo de
Lagarias/Steiner).

## Atualizações

- 2026-07-14: paper lido por completo (44 páginas), proposições/teoremas
  centrais verificados computacionalmente
  (`experiments/E-050-ruiz-castillo-dissipative-bounds-check/`),
  nenhum erro real encontrado (um falso positivo de ponto flutuante no
  nosso próprio código foi identificado e corrigido antes de reportar).
  Flags atualizadas em `literature/papers/INDEX.md` (item 008:
  Lido=Sim, Corrigido=Sim [nada a corrigir no paper], Implementado=Sim).
