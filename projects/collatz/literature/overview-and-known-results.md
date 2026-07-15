# Visão geral e resultados estabelecidos

## O problema

Para T(n) = 3n+1 se n ímpar, n/2 se n par (ou a versão acelerada
T(n) = (3n+1)/2 para ímpar), a conjectura afirma que toda órbita a partir de qualquer
inteiro positivo eventualmente atinge 1. Aberto desde ~1937.

## O que é fato estabelecido

- **Verificação computacional**: sem contraexemplo até 2^71 (David Barina, 2025) —
  recorde mais recente encontrado na pesquisa; antes disso o limite citado com
  frequência era 2.95×10^20 (Barina, 2020/2021). PDFs de ambos arquivados em
  2026-07-15: `literature/papers/110_Improved-Verification-Limit-2-71.pdf` e
  `literature/papers/105_Convergence-Verification-Collatz-Problem.pdf`.
  [Improved verification limit](https://link.springer.com/article/10.1007/s11227-025-07337-0)
- **Tao (2019)**: "Almost all orbits of the Collatz map attain almost bounded values"
  — para qualquer função f → ∞ (por mais lenta que seja), quase todo n (densidade
  logarítmica 1) tem sua órbita atingindo algum valor abaixo de f(n) em algum ponto.
  Ex.: Col_min(n) < log log log log n para quase todo n. É o resultado mais forte e
  rigoroso até hoje — mas é uma afirmação de densidade/quase-todos, não a conjectura
  completa (não descarta um conjunto de medida zero de contraexemplos, nem prova
  convergência a 1 especificamente, só a valores limitados). Versão publicada (Forum
  of Mathematics, Pi, 2022) arquivada em 2026-07-15:
  `literature/papers/106_Almost-All-Orbits-Almost-Bounded-Values-Tao.pdf`.
  [arXiv:1909.03562](https://arxiv.org/abs/1909.03562) ·
  [Quanta Magazine (resumo acessível)](https://www.quantamagazine.org/mathematician-proves-huge-result-on-dangerous-problem-20191211/) ·
  [post do próprio Tao](https://terrytao.wordpress.com/2019/09/10/almost-all-collatz-orbits-attain-almost-bounded-values/)

## Por que é difícil — o obstáculo estrutural

Todo framework conhecido que produz convergência de densidade 1 esbarra na mesma
obstrução: existem conjuntos aninhados de "sobreviventes" (números que, sob a
aritmética determinística de carry do 3n+1, poderiam em princípio nunca cair), e
nenhuma ferramenta probabilística, algébrica ou de teoria da medida disponível hoje
consegue certificar que esse conjunto é vazio. Isso é citado como a barreira comum a
métodos ergódicos, 2-ádicos e heurísticos de passeio aleatório — todos "quase"
fecham o argumento, mas não conseguem eliminar esse resíduo.

Fonte geral: [Wikipedia — Collatz conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture)

## Nota sobre indecidibilidade (Fractran, Conway)

John Conway criou o Fractran, uma generalização do estilo de dinâmica do
3n+1 que é Turing-completa. Isso levanta a possibilidade teórica de que
problemas desse tipo (incluindo, possivelmente, variantes do Collatz) sejam
formalmente indecidíveis — não no sentido de "não sabemos a resposta", mas
"não existe prova dentro do sistema formal usual". Não implica que a
Conjectura de Collatz especificamente seja indecidível, mas é um contexto
relevante para calibrar expectativas sobre a dificuldade do problema.
(Fonte: vídeo do Veritasium "The Simplest Math Problem No One Can Solve",
trazido pelo diretor científico em 2026-07-13.)

## Implicação prática para este laboratório

Qualquer hipótese que formularmos deveria, idealmente, dizer explicitamente **como
ela pretende lidar com esse conjunto residual de sobreviventes** — se não disser
nada sobre isso, provavelmente está reproduzindo um argumento já conhecido e já
insuficiente.
