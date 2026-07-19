# E-031 — Varredura sistemática de primos não testados

Hipótese relacionada: [`H-031-prime-modulus-scan.md`](../../hypotheses/H-031-prime-modulus-scan.md)

## O que foi testado

Se algum primo p≠2,3 (5,7,11,13,17,19,23), ou potência maior de 3 (27,
81), mostra alguma classe residual vazia nos 148 recordistas reais que
não seja já explicada por H-007/H-014/H-022/H-027/H-008.

## Resultado

Nenhuma exclusão nova. Primos 5-23: nenhuma classe com contagem baixa.
Mod 27: única classe com contagem baixa é o caso-base n=2. Mod 81: 3
classes com contagem 0 não explicadas, mas isso é **menos** do que o
esperado por puro acaso (~13 classes, calculado via Poisson) — ruído,
não sinal.

Reproduzir: `python3 experiment.py`.

## Status de H-031

**Confirmada (negativo limpo)** — checagem genuína (resultado não
previsível a priori), sem achado novo. Reforça que a família de exclusão
conhecida (só primos 2 e 3) está completa nos moduli pequenos testados.
