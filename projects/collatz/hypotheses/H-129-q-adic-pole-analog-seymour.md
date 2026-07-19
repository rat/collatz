# H-129 — Análogo q-ádico do polo −1/3 de Seymour para a árvore reversa qx+1

Status: aberta
Criada em: 2026-07-18

## Enunciado

Jon Seymour (paper externo, "Rigidity of the Syracuse Transition Matrix",
2026-07-12, não publicado formalmente) prova que TODA a não-rigidez da
matriz de transição de um passo do mapa Syracuse padrão (q=3, direção
PARA FRENTE) se concentra exatamente no ponto 2-ádico −1/3 (o "polo",
onde 3n+1=0): a sequência dos resíduos excepcionais r_k=(4^k−1)/3
converge 2-adicamente a −1/3, e são estes (e só estes) os resíduos onde
n mod M não basta para determinar S(n) mod M exatamente.

Pergunta: existe um análogo EXATO disso para a nossa árvore REVERSA do
mapa qx+1 acelerado — especificamente, a discrepância quenched-vs-anelada
(o "congelamento" da raiz maior da equação de pressão, já provado em
geral via convexidade em `main.tex` §3.2) se concentra numa sequência de
resíduos convergindo q-adicamente a um ponto específico, análogo ao
−1/3 de Seymour?

## Motivação

Estamos no meio de uma investigação (E-103, Estágio 1) tentando decidir
se a Conjectura do índice de cauda do martingale (q≥5) é consistente com
a estrutura quenched real, via um teste de momento numérico caro (DP
exata + enumeração de resíduos). Se existir uma caracterização EXATA
(elementar, tipo valuação q-ádica) do fenômeno de congelamento —
análoga ao argumento limpo do Seymour — isso poderia resolver a questão
de forma muito mais decisiva e barata do que testes numéricos.

## Primeira tentativa (registrada, resultado preliminar)

Tentei a transcrição mais literal: para o passo único da recursão
reversa w_a(v)=(2^a v−1)/q (a fixo, v arbitrário), calculei se v mod q^k
determina w_a mod q^k exatamente. Escrevendo v=v_0+q^k t (v_0=v mod
q^k, t desconhecido):

w_a = (2^a v_0 − 1)/q + 2^a q^{k-1} t

O último dígito (base q, posição k−1) de w_a mod q^k depende de t mod q
(o dígito SEGUINTE de v, seu dígito na posição k) através do fator
2^a t mod q, que percorre TODOS os resíduos de Z/qZ conforme t mod q
varia (já que 2^a é invertível mod q). Ou seja: **a ambiguidade de "um
dígito a mais" é UNIVERSAL — afeta TODO resíduo v e todo a admissível
igualmente, não se concentra num subconjunto excepcional decrescente**,
ao contrário do fenômeno do Seymour (onde a maioria dos resíduos é
exata e só uma sequência específica, cada vez mais rara, é excepcional).

Isso sugere que a transcrição literal do Teorema de rigidez do Seymour
NÃO se aplica diretamente — nosso "problema de um dígito" é uniforme,
o dele é localizado. A analogia pode existir em outro nível (ex: ponto
fixo q-ádico de w_a, v*=1/(2^a−q) ∈ Z_q, existe para todo a — pode ser
que resíduos PRÓXIMOS desse ponto fixo, ou de um ponto específico
relacionado ao congelamento, sejam os que geram a lentidão de
convergência quenched-anelado, mas isso ainda não foi verificado).

## Como testar

1. Consultar o Fable com a derivação acima para confirmar/refutar o
   diagnóstico ("universal, não localizado") antes de prosseguir.
2. Se houver uma reformulação correta da pergunta (ex: via ponto fixo
   q-ádico dos ramos w_a, ou via profundidade multi-geração em vez de
   passo único), investigar se os resíduos "lentos para congelar" (ou
   os que mais contribuem para a discrepância quenched-anelada em
   `verify_freezing_clean.py`/Estágio 1) se aproximam q-adicamente de
   um ponto específico.
3. Se sim: tentar um Teorema exato análogo ao do Seymour, potencialmente
   substituindo parte do teste numérico caro do Estágio 1.
4. Se não: registrar como refutada e documentar por quê (a analogia é
   estrutural mas não se transporta ao nível de teorema exato).

