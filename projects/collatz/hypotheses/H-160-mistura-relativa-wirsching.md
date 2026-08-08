# H-160: mistura relativa na janela central de Wirsching

Status: fechada-refutada

Criada: 2026-08-08

## Alvo

Para `f_ell=S_ell...S_1 f_0`, provar ou refutar, na janela central,

```text
|S_ell f_(ell-1)-S_infty f_(ell-1)|
 <= epsilon_ell S_infty f_(ell-1),
epsilon_ell -> 0.
```

H-134 prova que esta estimativa implica a Conjectura 2 de Wirsching e
explica por que a convergência absoluta do operador não basta.

## Plano experimental

1. Medir o defeito relativo nas multiplicidades exatas de E-115.
2. Distinguir zeros de suporte de oscilações em resíduos já atingidos.
3. Aumentar a janela e o nível até onde a aritmética exata permitir.
4. Testar se o supremo decai, estabiliza ou cresce.

## Refutação

O alvo é falso já na projeção módulo `3`. Na recursão de E-115, o
resíduo final satisfaz

```text
a = (3b+1) 2^(-(J+1)) mod 3^ell,
```

onde `J` é o incremento da etapa mais nova. Logo `a mod 3` depende
somente da paridade de `J`.

Considere custos `k_ell/ell -> lambda>0`. A enumeração das composições
limitadas tem o mesmo limite local, na coordenada mais nova, que a
composição sem teto: sob o condicionamento da soma, `J` converge para
a lei geométrica

```text
P(J=j)=(1-z)z^j,  z=lambda/(1+lambda).
```

Os tetos das coordenadas antigas alteram o coeficiente por fatores
analíticos que se cancelam no quociente local; o teto da coordenada
mais nova tende a infinito. Equivalentemente, o quociente de
coeficientes para custos separados por `j` converge a `z^j`, pelo TCL
local inclinado.

Portanto as massas das duas classes de unidades módulo `3` convergem a

```text
P(J even)=1/(1+z)=(1+lambda)/(1+2lambda),
P(J odd)=z/(1+z)=lambda/(1+2lambda).
```

Haar atribui massa `1/2` a cada classe. A distância de variação total
depois dessa projeção converge a

```text
1/(2(1+2lambda)).
```

Na janela central `lambda=1`, o limite é `1/6`, e o defeito relativo
pontual não pode tender a zero. Assim a condição suficiente proposta
em H-134 é forte demais e não pode provar a Conjectura 2 de Wirsching.
Uma formulação futura terá de dividir pelo perfil grosseiro correto ou
pedir apenas um limite inferior positivo, não convergência para Haar.

## Verificação E-128

E-128 computa multiplicidades inteiras exatas até `ell=12`. Na linha
central, a distância total completa permanece próxima de `0.38`, a
colisão normalizada próxima de `2`, e ainda existem zeros. As massas
módulo `3` convergem para `1/3` e `2/3`, confirmando a obstrução acima.
O total de cada linha é confrontado com a contagem independente de
composições limitadas.
