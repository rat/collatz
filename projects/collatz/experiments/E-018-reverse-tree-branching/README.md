# E-018 — Estrutura de ramificação da árvore reversa (Galton-Watson)

Hipótese relacionada: [`H-018-reverse-tree-branching.md`](../../hypotheses/H-018-reverse-tree-branching.md)

## O que foi feito

Construímos a árvore reversa de Collatz explicitamente via BFS a partir de
cada J_t (regra: todo nó v tem predecessor 2v sempre, e (v−1)/3 se v par e
v≡4 mod6), para entender mecanicamente a anomalia de H-013 (por que a
fração de órbitas terminando em J_5 é maior que em J_4, mas isso inverte em
t=10/11).

## Bug encontrado e corrigido durante a implementação

Primeira versão do BFS podava a busca assim que um nó excedia o limite de
magnitude (n_max) — mas um "filho" via ramo ímpar ((v−1)/3, que **divide**
por ~3) pode ser menor que n_max mesmo que seu "pai" (alcançado só depois de
várias duplicações) exceda n_max. Isso descartava excursões válidas que
retornam a valores pequenos, causando subcontagem por um fator de ~5.
Corrigido separando o limite de **busca** (generoso, ex. 100×n_max) do
limite de **contagem final** (n_max). Com mult=100, os resultados convergem
para os valores exatos do forward scan de H-013 (t=10 e t=11 batem
exatamente; t=4,5,7,8 com diferença <2%, resíduo de excursões ainda mais
profundas que precisariam de um limite ainda maior).

## Mecanismo encontrado

1. **Geração do primeiro "checkpoint"** (primeiro ponto na cadeia de
   duplicação de J_t que satisfaz v≡4 mod6, habilitando um ramo extra):
   **sempre geração 1** para t≡2 (mod 3), **sempre geração 2** para t≡1
   (mod 3) — um padrão constante, verificado para t=4,5,7,8,10,11,13,14.
   Isso por si só NÃO explica a inversão (é o mesmo padrão para todo t).

2. **"Orçamento" de bits disponível** = log₂(n_max/J_t). Como J_t≈4^t/3,
   esse orçamento **encolhe exatamente 2 bits por unidade de t**:

   | t | J_t | orçamento (bits, n_max=20M) |
   |---|---|---|
   | 4 | 85 | 17.84 |
   | 5 | 341 | 15.84 |
   | 7 | 5461 | 11.84 |
   | 8 | 21845 | 9.84 |
   | 10 | 349525 | 5.84 |
   | 11 | 1398101 | 3.84 |
   | 13 | 22369621 | −0.16 |
   | 14 | 89478485 | −2.16 |

## Explicação mecanicista (qualitativa, não uma fórmula fechada)

Há uma **competição entre dois efeitos**:
- Ramificar uma geração mais cedo (vantagem de t≡2 mod3) favorece
  sistematicamente mais densidade — isso explica por que p₅>p₄ e p₈>p₇
  (orçamento ainda grande, 15-18 e 10-12 bits, suficiente para a vantagem
  sistemática dominar).
- Mas J_t cresce exponencialmente com t, consumindo o orçamento disponível
  dentro de qualquer limite fixo n_max. Para t=10/11 e t=13/14, o orçamento
  cai para poucos bits (ou fica negativo) — a população absoluta de nós
  encontrados é minúscula (dezenas ou menos), e passa a ser dominada por
  flutuações idiossincráticas de uma árvore finita pequena, não pela
  vantagem sistemática média. Isso explica por que a razão pode (e de fato)
  inverte nesses casos.

## Atualização — a inversão é assintótica real, não ruído de amostra finita

A explicação original (acima) sugeria que a inversão em t=10/11 e t=13/14
viria de "flutuações idiossincráticas de árvore finita pequena" — o que
implicaria que a razão poderia mudar (ou até voltar a crescer) com n_max
muito maior. **Testamos isso diretamente**, escalando o BFS até n_max=10¹¹
(usando busca_bound modesto, 5×n_max, em vez do 100× anterior — o
multiplicador exagerado é que causava travamentos, não o n_max em si).
Resultado:

