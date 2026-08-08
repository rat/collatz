# H-157: renormalização logarítmica q-ádica e crescimento exponencial

Status: fechada-confirmada após auditoria algébrica e computacional

Criada: 2026-08-07

## Hipóteses aritméticas

Seja `q` um primo ímpar, `d=ord_q(2)` e suponha

```text
v_q(2^d-1)=1.
```

Por levantamento da ordem, `ord_(q^ell)(2)=d*q^(ell-1)` para todo
`ell>=1`. A condição exclui os primos excepcionais de base dois, mas
não exige que `2` seja raiz primitiva módulo `q`.

## Teorema

Seja `mu_(q,ell)` a lei Syracuse de parâmetro `q` e peso geométrico
`P(a)=2^-a`, e defina

```text
K_(q,ell)=q^ell sum_x mu_(q,ell)(x)^2.
```

Para `M=q^(ell-1)`, coloque

```text
a_j=mu_(q,ell-1)((2^(d*j)-1)/q mod M)
A_m=sum_j a_j exp(-2*pi*i*m*j/M).
```

Então

```text
K_(q,ell)=sum_m W_(q,d)(2*pi*m/M)|A_m|^2,

W_(q,d)(theta)
 = q*(4^d-1)/(3*(4^d+1-2^(d+1)*cos(theta))).
```

O multiplicador satisfaz

```text
c_(q,d) <= W_(q,d)(theta) <= C_(q,d),
c_(q,d)=q*(2^d-1)/(3*(2^d+1)),
C_(q,d)=q*(2^d+1)/(3*(2^d-1)).
```

Como `K_(q,ell-1)=sum_m |A_m|^2`, segue que

```text
c_(q,d) K_(q,ell-1) <= K_(q,ell)
                      <= C_(q,d) K_(q,ell-1).
```

Para todo `q>=5`, temos `d>=3` e
`c_(q,d)>=35/27>1`. Portanto

```text
K_(q,ell) >= c_(q,d)^ell,
```

e a lei q-ádica não possui densidade L2. Isso fornece um expoente de
colisão positivo explícito, mais quantitativo que a singularidade já
obtida pelo argumento de entropia.

## Derivação do filtro

Na órbita `y_k=2^k mod q^ell`, escreva
`x_k=mu_(q,ell)(y_k)` e `n_k=nu_(q,ell)(y_k)`, onde `nu` é a lei de
`1+q F_(ell-1)`. A memória geométrica fornece

```text
x_k=(n_(k+1)+x_(k+1))/2.
```

Os únicos índices com `n_k` não nulo são os múltiplos de `d`, e
`n_(d*j)=a_j`. Com `u_j=x_(d*j)`, um bloco de `d` etapas dá

```text
u_j=2^-d(a_(j+1)+u_(j+1)),
x_(d*j+r)=2^r u_j, 0<=r<d.
```

Logo `sum_k x_k^2=((4^d-1)/3)sum_j u_j^2`. O filtro circular tem
multiplicador `z/(2^d-z)`. Parseval fornece a fórmula declarada.

## Verificação

E-126 compara a recursão geométrica direta e o multiplicador espectral
para `q=3,5,7,11,13,17,19`, até `ell=5`. A lista inclui ordens
multiplicativas distintas e casos em que `2` não é raiz primitiva. O
maior erro absoluto observado foi inferior a `2e-12`, em valores de
`K` que chegam a `10^4`.

A busca dirigida encontrou a recursão primária de Tao para `q=3`, mas
não encontrou a diagonalização logarítmica ou seus limites uniformes.
Isso não é uma alegação global de prioridade.

## Limite

Para `q=3`, o limite inferior do multiplicador é `3/5<1`; não se obtém
crescimento por comparação uniforme. A fórmula refinada de H-156 reduz
o caso crítico a um balanço espectral, que continua aberto. A hipótese
de levantamento maximal também deixa de fora os primos excepcionais,
nos quais o agrupamento de órbitas precisa ser modificado.
