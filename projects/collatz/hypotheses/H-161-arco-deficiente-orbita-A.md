# H-161: reformulação exata de beta=1 como ausência de arco deficiente longo

Status: in-progress

Criada: 2026-08-08

Origem: surgiu durante uma tentativa (Regra 11b, consulta a modelo mais
forte) de atacar o passo 4 de H-158 (desigualdade recursiva para o pior
cilindro). Registrada como hipótese própria por exigência da Regra 8e
(todo caminho que uma tentativa de quebrar algo revela vira sua própria
entrada, mesmo saindo do escopo original).

## Identidade de base (verificada de forma independente, ver H-158)

Para `y` unidade mod `3^ell`, os `t>=1` com `2^t y == 1 (mod 3)` têm
paridade fixa `t0(y) in {1,2}`, e o passo `t -> t+2` age sobre
`z=2^t y mod 3^ell` como `z -> 4z`. Escrevendo `z=1+3k`, isso induz o
mapa afim

```text
A(k) = 4k+1 (mod 3^(ell-1))
```

que é um único ciclo de comprimento `N=3^(ell-1)` cobrindo todo
`Z/3^(ell-1)Z` (verificado: 4 tem ordem exatamente `3^(ell-1)` mod
`3^ell`). Disso segue a identidade exata (verificada numericamente a
~1e-14 contra `weighted_bridge.py`, independentemente, sem reusar o
código da consulta que a originou):

```text
mu_ell(y) = 2^-t0(y) * sum_{j=0}^{N-1} 4^-j * mu_(ell-1)(A^j(k0(y)))
```

(o fator de correção `(1-4^-N)^-1` é indistinguível de 1 em ponto
flutuante para qualquer `ell` testável). Logo

```text
c_ell = (1/4) * min_k G(k),   G(k) = sum_j 4^-j mu_(ell-1)(A^j(k))
```

## Enunciado — rederivado linha a linha (2026-08-08); só UMA direção fecha

Defina `N_ell(u) = 3^ell mu_ell(u)`. Para todo `eps>0`, considere o
maior arco consecutivo de `A` (na órbita de nível `ell`) contido no
conjunto `{u : N_ell(u) <= exp(-eps*ell)}`. A consulta original alegou
uma equivalência "sse". Rederivando linha a linha, isso está errado
como "sse": só uma direção fecha sem hipótese extra.

**(A) "nenhum arco cresce" implica "beta_eff -> 1" — PROVADO, sem
lacuna.** Suponha `beta_eff` NÃO tende a 1: existe `eps_0>0` com
`3^ell c_ell <= exp(-eps_0 ell)` para infinitos `ell`. Pela identidade
de base, no `k` que minimiza `G`, TODO termo individual
`4^-j mu_(ell-1)(A^j k)` é, em particular, `<= G(k) = 4 c_ell`,
logo (trocando para `N`) `N_(ell-1)(A^j k) <= 4^(j+1) c_ell`. Para
`j` até `~eps_0 (ell-1)/(2 log 4)`, isso já força
`N_(ell-1)(A^j k) <= exp(-eps_0(ell-1)/2)`: um arco de comprimento
`Theta(ell)`, não `o(ell)`. Contrapositiva: se nenhum arco cresce (para
NENHUM `eps`), `beta_eff` tem que tender a 1. Esta é a direção que
importa para usar "arco curto observado" como evidência a favor de
`beta_eff -> 1`, e não precisa de nenhuma hipótese adicional.

