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
  (a previsão numérica quantitativa de a* não se sustentou). Próximo
  passo, se retomado: análise espectral genuína do operador de
  transferência (Perron-Frobenius em Z/q^kZ) ou formalismo de
  Manneville-Pomeau/Sarig-Iommi para cadeias de alfabeto infinito —
  nenhum dos dois executado ainda, ambos de custo alto. Nada disso foi
  integrado ao paper — permanece só nesta hipótese.