| par | 20M | 80M | 1e10 | 1e11 |
|---|---|---|---|---|
| (10,11) | 0.048 | 0.072 | 0.0655 | **0.0656** |
| (13,14) | 0.200 | — | 0.296 | 0.271 |

A razão (10,11) **convergiu e estabilizou** entre 1e10 e 1e11 (0.0655 vs
0.0656 — praticamente idêntica). A razão (13,14) também está convergindo
(0.296→0.271, ainda se ajustando um pouco, mas na mesma faixa). **Isso
confirma que a inversão é um fato assintótico real e permanente**, não um
artefato transitório de amostra pequena que desapareceria com mais dados.

Isso corrige parcialmente a explicação qualitativa original: o "orçamento
de bits" explica por que as leituras em n_max pequeno (20M, 80M) eram
instáveis/ruidosas para t grande, mas **não explica por que o valor final
assintótico da razão é especificamente <1** para (10,11)/(13,14) e >1 para
(4,5)/(7,8) — essa parte continua sem explicação teórica completa.

## Tentativa de derivação teórica fechada (pedido do diretor científico)

Tentei derivar uma fórmula fechada usando a relação recursiva **exata**
D(v) = D(2v) + D(w) [quando v≡4 mod6, w=(v−1)/3], válida para a densidade
D(v) do subárvore reverso de qualquer nó v. Aplicando repetidamente ao longo
da cadeia de duplicações de J_t, obtém-se:

D(J_t) = Σ_{i=1}^∞ D(w_i)

