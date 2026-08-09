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
