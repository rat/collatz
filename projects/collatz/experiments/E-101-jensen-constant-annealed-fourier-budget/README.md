# E-101 — Constante de Jensen do orçamento de Fourier anelado (parede da Proposição C)

Hipótese relacionada: [`H-127-reducao-z-number-dicotomia-espectral-wcc.md`](../../hypotheses/H-127-reducao-z-number-dicotomia-espectral-wcc.md)

## O que foi feito

Calibração Monte Carlo do expoente de decaimento "anelado" (fases
independentes uniformes — o benchmark pseudoaleatório) do fator local
de uma cascata de produto de Riesz do tipo usado no post de blog de
Tao (2011, Littlewood-Offord/potências de 2 e 3), gerado originalmente
pelo Fable durante a consulta sobre o lema de redução Z-number (H-127)
e reproduzido/verificado nesta sessão.

Modelo: Z = Σ_{g≥1} w_g·e(U_g), U_g uniformes i.i.d. em [0,1), pesos
geométricos w_g = p(1-p)^{g-1} normalizados. Calcula-se
Λ := E[log(1/|Z|)] por Monte Carlo (2×10⁶ amostras, truncado em
G=60 termos — cauda geométrica já desprezível), para dois modelos:

- **Modelo 1** (p=1/2): pesos Geom(1/2), o modelo i.i.d. original de
  Tao (2022) para a medida de Syracuse.
- **Modelo 2** (p=1/γ₀, γ₀=1+log₄3≈1,7925): pesos tilted à inclinação
  crítica do limiar da WCC de Wirsching (j*/ℓ no limiar ingênuo).

A identidade de Jensen (E_U log|p·e(U)+(1-p)Z′| = log p sempre que
|Z′|≤p/(1-p), automático para p≥1/2 i.e. γ≤2) dá Λ=log γ **exatamente**
— o Monte Carlo é uma verificação, não a fonte do valor.

## Resultado

- Modelo 1: Λ = 0,6929 ± 0,0006 = ln 2 (exato, confirma a identidade).
- Modelo 2 (limiar WCC): Λ = 0,5834 ± 0,0005 = log(1,7925) = log γ₀
  (exato, confirma a identidade no ponto relevante para a WCC).
- Em ambos os casos, Λ < log 3 ≈ 1,0986 — **o orçamento de Fourier
  anelado cabe sem nenhuma estrutura extra**: um buraco espectralmente
  difuso é auto-consistente do ponto de vista ℓ¹, com folga de fator
  e^{log3-Λ} ≈ 1,88 (modelo 2). Esta é a base numérica da Proposição C
  de H-127 — explica por que a técnica de Littlewood-Offord/produtos
  de Riesz do post de 2011 não fecha no regime da WCC, ao contrário do
  regime onde Tao a usa originalmente (lá a razão dimensão/log-módulo
  é ilimitada, aqui é fixa e pequena).

## Arquivos

- `experiment_lambda_mc.py` — script único, dois modelos, cálculo
  exato de E|Z|² e estimativa Monte Carlo de Λ com erro padrão.

## Reproduzir

```
python3 experiment_lambda_mc.py
```

Custo: ~1-2s (2×10⁶ amostras × 60 termos, vetorizado em numpy).
