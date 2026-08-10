# H-163: cancelamento bilinear entre irmãs sem decaimento pontual nem l2

Status: fechada-inconclusiva (2026-08-10). Uma primeira tentativa de
fechamento (mesma sessão) marcou isto como `fechada-confirmada`; um
crítico independente (Regra 8/15) encontrou, e eu confirmei de forma
independente (Regra 8c, controles rodados de novo por mim), que a
medição original é um artefato sem relação com irmandade. Ver a seção
"Fechamento" (reescrita) no fim do arquivo para a análise completa,
incluindo o registro honesto do erro original.

Status anterior (histórico): backlog

Criada: 2026-08-09

Origem: passe dirigido a O4 de 2026-08-09, registrado em H-115. É a única
rota que aquela análise deixa de pé, e é registrada aqui por Regra 8e,
não porque haja indício de que funcione.

## Pergunta

A rota de segundo momento precisa que

```text
Cov ~ sum_{xi != 0} S_1(xi) * conj(S_2(xi))
```

seja pequena depois de removidos os modos afins grosseiros exatos
(H-126, Prop. 2), onde `S_1` e `S_2` são as somas de caracteres tipo
Syracuse condicionadas no primeiro passo, uma por irmã.

Toda tentativa registrada até hoje ataca isso por uma cota em cada fator
separadamente: cota pontual uniforme, ou Cauchy-Schwarz sobre o
somatório. H-115 (passe de 2026-08-09) mostra que as duas estão barradas
pelo mesmo lado. A cota pontual uniforme com power-saving implicaria
`K_infinity < infinity`, e é contrariada em nível finito pela medição de
E-137 (`sup * 3^(ell/2)` cresce de 1,13 para 61,7 entre `ell=2` e
`ell=15`). Cauchy-Schwarz gasta exatamente `K_ell - K_(r_ell)`, que
cresce linearmente sob o platô medido `E_r ~ 0,47`.

A pergunta que sobra: existe cancelamento na FASE RELATIVA entre
`S_1(xi)` e `S_2(xi)`, uniforme o bastante sobre `xi`, que torne o
pareamento pequeno sem que nenhum dos dois fatores decaia?

## Por que não é obviamente vazia

As duas irmãs não são independentes nem iguais. Elas diferem apenas pelo
primeiro passo. Pela recursão de Tao (eq. 1.22), condicionar no primeiro
passo `a_1 = j` multiplica o argumento por `2^(-j)` e translada por
`2^(-j)`, isto é, atua em `xi` por dilatação `xi -> 2^j xi` mais uma fase
linear. Logo `S_1(xi)` e `S_2(xi)` são, a menos dessas fases, valores da
MESMA função em frequências relacionadas por potências de 2 módulo
`3^ell`. O pareamento não é um produto de dois objetos arbitrários, é uma
correlação da função consigo mesma ao longo da órbita de duplicação.

Isso é exatamente onde E-137 vê estrutura: o maximizador do coeficiente
primitivo fica na órbita de `1` sob duplicação em quase todo nível. Ou
seja, o mesmo lugar onde a energia se concentra é o lugar onde os dois
fatores estão relacionados. Pode ser que a concentração ajude o
cancelamento em vez de atrapalhar, e pode ser que ela seja justamente a
ressonância que impede o cancelamento. Nenhuma das duas foi testada.

## Primeiro teste barato, antes de qualquer teoria

Calcular, para `ell` pequeno e um par de irmãs explícito, a soma
`sum_xi S_1(xi) conj(S_2(xi))` e compará-la com:

1. o orçamento trivial de Cauchy-Schwarz `sqrt(E_1) * sqrt(E_2)`;
2. o valor que sairia se as fases relativas fossem aleatórias
   (aproximadamente `sqrt(sum_xi |S_1|^2 |S_2|^2)`).

Se o valor medido ficar perto de (1), não há cancelamento e a rota morre
com um número. Se ficar perto de (2) ou abaixo, há cancelamento de fase e
a pergunta seguinte é se a taxa é suficiente e uniforme em `ell`. Custo
esperado: o mesmo da recursão de E-137, poucos minutos até `ell=12`.

E-129 já mede algo vizinho (agregação sobre o intervalo entre irmãs
contra o acoplamento de dígitos novos) e deve ser lido antes, para não
repetir a mesma medida com outro nome.

## Precedentes verificados antes de abrir

Grep em `hypotheses/` por rotas já fechadas sobre o mesmo objeto: H-126
(componente grosseira exata, sobrevive; lema condicional caiu por
`K_infinity`), H-127 (dicotomia espectral; ramo difuso inacessível a
métodos l¹ por uma parede exata de constantes), H-149 (buraco de suporte
não força espectro primitivo), H-153 (não equivalência dos vetores de
custo latentes, que não transfere para resíduos). Nenhuma delas ataca o
pareamento bilinear diretamente. Esta hipótese não repete nenhuma.