## Atualizações

- 2026-07-18: hipótese criada, rodando em paralelo ao teste de momento
  do Estágio 1 (E-103). Primeira tentativa de transcrição literal já
  mostrou não funcionar como esperado (ver acima) — próximo passo é
  consultar o Fable antes de tentar uma reformulação.

- 2026-07-18: Fable consultado com a derivação completa + um
  refinamento (ponto fixo q-ádico v*(a):=1/(2^a−q) do ramo guloso
  de peso máximo, que é sempre o menor a admissível já que
  (q·2^{-a})^α decresce em a). Três resultados:

  1. **Confirmado (a)**: a conclusão "universal, não localizado" da
     transcrição literal está correta — mas por uma razão mais forte
     do que eu tinha percebido: são dois MECANISMOS matematicamente
     distintos, não duas versões do mesmo fenômeno. O nosso é perda
     de exatamente 1 dígito, sempre, para todo v e todo a (módulo de
     continuidade uniforme do afim w_a — a "derivada" q-ádica tem
     valor absoluto q constante em toda parte). O de Seymour é
     explosão ILIMITADA de v_2(3n+1) numa sequência rara e cada vez
     mais fina (densidade→0) convergindo ao polo −1/3 (zero do afim
     3n+1). Perda limitada uniforme vs. blow-up raro concentrado de
     valuação — categorias diferentes, não a mesma coisa em dois
     contextos.

  2. **Reframing correto do congelamento (b)**: não é REM/vidro de
     spin de Derrida (não há desordem genuína — a admissibilidade de
     a depende só de u mod q, estado finito, então Z_k(α;u_0) é
     literalmente uma função de partição de subshift de tipo finito
     com condição de contorno fixa). O campo certo é **otimização
     ergódica / formalismo termodinâmico a temperatura zero** (Mañé,
     Bousch, Contreras–Lopes–Thieullen, Jenkinson — survey de
     Jenkinson "Ergodic Optimization", 2006): quando a fase congela, a
     medida de Gibbs se concentra na medida MAXIMIZANTE do potencial
     log(q·2^{-a}). "O ramo guloso sempre vence" (maximizante =
     órbita periódica curta) é uma hipótese natural, correta em
     muitos casos, mas **conhecida por falhar** em sistemas parecidos
     (medidas maximizantes tipo Sturmian, ex. expoente de Lyapunov de
     frações contínuas) — precisa ser checada caso a caso, não
     assumida.

  3. **v*(a) NÃO é o análogo do polo −1/3 (c)**: é genuinamente
     especial (único ponto fixo de w_a), mas por um motivo diferente
     do de −1/3. v* é fixo de otimização ergódica (papel de atrator);
     −1/3 é zero do afim 3n+1 (papel de polo/singularidade causando
     blow-up de valuação no mapa FORWARD). O análogo literal de −1/3
     no nosso contexto seria −1/q (zero de qn+1), uma pergunta sobre
     o mapa FORWARD T_q, não necessariamente conectada ao congelamento
     da árvore REVERSA — não deve ser assumida conectada sem teste.

  4. **Achado decisivo, só de aritmética (grátis)**: v*(a) é inteiro
     ordinário sse 2^a−q=±1, i.e. q=2^a∓1 (família esparsa
     Mersenne/Fermat). q=3 é DUPLAMENTE sortudo (é ao mesmo tempo
     2^2−1 e 2^1+1) — é por isso que o exemplo já verificado no paper
     (q=3, u_0=1, w_2(1)=1) funciona tão bem: é uma coincidência
     numérica de q pequeno, não o mecanismo genérico. Para q=11,13
     (testado até a=19): **nenhum a dá ponto fixo inteiro**. Para
     q=5,9,17 (=2^a+1): o único fixo existente é u=−1 (negativo,
     provavelmente fora do domínio se a árvore é só de inteiros
     positivos). Logo extrapolar do exemplo q=3 para "o mecanismo
     geral do congelamento" seria um erro.

  **Próximo passo recomendado pelo Fable, em ordem de custo**: (i)
  já descartado — ponto fixo de ramo único não existe em geral; (ii)
  busca barata de ciclos de período p=1,2,3 da dinâmica gulosa
  (a_0(u mod q) iterado, rastreando o valor real) em q=5,7,9,11,13,
  comparando com o gap quenched-anelado já medido no Estágio 1; (iii)
  se nenhum ciclo curto explicar o gap, ir direto ao autovalor de
  Perron-Frobenius do operador de transferência ponderado em
  Z/q^kZ, sem tentar adivinhar qual ramo domina.

  **Status**: nem morta nem confirmada — a analogia com Seymour
  especificamente é a categoria errada (polo/blow-up de valuação vs.
  ponto fixo de otimização ergódica são fenômenos distintos), mas
  existe conteúdo real e citável num campo maduro (otimização
  ergódica), com um próximo passo barato e bem definido (busca de
  ciclo curto) antes de decidir se vale mais investimento teórico.

