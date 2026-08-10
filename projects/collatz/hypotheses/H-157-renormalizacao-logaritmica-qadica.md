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

(Só o terceiro limite acima ficou superado: a taxa `q/3` da seção
datada abaixo não usa levantamento maximal e cobre os primos
excepcionais. Os dois primeiros continuam valendo. Em `q=3` a taxa
diagonal é `q/3=1`, então também ali não há crescimento estrito por
comparação uniforme, e o balanço espectral de H-156 continua aberto.)

## Taxa diagonal `q/3` e redução do caso `q=3` (2026-08-09)

Trabalho feito sob O7 (continuidade absoluta e índice de cauda na
árvore aritmética). Registrado aqui porque o resultado principal é uma
melhora direta do teorema desta hipótese. Status de H-157 inalterado;
nada acima foi reescrito, só anotado.

### Identidade no domínio do tempo

Condicione no primeiro expoente em vez de diagonalizar. Com
`F_ell = 2^-a (1 + q F_(ell-1))` e `Y = 1 + q F_(ell-1) mod q^ell`, duas
cópias independentes colidem exatamente quando `Y' = 2^(a'-a) Y`. Os
expoentes são geométricos iid em `{1,2,...}`, logo
`P[a'-a=s] = 2^-|s|/3` e

```text
K_(q,ell) = (q/3) sum_(s in Z) 2^-|s| H_(ell-1)(s),
H_(ell-1)(s) = q^(ell-1) P[Y' = 2^s Y mod q^ell] >= 0,
H_(ell-1)(0) = K_(q,ell-1).
```

Isto é a dual de Fourier da identidade desta hipótese, não uma
identidade nova: a transformada de `2^-|s|` no subgrupo gerado por
`2^d` é exatamente `W_(q,d)`, e `q/3` é a média de `W_(q,d)` no
círculo (com `A=4^d+1`, `B=2^(d+1)`, tem-se `A^2-B^2=(4^d-1)^2`, logo
a média de `1/(A-B cos)` é `1/(4^d-1)`). O que a forma no domínio do
tempo acrescenta é a não negatividade termo a termo, que a forma
espectral esconde num balanço com sinais.

### Teorema (incondicional, todo `q` ímpar)

Descartando todo `s != 0`, que só remove termos não negativos,

```text
K_(q,ell) >= (q/3) K_(q,ell-1)    para todo ell >= 1.
```

A desigualdade já vale em `ell=1`, onde `F_0=0` e `Y=1` é
determinístico: ali `H_0(s)=[d | s]` e a identidade dá o valor exato

```text
K_(q,1) = (q/3) (2^d+1)/(2^d-1),
```

conferido contra a lei em todos os `q` testados (`q=3`: `5/3`; `q=5`:
`17/9`; `q=25`: `8,333349`). Com a base `K_(q,0)=1` (lei trivial módulo
`q^0=1`), iterar dá

```text
K_(q,ell) >= (q/3)^ell.
```

Três linhas. Sem Parseval, sem estrutura de órbita, sem a hipótese
`v_q(2^d-1)=1`. Como

```text
c_(q,d) = (q/3) (2^d-1)/(2^d+1) < q/3    para todo d,
```

a taxa `q/3` melhora estritamente a constante desta hipótese em todo
`q` e todo `d`, e vale também para os primos excepcionais de base dois
e para `q` ímpar composto, os dois casos que o enunciado original
exclui. Ela fica dentro do intervalo `[c_(q,d), C_(q,d)]` já provado
aqui, então não contradiz nada.

Comparação (`q/3` contra `c_(q,d)`): `q=5`, `1,666667` contra
`1,470588`; `q=7`, `2,333333` contra `1,814815`; `q=11`, `3,666667`
contra `3,659512`.

### Verificação (E-138)

`experiments/E-138-diagonal-shifted-collision/diagonal_rate.py`
constrói a lei pela convolução direta `mu_ell(y)=sum_a 2^-a nu(2^a y)`,
sem hipótese de órbita, e confere a identidade e a razão para
`q` em `{3,5,7,9,11,13,15,21,25}` até módulo `2e6`. Erro absoluto
máximo da identidade: `2,3e-13`. A razão `K_(q,ell)/K_(q,ell-1)` nunca
fica abaixo de `q/3`; o menor excesso observado é `8,0e-9`, em `q=25`.
Os casos `q=15` e `q=21` têm grupo de unidades não cíclico
(`ord_15(2)=4` contra ordem 8, `ord_21(2)=6` contra ordem 12), então a
órbita única de 2 usada na derivação original nem existe lá, e mesmo
assim a taxa vale. Os primos de Wieferich (1093, 3511) não foram
testados numericamente: o módulo necessário é grande demais. A prova
não os distingue de nenhum outro `q`.

A razão desce para `q/3` por cima em todos os `q` testados, então a
cota é assintoticamente exata, não só válida. Para `q=5`: `1,7238`,
`1,6962`, `1,6814`, ..., `1,6688` em `ell=8`.

### Caso `q=3`: o que a taxa dá e o que não dá

Em `q=3` a taxa é `q/3 = 1`, ou seja só monotonicidade de `K_ell`.
Monotonicidade já é conhecida por dois caminhos independentes (H-155
escreve `K_ell - K_(ell-1) = E_ell` como soma de quadrados; H-140 a
registra como segundo momento de martingala). O termo diagonal, em
`q=3`, não acrescenta informação.

