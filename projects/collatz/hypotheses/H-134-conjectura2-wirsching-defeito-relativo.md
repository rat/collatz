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

## 2026-08-09: o enunciado primário, e onde a rota realmente para

Resumo: a Conjectura 2, como enunciada, é o alvo errado. O obstáculo
concreto que aparece nos dados não é o que esta nota e H-160
perseguiam, e não é o que a Conjectura 2 nomeia. Os buracos de suporte
em `k=ell` são artefato da janela simétrica de Wirsching, e a Proposição
abaixo mostra que o Teorema 1 não precisa do centro. O decaimento
quantitativo que aparece é do ínfimo sobre um grupo que cresce com
`ell`, não de nenhum resíduo fixo, e é sobre a constante uniforme em
`a`, que o Teorema 1 não consome. A pergunta viva é a de H-168.

Fonte lida na íntegra:
`literature/papers/132_Wirsching-2003-Positive-Predecessor-Density.pdf`,
18 páginas, marcada pelo autor como *preliminary version*. Nenhuma nota
de leitura existia em `literature/notes/`; as notas anteriores desta
linha usavam paráfrase. Três coisas mudam.

### 1. A Conjectura 2 é a implicação `(?4) => (?3)`

A cadeia do artigo é:

```text
Teorema 1   (provado)     (?1) => densidade positiva uniforme
Conjectura 1              (?2) => (?1)          [provada em H-133]
Teorema 2   (provado)     (?3) => (?2)
Conjectura 2              (?4) => (?3)
Conjectura 3              (?5), e (?5) => (?4) é provado na seção 7
```

com

```text
(?4)  liminf_ell (W_3^ell chi_1)(x_ell) / (W_3^ell chi_0)(x_ell) >= mu,
      chi_0 = 1_[0,2/3],  chi_1 = 1_[1/3,1].
```

`(?4)` não menciona os geradores. É um enunciado sobre o operador
unidimensional `W_3` e mais nada. A Conjectura 2 pede, portanto, uma
cota inferior pontual em `a` a partir de uma hipótese que não carrega
nenhuma informação sobre a coordenada 3-ádica. A única ponte oferecida
é o Teorema 3, e a obstrução de quadratura desta nota (`r <= s`,
`s = ell-r-1`, logo `2r <= ell-1`, contra escala de oscilação
`3^(-(ell-1))`) diz que essa ponte não alcança a resolução exigida.
Qualquer prova da Conjectura 2 tem de injetar uma equidistribuição da
órbita afim `a -> (2^(j+1) a - 1)/3` que não está em `(?4)`. Isto é uma
afirmação sobre o que uma prova precisa conter, não um teorema de
impossibilidade.

### 2. `(?3)` e `(?2)` são a mesma desigualdade, com quantificadores diferentes

Escrita por extenso, `(?3)` é `g_ell(k_ell,a) >= mu * gbar_ell(k_ell)`
com `mu>0` fixo: a constante de normalização `gamma_ell` da seção 3
cancela entre os dois lados. O conteúdo do Teorema 2 é só a troca de
quantificador. `(?3)` diz "existem `delta, mu > 0` e um índice `ell_0`"
e depois exige a desigualdade em todo `ell >= ell_0` e toda unidade `a`;
`(?2)` é um `liminf` em `ell` a cada `a` fixo.

O alvo desta nota, `epsilon_ell -> 0`, é o caso `mu -> 1`. Ele é
estritamente mais forte do que `(?3)` precisa. H-160 refutou esse alvo
mais forte e não tocou em `(?3)`. A rota não está fechada pelo motivo
registrado acima.

### 3. Um único zero central refuta `(?3)`

Como `(?3)` é quantificada em todo `ell >= ell_0` e toda unidade, e como
`k_ell = ell` é uma sequência admissível de `A_delta` para todo
`delta > 0`, basta um resíduo unitário com `g_ell(ell,a)=0` num nível
`ell >= ell_0` para falsificá-la. `(?2)`, sendo um `liminf` por `a`,
sobrevive a zeros que mudam de resíduo com `ell`.

### O que E-135 mede

Suporte booleano exato, todos os resíduos, `ell <= 18`
(`central_zeros.py`), e contagens inteiras exatas, `ell <= 16`
(`central_ratio.py`). Auditado contra o predicado regressivo
independente de E-121 e contra a contagem de composições limitadas.

- `Z_ell = {a : g_ell(ell,a)=0}` é não vazio em todo nível até 18.
  Em `ell=18` são 11.540.739 zeros entre 258.280.326 unidades (4,47%).
  O primeiro custo com suporte completo é `ell+5` para `10<=ell<=18`,
  estendendo o padrão que E-115 via até 16.
- A fração de zeros cai com razão `|Z_(ell+1)|/|Z_ell|` igual a
  2,39, 2,34, 2,27, 2,20 nos últimos quatro passos, contra 3 unidades
  novas por nível. A razão decresce cerca de 0,06 por nível. Nada nos
  dados decide se `Z_ell` esvazia.
- Existe uma subárvore coerente: 734.754 resíduos módulo `3^18` cujas
  truncagens são zeros centrais em *todos* os níveis anteriores. Se ela
  fosse não vazia em todo nível, o limite inverso daria um `alpha`
  3-ádico com `g_ell(ell,alpha)=0` sempre, refutando `(?3)` e também
  `(?2)` naquele `alpha`. Mas a razão de crescimento cai depressa,
  2,17, 2,06, 1,94, 1,79, e a extrapolação linear a leva a 1 perto de
  `ell=24`. Testemunhas foram reconferidas com o predicado de E-121.

