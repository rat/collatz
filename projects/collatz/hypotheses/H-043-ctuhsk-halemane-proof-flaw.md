# H-043 — Revisão do paper #016 (Halemane, "CTUHSK Theorem") — alegação de prova completa, furo lógico encontrado

Status: revisão externa concluída — **prova inválida**, furo lógico
identificado com precisão na condição suficiente
Criada em: 2026-07-14
Origem: quinto paper priorizado da coleção (item 016, local, engrxiv.org
preprint, 35 páginas).

## O paper

"Collatz-Thwaites-Ulam-Hasse-Syracuse-Kakutani (CTUHSK) Theorem:
Convergence of Collatz (3n+1) Sequence to the Trivial Cycle Proved" —
Dr. (Prof.) Keshava Prasad Halemane, professor aposentado do National
Institute of Technology Karnataka Surathkal (Índia), pesquisador
independente sem afiliação/financiamento atual. Diferente da maioria dos
outros papers da coleção, este **alega uma prova completa** da
Conjectura de Collatz — mesma categoria do PDF do Santos já catalogado
em `literature/unverified-proof-claims.md`.

## Estrutura da prova alegada

O paper constrói um aparato notacional (Binary-Exponential-Ladders BEL,
operadores D#/U#, framework estruturado H) que, examinado com cuidado,
é uma reformulação do mapa de Syracuse padrão (S(n)=(3n+1)/2^v2(3n+1))
e da árvore reversa de Collatz já bem conhecida — nada estruturalmente
novo até este ponto. A "prova" then se divide em duas partes:

1. **Condição necessária** (Seção 10.1): H^s — definido como o
   componente do framework conectado ao nó-sink BEL(1) (o ciclo trivial)
   — satisfaz os axiomas de Dedekind-Peano e é order-isomórfico a N.
2. **Condição suficiente** (Seção 10.2): argumento de redução ao absurdo
   pretende mostrar que não há ciclos extras (H^∞) nem cadeias
   divergentes (H^&), isto é, H^s = H ("domain exhaustion").

## Por que a condição necessária não prova nada

H^s é **definido** como o conjunto de elementos que alcançam BEL(1) (o
componente conectado ao sink). Mostrar que "todo elemento de H^s alcança
BEL(1)" é portanto verdade por construção/definição, não uma descoberta.
Isso é contabilidade (bookkeeping), não teorema. Todo o conteúdo
matemático real da conjectura está em mostrar que H^s = H (que não há
mais nada fora de H^s) — exatamente a Seção 10.2, a condição suficiente.

## O furo lógico central (Seção 10.2.1, páginas 22-23)

O argumento: assume um ciclo hipotético X_θ (diferente do trivial); toma
seu elemento mínimo do tipo (6m-1) [resíduo 2 mod 3], chamado BEL(6k-1);
aplica a fórmula de predecessores do paper (Eqn.8) **especificamente com
v=1**, obtendo o candidato BEL(4k-1); afirma que isso "estabelece" que
BEL(4k-1)∈X_θ; e então observa que, com k=2 (o menor k satisfazendo as
restrições modulares), isso dá BEL(7) e BEL(11) — ambos conhecidos por
pertencerem à trajetória trivial (H^s), gerando a contradição desejada.

**O problema**: a fórmula de predecessores do paper para um número tipo
(6m-1) tem **infinitas soluções válidas**, uma para cada expoente ímpar
v=1,3,5,7,... — não apenas v=1. Verificamos isso computacionalmente
(`experiments/E-043-ctuhsk-cycle-proof-check/`): para n=11, os
predecessores válidos via v=1,3,5,7,9 são 7, 29, 117, 469, 1877
(confirmamos `syracuse(pred) == 11` para cada um). **Apenas v=1 dá um
valor menor que 11**; todo v≥3 dá um valor **maior**. Provamos
algebricamente que isso vale para qualquer n do tipo (6m-1), não é
coincidência do exemplo escolhido: `pred(v=1)=(2n-1)/3 < n` e
`pred(v=3)=(8n-1)/3 > n` para todo n>0.

O paper nunca justifica por que o predecessor **real, dentro do ciclo
hipotético específico**, teria que ser exatamente o de v=1 (o menor
entre infinitos candidatos). Se o predecessor real correspondesse a
qualquer v≥3, o resultado seria maior que 6k-1 — e nenhuma contradição
de minimalidade surgiria. O argumento só testa/exclui **um ramo entre
infinitos**, e declara vitória geral a partir desse único ramo.

Enquadrando de outra forma: é um argumento de "descida pelo elemento
mínimo" (técnica válida quando existe uma descida monotônica genuína) —
mas o mapa reverso de Collatz não tem essa descida garantida, então o
autor fabrica uma ao fixar v=1 arbitrariamente. Essa substituição não
justificada é o único defeito, embora apareça de duas formas
(a escolha de v=1 na Eqn.8, e a busca pelo "menor k satisfazendo as
congruências" — que são a mesma manobra vista de dois ângulos: tratar
como livre uma quantidade que na verdade é fixada pelo ciclo hipotético
desconhecido).

A Seção 10.2.2 (cadeias divergentes H^&, páginas 23-24) usa
explicitamente "exatamente o mesmo argumento reductio-ad-absurdum
banking on [Eqn.17]" (palavras do próprio paper) — portanto sofre da
mesma falha, sem necessidade de análise separada. Testamos com k=1
(BEL(3), BEL(5)) e confirmamos o mesmo padrão.

Nota lateral (não é uma segunda falha independente, apenas uma
observação de retórica): a frase do paper "a menor valor de k com
(4k-1)MOD3=1 e (6k-1)MOD3 sendo igual a 2" apresenta duas condições como
se ambas restringissem k, mas `(6k-1) mod 3 = 2` é automaticamente
verdadeiro para **todo** inteiro k (pois 6k≡0 mod 3) — só a primeira
condição é real. Isso não muda o veredito, só infla artificialmente a
aparência de rigor da derivação.

## O que está correto no paper

- A construção BEL/D#/U# e a classificação mod 6 dos números ímpares
  (Seções 2-9): reformulação correta, mas não nova, do mapa de Syracuse
  e da árvore reversa de Collatz.
- Fatos estruturais preliminares: multiplicidade de 3 nunca tem
  predecessor (Eqn.9, confirmado computacionalmente até 3000); fórmula
  de predecessores para tipos (6m-5) e (6m-1) (Eqn.7, Eqn.8, confirmadas
  computacionalmente).
- O exemplo próprio do paper (trajetória de 9: 9→7→11→17→13→5→1,
  páginas 29-30) está aritmeticamente correto e, ironicamente, é o
  mesmo par (7, 11) usado como "contradição" na Seção 10.2.1 — ambos são
  elementos triviais e bem conhecidos da trajetória padrão, não de
  nenhum ciclo hipotético.
- Declaração de afiliação/financiamento/conflito de interesses honesta
  e completa (Seção 16); nenhuma alegação de verificação formal em
  Lean/Coq (diferente de outros papers da coleção que alegaram isso sem
  verificação possível).

## Veredito

**A prova não é válida.** O mesmo padrão de erro encontrado em outras
"provas" completas da Conjectura de Collatz que já catalogamos (cf.
Santos 2018 em `literature/unverified-proof-claims.md`): uma afirmação
existencial ("existe um predecessor com tal propriedade", ou "existe uma
sequência específica de passos que funciona") é usada como se fosse uma
afirmação universal sobre o objeto hipotético genérico em questão —
exatamente o obstáculo estrutural que nenhuma prova conhecida resolveu
até hoje (ver `literature/overview-and-known-results.md`). Adicionado a
`literature/unverified-proof-claims.md` como novo item catalogado.

## Novas hipóteses?

Nenhuma. O aparato BEL/H não introduz estrutura matemática nova (é uma
reformulação notacional da árvore reversa de Collatz padrão), e a
"prova" falha no ponto exato onde seria preciso resolver o problema
original. Não há nada aqui para incorporar ao nosso banco de hipóteses
além do próprio registro do erro.

## Atualizações

- 2026-07-14: paper lido por completo (35 páginas), estrutura da prova
  analisada, furo lógico identificado e confirmado computacionalmente
  (`experiments/E-043-ctuhsk-cycle-proof-check/`). Verificado com
  `advisor()` antes de finalizar a análise. Flags atualizadas em
  `literature/papers/INDEX.md` (item 016: Lido=Sim, Corrigido=Sim,
  Implementado=Sim). Adicionado a
  `literature/unverified-proof-claims.md`.
