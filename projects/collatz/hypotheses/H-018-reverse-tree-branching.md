# H-018 — Estrutura de ramificação da árvore reversa (Galton-Watson) para explicar a anomalia de H-013

Status: parcialmente resolvida (mecanismo qualitativo identificado, sem fórmula quantitativa fechada)
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
