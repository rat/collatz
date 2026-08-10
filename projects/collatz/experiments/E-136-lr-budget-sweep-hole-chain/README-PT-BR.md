# E-136: a família de orçamentos l^r para O5 e a estrutura de duplicação dos buracos da WCC

Hipóteses relacionadas:
[`H-164`](../../hypotheses/H-164-familia-lr-orcamento-anelado-o5.md),
[`H-165`](../../hypotheses/H-165-cadeia-duplicacao-buracos-wcc.md),
[`H-127`](../../hypotheses/H-127-reducao-z-number-dicotomia-espectral-wcc.md).

Duas partes independentes, ambas dirigidas a O5 (excluir uma falha
espectralmente difusa primitiva da Conjectura de Cobertura Fraca). A
Parte 1 pergunta se outra norma fecha o déficit de Jensen da Proposição
C. A Parte 2 testa um mecanismo do lado do suporte, sem nenhum
orçamento de Fourier dentro.

## Parte 1: `norm_sweep.py`

Mesmo modelo anelado da
[E-101](../E-101-jensen-constant-annealed-fourier-budget/README-PT-BR.md):
`Z = sum_{g>=1} w_g e(U_g)`, `U_g` i.i.d. uniformes, `w_g = p(1-p)^{g-1}`,
`p = 1/gamma`. Uma frequência de condutor `3^r` recolhe exatamente `r`
desses fatores, então `|muhat(xi)| ~ |Z|^r` no benchmark. A E-101
fornece o extremo `r -> 0` (`exp(E log|Z|) = p`, a identidade de
Jensen); este script não o recalcula, apenas o confere.

Um buraco no suporte força `sum_{xi != 0} |muhat(xi)| >= 1`. Hölder com
expoente `r >= 1` dá `||muhat||_{l^r} >= (3^ell-1)^{1/r-1}`, e o valor
anelado do lado esquerdo é `3^{ell/r} ||Z||_r^ell`. Logo o critério
fecha se, e somente se,

    ||Z||_r < 1/3.

Execução:

```sh
python3 norm_sweep.py --samples 2000000 --threshold-samples 200000
```

Leva cerca de dois minutos.

### O que é conferido e o que saiu

Autoverificações em `p_c = 1/gamma_c = 0,557886`, todas passando:

- `||Z||_2` contra a forma fechada `sqrt(p/(2-p))`, erro relativo
  `1,2e-4`;
- o limite `r -> 0` contra `p` (Jensen), erro relativo `1,0e-4`;
- o intervalo pré-registrado `p <= E|Z| <= ||Z||_2`;
- monotonicidade de `||Z||_r` em `r`.

| r | `\|\|Z\|\|_r` | déficit `D_r` | limiar gamma |
|---|---|---|---|
| 0 (Jensen) | 0,557830 | 1,8822 | 3,3079 |
| 0,5 | 0,575797 | 1,9902 | 3,7438 |
| 1 (l^1) | 0,592460 | 2,0987 | 4,1774 |
| 1,5 | 0,607812 | 2,2065 | 4,5860 |
| 2 (l^2) | 0,621902 | 2,3130 | 5,0000 |
| 3 | 0,646651 | 2,5200 | 5,8065 |
| 4 | 0,667506 | 2,7179 | 6,5986 |

`D_r = log 3 / log(1/||Z||_r)` é o fator pelo qual o expoente de
decaimento anelado fica aquém. O limiar gamma é a inclinação a partir da
qual aquele membro da família passaria a funcionar. A inclinação real é
`gamma_c = 1,7925`.

Formas fechadas confirmadas pela execução: `||Z||_2^2 = p/(2-p)`, logo o
limiar `l^2` é `p < 1/5`, isto é `gamma > 5` exatamente. O extremo
`r -> 0` é `p` exatamente, logo seu limiar nominal é `p < 1/3`, isto é
`gamma > 3`.

Segunda tabela da saída: `Lambda(p) = E log(1/|Z|)` contra `log(1/p)`.
Coincidem para `p >= 1/2` e se separam abaixo disso, porque a identidade
de Jensen exige `|Z'| <= p/(1-p)`. Em `p = 1/3`,
`Lambda = 1,032 < log 3 = 1,0986`. O verdadeiro ponto de inversão em
`r -> 0` é portanto `3,31`, não `3`.

## Parte 2: `hole_chain.py`

`S_j` é a imagem módulo `3^ell` de `sum_i 2^{alpha_i} 3^i` sobre tuplas
de expoentes estritamente decrescentes limitadas por `j+ell-1`, isto é
`R_{ell-1,j}`. `H_j = U \ S_j`, e `j*(ell)` é o menor `j` com `H_j`
vazio. Subir todos os expoentes em uma unidade custa uma casa extra no
topo, logo `2 S_j subset S_{j+1}`, e daí

    H_{j+m} subset intersection_{k=0}^{m} 2^k H_j,

de modo que um buraco no estágio `j+m` força toda a cadeia de
metades `b, b/2, ..., b/2^m` a ser de buracos no estágio `j`, dando
`|H_j| >= j*(ell) - j`.

O script calcula `S_j` para todos os `j` de uma vez, por programação
dinâmica sobre o menor expoente máximo alcançável, e depois verifica
cada afirmação.

Execução:

```sh
python3 hole_chain.py --max-level 10
```

Roda em bem menos de um segundo.

### O que saiu

Todas as verificações passam para `ell = 2, ..., 10`: `S_j` fica dentro
dos unitários, `2 S_j subset S_{j+1}`, as cadeias de metades estão
presentes, e `|H_j| >= j*-j` vale.

| ell | j* | j*/ell | `\|H_{j*-1}\|` | `\|H_{j*-2}\|` | `\|H_{j*-3}\|` |
|---|---|---|---|---|---|
| 4 | 7 | 1,75 | 3 | 10 | 20 |
| 5 | 9 | 1,80 | 1 | 9 | 28 |
| 6 | 10 | 1,67 | 3 | 24 | 77 |
| 7 | 11 | 1,57 | 9 | 66 | 208 |
| 8 | 12 | 1,50 | 22 | 169 | 552 |
| 9 | 13 | 1,44 | 48 | 415 | 1430 |
| 10 | 15 | 1,50 | 2 | 90 | 968 |

A razão `j*/ell` cai ao longo dessa faixa, coerente com o valor perto de
`1,2` reportado em H-114 em escalas maiores.

A cota inferior fica próxima em `j = j*-1`, onde prevê um buraco e as
contagens são de um dígito em todos os níveis conferidos, `2` em
`ell = 10`. Ela é exponencialmente frouxa dois ou três passos abaixo do
limiar, onde as contagens já chegam às centenas contra uma cota de `2`
ou `3`. Ou seja, a estrutura de duplicação é uma restrição real nos
últimos estágios antes da cobertura e não diz praticamente nada antes
disso.