**(B) "beta_eff -> 1" implica "nenhum arco cresce" — FECHA por uma
FAIXA de comprimentos, não por todos.** Correção (2026-08-08, segunda
rodada, apontada em consulta): não é "não fecha", é mais preciso do
que isso. A volta pediria: dado um arco curto (comprimento `m`) com `N`
pequeno no COMEÇO da janela, concluir que a soma INTEIRA `G(k)`
(incluindo a cauda além do arco, `j>=m`) também é pequena. Isso exige
controlar `max_u N_(ell-1)(u)` na cauda. Provamos uma cota a priori
limpa, por indução na própria recursão (`mu_ell(y) = 1/2 nu(2y) + 1/2
mu_ell(2y)`, logo `M_ell <= (2/3) M_(ell-1)` onde `M_ell = max_u
mu_ell(u)`, base `M_1=2/3`): `M_ell <= (2/3)^ell`, ou seja `N_max <=
2^ell` SEMPRE. Com essa cota, a volta FECHA para todo arco de
comprimento `m >= ell*(log2+eps)/log4 ~ 0.5 ell` (banda alta,
`c>=0.5` na escala `m=c*ell`) — usando só o que já está provado, sem
nada condicional. Medido o comportamento real de `N_max` (não só a
cota): cresce como `(3/2)^ell` quase exatamente (razão por nível
convergindo a 1.5000 já em `ell~10`, ver tabela abaixo). Usando essa
taxa (empírica, não provada) em vez da cota crua, a banda onde a volta
fecha desce para `c>=0.29`. O que fica genuinamente em aberto é só a
faixa intermediária `0 < c < 0.29` (ou `<0.5`, sem a taxa empírica) —
uma banda estreita, não a direção inteira. Os arcos observados (2 a 3
em `ell=8..18`, ver dados abaixo) caem dentro dessa banda ainda aberta
a partir de `ell~14`, é por isso que a evidência empírica de arco curto
não fecha (B) sozinha, mas uma cota melhor de `N_max` só precisaria
reduzir a banda, não resolver o problema inteiro do zero.

**Nota**: a taxa `N_max ~ (3/2)^ell` não é um insumo independente. A
cota crua `M_ell<=(2/3)M_(ell-1)` vem de permitir que TODOS os termos
com `t>=3` estejam simultaneamente perto do máximo `M_(ell-1)`; chegar
a `(1/2)M_(ell-1)` exigiria argumentar que eles não podem estar todos
quase-máximos ao mesmo tempo — exatamente a mesma pergunta de
anti-aglomeração de (B), um nível abaixo. Não é uma ferramenta externa
que resolve o problema; é o mesmo fenômeno visto de outro ângulo.

**Conclusão**: a direção útil (A) está provada e não precisa de nada
além da identidade de base. A direção (B) fecha para arcos de
comprimento `c*ell` com `c>=0.5` (provado) ou `c>=0.29` (com a taxa
empírica de `N_max`, não provada); a faixa `c` menor que isso continua
em aberto, e é justamente aí que caem os arcos observados a partir de
`ell~14`. Isso não invalida usar os dados de arco curto como evidência
a favor de `beta_eff -> 1` (via (A)); só
significa que a formulação "sse" da consulta original estava incorreta
e que "arco curto" não é (ainda) um critério equivalente, só suficiente
por um lado.

## Reformulação mais afiada da faixa em aberto (2026-08-09)

`W(k) := G(k)/mu_(ell-1)`-normalizado satisfaz, por reindexação direta
da soma geométrica (verificado numericamente: `W(k) = N(k) + (1/4)
W(A(k))` bate exatamente contra a recursão de referência em vários
`k`), a identidade exata

```text
W(k) = N(k) + (1/4) W(A(k))
```

Logo, após um arco deficiente de comprimento `m` a partir de `k0`
(isto é, `N(k0),...,N(A^(m-1) k0)` todos pequenos), a cauda que falta
controlar é EXATAMENTE `4^-m * W(A^m k0)` — nem mais, nem menos. Isso
reduz toda a faixa em aberto de (B) a uma única pergunta: **`W` pode
ser exponencialmente grande justamente na posição logo depois de um
arco deficiente terminar?** Sabemos que `max_k W(k) >= N_max ~
(3/2)^ell` (valores grandes de `W` existem em algum lugar da órbita);
o que não sabemos é se esses valores grandes podem ficar adjacentes a
um arco deficiente — se puderem, a volta da equivalência é falsa nessa
faixa (haveria arco curto sem `beta_eff->1`); se não puderem (por
algum motivo estrutural), a volta fecha na faixa toda.

