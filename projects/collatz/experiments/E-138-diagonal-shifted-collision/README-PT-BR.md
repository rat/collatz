# E-138: termo diagonal da decomposição em colisões deslocadas

Hipóteses relacionadas: H-157 (renormalização logarítmica q-ádica), H-156,
H-155, H-159 (transferência aritmética da cauda iid), H-161 (mesmo mapa
afim, pergunta diferente).

## O que isto testa

Escreva `mu_(q,ell)` para a lei de Syracuse de parâmetro `q` com peso
geométrico `P(a)=2^-a`, e `K_(q,ell) = q^ell sum_x mu_(q,ell)(x)^2`.

Condicione no primeiro expoente. Com `F_ell = 2^-a (1 + q F_(ell-1))` e
`Y = 1 + q F_(ell-1) mod q^ell`, duas cópias independentes colidem
exatamente quando `Y' = 2^(a'-a) Y`. Os expoentes são geométricos iid em
`{1,2,...}`, logo `P[a'-a = s] = 2^-|s| / 3` e

```text
K_(q,ell) = (q/3) sum_(s in Z) 2^-|s| H_(ell-1)(s),
H_(ell-1)(s) = q^(ell-1) P[Y' = 2^s Y mod q^ell],
H_(ell-1)(0) = K_(q,ell-1).
```

Cada `H` é uma probabilidade vezes uma constante positiva, então todo termo
é não negativo. Esta é a dual de Fourier de H-156 e H-157: a transformada de
`2^-|s|` no subgrupo gerado por `2^d` é exatamente o multiplicador `W_(q,d)`
de H-157, e `q/3` é a média dele no círculo. O que a forma no domínio do
tempo acrescenta é a não negatividade termo a termo, que a forma espectral
esconde dentro de um balanço com sinais.

Descartando todo `s != 0` sai a taxa incondicional

```text
K_(q,ell) >= (q/3) K_(q,ell-1)    para todo ell >= 1.
```

A desigualdade já vale em `ell=1`, onde `F_0 = 0` e `Y = 1` é
determinístico, logo `H_0(s) = [d | s]` e a identidade dá a forma fechada
`K_(q,1) = (q/3) (2^d+1)/(2^d-1)`, conferida contra a lei em todo `q`
testado. Com a base `K_(q,0) = 1` (lei trivial módulo `q^0 = 1`), iterar dá
`K_(q,ell) >= (q/3)^ell`.

Três linhas, sem Parseval, sem estrutura de órbita e sem a hipótese de
levantamento maximal `v_q(2^d-1)=1`. Como `c_(q,d) = (q/3) (2^d-1)/(2^d+1) <
q/3` para todo `d`, isto melhora estritamente a constante de H-157, e além
disso cobre os primos excepcionais (de Wieferich) e os `q` ímpares
compostos, ambos excluídos por H-157. A taxa fica dentro do próprio
intervalo `[c_(q,d), C_(q,d)]` de H-157, então não contradiz nada de lá.

## Scripts

```sh
python3 diagonal_rate.py            # identidade e a taxa q/3, vários q
python3 q3_shifted_profile.py       # q=3: o incremento E_ell e o mínimo sobre estados afins
python3 affine_transfer.py          # operador de transferência afim exato e um certificado que falha
```

`diagonal_rate.py` constrói a lei pela convolução direta
`mu_ell(y) = sum_(a>=1) 2^-a nu(2^a y)`, sem hipótese sobre a órbita de 2,
de modo que `q` composto e levantamento não maximal são entradas válidas.

## O que sai

`diagonal_rate.py`, para `q` em `{3,5,7,9,11,13,15,21,25}` até módulo 2e6: a
identidade vale com erro absoluto de no máximo `2,3e-13`, e a razão
`K_(q,ell)/K_(q,ell-1)` nunca fica abaixo de `q/3` (menor excesso observado
`8,0e-9`, em `q=25`, onde o primeiro deslocamento fora da diagonal com massa
é `s=20`). A razão desce para `q/3` por cima, então a cota não é só válida,
é assintoticamente exata:

```text
q=5  (q/3=1,666667, H-157 dá 1,470588):  1,7238; 1,6962; 1,6814; ...; 1,6688 em ell=8
q=7  (q/3=2,333333, H-157 dá 1,814815):  2,4187; 2,3701; 2,3463; ...; 2,3352 em ell=6
q=11 (q/3=3,666667, H-157 dá 3,659512):  3,6671; 3,6667; 3,6667; 3,6667 em ell=5
```

Para `q=3` a taxa é `q/3 = 1`, então ela dá monotonicidade de `K_ell` e nada
além disso. Monotonicidade já é conhecida (H-155 escreve o incremento como
soma de quadrados; H-140 a registra como segundo momento de martingala),
logo em `q=3` o termo diagonal não traz informação nova.

`q3_shifted_profile.py` dá o que é novo em `q=3`, a forma explícita do
incremento. Com `G_(ell-1)(r) = H_(ell-1)(2r)`,

