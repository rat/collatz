# E-039 — Cálculo explícito da pressão residual de Ruiz Castillo (item 001)

Hipótese relacionada: [`H-039-ruiz-castillo-geometria-residual-review.md`](../../hypotheses/H-039-ruiz-castillo-geometria-residual-review.md)

## O que foi testado

O paper #001 da coleção (`literature/papers/INDEX.md`) define uma
"pressão residual" P_RC(t) para o observável de dissipação
φ(a)=a-log₂(3), mas nunca a calcula explicitamente — toda a análise
fica em nível de "SE P_RC for convexa, ENTÃO g_RC(t)≥0" etc. Este
experimento calcula P_RC(t), g_RC(t) e K_RC(t) explicitamente para o
modelo i.i.d. padrão (a ~ Geométrica(1/2), já estabelecido em
H-001/H-011 deste projeto).

## Resultado

- Λ(t) [≡P_RC(t) até convenção de sinal] tem forma fechada:
  `t(1-log₂3) - log(2-eᵗ)`, domínio t<log(2).
- Verificação cruzada: Λ'(0)=2-log₂3≈0,415 e Λ''(0)=2 batem
  exatamente com E[a]-log₂3 e Var[a]=2, já estabelecidos.
- g_RC(t)=2eᵗ/(2-eᵗ)² — estritamente positiva/convexa em todo o
  domínio (confirma, para o modelo i.i.d., a hipótese que o paper só
  assume formalmente).
- **Singularidade real**: g_RC(t)→∞ quando t→log(2)⁻ — a métrica
  diverge exatamente no ponto onde a FGM da geométrica deixa de
  convergir (consequência direta do "2" na Geométrica(1/2)).
- K_RC(t) = -2·g_RC(t) exatamente (relação fechada específica deste
  modelo) — sempre estritamente negativa, nunca zero, diferente do
  desenho conceitual em U do próprio paper (que é explicitamente
  ilustrativo, não computado).

## Reproduzir

`python3 experiment.py`

## Status

Cálculo de apoio para H-039 — não é uma hipótese testada isoladamente
sobre a conjectura, é uma extensão computacional honesta de um paper
externo revisado, feita para preencher a lacuna que o próprio paper
deixa (nunca calcula nada explicitamente para o problema real).
