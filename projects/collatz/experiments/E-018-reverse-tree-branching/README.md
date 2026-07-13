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

## Status de H-018

**Mecanismo qualitativo parcial, refinado com dados melhor convergidos.**
A inversão é confirmada como um fato assintótico genuíno (não ruído), mas
o valor exato para onde cada razão converge ainda não tem uma fórmula
fechada — uma teoria quantitativa completa (função geradora para o
processo de ramificação) fica como trabalho futuro.