A metade quantitativa é o achado mais informativo. Onde o suporte já é
completo, `min_a g_ell(k,a)/gbar_ell(k)` continua caindo:

```text
d = k-ell    ell=6    ell=10   ell=15   razão por nível
+6           0.1706   0.0680   0.0729
+7           0.2656   0.1623   0.1123   ~0.91
+12          0.4805   0.3840   0.2749   ~0.94
```

Em `d=+12`, onde a série tem menos ruído, o decaimento é geométrico com
razão perto de 0,94 por nível, estável entre `ell=6..10` (0,946) e
`ell=11..16` (0,938). O deslocamento `d` compensaria isso apenas se
crescesse linearmente em `ell`, e a janela de Wirsching só permite
`d <= delta*sqrt(ell)`. Portanto o ínfimo sobre `Z_3^x` que `(?3)` pede
não estabiliza em nenhum ponto da janela, e `(?3)` não falha só em
`k=ell` por falta de suporte.

Uma ressalva que os dados impõem. O mínimo é tomado sobre
`2*3^(ell-1)` unidades, um conjunto que cresce com `ell`, então parte da
queda é estatística de extremos e não deterioração de nenhum resíduo.
Fixando o conjunto, o quociente fica plano: sobre as 1458 unidades
abaixo de `3^7`, em `d=+5`, ele dá 0,102, 0,074, 0,107, 0,079, 0,116,
0,108, 0,096 para `ell=10..16`. Separar os dois efeitos exige quantis
em vez do mínimo, e é o que H-168 registra.

Se a queda for real, ela custa caro: o Teorema 1 consome `mu` constante,
e com `mu_ell ~ 0.94^ell` a soma sobre `ell in Delta_y` tem
`~sqrt(y)` termos, todos carregando `0.94^(y/theta)`, de modo que a cota
de densidade degenera. Nesse cenário um enfraquecimento subexponencial
de `(?3)` não sobrevive ao Teorema 1, e pela implicação de H-143 (cota
uniforme `eta` implica `mu_ell(a) >= C*3^(-ell)`) um `eta_ell` que decai
como `0.94^ell` só entrega `mu_ell(a) >~ 3^(-1.06*ell)`. Se a queda for
artefato do tamanho do conjunto, nada disso se aplica e `(?3)` é apenas
forte demais.

### Proposição (janela unilateral): o Teorema 1 não precisa do centro

Seja `theta = 2 - log_2 3`. Para `c_0 >= 0` inteiro e `delta > 0`,
defina

```text
A'(delta,c_0) = {(k_ell) : c_0 <= k_ell - ell <= delta*sqrt(ell),
                 para todo ell >= ell_1}.
```

Se existirem `delta, mu > 0` e `c_0` com
`liminf_ell e_ell(k_ell,a)/ebar_ell(k_ell) >= mu` uniformemente para
`(k_ell) in A'(delta,c_0)`, então vale densidade positiva uniforme de
predecessores.

Prova. Na demonstração do Teorema 1 troque `Delta_y` por
`Delta'_y = {ell : c_0 <= k_ell(y) - ell <= delta*sqrt(ell)}`. Todos os
termos da soma (1.6) são não negativos, logo restringir o conjunto de
índices só diminui o lado direito e (1.7) continua válida. As duas
estimativas usadas após (1.12), `d_ell^2/nu_ell <= delta^2/2` e
`1/sqrt(nu_ell) >= c/sqrt(y)`, são herdadas de `Delta'_y` estar contido em `Delta_y`; a
segunda vale com a mesma constante porque `nu_ell = (ell+k_ell)/2` e
todo `ell` da janela satisfaz `ell = (y/theta)(1+O(y^(-1/2)))`, o que
não depende de o intervalo estar centrado. Também `d_ell^3/nu_ell^2 -> 0`
é herdada. Resta a contagem: `y - theta*ell` decresce de `theta` a cada
incremento de `ell`, logo `|Delta'_y| = (delta*sqrt(ell) - c_0)/theta +
O(1)`, que é `>= (delta/(2*theta^(3/2)))*sqrt(y)` para `y` grande. Fora
de `Delta'_y` estenda a sequência por `k_ell = ell + c_0`, admissível
assim que `delta*sqrt(ell) >= c_0`. As demais constantes são as de
Wirsching. QED

A prova da Conjectura 1 em H-133 transfere igual: se `(?2')` vale em
deslocamentos `[c_0, delta_1*sqrt(ell)]` e `k` tem deslocamento em
`[c_0 + eta*sqrt(ell), (delta_1-eta)*sqrt(ell)]`, então `j = k-m` com
`0 <= m <= eta*sqrt(ell)` cai na janela de `(?2')`. O Teorema 2 é
reescrita e transfere sem mudança.

Consequência: os buracos de suporte em `k=ell`, o único obstáculo
concreto e indiscutível nos dados, são artefato da janela simétrica de
Wirsching e não obstruem o programa. O que sobra é a questão
quantitativa, que a janela unilateral não conserta e que H-168 formula.

### O que continua vivo

O Teorema 1 só consome `a` inteiro, não cíclico, `a != 0 mod 3`. As
condições `(?2)`/`(?3)` são enunciadas sobre `Z_3^x` e são estritamente
mais fortes do que o Teorema 1 usa. Medindo o mínimo sobre um conjunto
fixo de inteiros em vez do mínimo sobre todas as unidades, em `d=+5`,
o contraste é de uma ordem de grandeza e o mínimo sobre um conjunto fixo
fica plano em `ell`: ver E-135 e H-168. Essa diferença, e não `(?4)`, é
onde a Conjectura 2 deveria ser reformulada. A persistência dos zeros
centrais ficou como H-167, inconclusiva até `ell=18`.