onde w_1, w_2, w_3, ... são os sucessivos "filhos de ramo" encontrados subindo
pela cadeia de duplicações a partir de J_t (uma soma infinita e exata, não
uma aproximação). O problema é que cada D(w_i) não se reduz a nenhum f(t')
já conhecido — w_i é um inteiro ímpar genérico sem relação simples com a
família J_t, e sua própria densidade depende recursivamente da mesma
estrutura, exigindo conhecer o resíduo de cada w_i módulo 3^k para k
arbitrariamente grande. **Não consegui fechar essa recursão numa fórmula
finita** — parece exigir entender a estrutura autossimilar completa da
árvore reversa (equivalente, possivelmente, a um problema em aberto na
literatura sobre a densidade do grafo de Collatz). Reportando isso com
honestidade em vez de forçar uma fórmula sem sustentação.

## Precisão numérica melhorada (usando múltiplos núcleos)

Diante da dificuldade teórica, usei os 16 núcleos e ~55GB de RAM disponíveis
para aumentar a precisão numérica das razões, paralelizando a construção da
árvore para diferentes t simultaneamente.

**Armadilha encontrada**: numa primeira tentativa, comparei t=10 (n_max=1e12)
com t=11 (n_max=1e13) — escalas DIFERENTES — e obtive uma razão claramente
errada (0.651, inflada por ~10× exatamente o fator entre os dois n_max).
Corrigido usando sempre o **mesmo n_max** para os dois membros de cada par.

**Limite de infraestrutura encontrado**: uma tentativa de empurrar ainda mais
(n_max=1e13 para o par 10/11, 1e15 para o par 13/14) foi **morta pelo OOM
killer do sistema** duas vezes (processos usando 33GB e 61GB) — o ambiente
tem um limite de memória efetivo menor que os ~62GB nominais (provavelmente
um cgroup), útil registrar para futuras tentativas de computação pesada
nesta sessão.

### Tabela final consolidada

| par | 20M | 80M | 1e10 | 1e11 | 1e12 | 1e14 |
|---|---|---|---|---|---|---|
| (10,11) | 0.048 | 0.072 | 0.0655 | 0.0656 | **0.0649** | — |
| (13,14) | 0.200 | — | 0.296 | 0.271 | — | **0.281** |

## Status de H-018 (antes da reescrita DFS)

**Mecanismo qualitativo confirmado; convergência numérica bem estabelecida;
fórmula fechada não encontrada (provavelmente um problema genuinamente
difícil).**

- **(10,11)**: alta confiança — a razão fica entre 0.0649 e 0.0656 em três
  escalas diferentes cobrindo duas ordens de magnitude (1e10, 1e11, 1e12),
  variação de <1.5%. Convergência muito bem estabelecida em torno de **~0.065**.
- **(13,14)**: confiança moderada — valores em 1e10, 1e11, 1e14 (0.296,
  0.271, 0.281) oscilam num intervalo de ~9%, consistente com convergência
  a algo em torno de **~0.27-0.28**, mas sem a mesma precisão do par (10,11)
  (faltam pontos intermediários em 1e12/1e13, que causaram OOM ao tentar).

A inversão do padrão é confirmada como fato assintótico genuíno (não ruído
de árvore finita). O valor exato para onde cada razão converge, e uma
derivação teórica fechada, continuam como questão em aberto — tentei via a
recursão exata D(v)=ΣD(w_i) e não consegui reduzi-la a uma forma finita.

## Reescrita com DFS — quebra o limite de memória (2026-07-15)

O limite de infraestrutura documentado acima (OOM em 33GB/61GB) vinha do
`build_tree_count` original (`experiment.py`): um **BFS** com `deque` +
`set visited`, que guarda **todo nó já visitado** em memória — O(número de
nós explorados), não O(profundidade). Para árvores com centenas de milhões
de nós (como as usadas aqui), isso estoura qualquer RAM razoável.

**Justificativa para remover o `visited` set**: o mapa de Collatz é uma
função (cada u tem exatamente uma imagem f(u)). Na árvore reversa, o único
pai possível de um nó w é f(w) — nenhum nó pode ter dois pais, exceto se a
busca reentrar no ciclo trivial {1,2,4}. Para as raízes J_t usadas aqui
(t≥4, logo J_t≥85), isso nunca acontece: a órbita direta de 1 fica presa em
1→4→2→1 para sempre e nunca alcança nenhum J_t>4. Logo o `visited` é
desnecessário para corretude — é puramente o que causava o estouro de
memória. Trocando BFS+visited por **DFS com pilha explícita**
(`experiment_dfs.py`, função `build_tree_count_dfs`), a memória cai para
O(profundidade).

**Validação da reescrita** (antes de confiar em qualquer resultado novo):

1. **Idêntico ao BFS original, nó a nó**: rodando ambas as versões com os
   mesmos parâmetros (n_max=20M, mult=5), os dois métodos retornam
   exatamente os mesmos `nos_impares` para t=4,5,7,8,10,11 — confirma que a
   reescrita não mudou a lógica, só a estrutura de dados.
2. **Convergência ao ground-truth**: com mult=200 (o multiplicador
   original), o DFS reproduz exatamente os valores do forward-scan de
   H-013 para t=10 (311) e t=11 (15).
3. **Ganho de memória medido**: t=10 com n_max=1e13 (266M nós explorados)
   usou **9,8 MB** de RSS no DFS (`/usr/bin/time -v`), profundidade máxima
   665 — antes disso não era sequer tentável com o BFS+visited na mesma
   escala.
4. **`mult=5` é suficiente em escala grande** (checagem crítica, já que em
   n_max=20M só `mult=200` batia com o ground-truth): repeti três pares
   representativos — um de cada "família" de comportamento observada — em
   `mult=5` vs `mult=25`, e dois deles também em n_max 10× maior:

   | par (n_max) | mult=5 | mult=25 | diferença |
   |---|---|---|---|
   | (10,11) @ 1e13 | 0.064758 | 0.064728 | 0.05% |
   | (13,14) @ 1e15 | 0.282291 | 0.282466 | 0.06% |
   | (16,17) @ 1e17 | 0.774575 | 0.774298 | 0.04% |

   e para n_max 10× maior (mesmo mult=5):

   | par | n_max original | n_max ×10 | diferença |
   |---|---|---|---|
   | (10,11) | 0.064758 (1e13) | 0.064808 (1e14) | 0.08% |
   | (13,14) | 0.282291 (1e15) | 0.282494 (1e16) | 0.07% |

   Em todos os casos a razão é estável a <0.1% mesmo quando as contagens
   absolutas continuam subindo (~26% mais nós entre mult=5 e mult=25) — ou
   seja, o que falta capturar em `mult=5` afeta os dois membros do par
   proporcionalmente e cancela na razão. Isso confirma que `mult=5` já era
   suficiente nessas escalas para o propósito de medir a razão (não para
   contar o total exato de nós).

## Nove pares, escala muito maior — a razão NÃO converge a um limite único

Com o gargalo de memória eliminado, computamos a razão em 7 pares via
árvore reversa (mais os 2 pares pequenos de H-013/CORRECTION.md via
forward-scan exaustivo, que já eram ground-truth) — cobrindo t de 4 a 29,
cada um calibrado para um "orçamento" log₂(n_max/J_t) similar (~25-27 bits,
o mesmo usado nos pares (10,11)/(13,14) já validados):

| par | razão | n_max | método |
|---|---|---|---|
| (4,5) | 1.594 | 80M | forward-scan exaustivo (H-013/CORRECTION.md) |
| (7,8) | 5.972 | 80M | forward-scan exaustivo (H-013/CORRECTION.md) |
| (10,11) | **0.0648** | 1e14 | árvore DFS, validado (mult e n_max) |
| (13,14) | **0.2825** | 1e16 | árvore DFS, validado (mult e n_max) |
| (16,17) | **0.7745** | 1e17 | árvore DFS, validado (mult) |
| (19,20) | 0.0459 | 3e18 | árvore DFS, só mult=5 |
| (22,23) | 0.1592 | 2e20 | árvore DFS, só mult=5 |
| (25,26) | 3.610 | 2e22 | árvore DFS, só mult=5 |
| (28,29) | 0.1473 | 2e24 | árvore DFS, só mult=5 |

(Os últimos quatro pares não passaram individualmente pela checagem
mult×n_max acima. A extensão de confiança não vem de cobrir a mesma faixa
de valores — (25,26)=3.610 e (19,20)=0.046 são, na verdade, os dois pontos
mais extremos de toda a amostra, fora do intervalo dos três pares
validados — vem do **mecanismo** verificado: o que falta capturar em
mult=5 infla as contagens absolutas dos dois membros do par de forma
proporcional (contagens sobem ~26% de mult=5 para mult=25, mas a razão se
move <0.1%), e esse mecanismo de cancelamento não depende de onde no
intervalo o par cai. Isso é suficiente para confiar na razão a poucos
porcento de precisão; o fato de ser >1 ou <1 não está em dúvida em nenhum
dos nove pares.)

**Suspeita inicial (levantada e depois derrubada pelos próprios dados)**:
com os primeiros 6 pontos, pareceu haver um padrão ligado a t mod 9 (as
razões agrupadas por t mod9 de cada "primeiro elemento do par" pareciam
decair monotonicamente dentro de cada classe: mod9=4 → 1.59→0.28→0.159 é de
fato monótona). Mas as classes mod9=7 (5.972→0.7745→**3.610**) e mod9=1
(0.0648→0.0459→**0.1473**) **não são monótonas** — caem e depois sobem. Com
apenas 9 pontos espalhados entre 0.046 e 5.97, qualquer módulo pequeno
"explicaria" alguns pontos por acaso; **não vale a pena caçar um módulo mais
fino (mod 27, subsequências alternadas, etc.)** com esta quantidade de
dados — não há sustentação para isso.

## Resposta honesta: a razão converge quando t→∞?

**Não, pelo menos não de forma simples.** A razão entre classes adjacentes
oscila por **~2 ordens de magnitude** (0.046 a 5.97) ao longo dos 9 pontos
medidos, sem nenhum padrão periódico simples identificado. A suposição
inicial de H-018 (mecanismo do "orçamento de bits") explica por que
leituras em n_max pequeno eram ruidosas/instáveis, mas **não prevê, e não
explica, este padrão de oscilação de larga escala** — isso permanece
genuinamente em aberto. O achado desta rodada não é uma fórmula ou um
limite; é a resposta (negativa, mas precisa) à pergunta "converge?", mais a
eliminação do gargalo computacional que impedia sequer fazer a pergunta
para t>14.

Reproduzir: `python3 experiment_dfs.py [N_MAX] [SEARCH_MULT] [T_LIST]` (ver
docstring do arquivo para a justificativa completa de remover o `visited`).

## Decomposição D(J_t) = raiz + Σ D(w_i): dois teoremas provados (2026-07-15)

Pedido do diretor científico para tentar avançar em *por que* a razão
oscila desse jeito (não só *que* oscila). A recursão exata de H-018,
D(v)=D(2v)+D(w) quando v≡4mod6, aplicada repetidamente ao longo da cadeia
de duplicações de J_t, dá D(J_t) = 1 (a própria raiz, sempre ímpar) +
Σ_{i=1}^∞ D(w_i), onde w_1,w_2,... são os filhos de galho sucessivos
encontrados subindo a cadeia. Isso nunca fechou (H-024) porque cada D(w_i)
exige resíduos mod 3^k arbitrários. Em vez de tentar fechar a soma inteira,
instrumentamos um único DFS (`experiment_decompose.py`) que marca cada nó
com o índice do galho a que pertence e soma por bucket — testando se a
soma **converge rápido na prática**, mesmo sem fórmula fechada.

**Checagem de corretude embutida**: `1 (raiz) + Σ buckets == D(J_t)` total
(já que J_t é o único nó ímpar da espinha — todo 2^g·J_t com g≥1 é par).
Bateu exatamente em todos os testes.

### Dois teoremas provados

**Teorema 1 (esterilidade generalizada — generaliza H-005 a todo nó da
árvore reversa, não só à família J_t)**: um nó ímpar w tem toda sua
subárvore reversa reduzida à própria cadeia de duplicação — contribuindo
**exatamente 1 nó ímpar, para sempre, qualquer que seja o limite de
magnitude** — se e somente se w≡0 (mod 3).

*Prova*: duplicação preserva a classe "≡0 mod3" (2·0≡0), e ramificar num nó
v exige v≡4 mod6 (i.e. v par e v≡1 mod3). Se w≡0mod3, nenhum 2^k·w jamais
é ≡1mod3, logo a cadeia nunca ramifica. Se w≢0mod3, a sequência 2^k·w mod3
alterna entre os dois resíduos não-nulos (ord₃(2)=2), atingindo ≡1mod3 a
cada 2 passos — logo ramifica cedo ou tarde. ∎

**Teorema 2 (periodicidade mod 3 dos galhos, período 3)**: para uma raiz
ímpar não-estéril m, com A=2^{g₁}·m (g₁∈{1,2} a geração do primeiro
galho), a sequência de galhos de primeiro nível w_i=(A·4^{i-1}−1)/3 tem
**w_i mod 3 exatamente periódico em i com período 3**, percorrendo
{0,1,2} numa rotação fixa determinada por A mod 9.

*Prova*: ord₉(4)=3 (4¹=4, 4²=7, 4³=1 mod9), logo 4^{i-1} mod9 é periódico
em i com período 3; como A mod9 é fixo, (A·4^{i-1}−1)/3 mod3 herda essa
periodicidade. Calculando para os três resíduos possíveis de A mod9 que
são ≡1mod3 (1, 4, 7): a=1 dá ciclo (0,1,2); a=4 dá (1,2,0); a=7 dá
(2,0,1). ∎

**Corolário**: exatamente 1 em cada 3 galhos consecutivos é estéril
(contribui exatamente 1, para sempre) — não aleatoriamente, mas numa
posição fixa determinada por A mod9 (equivalentemente, para a família
J_t, por **t mod 9**, já que g₁ depende de t mod3 e J_t mod27 depende de
t mod9 via ord₂₇(4)=9). Verificado por aritmética direta — não pelo DFS
completo, que só rodamos para t=10,11,13 — nos 18 valores de t usados
neste experimento: t≡1,8 (mod9) dá rotação (1,2,0); t≡2,7 dá (0,1,2);
t≡4,5 dá (2,0,1) (t≡0,3,6 são as classes estéreis de H-013, fora de
consideração aqui). Isso confirma t=10/19/28 (t≡1) na rotação (1,2,0);
t=13/22 (t≡4) e t=5/14/23 (t≡5) na rotação (2,0,1); t=7/16/25 (t≡7) e
t=11/20/29 (t≡2) na rotação (0,1,2).

### Por que isso importa: explica a convergência rápida, não a magnitude

Validado nos três pares (10,11)/(13,14) — mais um decomposto à parte
(t=13): em todos os casos, os primeiros 2-3 galhos **férteis** (não os
primeiros 2-3 galhos em ordem bruta — um deles pode ser estéril, como o
galho 1 de t=11) já capturam >97% do total. Isso explica *por que* a soma
infinita converge rápido na prática, e por que uma medida ingênua "só o
galho 1" (R₁) pode enganar feio: para t=11, w_1=932067 é estéril (932067=
3×310689), contribuindo só 1 nó, enquanto os galhos 2+3 carregam 98% do
total — se o galho estéril cai na 1ª posição (o "slot" potencialmente
maior, antes de qualquer decaimento), o total sofre mais do que se cair na
3ª posição (t=10) ou na 2ª (t=13).

