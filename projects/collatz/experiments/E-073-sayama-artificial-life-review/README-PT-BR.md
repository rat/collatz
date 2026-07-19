# E-073 — Revisão de Sayama, "An Artificial Life View of the Collatz Problem" (2011)

Hipótese relacionada: [`H-073-sayama-artificial-life-review.md`](../../hypotheses/H-073-sayama-artificial-life-review.md)

## O que foi feito

Verificamos as duas fórmulas centrais do paper (item 103): taxa de
crescimento L_app=log₂3≈1,585 bits/passo (Eq.5) e taxa de extinção
R_app=2 bits/passo (Eq.6), para a dinâmica acelerada sem divisão
x_{t+1}=3x_t+LSNB(x_t).

## Achado interessante durante a verificação

Medir L sobre uma trajetória longa deu ~2,0 em vez de ~1,585 — pareceu
uma discrepância real. Investigação mostrou que potências de 2 são
estado absorvente exato dessa dinâmica (3·2^k+2^k=2^(k+2)), e 200/200
amostras aleatórias atingem uma potência de 2 em ≤500 passos. Medindo
só a fase ativa (antes de atingir a potência de 2), a taxa bate com
log₂3 dentro de <0,5%. **Não é um erro do paper** — o texto já reconhece
esse caso extremo explicitamente logo após a Eq.5.

## Resultado

Ambas as fórmulas centrais confirmadas. Ver H-073 para o veredito
completo e a discussão sobre o que esse estado absorvente implica para
o alcance da "explicação ecológica" proposta pelo paper.

## Reproduzir

```
python3 experiment.py
```
