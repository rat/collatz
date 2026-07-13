# H-010 — Constante assintótica do stopping time: derivação própria vs. dados

Status: confirmada (K empírico 7.1833 vs teórico 7.2283, diferença 0.62%)
Criada em: 2026-07-13

## Enunciado

A heurística de passeio aleatório padrão (Kontorovich–Lagarias,
`literature/approaches-stochastic-heuristic.md`) prevê que
total_stopping_time(n) cresce como K·log₂(n) para uma constante K derivável
da distribuição geométrica das valuações. Propomos derivar K nós mesmos a
partir dos fatos já estabelecidos em H-001 (marginal geométrica de a(n),
E[a]=2; independência não rejeitada) e comparar com um ajuste empírico direto
nos nossos próprios dados — não só citar a literatura qualitativamente, como
o diretor científico pediu.

## Derivação

Por passo acelerado, log₂(m/n) ≈ log₂3 − a. Como E[a]=2 (H-001), o "drift"
esperado por passo é log₂3 − 2 ≈ −0.41504. Logo o número esperado de passos
acelerados para ir de n a O(1) é ≈ log₂(n)/0.41504 ≈ 2.4095·log₂(n). Cada
passo acelerado consome, em média, 1 (passo ímpar) + E[a]=2 (divisões) = 3
passos padrão. Logo:

total_stopping_time(n) ≈ 3 / (2 − log₂3) · log₂(n) ≈ **7.2283 · log₂(n)**

## Como testar

Calcular total_stopping_time(n) para uma amostra grande de n, ajustar
regressão linear contra log₂(n), e comparar o coeficiente angular empírico
com o K≈7.2283 derivado acima. Também reportar a dispersão dos resíduos.

## Atualizações

- 2026-07-13: hipótese aberta, derivação teórica registrada.
- 2026-07-13: testada em `experiments/E-010-stopping-time-asymptotic-constant/`
  (~1M amostras, n até 2M). K empírico=7.1833 vs teórico=7.2283 (diferença
  0.62%) — ótima concordância. R²=0.03: log₂(n) sozinho explica muito pouco
  da variância individual — a maior parte vem de estrutura fina, não do
  tamanho de n. Desvio padrão dos resíduos cresce lentamente com log₂(n),
  consistente com teoria de tempos de passagem de passeios aleatórios com
  deriva. Confirmada.
