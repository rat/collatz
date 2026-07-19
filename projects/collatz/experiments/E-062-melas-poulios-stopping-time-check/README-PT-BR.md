# E-062 — Verificação do paper #031 (Melas & Poulios, "Predicting Extreme Stopping Time Behavior")

Hipótese relacionada: [`H-062-melas-poulios-stopping-time-review.md`](../../hypotheses/H-062-melas-poulios-stopping-time-review.md)

## Paper

Melas, E. & Poulios, N.C. (2026). *Predicting Extreme Stopping Time
Behavior in the Collatz System: A Probabilistic and Statistical
Approach*. Journal of Dynamics and Games (AIMS), peer-reviewed. PDF
local: `literature/papers/031_Predicting-Extreme-Stopping-Time.pdf`.

## O que foi testado

Paper estatístico (regressão logit + árvore de decisão) para prever
tempo de parada extremo, não para provar Collatz. Usa `Col(n)=n/2`
(par) `/(3n+1)/2` (ímpar) — mapa diferente do acelerado `T(n)` usado
em outras revisões desta coleção.

1. Identidade logarítmica exata (Eq. 3), via `Fraction`, 300 casos.
2. Exemplo numérico específico do paper (`n=10`).
3. Sanidade do mapa Collatz modificado `Col_mod` (`n=2..200.000`).
4. Reprodução exata e determinística (censo completo, sem amostragem
   aleatória) das 6 janelas de densidade citadas (Figuras 7 e 8).

## Resultado

**Tudo confirmado exatamente**, incluindo as 6 contagens de densidade
(potências de 10 e de 3, até `10¹⁵`). Os modelos logit/árvore de
decisão (Seções 5-7) não foram reproduzidos byte-a-byte — dependem de
amostragem aleatória cujo gerador/semente exato não é totalmente
especificado no paper (fora de escopo, não uma falha).

## Como reproduzir

```
python3 experiment.py
```

Sem dependências além da stdlib (`fractions`). Roda em ~1,6s.