```text
E_ell = K_ell - K_(ell-1) = 2 sum_(r>=1) 4^-r G_(ell-1)(r) >= (1/2) G_(ell-1)(1),
G_(ell-1)(1) = T_(ell-1)(4,1),   T_ell(u,v) = 3^ell P[F' = u F + v mod 3^ell].
```

Medido:

```text
ell   K_ell      E_ell      G(1)      G(2)      G(3)     (1/2)G(1)
  4   3,068646   0,464214   0,70303   0,49512   1,33461   0,351515
  8   4,931742   0,465921   0,71709   0,47605   1,24238   0,358544
 12   6,802899   0,468941   0,72427   0,47333   1,23741   0,362133
```

Assim a margem uniforme que falta em `q=3` se reduz a uma única afirmação
aritmética: uma cota inferior positiva, uniforme no nível, para a colisão
deslocada afim `T_ell(4,1)`. Não há cancelamento envolvido, só positividade.
O valor observado sobe devagar até `0,724` em `ell=12`; `0,5 * 0,72` daria
`K_ell >= K_1 + 0,36 (ell-1)`.

O mesmo script varre todos os estados afins. Sobre todas as unidades `u` e
todos os `v`,

```text
ell        1        2        3        4        5        6        7        8
min T   0,3333   0,2449   0,2137   0,2023   0,1961   0,1930   0,1915   0,1911
```

O mínimo cai e achata perto de `0,191`, o que é evidência, não prova, de que
`inf_ell inf_(u,v) T_ell(u,v) > 0`. Essa afirmação sozinha fecharia a margem
de `q=3`.

## Duas rotas que falharam

`affine_transfer.py` valida, em aritmética racional exata nos níveis 1, 2 e
3, a recursão independente do nível

```text
T_ell(u,v) = 3 sum_(a,a'>=1) 2^-(a+a') T_(ell-1)(w, (w + v 2^a' - 1)/3),
w = u 2^(a'-a),   sobre os pares com 3 | (w + v 2^a' - 1),   T_0 = 1.
```

Rota A, indução em `ell`. O operador é monótono, então `T_2 >= T_1` em todo
estado daria `T_ell >= T_1(4,1) = 2/3` para todo `ell` e fecharia a questão.
É falso: 22 dos 54 estados módulo 9 têm `T_2 < T_1`, por exemplo
`T_2(1,1) = 24/49 < 2/3`. O estado alvo em si está bem
(`T_1(4,1) = 2/3`, `T_2(4,1) = 34/49`), quem não funciona é a indução.

Rota B, certificado sub-invariante em resolução finita. Uma função `h` de
`(u,v) mod 3^k` com `0 <= h <= 1` e `(Th) >= h` em todo levantamento daria
`T_ell >= h` por indução a partir de `T_0 = 1`. O maior `h` desse tipo é o
limite de `h <- min(h, T_* h)` partindo de `h = 1`, com `T_*` minimizando
sobre levantamentos. Ele colapsa geometricamente: cerca de `0,79` por rodada
em `k=1`, cerca de `0,88` em `k=2`. Refinar `k` melhora a taxa, mas a razão
estrutural da perda continua, porque o `min` sobre levantamentos deixa um
adversário reescolher o pior levantamento em cada nível, sem consistência
entre níveis, coisa que a dinâmica real proíbe. Não existe certificado desse
formato em `k=1` nem em `k=2`.

## O que isto não mostra

`K_ell -> infinito` equivale a a martingala de densidade ser ilimitada em
`L^2` (H-155), o que exclui densidade `L^2`. Não prova por si só que a
medida limite é singular; isso exigiria não integrabilidade uniforme em
`L^1`, que não está estabelecida aqui.

A taxa `q/3` vale para todo `q` ímpar, primo ou composto. O passo de
divergência para "sem densidade `L^2`" passa pela decomposição de Parseval
de H-155, enunciada para módulo primo, e não foi conferido se o bookkeeping
de condutores de caractere dela sobrevive a `q^ell` com grupo de unidades
não cíclico. A conclusão em `L^2` fica restrita a `q` primo; a taxa não.

Para `q=3` nada é provado além da monotonicidade, que já era conhecida. A
redução a `T_ell(4,1)` é uma reformulação, e o piso `0,191` é uma medição de
nível finito sobre oito níveis.

## Relação com O1 e H-161

O mapa `A(k) = 4k+1` e a recursão `W = N + (1/4) W circ A` usados em H-161
são os mesmos objetos que aparecem aqui: `G_ell(1)` é a correlação de
vizinhos `(1/M) sum_j N_j N_(j+1)` exatamente ao longo da órbita que E-132
mede. As duas perguntas são relacionadas, não idênticas. E-132 mede com que
frequência duas posições consecutivas são pequenas ao mesmo tempo, e acha
antiaglomeração; o que a margem daqui precisa é de uma cota inferior para a
esperança do produto delas. A antiaglomeração empurra na direção útil para
essa cota, sem fornecê-la.
