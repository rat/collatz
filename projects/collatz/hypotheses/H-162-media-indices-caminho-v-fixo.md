# H-162: cancelamento diagonal pela média sobre índices de caminho, com v fixo

Status: backlog

Criada: 2026-08-09

Origem: surgiu de E-133 (Regra 8e), enquanto se delimitava o alcance do
cancelamento do funcional diagonal registrado na atualização de H-159.

## Enunciado

E-133 mostra que o coeficiente de Fourier diagonal
`D(xi) = E[e_{3^s}(xi(X-Y))]` de um par de folhas irmãs se anula em
toda frequência primitiva acima do condutor `3^(1+v3(k))`, e continua
anulado depois de agregar sobre a medida de ramificação em `Delta`.
Mas a esperança ali é sobre o **parâmetro aritmético livre** `t`, que é
a aleatoriedade postulada por `thm:fresh-digit-coupling`.

O que O1 precisa é outra coisa. Para um inteiro `v` fixo não existe `t`
variando: o produto `S_1(xi) conj(S_2(xi))` de um par de caminhos é uma
única fase de módulo 1, e o cancelamento tem que vir da soma sobre os
dois índices de caminho dentro de cada subárvore, com os pesos reais de
ramo.

A hipótese: para `v` fixo, a soma
`sum_{xi != 0} S_1(xi) conj(S_2(xi))` sobre pares de caminhos exibe o
mesmo tipo de cancelamento, com a ressonância confinada aos modos de
condutor pequeno, depois de removidos os modos afins grosseiros.

## Por que vale investigar

O resultado de E-133 é forte no modelo em que foi provado e diz onde a
ressonância mora (condutor `3^(1+v3(k))`, e o peso de ramificação dos
gaps ressonantes é `4^(1-3^(s-1))`). Se a mesma localização de condutor
valer para a média sobre índices de caminho, e não só sobre o parâmetro
livre, O1 muda de natureza. Se não valer, a diferença entre as duas
médias é ela própria uma descrição limpa da barreira, no mesmo estilo
dos outros resultados do paper.

## Primeiro passo barato

Enumerar, para alguns `v` fixos pequenos e profundidade moderada, as
duas subárvores irmãs completas, formar `S_i(xi)` com os pesos de ramo,
e medir `|sum_{xi primitivo} S_1 conj(S_2)|` contra a linha de base de
fase aleatória, por escala e por condutor. Comparar a localização
observada com a previsão `3^(1+v3(k))` de E-133.

## Relações

Dívida deixada em aberto por H-159 depois de E-133. Toca O1 diretamente
e O7 por meio de H-159. O funcional é o mesmo que
`thm:multiscale-parseval` (H-155) e `prop:primitive-fibre-energy`
(H-154) consomem.

## Nota de numeração

Criada durante trabalho paralelo em worktree isolado. Se outro ramo
tiver usado `H-162` ao mesmo tempo, renumerar na integração.
