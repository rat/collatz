# H-131 — Cobertura ponderada e a ponte correta entre WCC e beta=1

Status: fechada-confirmada; identidade de custo e insuficiência da WCC provadas
Criada em: 2026-08-07

## Enunciado

A identidade de suporte entre as somas mistas de Wirsching e a variável
de Syracuse de Tao não basta para deduzir beta=1 a partir da Weak Covering
Conjecture. A ponte exige controlar o custo geométrico das representações.

Para uma tupla `a_1,...,a_ell >= 1`, defina

`B = a_1+...+a_ell`

e

`Syrac_ell = sum_{m=1}^ell 3^(m-1) 2^-(a_1+...+a_m) mod 3^ell`.

Se `B_ell(z)` é o menor custo de uma tupla que representa a unidade `z`,
a condição mínima para obter beta=1 por uma única representação por
resíduo é

`max_z B_ell(z) <= ell log_2(3) + o(ell)`.

Uma condição mais fraca pode bastar se a soma ponderada de várias
representações também alcançar custos próximos da média canônica. O
objeto definitivo é

`c_ell = min_z sum_{a: Syrac_ell(a)=z} 2^-B(a)`.

## Motivação

O paper 01 afirma que WCC implica beta=1 por uma contagem de entropia.
A fonte primária de Tao define beta=1 por massa ponderada, enquanto WCC
é uma afirmação de cobertura não ponderada. A conversão entre orçamento
de Wirsching e custo geométrico não foi demonstrada no projeto original.

## Como testar

1. Derivar exatamente a transformação entre tuplas de Syracuse e somas
   mistas normalizadas.
2. Calcular `B_ell(z)` por DP exato e validar contra força bruta.
3. Comparar `max_z B_ell(z)` com `ell log_2(3)` e com `j*(ell)+ell`.
4. Calcular a massa ponderada completa quando viável.
5. Procurar uma desigualdade analítica que converta WCC em controle de
   custo ou construir uma família que separe as duas propriedades.

## Atualizações

- 2026-08-07: a identidade dos suportes foi confirmada, mas a ponte de
  entropia foi reaberta porque cobertura não ponderada não controla
  automaticamente a massa geométrica de Tao.
- 2026-08-07: criado E-111 para calcular o custo mínimo por resíduo por
  uma recursão independente e validá-la contra força bruta.
- 2026-08-07: E-111 passou em quatro comparações DP versus força bruta e
  encontrou, para todo `1 <= ell <= 12`, a identidade exata
  `max_z B_ell(z) = ell + j*(ell)`.

## Resultado analítico 1: identidade exata entre os dois orçamentos

Defina `C_ell(J)` como o conjunto dos valores de `Syrac_ell` produzidos
por tuplas positivas de custo total `B <= ell+J`. Então

`2^(ell+J) C_ell(J) = R_{ell-1,J} mod 3^ell`.

De fato, escreva `A_m=a_1+...+a_m` e `B=A_ell`. Após multiplicar por
`2^(ell+J)`, o expoente do termo de índice `m-1` é

`gamma_(m-1) = ell+J-A_m`.

Como cada `a_m>=1`, esses expoentes são estritamente decrescentes,
`gamma_0 <= ell+J-1` e `gamma_(ell-1)=ell+J-B>=0`. Logo a soma pertence
a `R_{ell-1,J}`. Reciprocamente, para

`ell+J-1 >= gamma_0 > ... > gamma_(ell-1) >= 0`, ponha

`A_m=ell+J-gamma_(m-1)`.

As diferenças definem `a_m>=1`, o custo final é
`B=ell+J-gamma_(ell-1)<=ell+J`, e a construção inverte a anterior.
Como multiplicar por `2^(ell+J)` permuta as unidades módulo `3^ell`,
`C_ell(J)` cobre todas as unidades se e somente se `R_{ell-1,J}` cobre.
Portanto

`max_z B_ell(z) = ell + j*(ell)`.

## Consequência para a alegação WCC implica beta=1

WCC na escala crítica daria

`j*(ell)=log_4(3) ell+o(ell)`

e, pela identidade acima,

`max_z B_ell(z)=(1+log_4(3))ell+o(ell)`.

Uma única representação por resíduo forneceria então apenas

`c_ell >= 2^(-(1+log_4(3))ell-o(ell))`

ou, na escala `c_ell=3^(-beta ell+o(ell))`,

`beta <= (1+log_4(3))/log_2(3) = 1.130929...`,

não `beta=1`. A diferença de custos é linear:

`1+log_4(3)-log_2(3) = 0.207518...`.

Assim, a contagem de uma representação usada no paper 01 não prova a
implicação. H-148 mostra que a multiplicidade ponderada restrita a esse
mesmo orçamento não pode recuperar o fator inteiro: a fatia tem massa
total exponencialmente pequena. É necessário controlar custos que se
aproximam da média canônica `2ell`.

## Resultado computacional 2: a multiplicidade recupera parte do déficit

E-111 também calcula a distribuição completa pela recursão memoryless
de Tao, validada por `c_1=1/3` e `c_2=2/63`. Definindo

`beta_eff(ell) = -log(c_ell)/(ell log 3)`, foram obtidos:

```text
ell   beta_eff   3^ell c_ell
  1    1.000000   1.000000
  2    1.570157   0.285714
  3    1.547448   0.164590
  4    1.439555   0.144916
  5    1.405113   0.108034
  6    1.364641   0.090393
  7    1.333230   0.077101
  8    1.294619   0.075067
  9    1.273890   0.066664
 10    1.254768   0.060876
 11    1.240830   0.054456
 12    1.222938   0.052915
```

A queda de `beta_eff` é compatível com `beta=1`. Ela mostra que usar
somente a representação de menor custo perde massa exponencialmente
relevante na faixa medida. Não estabelece que WCC controle essa massa.
O lema faltante deve limitar a perda de multiplicidade ponderada no pior
resíduo em uma janela que alcance custo `2ell-o(ell)`, por exemplo
provando `3^ell c_ell=exp(-o(ell))` a partir de uma propriedade
combinatória mais forte que cobertura. H-148 prova que a fatia crítica
da WCC, sozinha, tem massa insuficiente mesmo sob equidistribuição ideal.

A conjectura assintótica sobre `c_ell` foi separada como H-158. Ela não
faz parte do fechamento desta hipótese, cujo enunciado é a ponte correta
e a demonstração de que cobertura não ponderada é insuficiente.
