# H-049 — Revisão do paper #007 (Hikawa, "Parity Vector Structures") — sem erros encontrados

Status: revisão externa concluída — paper combinatório de alta
qualidade, todos os teoremas testados confirmados corretos
Criada em: 2026-07-14
Origem: paper baixado manualmente pelo diretor científico (item 007 da
coleção, `literature/papers/007_Parity-Vector-Structures-Accelerated-Collatz.pdf`,
Kazunobu Hikawa, Professor Emeritus, Kanazawa Gakuin University, 34 páginas).

## O paper

"Finite-Dimensional Combinatorial and Arithmetic Structures of Parity
Vectors for the Accelerated Collatz Map" — estudo puramente
combinatório/aritmético sobre "vetores de paridade" (strings binárias
que codificam a sequência ímpar/par do mapa acelerado T), classificados
por comprimento k e peso de Hamming d (número de passos ímpares). É o
terceiro estágio de uma série de investigações (após Hikawa–Nakanishi
2026 e Nakanishi 2026, citados como refs [10]-[11]) que completa
rigorosamente uma identidade empírica observada anteriormente.

## O que foi verificado (todos confirmados)

- **Teorema 3.2** (bijeção explícita Φ:U(d)→J(d+1), identidade
  X(d+1)=W(d)): confirmado por força bruta para d=1..7
  (`experiments/E-049-hikawa-parity-vector-structures-check/`) — a
  imagem de Φ aplicada a todo U(d) coincide exatamente com J(d+1).
- **Teorema 5.2** (rigidez 2-ádica: para vetores de mesmo comprimento
  e mesmo peso, a valuação 2-ádica da diferença dos termos de correção
  é determinada exatamente pelo primeiro índice onde os vetores
  diferem): confirmado em 2000 pares aleatórios, aritmética exata.
- **Remark 5.3** (contraexemplo do próprio paper mostrando que a
  hipótese de peso igual é necessária): confirmado — a fórmula
  realmente falha para pesos desiguais, exatamente como o autor prevê.
- **Tabelas 1-2** (valores numéricos de W(k) e W(d)): reproduzidos
  exatamente via reimplementação independente do Algoritmo 1 (DP),
  para k=1,10,100 e d=1,2,5,10,20 — todos batem (k=100 bate dentro do
  arredondamento de 3 dígitos significativos que o paper usa).

**Nenhum erro encontrado** em nenhuma reivindicação testável.

## Caráter do paper

Diferente de quase todos os outros itens da coleção, este paper não
propõe nenhum mecanismo, analogia ou heurística sobre a dinâmica global
do Collatz — é inteiramente sobre a estrutura combinatória FINITA do
espaço de vetores de paridade (independente de o Collatz ser verdadeiro
ou falso). O próprio autor repete essa ressalva em praticamente toda
seção: "The results established in this paper concern finite
parity-vector structures and are derived independently of the truth or
falsity of the Collatz conjecture"; "these finite-dimensional results
do not by themselves determine the existence or nonexistence of such
an infinite trajectory... remain an open problem"; "Accordingly, the
present work should be regarded as a study of finite-dimensional
combinatorial and arithmetic structures... rather than as a proof
strategy for the Collatz conjecture itself." A Figura 4 (um "corredor
infinito hipotético") é explicitamente rotulada "purely illustrative
and should not be interpreted as a rigorous theorem."

Declara uso de IA generativa apenas para "clarifying the prose and
adjusting the structure", com responsabilidade final do autor — mesma
prática exemplar de transparência de H-042 (Williams).

## Novas hipóteses?

Nenhuma diretamente aplicável à nossa linha principal. A classificação
por peso de Hamming e a "rigidez 2-ádica" são resultados combinatórios
autocontidos sobre o espaço de vetores de paridade, não sobre a
dinâmica de convergência em si — não conectam com nosso obstáculo
estrutural central (H-013/H-018/H-024/H-028).

## Atualizações

- 2026-07-14: paper lido por completo (34 páginas), teoremas centrais
  verificados computacionalmente
  (`experiments/E-049-hikawa-parity-vector-structures-check/`), nenhum
  erro encontrado. Flags atualizadas em `literature/papers/INDEX.md`
  (item 007: Lido=Sim, Corrigido=Sim [nada a corrigir], Implementado=Sim).
