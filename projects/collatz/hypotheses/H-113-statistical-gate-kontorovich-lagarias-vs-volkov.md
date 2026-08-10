# H-113 — Portão estatístico para o expoente de 5x+1: Kontorovich-Lagarias (0,650919) versus Volkov (0,678)

Status: fechado em 2026-08-09, por um caminho diferente do de
2026-07-17. O estimador de E-097 tem viés medido de 0,038 num processo
de expoente conhecido, maior que a separação Δ=0,027, então a leitura
crua nunca poderia ser comparada contra uma previsão teórica. Rodando o
mesmo estimador em processos construídos para ter cada um dos dois
expoentes em disputa, a árvore aritmética casa com o de 0,650919
(0,64791 contra 0,64796 na década 1e7→1e8) e fica fora do intervalo do
de 0,678 (0,67079). Medição empírica com controles calibrados, não
prova, e testa o expoente 0,678, não o modelo de Volkov.

O texto até a seção datada de 2026-08-09 é o registro de 2026-07-17,
mantido como está. O veredito daquela seção estava certo na direção e
errado no método; H-137 estava certo em derrubá-lo, e o `main.tex` já
refletia isso. Este arquivo e o `OUTLINE.md` é que ficaram para trás.
Criada em: 2026-07-17
Origem: sexta rodada de consulta à IA externa recomendou consolidar um
pacote de publicação (H-113 planejado); o Fable identificou que a peça
mais citável desse pacote — resolver empiricamente a disputa
Kontorovich-Lagarias (2009) vs. Volkov sobre o expoente de contagem de
5x+1 — não estava de fato fechada, porque a citação anterior em H-109
("Hill batendo em 0,650919") não tinha intervalo de confiança e, como o
próprio Fable calculou depois, tinha erro padrão real ~0,45 (a
concordância de 2 casas decimais era sorte estatística, não confirmação
válida — H-109 precisa ser corrigido para não repetir essa alegação).

## Enunciado

Kontorovich & Lagarias (2009) preveem, para a árvore reversa de 5x+1,
expoente de contagem η₅,BP≈0,650919 (idêntico à nossa segunda raiz da
equação de pressão qx+1, H-109/H-112). Um modelo estocástico concorrente
(Volkov) prevê η*₅,BP≈0,678. Os próprios autores citam isso como uma
disputa em aberto desde 2009 por falta de dados suficientes. Este
experimento mede o expoente empírico em árvores reais de 5x+1 com poder
estatístico suficiente para discriminar entre os dois valores (Δ=0,027).

## Regra de admissibilidade (q=5, derivada pelo Fable)

Nó ímpar u, filhos w=(2^a·u−1)/5 válidos sse 2^a·u≡1 (mod 5), i.e.
a≡A0[u mod 5] (mod 4), com A0={1:4, 2:3, 3:1, 4:2}. u≡0 mod 5 não tem
filhos (nó estéril, conta mas não ramifica). Diferente de q=3: não há
condição de paridade — a integralidade mod 5 é a única condição, e o
filho é automaticamente ímpar quando inteiro. O ramo a=1 (u≡3 mod 5)
ENCOLHE (w≈0,4u) — fonte do viés de truncamento abaixo.

## Como testar (e o que deu errado antes de dar certo)

**Bug de truncamento (mesma classe do bug histórico do E-018)**: o ramo
que encolhe (a=1) faz com que nós abaixo de um checkpoint possam ter
ancestrais ACIMA dele — o teto de BUSCA precisa ficar ≥5 décadas acima
do maior checkpoint usado, senão o slope sai enviesado para baixo
(medido: ~-0,012 na fronteira buffer 3→4, metade do Δ=0,027 a
discriminar).

**Piloto** (60 raízes, mult/search_bound=1e12): slope médio=0,6433,
IC95%=[0,6327, 0,6531] — já excluía 0,678 por ~6,4 erros-padrão.

**Produção inicial (n=300, bug meu)**: amostrei raízes até 200.000,
ultrapassando o checkpoint inferior da janela (1e5) — descartou 83/300
raízes não-aleatoriamente e poluiu o painel de convergência. Corrigido
(raízes em (101,9999), bem abaixo da janela).

**Produção corrigida (n=300, mesma janela)**: slope médio=0,63801,
IC95%=[0,63159, 0,64410] — **excluiu os DOIS valores candidatos**
(0,678 por 12,57 SE; 0,650919 por 4,06 SE). Modo de falha previsto
explicitamente pelo Fable antes de rodar: com n grande o SE cai abaixo
do viés residual de truncamento, e um IC bilateral do ESTIMADOR
enviesado exclui tudo — não é evidência contra Kontorovich-Lagarias.