## Por que isso importa

Se verdadeiro, reduz a pergunta original (limite de uma sequência
numérica) a uma pergunta estrutural sobre anti-aglomeração de pontos
deficientes ao longo da órbita de um mapa afim explícito — uma
pergunta mais concreta, mas não necessariamente mais fácil.

## Como testar

1. Rederivar a álgebra da equivalência linha a linha (não foi feito
   ainda com o rigor que os outros resultados fechados deste projeto
   recebem).
2. ~~Medir o maior arco deficiente usando o limiar CORRETO
   `exp(-eps*ell)`~~ Feito (ver "Primeira medição com limiar correto"
   abaixo e `E-131`). Uma primeira tentativa com limiares fixos (0.2,
   0.3, 0.5) tinha mostrado crescimento do maior arco com `ell`, mas
   isso não testava a alegação: a um limiar fixo, a fração de posições
   abaixo dele também cresce com `ell`, então até um arranjo aleatório
   i.i.d. das mesmas frequências produziria um maior-arco crescendo
   como `log(N)/log(1/p)`, linear em `ell`.
3. ~~Comparar o arco observado contra a linha de base aleatória~~ Feito
   (ver abaixo): sinal de anti-aglomeração no intervalo testado
   (`ell=8` a `18`), preliminar, intervalo curto demais para
   extrapolar. Estender a faixa de `ell` é o próximo passo natural.

## Crescimento de N_max (2026-08-08)

`M_ell := max_u mu_ell(u)` satisfaz `M_ell <= (2/3) M_(ell-1)` (uma
linha, direto da recursão: cada termo de `mu_ell(y)=1/2 nu(2y)+1/2
mu_ell(2y)` é `<= M_(ell-1)` ou `<= M_ell`, e só metade dos `t` (por
paridade) contribui, dando fator `2/3` no pior caso de fase). Medido
`N_max = 3^ell M_ell`:

```text
ell   N_max        razão_por_nível   log(N_max)/ell
 1     2.0000          -               0.6931
 5    10.9778        (~1.51 estável)   0.4792
10    84.1769         1.5011           0.4433
15   640.1920         1.5001           0.4308
16   960.3429         1.5001           0.4292
```

A razão converge a exatamente `1.5000` já em `ell~10`: `N_max ~
C*(3/2)^ell`. Melhor que a cota provada (`2^ell`), mas ainda
exponencial, não limitada — é isso que faz a direção (B) da
equivalência não fechar para os arcos curtos observados (ver acima).

## Primeira medição com limiar correto (2026-08-08)

**Correção (2026-08-08, terceira rodada, apontada em consulta):** a
primeira versão deste script tinha um bug real: `longest_run` rodava
sobre a órbita INTEIRA (incluindo posições não-unidade, onde `mu=0`
sempre, contando como "deficiente" de graça), enquanto a fração `p`
era calculada só sobre unidades. Como `A(k)==k+1 (mod 3)`, uma em cada
três posições da órbita é não-unidade — essas posições "grátis" podiam
emendar arcos que na verdade eram só unidades isoladas, inflando o
arco observado sem inflar `p` (nem a linha de base calculada a partir
de `p`). Corrigido contraindo a órbita à subsequência de só unidades
antes de medir o arco (mesma população que `p` mede). Os números
abaixo já são os corrigidos; note que, ao contrair a sequência dessa
forma, o teto estrutural que o padrão módulo 3 impunha sobre arcos na
órbita completa desaparece — um arco de comprimento 2 ou 3 na
sequência contraída não é um artefato geométrico do mapa `A`, é sinal
real sobre os valores.

