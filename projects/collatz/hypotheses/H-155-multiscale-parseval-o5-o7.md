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