**Correção final — path-max + Richardson (Aitken Δ²)**: reescrita do
DFS para rastrear path_max (maior valor de nó visitado ao longo do
caminho raiz→nó) numa única passada em search_bound=1e13, dando as
contagens em TODOS os buffers 9-13 simultaneamente (validado
byte-a-byte contra o método antigo de DFS separado por buffer, 4
raízes de teste, 100% de concordância). Extrapolação de Aitken na
curva MÉDIA entre raízes (não por raiz — séries por raiz são
granulosas e o Aitken diverge; a média pooled decai quase
geometricamente, razão~0,4-0,5/década).

## Resultado final

- Curva média por buffer: 0,60049 (1e9) → 0,62387 (1e10) → 0,63261
  (1e11) → 0,63650 (1e12) → 0,63801 (1e13) — incrementos decrescendo
  geometricamente (0,0234, 0,0087, 0,0039, 0,0015).
- **Aitken Δ² (extrapolação buffer→∞): 0,639**, bootstrap por raiz
  reamostrada: **IC95%=[0,633, 0,645]**.
- **Exclui Volkov (0,678)** com folga ampla (limite superior do IC a
  0,033 de distância, ~10+ erros-padrão).
- **Resíduo até Kontorovich-Lagarias (0,650919)**: ~0,012 (o valor
  KL/pressão fica logo acima do limite superior do IC). Diagnóstico:
  painel de slope por década DENTRO da janela fixa (1e4→1e5 até
  1e7→1e8) mostra o slope ainda SUBINDO na última década testada
  (0,6021 → 0,6296 → 0,6432 → 0,6460 — não platôs), aproximando-se
  monotonicamente de 0,6509 sem ter chegado lá — assinatura de
  **pré-assintótica de janela fixa** (a janela 1e5-1e8 ainda não é
  "profunda o suficiente"), não de viés de truncamento residual (esse
  já foi corrigido pela extrapolação de Richardson).

## Veredito

Evidência empírica forte a favor da previsão de Kontorovich-Lagarias
(0,650919) e contra a de Volkov (0,678) — o portão fecha para excluir
Volkov com confiança alta; o pequeno resíduo restante até o valor exato
de KL tem o tamanho e a assinatura esperados de um efeito de janela
finita (mensurável e explicado), não uma discrepância não resolvida.

**Correção necessária em H-109**: a citação anterior "Hill batendo em
0,650919 (600 raízes, top 2%) vs. previsão 1,5363" deve ser sinalizada
como **não confirmatória** — o erro padrão real desse estimador, dado
k≈12 pontos de cauda, é ≈0,45 (ξ_cauda/√k), então a concordância de 2
casas decimais foi coincidência estatística, não evidência. O resultado
válido e citável é este H-113 (slope de contagem por década, n=300,
com correção de Richardson), não o Hill estimator da rodada anterior.

## 2026-08-09 — o veredito acima está errado. O estimador tem viés maior que Δ (E-133)

Trabalho em O8. Três coisas, em ordem de importância.

### 1. O arquivo estava desatualizado em relação ao paper

