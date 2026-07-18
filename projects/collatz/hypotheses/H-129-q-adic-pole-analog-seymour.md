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
