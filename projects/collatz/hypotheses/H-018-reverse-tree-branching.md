# H-018 — Estrutura de ramificação da árvore reversa (Galton-Watson) para explicar a anomalia de H-013

Status: parcialmente resolvida. Pergunta "converge quando t→∞?" respondida (não, oscila ~2 ordens de magnitude). Dois teoremas provados sobre a estrutura dos galhos (esterilidade generalizada; periodicidade mod3 com período 3) explicam a convergência rápida da soma. Pergunta "por que oscila desse jeito específico?" também respondida: não é padrão escondido, é ruído genérico de ramificação — confirmado estatisticamente (n=500) contra o null correto D(4m+1)/D(m), centro e dispersão batem com as 9 razões medidas dentro do erro esperado. Não fecha H-024 (sem fórmula fechada), mas dissolve a pergunta do "porquê" — melhor desfecho possível dado a obstrução conhecida.
Criada em: 2026-07-13
Origem: pedido do diretor científico para atacar a anomalia p₅>p₄ (H-013)
com uma análise de processo de ramificação, em vez de só resíduos.

## Contexto

H-013 encontrou que a fração de n cujo último valor ímpar é J_t não decai
monotonicamente em t, e minha hipótese inicial (ligada a resíduo mod 3 de
J_t) foi refutada. Esta hipótese ataca o mecanismo diretamente: construir a
árvore reversa de Collatz explicitamente e estudar sua taxa de ramificação.

## Regra de ramificação (revisão de H-005/H-007/H-012)

Todo nó v tem sempre o predecessor "duplicação" 2v. Adicionalmente, v tem um
segundo predecessor (v−1)/3 **se e somente se** v é par e v≡1 (mod 3) — ou
seja, v≡4 (mod 6). Isso dá um processo de ramificação binário: cada nó tem
grau 1 (só duplicação) ou grau 2 (duplicação + ramo extra), dependendo do
seu resíduo mod 6.

## Observação-chave sobre J_t

J_t é sempre ímpar, então nunca ramifica diretamente. Subindo pela cadeia de
duplicações 2^j·J_t, o primeiro ponto de ramificação (menor j tal que
2^j·J_t ≡ 4 mod 6) depende do resíduo de J_t mod 3:

- Se J_t≡2 (mod 3): 2·J_t≡1 (mod 3) já — ramifica em j=1 (mais cedo).
- Se J_t≡1 (mod 3): só 4·J_t≡1 (mod 3) — ramifica em j=2 (mais tarde).
- Se J_t≡0 (mod 3): nunca ramifica (classe estéril, ver H-005/H-013).

Hipótese: ramificar mais cedo (mais perto de J_t, em números menores) dá
mais "espaço" para a subárvore extra crescer dentro de um limite de
magnitude N fixo, favorecendo t≡2 mod3 sobre t≡1 mod3 adjacente — mas
efeitos de ramificação de ordem mais alta (mais longe na árvore) podem
inverter esse efeito para t maiores, como observado em H-013.

## Como testar

Construir a árvore reversa explicitamente via BFS a partir de cada J_t,
respeitando a regra de ramificação, até um limite de magnitude N. Contar
nós por nível/geração e comparar com os dados empíricos de H-013 (deve
bater exatamente, já que são o mesmo conjunto por construção). Analisar a
taxa de crescimento da árvore como função da geração em que ocorre o
primeiro fork, para tentar explicar quantitativamente o crescimento e a
posterior inversão da razão entre classes adjacentes.

## Atualizações

- 2026-07-13: hipótese aberta.
- 2026-07-13: testada em `experiments/E-018-reverse-tree-branching/`. BFS
  explícito da árvore reversa (após corrigir um bug de poda por magnitude)
  converge para os valores exatos de H-013. Mecanismo encontrado: geração
  do primeiro checkpoint é constante (1 para t≡2mod3, 2 para t≡1mod3) — não
  explica a inversão sozinha. O "orçamento" log₂(n_max/J_t) encolhe 2 bits
  por unidade de t (já que J_t~4^t); para t pequeno esse orçamento é
  grande o suficiente para a vantagem geracional dominar (explicando
  p₅>p₄, p₈>p₇), mas para t maior o orçamento cai a poucos bits e a
  população absoluta fica pequena o suficiente para flutuações
  idiossincráticas dominarem, invertendo o padrão (t=10/11, t=13/14).
  Explicação mecanicista qualitativa, não uma fórmula fechada.
