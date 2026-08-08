# H-132: índice de cauda no modelo iid por renovação de martingala aditiva

Status: fechada-confirmada; citação primária conferida

Criada: 2026-08-07

## Verificação contra as fontes primárias (2026-08-08)

As três fontes foram obtidas e arquivadas em
`literature/papers/145` a `147` (ver `literature/papers/INDEX.md`).

O Teorema 2.2 de Liu (2000, p. 270) diz, textualmente: supondo que para
algum `chi>1`, `E[sum A_i^chi]=1`, `E[sum A_i^chi log+ A_i]<infinity` e
`E[(sum A_i)^chi]<infinity`, se a cascata é não reticulada então
`lim x^chi P(Z>x)` existe e é estritamente positivo e finito. As quatro
condições listadas abaixo em "Resultado" traduzem essas hipóteses para
a notação de pressão deste projeto: a condição 2 (`kappa>1`,
`psi(kappa)=0`) é exatamente `E[sum A_i^chi]=1` com `chi=kappa`, via
`A_i=rho_ann(theta)^(-1) exp(-theta B_i)` e `psi(s)=log rho_ann(theta s)`;
a condição 4 é a definição de "não reticulada" do artigo; a condição 3
segue porque `rho_ann` é racional em `2^t`, logo analítica sem polos em
qualquer vizinhança compacta de `[1,kappa]`, o que dá finitude de todos
os momentos ali; a condição 1 é o pré-requisito de não degenerescência
do Teorema 2.0 do mesmo artigo, necessário antes de aplicar o Teorema 2.2.

Confirmação independente: Chen, de Raphélis e Ma (arXiv:2408.05538,
p. 2) enunciam as mesmas quatro hipóteses (lá chamadas Assumption 1-4)
e atribuem a mesma fórmula de cauda `P(W_infinity>=x)~C_0 x^(-kappa)`
diretamente ao Teorema 2.2 de [Liu00], na mesma correspondência.

Jelenkovic e Olvera-Cravioto (2012, abstract) confirmam a caracterização
de H-132: o artigo trata da recursão aditiva `R=sum C_i R_i+Q` com
pesos reais quaisquer, generalização de um resultado anterior dos
mesmos autores para pesos não negativos; não é sobre o caso homogêneo
puro relevante aqui, consistente com "não foi usada sozinha para
justificar o caso homogêneo" abaixo.

Nenhuma discrepância encontrada. Restaurada de "aberta" para
"fechada-confirmada".

## Pergunta

O índice `alpha_plus(q)/alpha_minus(q)` de O7 é apenas uma previsão da
equação de pressão, ou é um teorema para a martingala do modelo iid?

## Resultado

É um teorema no modelo iid. Escreva `theta=alpha_minus(q)` e normalize a
marcha ramificada de modo que seus pesos de primeira geração sejam
`exp(-V(u))`. Sua transformada log-Laplace é

```text
psi(s) = log rho_ann(theta*s),
rho_ann(t) = q^(t-1)/(2^t-1).
```

Logo `psi(1)=0`. O segundo zero é
`kappa=alpha_plus(q)/alpha_minus(q)`.

As hipóteses do teorema de cauda para a martingala aditiva são satisfeitas:

1. `psi'(1)=theta P'(theta)<0`, pois `theta` é a raiz menor da pressão.
2. `kappa>1` e `psi(kappa)=0`.
3. Os ramos de cada tipo formam progressões geométricas. Há finitos tipos.
   Assim, a transformada é finita numa vizinhança compacta de
   `[1,kappa]`, e as somas ponderadas por potências de `1+|V|` têm todos os
   momentos necessários.
4. O grupo aditivo fechado gerado pelos deslocamentos contém
   `theta*log(2)` e `theta*log(q)`. Como `q` é ímpar, a razão
   `log(q)/log(2)` é irracional: uma igualdade racional implicaria
   `q^n=2^m`, impossível pela fatoração única. O grupo é denso, que é a
   condição não reticulada para a renovação por convoluções.

Portanto existe `C_q` estritamente positiva tal que, no modelo iid,

```text
P(W_infinity > x) ~ C_q x^(-kappa).
```

O congelamento da raiz maior no problema quenched não invalida este teorema
de cauda da martingala aditiva. São afirmações diferentes. A frase atual do
paper segundo a qual a pressão não estabelece o índice nem no modelo iid deve
ser corrigida.

## Fontes primárias auditadas

- Q. Liu, *On generalized multiplicative cascades*, Stochastic Processes and
  their Applications 86 (2000), 263-286, Teorema 2.2.
- X. Chen, L. de Raphélis e H. Ma, *Branching random walk conditioned on large
  martingale limit*, arXiv:2408.05538, hipóteses 1 a 4 e a fórmula de cauda
  atribuída ao Teorema 2.2 de Liu.
- P. Jelenkovic e M. Olvera-Cravioto, *Implicit Renewal Theorem for Trees with
  General Weights*, SPA 122 (2012), 3209-3238. Esta fonte aceita infinitos
  filhos, mas sua aplicação pronta à recursão linear inclui um termo aditivo;
  ela não foi usada sozinha para justificar o caso homogêneo.

## Limite do resultado

O `W_u` de uma raiz aritmética fixa ainda não é uma martingala de uma lei de
reprodução iid. A passagem exige a independência ou mistura quantitativa dos
dígitos novos em subárvores irmãs, isto é, O1. Assim O7 fica decomposto em:

- O7-iid: resolvido;
- O7-aritmético: aberto, condicionado à transferência iid para a árvore real.

A transferência aritmética foi separada como H-159.

Verificação algébrica: `experiments/E-112-iid-tail-theorem/`.
