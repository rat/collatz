# H-132: índice de cauda no modelo iid por renovação de martingala aditiva

Status: aberta; pendente de verificação de citação primária

Criada: 2026-08-07

## Pendência (2026-08-08)

A prova depende inteiramente de invocar o Teorema 2.2 de Q. Liu (2000)
como caixa-preta, mais o uso de Jelenkovic-Olvera-Cravioto (2012) e
Chen-de Raphélis-Ma (arXiv:2408.05538) para justificar as hipóteses do
teorema. Nenhuma dessas três fontes está em `literature/`. O E-112
confirma numericamente que o problema satisfaz quatro condições, mas
essas condições são a paráfrase do Codex do que o Teorema 2.2 exige,
não uma conferência contra o artigo original. Isso é exatamente o tipo
de citação por paráfrase que a Regra 11 do CLAUDE.md proíbe, e o
`main.tex` já cita `\cite{Liu2000}` publicamente. Rebaixada de
"fechada-confirmada" para "aberta" até que as três fontes primárias
sejam obtidas e a atribuição seja checada contra o texto real.

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
