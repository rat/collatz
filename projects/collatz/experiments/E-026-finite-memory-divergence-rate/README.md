# E-026 — Taxa de divergência de aproximações de memória 3-ádica finita

Hipótese relacionada: [`H-026-divergence-rate-independent-of-K.md`](../../hypotheses/H-026-divergence-rate-independent-of-K.md)

Origem: extensão de H-024/E-024, item #15 de uma quarta lista de ideias
externas.

## O que foi testado

Se usar mais dígitos 3-ádicos (K maior) ao aproximar D(v) por resíduo
"aguenta" mais tempo (magnitude maior) antes de divergir do valor real,
comparado a usar menos dígitos (K menor).

## Bug encontrado e corrigido no caminho

Primeira tentativa usou multiplicadores consecutivos (m=0,1,2,5,...) com
uma correção de paridade ("se v par, soma mod"). Como mod=3^K é ímpar e o
resíduo-base é ímpar, m ímpar seguido de correção podia colidir com o
v bruto do próximo m par (ex: m=1 corrigido dava exatamente o mesmo v que
m=2 sem correção). Corrigido usando só multiplicadores pares — garante v
ímpar sem precisar de correção, eliminando a colisão.

## Resultado

Comparando K=4,6,8 na mesma faixa de magnitude de v (não no mesmo
multiplicador m, que dá escalas bem diferentes por K): a divergência
|log(D(v)/D(v₀))| fica na mesma ordem de grandeza para os três K's. Não há
evidência de que resíduo mais profundo atrase a divergência.

**Ressalva**: cada ponto é uma única medição de uma quantidade já
conhecida (H-024) como extremamente errática — não é uma média
estatística. Resultado sugestivo, não robusto. Ver hipótese para detalhes
e não-monotonicidade observada dentro do mesmo K.

Reproduzir: `python3 experiment.py 18 4,6,8 0,2,4,10,20,50,100,200,400`
(requer o módulo `experiment.py` de E-018 no path relativo).

## Status de H-026

**Confirmada com ressalva** — sinal real mas não estatisticamente
robusto; promediar sobre múltiplos resíduos por (K, magnitude) é o
próximo passo natural se esta linha for retomada.
