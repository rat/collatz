# E-021 — Erosão de runs de 1s terminais

Hipótese relacionada: [`H-021-terminal-run-erosion.md`](../../hypotheses/H-021-terminal-run-erosion.md)

## O que foi testado

(a) Regra de erosão: n terminando em run de t≥2 uns dá valuação a=1 e
resultado com run t−1. (b) Comparação de comprimento médio de runs de a=1
entre recordistas oficiais e órbitas típicas.

## Resultado

(a) **Confirmada sem exceção** em 50.000 testes, t de 2 a 20.

(b) Recordistas: 13.741 runs, média=**2.512**. Órbitas típicas: 4.744 runs,
média=**2.035** (bate quase exatamente com a previsão teórica sob H-001:
E[run]=1/(1−0.5)=2, já que a run de a=1's consecutivos, sob i.i.d.
geométrica(1/2), é ela mesma geométrica com taxa de parada 0.5).

## Interpretação (com ressalva de tautologia)

Recordistas têm runs de subida (a=1) sistematicamente mais longos que o
típico. Isso é plausível mas **parcialmente tautológico**: ter stopping
time excepcionalmente alto quase por definição exige períodos mais longos
de descida lenta (a=1 = subida, contribui menos para a queda). Não
tratamos isso como descoberta nova — é consistente com (e talvez
redutível a) o próprio mecanismo que já caracterizamos em H-002/H-004.

Reproduzir: `python3 experiment.py 50000`.

## Status de H-021

**Confirmada** (mecanismo de erosão, parte a) e **suportada com ressalva
de tautologia** (diferença de runs recordistas vs. típico, parte b) — não
apresentada como descoberta nova.