Medido `exp(-eps*ell)` para `eps=0.1` e `eps=0.2`, níveis `ell=8` a
`18` (ir além de 18 com o método rápido atual exigiria mais memória do
que é seguro usar nesta máquina de uma vez — a tentativa em `ell=19`
já passou de 47GB residentes com só 16GB livres no sistema, e foi
interrompida antes de arriscar; o array de nível 20 sozinho chegaria
perto de 90GB), contra a linha de base de arranjo aleatório
`log(N)/log(1/p_ell)` (`N`= número de posições-unidade na órbita,
`p_ell`= fração observada abaixo do limiar naquele nível):

```text
eps=0.1:
ell    frac      arco_observado   linha_de_base
 8   0.29630          3              6.89
 9   0.26947          3              7.23
10   0.24539          3              7.53
11   0.22203          3              7.76
12   0.19951          3              7.93
13   0.17812          3              8.04
14   0.15774          2              8.11
15   0.13851          2              8.13
16   0.11999          2              8.10
17   0.10219          2              8.01
18   0.08545          2              7.87

eps=0.2: fração já minúscula a partir de ell~13 (3.5e-3 a 4.8e-6),
poucas posições marcadas o bastante para o arco (sempre 1, isolado, ou
0 quando a fração some) dizer algo: não é evidência, é a contagem
esperada de qualquer jeito quando há tão poucas posições marcadas.
```

O arco observado (limiar `eps=0.1`, a única coluna com sinal
suficiente) fica ABAIXO da linha de base aleatória em todo o
intervalo, e não cresce: cai de 3 para 2 entre `ell=13` e `ell=14` e
se mantém em 2 até `ell=18`. Isso é evidência a favor de
anti-aglomeração real (não apenas ausência de aglomeração) dos pontos
deficientes ao longo da órbita de `A`, consistente com a Hipótese (D)
proposta na consulta original — mas o intervalo (`ell=8` a `18`, 11
pontos) é curto demais para distinguir um efeito assintótico genuíno de
uma flutuação finita, e (ver seção
acima) mesmo que a tendência de queda se confirme, isso sozinho não
prova `beta_eff->1` pela direção (B) da equivalência, que continua sem
fechar. Script limpo e commitado em
`projects/collatz/experiments/E-131-affine-orbit-reformulation/deficient_arc_scan.py`
(reescrito do zero a partir da versão exploratória usada na consulta,
que ficou só no scratchpad da sessão).

Cross-check: a coluna `min_N` do script bate exatamente com `3^ell c_ell`
já verificado em E-127 (`ell=12`: 0.052915; `ell=18`: 0.040424),
confirmando que a reimplementação rápida usada aqui está correta.

**Avaliação**: sinal real, mas preliminar — o suficiente para justificar
`in-progress` em vez de `open-unexplored`, não para fechar H-158 nem
para promover esta hipótese a confirmada. A direção (A) da equivalência
(a que realmente sustenta usar este sinal como evidência) está provada
sem lacuna; a direção (B) precisaria de um controle de `N_max` melhor
que o disponível hoje, ou de uma técnica diferente, para fechar nos
comprimentos de arco observados. Próximo passo natural: o método atual
(`circ_geom_half`, O(M log M) por nível via duplicação binária) já
esbarrou no teto seguro de memória desta máquina em `ell=19-20`
(array de nível 20 chegaria perto de 90GB); estender mais exigiria uma
implementação que não materialize a lei inteira (rastrear só a órbita
de `A` a partir de um `k` candidato, recursivamente, sem o array
completo de tamanho `3^ell`), não simplesmente mais RAM.

## Segunda consulta (2026-08-09): reduz a faixa aberta a uma pergunta sobre pares

Nova consulta (Fable, Regra 11b), com o contexto totalmente corrigido
(a "sse" errada, o bug do arco, os números certos) e duas perguntas
concretas: (1) a identidade `W(k)=N(k)+(1/4)W(A(k))` reduz toda a
faixa aberta de (B) a "pode `W` ficar exponencialmente grande logo na
posição seguinte a um arco deficiente terminar?"; (2) uma tentativa de
prova real de anti-concentração conjunta em pares consecutivos
(`m=2`). Cada alegação verificada de forma independente antes de
aceitar (Regra 8c); desta vez TUDO que foi verificado passou —
nenhuma correção necessária, ao contrário das duas rodadas anteriores.

