# H-168: o quociente mínimo de Wirsching estabiliza em `ell`; o ínfimo em `a` é positivo?

Status: fechada-inconclusiva (2026-08-10), ver seção final

Criada: 2026-08-09

Origem: H-134, seção de 2026-08-09, e H-167. Ao medir a metade
quantitativa de `(?3)` apareceu uma separação que nenhuma nota anterior
desta linha registra.

## Observação

Defina

```text
R_ell(k, S) = min_{a em S} g_ell(k,a) / gbar_ell(k),
gbar_ell(k) = (soma sobre unidades de g_ell(k,a)) / (2*3^(ell-1)).
```

Com `S` = todas as unidades módulo `3^ell`, `R` decai geometricamente em
`ell`. Com `S` = um conjunto **fixo** de inteiros, `R` fica plano em
`ell`. Medidas de E-135 (`central_ratio.py`) em `k = ell + 5`, o menor
custo com suporte completo:

```text
S                     ell=10   ell=11   ell=12   ell=13   ell=14   ell=15   ell=16
todas as unidades     0.0509   0.0368   0.0536   0.0197   0.0435   0.0215   0.0240
a < 3^4  (54)         0.3056   0.2576   0.1877   0.2361   0.1742      .        .
a < 3^6  (486)        0.1019   0.1472   0.1341   0.1377   0.1306   0.1397      .
a < 3^7  (1458)       0.1019   0.0736   0.1073   0.0787   0.1161   0.1075   0.0958
a < 3^8  (4374)       0.0509   0.0736   0.0805   0.0787   0.1016   0.0967   0.0878
```

Todos os conjuntos fixos acima são completos, não amostrados. Em
`ell=10` a linha de `3^8` coincide com a linha de todas as unidades
porque 4374 dos 39366 resíduos já contêm o minimizador global; a partir
de `ell=11` o conjunto fixo é uma fração que encolhe e as duas linhas
se separam.

A linha das unidades decai a cerca de 0,88 por nível em `d=+5`. Em
`d=+12`, onde o suporte é completo desde `ell=4` e a série tem menos
ruído, o mínimo sobre todas as unidades cai de 0,4805 em `ell=6` para
0,2555 em `ell=16`, razão 0,94 por nível, estável entre as metades
`6..10` e `11..16`. As linhas de conjunto fixo não têm tendência ao
longo de seis ou sete níveis.

## Interpretação, e o confundidor que precisa ser separado

`min` sobre todas as unidades módulo `3^ell` é o mesmo que `min` sobre
inteiros `a < 3^ell`. Isso não é evidência sobre `liminf_ell` em nenhum
`a` fixo: o resíduo que realiza o mínimo no nível `ell` tem
representante inteiro da ordem de `3^ell`, e o `liminf` que `(?2)` pede
para esse inteiro só começa em níveis bem acima de `ell`. As duas
estatísticas medem coisas diferentes.

Mas o mínimo sobre `a < 3^m` também depende de `m` só por ser mínimo
sobre um conjunto maior. Em `ell=14`, onde as quatro linhas existem,
passar de `a < 3^4` para `a < 3^8` multiplica o conjunto por 81 e o
mínimo cai de 0,1742 para 0,1016, fator 1,71; passar daí para todas as
3.188.646 unidades multiplica por mais 729 e o mínimo cai para 0,0435,
fator 2,34. O mínimo cai muito devagar com o tamanho do conjunto,
compatível
tanto com uma cauda esquerda de ínfimo positivo quanto com decaimento
lento até zero. Os dados não separam as duas coisas, e qualquer leitura
que atribua a queda ao tamanho 3-ádico de `a`, e não ao tamanho do
conjunto, estaria confundindo os dois efeitos.

O que está estabelecido: **a `ell` fixo o quociente não se deteriora**.
O decaimento em `ell` do mínimo sobre todas as unidades é o crescimento
do conjunto de índices, `2*3^(ell-1)`, não a piora de nenhum resíduo.

## A pergunta

`(?3)` pede `inf` sobre `Z_3^x` inteiro, e esse ínfimo continua caindo
enquanto o grupo cresce. `(?1)`, que é o que o Teorema 1 consome, pede
só, para cada inteiro `a` não cíclico com `a != 0 mod 3`, um `liminf` em
`ell`, com constante uniforme em `a`. A pergunta é se

```text
inf_{a inteiro unitário} liminf_ell g_ell(k_ell,a)/gbar_ell(k_ell)
```

é positivo. Equivalentemente, se a cauda esquerda da distribuição do
quociente tem ínfimo positivo.

Se for positivo, `(?3)` como enunciada é forte demais sem prejuízo para
a cadeia, e a Conjectura 2 é o alvo errado. Se for zero com decaimento
`rho^m` em `m = log_3 a`, então `mu_1` na prova do Teorema 1 vira
`a^(-log(1/rho)/log 3)` e a conclusão enfraquece de `densidade >= c/a`
para `densidade >= c*a^(-1-eps)`: ainda densidade positiva de
predecessores para cada `a`, mas não a taxa uniforme da Definição 1 de
Wirsching.