- 2026-07-18: executei o passo barato sugerido (busca de ciclos de
  período curto da dinâmica gulosa nos resíduos — sempre o menor a
  admissível — para q=5,7,9,11,13), e depois CONFERI contra os ciclos
  reais conhecidos do mapa T_q (força bruta, `T(q,n)=(qn+1)/2^v2(qn+1)`
  iterado). Resultado:

  - **q=7**: dinâmica gulosa tem ponto fixo único no resíduo 1. Ciclo
    real conhecido de q=7 é exatamente {1} (CYCLES[7]={1}). Match
    exato.
  - **q=5**: dinâmica gulosa tem 2-ciclo nos resíduos {1,3}. Dos TRÊS
    ciclos reais distintos de q=5 (CYCLES[5]={1,3,13,33,83,17,27,43}
    se decompõe em: {1,3} residuos[1,3]; {13,33,83} residuos[3,3,3];
    {17,43,27} residuos[2,3,2]), o PRIMEIRO bate exatamente com o
    2-ciclo guloso. Os outros dois (que usam ramos não-gulosos, não
    o menor a a cada passo) não são capturados por essa dinâmica
    simples.
  - **q=9,11,13**: dinâmica gulosa dá ciclos de residuo (ponto morto
    em 3 para q=9 — residuo com gcd(3,9)≠1, sem filhos; 2-ciclo {5,7}
    para q=11; 3-ciclo {1,3,7} para q=13) — ainda não conferidos
    contra ciclos reais desses q (não computados aqui).

  **Interpretação**: a dinâmica gulosa (sempre o ramo de peso máximo,
  ou seja, o "argmax" de otimização ergódica) recupera EXATAMENTE o
  ciclo mais simples/dominante conhecido, quando existe um único ciclo
  (q=7) ou quando há um ciclo "óbvio" entre vários (q=5) — consistente
  com a previsão de otimização ergódica de que a medida maximizante
  tende a se concentrar numa órbita periódica curta. Mas NÃO explica
  os ciclos "secundários" de q=5 (que exigem desviar do ramo guloso) —
  ou seja, a dinâmica gulosa sozinha é insuficiente para uma explicação
  completa do congelamento; capturaria só parte do fenômeno.

  **Avaliação**: achado real, pequeno, verificado por força bruta
  (não só plausível) — mas não decisivo. Não fecha H-129; próximo
  passo (Perron-Frobenius espectral, ou entender por que os ciclos
  secundários de q=5 escapam do ramo guloso) fica em aberto, não
  executado nesta sessão (fora do escopo do que foi pedido — a
  investigação foi pausada aqui para consolidar e reportar).

