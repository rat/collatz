# E-003 — Dependência de longo alcance entre valuações

Hipótese relacionada: [`H-003-long-range-dependency.md`](../../hypotheses/H-003-long-range-dependency.md)

## O que foi testado

Extensão de H-001/E-001: em vez de só o lag 1 (a_1 vs a_2), testamos lags de 1 a
6 (a_1 vs a_{1+k}), cada um com uma amostra fresca de 500.000 números ímpares
distintos e aleatórios em [10^9, 10^12] — mesmo desenho limpo validado em E-001
(sem agregação por posição-em-órbita, evitando colisão de trajetórias).

## Resultado

| lag | n_pares | colisões | Pearson r | p (corr) | qui-quadrado | dof | p (qui2) | veredito |
|---|---|---|---|---|---|---|---|---|
| 1 | 500.000 | 3  | -0.00043 | 0.763 | 35.6 | 49 | 0.924 | independência ok |
| 2 | 500.000 | 2  |  0.00004 | 0.975 | 48.7 | 49 | 0.484 | independência ok |
| 3 | 500.000 | 6  |  0.00181 | 0.201 | 50.7 | 49 | 0.407 | independência ok |
| 4 | 500.000 | 21 |  0.00006 | 0.967 | 49.9 | 49 | 0.436 | independência ok |
| 5 | 500.000 | 36 | -0.00030 | 0.834 | 26.2 | 49 | 0.997 | independência ok |
| 6 | 500.000 | 91 |  0.00024 | 0.864 | 33.5 | 49 | 0.956 | independência ok |

Reproduzir: `python3 experiment.py 500000 6`

Colisões (mesmo valor visitado por duas trajetórias diferentes) crescem com o
lag, como esperado (órbitas mais longas têm mais chance de se cruzar), mas
permanecem uma fração desprezível da amostra (máx. 91/500.000 = 0.018% no lag 6)
— não o suficiente para distorcer o resultado.

## Conclusão

Nenhuma dependência estatisticamente significativa detectada em nenhum dos 6
lags testados. Isso estende — com bastante confiança — o resultado de E-001: não
é só o lag 1 que é consistente com o modelo i.i.d., a independência se sustenta
em toda a janela de curto/médio alcance testada. Fortalece a confiança na
suposição usada pelos modelos estocásticos padrão (Kontorovich–Lagarias).

## Status de H-003

Hipótese (existe dependência de longo alcance) **não suportada** — resultado
consistente com independência em todos os lags testados.
