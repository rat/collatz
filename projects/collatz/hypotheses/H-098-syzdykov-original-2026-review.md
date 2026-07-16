# H-098 — Revisão: Syzdykov (2025), "Disproof of Collatz Conjecture by using O-notation" — ALEGAÇÃO DE REFUTAÇÃO REFUTADA (fonte primária da disputa 092/093)

Status: alegação de refutação refutada — mesmo erro categorial já
identificado indiretamente em H-094/H-095, agora confirmado na fonte
primária
Criada em: 2026-07-16
Origem: **novo item no catálogo (115)** — paper original citado por
092 (réplica do mesmo autor, H-094) e 093 (crítica de Lafontaine &
Cheong, H-095), mas que não estava catalogado até agora. Localizado
via busca e baixado manualmente pelo diretor científico. 1 página,
ResearchGate, não peer-reviewed, maio de 2025.

## O que o paper faz

Alega refutação completa da Conjectura de Collatz em menos de uma
página. O argumento central, na íntegra:

1. Assume O(f(n)) ≤ n para a função de Collatz f.
2. Considera n = 2^m − 1 (o caso com o menor número de fatores de 2).
3. Escreve O(f(n)) = O(f(2^m−1)) ≈ 3^m > 2^m−1.
4. Conclui: "isso é uma contradição, logo a função de Collatz não pode
   ser aproximada no número de passos dado" e portanto "a conjectura
   de Collatz é falsa para qualquer inteiro".

## Avaliação

**O mesmo erro categorial já identificado por Lafontaine & Cheong
(item 093, H-095)**, agora visível diretamente na fonte: O(f(n)) denota
uma classe de funções (um conjunto), não um valor escalar — a
expressão O(f(n)) ≤ n já não tem sentido bem definido antes de
qualquer cálculo. Além disso, o passo 3 comete um segundo erro
independente: mesmo tratando informalmente O(f(n)) como "o número de
passos", "3^m > 2^m−1" não é uma contradição matemática — é apenas um
fato aritmético verdadeiro (3^m cresce mais rápido que 2^m para m
grande), sem nenhuma relação lógica estabelecida com a premissa do
passo 1. O texto simplesmente declara "contradição" sem derivar uma
de fato. Não há uso de nenhuma propriedade real da função de Collatz
além da notação mal-empregada — nenhuma trajetória real é calculada,
nenhuma fórmula de órbita é usada.

**Confirma retroativamente H-094 e H-095**: a réplica do próprio autor
(item 092) já havia mostrado, ao defender o artigo original contra a
crítica, que ele de fato trata O(f(n)) como um valor numérico
específico ("o número de passos") — o que este documento primário
confirma diretamente. A crítica de Lafontaine & Cheong (H-095) estava
correta e não é uma leitura uncharitable do argumento original.

## O que não é possível verificar computacionalmente

Não há fórmula, cálculo ou alegação numérica testável no texto — é
puramente um argumento verbal com uma notação malformada. Não há nada
para reproduzir experimentalmente além de confirmar que "3^m>2^m-1"
é aritmética trivialmente verdadeira (não uma contradição), o que não
requer script dedicado.

## Referências

- Réplica do próprio autor: H-094 (item 092).
- Crítica publicada: H-095 (item 093, Lafontaine & Cheong) — já
  identificava corretamente este erro sem acesso direto a este texto.
- Paper: `literature/papers/115_Disproof-Collatz-Conjecture-O-notation.pdf`.
