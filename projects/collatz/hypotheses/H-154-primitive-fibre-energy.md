# H-154: identidade de energia primitiva por fibras novas

Status: fechada-confirmada após auditoria

Criada: 2026-08-07

## Identidade

Seja `mu` uma probabilidade em `Z/3^ell Z`, com transformada não
normalizada. Para `b mod 3^(ell-1)`, escreva

```text
x_t(b)=mu(b+t*3^(ell-1)),  t=0,1,2.
```

Então

```text
sum_(3 does not divide xi) |mu_hat(xi)|^2
 = 3^(ell-1) sum_b [
     (x_0-x_1)^2+(x_1-x_2)^2+(x_2-x_0)^2
   ].
```

## Prova

Parseval no nível `ell` dá

```text
sum_xi |mu_hat(xi)|^2 = 3^ell sum_x mu(x)^2.
```

As frequências não primitivas são `xi=3 eta`, e seus coeficientes são
os coeficientes da marginal `m(b)=x_0+x_1+x_2`. Outro uso de Parseval
subtrai

```text
3^(ell-1) sum_b m(b)^2.
```

A identidade

```text
3(x_0^2+x_1^2+x_2^2)-(x_0+x_1+x_2)^2
 = (x_0-x_1)^2+(x_1-x_2)^2+(x_2-x_0)^2
```

conclui a prova.

## Consequências

Todo coeficiente primitivo é zero se, e somente se, a lei é o
levantamento uniforme de sua marginal: os três filhos de cada fibra têm
a mesma massa. Logo existem cadeias projetivamente consistentes, com
suporte incompleto em todos os níveis e espectro primitivo zero: basta
começar com uma lei não plena em algum nível e levantá-la uniformemente.

Se `mu(x)=n_x/T` vem de contagens inteiras e alguma fibra não é uniforme,
a soma dos três quadrados de diferenças de contagens é pelo menos dois.
Como há `2*3^(ell-1)` frequências primitivas, a identidade implica

```text
max_(3 does not divide xi) |mu_hat(xi)| >= 1/T.
```

A cota é atingida pela lei uniforme sobre todos os pontos menos um.

## Alcance para O5

Compatibilidade entre níveis e buracos de suporte não implicam
`SC_prim`. O ingrediente exato é desequilíbrio dentro de fibras novas.
Mesmo energia positiva não fornece a cota exponencial forte exigida por
`SC_prim(epsilon)` sem uma estimativa quantitativa adicional. O alvo
encadeado continua aberto, agora com uma variável intermediária exata:
energia de dígito novo em escalas consecutivas.

E-123 verifica a identidade e os casos extremos numericamente até o
nível 8.
