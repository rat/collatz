# E-106 — Verificação Monte Carlo da identidade de Jensen (H-127, Proposição C)

Hipótese relacionada: [`H-127-reducao-z-number-dicotomia-espectral-wcc.md`](../../hypotheses/H-127-reducao-z-number-dicotomia-espectral-wcc.md)

## O que é

Promoção formal de um script gerado pelo Fable em scratchpad de sessão
(2026-07-17, `lambda_mc.py`) para experimento persistido no repositório
— pendência explícita registrada em H-127: "não persistido como
experimento formal; promover a E-0xx se este resultado entrar no
paper". O script sobreviveu no scratchpad da sessão de 2026-07-19 e foi
verificado antes de mover (reproduz o valor citado exatamente).

## O que testa

H-127 (Proposição C, item b) deriva, via uma identidade EXATA de
Jensen (não estimativa), que o expoente de decaimento "anelado" do
modelo tilted de gaps satisfaz Λ = log(γ_c), com γ_c = 1+log₄3
(limiar da WCC, c→0). Numericamente γ_c=1,7925, log(γ_c)≈0,5834 — bem
abaixo do log3≈1,0986 necessário para a técnica de Littlewood-Offord
fechar (déficit ~2,2x no orçamento de Fourier incondicional, ~7x com
densidade realista ρ≈0,3). Este é o resultado negativo central da
Proposição C: mesmo no benchmark pseudoaleatório mais favorável, o
orçamento não fecha.

Este experimento confirma numericamente essa identidade via simulação
direta de Z = soma de fases aleatórias ponderadas geometricamente
(8×10⁶ amostras), em dois modelos:

- **Modelo 1** (Geom(1/2), i.i.d. "Syracuse" de Tao 2011): benchmark de
  referência, não o modelo relevante para a WCC.
- **Modelo 2** (Geom tilted, média γ₀=1+log₄3, limiar da WCC): o modelo
  que entra na Proposição C(b) — Λ deve dar log(γ₀).

## Resultado

Modelo 2: Λ medido = 0,5834±0,0005, contra previsto log(γ₀)=0,5836 —
bate dentro do erro. Confirma a identidade de Jensen numericamente
(a identidade em si já é exata/provada, não precisa de Monte Carlo para
ser verdadeira — isso é uma checagem de sanidade da derivação, não uma
descoberta nova).

## Arquivos

- `experiment_lambda_mc.py` — script (documentado, idêntico em lógica
  ao script original de scratchpad).
- `output.txt` — saída completa da execução.

## Reproduzir

```
python3 experiment_lambda_mc.py    # segundos
```
