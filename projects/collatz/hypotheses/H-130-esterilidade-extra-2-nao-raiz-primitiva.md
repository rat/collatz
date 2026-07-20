# H-130 — Esterilidade extra na árvore reversa de qx+1 quando 2 não é raiz primitiva mod q

Status: resolvida a favor da opção (i) — nível modelo (exato) + confirmação
empírica q=5 e q=7; expoente θ agora provado por duas rotas independentes.
Ressalva aritmética padrão (`rem:transfer-basis`) permanece, não é específica
de H-130. Ver "Resolução" abaixo.
Criada em: 2026-07-20
Resolvida em: 2026-07-20 (julgamento de máximo esforço, Opus + advisor)

## Origem

Uma auditoria externa do paper (2026-07-20, terceira rodada) achou um
erro real na §2 (Setup): o texto afirmava que todo resíduo $u\not\equiv
0\pmod q$ tem um único expoente de ramo admissível $a_0(u)$. Isso é
falso quando $2$ não é raiz primitiva mod $q$: verifiquei
computacionalmente (Python) que para $q=7$ ($\ord_7(2)=3<\varphi(7)=6$),
os resíduos $u\equiv3,5,6\pmod7$ também não têm expoente admissível
algum — são estéreis, além de $u\equiv0$. Corrigido no paper (§2 agora
descreve a condição correta: $a_0(u)$ existe sse $u\bmod q$ está no
subgrupo $\langle2\rangle\le(\mathbb{Z}/q\mathbb{Z})^\times$). Confirmei
que o Teorema 3.3 (identidade de pressão) não é afetado — sua prova
usa a bijeção na direção reversa (sequência de expoentes → raiz única),
nunca a existência de $a_0(u)$ para todo $u$ — e que o código real de
enumeração (`empirical_qx1_tree.py`) já tratava isso corretamente.

Esta hipótese registra a pergunta que a correção deixou em aberto:
**existe estrutura genuinamente nova (não apenas uma correção de
prosa) na árvore reversa quando $2$ não é raiz primitiva mod $q$?**

## Enunciado

Para $q$ ímpar com $d:=\ord_q(2) < \varphi(q)$ (i.e. $2$ não gera todo
$(\mathbb{Z}/q\mathbb{Z})^\times$), a árvore reversa de $T_q$ tem
$\varphi(q)-d$ classes de resíduo estéreis "extras" (além de
$u\equiv0$) — residuos fora do subgrupo $\langle2\rangle$. Pergunta:
essa esterilidade extra (i) é apenas um fator multiplicativo constante
na população total (não afeta o expoente $\alpha_-(q)$ da identidade
de pressão, já confirmado), ou (ii) introduz uma estrutura mais rica
(por exemplo, cosets de $\langle2\rangle$ atuando como "camadas" com
comportamento assintótico distinto entre si)?

## Exploração numérica preliminar (esta sessão)

Tabulei $d=\ord_q(2)$, $\varphi(q)$, e a fração estéril extra
$(\varphi(q)-d)/\varphi(q)$ para $q$ ímpar de 3 a 61 (`sympy`,
`n_order`/`totient`):

```
   q  phi(q)  ord_q(2)  primitiva?  esteril extra
   3       2         2        True              0
   5       4         4        True              0
   7       6         3       False              3
   9       6         6        True              0
  11      10        10        True              0
  13      12        12        True              0
  15       8         4       False              4
  17      16         8       False              8
  19      18        18        True              0
  21      12         6       False              6
  23      22        11       False             11
  25      20        20        True              0
  27      18        18        True              0
  29      28        28        True              0
  31      30         5       False             25
  33      20        10       False             10
  35      24        12       False             12
  37      36        36        True              0
  39      24        12       False             12
  41      40        20       False             20
  43      42        14       False             28
  45      24        12       False             12
  47      46        23       False             23
  49      42        21       False             21
  51      32         8       False             24
  53      52        52        True              0
  55      40        20       False             20
  57      36        18       False             18
  59      58        58        True              0
  61      60        60        True              0
```

**Observação 1**: mesmo restringindo a $q$ primo, $2$ nem sempre é raiz
primitiva ($q=7,17,23,31,41,43,47$ são contraexemplos primos na faixa
testada) — isto é exatamente o território da Conjectura da Raiz
Primitiva de Artin (aberta em geral; para a base fixa $2$ especificamente
há resultados incondicionais parciais e resultados condicionais a GRH
por Hooley 1967). Isso conecta a estrutura da árvore reversa de $qx+1$
a uma conjectura clássica de teoria dos números — não perseguida aqui
a fundo, só registrada como conexão citável.

**Observação 2**: $q=31$ é o caso extremo da faixa testada — $2$ tem
ordem $5$ (mínima possível não-trivial) contra $\varphi(31)=30$, dando
$25/30\approx83\%$ dos resíduos não-nulos estéreis. Um caso assim
seria o candidato natural para testar empiricamente se a árvore
reversa "rala" tem comportamento qualitativamente diferente (ex.:
constante de escala muito menor, ou variância anômala) do que os casos
"densos" como $q=3,5,9$.

