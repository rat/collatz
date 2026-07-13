# H-013 — Todo órbita termina em J_t=(4^t−1)/3; classes estéreis explicadas por H-005

Status: confirmada (teorema + verificação); anomalia p₅>p₄ confirmada como fato assintótico real (H-018), ainda sem fórmula fechada
Criada em: 2026-07-13
Origem: brainstorm assistido pelo modelo Fable (consultado a pedido do diretor
científico sobre padrões binários), verificado de forma independente.

## Enunciado

O último valor ímpar (>1) de qualquer órbita de Collatz é sempre da forma
J_t = (4^t−1)/3, para algum t≥2 — o mesmo conjunto de números caracterizado
em H-012 (predecessores ímpares de potências de 2: 3·J_t+1 = 4^t = 2^(2t)).
Isto é consequência direta de H-012: toda órbita termina numa cadeia pura de
divisões por 2 (...→4→2→1), e o ponto de entrada nessa cadeia (o último
valor ímpar) precisa satisfazer 3m+1=2^k para algum k — e por H-012, isso só
tem solução ímpar quando k é par (k=2t), dando m=J_t.

## Consequência: classes "estéreis"

J_t é divisível por 3 sempre que t≡0 (mod 3) — ex: J_3=21, J_6=1365. Pelo
lema de H-005 (um valor divisível por 3 nunca reaparece depois do primeiro
passo ímpar de uma órbita), esses J_t **nunca podem ser o último valor ímpar
de uma órbita genérica** (só apareceriam se a própria órbita começasse
exatamente nesse valor). Isso explica completamente por que as classes
t=3,6,9,... têm densidade zero — não é um mistério novo, é H-005 aplicado.

## Anomalia observada (questão em aberto — hipótese inicial refutada)

A fração de órbitas que termina em cada J_t **não decai monotonicamente**:
a fração para t=5 (J_5=341) é **maior** que para t=4 (J_4=85) — contrariando
a expectativa ingênua de decaimento ~1/4 por passo.

Especulei inicialmente que isso estivesse ligado ao resíduo mod 3 de J_t
(J_4≡1, J_5≡2 mod3). **Essa hipótese foi refutada** por uma varredura
exaustiva até 80 milhões (ver `experiments/E-013-last-odd-value-structure/CORRECTION.md`):
a razão entre classes adjacentes CRESCE para os pares (t=4,5)→1.59 e
(t=7,8)→5.97, mas **inverte** para (t=10,11)→0.072 e (t=13,14)→0.200. Não é
um efeito simples de mod 3 — o comportamento é não-monotônico de forma mais
complexa. Continua genuinamente em aberto; provavelmente requer análise da
estrutura de ramificação da árvore reversa (processos tipo Galton-Watson),
não tentada ainda.

## Como testar

Simulação Monte Carlo: para n aleatório, achar o último valor ímpar antes de
1, verificar se bate com a fórmula J_t, e tabular a distribuição de t.

## Atualizações

- 2026-07-13: hipótese confirmada. 300.000 amostras, 0 incompatibilidades
  com a fórmula. Distribuição observada: t=2 (93.77%), t=4 (2.37%), t=5
  (3.78%), t=7 (0.01%), t=8 (0.06%), t=10/11 (~0%). Classes t=3,6,9 com zero
  ocorrências, explicadas por H-005. Anomalia p₅>p₄ registrada como questão
  em aberto.
- 2026-07-13: tentei explicar a anomalia via resíduo mod 3 de J_t — **refutei
  minha própria hipótese** com varredura exaustiva (não amostrada) até 80
  milhões: a razão entre classes adjacentes cresce em (4,5) e (7,8) mas
  inverte em (10,11) e (13,14). Não é um padrão simples de mod 3. Anomalia
  confirmada como real (não é ruído — verificada em duas escalas, 20M e
  80M) mas continua sem explicação. Ver `experiments/E-013-last-odd-value-structure/CORRECTION.md`.
- 2026-07-13: mecanismo qualitativo encontrado em H-018 (construção
  explícita da árvore reversa via Galton-Watson): competição entre
  "ramificar uma geração mais cedo" (vantagem constante de t≡2mod3) e o
  "orçamento" log₂(n_max/J_t), que encolhe 2 bits por unidade de t. Para t
  pequeno a vantagem geracional domina (explica p₅>p₄, p₈>p₇); para t maior
  o orçamento fica tão pequeno que a população absoluta (dezenas de nós) é
  dominada por flutuações de árvore finita, invertendo o padrão. Não é uma
  fórmula fechada, mas explica qualitativamente por que a razão não é
  monotônica. Ver `experiments/E-018-reverse-tree-branching/`.
- 2026-07-13: **refinamento** — escalei o cálculo até n_max=10¹¹ (corrigindo
  o multiplicador de busca, que era a causa real dos travamentos, não o
  n_max). A razão (10,11) convergiu e estabilizou entre 10¹⁰ e 10¹¹ (0.0655
  vs 0.0656). **Confirma que a inversão é um fato assintótico real e
  permanente**, não ruído de árvore finita pequena como eu havia sugerido.
  O valor exato para onde cada razão converge continua sem explicação
  teórica fechada — questão genuinamente em aberto, agora caracterizada com
  mais precisão numérica. Ver atualização em
  `experiments/E-018-reverse-tree-branching/README.md`.
