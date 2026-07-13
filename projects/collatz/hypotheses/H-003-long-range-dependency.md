# H-003 — Dependência de longo alcance entre valuações (lag k > 1)

Status: refutada (não suportada — ver experimento E-003)
Criada em: 2026-07-13

## Enunciado

H-001 testou apenas a independência entre passos consecutivos (a_1, a_2), sem
rejeitá-la. Propomos estender o teste para lags maiores: existe correlação
mensurável entre a_i e a_{i+k} para k = 2, 3, 4, 5, 6? Um modelo i.i.d. correto
preveria independência em todos os lags, não só no lag 1.

## Motivação

- Testar só o lag 1 não descarta dependências de alcance maior (ex: um padrão
  que só aparece a cada 3 passos, ligado à interação entre os fatores de 2 e 3
  na aritmética 3n+1).
- Se todos os lags também não rejeitarem independência, isso fortalece
  consideravelmente a confiança no modelo i.i.d. padrão da literatura — não é
  mais só "lag 1 parece ok", é "não achamos dependência em lugar nenhum que
  procuramos".

## Como testar

Reaproveitar o desenho limpo validado em H-001 (amostras de n grandes e
distintos, sem colisão de órbitas — ver `protocols/new-experiment.md`), mas para
cada lag k usar uma amostra fresca e olhar para o par (a_1, a_{1+k}) de cada
trajetória. Testar independência via qui-quadrado e correlação de Pearson, como
em E-001.

## Atualizações

- 2026-07-13: hipótese aberta.
- 2026-07-13: testada em `experiments/E-003-long-range-dependency/` para lags
  1-6, 500.000 amostras independentes por lag. Nenhuma dependência
  estatisticamente significativa detectada em nenhum lag (todos p > 0.2).
  Colisões de órbita negligíveis mesmo no lag 6 (0.018% da amostra). Resultado
  reforça a suposição i.i.d. dos modelos estocásticos padrão para além do lag 1
  já testado em H-001. Hipótese refutada.
