# Literatura — índice

Levantamento inicial (2026-07-13). Organizado por tema, não por paper individual —
fragmentar por paper só vale a pena se o volume justificar depois.

1. [`overview-and-known-results.md`](overview-and-known-results.md) — definição do
   problema, o que é fato estabelecido, verificação computacional, por que é difícil.
2. [`approaches-2adic-ergodic.md`](approaches-2adic-ergodic.md) — dinâmica 2-ádica,
   ergodicidade, medida invariante.
3. [`approaches-stochastic-heuristic.md`](approaches-stochastic-heuristic.md) —
   modelos de passeio aleatório, heurísticas probabilísticas (Kontorovich–Lagarias).
4. [`unverified-proof-claims.md`](unverified-proof-claims.md) — catálogo de "provas"
   publicadas em veículos de baixo rigor. Tratamento cético — **leia antes de reagir
   a qualquer alegação de prova completa** encontrada depois.
5. [`resources-and-tools.md`](resources-and-tools.md) — bibliografias de referência,
   projeto de formalização em andamento, e um paper metodológico sobre colaboração
   humano-LLM neste mesmo problema (relevante para como operamos aqui).
6. [`external-ideas-review.md`](external-ideas-review.md) — avaliação crítica de
   listas de ideias sugeridas por outras IAs.
7. [`ruiz-castillo-research-program.md`](ruiz-castillo-research-program.md) — síntese
   de sete papers do mesmo autor (Juan Carlos Ruiz Castillo) revisados individualmente
   (H-039, H-050, H-052 a H-056): mesma identidade de drift revestida por um
   vocabulário formal diferente a cada paper, dois erros reais de consistência
   interna encontrados, chave explicativa no paper de filosofia da matemática do
   mesmo autor (item 055).

## Conclusão do levantamento inicial

Não há prova aceita pela comunidade matemática. O resultado mais forte e verificado é
o de Tao (anunciado 2019, publicado 2022 em Forum of Mathematics, Pi — PDF arquivado
em `literature/papers/106_Almost-All-Orbits-Almost-Bounded-Values-Tao.pdf`): quase
todas as órbitas atingem valores quase limitados — uma afirmação de densidade, não a
conjectura completa. Verificação computacional cobre todos os inteiros até 2^71
(Barina, 2025 — PDF arquivado em
`literature/papers/110_Improved-Verification-Limit-2-71.pdf`; verificação anterior de
2020/2021 até 10^20 também arquivada, item 105) sem contraexemplo. Ver
`overview-and-known-results.md` para o obstáculo estrutural que todo método conhecido
esbarra.