**Mas checamos explicitamente se essa posição explica a magnitude da razão
— e não explica.** Como a fase (posição do galho estéril) é função só de
t mod9, se ela explicasse a razão, agrupar as 9 razões já medidas por
J_t mod9 deveria dar grupos consistentes. Não dá:

| J_t mod 9 | pares (t,t+1) | razões medidas |
|---|---|---|
| 4 | (4,5), (13,14), (22,23) | 1.594, 0.2825, 0.1592 |
| 7 | (7,8), (16,17), (25,26) | 5.972, 0.7745, 3.610 |
| 1 | (10,11), (19,20), (28,29) | 0.0648, 0.0459, 0.1473 |

Há uma tendência grosseira (mod9=7 tende a valores maiores, mod9=1 tende a
menores), mas a dispersão **dentro** de cada grupo (até ~10× no grupo
mod9=4) é comparável ou maior que o espaçamento **entre** grupos (o máximo
do grupo mod9=4, 1.594, já ultrapassa o mínimo do grupo mod9=7, 0.7745) —
ou seja, a fase é uma tendência fraca, não um preditor. Isso é exatamente
consistente com outra observação: a taxa de decaimento entre galhos
férteis consecutivos da MESMA fase varia por t de forma não explicada por
esta teoria (680× entre galho1 e galho4 para t=10, mas só 73× para t=13,
ambos "mesma fase, 3 posições de distância") — essa taxa de decaimento é
que carrega a informação que falta, e ela depende de resíduos mais
profundos (mod 27, mod 81, ... recursivamente).

**Conclusão honesta**: os dois teoremas são reais e explicam mecanicamente
*por que* a soma converge rápido e *por que* medir só o primeiro termo
engana. Mas eles **reduzem** a pergunta ("por que a razão oscila") a uma
pergunta mais precisa e ainda em aberto ("por que a magnitude relativa de
galhos férteis consecutivos varia como varia") — não a **resolvem**. Essa
pergunta mais precisa é exatamente a obstrução de H-024 (precisão 3-ádica
ilimitada), agora localizada num objeto concreto e específico em vez de
uma dificuldade abstrata geral. Não vale a pena caçar mais pares ou
decompor mais t's atrás de uma estrutura mais fina — o mesmo tipo de caça
já matou a hipótese mod9 duas vezes nesta sessão.