O que é novo em `q=3` é a forma explícita do incremento. Com
`G_(ell-1)(r) = H_(ell-1)(2r)` (só os deslocamentos pares carregam
massa, porque `Y == 1 mod 3`),

```text
E_ell = 2 sum_(r>=1) 4^-r G_(ell-1)(r) >= (1/2) G_(ell-1)(1),
G_(ell-1)(1) = T_(ell-1)(4,1),
T_ell(u,v) = 3^ell P[F' = u F + v mod 3^ell].
```

Logo a margem uniforme que falta deixa de ser um balanço espectral com
sinais e vira uma única cota inferior de positividade: basta
`T_ell(4,1) >= c > 0` uniforme em `ell` para ter `E_ell >= c/2` e
`K_ell` divergindo linearmente. Medido (E-138,
`q3_shifted_profile.py`): `G(1)` sobe devagar, `0,70303` em `ell=4`,
`0,71709` em `ell=8`, `0,72692` em `ell=14`, sempre com `G(1)/2` abaixo
de `E_ell` como a desigualdade exige.

Varrendo todos os estados afins (todas as unidades `u`, todos os `v`),
o mínimo de `T_ell(u,v)` cai e achata:

```text
ell        1        2        3        4        5        6        7        8
min T   0,3333   0,2449   0,2137   0,2023   0,1961   0,1930   0,1915   0,1911
```

Isso é evidência de nível finito (oito níveis) de que
`inf_ell inf_(u,v) T_ell(u,v) > 0`, não prova. Essa única afirmação
fecharia a margem de `q=3`.

### Duas rotas tentadas que não fecham

Existe uma recursão exata, independente do nível, na família afim
inteira (validada em aritmética racional exata nos níveis 1, 2 e 3
contra a própria lei, em `affine_transfer.py`):

```text
T_ell(u,v) = 3 sum_(a,a'>=1) 2^-(a+a') T_(ell-1)(w, (w + v 2^a' - 1)/3),
w = u 2^(a'-a),   sobre os pares com 3 | (w + v 2^a' - 1),   T_0 = 1.
```

Rota A, indução em `ell`. O operador é monótono, então `T_2 >= T_1` em
todo estado daria `T_ell >= T_1(4,1) = 2/3` e fecharia. É falso: 22 dos
54 estados módulo 9 têm `T_2 < T_1`, por exemplo `T_2(1,1) = 24/49`. O
estado alvo passa (`T_1(4,1)=2/3`, `T_2(4,1)=34/49`), a indução não.

Rota B, certificado sub-invariante em resolução finita. Uma `h` de
`(u,v) mod 3^k` com `0 <= h <= 1` e `(Th) >= h` em todo levantamento
daria `T_ell >= h` por indução a partir de `T_0 = 1`. O maior `h`
desse tipo é o limite de `h <- min(h, T_* h)` a partir de `h=1`. Ele
colapsa geometricamente, cerca de `0,79` por rodada em `k=1` e `0,88`
em `k=2`. Refinar `k` melhora a taxa mas não remove a causa: o `min`
sobre levantamentos deixa um adversário reescolher o pior levantamento
a cada nível, sem consistência entre níveis, coisa que a dinâmica real
proíbe. Resultado negativo nesses dois `k`.

### Escopo

`K_ell -> infinito` equivale a a martingala de densidade ser ilimitada
em `L^2` (H-155), o que exclui densidade `L^2`. Não prova sozinho
singularidade da medida limite; isso exigiria não integrabilidade
uniforme em `L^1`, que não está estabelecida.

A taxa `q/3` vale para todo `q` ímpar, primo ou composto, e para
`q >= 5` dá divergência exponencial incondicional de `K_(q,ell)`. A
passagem de "K diverge" para "não há densidade `L^2`" usa a
decomposição de Parseval de H-155, que está enunciada para módulo
primo; não foi conferido se o bookkeeping de condutores de caractere de
H-155 sobrevive a `q^ell` com grupo de unidades não cíclico. Logo a
conclusão sobre densidade `L^2` fica restrita a `q` primo, enquanto a
taxa em si vale para todo `q` ímpar. Para `q = 3` não há nada provado
além do que já se sabia.

### Pista aberta (Regra 8e)

`inf_ell inf_(u,v) T_ell(u,v) > 0` (colisão deslocada afim limitada
inferiormente, uniformemente em nível e em estado) é uma pista própria,
surgida ao tentar quebrar a margem de `q=3`. Ela implica a margem
uniforme de `q=3`, e por isso implica `K_ell -> infinito` para a lei de
Syracuse clássica. Não recebeu número de hipótese aqui para não colidir
com as hipóteses abertas em paralelo; o número deve ser atribuído pelo
coordenador.

### Relação com O1 e H-161

O mapa `A(k)=4k+1` e a recursão `W = N + (1/4) W circ A` de H-161 são
os mesmos objetos: `G_ell(1)` é a correlação de vizinhos
`(1/M) sum_j N_j N_(j+1)` ao longo exatamente da órbita que E-132 mede.
As perguntas são relacionadas, não idênticas. E-132 mede com que
frequência duas posições consecutivas são pequenas ao mesmo tempo e
acha antiaglomeração; o que a margem aqui precisa é de cota inferior
para a esperança do produto delas. A antiaglomeração empurra na direção
útil sem fornecer a cota.
