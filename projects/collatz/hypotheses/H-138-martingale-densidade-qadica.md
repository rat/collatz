# H-138: martingale de densidade q-ádica

Status: fechada-confirmada

Criada: 2026-08-07

## Enunciado

Se `alpha` é qualquer raiz de pressão e `U` é Haar-uniforme em `Z_q`,
então

```text
M_k(U)=Z_k(alpha; U mod q^k)
```

é um martingale não negativo de média um. Portanto converge quase
certamente para um limite finito `W_q`.

Se `mu_theta=f_q Haar+mu_s` é a decomposição de Lebesgue da medida
projetiva inclinada, o teorema de diferenciação por martingales dá

```text
W_q=f_q(U)  Haar-quase certamente.
```

Logo `W_q` é não nulo com probabilidade positiva exatamente quando a
medida tem componente absolutamente contínua. Além disso,
`E[W_q]=1` exatamente quando a medida inteira é absolutamente contínua.

## Prova

Na raiz de pressão,

```text
p_theta(a)=q^(theta-1) 2^(-theta a)
```

é uma probabilidade em `a>=1`. Para dígitos independentes com essa lei,
defina

```text
F_k=sum_(i=1)^k q^(i-1) 2^(-S_i) mod q^k.
```

A bijeção de fibras dá

```text
Z_k(theta;u)=q^k P(F_k=u).
```

Como `F_(k+1)=F_k mod q^k`, essas medidas são projetivamente
consistentes. A média de `q^(k+1)P(F_(k+1)=v)` sobre os `q` levantamentos
de `u mod q^k` é `q^k P(F_k=u)`. Esta é exatamente a propriedade de
martingale.

## Consequência para O7

A existência e a identificação do limite deixaram de ser conjecturais.
Permanecem abertas a absoluta continuidade da medida inclinada e a cauda
regularmente variável de sua densidade. O teorema de cauda i.i.d. de
H-132 não transfere automaticamente essas propriedades, pois as
subárvores aritméticas compartilham dígitos.
