# H-163: rigidez por duplicação dos buracos da WCC (mecanismo sem orçamento)

Status: fechada-inconclusiva. A estrutura é exata e verificada, mas
quantitativamente fraca demais para excluir uma falha da WCC; fechá-la
exigiria a mesma estimativa anticolisão em que toda a linha está presa.

Criada em: 2026-08-09

Origem: metade (b) da tarefa sobre O5, procurar um mecanismo de exclusão
genuinamente diferente, não baseado em orçamento de Fourier, depois que
H-162 mostrou que a família `l^r` inteira está esgotada.

## A estrutura

Notação de H-114/H-127. Para `j >= 0`,

```text
S_j = { sum_{i=0}^{ell-1} 2^{alpha_i} 3^i mod 3^ell :
        j+ell-1 >= alpha_0 > alpha_1 > ... > alpha_{ell-1} >= 0 },
```

a imagem de `R_{ell-1,j}`. Todo elemento é `= 2^{alpha_{ell-1}} mod 3`,
logo `S_j` está contido nos unitários `U`. Ponha `H_j = U \ S_j` e
`j*(ell) = min { j : H_j vazio }`.

Subir todos os expoentes em uma unidade preserva a monotonicidade
estrita e custa exatamente uma casa a mais no topo. Logo

```text
S_j subset S_{j+1}   e   2 S_j subset S_{j+1}.
```

Tomando complementos dentro de `U`,

```text
H_{j+1} subset H_j interseccao 2 H_j,
H_{j+m} subset interseccao_{k=0}^{m} 2^k H_j.
```

**Consequência.** Se `b` é buraco no estágio `j+m`, então
`b, b/2, ..., b/2^m` são todos buracos no estágio `j`. Como `2` é raiz
primitiva módulo `3^ell` para todo `ell`, esses `m+1` elementos são
distintos enquanto `m < 2 * 3^{ell-1}`. Portanto

```text
|H_j| >= j*(ell) - j   para todo j < j*(ell).
```

Nenhuma transformada de Fourier aparece nisto. É contagem de suporte
mais a ação de `x -> 2x`.

## Verificação (E-136, `hole_chain.py`)

Cálculo exato de `S_j` para todo `j` de uma vez, por programação
dinâmica sobre o menor expoente máximo alcançável. Para
`ell = 2, ..., 10`, todas as afirmações passam: `S_j` dentro de `U`,
`2 S_j subset S_{j+1}`, as cadeias de metades presentes, e
`|H_j| >= j*-j`.

| ell | j* | j*/ell | `|H_{j*-1}|` | `|H_{j*-2}|` | `|H_{j*-3}|` |
|---|---|---|---|---|---|
| 4 | 7 | 1,75 | 3 | 10 | 20 |
| 5 | 9 | 1,80 | 1 | 9 | 28 |
| 6 | 10 | 1,67 | 3 | 24 | 77 |
| 7 | 11 | 1,57 | 9 | 66 | 208 |
| 8 | 12 | 1,50 | 22 | 169 | 552 |
| 9 | 13 | 1,44 | 48 | 415 | 1430 |
| 10 | 15 | 1,50 | 2 | 90 | 968 |

`j*/ell` cai nessa faixa, na direção do valor perto de `1,2` medido em
H-114 em escalas maiores.

## Por que não fecha

A cota é linear em `ell` (pois `j*` é linear em `ell`) contra
`|U| = 2 * 3^{ell-1}`. Perto do limiar ela é quase justa: em `j = j*-1`
prevê um buraco e as contagens medidas são de um dígito em todos os
níveis conferidos. Dois ou três passos abaixo ela é exponencialmente
frouxa: `2` ou `3` previstos contra centenas ou milhares observados.

Para transformar isso em exclusão faltaria uma cota **superior** para
`|H_{j-m}|` que colidisse com a inferior, e essa cota superior é
precisamente a estimativa anticolisão que a linha inteira persegue.
Registro isto explicitamente para não voltar a tentar: a rota não é
independente do obstáculo central, ela desemboca nele por outra porta.

O que a estrutura entrega, e vale guardar:

1. **Uma restrição testável, e testada, sobre o formato do conjunto de
   buracos.** Buracos vêm em progressões geométricas de razão `1/2`, e
   o comprimento da progressão cresce com a distância até `j*`. Perto do
   limiar o conjunto de buracos é essencialmente uma única cadeia de
   duplicação.
2. **Um alvo mais estreito.** Provar a WCC na margem basta provar que
   nenhuma cadeia de duplicação de comprimento `Theta(ell)` sobrevive,
   em vez de controlar `|H_j|` inteiro.
3. **Um paralelo estrutural com a Etapa 6 de H-127.** Lá o objeto com
   conteúdo era um segmento *encadeado* de escalas, não uma configuração
   solta; aqui o objeto é uma cadeia de duplicação em `j`. Nos dois
   casos o encadeamento é o que carrega a informação, e nos dois casos
   ele não é fornecido pelas ferramentas em jogo. Não afirmo que sejam o
   mesmo obstáculo, só que a forma é a mesma.

## Escopo (Regra 10b)

`2 S_j subset S_{j+1}` e suas consequências são provadas, não medidas; a
prova é a substituição de expoentes acima e não depende do cálculo. A
tabela é verificação exata em níveis finitos (`ell <= 10`), não um
resultado assintótico. Nada aqui exclui uma falha da WCC.

## Referências

- H-114 (WCC, medição de `j*/ell`), H-127 (definição de `R_{ell-1,j}`,
  Etapa 6).
- H-162 (a metade de orçamento da mesma tarefa; esta hipótese é a
  resposta à outra metade).
- E-136, `hole_chain.py`.
