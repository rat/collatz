# E-050 — Verificação do paper #008 (Ruiz Castillo, "Dissipative Bounds and Residual Decomposition")

## Objetivo

Verificar "Dissipative Bounds and Ruiz Castillo Residual Decomposition
in the Accelerated Dynamics of the Collatz Conjecture" (Juan Carlos
Ruiz Castillo, University of San Carlos of Guatemala, 44 páginas).
Segundo paper deste autor revisado na coleção (o primeiro foi item 001,
H-039). Não alega prova: "The present work does not claim to assert a
final proof of the Collatz Conjecture."

## O que fizemos

Verificamos computacionalmente todas as proposições/teoremas centrais:

1. **Identidade afim exata** U^k(n)=(3^k n+B_k(n))/2^{A_k(n)} e fórmula
   fechada de B_k(n) (Proposições 3.1/3.3): confirmadas exatamente para
   44 valores de n × 6 valores de k.
2. **Decomposição residual** U^k(n)=2^{L_k(n)}n+R_k(n) (Teorema 4.3):
   confirmada.
3. **Não-existência de equilíbrio exato** (Proposição 2.14): confirmada
   (checagem de sanidade, já garantida por fatoração única).
4. **Sensibilidade à ordem** (Proposição 5.5): confirmado que as
   palavras (1,3) e (3,1) — mesma soma A₂=4 — dão R₂=5/16 e R₂=11/16
   respectivamente, exatamente como o paper afirma.
5. **Cota universal** R_k(n)≤(3/2)^k−1 (Proposição 7.1): confirmada.
6. **Critério de descida** (Teorema 8.7): confirmado — com uma nota
   importante abaixo.

## Nota de integridade: falso positivo na primeira tentativa

A primeira verificação do Teorema 8.7 usando `2**(k*log2(3)-A_k)` via
ponto flutuante do Python encontrou 3 "falhas", todas em n=1 (o ponto
fixo, onde U^k(1)=1 para todo k). Investigamos antes de reportar como
erro: usando aritmética exata (`2^{L_k(n)} = 3^k/2^{A_k(n)}`, uma
fração exata, evitando `log2(3)` em ponto flutuante), as 3 "falhas"
desaparecem — eram um artefato de arredondamento bem no limiar da
desigualdade (onde ambos os lados são exatamente iguais a n), não um
erro do paper. O teorema está correto; o bug era no nosso código de
verificação, corrigido antes de reportar.

## Resultado

**Nenhum erro real encontrado.** O paper é matematicamente correto em
tudo que verificamos, mas o conteúdo é inteiramente **elementar**: a
"identidade afim exata" é o mesmo "desenrolar" padrão do mapa acelerado
que aparece (com notação diferente) em vários outros papers já
revisados (Fu-Liu-Wang E-044, Mohammed E-045), e as "cotas dissipativas"
são séries geométricas elementares.

**Zero conteúdo numérico real**: ambas as figuras do paper são
explicitamente rotuladas "conceptual... does not represent real
computational data" — mesmo padrão do primeiro paper Ruiz Castillo
(H-039: "zero conteúdo numérico, única figura explicitamente
conceptual").

**Padrão de citação**: 4 referências externas reais (Lagarias ×2,
Wirsching, Tao) e 12 autocitações do próprio Ruiz Castillo (75%
autocitação) — a lista revela ~12 outros papers com títulos quase
idênticos já escritos pelo mesmo autor sobre a mesma "decomposição
residual", forte indício de que os demais papers Ruiz Castillo ainda
na fila (itens 010, 013, 017, 020) seguirão o mesmo padrão.

Ver `hypotheses/H-050-ruiz-castillo-dissipative-bounds-review.md`.

## Como rodar

```
/home/rat/.venv/bin/python3 experiment.py
```