## Próximo passo

Trocar o mínimo por quantis fixos da distribuição de
`g_ell(k,a)/gbar_ell(k)` sobre as unidades. Um quantil não sofre do
confundidor de tamanho de conjunto. Se o quantil de `10^(-3)` for plano
em `ell` enquanto o mínimo cai, a queda do mínimo é estatística de
extremos; se o quantil também cair, é deterioração real da cauda.
E-116 e E-128 já computam estatísticas de colisão sobre as mesmas
tabelas e podem ser reaproveitados. A tabela exata vai a `ell=16` em
cerca de 96 s.

## Ligação com H-143

H-143 prova que uma cota uniforme `g_ell(k,a) >= eta*gbar_ell(k)` na
janela implica `mu_ell(a) >= C*3^(-ell)`. Com `eta` substituído pelo
valor medido para o mínimo sobre todas as unidades, a mesma implicação
só entrega `mu_ell(a) >~ 3^(-1.06*ell)`. Com `eta` fixo em `a`, ela
entrega a forma original `C_a*3^(-ell)`, com `C_a` dependendo de `a`.
Qual das duas é a verdadeira é exatamente o conteúdo desta hipótese.

## 2026-08-10: execução do próximo passo, escalonamento, e fechamento

Quatro medições novas, todas em `E-135`
(`central_quantiles.py`, novo nesta sessão, mesma recursão auditada de
`central_ratio.py`), mais uma consulta a modelo externo (Codex,
Regra 11b).

### 1. Quantis fixos, `d=+5` e `d=+12`, `ell<=16`

O teste que a seção anterior já registrava como próximo passo: se um
quantil baixo fica plano em `ell` enquanto o mínimo cai, a queda é
estatística de extremos; se o quantil também cai, é deterioração real.
Rodado nos dois deslocamentos originais, o teste dá vereditos opostos:
em `d=+5`, `q=10^-3` fica achatado em `0,10-0,12` de `ell=10` a `16`;
em `d=+12`, `q=10^-4` cai de `0,402` para `0,276`, razão `~0,94` por
nível, perto do próprio mínimo. Isso abriu H-171 (Regra 8e).

### 2. Grade de deslocamentos intermediários, `d=6..11`, `ell<=16`

H-171 pedia decidir se o veredito por deslocamento é monótono ou
oscila sem padrão. Rodando a grade completa, a resposta é limpa:
`d=6` a `d=11` formam uma família consistente, todos com `q=10^-3` em
queda suave e regular (por exemplo `d=6`: `0,170 -> 0,131`, razão
`~0,955`/nível; `d=11`: `0,394 -> 0,265`, razão `~0,932`/nível). Só
`d=+5` foge do padrão, e `d=+5` é exatamente o primeiro custo com
suporte completo em cada nível (a fronteira medida por `central_zeros.py`
desde E-115/E-135), não um ponto genérico da janela. A interpretação
mais simples é que `d=+5` mede um regime de fronteira (muitos resíduos
com contagem ainda pequena por terem acabado de sair do suporte
incompleto), qualitativamente diferente do regime já assentado que
`d>=6` mede. H-171 fecha com essa leitura: a sensibilidade ao
deslocamento é real, mas tem uma causa estrutural identificada
(fronteira de suporte), não é um efeito sem explicação.

Conclusão da parte 1+2: fora da fronteira de suporte, o quantil baixo
da população cai junto com o mínimo. A leitura "estatística de
extremos" não se sustenta como explicação geral; na maior parte da
janela testada, é deterioração real da cauda populacional.

### 3. Composição do bucket inferior

Mas "deterioração real da cauda populacional" não é a mesma pergunta
que H-168 faz. A pergunta é sobre `a` FIXO. Medindo, em cada nível, que
fração dos resíduos no bucket inferior de `10^-3` da distribuição tem
representante inteiro pequeno (`a < 3^8 = 6561`), a fração cai de forma
consistente em todo deslocamento testado (`d=5` a `d=12`): perto de
`0,5` em `ell=9`, perto de `0,0002` a `0,0007` em `ell=16`. Ou seja,
o bucket inferior populacional é, em níveis altos, quase inteiramente
composto por resíduos NOVOS, cujo representante inteiro só existe a
partir daquele nível, e não por algum `a` pequeno e fixo que piora.
Isso concilia a parte 1+2 com a parte 4 abaixo: a cauda populacional
cai porque o grupo cresce e traz resíduos novos e ruins, não porque
resíduos antigos piorem.

### 4. Conjuntos fixos, extensão a `ell=17`

`central_ratio.py` estendido a `ell=17` (memória de pico ~39 GiB,
checada antes e durante a execução para não estourar). O quociente
mínimo sobre as 1458 unidades inteiras abaixo de `3^7` (conjunto
exaustivo, não amostrado) continua sem tendência:
`0,102, 0,074, 0,107, 0,079, 0,116, 0,108, 0,096, 0,089` para
`ell=10..17`. Sete níveis sem sinal de queda, incluindo o nível novo.

