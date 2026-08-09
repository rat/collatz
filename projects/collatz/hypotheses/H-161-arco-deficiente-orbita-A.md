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

**(B) "beta_eff -> 1" implica "nenhum arco cresce" — NÃO FECHA sem uma
hipótese extra sobre `N_max`.** A volta pediria: dado um arco curto
(digamos, de comprimento `m`) com `N` pequeno no COMEÇO da janela,
concluir que a soma INTEIRA `G(k)` (incluindo a cauda além do arco,
`j>=m`) também é pequena. Isso exige controlar
`max_u N_(ell-1)(u)` (o valor MÁXIMO possível na cauda, não só no
arco). Provamos uma cota a priori limpa, por indução na própria
recursão (`mu_ell(y) = 1/2 nu(2y) + 1/2 mu_ell(2y)`, logo
`M_ell <= (2/3) M_(ell-1)` onde `M_ell = max_u mu_ell(u)`, com base
`M_1=2/3`): `M_ell <= (2/3)^ell`, ou seja `N_max <= 2^ell` SEMPRE.
Mas essa cota só fecha a volta para arcos de comprimento
`m >= ell*(log2 + eps)/log4 ~ 0.5 ell` — MUITO maior que os arcos
observados (3 a 5, ver dados abaixo). Medido o comportamento real de
`N_max` (não só a cota): `N_max` cresce como `(3/2)^ell` quase
exatamente (razão por nível convergindo a 1.5000 já em `ell~10`, ver
tabela abaixo) — melhor que a cota provada, mas ainda EXPONENCIAL, não
limitado. Usando essa taxa (empírica, não provada) em vez da cota
crua, o comprimento crítico cai para `~0.29 ell`, mas isso AINDA excede
os arcos observados a partir de `ell~14` (crítico `~4.7` contra arco
observado `4`, piorando: crítico `6.6` contra arco `3` em `ell=18`).

**Conclusão**: a direção útil (A) está provada e não precisa de nada
além da identidade de base. A direção (B) — que seria necessária para
usar um arco longo hipotético como REFUTAÇÃO, ou para provar que arco
curto é NECESSÁRIO para `beta_eff->1`, não só suficiente pelo lado
certo — continua em aberto, e os dados atuais não bastam para fechá-la
mesmo com a taxa empírica de `N_max`. Isso não invalida usar os dados
de arco curto como evidência a favor de `beta_eff->1` (via (A)); só
significa que a formulação "sse" da consulta original estava incorreta
e que "arco curto" não é (ainda) um critério equivalente, só suficiente
por um lado.

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

## Primeira medição com limiar correto (2026-08-08, estendida a ell=19)

Medido `exp(-eps*ell)` para `eps=0.1` e `eps=0.2`, níveis `ell=8` a
`19` (estendido de 18 para 19; ir além de 19 com o método rápido atual
exigiria mais memória do que é seguro usar nesta máquina de uma vez —
o array de nível 20 chegaria perto de 90GB, o processo foi interrompido
antes de tentar alocá-lo), contra a linha de base de arranjo aleatório
`log(N)/log(1/p_ell)` (`N`= número de posições-unidade na órbita,
`p_ell`= fração observada abaixo do limiar naquele nível):

```text
eps=0.1:
ell    frac      arco_observado   linha_de_base
 8   0.29630          5              6.89
 9   0.26947          5              7.23
10   0.24539          5              7.53
11   0.22203          5              7.76
12   0.19951          5              7.93
13   0.17812          5              8.04
14   0.15774          4              8.11
15   0.13851          4              8.13
16   0.11999          4              8.10
17   0.10219          4              8.01
18   0.08545          3              7.87
19   0.07028          2              7.71

eps=0.2:
ell    frac      arco_observado   linha_de_base
 8   0.09785          2              3.61
 9   0.06889          2              3.54
10   0.04550          2              3.42
11   0.02809          2              3.27
12   0.01339          2              2.96
13   0.00348          2              2.45
14   0.00039          2              1.91
15   4.8e-6           2              1.31
16-18  0 posições abaixo do limiar (arco trivial)
```

Em ambos os limiares, o arco observado fica ABAIXO da linha de base
aleatória em quase todo o intervalo (a única exceção é `eps=0.2`,
`ell=13-15`, onde a linha de base cai abaixo de 2 simplesmente porque
`p_ell` fica minúsculo, tornando qualquer arco de tamanho >=1
estatisticamente "acima do esperado" por definição quando há pouquíssimas
posições no total). Em `eps=0.1`, o arco observado não só não cresce
como DIMINUI (5 → 2 de `ell=8` a `19`) enquanto a linha de base
aleatória sobe e depois se estabiliza (6.89 → 8.13 → 7.71). Isso é
evidência a favor de anti-aglomeração real (não apenas ausência de
aglomeração) dos pontos deficientes ao longo da órbita de `A`,
consistente com a Hipótese (D) proposta na consulta original — mas o
intervalo (`ell=8` a `19`, 12 pontos) é curto demais para distinguir um
efeito assintótico genuíno de uma flutuação finita, e (ver seção
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
