# H-134: defeito relativo de mistura na Conjectura 2 de Wirsching

Status: fechada-confirmada; redução relativa provada

Criada: 2026-08-07

## Identidade de um passo

Com a normalização de Wirsching, escreva `f_ell=gtilde_ell`. A recursão
é exata:

```text
f_ell = S_ell f_(ell-1).
```

O operador limite elimina a variável 3-ádica:

```text
(S_infty f)(x,a) = (3/2) integral_[3x-2,3x] integral_Z3x f(t,b) db dt.
```

Defina o defeito

```text
D_ell(f;x,a) = (S_ell f)(x,a) - (S_infty f)(x,a).
```

Uma cota relativa uniforme

```text
|D_ell(f_(ell-1);x,a)|
    <= epsilon_ell (S_infty f_(ell-1))(x,a),
epsilon_ell -> 0,
```

na janela central implica a condição `(?3)` e, pelo teorema provado em
H-133, densidade uniforme positiva de predecessores. Basta comparar o
valor pontual com sua média em `a`; o termo limite `A` já não depende de
`a`. De fato, `f_ell(x,a)>=A(1-epsilon_ell)` e
`integral f_ell(x,a)da<=A(1+epsilon_ell)`, logo o quociente de `(?3)` é
ao menos `(1-epsilon_ell)/(1+epsilon_ell)` sempre que `A>0`.

## Por que o Teorema 3 não fornece a cota

Na prova do Teorema 3 de Wirsching escolhe-se uma resolução `3^(-r)`.
O lema de quadratura exige simultaneamente

```text
r <= s,    s=ell-r-1,
```

portanto `2r<=ell-1`. Para uma família equicontínua, `r` é fixado antes
de `ell`, e isso prova convergência uniforme absoluta.

A função `f_(ell-1)` pode depender de todos os primeiros `ell-1`
dígitos nas duas coordenadas. Sua escala natural de oscilação é então
`3^(-(ell-1))`, que exigiria `r=ell-1` e viola `2r<=ell-1`. O número de
pontos de quadratura não resolve oscilações criadas na mesma escala que
a própria malha.

Há uma segunda perda. Na janela usada por Wirsching,
`x_ell` é da ordem de `ell*3^(-ell)` e o perfil limite tende rapidamente
a zero. Uma estimativa absoluta `|D_ell|=o(1)` não controla o quociente
pontual. É necessária a estimativa relativa acima.

## Relação com O1

A cota relativa afirma que os dígitos 3-ádicos ainda não consumidos pela
recursão se distribuem quase como Haar quando condicionamos o primeiro
argumento à janela extrema. Esta é a formulação de operador do mesmo
problema de dígitos frescos entre subárvores em O1. O Teorema 3 trata
funções teste de resolução fixa; O1 e a Conjectura 2 exigem resolução
crescente e erro relativo.

## Resultado

O3 fica reduzido ao seguinte alvo quantitativo: provar mistura relativa
para a órbita não autônoma `S_ell ... S_1 f_0` em escalas que crescem
com `ell`. Convergência forte de `S_ell` para `S_infty`, mesmo uniforme
em famílias equicontínuas, não basta.

## Avanço H-143

O alvo relativo também admite uma formulação microcanônica exata. A
condição `(?3)` equivale a limitar inferiormente `g_ell(k,a)` pela sua
média em `a`, uniformemente para `k=ell+O(sqrt(ell))`. H-143 prova que
a medida de Syracuse é a mistura geométrica desses geradores. O TCL da
variável de custo mostra que `(?3)` implica diretamente
`mu_ell(a) >= C*3^(-ell)`, mais forte que a forma subexponencial de
`beta=1`.

Isso não prova a Conjectura 2, mas identifica sua consequência
aritmética exata e une O3 a O2 sem uma analogia informal. E-115 mostra
que, até `ell=12`, a cobertura por custo fixo ainda tem buracos mesmo
na janela central, embora na borda superior da janela já cubra 99,73%
dos resíduos.

A estimativa de mistura relativa foi separada como H-160.

## Correção posterior por H-160

H-160 refutou a convergência relativa para Haar usada aqui como alvo
suficiente. A projeção módulo `3` mantém massas assintóticas `1/3` e
`2/3` na janela central, logo o defeito relativo não tende a zero.
A redução lógica desta nota continua correta como implicação, mas sua
hipótese é impossível. A Conjectura 2 exige normalização pelo perfil
grosseiro correto ou uma estimativa inferior positiva mais fraca.
