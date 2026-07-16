# H-095 — Revisão: Lafontaine & Cheong (2026), "A Note on a Claimed Disproof of the Collatz Conjecture" — sem erros

Status: revisado, sem erros encontrados — crítica correta e bem
fundamentada
Criada em: 2026-07-16
Origem: item 093 do catálogo, baixado manualmente pelo diretor
científico (bloqueado, ResearchGate). 6 páginas (4 de conteúdo + 2 de
referências), não peer-reviewed (nota curta/comentário técnico), mas
metodologicamente sólida.

## O que o paper faz

Nota crítica curta e focada, analisando um único passo de um argumento
publicado por M. Syzdykov ("Disproof of Collatz Conjecture by using
O-notation", ResearchGate preprint, 2025 — **não catalogado neste
projeto**, conhecido só indiretamente). Não é uma revisão completa do
argumento de Syzdykov — os autores dizem isso explicitamente.

O ponto central: Syzdykov usa uma expressão da forma O(f(n)) ≤ n. Os
autores mostram que essa expressão é **malformada** (não apenas
incorreta): Big-O denota um conjunto de funções,

  O(f(n)) = {g : ∃C>0, ∃n₀, ∀n≥n₀, |g(n)| ≤ C|f(n)|},

um objeto de natureza conjuntística, enquanto n é um inteiro escalar.
Comparações como "O(f(n)) ≤ n" tentam ordenar objetos de categorias
incompatíveis — não são falsas no sentido matemático usual, são
indefinidas. Além disso, mesmo quando uma função específica L(n)
satisfaz L(n)∈O(f(n)), isso só garante uma cota assintótica (existe
C,n₀ tal que L(n)≤Cf(n) para n≥n₀) — não uma conclusão pontual sobre o
valor exato de L(n) para um n individual, que é o que a alegação de
refutação de Syzdykov precisaria.

## Avaliação

O ponto é matematicamente correto e é uma confusão real e documentada
na literatura de notação assintótica em geral (não específica de
Collatz) — comparar uma classe O(·) a um número é de fato um erro
categorial padrão, e a distinção entre cota assintótica (existencial,
"para n grande") e cota pontual (universal, "para todo n") é
exatamente a diferença entre um argumento heurístico/de ensemble e uma
prova sobre trajetórias individuais — o mesmo tipo de confusão que
este projeto já identificou repetidamente em outras alegações de prova
(H-045, H-065, e agora H-093/Tynski nesta mesma rodada).

**Confirmação cruzada**: a réplica do próprio Syzdykov a esta crítica
(item 092, "Continued Disproof Sentence", H-094) não nega ter usado
O(f(n)) como se fosse um valor escalar — ao contrário, ele **defende**
essa interpretação não-padrão como "a correta". Isso reforça, pela
própria reação do autor criticado, que a caracterização de Lafontaine
& Cheong do argumento original é precisa, não uma leitura injusta ou
uncharitable.

O paper é honesto sobre seu escopo limitado ("O propósito desta nota
não é discutir a conjectura de Collatz em geral... focamos
exclusivamente no passo central") e se anuncia como o primeiro de uma
série examinando manuscritos recentes sobre Collatz — não encontramos
os outros da série no nosso catálogo.

## O que não foi possível verificar

O paper original de Syzdykov que é objeto da crítica não está
catalogado neste projeto — não pudemos ler o argumento completo na
fonte primária, só através das citações de ambos os itens 092 e 093 (e
da própria caracterização dos autores, corroborada pela reação do
autor criticado).

## Referências

- Paper: `literature/papers/093_Note-Claimed-Disproof-Collatz-Conjecture.pdf`.
- Réplica do autor criticado: H-094 (item 092, Syzdykov).
- Padrão de erro análogo (mistura de cota assintótica/média com
  garantia pontual/determinística): H-045, H-065, H-093.
