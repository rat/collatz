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

## Enunciado (a verificar; a álgebra é elementar dado o acima, mas não
foi rederivada linha a linha por nós, só a identidade de base)

Defina `N_ell(u) = 3^ell mu_ell(u)`. Para todo `eps>0`, considere o
maior arco consecutivo de `A` (na órbita de nível `ell`) contido no
conjunto `{u : N_ell(u) <= exp(-eps*ell)}`. A alegação é:

```text
beta_eff(ell) -> 1  <=>  para todo eps>0, esse maior arco tem
                          comprimento o(ell).
```

Direção fácil: se `3^(ell+1) c_(ell+1) <= exp(-eps*ell)`, cada termo da
soma geométrica do minimizador satisfaz `4^-j N_j <= 4 exp(-eps*ell)`,
dando uma janela de comprimento `~eps*ell/(2 log4)` com
`N_j <= exp(-eps*ell/2)` — decorre direto da identidade acima. A volta
(arco curto implica `c_ell` não pode ser pequeno demais) é a mesma
conta ao contrário.

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

## Primeira medição com limiar correto (2026-08-08)

Medido `exp(-eps*ell)` para `eps=0.1` e `eps=0.2`, níveis `ell=8` a
`18`, contra a linha de base de arranjo aleatório
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
como DIMINUI (5 → 3) enquanto a linha de base aleatória sobe e depois
se estabiliza (6.89 → 8.13 → 7.87). Isso é evidência a favor de
anti-aglomeração real (não apenas ausência de aglomeração) dos pontos
deficientes ao longo da órbita de `A`, consistente com a Hipótese (D)
proposta na consulta original — mas o intervalo (`ell=8` a `18`, 11
pontos) é curto demais para distinguir um efeito assintótico genuíno de
uma flutuação finita. Script limpo e commitado em
`projects/collatz/experiments/E-131-affine-orbit-reformulation/deficient_arc_scan.py`
(reescrito do zero a partir da versão exploratória usada na consulta,
que ficou só no scratchpad da sessão).

Cross-check: a coluna `min_N` do script bate exatamente com `3^ell c_ell`
já verificado em E-127 (`ell=12`: 0.052915; `ell=18`: 0.040424),
confirmando que a reimplementação rápida usada aqui está correta.

**Avaliação**: sinal real, mas preliminar — o suficiente para justificar
`in-progress` em vez de `open-unexplored`, não para fechar H-158 nem
para promover esta hipótese a confirmada. Próximo passo natural:
estender a faixa de `ell` (o método rápido usado aqui, `circ_geom_half`,
é O(M log M) por nível via duplicação binária, bem mais barato que a
recursão ingênua — deveria alcançar `ell~25-30` sem dificuldade) para
ver se a tendência de queda em `eps=0.1` persiste ou se estabiliza.
