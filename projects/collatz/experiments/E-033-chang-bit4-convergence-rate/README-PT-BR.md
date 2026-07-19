# E-033 — Extensão do problema aberto de Chang (2026) com órbitas mais longas

Hipótese relacionada: [`H-033-chang-bit4-longorbit-extension.md`](../../hypotheses/H-033-chang-bit4-longorbit-extension.md)

## O que foi testado

O paper de Chang (H-030) deixa aberto: toda órbita visita 9 e 25 (mod 32)
com equilíbrio suficiente ao longo do fim-de-burst no canal ≡1 mod8? Ele
testou até n0=10⁹ com poucas dezenas de observações por órbita. Aqui
rastreamos o equilíbrio individualmente ao longo dos 8 maiores
recordistas reais (878-920 passos, 131-134 observações cada — 3× mais
que o melhor caso do paper original).

## Resultado

Desvio persiste (0,54-0,64, não 0,5), sem sinal de convergência mesmo com
mais dados. Consistente com H-021/H-030 (recordistas têm runs de subida
mais longos por seleção) e com o próprio reconhecimento do Chang de que
órbitas individuais desviam ±10-25%. Não resolve nem contradiz o
problema aberto dele — δ_max exato não foi derivado aqui.

Reproduzir: `python3 experiment.py`.

## Status de H-033

**Confirmada** como extensão empírica honesta — dado novo e maior escala,
sem superclaim sobre o problema aberto original.
