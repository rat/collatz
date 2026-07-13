# H-012 — Estrutura de predecessores de potências de 2 na árvore reversa

Status: confirmada (prova algébrica + verificação computacional)
Criada em: 2026-07-13

## Contexto

Observação do diretor científico: explorando a árvore reversa de Collatz
(predecessores), potências de 2 como 32 e 64 se comportam de forma
qualitativamente diferente — algumas parecem mais "isoladas" (só alcançadas
via a cadeia trivial de dobramentos) que outras.

## Enunciado

Na árvore reversa de Collatz, 2^k (k≥1) tem exatamente dois predecessores
possíveis em um passo: o predecessor par trivial 2^(k+1) (sempre existe), e
um possível predecessor ímpar m=(2^k−1)/3 (só existe se for inteiro). **Esse
predecessor ímpar existe se e somente se k é par** — se k é ímpar, 2^k só é
alcançado pela cadeia trivial de dobramentos, sem nenhum outro ramo entrando
nele (é um "beco" estrutural na árvore).

## Prova

2 ≡ −1 (mod 3), logo 2^k ≡ (−1)^k (mod 3): ≡1 se k par, ≡2 se k ímpar.
Para (2^k−1)/3 ser inteiro, precisamos 2^k ≡ 1 (mod 3), ou seja, **k par**.

Para k=2j (j≥1): 2^k−1 = 4^j−1 = (4−1)(4^{j-1}+4^{j-2}+...+4+1) =
3·(soma dos j primeiros termos da progressão 4^0,4^1,...,4^{j-1}). Logo:

(2^k−1)/3 = Σ_{i=0}^{j-1} 4^i

Essa soma é sempre **ímpar** (todos os termos 4^i com i≥1 são pares; o termo
i=0 vale 1, ímpar; soma de pares + um ímpar = ímpar). Logo o predecessor é
sempre um inteiro ímpar válido quando k é par — confirmando que 2^k (k par)
sempre tem um predecessor ímpar genuíno, e 2^k (k ímpar) nunca tem.

## Conexão com H-005

Isso é essencialmente o lema de H-005 (resíduo mod 3 determinado pela
paridade da valuação) aplicado de trás para frente: como a cadeia de
2^(k-1)→2^k é uma sequência pura de duplicações (sem nenhum passo ímpar), o
resíduo mod 3 de 2^k depende só de k, alternando a cada duplicação — e só a
classe residual 1 mod 3 admite um predecessor ímpar via a fórmula
(v−1)/3.

## Verificação

Confirmado computacionalmente para k=2 até 28 (j=1 até 14): a fórmula
Σ4^i bate exatamente com (2^k−1)/3, e é sempre ímpar.

## Atualizações

- 2026-07-13: hipótese levantada a partir de observação do diretor
  científico, provada algebricamente e verificada computacionalmente no
  mesmo dia.
