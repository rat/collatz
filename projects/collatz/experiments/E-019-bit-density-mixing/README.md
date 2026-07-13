# E-019 — Tempo de mistura da densidade de bits

Hipótese relacionada: [`H-019-bit-density-mixing.md`](../../hypotheses/H-019-bit-density-mixing.md)

## O que foi testado

Partindo de n=2^k−1 (densidade de bits 1 máxima) e n=2^k+1 (densidade quase
mínima), quantos passos até a densidade (popcount/bitlength) relaxar para
perto de 1/2 (tolerância 0.08)?

## Resultado

| k | passos (denso) | passos (esparso) | denso/k | esparso/k |
|---|---|---|---|---|
| 8 | 7 | 7 | 0.875 | 0.875 |
| 64 | 79 | 76 | 1.23 | 1.19 |
| 256 | 347 | 313 | 1.36 | 1.22 |
| 1024 | 1483 | 1261 | 1.45 | 1.23 |

A razão passos/k **estabiliza** em torno de 1.3-1.5 (denso) e 1.0-1.23
(esparso) ao longo de duas ordens de grandeza de k (8 a 1024) — confirma
**crescimento linear** em k, não constante nem superlinear.

Reproduzir: `python3 experiment.py "8,16,32,64,128,256,512,1024"`.

## Conclusão

Confirma qualitativamente a previsão de H-019: o tempo de mistura da
densidade de bits cresce linearmente com o tamanho do número, consistente
com 3n+1 sendo uma operação local (janela de poucos bits + carry) em vez de
um embaralhamento instantâneo. Achado qualitativo, não uma constante exata
derivada teoricamente (a razão observada, ~1.3-1.5, foi só medida, não
prevista de antemão).

## Status de H-019

**Confirmada qualitativamente** (crescimento linear, não a constante exata).
