# E-013 — Estrutura do último valor ímpar de uma órbita

Hipótese relacionada: [`H-013-last-odd-value-structure.md`](../../hypotheses/H-013-last-odd-value-structure.md)

## O que foi testado

Se o último valor ímpar (>1) de qualquer órbita é sempre J_t=(4^t−1)/3
(consequência de H-012), e como se distribui o valor de t.

## Resultado (300.000 amostras aleatórias, n até 10^9)

Fórmula confirmada sem exceção. Distribuição de t:

| t | J_t | fração |
|---|---|---|
| 2 | 5 | 93.77% |
| 4 | 85 | 2.37% |
| 5 | 341 | 3.78% |
| 7 | 5461 | 0.01% |
| 8 | 21845 | 0.06% |
| 10 | 349525 | ~0% |
| 11 | 1398101 | ~0% |

Classes t=3,6,9 (J_t divisível por 3: 21, 1365, 87381) têm **zero**
ocorrências — explicado por H-005 (valor divisível por 3 nunca reaparece
depois do primeiro passo ímpar de uma órbita genérica).

**Anomalia não explicada**: t=5 tem fração maior que t=4, contrariando a
expectativa ingênua de decaimento monotônico ~1/4 por passo. Registrado como
questão em aberto em H-013.

Reproduzir: `python3 experiment.py 300000 2`

## Status

**Confirmada** (estrutura + explicação das classes estéreis). Anomalia p₅>p₄
deixada como questão em aberto.
