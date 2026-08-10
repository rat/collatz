# H-155: decomposição multiescala de Parseval entre O5 e O7

Status: fechada-confirmada após auditoria

Criada: 2026-08-07

## Enunciado

Se `mu_ell` são leis compatíveis módulo `3^ell`, defina

```text
K_ell = 3^ell sum_x mu_ell(x)^2,
E_ell = sum_(3 does not divide xi) |mu_ell_hat(xi)|^2.
```

Então

```text
K_ell-K_(ell-1)=E_ell,
K_ell=1+sum_(r=1)^ell E_r.
```

## Prova

Por Parseval, `K_ell` é a soma de `|muhat_ell(xi)|^2` sobre todos os
caracteres módulo `3^ell`. Os caracteres com frequência divisível por
três são exatamente os pullbacks dos caracteres do nível `ell-1`; pela
compatibilidade, seus coeficientes são os coeficientes de `mu_(ell-1)`.
A contribuição deles é `K_(ell-1)`. O complemento é o conjunto das
frequências primitivas, cuja energia é `E_ell`.

Iterando, cada caráter não trivial aparece uma única vez, no seu
condutor primitivo. O caráter trivial fornece o termo inicial um.

## Consequência 3-ádica

Para uma lei em `Z_3`, o martingale de densidade no nível `ell` tem
norma L2 ao quadrado igual a `K_ell`. Logo ele converge em L2 para uma
densidade se, e somente se,

```text
sum_(ell>=1) E_ell < infinity.
```

Assim a condição L2 de O7 é exatamente a somabilidade, sobre as escalas,
da energia primitiva de dígitos novos identificada em H-154. Não são
apenas duas técnicas que usam Fourier: são as versões cumulativa e
incremental da mesma quantidade.

## Limites

A identidade não controla o maior coeficiente em uma escala nem alinha
frequências entre escalas. Portanto ela não prova a concentração
encadeada de O5. Também não decide se a soma das energias da lei de
Syracuse converge.

E-124 verifica as duas identidades nas leis de Syracuse e em uma cadeia
independente de refinamentos de Dirichlet até o nível 12.

## Atualização 2026-08-09: a ponte para O5, quantificada, e o que ela custa

Sessão dirigida a O5. Detalhe em
[`H-162`](H-162-familia-lr-orcamento-anelado-o5.md), numérica em
[`E-136`](../experiments/E-136-lr-budget-sweep-hole-chain/README.md).

**Desigualdade de cascas.** Cauchy-Schwarz dentro de cada casca de
condutor, para uma medida qualquer em `Z/3^ell Z`, sem hipótese de
compatibilidade:

```text
sum_(xi != 0) |muhat_ell(xi)|
  <= sum_(r=1)^ell sqrt(2*3^(r-1)) * sqrt(E_r^(ell)),
E_r^(ell) := sum_(cond(xi)=3^r) |muhat_ell(xi)|^2,
sum_r E_r^(ell) = K_ell - 1.
```

Combinada com "buraco implica soma `l^1` maior ou igual a 1", ela dá a
ponte pedida entre suporte e as energias multiescala. Compatibilidade
projetiva é necessária apenas para identificar `E_r^(ell)` com a energia
primitiva de nível `r` desta hipótese; a desigualdade em si vale sempre.

**Ressalva verificada, que limita o alcance.** As leis `mu_{ell,j}` da
WCC (H-114/H-127) **não** formam família projetivamente compatível.
Reduzir `mu_{ell,j}` módulo `3^(ell-1)` descarta o termo `i = ell-1` e
deixa uma marginal ponderada, com peso proporcional a `alpha_(ell-2)`,
pelo número de escolhas de `alpha_(ell-1) < alpha_(ell-2)`. Não é
`mu_(ell-1,j')` para nenhum `j'`. Logo `K_r - K_(r-1) = E_r` **não** se
aplica às leis da WCC, e a leitura telescópica fica restrita à família
projetiva 3-ádica genuína (as leis de Syracuse, onde O7 vive).

**Quanto custa fechar O5 por esta ponte.** Somabilidade não basta. A
desigualdade acima só exclui um buraco quando
`sum_r sqrt(2*3^(r-1) E_r) < 1`, e isso é uma **constante dura**, não
uma taxa: nenhuma condição assintótica sobre `E_r` sozinha basta, porque
`E_r` pequeno demais em cauda ainda deixa a soma acima de 1 se os
primeiros termos forem grandes. O que se pode dizer é a direção
necessária: `E_r` tem que decair estritamente mais rápido que `3^(-r)`.
A condição `L^2` de O7 é apenas `sum_r E_r < infinito`.

Comparação por taxa, com `theta` medido **por nível de condutor** (a
graduação desta hipótese), isto é `|muhat_ell(xi)| <= 3^(-theta*r)` para
`cond(xi) = 3^r`: então `E_r <= 2*3^(r-1) 3^(-2 theta r)`, e
`sum_r E_r < infinito` sse `theta > 1/2`, enquanto
`sum_r sqrt(2*3^(r-1) E_r) = (2/3) sum_r (3^(1-theta))^r` converge sse
`theta > 1`. Fator dois no expoente. (A versão chapada,
`|muhat_ell(xi)| <= 3^(-theta*ell)` para todo `xi != 0`, dá o mesmo par
de limiares, mas é a versão por condutor que casa com H-154/H-155 e é
essa que deve ser citada.)

A razão estrutural é banal e vale a pena dizer:
uma densidade `L^2` pode se anular num conjunto, então `L^2` nunca
força cobertura; o que forçaria é cota inferior para a densidade.

**Dependência O5-O7, registrada.** Progresso em O7 não fecha parte de
O5 mecanicamente. Se o trabalho paralelo em O7 provar
`sum_r E_r < infinito` para a lei de Syracuse, O5 segue aberto, e o
hiato que resta é exatamente o fator dois acima. A direção contrária
também não vale: as leis da WCC nem sequer são compatíveis, então nem
formam a cadeia que O7 estuda.

**Não ganha nada como norma ponderada para O5.** Avaliada no benchmark
anelado de H-127, `E_r^(ell) ~ 2*3^(r-1) p^(2r)`, e a desigualdade de
cascas reproduz o critério `3p < 1`, isto é `gamma > 3`, idêntico ao
`l^1` chapado. A Cauchy-Schwarz intra-casca é justa quando os módulos
dentro da casca são iguais, que é o que o modelo anelado supõe, então a
coincidência é estrutural. Ponderar por condutor não move o muro.