- 2026-07-19: retomada por pedido explícito do diretor científico
  ("vamos seguir com h-129"). Executado o teste de otimização ergódica
  propriamente dito — ver `experiments/E-104-h129-ergodic-optimization-freezing/`.

  **Teste 1 — concentração da medida de Gibbs quenched na trajetória
  gulosa**: calculei p_greedy(k) = P_quenched(seguir sempre o ramo
  guloso nos k primeiros passos), reusando a DP exata Z_k já validada,
  para q=3 e q=5, nas raízes α₊ (congelada) e α₋ (não-congelada), até
  k=20/16. Observação inicial: em q=5 congelada, p_greedy parecia
  desacelerar para quase-platô (taxa de decaimento caindo ~100x),
  sugerindo concentração — mas o Fable, com um **argumento exato**
  (Z_k(α;u₀) ≥ peso_guloso(k), válido para todo k já que todos os
  pesos são positivos), mostrou que a taxa própria do caminho guloso
  (L_guloso, média temporal exata sobre seu ciclo) é muito mais
  negativa que a taxa real A(α) em AMBOS os casos — ou seja, p_greedy→0
  eventualmente em toda fase, o platô observado é artefato
  pré-assintótico (o mesmo crossover k≈407 já conhecido de H-109,
  muito além do k=16 alcançável). **Não há concentração genuína no
  caminho guloso** — conclusão revisada, não confirma a hipótese
  original do Teste 1.

  **Achado colateral real (mas ver correção abaixo)**: no caminho,
  o Fable notou que A(α)/α = P(α_c)/α_c é CONSTANTE (fato exato, da
  fórmula já estabelecida em H-109), e que B(α_c)=3α_c/(2α_c)=3/2 é
  literalmente a constante de Bramson de máximos de branching random
  walk — conexão real com a literatura de extremos de BRW (Bramson
  1978), citável independente do resto. Isso levou a definir
  a*=(log q − P(α_c)/α_c)/log 2 como candidato a "⟨a⟩ ótimo teórico"
  (a*(q=3)≈1,64; a*(q=5)≈2,36; a*(q=7)≈3,09).

  **Confirmação inicial (empolgante, depois revertida)**: calculei
  ⟨a⟩ = média de v2(qx+1) sobre TODOS os ciclos reais conhecidos de
  q=3,5,7 (força bruta). Os DOIS ciclos secundários de q=5 (que
  escapavam da dinâmica gulosa) deram ⟨a⟩=7/3≈2,333 — a 1,3% do
  a*=2,362 previsto, mais perto que o ciclo guloso (2,5, erro 5,8%).
  Reportei isso ao diretor científico como achado forte antes de
  verificar mais a fundo — **erro de processo**, ver correção abaixo.

  **CORREÇÃO (advisor + Fable, mesma rodada)**: a fórmula de a* não é
  uma previsão testada — é, na melhor hipótese, um LIMITE SUPERIOR não
  verificado (a_min≤a*), não uma igualdade. A igualdade exigiria uma
  fórmula de congelamento tipo REM/cascata i.i.d. que nunca foi
  demonstrada NEM testada para este subshift determinístico específico
  (que pode até exigir o formalismo termodinâmico de cadeias de Markov
  de alfabeto infinito — Manneville-Pomeau, Sarig/Iommi — em vez de
  REM). Teste direto que o Fable rodou (A(α)/α calculado via DP,
  SEM o atalho anelado, para 3 raízes reais de q=5, α até 32): **não
  reproduziu a*=2,362 em nenhuma das três raízes** (deu 2,636, 2,4545,
  2,4545) e mostrou oscilação instável ao variar k — sinal de
  convergência não estabelecida, mesmo problema de transiente lento já
  visto em toda esta investigação. Terceiro ponto de dados (q=7, único
  ciclo conhecido ⟨a⟩=3,0 vs a*(7)=3,0914, erro 2,96%) refutou a
  hipótese alternativa (razão α₊/α_c prever a qualidade do ajuste) —
  não é monotônica entre os 3 q's testados.

  **Veredito final honesto**: a concordância numérica de a* com os
  ciclos catalogados de q=5/q=7 deve ser registrada como **evidência
  anedótica fraca, não confirmação**, de uma conjectura em aberto sem
  mecanismo verificado por trás. O que sobrevive como sólido: a
  constante de Bramson B=3/2 (fato exato, citável por si só) e o
  framing geral de otimização ergódica/formalismo termodinâmico como
  a lente teórica certa (mais correta que REM/vidro de spin) — mas
  SEM a previsão quantitativa de a*, que não resistiu a verificação
  direta.

  **Status**: ainda aberta. Nem morta (a constante de Bramson e o
  framing termodinâmico continuam válidos e citáveis) nem confirmada
  (a previsão numérica quantitativa de a* não se sustentou). Nada disso
  foi integrado ao paper — permanece só nesta hipótese.