A seção "Veredito" acima ("exclui Volkov com confiança alta") e a
entrada correspondente no `OUTLINE.md` §6 ("excluindo Volkov (0.678)
com folga") **contradizem o próprio `main.tex`**, que em
`\begin{empirical}[...]\label{thm:kl}` diz o contrário: "Since it has
not stabilized, the experiment does not provide a calibrated confidence
interval for the asymptotic exponent and does not exclude the Volkov
prediction."

Isto não é descoberta minha. H-137 (2026-08-07, "Auditoria do
experimento KL--Volkov") já tinha feito essa auditoria e corrigido o
manuscrito. O que ficou para trás foram H-113 e o `OUTLINE.md`, que
nunca foram atualizados. O paper está certo; estes dois arquivos é que
estão velhos. Não editei `OUTLINE.md` (fora do escopo desta sessão);
fica sinalizado.

### 2. O que E-133 acrescenta a H-137: o tamanho do viés

H-137 disse que existe viés sistemático fora do intervalo e que o
experimento "favorece a direção da previsão de Kontorovich--Lagarias".
E-133 mede o viés, e a segunda metade dessa frase não sobrevive.

Reimplementei a enumeração em C (validada byte a byte contra o Python
de E-097 em 5 raízes, 165x mais rápida) com dois controles estocásticos
casados que compartilham o mesmo caminho de código. A única coisa que
muda entre os modos é de onde vem a classe de ramo de um nó:

- `arith`: `r = u mod q`, a árvore de verdade;
- `iid`: `r` sorteado uniforme em cada nó. É o passeio ramificado cuja
  pressão anelada é a do paper, logo seu expoente de contagem **é**
  `alpha_-(5) = 0.650919`, provadamente;
- `cyc`: como `iid`, mas os irmãos avançam de `+3 mod 5`, que é o que a
  árvore aritmética faz exatamente (H-162).

Mesma janela `1e5..1e8`, mesmas 300 raízes, mesmos buffers, mesmo
Aitken, mesmo bootstrap (valores de `summary.py`):

| modo | estimador | verdade |
|------|-----------|---------|
| iid | 0.6131 | 0.650919 |
| cyc | 0.6294 | 0.650919 |
| arith | 0.6382 | em disputa |

**O estimador subestima em 0.038 num processo cujo expoente é
conhecido.** A separação KL vs. Volkov é Δ = 0.027081. O viés é maior
que a coisa que se queria medir, então comparar a leitura crua contra
uma previsão teórica não decide nada, e é isso que E-097 e a seção de
2026-07-17 fizeram.

Somar o viés de volta na mão também não resolve: 0.6382 + 0.038 = 0.676
daria quase exatamente Volkov, e o passo é ilícito, porque o viés depende
de quanto o processo flutua e os três modos flutuam de formas
diferentes. Registro o número só para deixar claro que ele existe e que
foi deliberadamente não usado. A saída correta é a seção 4 abaixo.

### 3. O viés é atraso quenched, não correção anelada, e isso é computável

A forma da correção nunca tinha sido determinada, e as duas escolhas
naturais (correção em lei de potência ou em `1/log x`) extrapolam o
mesmo painel para valores muito diferentes, um perto de KL e outro
perto de Volkov. Dava para decidir isso, e decidi, com forma fechada.

Para o modelo, o número esperado de filhos de um nó no expoente
exatamente `n >= 1` é `1/q` (o filho existe sse `2^n r == 1 (mod q)`,
uma classe entre `q`). Logo
`E[# nós de nível k com sum a_i = A] = q^(-k) C(A-1,k-1)`, e contando
os que têm `2^A/q^k <= 10^t`, a identidade do taco de hóquei dá

```text
M(t) = sum_{k>=1} C(N_k(t), k) / q^k ,   N_k(t) = floor((t + k log10 q)/log10 2).
```

Conferida contra a soma dupla bruta em `q = 3, 5, 7`, `t = 1..4`, e
contra a média do simulador. Avaliável em `t` muito além de qualquer
enumeração.

O slope local anelado chega a **0.6517 em `t = 3`** e 0.65079 em
`t = 4`, contra `alpha_-(5) = 0.650919`. Ou seja: nas escalas em que
E-097 trabalhou (`t = log10(x/u)` entre 1 e 5), o lado anelado do
modelo praticamente não tem viés de janela. Todo o viés de 0.039 é
atraso do log-slope de UMA realização atrás do log-slope da média. A
diagnose de "pré-assintótica de janela fixa" na seção de 2026-07-17
acima está certa no fenômeno e errada no mecanismo.

Consequência prática: o estimador de janela de três décadas é a parte
ruim. Slopes por década, cada um extrapolado no buffer separadamente,
se comportam muito melhor.

### 4. Como o portão fecha de verdade: comparar leituras, não leitura contra previsão

O erro metodológico de E-097 e da seção de 2026-07-17 acima não foi o
número, foi o que se comparou com o quê. Comparava-se uma leitura
enviesada (0.639) contra uma previsão teórica não enviesada (0.650919).
Com viés de 0.038, isso não decide nada.

A correção: rodar o mesmo estimador num processo construído para ter
expoente 0.650919 e noutro construído para ter 0.678, e ver qual leitura
a árvore aritmética casa. Modo `cycq` de E-133: a estrutura de `cyc` com
o denominador de valor trocado por um real `qval`, e o expoente resolve
`qval^alpha = q(2^alpha - 1)`. `qval=5.00000` dá 0.650919 e
`qval=5.05398` dá 0.678. Conferido contra a forma fechada anelada, que
para `qval=5.05398` dá slope anelado 0.6768 a 0.6782.

Mesmo estimador, mesmas 300 raízes, mesma janela, mesmos buffers:

| processo | expoente verdadeiro | estimador de janela | década 1e7→1e8 |
|----------|--------------------|---------------------|----------------|
| cycq 5.00000 | 0.650919 | 0.63950 [0.63357, 0.64647] | 0.64796 [0.64426, 0.65204] |
| cycq 5.05398 | 0.678000 | 0.65943 [0.65290, 0.66630] | 0.67079 [0.66649, 0.67585] |
| cyc | 0.650919 | 0.62943 [0.62213, 0.63650] | 0.64437 [0.64067, 0.64819] |
| iid | 0.650919 | 0.61308 [0.60233, 0.62415] | 0.64068 [0.63276, 0.64962] |
| **arith** | em disputa | **0.63824** [0.63183, 0.64474] | **0.64791** [0.64391, 0.65241] |

A árvore aritmética lê 0.64791 na década comum mais profunda; um
processo de expoente 0.650919 lê 0.64796 ali. Diferença: 0.00005. Um
processo de expoente 0.678 lê 0.67079, e o intervalo dele não encosta no
da árvore. Mesma conclusão no estimador de janela.

Ou seja: **o 0.639 de E-097 nunca foi evidência contra
Kontorovich-Lagarias.** É, com três casas, exatamente o que um processo
com o expoente deles devolve nesse estimador. O veredito de 2026-07-17
chegou na direção certa por um caminho que não sustentava a conclusão;
H-137 estava certo em derrubá-lo, e o que faltava era o controle
calibrado, não mais dados.

Rodada profunda (checkpoints até `1e12`, buffers até `1e17`, 300
raízes), slope aritmético por década, cada década extrapolada no buffer:

| década | slope | bootstrap | distância a 0.650919 |
|--------|-------|-----------|----------------------|
| 1e7→1e8 | 0.6465 | [0.6425, 0.6506] | 0.0044 |
| 1e8→1e9 | 0.6487 | [0.6467, 0.6506] | 0.0022 |
| 1e9→1e10 | 0.6490 | [0.6479, 0.6499] | 0.0020 |
| 1e10→1e11 | 0.6506 | [0.6502, 0.6510] | 0.0003 |
| 1e11→1e12 | 0.6505 | [0.6503, 0.6508] | 0.0004 |

As bandas cobrem só reamostragem de raízes; o erro da extrapolação de
truncamento está limitado em 0.002 (E-133, `buffer_squeeze.py`), então
leia as décadas profundas como `0.6505 ± 0.002` contra 0.650919 e 0.678.
O estimador de janela satura em 0.63778 no buffer `1e17`, confirmando
que o Aitken de buffer de E-097 estava certo e que toda a diferença
restante era viés de janela.

### Categoria do resultado (Regra 10b)

Medição empírica com controles calibrados. Não é prova. E testa o
**expoente** 0.678, não o **modelo** de Volkov, que é uma árvore binária
completa com outra codificação dos iterados e não foi implementado.
Para O8 (`conj:transition-arithmetic`), isto é suporte empírico
calibrado ao valor do expoente em `q=5`; a lacuna de transferência
continua sendo O1/O7.

### Arquivos

`experiments/E-133-kl-volkov-window-calibration/`. Ver também H-162
(congruência de irmãos, provada aqui) e H-137 (a auditoria anterior).

### Erro meu, registrado

A primeira rodada do controle iid deu 0.484 e eu quase escrevi que o
modelo é absurdamente mais lento que a árvore. Era artefato: as raízes
aritméticas são sorteadas com `u mod q != 0`, sempre férteis, enquanto
o controle sorteava o resíduo da raiz em `{0..q-1}` e matava uma árvore
em cinco na largada. Corrigido antes de qualquer conclusão.

## Notação (clarificada, corrige ambiguidade α₁/α₂ de H-109)

- α₋ = menor raiz de q^(α−1)=2^α−1; α₊ = maior raiz.
- q=3: {α₋,α₊}={1,2}. q=5: {α₋,α₊}={0,650919, 1} (a raiz trivial é a
  MAIOR para q≥5, ao contrário de q=3).
- **Expoente de contagem (o que este experimento mede) = α₋ sempre.**
- Cauda de W (fator martingale) = α₊/α₋; ξ de Fréchet = α₋/α₊.

## Referências

- H-109 (equação de pressão, valores teóricos) — corrigir a citação do
  Hill estimator conforme acima.
- H-112 (checagem de novidade — identificou a disputa KL vs. Volkov).
- `experiments/E-097-qx1-empirical-gate/` — todos os scripts
  (`empirical_qx1_tree.py`, `pressure_qx1.py`, pilotos, produção,
  versão final com Richardson).
