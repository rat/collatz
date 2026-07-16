# H-091 — G(v) é bem descrito por 3^m·μ_m(r), quase proporcionalidade; a degradação em resolução fina de H-090 era artefato de headroom fixo, não quebra real

Status: confirmada com ressalva estatística importante (ver Parte 2) —
o diagnóstico do artefato de headroom e a direção da correção estão
sólidos; a frase original "converge a ~1,00 exato" foi corrigida pelo
Fable para "consistente com b=1 dentro de ±0,01-0,015" (análise de
poder estatístico), e um teste mais forte (convergência pareada por-v)
dá evidência direta e limpa de que G(v) converge com o headroom —
mas o teste de refinamento mostra que a "exatidão total" ainda não
está certificada (resíduo cai mas não zera até M=14). Ver Parte 2
abaixo.
Criada em: 2026-07-16
Origem: resposta a três perguntas deixadas em aberto por H-090 ("a
correlação converge a 1,0?", "é proporcionalidade exata ou só
correlação?", "há uma ponte teórica real, não só coincidência
algébrica?"), a pedido explícito do diretor científico, com consulta
obrigatória ao Fable para a parte teórica crítica.

## As três perguntas e o que a investigação encontrou

### 1. A correlação converge a 1,0 conforme m cresce?

Testei diretamente, estendendo o sweep de H-090 até m=12 com muito mais
amostras por resíduo (removendo ruído de amostragem — confirmado por
reamostragem independente: dispersão entre reamostragens de ~0,02-0,03
dex, bem menor que o efeito observado de ~0,05-0,09 dex). Resultado
inicial (preocupante): a correlação **não** converge a 1 — sobe de
0,994 (m=2) a um pico de ~0,998 em m=3-4, depois **cai**
monotonicamente até ~0,973 em m=12. A dispersão do resíduo (log10(G) −
log10(3^m·μ)) tem o padrão espelhado: mínimo (~0,04 dex) em m=3-4,
crescendo a ~0,11 dex em m=12.

Descartei duas explicações óbvias antes de escalar ao Fable:
- **Deslocamento da janela de magnitude** (necessária para acomodar
  3^m maior): testado com janela FIXA para m=10,11,12 também — mesmo
  padrão de degradação, não é o efeito.
- **Ruído amostral residual**: reamostragem independente com muito
  mais amostras por resíduo em m=8 e m=12 mudou o resid_std em menos
  de 0,03 dex — a degradação é real, não artefato de amostra pequena.

Testei também minha própria hipótese de trabalho (valuações 2-ádicas
deixam de ser i.i.d. quando condicionadas a um resíduo 3-ádico fino) —
**refutada diretamente**: autocorrelação lag-1 da sequência de
valuações a_i ao longo de órbitas de Syracuse, condicionadas a resíduo
fixo mod 3^m, fica achatada em ~0 para todo m testado (2 a 12), depois
de corrigir um bug de reamostragem (janela estreita demais para m
grande dava só ~17 candidatos distintos para 4000 "amostras" — mesma
classe de bug já vista em E-089 nesta sessão).

### 2. É proporcionalidade exata (constante única) ou só correlação?

Testado via regressão log-log com expoente livre: ajustando G ~ μ^b em
vez de assumir b=1, o b ajustado ficava sistematicamente abaixo de 1
(0,92-0,95) para m grande, mas reduzia o resíduo só modestamente
(~10%) — não bastava para "resolver" a degradação sozinho.

### 3. Há uma ponte teórica real, e o que explica a degradação? (consulta ao Fable)

Escrevi minha própria derivação (os filhos-ramo de v na árvore reversa
são exatamente as pré-imagens (2^a·v−1)/3 do mapa direto acelerado,
"mesma estrutura de soma-sobre-pré-imagens" que a recursão de Tao) e
pedi uma crítica dura ao Fable, incluindo os números da degradação.

**A ponte teórica está certa e é mais forte do que eu tinha
formulado**: os pesos 2^{-a} do lado da árvore não vêm de nenhuma
heurística probabilística — são identidade combinatória EXATA (razão
de magnitudes v/w_a ≈ 3·2^{-a}, mais linearidade da contagem sobre
subárvores disjuntas):

  G(v) = Σ_a 3·2^{-a}·(1+O(2^{-a}/v))·G(w_a) + v/N

Isso coincide com a recursão de Tao **apenas no limite headroom
(N/v) → ∞**, condicional à existência de um limite de escala de G — o
que, apontou o Fable, é essencialmente equivalente a afirmações de
densidade sobre o grafo de Collatz que continuam em aberto (densidade
positiva plena não está provada; Krasikov–Lagarias dá só cota inferior
x^0,84).

**O suspeito concreto para a degradação**: `measure_G` no meu código
usa `n_max = v*20` — headroom **fixo**, independente de m. Mas cada
dígito 3-ádico extra de resolução exige a árvore ser contada ~4/3× mais
fundo antes de truncar (deriva média ~0,42 bits/geração, com desvio-
padrão ~1,3-1,4 bits/passo — números derivados de E[a]=8/3 ou 5/3
conforme resíduo mod3 do pai, ord₉(4)=3, já estabelecidos em H-018).
Com barreira de log₂20≈4,3 bits, a fração de massa já truncada cresce
com m: ~10% em m=3, ~30% em m=6, ~45% em m=9 — previsão quantitativa:
**o pico de correlação deveria se deslocar de m≈3 para m≈7 com
headroom 200, e m≈11-12 com headroom 2000**. Também identificou um erro
metodológico menor meu: usei média GEOMÉTRICA de G por classe residual,
quando o operador da recursão é linear — quem satisfaz a recursão é a
média ARITMÉTICA, E[G|classe]. A média geométrica introduz viés
multiplicativo correlacionado com a classe (~0,01-0,03 dex — contribui,
mas não explica o grosso do efeito).

## Teste decisivo (implementado em `experiments/E-090-syracuse-measure-vs-density/experiment_headroom.py`)

Reproduzi o sweep de m com headroom parametrizável (20, 200, 2000) e
média aritmética por classe. Custo por medição escala com o headroom,
não com v — confirmado empiricamente (0,00004s em headroom=20,
0,0025s em headroom=2000, ainda trivial).

| headroom | m=4 | m=6 | m=8 | m=10 | m=12 | m=14 |
|---|---|---|---|---|---|---|
| 20   | corr=0,986 b=0,985 | corr=0,990 b=0,991 | corr=0,989 b=0,980 | corr=0,982 b=0,988 | corr=0,983 b=0,956 | — |
| 200  | corr=0,986 b=0,984 | corr=0,991 b=0,987 | corr=0,995 b=0,994 | corr=0,996 b=1,004 | corr=0,996 b=1,006 | — |
| 2000 | corr=0,974 b=1,048 | corr=0,984 b=0,995 | corr=0,990 b=0,997 | corr=0,991 b=0,990 | corr=0,992 b=0,997 | corr=0,995 b=1,003 |

**A previsão do Fable bateu**: com headroom=20, a correlação não sobe
de forma consistente com m (oscila, sem tendência clara — a queda
acentuada vista antes em H-090 já estava parcialmente inflada pelo viés
da média geométrica). Com headroom=200 e 2000, a correlação **sobe
monotonicamente** conforme m cresce (não degrada mais dentro do range
testado, m até 14), e o expoente ajustado **converge a
aproximadamente 1,0 exato** (0,994 a 1,006 para headroom=200 com m≥7;
0,990 a 1,008 para headroom=2000 com m≥6) — dentro do ruído estatístico
da regressão.

## Interpretação

**Caso resolvido, com resultado mais forte do que H-090 original
relatava**: G(v) não é apenas "bem correlacionado" com a medida de
Syracuse de Tao — é **proporcional a ela quase exatamente** (expoente
≈1,00), uma vez corrigido o artefato de medição (headroom insuficiente
para resolver m fino). A "degradação" documentada em H-090 não era um
limite real da conexão teórica; era o instrumento de medição
(`measure_G` com headroom fixo em 20) que não tinha folga suficiente
para acompanhar a resolução crescente pedida. A ponte teórica é
sólida: os pesos da recursão da árvore reversa são uma identidade
combinatória exata (razão de magnitudes de subárvores disjuntas), que
coincide com a recursão de Tao no limite correto — e os dados agora
confirmam esse limite sendo alcançado experimentalmente conforme o
headroom aumenta, exatamente como a derivação previa.

**O que continua em aberto, honestamente**: a coincidência com a
recursão de Tao depende da EXISTÊNCIA de um limite de escala de G — o
Fable apontou que isso é próximo de afirmações de densidade no grafo de
Collatz ainda não provadas. Não fechamos essa questão (não é o
objetivo deste projeto resolver isso), mas agora sabemos que, condicional
a esse limite existir (o que os dados sugerem fortemente, mas não
provam), a proporcionalidade com μ é exata, não aproximada.

## Parte 2 (2026-07-16, mesmo dia) — segunda consulta ao Fable: "isso é exato de verdade, ou aceitamos b≈1 cedo demais?"

Pedido explícito do diretor científico para testar a fundo antes de
aceitar a conclusão, com Fable em caso de dúvida. Consultei de novo,
apresentando os números de H-091 (b entre 0,990 e 1,008) e as duas
dúvidas que tinham ficado abertas.

### O que o Fable esclareceu sobre a hipótese teórica

A afirmação da qual a ponte depende ("o limite de escala de G existe,
é positivo, e satisfaz a recursão de Tao") se decompõe em três partes
logicamente distintas: **(E)** existência do limite D(v)=lim C(v,N)/N;
**(P)** positividade D(v)>0; **(S)** estrutura de escala (G(v)~g(r)/v
dependendo só do resíduo). Ponto importante que eu tinha errado: essa
conjunção **não é mais fraca** que densidade positiva da árvore inteira
— é **estritamente mais forte**, porque as bacias são aninhadas
(B(v)⊆B(1) para todo v que comprovadamente chega a 1) — então (E)+(P)
para um único v já implica densidade inferior positiva de B(1). Também
**não é equivalente à Collatz** — é quase ortogonal (Collatz verdadeira
não dá (E)/(P)/(S) para v≠1). Hierarquia honesta: Krasikov–Lagarias
x^0,84 (provado) ≪ densidade positiva de B(1) (aberto) < (E)+(P) para
um v (aberto, mais forte) < (E)+(P)+(S) = a hipótese da ponte (aberto,
mais forte ainda). Detalhe relevante: o método de Krasikov–Lagarias/
Applegate–Lagarias já estratifica por mod 3^k — a mesma estratificação
3-ádica que medimos aqui com μ_m tem uma sombra rigorosa na literatura,
mas essa técnica só fecha expoentes <1, nunca densidade positiva.
Também esclareceu a parte "barata": como a recursão de Tao é uma
contração de ponto fixo único, **qualquer** limite de escala de G que
exista, seja positivo, e satisfaça a recursão é forçado a ser μ — o
experimento mede, com efeito, "se o limite existe, ele é μ" — e dá
evidência de que o limite existe, mas evidência numérica nunca fecha
uma questão de existência.

### Análise de poder estatístico — a frase "converge a ~1,00 exato" era otimista demais

O Fable mediu sd_x (dispersão de log₁₀(3^m·μ_m) entre classes) ≈ 0,46
dex, estável de m=6 a m=12. Com isso, SE(b) ≈ resid_std/(sd_x·√n):
com resid_std 0,04-0,09 e n=400-800 classes, SE(b) fica entre 0,003 e
0,010 — o que os dados de H-091 realmente certificam é **b = 1,000 ±
~0,012 (IC 95%)**, não "exato". Também apontou que "corr sobe
monotonicamente com m" é evidência fraca por si só (a dispersão de
log(3^m·μ_m) cresce mecanicamente com m, então corr sobe mesmo sem
melhora real) — as estatísticas informativas são b e resid_std(b=1),
não corr bruta. E identificou que o resid_std medido (0,04-0,09 dex)
excede o piso de reamostragem (0,02-0,03 dex) em ~0,03-0,08 dex — um
excedente sistemático de origem não identificada até então.

### Dois testes decisivos propostos (evitam o problema de pareamento do stress test anterior)

O `experiment_stress.py` rodado antes desta consulta tinha um defeito
real apontado pelo Fable: `n_per_residue` variava com o headroom
(30/20/15/8), mudando a janela e a sequência do RNG — **v's diferentes
em cada nível de headroom**, o que invalida comparação direta entre
eles (confirmado: em headroom=100000 com só 8 amostras/classe,
resid_std na verdade SOBE, efeito do viés de amostra pequena que o
Fable avisou, não um efeito real de headroom).

Implementados dois testes por v individual (`experiment_pervalue.py`,
G(v) é determinístico dado v e o headroom — sem ruído de medição por
v, evitando o problema de pareamento por completo):

**Teste B — convergência pareada**: mesmos 2.997 v's medidos em
headroom 200, 2000, 20000, 100000. Δ(v)=log G_{H2}(v)−log G_{H1}(v):

| H1→H2 | média(Δ) dex | desvio(Δ) dex |
|---|---|---|
| 200→2000 | −0,0037 | 0,0599 |
| 2000→20000 | −0,0009 | 0,0241 |
| 20000→100000 | −0,0007 | 0,0099 |

O desvio de Δ **encolhe geometricamente** (~2,5× a cada 10× de
headroom) — evidência direta e limpa de que G(v) converge por v
individual conforme o headroom cresce. Esta é a evidência mais forte
obtida até agora a favor da existência do limite de escala (E).

**Teste A — refinamento em M (mesmo conjunto de v's, headroom=100000)**:
regressão log G(v) contra log(3^M·μ_M(v mod 3^M)) por v individual
(não agregado por classe):

| M | b | resid_std | corr |
|---|---|---|---|
| 4 | 0,955 | 0,261 | 0,843 |
| 6 | 0,967 | 0,214 | 0,898 |
| 8 | 0,963 | 0,183 | 0,926 |
| 10 | 0,969 | 0,158 | 0,946 |
| 12 | 0,976 | 0,138 | 0,959 |
| 14 | 0,976 | 0,121 | 0,969 |

O resíduo cai monotonicamente com M (0,26→0,12), confirmando que parte
do excedente vinha de estrutura 3-ádica mais fina que M ainda não
capturava (candidato "inócuo" do Fable — na verdade uma predição da
própria hipótese). **Mas não zera até M=14** — ainda sobra dispersão
não explicada, e o expoente b nesta versão por-v fica em 0,96-0,98, não
exatamente 1,00 (mais baixo que nos testes agregados por classe).

## Interpretação final (honesta, revisada)

O diagnóstico do artefato de headroom e a direção da correção
continuam sólidos: a degradação vista em H-090 era mesmo instrumento de
medição, não limite teórico real. Mas "proporcionalidade exata" era
uma afirmação otimista demais para o tamanho de amostra que tínhamos —
o correto é **"consistente com proporcionalidade (b=1) dentro de
±0,01-0,015; G(v) individual converge claramente conforme o headroom
cresce (evidência forte para existência do limite); a exatidão total
(zerar o resíduo completamente) não está certificada e pode nunca ser,
por depender de uma questão de densidade no grafo de Collatz que
permanece em aberto"**. Isso é ao mesmo tempo mais honesto e, no teste
B, uma evidência numérica mais forte e mais direta do que qualquer
correlação agregada por classe já tinha dado neste projeto.

## Referências

- H-090 (hipótese original, ver nota de atualização lá).
- H-086/H-087 (origem de G(v) e sua continuidade 3-ádica).
- H-018 (E[a], ord₉(4)=3, usados na estimativa quantitativa do Fable).
- E-089 (mesma classe de bug de janela estreita/reamostragem, já
  catalogada e corrigida antes nesta sessão).
- Experimentos: `experiments/E-090-syracuse-measure-vs-density/
  experiment_extended.py` (sweep de correlação/dispersão vs m),
  `experiment_iid_check.py` (teste e refutação da hipótese i.i.d.),
  `experiment_headroom.py` (teste decisivo de headroom, confirma a
  previsão do Fable), `experiment_stress.py` (stress test não pareado —
  defeito de metodologia identificado pelo Fable, mantido para registro
  honesto do erro), `experiment_pervalue.py` (testes A e B pareados por
  v individual, propostos pelo Fable, os mais decisivos desta hipótese).
