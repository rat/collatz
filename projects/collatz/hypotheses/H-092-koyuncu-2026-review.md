# H-092 — Revisão: Koyuncu et al. (2026), "Parity-Based Level-Set Approach to the Collatz Conjecture"

Status: revisado, sem erros encontrados
Criada em: 2026-07-16
Origem: item 071 do catálogo (`literature/papers/INDEX.md`), baixado
manualmente pelo diretor científico (estava bloqueado para download
automatizado por 403 do mdpi.com). Mathematics 2026, 14, 1763, MDPI —
peer-reviewed formal, journal estabelecido.

## O que o paper faz

Define o conjunto de nível l_x = {n : L(n) = x} (L = comprimento de
Collatz) e, para cada n ∈ l_x, o vetor de paridade p(n) (1 se o passo é
ímpar, 0 se par). k(n) = número de passos ímpares. Particiona l_x em
subconjuntos S_{x,k} pelo valor de k, e estuda a média μ_{x,k} de cada
subconjunto.

**Lemma 1** (fórmula exata): se t_1<...<t_k são as posições dos passos
ímpares, então

  n = 2^(x-k)/3^k − Σ_{r=1}^k 2^(t_r+1-r)/3^r

equivalentemente n = C(p)·2^x/6^k, onde C(p) = n·6^k/2^x depende só do
padrão de paridade.

**Lemma 2, Corolário 1, Teorema 1**: assumindo que C(p) é uniformemente
limitado (A_x ≤ C(p) ≤ B_x) dentro de cada l_x — o que é
automaticamente verdade para qualquer x finito, já que C(p) é um
mínimo/máximo sobre um conjunto finito — derivam por álgebra direta
que μ_{x,k} respeita os mesmos limites, que a razão μ_{x,k+1}/μ_{x,k}
fica no intervalo [A_x/(6B_x), B_x/(6A_x)], e que diferenças entre
razões sucessivas são limitadas pelo comprimento desse intervalo.

**Seção 3 (resultado empírico central)**: para todo n≤100.000 e
L=10..50, calcula l_x, particiona por k, ajusta regressão log(μ_k)=a+bk
— relata slope b estável entre −1.80 e −1.86, R²≈1 em toda a faixa.

## Verificação

`experiments/E-092-koyuncu-2026-review/experiment.py`:

1. **Lemma 1 verificado exatamente** (aritmética `Fraction`, sem erro de
   arredondamento) contra 6 trajetórias reais, incluindo n=27 (241
   passos) e n=837799 (524 passos, recordista clássico até 10⁶) —
   bate em todos os casos.
2. **Tabela 1 reproduzida de forma essencialmente exata**: para
   L=10,11,12 os valores de b batem com o paper até a 4ª casa decimal
   (-1.8563, -1.8464, -1.8307 — idênticos). Para L=13..30 (faixa
   testada), slopes e R² batem no mesmo padrão de estabilidade relatado
   pelo paper.

## Observação (não é erro, mas nuance que o paper não discute)

O slope médio observado (−1.8300, desvio-padrão 0.0108 em L=10..30) é
sistematicamente mais negativo que o valor "ingênuo" −log(6)≈−1.7918
que a própria heurística do paper (Seção 2, antes do Lemma 2) sugeriria
se C(p) fosse aproximadamente constante. O paper nunca reivindica que
b deveria ser exatamente −log(6) — trata b como parâmetro empírico de
ajuste — mas também não comenta ou explica essa diferença sistemática
de ~0,04 (2%). Não invalida nada do que é reivindicado, só fica como
uma pergunta em aberto não explorada pelos próprios autores.

## Avaliação

Paper metodologicamente limpo e honesto: não alega provar nada sobre a
conjectura, distingue claramente heurística (Seção 2) de resultado
formal condicional (Lemma 2 em diante, sob hipótese explícita de
limitação uniforme) de resultado empírico (Seção 3). Toda a matemática
verificada bate exatamente. Mesmo território que outros papers já
revisados nesta coleção (fatoração de n em termo de magnitude ×
resíduo de padrão — ecoa H-086/H-087 deste projeto, embora sem conexão
direta), mas aqui aplicado à estrutura de nível fixo (mesmo x), não à
árvore reversa.

## Referências

- Experimento: `experiments/E-092-koyuncu-2026-review/experiment.py`.
- Paper: `literature/papers/071_Parity-Based-Level-Set-Approach-Collatz.pdf`.