- **2026-07-19 — Análise espectral do operador de transferência executada
  (E-105): gap confirmado, via fechada, erro de terminologia corrigido.**

  A pedido do diretor científico ("puxar o H-129 primeiro"), retomamos
  exatamente o próximo passo listado acima: a análise espectral do
  operador de transferência. Antes de programar, consultei o Fable
  (via `Agent`/`model:"fable"`) com contexto completo — em particular
  o Fato 2 já provado no paper (Exemplo ex:naive-fails: não existe
  operador de estado finito de uma geração, pois a classe do filho mod
  q^k depende do pai mod q^(k+1)) e a tensão entre "raiz complexa
  subdominante" (decaimento geométrico oscilatório, exigiria gap com
  autovalor isolado) vs. o k^-0,222 observado empiricamente (lei de
  potência, assinatura clássica de AUSÊNCIA de gap).

  **Resposta do Fable — resolve a tensão por camadas, não por escolher
  um lado**:
  1. O objeto certo não é L_α (Koopman ponderado filho→pai — esse é
     exatamente o operador "level-raising" do Fato 2, não preserva
     funções localmente constantes mod q^K). É o seu DUAL M_α
     (pai→filho, via os mapas afins φ_a(w):=(qw+1)·2^-a, que são
     definidos para TODO a≥1 sem restrição de admissibilidade — a
     condição 2^a·φ_a(w)≡1 mod q vale automaticamente por construção).
     M_α PRESERVA funções localmente constantes mod q^K exatamente
     (baixa o nível em 1 a cada aplicação) — dualidade sob a medida de
     Haar: M_α 1 = Λ·1 com Λ=q^α/(2^α−1), e a identidade de pressão
     anelada já provada é exatamente "Haar é automedida de M_α*".
  2. **M_α TEM gap espectral, e não é sutil**: cada ramo φ_a é
     uniformemente expansor por fator exato q (métrica q-ádica),
     distorção zero (ramos afins, pesos constantes por ramo) — as
     hipóteses clássicas de Mauldin-Urbański/Sarig para IFS conforme de
     alfabeto contável (que dão quasi-compacidade com gap) valem aqui
     de forma quase trivial. Argumento mais forte, específico deste
     operador: em Fourier por nível, M_α é estritamente triangular
     inferior por nível (desce 1 nível por aplicação) — logo o espectro
     de M_α restrito a qualquer LC_K (funções mod q^K) é EXATAMENTE
     {Λ, 0}, autovalor Λ simples, resto nilpotente. NÃO existe
     autovalor complexo subdominante isolado intrínseco. Manneville-
     Pomeau/Sarig-Iommi (sem-gap) NÃO se aplica — não há ponto
     parabólico possível com expansão uniforme exata.
  3. O k^-0,222 é real e compatível com gap perfeito, porque vive numa
     CAMADA DIFERENTE: não é a média anelada linear (essa tem gap), é
     um funcional NÃO-LINEAR de Z_k (teste de momento em α perto do
     índice de cauda) — e como já provamos que α_+ é sempre congelado,
     esse teste está sentado exatamente no CASO DE FRONTEIRA da teoria
     de branching random walk / transformada de suavização, onde
     correções polinomiais em k (Bramson, Aïdékon — deslocamento
     (3/2)log k, martingale derivativo normalizado por k^-1/2) são o
     comportamento PADRÃO esperado, sem nenhuma implicação sobre o gap
     da camada linear. Suspeito adicional: os pesos são potências de 2
     (caso reticulado) — no caso reticulado a cauda é log-periódica
     (Guivarc'h; Buraczewski-Damek-Mikosch), o que produziria exatamente
     as oscilações sem convergência monotônica vistas em E-103. A
     "raiz complexa subdominante" das notas antigas provavelmente veio
     de uma análise de Mellin (polos complexos na mesma reta vertical
     do polo dominante, causando oscilação log-periódica) mal registrada
     com vocabulário espectral errado — real como fenômeno, errada como
     descrição do operador.

  **Verificação numérica** (`experiments/E-105-transfer-operator-spectral-gap/experiment_gap_check.py`,
  q=5, α_+=1 e α_-=0,650919, K=2,3,4, aritmética exata para os índices
  e ponto flutuante para os autovalores): confirma exatamente a
  previsão — soma de linhas de M_α = Λ teórico em toda linha (casa
  8+ dígitos), autovalor dominante = Λ, todos os demais autovalores
  ≈0 (2e-8 em K=2, crescendo para 2e-4 em K=4 — ruído de não-
  normalidade do bloco nilpotente crescente, EXATAMENTE o artefato que
  o próprio Fable avisou que apareceria se eu tentasse ler isso como
  "gap fechando conforme K cresce"; não fiz essa leitura errada porque
  fui avisado antes de rodar).

  **Terminologia corrigida** em H-109 e `experiments/E-103.../README.md`
  e em `STATE.md`: a frase "raiz complexa subdominante do operador de
  transferência" foi removida/anotada como erro nos três lugares.

  **Consequência para H-129**: a via "análise espectral de Perron-
  Frobenius" listada como próximo passo está FECHADA — não por falta
  de recursos, mas porque a resposta é estruturalmente definitiva (gap
  perfeito, provado) e não ajuda a resolver a Conjectura do índice de
  cauda (que vive na camada errada). O formalismo de Manneville-
  Pomeau/Sarig-Iommi também está descartado como caminho (não há
  ausência de gap a explicar). **Status: ainda aberta.**

- **2026-07-19 (mesma sessão, continuação) — hipótese log-periódica
  também testada e FECHADA como não suportada (E-103 Estágio 2).**

  A hipótese de trabalho levantada acima ("compatíveis com
  log-periodicidade... pesos são potências de 2") foi testada, não só
  especulada. Consulta ao Fable derivou a previsão teórica ANTES do
  teste (mesma disciplina que faltou na primeira tentativa de a*): os
  multiplicadores A_a=(5·2^-a)^θ formam um reticulado deslocado por
  tipo de resíduo, com deslocamento irracional (log₂5 ∉ ℚ, pois 5 não é
  potência de 2) — pela dicotomia aritmético/não-aritmético da teoria
  de renovação implícita (Goldie 1991), este é o caso NÃO-ARITMÉTICO:
  **sem log-periodicidade assintótica esperada**. Dois períodos
  candidatos (só visíveis como artefato de profundidade finita, com
  amplitude prevista para DECRESCER em k): θ·log2=0,4512 (união de
  todos os a) e 4θ·log2=1,8047 (por tipo, espaçamento d=ord₅(2)=4).

  Teste pré-registrado (`experiments/E-103.../stage2_periodogram.py`):
  potência de periodograma de Lomb-Scargle exatamente nesses dois
  períodos, nas 4 amostras de W_v já coletadas (headroom 10⁵-10⁸).
  **Resultado**: potência no nível de ruído de fundo em todos os 4
  headrooms, para ambos os períodos (bem cotado no período "união":
  6,7-9,7 ciclos cabem no alcance dos dados). Um único valor não-trivial
  (H=10⁸, período-tipo) fica abaixo do limiar de significância, tem
  poucos ciclos, e aparece no headroom mais profundo — o oposto do que
  a previsão diria. Teoria e dado concordam: **sem log-periodicidade**.

  **Status de H-129: continua aberta.** Agora refutamos DUAS
  explicações candidatas para o transiente k^-0,222 (raiz espectral
  isolada; log-periodicidade) — isso não fecha nem explica o
  transiente, só elimina duas hipóteses específicas.

  Checagem leve complementar no eixo k (`stage3_k_axis_check.py`,
  dados da Rodada 3, k=5..11): razão de incrementos de M_k(p)
  monotônica, sem oscilação visível — corrobora, não prova de novo.
  Uma tentativa de ajustar |razão−1|~k^-χ para comparar contra "0,222"
  foi feita e descartada (revisão do advisor: alvo assintótico "1" só
  correto exatamente no p crítico; n=5 pontos correlacionados não
  sustenta erro-padrão confiável — χ ajustado variou 0,98 a 3,60 entre
  3 valores próximos de p, sinal de sub-poder, não medida real). A
  origem de "0,222" segue sem localização — resolvê-la exige localizar
  a derivação original ou estender k além do teto de memória de 5^k,
  nenhum dos dois uma ação imediata.

  Achado colateral não testado: κ=α₊/α₋ recuperado por um argumento de
  matriz média de posto 1 no modelo idealizado multi-tipo — não escapa
  a ressalva quenched-vs-anelado já honesta do paper (rem:transfer-basis).
