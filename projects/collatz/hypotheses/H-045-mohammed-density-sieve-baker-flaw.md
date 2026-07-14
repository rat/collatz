# H-045 — Revisão do paper #011 (Abdullah Mohammed, "Density Sieve") — alegação de prova completa, furo lógico encontrado

Status: revisão externa concluída — **prova inválida**, furo lógico
identificado com precisão na aplicação do Teorema de Baker
Criada em: 2026-07-14
Origem: paper baixado manualmente pelo diretor científico (item 011 da
coleção, `literature/papers/011_Structural-Analysis-Density-Sieve-Logarithmic-Contraction.pdf`,
11 páginas).

## O paper

"Structural Analysis, Dynamic Density Sieve, and Logarithmic
Contraction of Collatz Sequences" — Abdullah Mohammed, Faculty of
Science, Kafr El-Sheikh University, Egito. Alega prova completa da
Conjectura de Collatz combinando um sieve de densidade geométrica com o
Teorema de Baker sobre formas lineares em logaritmos.

## O que está correto (Seções 2-5)

- **Sieve de densidade geométrica** (Seção 2-3): P(M=m)=1/2^m para o
  expoente 2-ádico M, com E[M]=2 — exatamente nosso próprio H-001/H-011.
  Derivação correta via série geométrica padrão.
- **Exclusão de 1-ciclos** (Seção 4): de 3n+1=n·2^m, deriva n=1/(2^m-3);
  confirmado computacionalmente que a única solução inteira positiva
  para m∈{1,...,1000} é (m=2, n=1) — argumento elementar e correto.
- **"Special numbers"** (Seção 5): n₀=(4^k-1)/3 = 1,5,21,85,341,1365,...
  — confirmado que cada um atinge 1 em exatamente um passo de Syracuse.
  Sequência conhecida (OEIS A002450), não é descoberta nova.

## O furo decisivo (Seção 7.1, Eq.48)

A Seção 6 deriva corretamente (no formato) a equação de ciclo P-genérico
(equivalente a 2^M=∏(3+1/n_i) para um ciclo hipotético de P elementos —
a mesma identidade usada, por exemplo, no paper Fu-Liu-Wang já revisado
em H-044). A Seção 7.1 tenta então aplicar o Teorema de Baker (formas
lineares em logaritmos) para excluir ciclos não-triviais via
Λ=M ln2 − P ln3.

**O erro**: para que a comparação com Baker exclua algo, é preciso usar
o valor de M/P que um ciclo REAL forçaria — que a própria Seção 6 do
paper implica ser M/P → log₂(3) ≈ 1,585 para elementos grandes (prova
elementar, confirmada em `experiments/E-045-mohammed-density-sieve-baker-check/`:
como 3 < 3+1/n_i ≤ 4 para todo n_i≥1, temos 3^P < ∏(3+1/n_i) < 4^P
estritamente sempre que P≥2 — logo M está estritamente entre P·log₂(3)
e 2P, nunca igual a 2P, exceto no caso degenerado P=1 com n=1 — o ciclo
trivial). Em vez disso, a Eq.48 substitui **M≈2P** — a expectativa
ERGÓDICA/MÉDIA E[M]=2 da Seção 3, que descreve o comportamento do
número ímpar TÍPICO/ALEATÓRIO, uma quantidade completamente diferente e
irrelevante para as restrições de um ciclo hipotético específico
(objeto autoconsistente, não genérico).

Essa substituição produz Λ≈0,288·P — cresce linearmente com P (valor
exato confirmado computacionalmente, bate com o número do próprio
paper, ln(4/3)≈0,28768) — que trivialmente satisfaz o limite inferior
fraco de Baker (~1/P^κ). A "checagem" não restringe absolutamente nada:
qualquer P satisfaz essa desigualdade. A comparação que de fato
importaria (Λ→0 quando M/P→log₂3, o valor real forçado por um ciclo) é
exatamente onde estaria a dificuldade genuína — e é precisamente aí que
a literatura séria (**Simons & de Weger, 2005**, "Theoretical and
computational bounds for m-cycles of the 3n+1 problem") usa constantes
de Baker **explicitamente computadas** para excluir ciclos até certos
comprimentos específicos — mas não "todos os ciclos" em geral, porque o
argumento não fecha para P arbitrariamente grande com as constantes
efetivas atualmente conhecidas. É exatamente por isso que esse caminho
não resolve a conjectura até hoje. O paper de Mohammed nem chega a esse
nível de rigor (não computa C, κ explicitamente — apenas os cita como
"strictly computable") e ainda assim usa a substituição errada no único
lugar em que o argumento precisaria realmente morder.

A Seção 7.2 ("Global Contraction") comete uma variante do mesmo erro:
generaliza um fato estatístico/ergódico (média geométrica do fator
multiplicativo por passo ≈0,866<1 — essencialmente o heurístico por
trás do resultado "quase todas as órbitas" de Tao 2022, citado como
referência [1] do próprio paper) para uma alegação sobre **toda**
trajetória individual, sem justificativa — exatamente a lacuna que o
resultado de Tao explicitamente não fecha ("almost all", não "all").

## Padrão de erro

Mesma categoria de falha das outras "provas completas" já catalogadas
(Santos 2018; CTUHSK/H-043): confundir uma afirmação estatística/média
("em média", "tipicamente", "quase todo") com uma afirmação universal
sobre o objeto hipotético específico em questão (aqui: um ciclo
autoconsistente, ou toda trajetória individual) — precisamente o
obstáculo estrutural que nenhum método conhecido resolve.

## Novas hipóteses?

Nenhuma. O sieve geométrico e E[M]=2 já são nossos (H-001/H-011); a
sequência de special numbers é conhecida (OEIS A002450); a equação de
ciclo é padrão na literatura. Adicionado a
`literature/unverified-proof-claims.md` (é alegação de prova completa,
mesma categoria do Santos e do CTUHSK).

## Atualizações

- 2026-07-14: paper lido por completo (11 páginas), furo identificado e
  confirmado computacionalmente
  (`experiments/E-045-mohammed-density-sieve-baker-check/`). Verificado
  com `advisor()`. Flags atualizadas em `literature/papers/INDEX.md`
  (item 011: Lido=Sim, Corrigido=Sim, Implementado=Sim).
