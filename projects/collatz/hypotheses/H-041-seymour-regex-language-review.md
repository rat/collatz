# H-041 — Revisão crítica do paper #005 (Seymour, "A Regular Expression Language for the Collatz Graph")

Status: revisão externa concluída — na maior parte confirmado correto,
um erro pequeno encontrado; boa prática de honestidade epistêmica
observada
Criada em: 2026-07-14
Origem: terceiro paper priorizado da coleção (item 005, local, mesmo
autor do item 004/H-040).

## O paper

"A Regular Expression Language for the Collatz Graph" — Jon Seymour,
julho de 2026, 18 páginas, explicitamente marcado como **"WORKING
PAPER"** (marca d'água e declaração de status). É o "Paper 1" de uma
série de quatro ("architecture, tools, results, capstone"). Diferente
do item 004, este paper **separa explicitamente** o que está provado
do que é conjecturado: "Status. This is a working paper. All theorems
carry complete proofs. Results labelled *Conjecture* are stated
precisely but not yet proved."

## O que está correto (verificado independentemente)

- **Proposição 3.1** (aritmética do circuito Steiner via mapa natural
  C: α pares OE seguidos de descida par pura) — confirmada em 20.000
  casos aleatórios, sem exceção
  (`experiments/E-041-seymour-regex-language-check/`).
- **Teorema 3.6** (comprimento da corrida "7 mod 8" = v₂(n+1)−2,
  saindo sempre para classe 3) — confirmado em 50.000 casos, sem
  exceção.

## O que está incorreto (pequeno, contido)

**Corolário 2.2** (exit ping-pong mod 24): alega S^ℓ(n)≡11 mod24 se t
par, ≡23 mod24 se t ímpar. Testado em 50.000 casos: quando t é par,
bate 100%. Quando t é ímpar, o valor real observado é **sempre 11**,
nunca 23 — erro sistemático, não ocasional. A prova alega que
t↦(3t+1)/2 "preserva a paridade de t" — isso é falso em geral (t=1→2,
t=5→8, ambos pares apesar de t ímpar; a paridade do resultado depende
de t mod4, não da paridade de t). Valor correto aparente: S^ℓ(n)≡11
mod24 sempre, independentemente da paridade de t.

**Calibração importante**: este erro é pequeno e contido — o
Corolário 2.2 nem consta na lista "What is proved" da própria conclusão
do paper (só mod-8 taxonomy, Prop 3.1, Teorema 3.6, universo mod-24 e
fundamentos de grafos constam lá), sugerindo que o autor já trata esse
corolário como material mais secundário/preliminar. Não é comparável
em gravidade ao erro do item 004 (H-040), que estava no teorema central
alegadamente verificado formalmente.

## Sobre a Conjectura 5.1 (o resultado central do paper)

"Toda órbita de Collatz, codificada por resíduos mod 8, casa com
`((7*3)?(1|5))*`" — apresentada honestamente como **conjectura**, não
como teorema. Dado que já verificamos independentemente a matriz de
transição equivalente (Teorema 2.1 do paper #004/H-040 — mesma
estrutura, mesmo autor), essa conjectura parece **quase uma consequência
direta** da estrutura já confirmada (classes 1 e 5 são imediatamente
terminais; classe 3 só alcança 1 ou 5; classe 7 só alcança 3 ou 7 —
logo todo caminho a partir de qualquer resíduo eventualmente casa com
o padrão). Não a provamos formalmente nós mesmos, mas não encontramos
motivo para duvidar dela — ao contrário do que aconteceu com o teorema
do item 004.

## Novas hipóteses?

Nenhuma nova sobre a conjectura de Collatz em si. A infraestrutura
mod-8/circuitos Steiner continua sendo a mesma família de ideias já
notada em H-040 como potencialmente relacionável à nossa própria
H-007/H-014/H-022/H-028 — vale reconsiderar numa sessão futura com uma
pergunta mais concreta, não como está agora.

## Atualizações

- 2026-07-14: paper lido por completo, dois resultados centrais
  confirmados, um erro pequeno encontrado em corolário secundário.
  Flags atualizadas em `literature/papers/INDEX.md` (item 005:
  Lido=Sim, Corrigido=Sim, Implementado=Sim).
