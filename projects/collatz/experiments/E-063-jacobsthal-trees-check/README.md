# E-063 — Verificação do paper #032 (Kosobutskyy & Mailland, "Jacobsthal Trees and Generalized κx±1 Transformations")

Hipótese relacionada: [`H-063-jacobsthal-trees-review.md`](../../hypotheses/H-063-jacobsthal-trees-review.md)

## Paper

Kosobutskyy, P. & Mailland, D. (2026). *Jacobsthal Trees and
Generalized κx±1 Transformations*. Communications in Advanced
Mathematical Sciences, 9(2), 77-91, peer-reviewed. PDF local:
`literature/papers/032_Jacobsthal-Trees-Generalized-Transformations.pdf`.

Também cobre os exemplos numéricos do paper #084 (mesmos autores, versão
pedagógica restrita a κ=3) — ver [`H-065`](../../hypotheses/H-065-mailland-kosobutskyy-jacobsthal-viewpoint-review.md).

## O que foi testado

Paper estrutural/notacional que generaliza a árvore inversa de Collatz
para `κx±1` (κ ímpar qualquer) via "números de Jacobsthal
generalizados". Não alega provar a conjectura clássica.

1. Definição 1.1 vs. Tabela 2.1 (reduz-se a Jacobsthal clássico, OEIS
   A001045, no caso κ=3).
2. Teorema 2.1 (periodicidade) — `T_κ` = ordem multiplicativa de 2 mod
   κ, testado para κ=1..199 e contra a Tabela 2.2 (incluindo um número
   de 52 dígitos para κ=181).
3. Tabela 2.4 (formação periódica dos nós) — 24 células.
4. Tabela 2.6 / Remark 1.7 (pontos-atratores) — simulação direta do
   mapa forward para κ=3,5,181.
5. Property 2.6 (unicidade da partição).
6. Property 2.7 (nós de ramificação = valores ímpares no ciclo).
7. Property 2.5 (razão assintótica entre nós consecutivos).
8. Exemplos específicos do paper #084 (caso especial κ=3).

## Resultado

**0 falhas em todas as 8 partes.** Um achado menor: o Remark 1.7 diz
"PA={1,27,35}" para κ=181, mas a própria Tabela 2.6 mostra que `q0=1`
diverge sob κ=181 (`⋯→1→∞`) — confirmado por simulação (diverge,
32+ dígitos em 47 iterações). Inconsistência textual entre seções do
mesmo paper, não um erro matemático de fundo.

## Nota de metodologia

Duas iterações do próprio script de verificação continham bugs de
indexação (mistura das famílias `m`/`p`, que têm paridades de índice
diferentes) — corrigidos antes de finalizar; ver seção "Notas de
metodologia própria" em H-063 para detalhes.

## Como reproduzir

```
python3 experiment.py
```

Sem dependências além da stdlib. Roda em alguns segundos.
