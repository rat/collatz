# H-017 — Cauda do pico da órbita: decaimento exato de fator 2 por bit

Status: confirmada (inclinação da cauda −1.0045 vs teórico −1.0, diferença 0.45%)
Criada em: 2026-07-13
Origem: ideia do brainstorm do modelo Fable ("H-D"), derivação verificada
independentemente antes de testar.

## Enunciado

A sequência de valores ímpares de uma órbita de Collatz é, sob o modelo
i.i.d. já validado (H-001/H-003), um **martingale multiplicativo exato**:
E[3/2^a] = 1 (não uma aproximação — soma exata da série geométrica). Isso
implica, via teoria de grandes desvios para passeios aleatórios com deriva
(equação de Cramér), que o expoente de decaimento da cauda do **pico** da
órbita (o maior valor atingido antes de descer a 1) é **exatamente θ*=1,
sem parâmetro livre**:

P(pico(n) ≥ n · 2^Δ) ~ C · 2^(−Δ) para Δ grande

ou seja: a cada bit extra de "excursão" acima do tamanho inicial de n, a
probabilidade cai por um fator de exatamente 2 — nem mais, nem menos.

## Derivação da equação de Cramér

Por passo acelerado, m/n ≈ 3/2^a (a = valuação, Geométrica(1/2)). Queremos
θ* tal que E[(3/2^a)^θ*] = 1 (condição de Cramér para a cauda exponencial de
um passeio multiplicativo). Isso dá:

3^θ* · Σ_{k=1}^∞ 2^(−k) · 2^(−θ*k) = 3^θ* / (2^(1+θ*) − 1) = 1

Testando θ*=1: 3¹=3, 2²−1=3 — **bate exatamente**. Isso não é coincidência:
θ*=1 é justamente a condição do martingale (E[3/2^a]=1 já usa exatamente
θ=1 no expoente). Verificado numericamente antes de prosseguir.

## Como testar

Amostrar n grandes e aleatórios (evitar números pequenos, onde a
aproximação 3n+1≈3n falha), computar pico(n) = maior valor na órbita
completa, Δ(n) = log₂(pico) − log₂(n), e estimar P(Δ≥x) para vários x.
Previsão: log₂(P(Δ≥x)) vs. x deveria ter inclinação exatamente −1.

## Atualizações

- 2026-07-13: hipótese aberta, equação de Cramér verificada numericamente
  (θ*=1 exato).
- 2026-07-13: testada em `experiments/E-017-peak-excursion-tail/` (2M
  amostras, n em [10⁹,10¹²]). Inclinação empírica da cauda distante (x≥6):
  −1.0045 vs. teórico −1.0 (diferença 0.45%). Confirmado com duas amostras
  independentes (500k e 2M, seeds diferentes). Terceira confirmação teórica
  precisa do projeto (no estilo H-010/H-011), agora para o máximo da órbita.
