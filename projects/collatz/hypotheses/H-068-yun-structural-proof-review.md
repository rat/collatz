# H-068 — Revisão do paper #076 (Yun, "A Structural Proof of the Collatz Conjecture via non-repeating trajectory and Recursive Decay") — ALEGAÇÃO DE PROVA refutada, três circularidades independentes

Status: revisão externa concluída — gap fatal localizado (circularidade
na "função de posto"), mais dois argumentos circulares independentes e
um erro aritmético; NÃO é uma prova válida
Criada em: 2026-07-15
Origem: item 076 da coleção (`literature/papers/INDEX.md`), já baixado
(`075_Structural-Proof-Collatz-nonrepeating.pdf`). **Alegação de prova
completa** — requer maior rigor de escrutínio (osf.io, não
peer-reviewed).

## O paper

Yun, Y.H. (2026), *A Structural Proof of the Collatz Conjecture via
non-repeating trajectory and Recursive Decay*, osf.io, 13 páginas.
Zero Theoretical Physics Lab, Seul, Coreia do Sul.

## Veredito: NÃO é uma prova válida — mais fraco que o item 049 (Boyle)

Diferente do item 049 (H-065), que tinha pelo menos UM argumento
coerente (embora inválido), este paper contém **três argumentos
circulares independentes** — cada um, sozinho, já invalida a "prova" —
além de um erro aritmético concreto num exemplo numérico.

## Gap mais grave — a "função de posto" (Seção 8, Equação 9.2)

O paper define, para fundamentar um "argumento de boa ordenação em
ZFC" (reforçado retoricamente no Apêndice A):

```
r(x) := min{n ∈ N | f^(n)(x) = 1}
```

**Esta função só está definida para valores de `x` cuja órbita já
atinge 1.** Se a órbita de algum `x` nunca atingir 1 (exatamente a
possibilidade que a conjectura precisa excluir), o conjunto
`{n : f^(n)(x)=1}` é **vazio** e não tem mínimo — `r(x)` simplesmente
não existe. Ou seja, o domínio da própria função usada no argumento de
descida bem-fundada **já pressupõe** que toda órbita atinge 1 — a
conclusão que deveria ser provada aparece embutida na definição do
objeto central da prova.

**Demonstração por analogia** (`experiments/E-068-yun-structural-proof-check/experiment.py`,
Parte 3): apliquei o mesmo estilo de definição a um mapa que
**provadamente diverge** para todo `x>0`, `g(x)=2x`. A "função de
posto" análoga `r_g(x):=min{n : g^(n)(x)=1}` fica **indefinida para
todos os 18 valores testados** (`x=2..19`) — exatamente o que
aconteceria com `r(x)` do paper se `f` não levasse todo `x` a 1. Isso
expõe que a técnica de "boa fundamentação em ZFC", embora
logicamente correta *em si mesma* (N é de fato bem-fundado), é
**vazia de conteúdo** aqui: o Apêndice A do paper ("all reasoning...
can be interpreted within ZFC... no use of... unprovable hypotheses")
é retórica sobre uma definição mal-posta, não um reforço real de rigor.

## Gap 2 — Teorema 6.1 (ausência de ciclos não-triviais)

A "prova" de que não existem ciclos não-triviais afirma: *"the only
known fixed point under iteration is `x_m=1`"* — isso é **exatamente**
a conclusão que precisa ser provada (ausência de outros ciclos),
apresentada como premissa (todo elemento de QUALQUER ciclo de
comprimento `k` é, por definição, um ponto fixo de `f^(k)`; dizer que
"o único conhecido é 1" não exclui a existência de outros). A álgebra
que segue (`(2^l-3)x_m=1`) apenas **re-deriva o Lema 6.1** (repetição
IMEDIATA, `x_n=x_{n-1}`), não trata o caso geral de ciclos de
comprimento `n-m>1` que o próprio teorema afirma cobrir.

## Gap 3 — "compressão informacional" (Seção 5/9.2.3)

O argumento de que "A e B são ambos infinitos contáveis, `f:A→B` não é
injetiva, logo por 'compressão'/princípio da casa dos pombos a
sequência deve eventualmente repetir" é uma **falácia sobre
cardinalidades infinitas**: não-injetividade entre conjuntos infinitos
contáveis não implica nada sobre convergência dinâmica de uma
sequência determinística específica — e mesmo que implicasse "alguma
repetição eventual", isso não distingue "converge para 1" de "entra em
qualquer OUTRO ciclo" (o argumento é compatível com qualquer cenário).

## Erro aritmético concreto (Equação 9.8)

O paper afirma `f(5)=(3·5+1)/2³=2` e `f(21)=(3·21+1)/2⁴=2`. Verificado
computacionalmente (Parte 2 do experimento): `3·5+1=16=2⁴` (não `2³`) e
`3·21+1=64=2⁶` (não `2⁴`). Os valores corretos são **`f(5)=f(21)=1`**,
não 2 — e note-se que 2 **nem é ímpar**, violando a própria Definição
4.1 do paper (que exige `f` mapear ímpar em ímpar). A conclusão
qualitativa pretendida pelo exemplo (`f(5)=f(21)`, demonstrando
não-injetividade) sobrevive com os valores corretos — é apenas a
aritmética mostrada que está errada.

## O que está correto no paper

**Lema 6.1** (distinção de vizinhos: `x_n≠x_{n-1}` exceto em `x_n=x_{n-1}=1`)
— álgebra correta, verificada (Parte 1): a equação `(2^k-3)x=1` tem
como única solução inteira positiva `x=1,k=2`. Este é o único ponto do
aparato formal do paper que resiste a escrutínio — mas sozinho só
exclui repetição *imediata*, não ciclos mais longos (que é justamente
o que os Gaps 2 e 3 falham em excluir).

## Busca computacional (sanity check da conclusão, não do argumento)

Busca por ciclos não-triviais do mapa comprimido `f`, `x₀=1..2.000.000`,
até 200 passos: **nenhum encontrado** — consistente com décadas de
verificação numérica já publicada (Oliveira e Silva et al., citada
pelo próprio paper). Isso não resgata os argumentos do paper — apenas
reafirma o que já era conhecido antes dele.

## Por que isso é ainda mais fraco que o item 049

O item 049 (Boyle, H-065) tinha um argumento probabilístico coerente
(embora inválido pela conflação ensemble/trajetória específica) mais
um gap secundário isolado. Este paper (076) tem **três** argumentos
estruturalmente diferentes, e **todos os três** são circulares
(assumem a conclusão de formas distintas) — não há um único argumento
coerente no cerne da "prova". A linguagem de rigor (ZFC, Axioma da
Escolha, "well-founded ordering") no Apêndice A é particularmente
enganosa: soa formal e rigorosa, mas está aplicada a uma definição
vazia.

## Novas hipóteses?

Nenhuma. Item descartado como alegação de prova inválida, com os três
gaps localizados e documentados.

## Atualizações

- 2026-07-15: paper lido por completo (13 páginas), gap fatal
  localizado (função de posto circular, Seção 8) e demonstrado por
  analogia com um mapa divergente; dois gaps circulares adicionais
  identificados (Teorema 6.1, Seção 5/9.2.3); erro aritmético
  concreto confirmado (Equação 9.8). `INDEX.md` atualizado (item 076:
  Lido=Sim, Corrigido=Não [alegação de prova refutada — três
  circularidades independentes], Implementado=Sim [partes verificáveis
  testadas]).
