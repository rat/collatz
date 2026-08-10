# H-164: a família de orçamentos l^r para O5, e por que a norma não é a variável livre

Status: fechada-refutada (a hipótese testada era "outra norma fecha o
hiato de 1,88"; ela é falsa, e falsa por uma razão exata)

Criada em: 2026-08-09

Origem: tarefa dirigida sobre O5. A rota de Jensen (H-127, Proposição
C / `thm:jensen`) fecha um mecanismo específico, o orçamento anelado
`l^1` sobre um buraco difuso, com déficit de fator 1,88. A pergunta era
se um orçamento mais apertado, ou em outra norma (`l^2`, ou uma norma
ponderada casada com a decomposição multiescala de H-155), fecharia
esse hiato.

## Enunciado

Modelo anelado de H-127/E-101: `Z = sum_{g>=1} w_g e(U_g)`, fases
i.i.d. uniformes, pesos geométricos `w_g = p(1-p)^{g-1}`, `p = 1/gamma`.
Uma frequência de condutor `3^r` recolhe exatamente `r` desses fatores,
porque em

```text
muhat(xi) = E e( sum_i xi 2^{alpha_i} 3^{i-ell} )
```

os termos com `i >= r` são inteiros quando `xi = 3^{ell-r} xi_0` com
`3` não dividindo `xi_0`. Logo `|muhat(xi)| ~ |Z|^{cond-level(xi)}` no
benchmark, e a graduação por condutor (a mesma de H-154/H-155) é a
graduação natural do modelo, não uma escolha.

**Proposição (colapso da família).** Um buraco no suporte força
`sum_{xi != 0} |muhat(xi)| >= 1`. Para `r >= 1`, Hölder dá

```text
||muhat||_{l^r(xi != 0)} >= (3^ell - 1)^{1/r - 1},
```

e o valor anelado do lado esquerdo é `3^{ell/r} ||Z||_r^ell` (a casca de
condutor máximo domina sempre que `3 ||Z||_r^r > 1`). O critério fecha
se, e somente se,

```text
||Z||_r < 1/3,
```

**independente de `r`**. Como `||Z||_r` é não decrescente em `r`, o
melhor membro da família é `r = 1`, e o limite `r -> 0`, que é
exatamente `exp(E log|Z|) = p`, o expoente de Jensen da Proposição C, é
cota inferior estrita para todos eles.

## Consequências numéricas (E-136)

Em `p_c = 1/gamma_c = 0,557886`, com `D_r := log 3 / log(1/||Z||_r)` o
fator de déficit no expoente:

| r | `||Z||_r` | `D_r` | inclinação gamma necessária |
|---|---|---|---|
| 0 (Jensen, ideal) | 0,557886 (exato) | 1,882 | 3,31 |
| 1 (`l^1`) | 0,592460 | 2,099 | 4,18 |
| 2 (`l^2`) | 0,621975 (exato) | 2,313 | 5 (exato) |
| 4 | 0,667506 | 2,718 | 6,60 |

Duas formas fechadas, sem Monte Carlo: `||Z||_2^2 = p/(2-p)` (as fases
são independentes, os termos cruzados somem), logo o critério `l^2` é
`p < 1/5`, isto é `gamma > 5`; e `lim_{r->0} ||Z||_r = p` pela
identidade de Jensen. A inclinação real é `gamma_c = 1,7925`.

**Passar de `l^1` para `l^2` piora o limiar de `3` para `5`.** O hiato
de 1,88 não é um artefato da norma escolhida; a norma escolhida já era a
melhor da família.

## Correção à Proposição C, na direção favorável à barreira

A identidade `Lambda = log(1/p)` exige `p >= 1/2` (é a condição
`|Z'| <= p/(1-p)` do `thm:jensen`). Abaixo de `p = 1/2`, a fórmula de
Jensen com zeros dentro do disco dá

```text
E log|Z| = log p + E log^+((1-p)|Z'|/p) >= log p,
```

isto é `Lambda(p) <= log(1/p)`, com desigualdade estrita. Então o ponto
em que o critério anelado inverteria **não** é `gamma = 3`: é a solução
de `Lambda(gamma^{-1}) = log 3`, medida em `gamma = 3,31` (E-136). Em
`p = 1/3` a medição dá `Lambda = 1,032 < log 3 = 1,0986`.

O `main.tex` afirma hoje "The annealed criterion would only invert at
$\gamma=3$ ($j\ge 2\ell$)". Isso subestima a barreira. A correção é
"`gamma >= 3`, e numericamente `3,31`", ou simplesmente `gamma > 3`. Não
editei o manuscrito (outro agente pode estar nele); registrado aqui para
o diretor científico decidir.

## Norma ponderada casada com H-155: mesmo muro, exatamente

Cauchy-Schwarz dentro de cada casca de condutor, sem hipótese nenhuma
sobre a medida, dá

```text
sum_{xi != 0} |muhat_ell(xi)|
  <= sum_{r=1}^{ell} sqrt(2 * 3^{r-1}) * sqrt(E_r^{(ell)}),
E_r^{(ell)} := sum_{cond(xi)=3^r} |muhat_ell(xi)|^2,
sum_r E_r^{(ell)} = K_ell - 1.
```

Avaliando no modelo anelado, `E_r^{(ell)} ~ 2*3^{r-1} p^{2r}`, e a soma
vira `(2/3) sum_r (3p)^r`. O critério é `3p < 1`, isto é `gamma > 3`:
**exatamente o mesmo limiar do `l^1` chapado**, sem ganho algum. A
Cauchy-Schwarz intra-casca é justa precisamente quando os coeficientes
da casca têm módulos iguais, que é o que o modelo anelado supõe, então a
coincidência é estrutural, não numérica.

Uma ressalva que importa: a identidade `K_r - K_{r-1} = E_r` de H-155
exige compatibilidade projetiva, e as leis `mu_{ell,j}` da WCC **não**
formam uma família compatível. Reduzir `mu_{ell,j}` módulo `3^{ell-1}`
descarta o termo `i = ell-1` e deixa uma marginal ponderada, não
`mu_{ell-1,j'}`: o peso de uma `(ell-1)`-tupla é proporcional a
`alpha_{ell-2}`, pelo número de escolhas de `alpha_{ell-1} <
alpha_{ell-2}`. A desigualdade de cascas acima vale para qualquer
medida isolada; só a leitura telescópica em termos das energias de nível
de H-155 fica restrita à família projetiva 3-ádica genuína.

## Onde a família não fecha, e o que sobra

O buraco é a condição `mu(b) = 0`, e

```text
1 = | sum_{xi != 0} muhat(xi) e(-xi b/N) | <= sum_{xi != 0} |muhat(xi)|
```

usa apenas desigualdade triangular. Entre todos os funcionais que
dependem só dos módulos `(|muhat(xi)|)`, `sum |muhat(xi)| >= 1` é o mais
forte válido: dado qualquer perfil de módulos com soma 1, existem fases
que anulam a inversão em `b`. Logo todo orçamento com expoente maior ou
peso qualquer é relaxamento estrito de `l^1`, e a família inteira está
esgotada.

O que **não** está excluído, e é o único lugar onde procurar:

1. **Argumentos que usam a positividade de `mu`.** A construção de fases
   acima ignora `mu >= 0`. Majorantes não negativos (produtos de Riesz
   como majorante, Turán, Beurling-Selberg) usam exatamente a informação
   descartada aqui.
2. **Separação em arcos maiores e menores.** Hölder sobre todas as
   frequências não exclui tratar um conjunto pequeno de frequências
   ruins à parte. Que a versão por cascas caia no mesmo muro é evidência
   de que as separações naturais (por condutor) não ajudam, mas não
   fecha a questão para separações aritméticas.
3. **A informação de fase aritmética.** É a mesma conclusão de H-149 e
   H-154 por outro caminho: estrutura aritmética além da existência de
   um buraco é indispensável.

## Escopo (Regra 10b)

Isto é um resultado negativo dentro do benchmark anelado, calculado, não
provado sobre a lei verdadeira. O que fica estabelecido: dentro do
modelo anelado de produto, nenhum orçamento `l^r` não ponderado sobre o
conjunto completo de frequências fecha, e a separação por condutor dá o
limiar idêntico. O que **não** fica estabelecido: que nenhum argumento
`l^r` funcione. H-135 (achado 3) já obrigou esta linha a recuar de uma
alegação desse tipo uma vez; a fronteira acima é o enunciado honesto.

As partes exatas, independentes de Monte Carlo: o critério
`||Z||_r < 1/3`; a monotonicidade em `r`; `||Z||_2^2 = p/(2-p)` e o
limiar `gamma = 5`; `Lambda(p) <= log(1/p)` e portanto ponto de inversão
`gamma >= 3`; a maximalidade de `l^1` entre funcionais só de módulos. O
Monte Carlo fornece `E|Z| = 0,5925`, `D_1 = 2,099` e o valor `3,31`, e é
refinamento, não sustentação. O intervalo `p <= E|Z| <= ||Z||_2` já
dava `D_1` em `(1,883; 2,314)` antes de rodar qualquer coisa.

## Dependência O5-O7 (registrada, ver também H-155)

Progresso em O7 **não** fecha parte de O5 mecanicamente. Meça o
decaimento **por nível de condutor**, a graduação de H-154/H-155:
`|muhat_ell(xi)| <= 3^{-theta r}` para `cond(xi) = 3^r`. Então
`E_r <= 2*3^{r-1} 3^{-2 theta r}`, e a densidade `L^2` de O7
(`sum_r E_r < infinito`) pede `theta > 1/2`, enquanto a desigualdade de
cascas, `sum_r sqrt(2*3^{r-1} E_r) = (2/3) sum_r (3^{1-theta})^r`, pede
`theta > 1`. Fator dois. (A versão chapada `3^{-theta ell}` sobre todo
`xi != 0` dá o mesmo par de limiares; cito a versão por condutor porque
é a que casa com a graduação.) Sem passar por taxa, a exclusão de buraco
exige `sum_r sqrt(2*3^{r-1} E_r) < 1`, uma constante dura: nenhuma
condição assintótica sobre `E_r` sozinha basta, só se pode dizer que
`E_r` precisa decair estritamente mais rápido que `3^{-r}`.
Estruturalmente é óbvio: uma
densidade `L^2` pode se anular num conjunto, então `L^2` não força
cobertura; o que forçaria é cota inferior para a densidade. Se o agente
de O7 provar `sum_r E_r < infinito` para Syracuse, O5 segue aberto.

## Referências

- H-127, Proposição C e `thm:jensen`, mais E-101 (extremo `r -> 0`).
- H-135, achado 3 (o recuo anterior que fixa o escopo permitido).
- H-149, H-154, H-155 (graduação por condutor, energia primitiva).
- H-126 (precedente de orçamento `L^infinito`/`L^2` por nível primitivo,
  para outro objeto: a covariância de agregados irmãos, não o buraco).
- E-136, `norm_sweep.py`.