### Identidades novas, provadas e verificadas numericamente (a ~1e-14, código escrito do zero)

- **F1** (consequência direta de definições já estabelecidas):
  `N_ell(y) = 3*2^-t0(y)*W(k0(y))`. Cada ponto `k0` da órbita tem
  exatamente dois "filhos" `y`, com valores `(3/2)W(k0)` e `(3/4)W(k0)`.
- **F3** (indução de uma linha na própria recursão sem memória):
  `N_ell(2y) <= 2 N_ell(y)` SEMPRE, com igualdade exata quando `y==1
  mod 3`. Verificado: 0 violações em 2029 amostras aleatórias; a
  igualdade em `y==1 mod 3` bate a `<1e-9` em todos os casos testados.
  Consequência usada em Q1 abaixo: `N_ell(2^s y) <= 2^s N_ell(y)`.
- **F4** (consistência marginal entre níveis, pushforward): a soma das
  3 massas "filhas" de `u` no nível `ell` é exatamente `mu_(ell-1)(u)`.
  Verificado exatamente (erro `~1e-19`).
- **F2** (a estrutura por trás da pergunta de pares — a mais elaborada,
  verificada em 30+30 amostras com erro relativo `~1e-16`): na
  sequência contraída às unidades, pares consecutivos vêm em dois
  tipos, ambos redutíveis a um par de valores de `W` no nível
  `ell-2` ligados por um mapa afim explícito:
  - Tipo (1,2) (`k==1 mod 3`, par com `A(k)`): `N(k)=(3/4)W''(a)`,
    `N(A(k))=(3/2)W''(b)`, com `b = 2a+1 (mod 3^(ell-2))`. Confirmado
    exatamente.
  - Tipo (2,1) (`k'==2 mod 3`, par com `A²(k')`, pulando a
    não-unidade): `N(k')=(3/2)W''(b)`, `N(A²(k'))=(3/4)W''(a''')`, com
    `a''' = 32b+17 (mod 3^(ell-2))`. Confirmado exatamente.

### Questão 1: `W` pode ficar grande logo depois de um arco deficiente?

**Exclusão provada (sem deslocamento aditivo, o resgate é impossível):**
`A^m(k) = 4^m k + (4^m-1)/3` (fórmula fechada, indução trivial). Se o
deslocamento aditivo não existisse, F3 daria `N(4^m k0) <= 4^m N(k0)
<= 4^m exp(-eps*ell)` — um fator `exp(eps*ell)` ABAIXO do necessário
para resgatar `W(A^m k0)`. Ou seja: a pequenez de `N` se propaga
exatamente ao longo de retas multiplicativas (potências de 2), mas a
janela do arco lê ao longo de uma reta multiplicativa DESLOCADA
aditivamente por `(4^m-1)/3`. Isso identifica a faixa aberta como um
problema tipo soma-produto em `Z/3^ell`, não uma questão vaga — e
explica por que um argumento espectral "soft" sozinho não fecha.

Sem essa exclusão, nada mais foi provado: um argumento de contagem por
entropia (heurístico, não uma prova) sugere que em escala `m=O(1)`
adjacência de `W` grande a um valor pequeno NÃO é proibida e pode até
ser comum; só em escala `m=Theta(ell)` (a que quebraria `beta_eff->1`)
a heurística pesa contra. Ambos os lados continuam sem prova.

### Questão 2: anti-concentração em pares consecutivos (`m=2`)

**Correção necessária no nosso próprio enunciado original**: pedir
`P(N(k)<=x` e `N(A(k))<=x)` sobre `k` unidade qualquer é trivialmente
falso, porque `A(k)` pode ser não-unidade (`N=0` de graça) para
`k==2 mod 3`. O enunciado certo é sobre pares de unidades CONSECUTIVAS
na sequência contraída (cobrindo os dois tipos de F2) — o mesmo
cuidado de contração já usado no conserto do bug do arco.

