# E-017 — Cauda do pico da órbita: fator exato de 2 por bit

Hipótese relacionada: [`H-017-peak-excursion-tail.md`](../../hypotheses/H-017-peak-excursion-tail.md)

## O que foi testado

A sequência de Collatz é um martingale multiplicativo exato (E[3/2^a]=1,
verificado analiticamente — soma exata da série geométrica, não
aproximação). Isso implica, via equação de Cramér para grandes desvios, que
o expoente de decaimento da cauda do pico da órbita é **exatamente θ*=1**
— verificamos isso resolvendo 3^θ = 2^(1+θ)−1 e confirmando θ=1 é raiz
exata (3¹=3, 2²−1=3).

Previsão: P(pico(n) ≥ n·2^Δ) ~ C·2^(−Δ) — a cauda decai por um fator de
exatamente 2 a cada bit extra de excursão.

## Resultado

Amostra de 2.000.000 de n aleatórios em [10⁹, 10¹²]. Ajuste log-linear de
P(Δ≥x) vs. x:

- Usando todos os pontos com contagem estatística razoável (x=2 a 15):
  inclinação empírica = **−0.9657** (previsto −1.0).
- Usando só a cauda mais distante (x≥6, onde a aproximação assintótica é
  mais precisa): inclinação empírica = **−1.0045** — diferença de apenas
  **0.45%** do valor teórico exato.

Reproduzir: `python3 experiment.py 2000000 1000000000 1000000000000 99`
(~30s). Confirmado também com amostra menor (500k) e seed diferente (42):
inclinação −0.9682 (todos os pontos).

## Conclusão

O expoente de Cramér θ*=1 (sem nenhum parâmetro livre, derivado só da
propriedade de martingale já implícita em H-001) prevê a cauda do pico da
órbita com precisão de menos de 0.5% na região assintótica. Esta é a
terceira confirmação teórica precisa do projeto no estilo H-010/H-011
(derivar → confirmar), desta vez para o **máximo** da órbita em vez da
média/variância do tempo.

## Status de H-017

**Confirmada** (inclinação da cauda distante dentro de 0.5% do previsto).
