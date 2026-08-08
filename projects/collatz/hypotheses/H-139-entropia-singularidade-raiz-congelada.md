# H-139: entropia e singularidade na raiz congelada

Status: fechada-confirmada

Criada: 2026-08-07

## Identidade de entropia

Em qualquer raiz de pressão `alpha`, a lei inclinada é geométrica:

```text
p_alpha(a)=(1-r)r^(a-1),  r=2^(-alpha).
```

Se `P(alpha)=log rho_ann(alpha)` e
`s(alpha)=P(alpha)-alpha P'(alpha)`, então

```text
H(p_alpha)-log(q)=s(alpha).
```

Portanto a raiz menor possui excesso de entropia sobre um dígito
q-ádico e a raiz maior possui déficit.

## Momento fracionário

Para `0<t<1`, subaditividade e a soma sobre todas as representações dão

```text
E_Haar[M_k(alpha)^t]
 <= [q^(t-1) sum_a p_alpha(a)^t]^k.
```

A derivada do logaritmo do fator em `t=1` é
`log(q)-H(p_alpha)`. Na raiz congelada ela é positiva; escolhendo
`t<1` próximo de um, o fator é menor que um. Logo o momento fracionário
tende a zero e o limite do martingale é zero Haar-quase certamente.
Pela identificação de H-138, a medida inclinada é singular.

## Alcance

Isto resolve completamente a regularidade na raiz congelada. Na raiz
menor, o sinal se inverte e a estimativa não fecha. Para momentos
`p>1`, a dificuldade é controlar a soma de pesos de representações que
colidem no mesmo resíduo. Essa é exatamente a multiplicidade ponderada
isolada em H-131. Assim O2 e O7 compartilham agora um objeto formal,
sem alegar que WCC não ponderada resolve nenhum dos dois.