**Teorema condicional, rederivado e confirmado por nós (não só aceito
da consulta):** se existem `kappa>0`, `C<infinito` com

```text
P(par consecutivo, ambos <= x) <= C*x^(2*kappa)   para x >= exp(-c0*ell)
```

com `c0 >= log(3)/(2*kappa)` (condição de escopo: o piso da união
precisa estar dentro do intervalo onde a cota vale), então
`beta_eff <= 1 + 1/(2*kappa) + o(1)`, incondicionalmente. Rederivação:
cota de união sobre os `~3^(ell-1)` pares força zero pares abaixo de
`x* ~ 3^(-ell/(2*kappa))`; se nenhum par tem os dois valores `<=x*`,
então para todo `k`, ou `N(k)>x*` (daí `W(k)>=N(k)>x*`) ou `N(k)<=x*`
e o próximo par força `N` da próxima unidade `>x*`, contribuindo pelo
menos `x*/16` a `W(k)` (peso mínimo `4^-2` no pior caso, distância 2
no Tipo (2,1)) — em ambos os casos `W(k)>=x*/16` para todo `k`, logo
`3^ell c_ell = (3/4)min_k W(k) >= (3/16)x*`, dando o resultado.
Calibração: a cota escalar já registrada acima (`beta<=2.523719`, via
`c_ell>=c_(ell-1)/16`) corresponde a este mecanismo sem nenhuma
informação de par; QUALQUER `kappa` constante provado já melhora essa
cota (`kappa=0.4` já daria `beta<=2.25`, incondicional e novo).

**O que falta provar**: só a direção difícil do teorema condicional
acima — a própria desigualdade de par. A direção fácil (par implica
controle em nível `ell`, "sanduíche") foi verificada como consequência
direta de F1 e da recursão de `W`; a direção difícil (desacoplamento
genuíno) não tem argumento algébrico exato disponível (as janelas de
`k` e do "próximo" ponto só coincidem exatamente por 1 nível; além
disso, ficam genericamente disjuntas, mas "genericamente disjuntas"
não é uma prova de independência). Um programa concreto (não fechado)
foi esboçado via somas de Weyl 3-ádicas no tempo de órbita explícito
`tau(u) = log(1+3u)/log(4)` (3-adicamente convergente), com uma
checagem de não-degenerescência da fase que se sustenta algebricamente
mas não foi verificada por nós além da conferência da álgebra em si.

### E-132: medição direta do expoente de descorrelação — sinal forte (corrigido)

Medido `pair(x)/d(x)^2` a limiar ESCALADO `exp(-eps*ell)` (limiar fixo
mistura o efeito de correlação com a mudança de raridade — a mesma
armadilha já corrigida no arco). A primeira versão usava um `d(x)`
único, poolado sobre as duas fases do par.

**Correção (2026-08-09, segunda escalada Regra 11b):** F1 mostra que os
dois membros de todo par consecutivo têm marginais DIFERENTES
(`N=(3/2)W` na fase 2, `N=(3/4)W` na fase 1, e a sequência contraída
alterna fase 1,2,1,2,... estritamente). Comparar a cauda conjunta
contra um `d(x)^2` poolado não é a linha de base de independência
correta: por AM-GM, `d1*d2 <= ((d1+d2)/2)^2` sempre que `d1!=d2`, então
o pooling empurra o denominador de "independência" para cima e a razão
aparente para baixo, mecanicamente — o mesmo formato de erro já visto
duas vezes nesta sessão (limiar fixo; inflação por não-unidades no
arco). Detectado antes de aceitar os números. Corrigido calculando
`d1(x)` e `d2(x)` por fase separadamente, com checagem gratuita
`d1(x)=d2(2x)` (forçada por F1, bate exatamente em todos os níveis
testados) e comparando contra a linha de base correta
`E[d(fase_a)*d(fase_b)]`.

