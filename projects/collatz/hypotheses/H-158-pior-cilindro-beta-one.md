# H-158: massa do pior cilindro na lei de Syracuse

Status: em andamento

Criada: 2026-08-08

## Alvo

Para a lei de Syracuse `mu_ell` módulo `3^ell`, defina

```text
c_ell=min_(3 does not divide a) mu_ell(a).
```

Decidir se

```text
3^ell c_ell = exp(-o(ell)),
```

equivalentemente `beta_eff(ell)->1`. Esta é a forma de pior cilindro
da estimativa ponderada `beta=1`.

## Estado conhecido

H-131 prova que a Weak Covering Conjecture, por si só, não fornece essa
estimativa. H-148 prova que até uma distribuição ideal das representações
na fatia de custo da WCC deixa massa exponencialmente insuficiente.
E-111 calculou `c_ell` até `ell=12`, com `beta_eff` decrescendo até
`1.222938`; isso é evidência finita e não decide o limite.

## Próximos testes

1. ~~Estender o cálculo do pior cilindro sem executar o DP de custo
   mínimo.~~ Feito (E-127, até `ell=18`).
2. ~~Registrar o resíduo minimizante em coordenadas aditiva e
   logarítmica.~~ Feito: E-127 já reporta `argmin` (aditiva) e
   `log2_argmin` (logarítmica, base 2) a cada nível.
3. ~~Separar a contribuição por faixas do custo microcanônico.~~ Feito
   (E-130): ver "Atualização E-130" abaixo.
4. Procurar uma desigualdade recursiva subexponencial para o mínimo.
   Tentado nesta sessão (consulta a modelo mais forte, Regra 11b, mais
   verificação independente nossa). Resultado: uma desigualdade
   recursiva ESCALAR (`c_ell` em função só de `c_(ell-1)`) provavelmente
   não pode funcionar (ver "Atualização: tentativa do passo 4" abaixo).
   A pergunta foi reformulada como uma condição estrutural sobre a
   órbita de um mapa afim explícito, registrada como H-161. Continua em
   aberto.

## Atualização E-127 (estendida a `ell=18`)

O cálculo direto foi estendido até `ell=18`, sem executar o DP de custo.
Os valores completos de `ell=12` a `18` foram

```text
ell   beta_eff    3^ell c_ell
 12   1.222938    0.0529150
 13   1.209617    0.0500995
 14   1.198911    0.0469172
 15   1.189390    0.0441133
 16   1.179102    0.0429289
 17   1.170057    0.0417504
 18   1.162241    0.0404242
```

Um ajuste descritivo nos níveis `6<=ell<=18` dá `3^ell c_ell`
proporcional a `exp(-1.084099)*ell^(-0.744288)` (substitui o ajuste
anterior, `ell^(-0.773)` sobre `6<=ell<=15`; a mudança de expoente ao
incluir três níveis a mais mostra que esse ajuste é sensível ao
intervalo, não um expoente estável). Isso é compatível com perda
subexponencial, mas o intervalo continua curto e não constitui uma
conclusão assintótica. O resíduo minimizante muda de ramo várias vezes
(coluna `same_parent` de E-127); no total de 17 transições testadas
(`ell=1` a `18`), pouco mais da metade são levantamentos do minimizante
anterior.

## Atualização E-130: decomposição por faixa de custo (passo 3)

A recursão sem memória de Tao, desenrolada em série geométrica, dá uma
coordenada de custo gratuita: `mu_ell(y) = soma_s 2^-(s+1) *
nu(2^-(s+1) y mod 3^ell)`, onde `s` conta duplicações extras antes de
recair na lei do nível anterior. Comparado ao resíduo de massa MÁXIMA
(dominado quase inteiramente pelo termo `s=0`, que sozinho excede 99%
do total a partir de `ell=5`) e ao de massa mediana (precisa de poucos
termos, `s` até ~1-6 para 90%), o resíduo de massa MÍNIMA (`c_ell`)
precisa consistentemente de mais bandas: `s` até 5 para 90%, até 9-11
para 99%, em todos os níveis de 2 a 15 testados. Nenhum dos três limiares
mostra tendência com `ell` no intervalo testado.

Achado descritivo, não assintótico: o déficit do pior resíduo não vem
de um único caminho barato dominante (como no resíduo de massa máxima);
ele recebe contribuições comparáveis de várias bandas de custo. Não
identifica uma desigualdade recursiva (passo 4) nem se conecta à
variável de custo do DP de custo mínimo de E-111 (uma coordenada
diferente, mais cara, que este experimento evita computar). Ver
`projects/collatz/experiments/E-130-worst-cylinder-cost-bands/`.

## Atualização: tentativa do passo 4 (2026-08-08)

Consultado um modelo mais forte (Fable, Regra 11b) com contexto
completo (definições, H-131, H-148, a extensão de E-127/E-130). Cada
alegação foi verificada de forma independente antes de aceitar
(Regra 8c) — nem tudo passou. Resultado, separado por grau de
confiança:

**Provado e verificado por nós, de forma independente (não só lendo o
script da consulta, rederivado do zero e conferido contra
`weighted_bridge.py`):** a recursão `mu_ell(y) = 1/2 nu(2y) + 1/2
mu_ell(2y)` (potências CRESCENTES de 2, corrigindo uma tentativa nossa
anterior na direção errada) admite reindexação exata: para `y` unidade
com `t0(y) in {1,2}` o menor `t>=1` tal que `2^t y == 1 (mod 3)`, o
passo `t -> t+2` age sobre `z=2^t y` como `z -> 4z`, e escrevendo
`z=1+3k` isso vira o mapa afim `A(k)=4k+1 (mod 3^(ell-1))`, um único
ciclo de comprimento `3^(ell-1)` cobrindo todo `Z/3^(ell-1)Z`. Disso:

```text
mu_ell(y) = 2^-t0(y) * sum_j 4^-j mu_(ell-1)(A^j(k0(y)))
c_ell = (1/4) min_k G(k),  G(k) = sum_j 4^-j mu_(ell-1)(A^j(k))
```

Verificado a ~1e-14 contra a implementação de referência, para vários
níveis, com código escrito do zero (não reaproveitando o script da
consulta). Desta identidade seguem duas cotas elementares, também
conferidas por nós:

- Cota de um termo: a primeira posição-unidade da janela está em
  `j<=1`, logo `c_ell >= c_(ell-1)/16`, ou seja `beta <= 2.523719`.
- Cota da soma no pior caso de fase: somando `4^-j` sobre todas as
  posições-unidade na fase mais desfavorável (`k==0 mod 3`), o fator
  é `20/63`, dando `c_ell >= (5/63) c_(ell-1)`, ou seja
  `beta <= 2.306270` (recalculado por nós; a consulta original errou
  esse número em ~0.003, provavelmente arredondamento).

**Plausível, esboço de prova não rederivado linha a linha por nós:**
um argumento adversarial (construir uma medida hipotética de nível
`ell-1` com um bloco de valores todos iguais ao mínimo ao longo de um
arco de `A`) sugere que NENHUMA desigualdade que use só o valor escalar
`c_(ell-1)` (ou qualquer lista finita de estatísticas de ordem, sem
informação posicional) pode fazer melhor que aproximadamente essa
mesma cota `beta<=2.31`. Se correto, isso responde ao passo 4 como
originalmente formulado: uma desigualdade recursiva ESCALAR não pode
provar `beta=1`; qualquer prova precisa de informação sobre ONDE ao
longo da órbita de `A` os valores pequenos de `mu_(ell-1)` estão, não
só de quão pequenos eles são.

**Conjectural, com suporte empírico não conclusivo:** a consulta propôs
uma hipótese de descorrelação (não conspiração da cauda inferior de
`mu_(ell-1)` ao longo de janelas da órbita de `A`) que implicaria
`3^ell c_ell >= exp(-O(sqrt(ell)))`, logo `beta_eff -> 1`. A alegação
de suporte empírico ("arcos deficientes não crescem com `ell`") não
se sustentou na primeira checagem: o script usado testava limiares
FIXOS (0.2, 0.3, 0.5), não o limiar `exp(-eps*ell)` que a própria
reformulação exige. A um limiar fixo, a fração de posições abaixo dele
CRESCE com `ell` (verificado: de 0.179 em `ell=8` a 0.204 em
`ell=14`), então mesmo um arranjo i.i.d. aleatório das mesmas
frequências produziria um maior-arco crescendo como `log(N)/log(1/p)`,
linear em `ell` — e de fato a coluna de limiar 0.5 cresce claramente
(5,5,5,8,8,11,11 em `ell=8..14`), contradizendo a alegação de "achado
plano" da consulta. As colunas de limiar mais estrito (0.2, 0.3)
crescem mais devagar (3→5 e 2→4), mas 7 pontos não bastam para
distinguir `O(1)`, `O(log ell)` ou algo pior. Refeita a medição com o
limiar correto (`exp(-eps*ell)`) e uma linha de base de arranjo
aleatório explícita (`ell=8` a `18`): o arco observado fica abaixo da
linha de base aleatória na quase totalidade dos níveis e, em
`eps=0.1`, diminui (5→3) enquanto a linha de base sobe e estabiliza
(6.89→8.13→7.87) — sinal de anti-aglomeração real, não só ausência de
aglomeração, mas o intervalo (11 pontos) é curto demais para
extrapolar. Ver H-161 para a reformulação, o critério de teste correto
e a tabela completa.

**Não registrado como achado, por falta de sustentação:** o veredito
da consulta de que "`beta_eff -> 1` é verdadeiro" foi descartado. É o
julgamento heurístico de um único modelo, apoiado em parte numa
estatística que, como medida, não consegue distinguir os dois
cenários (ver acima). Nem confirma nem refuta H-158.

Reformulação estrutural (arco deficiente ao longo da órbita de `A`)
registrada como H-161, separada desta hipótese por não ser uma
auditoria computacional e sim uma nova pergunta em aberto (Regra 8e).