## Expectativa honesta

Baixa. Cancelamento bilinear sem decaimento em nenhum fator é raro e,
quando ocorre, costuma vir de uma estrutura algébrica que aqui seria
justamente a rigidez `x2, x3` que H-115 já identificou como território
sem ferramenta. O motivo para registrar mesmo assim é que é a última
formulação não refutada do alvo de O4, e o primeiro teste custa poucos
minutos.

## Primeira tentativa de fechamento (2026-08-10), depois retratada

Uma primeira passada mediu `S_1`, `S_2` por enumeração ponderada real
(dois irmãos = dois menores expoentes de primeiro passo admissíveis em
`v`; `S_i` soma sobre toda a subárvore admissível de profundidade
`ell-1`, peso real `prod_j 2^{-a_j}`, avaliada em `e(xi*leaf/3^ell)`).
`ratio_CS` e `ratio_RP` pareciam cair monotonicamente com `ell` em toda
raiz testada, e o veredito registrado foi `fechada-confirmada` (caso
(2) do critério pré-registrado: cancelamento de fase real). Esse
veredito estava errado, pelo motivo abaixo, e a leitura da tabela em si
já não era exata (várias das linhas resumidas escondiam exceções reais,
por exemplo `v=17` chegando a `ratio_RP=1,9986` em `ell=4`, contra o
"nunca perto de (1)" que o texto original afirmava).

## Fechamento correto (2026-08-10, mesma sessão): a medição original é um artefato

Um crítico independente (Regra 8/15, subagente com contexto fresco)
recomputou tudo do zero, incluindo dois controles que a primeira
passada nunca rodou, e encontrou o problema real. Verifiquei cada
alegação de forma independente (Regra 8c) antes de aceitar, refazendo
os controles com meu próprio código, não copiando o do crítico.

**O mecanismo exato.** Por Parseval, para `h_i` o histograma ponderado
de resíduos de `S_i` e `m=3^ell`:

```text
sum_{xi=0}^{m-1} S_1(xi) conj(S_2(xi)) = m * <h_1, h_2>   (produto interno dos histogramas)
```

O termo `xi=0` sozinho vale `S_1(0)*conj(S_2(0)) = m_1*m_2` (`m_i` = massa
total de `h_i`). Logo

```text
measured := sum_{xi!=0} S_1(xi) conj(S_2(xi)) = m*<h_1,h_2> - m_1*m_2.
```