### 5. Escalonamento (Regra 11b): a rota de H-166 não transfere

H-166 (paper 01) provou que `min_u N_ell(u)/N_(ell-1)(...)` é uma
combinação convexa de razões do nível anterior, o que dá monotonicidade
e certifica uma cota em todo nível acima de um cálculo finito. Perguntei
a um modelo externo (Codex, `gpt-5.6-sol`, esforço alto) se o mesmo
mecanismo se aplica a `R_ell(k,a) = g_ell(k,a)/gbar_ell(k)`. Resposta
rigorosa, com derivação e contraexemplo explícito, não apenas
afirmação:

- A recursão natural de `g_ell` dividida por `gbar_ell` produz pesos
  `c_{ell,k}(j) = 3*bar_g_(ell-1)(k-j)/bar_g_ell(k)` cuja soma sobre os
  `j` admissíveis em `a`, `S_ell(k,a)`, NÃO é identicamente `1`: só a
  MÉDIA de `S_ell(k,a)` sobre `a` vale `1` (identidade de Haar), não o
  valor pontual. Contraexemplo exato em `ell=3,k=3`: `S_3(3,a)` vale
  `9/7, 12/7, 6/7, 6/7, 3/7, 6/7` para `a=1,2,4,5,7,8 mod 9`. A
  diferença com H-166 não é o peso `4^-j` versus peso `1`; é que em
  H-166 o denominador se transforma pelo MESMO operador que o
  numerador (identidade de pushforward pontual), e aqui não.
- Mesmo ignorando isso, a diagonal `k=ell+d` não é preservada pela
  recursão (`k-j = (ell-1)+(d+1-j)`, mistura muitos deslocamentos
  diferentes no nível anterior), então qualquer cota inferior formal
  para `min_a R_ell(ell+d,a)` degenera para zero na prática.
- Contraexemplo à monotonicidade em nível finito, com frações exatas:
  `m_ell = min_a R_ell(ell+12,a)` vale `9/28, 648/1459, 2430/5057,
  13851/30695` para `ell=4,5,6,7` (aproximadamente `0,3214, 0,4441,
  0,4805, 0,4512`): sobe e depois desce. Esses valores batem com os já
  medidos independentemente em `central_ratio.py` (Regra 8c). Não há
  monotonicidade nem no início da série.
- Existe uma combinação convexa genuína, mas de VETORES de
  probabilidade inteiros (`p_ell(k) = sum_j alpha_j M_j p_(ell-1)(k-j)`,
  `alpha_j = B_(ell-1)(k-j)/B_ell(k) >= 0` somando `1`), não da razão
  `R_ell` ponto a ponto. Isso dá desigualdades funcionais convexas
  (entropia, normas), não um mínimo de coordenada positivo.

Conclusão do Codex, citada porque é a parte que decide o fechamento:
"the direct H-166 mechanism does not transfer [...] neither certifies
a uniform future lower bound for min_a R_ell(ell+d,a), nor yields
monotonicity of that minimum or of the population's low quantiles. A
structurally different argument could still exist, but it would need
information beyond the bounded-composition recursion and its Haar row
average." Verifiquei a derivação até onde consegui reproduzir
manualmente (a identidade (1), a assimetria pontual/média de `S_ell`, e
os quatro valores exatos de `m_ell` contra meus próprios dados
numéricos): sem discrepância.

### Por que fecha como inconclusiva, não confirmada nem refutada

O peso da evidência empírica (partes 1 a 4) aponta na mesma direção: a
queda do mínimo e dos quantis populacionais é efeito do crescimento do
grupo, não deterioração de nenhum `a` fixo testado, e nenhum conjunto
fixo de inteiros (até `3^8`, até `ell=17`) mostra qualquer sinal de
piora. Isso é consistente com `inf_a liminf_ell R_ell(ell+d,a) > 0`, o
que deixaria `(?3)` forte demais como enunciada, mas o Teorema 1 de
Wirsching (que só precisa do `liminf` por `a`, Regra correspondente à
Proposição da janela unilateral acima) intacto.

Mas nenhuma computação finita decide um `inf` sobre todo `a` inteiro e
um `liminf` sobre todo `ell`, e a única rota que poderia ter fechado
isso como teorema (transferir o mecanismo de H-166) está agora fechada
com contraexemplo explícito, não por falta de tentativa. Fechando como
`closed-inconclusive`, no mesmo padrão de H-167: pergunta bem colocada,
computação exaustiva onde era viável, escalonamento a um segundo modelo
tentado e documentado, sem prova em nenhuma direção. Nada aqui muda a
cadeia de Wirsching (ver H-134, seção de 2026-08-09): o alvo real que
falta é um argumento sobre `W_3` em si, não sobre os geradores.
