# E-014 — Exclusão por empate: recordistas nunca ≡5 mod 8

Hipótese relacionada: [`H-014-tie-exclusion-mod8.md`](../../hypotheses/H-014-tie-exclusion-mod8.md)

## O que foi testado

Para N=4u+1 com u ímpar (N≡5 mod 8), se total_stopping_time(N) =
total_stopping_time(N−1) exatamente (empate por coalescência de
trajetórias — prova completa em `hypotheses/H-014-tie-exclusion-mod8.md`),
e se nenhum recordista oficial cai nessa classe.

## Resultado

- Identidade σ(N)=σ(N−1) confirmada sem exceção em 200.000 casos aleatórios.
- **Nenhum dos 148 recordistas oficiais (OEIS A006877) é ≡5 mod 8.**

Reproduzir: `python3 experiment.py 200000 1`

## Status

**Confirmada.** Segunda técnica de exclusão de classe residual do projeto
(a primeira foi H-007, via domínio estrito; esta é via empate exato).