**Correção (2026-08-10, segunda rodada de crítica): o parágrafo abaixo
estava errado sobre ONDE mora o efeito, mesmo com o veredito certo.**
Os suportes de `h_1` e `h_2` NÃO são minúsculos: são PLENOS (todo
resíduo coprimo com 3, `(2/3)*3^ell` pontos, verificado diretamente
com `(h>0).sum()`: `4374` de `6561` em `ell=8`, `354294` de `531441`
em `ell=12`, mesmo suporte para os dois irmãos). O que é pequeno é a
RAZÃO DE PARTICIPAÇÃO (`m_i^2/||h_i||_2^2`, uma contagem de "átomos
efetivos", cerca de 11 a 85 nos casos medidos), uma estatística
diferente do tamanho do suporte, que eu confundi na primeira versão
desta correção. O peso de ramo não renormalizado (`prod 2^{-a_j}`)
concentra quase toda a massa num punhado de resíduos "pesados" dentro
do suporte pleno; os resíduos pesados dos dois irmãos raramente
coincidem. Medido diretamente: `m*<h_1,h_2>/(m_1*m_2)` fica entre
`0,03` e `0,5` nos casos testados (não `~0`; há exceção clara em
`v=17, ell=4`, onde vale `5,8`), o suficiente para que `measured`
fique dominado pelo termo `-m_1*m_2` na maioria dos casos, mas não por
um argumento de suporte esparso. `|measured|` continua sem carregar
informação de fase específica de irmandade (é isso que os dois
controles abaixo mostram diretamente), só que o motivo é concentração
de massa dentro de um suporte pleno, não ausência de suporte.

**Verificado com dois controles, refeitos por mim de forma
independente** (não só lendo os números do crítico):

- Controle B: dilatar `h_2` por um resíduo aleatório `u` (permuta as
  frequências, preserva toda norma exatamente, destrói qualquer relação
  aritmética real entre os dois irmãos). Um único sorteio é ruidoso
  (achado do crítico, segunda rodada: a mesma célula lia de `0,04` a
  `0,11` conforme o sorteio); corrigido para reportar a MEDIANA de 5
  sorteios independentes, com sementes gravadas no código
  (`control_dilation_median`), não um número interativo avulso.
- Controle C: substituir o segundo irmão pela subárvore de uma raiz
  completamente não relacionada (`v'=1000003+6v`).

Saída persistida (não regenerada ad-hoc) em
`experiments/E-140-bilinear-sibling-pairing/controls_ell8_10_12.txt`:

```text
v    ell   ratio_RP (irmãos reais)   ratio_RP (dilatação, mediana de 5)   ratio_RP (raiz não relacionada)
 1     8         0.1304                        0.0680                              0.0822
 1    10         0.0559                        0.0487                              0.0406
 1    12         0.0359                        0.0480                              0.0343
 5     8         0.0961                        0.1011                              0.1467
 5    10         0.0523                        0.0511                              0.0897
 5    12         0.0337                        0.0296                              0.0429
11     8         0.1147                        0.1185                              0.0624
11    10         0.0513                        0.0541                              0.4688
11    12         0.0363                        0.0205                              0.0139
17     8         0.1377                        0.1224                              0.1218
17    10         0.0432                        0.0881                              0.0837
17    12         0.0165                        0.0443                              0.3207
```

Os controles cobrem a mesma faixa (ou uma faixa maior) que os irmãos
reais em toda profundidade testada; em duas células a diferença é
grande na direção que FORTALECE a conclusão, não que a enfraquece
(`v=11, ell=10`: controle não relacionado `0,4688` contra real
`0,0513`; `v=17, ell=12`: `0,3207` contra `0,0165`). O que E-140 media
não era uma propriedade do par de irmãos.

**Consequência para a regra de decisão pré-registrada**: o caso (1) do
critério original ("medido perto do orçamento trivial de
Cauchy-Schwarz, `sqrt(E_1*E_2)`") exigiria `h_1` proporcional a `h_2`,
o que duas subárvores diferentes essencialmente nunca satisfazem para
`ell>2`. A regra de decisão como formulada não tinha como dar o
resultado (1); o resultado (2) era o único alcançável, e chegar nele
não carregava a informação que se pensava carregar. Um critério de
fechamento que só pode dar uma resposta não decide nada; isso deveria
ter sido percebido antes de rodar, não depois.

**Onde a construção original errou (achado colateral, real; corrigido
na segunda rodada de crítica)**: o alvo de H-115/H-126 é a decomposição
de Tao `mu_ell = sum_j 2^{-j} mu_ell^{(j)}` (medida IDEALIZADA, suporte
espalhado por todos os resíduos unidade mod `3^ell`), com os modos
afins grosseiros já removidos (H-126, Prop. 2) antes de perguntar sobre
cancelamento. A construção usada aqui (subárvore real truncada em
profundidade `ell-1`, sem remover modo grosseiro nenhum) tem suporte
PLENO, igual ao da medida idealizada, mas concentra a massa em poucos
átomos efetivos dentro desse suporte (razão de participação de ordem
dezenas, não milhões), o regime onde o argumento de Parseval acima
domina. A substituição do modelo idealizado por enumeração real não era
o problema (as razões são invariantes de escala, renormalizar não
mudaria nada); o problema era a CONCENTRAÇÃO da massa dentro do
suporte, não o tamanho do suporte em si nem a escolha entre real e
idealizado.

**Veredito**: `fechada-inconclusiva`, não `fechada-refutada`. O teste
como construído não decide se existe cancelamento de fase real no
objeto que O4 precisa (a decomposição idealizada de Tao, com modos
grosseiros removidos): ele mediu outra coisa, que por acaso também
decai, mas por um motivo trivial e não relacionado a irmandade. A
pergunta original de H-163 (existe cancelamento bilinear sem decaimento
pontual nem l²?) permanece genuinamente sem teste.

**Escalonamento (Regra 11b)**: o processo que deveria ter capturado
isto antes de aceitar o resultado é exatamente a Regra 11b/8c
(consultar antes de declarar feito, verificar antes de aceitar) e a
prática de rodar um controle negativo antes de interpretar um número
pequeno como sinal. Nenhuma das duas foi feita na primeira passada;
ambas foram feitas na correção, com um crítico independente detectando
o problema e uma segunda verificação minha confirmando.

**Se a linha for retomada**: construir `S_i` como a decomposição
idealizada de Tao (`mu_ell^{(j)}`, suporte pleno em unidades mod
`3^ell`, não uma subárvore real truncada), remover os modos afins
grosseiros de H-126 Prop. 2 antes de somar, e comparar contra os MESMOS
dois controles usados aqui (dilatação aleatória; objeto não
relacionado) como parte do protocolo, não como reação a uma crítica.
Nenhuma tentativa nesta direção foi feita nesta sessão (fora do escopo
depois da retratação; ver H-174 para o registro da pergunta
corretamente colocada).

Ver `experiments/E-140-bilinear-sibling-pairing/` (script, README,
verificação de corretude, tabela completa, controles). O README e o
script foram atualizados para registrar o achado do artefato e os
controles como parte permanente do experimento, não removidos.