## Como testar (próximo passo, não executado ainda)

1. Confirmar analiticamente (deveria ser imediato a partir do Lema da
   bijeção de fibra) que a esterilidade extra só reescala a constante
   $W_u$ da Conjectura~3.7/3.9, sem mudar $\alpha_-(q)$ — isto já é
   fortemente sugerido pela prova do Teorema 3.3 não depender da
   alegação de admissibilidade universal, mas vale um argumento
   explícito (ou uma citação, se a estrutura de coset já for conhecida
   na teoria de smoothing transforms multitipo).
2. Se (1) se confirmar trivialmente, a pergunta interessante que
   sobra é sobre a CONSTANTE $W_u$: ela depende do coset de $u_0$ em
   $(\mathbb{Z}/q\mathbb{Z})^\times/\langle2\rangle$? Testável
   empiricamente para $q=31$ (enumeração real, como em `E-097`),
   comparando $W_u$ entre raízes em cosets diferentes.
3. Literatura: checar se a estrutura multitipo já citada no paper
   (Guivarc'h, Liu, Mentemeier, Kolesko–Mentemeier) já cobre esse caso
   como um "tipo" adicional (cada coset de $\langle2\rangle$ vira um
   tipo na cadeia de Markov multitipo) — se sim, isso pode já estar
   implicitamente coberto pela teoria citada, sem trabalho novo.

## Atualizações

- 2026-07-20: hipótese criada a partir da correção da §2 na terceira
  rodada de auditoria do paper. Exploração numérica preliminar feita
  (tabela acima); nenhum experimento formal (E-XXX) ainda — aberta
  para retomada futura.
- 2026-07-20 (mesma sessão, continuação — `E-109`): testado o passo 2
  do "como testar" acima — a família de escala por tipo
  ($W_i\sim2^{-a_0(i)\theta}W^*$, já confirmada para q=5 em E-103
  Estágio 4) sobrevive entre os 3 tipos não-estéreis de q=7
  ($\langle2\rangle=\{1,2,4\}$, $a_0$: 3,2,1) apesar da esterilidade
  extra em $\{3,5,6\}$? **Sim**: com 5000 raízes por tipo (headroom
  $10^7$), todas as 3 razões $W_i/W_j$ batem com a previsão a 2–4%
  (mesma faixa de precisão do achado original para q=5). q=31 (caso
  mais extremo da tabela) foi descartado como inviável — $\theta_{31}
  \approx0{,}0552$ exigiria $H\sim10^{36}$ para amostra razoável.
  **Conclusão parcial**: evidência a favor da opção (i) do enunciado —
  a esterilidade extra parece só remover os tipos que não sobrevivem,
  sem introduzir estrutura nova entre os que sobrevivem. Não é prova
  geral (um só q testado). Ver
  `experiments/E-109-h130-sterility-scale-family-q7/`.
- 2026-07-20 (mesma sessão, segundo caso): estendido `E-109` para
  também testar q=15 (composto, $\ord_{15}(2)=4<\varphi(15)=8$,
  $\langle2\rangle=\{1,2,4,8\}$, 4 de 8 resíduos coprimos
  não-estéreis) — um caso estruturalmente diferente de q=7 (composto
  em vez de primo, mais tipos). Com 3000 raízes por tipo (headroom
  $10^8$, $\theta=0{,}131006$), todas as 6 razões $W_i/W_j$ batem a
  1–4%. **Duas confirmações empíricas independentes agora, com
  estruturas distintas (q primo e q composto).**
- 2026-07-20 (mesma sessão, fechamento): resolução analítica registrada
  (seção "Resolução" abaixo). O passo que faltava — um argumento, não só
  a repetição empírica — veio do cálculo do autovalor de posto 1
  (cancelamento $d$-independente), verificado numericamente para
  $q=3,5,7,9,15,17,21,31,33$.

## Resolução (2026-07-20) — a favor da opção (i)

**Núcleo analítico (cálculo do autovalor de posto 1).**
A matriz média multitipo do smoothing transform, restrita aos tipos
*férteis* $i\in\langle2\rangle$, é de **posto 1**:
$M(s)_{ij}=\tfrac1q\,c_i(s)$ com
$c_i(s)=\sum_{k\ge0}\bigl(q\,2^{-(a_0(i)+kd)}\bigr)^s
      = q^{s}\,2^{-a_0(i)s}/(1-2^{-ds})$.
Posto 1 = *a lei do tipo do filho independe do tipo do pai* (o "input de
equidistribuição"; ver ressalva). O autovalor de Perron–Frobenius de uma
matriz de posto 1 $r_i s_j$ é $\sum_i r_i s_i$, então
$$\rho(s)=\tfrac1q\sum_{i\in\langle2\rangle}c_i(s)
        =\frac{q^{s-1}}{1-2^{-ds}}\sum_{i\in\langle2\rangle}2^{-a_0(i)s}.$$
Como $a_0$ é **bijeção** $\langle2\rangle\to\{1,\dots,d\}$,
$\sum_i 2^{-a_0(i)s}=\sum_{m=1}^{d}2^{-ms}=2^{-s}\tfrac{1-2^{-ds}}{1-2^{-s}}$,
e o fator $(1-2^{-ds})$ **cancela**:
$$\rho(s)=\frac{q^{s-1}}{2^{s}-1}\qquad\text{— independente de }d.$$
Logo $\rho(\theta)=1 \iff q^{\theta-1}=2^{\theta}-1$, que é **exatamente a
equação de pressão do Teorema 3.3**. Verificado numericamente (mpmath, 30
díg.) para $q=3,5,7,9,15,17,21,31,33$ (primos, potências e compostos):
$|\rho_{\text{posto-1}}-\rho_{\text{fechado}}|\lesssim10^{-30}$, resíduo
de pressão $=0$.

**Consequências (respondendo o enunciado).**
- Autovetor direito de PF: $C_i\propto c_i\propto 2^{-a_0(i)\theta}$ — a
  família de escala por tipo, idêntica em forma para todo $q$.
- A esterilidade extra ($d<\varphi(q)$) só **remove** os tipos estéreis.
  A matriz restrita aos sobreviventes continua de posto 1 e o cancelamento
  é $d$-independente, então **expoente $\theta$ E direção do autovetor
  sobrevivem intactos** — conteúdo exato da opção (i).
- Ponto fino (por que "restringir a posto 1" sozinho não basta): uma
  restrição ingênua a um sub-bloco baixaria o autovalor de PF e **não**
  daria θ-invariância; é o *cancelamento $d$-independente* que garante
  $\rho(\theta)=1$ para todo $q$. Autovalor ≠ autovetor (mesma família do
  quase-erro coset-vs-subgrupo registrado no STATE).

**Opção (ii) descartada estruturalmente.** Fértil $\iff$ resíduo
$\in\langle2\rangle$: existe **um único coset fértil** (o próprio
subgrupo). Os cosets não-triviais são *inteiramente* estéreis e não têm
assíntota própria — a leitura de "camadas de coset com comportamento
distinto" da opção (ii) é vazia. Corolário: q=5, q=7 e q=15 testam só a
escada *dentro* de $\langle2\rangle$ (comparação inter-coset é vácua); as
confirmações devem ser lidas como "cosets estéreis alhures não perturbam
a escada sobrevivente" = exatamente a opção (i).

**Distribuição completa (Claim B).** No modelo i.i.d. do smoothing
transform: posto 1 ⟹ tipo do filho independe do pai ⟹ tipo ao longo da
espinha é i.i.d. após a raiz ⟹ $W_i\stackrel{d}{=}c_i\,W^*$ com $W^*$
**comum** resolvendo uma SFPE de tipo único. Exato no modelo; para a
árvore aritmética real é a lacuna padrão `rem:transfer-basis`, não um
problema aberto específico de esterilidade.

**Evidência empírica (três casos independentes).** q=5 (E-103 Estágio 4):
razões de quantil em 3 níveis de cauda (30/20/10%) todas batendo o mesmo
$c_i/c_j$ — a *constância entre níveis* é evidência de invariância de
FORMA de cauda, não só de escala. q=7 e q=15 (E-109): média/mediana/
geomean (só escala), q primo e q composto. Precisão 1–9%, consistente com
desvio de amostra finita.

**Ressalva (não bloqueia o veredito).** Tudo é exato no modelo i.i.d.; o
posto-1 da árvore aritmética real é a hipótese de *equidistribuição* (os
filhos equidistribuem sobre $\langle2\rangle$ independente do tipo do
pai). O espalhamento mod $q^2$ do Example 3.1 é o **mecanismo** que
fornece essa equidistribuição (equidistribuição tipo Weyl, não autômato
finito), não um defeito — o argumento não depende de estrutura de Markov
finita, só de auto-similaridade estatística + equidistribuição. É a mesma
lacuna modelo-vs-aritmética de todo o projeto, não específica de H-130.

**Veredito de registro.** RESOLVIDA a favor da opção (i), em três camadas:
(a) expoente $\theta=\alpha_-$ — **provado**, agora por duas rotas
independentes (bijeção reversa do Teorema 3.3 + cancelamento de autovalor
de posto 1); (b) razão de escala por tipo $C_i\propto2^{-a_0(i)\theta}$ —
exata no modelo + empírica q=5,7,15; (c) forma / $W^*$ comum — exata no
modelo + empírica de cauda q=5. Opção (ii) descartada estruturalmente.
**Não alegar** "prova analítica geral para a recursão aritmética" — isso
permanece sob a ressalva `rem:transfer-basis` padrão do projeto.