- 2026-07-13: **refinamento importante** — escalei o BFS até n_max=10¹¹
  (corrigindo o multiplicador de busca de 100× para 5×, que era a causa
  real dos travamentos anteriores, não o n_max). A razão (10,11) **convergiu
  e estabilizou** entre n_max=10¹⁰ e 10¹¹ (0.0655 vs 0.0656 — praticamente
  idêntica). A razão (13,14) também está convergindo (0.296→0.271). **Isso
  confirma que a inversão é um fato assintótico real e permanente**, não um
  artefato de amostra pequena que desapareceria com mais dados — corrigindo
  parte da explicação original (que sugeria "flutuações de árvore finita").
  O "orçamento de bits" ainda explica por que leituras em n_max pequeno
  eram instáveis, mas não explica por que o valor assintótico final é
  especificamente <1 para (10,11)/(13,14) e >1 para (4,5)/(7,8) — isso
  continua sem teoria fechada.
- 2026-07-13: **tentativa de derivação teórica fechada** (pedido do diretor
  científico). Usando a relação recursiva exata D(v)=D(2v)+D(w) [ramo],
  obtive D(J_t)=Σ D(w_i) (soma infinita exata sobre os filhos de ramo da
  cadeia de duplicações) — mas cada w_i não se reduz a nenhum f(t') já
  conhecido, exigindo entender recursivamente resíduos módulo 3^k para k
  arbitrário. **Não consegui fechar numa fórmula finita** — parece um
  problema genuinamente difícil (talvez conectado a questões em aberto
  sobre a densidade do grafo de Collatz). Usei os 16 núcleos/55GB
  disponíveis para melhorar a precisão numérica em vez disso: (10,11)
  confirmado em ~0.065 com alta confiança (3 escalas, 1e10-1e12, variação
  <1.5%); (13,14) em ~0.27-0.28 com confiança moderada (oscila ~9% entre
  1e10/1e11/1e14). Uma tentativa de escalar ainda mais (1e13/1e15) foi
  morta pelo OOM killer do sistema (limite de memória menor que os 62GB
  nominais) — registrado como limite prático de infraestrutura.
- 2026-07-15: **quebra do limite de memória e resposta à pergunta central
  ("a razão converge?")**. O gargalo do OOM era o `visited` set do BFS
  original — O(nós explorados), não O(profundidade). Prova: o mapa de
  Collatz é uma função, então na árvore reversa cada nó tem no máximo um
  pai (=f(nó)); para raízes J_t com t≥4 (J_t≥85) a busca nunca reentra no
  ciclo trivial {1,2,4}, logo nenhum nó é redescoberto e o `visited` é
  desnecessário. Reescrevi como DFS com pilha explícita
  (`experiment_dfs.py`), memória O(profundidade): t=10 com n_max=1e13 (266M
  nós) usou 9,8MB de RAM, contra OOM em 33-61GB antes. Validado em 3 frentes
  antes de confiar em qualquer resultado novo: (a) idêntico ao BFS original
  nó a nó em mult=5; (b) reproduz exatamente o forward-scan de H-013 em
  mult=200; (c) a razão fica estável a <0.1% entre mult=5/25 e entre n_max/
  10×n_max em 3 pares representativos, mesmo com as contagens absolutas
  subindo ~26% — ou seja, o que falta capturar afeta os dois membros do par
  proporcionalmente e cancela na razão.

  Com o gargalo resolvido, computei mais 5 pares novos, nunca antes
  alcançados: (16,17)=0.7745, (19,20)=0.0459, (22,23)=0.1592, (25,26)=3.610,
  (28,29)=0.1473 (mais os já conhecidos, agora com dupla verificação:
  (10,11)=0.0648, (13,14)=0.2825). **Resposta honesta**: a razão NÃO
  converge a um limite único — oscila por ~2 ordens de magnitude (0.046 a
  5.97) ao longo dos 9 pontos medidos. Cheguei a suspeitar de um padrão
  ligado a t mod 9 com os primeiros 6 pontos (decaimento monótono dentro de
  cada classe), mas os 3 pontos novos **derrubaram essa hipótese** —
  mod9=7 vai 5.97→0.77→3.61 (não monótona) e mod9=1 vai 0.065→0.046→0.147
  (idem). Com só 9 pontos entre 0.046 e 5.97, não vale a pena caçar um
  módulo mais fino sem mais dados/uma reformulação da pergunta — registro
  isto como a resposta atual, não como um beco sem saída a perseguir mais.
  Ver `experiments/E-018-reverse-tree-branching/README.md` para a tabela
  completa e a validação passo a passo.
- 2026-07-15: **dois teoremas provados sobre a estrutura dos galhos**
  (pedido do diretor científico para avançar no "por quê", não só no
  "que"). A recursão exata D(J_t)=Σ D(w_i) nunca fechou (H-024) porque
  cada w_i exige resíduos mod 3^k arbitrários — mas em vez de tentar
  fechar a soma inteira, testei se ela **converge rápido na prática**.
  **Teorema 1** (generaliza H-005 a qualquer nó, não só à família J_t): um
  nó ímpar w tem subárvore reversa trivial (só a própria cadeia de
  duplicação, contribuindo exatamente 1 nó ímpar para sempre) sse w≡0
  mod3 — prova direta de que duplicação preserva "≡0 mod3" e ramificação
  exige ≡1 mod3. **Teorema 2**: a sequência de galhos de primeiro nível
  w_1,w_2,... ao longo de uma cadeia de duplicação tem w_i mod3
  EXATAMENTE periódico em i com período 3 (consequência de ord₉(4)=3) —
  exatamente 1 em cada 3 galhos consecutivos é estéril, numa posição fixa
  determinada por t mod9. Isso explica por que a soma converge rápido
  (2-3 galhos férteis já capturam >97%) e por que medir só o galho 1
  engana (para t=11 o galho 1 é estéril, contribuindo 1 nó, enquanto
  galhos 2+3 carregam 98%). **Mas checei explicitamente que essa fase
  (função só de t mod9) NÃO explica a magnitude da razão** — agrupando as
  9 razões já medidas por J_t mod9, a dispersão dentro de cada grupo (até
  ~10×) é comparável ao espaçamento entre grupos. A parte que falta (taxa
  de decaimento entre galhos férteis da mesma fase, que varia de 73× a
  680× entre os casos checados) depende de resíduos mais profundos (mod
  27, 81, ...) — é a obstrução de H-024, agora localizada num objeto
  concreto em vez de uma dificuldade abstrata. Redução real obtida, não
  resolução. Ver `experiments/E-018-reverse-tree-branching/README.md`.
- 2026-07-15: **a oscilação é ruído genérico de ramificação, não um padrão
  escondido**. Pedido explícito do diretor científico para gerar (via
  agente rodando Opus) uma lista de ângulos novos e testar o melhor. Uma
  primeira tentativa (D(w1)/D(w4), decaimento dentro de uma mesma raiz)
  teve um erro metodológico real — pego pelo advisor antes de qualquer
  conclusão: comparava um objeto diferente do que medimos nos 9 pares
  (dentro-de-uma-raiz vs entre-duas-raízes), com um parâmetro livre ("3
  posições") e n=9 com erro padrão grande demais para a coincidência
  encontrada significar algo. O teste correto usa J_{t+1}=4·J_t+1 (exato)
  como modelo: para m ímpar aleatório (m≡1mod3) e m'=4m+1, medir
  D(m')/D(m) — o mesmo objeto exato das 9 razões medidas, sem parâmetro
  livre. Resultado (500 amostras): média geométrica 0.542 e desvio-padrão
  0.758 dex, contra 0.432 e 0.715±0.179 dex medidos nos 9 pares reais —
  **ambos batem dentro do erro esperado**. Conclusão: a oscilação de ~2
  ordens de magnitude não é especial à família J_t — é o espalhamento
  típico de comparar D(m) entre inteiros relacionados por m'=4m+1
  quaisquer. Não fecha H-024 (nenhuma fórmula), mas dissolve a pergunta
  "por que oscila desse jeito" em "isso é ruído esperado de um processo
  de ramificação 3-ádico genérico" — o melhor desfecho possível dado o
  que já sabíamos. Não vale a pena testar os outros 5 ângulos propostos
  pelo agente — mirariam a mesma pergunta já respondida. Ver
  `experiments/E-018-reverse-tree-branching/README.md`.
