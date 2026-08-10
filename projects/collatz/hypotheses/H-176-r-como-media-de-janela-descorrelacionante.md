# H-176: R_ell como operação descorrelacionante (por que a razão de par cai)

Status: fechada-refutada (2026-08-10). Ver "Fechamento" no fim.

Criada: 2026-08-10

Origem: pista aberta na "Terceira rodada" de H-161 (2026-08-09, item 3
de "Pistas abertas"), nunca antes registrada como hipótese própria.
Número escolhido para não colidir com outros agentes rodando em
paralelo nesta sessão (estado do repositório nesta rodada ia até
H-175); renumerar na integração se necessário.

## O que já se sabe

H-166 prova que `R_ell(u) := N_ell(u)/N_{ell-1}(u mod 3^{ell-1})`
satisfaz `R_ell(k) = combinação convexa de valores de R_{ell-1}` ao
longo da órbita de `A` (a mesma identidade que dá a monotonicidade de
`min R`). Ou seja: `R_ell` em cada ponto é literalmente uma MÉDIA
PONDERADA (janela geométrica de peso `4^{-j}`) de `R_{ell-1}` ao longo
da órbita de `A`.

Separadamente, E-132 (H-161) mediu que a razão `pair(x)/(d1(x)*d2(x))`
(cauda conjunta de um par consecutivo de `N` pequenos, contra o produto
das marginais) cai monotonicamente e com força crescente em `ell`
(`theta` implícito de `3,05` em `ell=8` a `5,91` em `ell=16`), sinal
de descorrelação real, mais forte que independência, sem explicação
mecanística registrada além da observação qualitativa "pode ser a
mesma operação de médias por janela".

## Pergunta

A identidade de combinação convexa de H-166 (`R_ell` = média de janela
de `R_{ell-1}`) É, ela mesma, um mecanismo de descorrelação suficiente
para explicar (ou até provar uma versão de) o que E-132 mede
empiricamente? Médias por janela geométrica de uma sequência ao longo
de uma órbita ergódica são um objeto clássico (soma de Birkhoff
ponderada); a teoria de mixing/decaimento de correlações para esse
tipo de média (para o mapa `A`, que é multiplicação por 4 num grupo
cíclico, um mapa MUITO simples, sem mixing genuíno por si só, já que
é uma rotação/multiplicação em grupo finito) tem alguma coisa a dizer
sobre por que médias sobrepostas (janela de `k` vs janela de `k+1`,
que compartilham quase todos os termos) ficam descorrelacionadas em
vez de correlacionadas?

## Por que vale investigar

Se este mecanismo for real e quantificável, dá exatamente o `kappa` que
Q2 de H-161 precisa (`kappa>0,567`), por uma via estrutural (a própria
identidade de H-166) em vez de uma estimativa harmônica externa (que já
falhou três vezes, ver H-161 "Terceira rodada" e H-175). É a pista mais
barata de todas as registradas aqui porque não pede NENHUMA ferramenta
nova, só olhar de novo para uma identidade já provada com a pergunta
certa.

## Contra-argumento óbvio, a checar antes de investir

Médias de janela SOBREPOSTA classicamente aumentam a correlação (não
diminuem) entre pontos próximos, porque compartilham a maior parte dos
termos, o oposto do que seria preciso aqui. Se isso for o caso
dominante, a observação (3) desta hipótese e a medição de E-132 seriam
uma coincidência de escala, não uma relação causal, e a hipótese fecha
refutada rápido. Vale checar isso primeiro (analiticamente, com um
exemplo pequeno) antes de qualquer coisa mais cara.

## Primeiro passo barato

Calcular `Corr(R_ell(k), R_ell(A(k)))` (correlação entre `R` em pontos
CONSECUTIVOS da órbita, não a correlação de par de `N`/`W` que E-132
já mediu) diretamente dos dados já existentes de `min R`/`R_ell`
(E-134) para `ell` pequeno a moderado, e comparar contra a mesma
quantidade para uma sequência i.i.d. sintética com a mesma marginal.
Se `R_ell` já é POSITIVAMENTE correlacionado ponto a ponto (esperado
pelo contra-argumento acima), a pista provavelmente não explica a
descorrelação de E-132 e deve fechar refutada sem mais trabalho.

## Fechamento (2026-08-10)

Executado o passo barato: para `k` unidade, tomado o ramo `t0=1`
(representante `y=(3k+1)*inv(2) mod 3^ell`), medido
`R_ell(y(k))` contra `R_ell(y(A(k)))`, `ell=4` a `14`, reusando
`float_levels` de `E-134/cascade_factor_bound.py` (nenhum código novo
de lei, só a extração da razão e a correlação).

```text
ell   corr(R(k), R(A(k)))   corr(R, R embaralhado)
 4          0.401                  -0.065
 6          0.504                   0.002
 8          0.510                   0.010
10          0.530                   0.002
12          0.539                  -0.003
14          0.546                   0.007
```

Exatamente o contra-argumento previsto: `R_ell` é POSITIVAMENTE
correlacionado entre pontos consecutivos da órbita de `A` (correlação
`0,40` a `0,55`, crescendo e estabilizando, contra `~0` para uma
permutação aleatória do mesmo vetor). Médias de janela sobreposta
correlacionam pontos próximos, não os descorrelacionam. A intuição
padrão vale aqui, sem surpresa.

**Veredito**: `fechada-refutada` para a pergunta EXATA pré-registrada
(correlação de Pearson em massa, sobre toda a distribuição de `R`).
**Correção de escopo (2026-08-10, segunda rodada de crítica)**: a
frase original aqui ("os dois fenômenos não têm o mesmo mecanismo,
pelo motivo mais simples possível") extrapolava demais. Uma correlação
de Pearson positiva EM MASSA não exclui anti-concentração conjunta na
CAUDA PROFUNDA a um limiar escalado `exp(-eps*ell)`, que é o que Q2
(H-161) realmente precisa; correlação positiva no grosso da distribuição
é compatível, em princípio, com descorrelação nas caudas extremas. O
que fica estabelecido é mais estreito: a identidade de combinação
convexa de H-166 NÃO explica a descorrelação de E-132 via este
mecanismo específico (correlação em massa entre pontos consecutivos de
`R`); não fica estabelecido que os dois fenômenos sejam
estruturalmente independentes em geral.

**Escalonamento (Regra 11b)**: não necessário. O contra-argumento
registrado na abertura da própria hipótese já previa este resultado, e
a medição confirmou sem ambiguidade.

Script persistido como experimento formal (2026-08-10, depois de uma
crítica apontar que a única evidência por trás de um veredito
`fechada-refutada` vivia só em prosa, não em código rodável):
`experiments/E-143-r-adjacent-correlation/` (script, README, saída
persistida).