```text
ell   razão=pair/(d1*d2)   theta implícito (base d1)
 8         0.379                  3.05
10         0.237                  3.32
12         0.100                  3.81
14         0.024                  4.56
16        0.0015                  5.91
18       ~0.00000                 8.80    <- só 2 acertos, ver nota abaixo
```

**Nota sobre `ell=18`**: contando acertos exatos por tipo de par,
`ell=18` tem só 2 acertos no total (0 no Tipo (1,2), 2 no Tipo (2,1)),
contra ~86 milhões de pares candidatos. Uma razão calculada com 2
acertos não é uma medição de nada, é o retrato de um único par
observado expresso como fração. O ponto de `ell=18` é consistente com
a tendência continuar, mas não fornece evidência real disso — em
`eps=0.1` o limiar já esgota o sinal utilizável por volta desse nível,
mesmo com o baseline corrigido.

A razão corrigida é próxima da versão poolada e cai um pouco MAIS
rápido, não menos: consertar o artefato de pooling não explicou o
sinal, ao contrário do que seria a expectativa natural para esse
formato de viés. Separado por tipo de par (ambos contra a mesma linha
de base `d1*d2`):

```text
ell   razão (1,2)   acertos (1,2)   razão (2,1)   acertos (2,1)
 8      0.423            72            0.335           57
10      0.268           275            0.205          210
12      0.100           588            0.101          596
14      0.020           619            0.028          861
16     0.0008           104           0.0023          310
```

Os dois tipos mostram o mesmo padrão qualitativo (razão caindo, sem
sinal de estabilizar), com contagens de acerto comparáveis — o
resultado poolado não é artefato de um tipo dominar o outro.

A razão cai bem abaixo de 1 e continua caindo; o `theta` implícito não
converge a uma constante, CRESCE. Um `theta` fixo já daria o teorema
condicional acima com folga (qualquer `theta>1` já é útil); um `theta`
crescente sugeriria descorrelação ainda mais forte que a Hipótese (D)
pedia. Mas 5 pontos até `ell=16` não bastam para distinguir "expoente
genuinamente crescente" de "aproximação lenta a um expoente maior
fixo" de "efeito de alcance finito que não persiste"; além disso, em
`eps=0.1` o limiar testado (`d1(x)` entre 0.40 e 0.19) fica no grosso
da cauda, não na cauda profunda que o teorema exige
(`x ~ exp(-c0 ell)` com `c0>=log(3)/(2 kappa)`), e empurrar `eps` mais
fundo esbarra na mesma parede do arco (o limiar cai abaixo do menor
`N` observado por volta de `ell~14`). É o sinal quantitativo mais
forte desta linha de investigação até agora, não uma prova de taxa
nenhuma. Ver `projects/collatz/experiments/E-132-pair-decoupling-exponent/`.

### Avaliação e próximos passos

Nenhum erro nas identidades básicas desta rodada (ao contrário das
duas rodadas anteriores, tudo verificado passou de primeira) — mas a
própria medição de E-132 teve um bug de mesma família (marginais
poolados incorretamente), corrigido antes de ser aceita, ver acima.
Provado nesta rodada: F1, F3, F4, F2 (os dois tipos), a exclusão sem-
deslocamento de Q1, o teorema condicional par->beta. Heurístico, não
provado: a plausibilidade de Q2 ser verdadeira, o programa de Weyl, a
leitura de Q1 em escala `Theta(ell)`. Aberto: a desigualdade de par em
si (o conteúdo real de Q2), que E-132 (já corrigido, separado por tipo
de par) tem evidência empírica forte a favor. Próximos passos
concretos, nenhum tentado ainda: medir em mais níveis (`ell=18` em
andamento) e mais valores de `eps` para ver se `theta` estabiliza;
tentar a indução de Weyl esboçada acima usando a estrutura de cilindro
de F4 (cilindros de profundidade `L` em `u` correspondem a progressões
aritméticas de módulo `3^L` em tempo de órbita — a ponte que falta
entre a álgebra e as somas de Weyl).
