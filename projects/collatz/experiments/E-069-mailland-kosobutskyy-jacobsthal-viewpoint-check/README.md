# E-069 — Verificação do paper #084 (Mailland & Kosobutskyy, "Modelling the Collatz Problem from a Jacobsthal Viewpoint")

Hipótese relacionada: [`H-069-mailland-kosobutskyy-jacobsthal-viewpoint-review.md`](../../hypotheses/H-069-mailland-kosobutskyy-jacobsthal-viewpoint-review.md)

## Paper

Mailland, D. & Kosobutskyy, P. (2026). *Modelling the Collatz Problem
from a Jacobsthal Viewpoint*. Communications in Advanced Mathematical
Sciences, 8(1), 49-55, peer-reviewed. PDF local:
`literature/papers/084_Modelling-Collatz-Jacobsthal-Viewpoint.pdf`.

Versão pedagógica, restrita a κ=3, do mesmo framework do paper #032
(mesmos autores, ordem reversa) — ver
[`E-063`](../E-063-jacobsthal-trees-check/) / [`H-063`](../../hypotheses/H-063-jacobsthal-trees-review.md).

## O que foi testado

Este script **não duplica** E-063 (que já verificou exaustivamente o
framework geral e os dois exemplos numéricos deste paper na sua Parte
8). Cobre apenas o que E-063 não tinha verificado:

1. Eq. 5-8 (integralidade/periodicidade mod 3) — reconfirmação rápida e
   independente.
2. Exemplos 1 e 2 do paper — reconfirmação rápida.
3. Fig. 1 — reconstrução da árvore geradora completa (colunas θ=5 e
   θ=1 expandidas em vários k, incluindo os ramos mortos θ=3,21).
4. Fig. 2 — confirma que as 10 colunas mostradas na rede de Petri são
   alcançáveis a partir da raiz θ=1.

## Resultado

**0 falhas em todas as 4 partes.** Nenhum erro matemático encontrado.

## Nota de metodologia

Leitura visual inicial da Fig. 1 sugeriu incorretamente que os nós 57 e
229 estariam ligados a 85; verificação computacional mostrou que ambos
vêm de θ=43, não de θ=85. Provável erro de transcrição da figura (não
do paper) — ver H-069 para detalhes. Por isso o script verifica apenas
os números (todos válidos), não a adjacência exata de cada aresta.

## Como reproduzir

```
python3 experiment.py
```

Sem dependências além da stdlib. Roda em menos de um segundo.
