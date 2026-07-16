# H-103 — Abordagem #2 (reformulada): taxa de decaimento da variância residual é só modestamente heterogênea entre classes grosseiras (mod 9)

Status: testado, resultado modesto/inconclusivo — não confirma nem
refuta fortemente o mecanismo de mistura de taxas
Criada em: 2026-07-16
Origem: sugestão #2 (espectro do operador de transferência), reformulada
pelo Fable como decomposição hierárquica de variância por dígito,
estratificada por classe grosseira, para evitar as armadilhas sérias
do PCA cru (inflação Marchenko-Pastur com poucas amostras por classe).

## Teste

`experiment_stratified_variance.py`: para cada uma das 6 classes
não-estéreis de v₁ mod 9 (1,2,4,5,7,8), gerados pares casados
(v₁,v₂) com v₁ restrito àquela classe, em dois níveis de profundidade
(m=11 e m=23, 400 pares cada), comparando a razão var(m=23)/var(m=11)
por classe — se essa razão (a taxa de decaimento) variar muito entre
classes, confirma heterogeneidade real de taxa (mecanismo sugerido
pelo achado de Jensen de H-099, onde o termo de Jensen variou ~46×
entre classes finas mod 3⁸).

## Resultado

| classe (mod 9) | var(m=11) | var(m=23) | razão |
|---|---|---|---|
| 1 | 0,01962 | 0,00588 | 0,300 |
| 2 | 0,02142 | 0,00424 | 0,198 |
| 4 | 0,02562 | 0,00711 | 0,278 |
| 5 | 0,02112 | 0,00638 | 0,302 |
| 7 | 0,02282 | 0,00666 | 0,292 |
| 8 | 0,02470 | 0,00891 | 0,361 |

Razão média = 0,288, desvio-padrão = 0,048 (coeficiente de variação
~17%). As razões variam por um fator de ~1,8× entre os extremos
(0,198 a 0,361) — uma dispersão real mas **modesta**, bem menor que o
fator de ~46× encontrado no termo de Jensen (H-099, medido em classes
muito mais finas, mod 3⁸=6561).

## Interpretação

A heterogeneidade de taxas entre classes existe mas não é dramática
já no nível grosseiro (mod 9, os 2 primeiros dígitos 3-ádicos) — a
variação de ~1,8× aqui é bem menor que a de ~46× vista no gap de
Jensen. Isso sugere que a heterogeneidade principal encontrada em
H-099 se concentra em escalas 3-ádicas **mais finas** (dígitos mais
profundos) do que mod 9, não já visível neste nível de agregação.
Não é um resultado que feche a questão — apenas mostra que a
estratificação grosseira usada aqui não é fina o suficiente para
capturar o grosso da heterogeneidade de taxa. Uma estratificação mais
fina (mod 27 ou mod 81) poderia revelar mais, mas o custo computacional
cresce (menos pares por classe disponíveis a amostra fixa).

## Referências

- H-099 (achado de Jensen, heterogeneidade ~46× em classes finas).
- H-101 (infraestrutura de pares casados reutilizada aqui).
- Experimento: `experiments/E-090-syracuse-measure-vs-density/experiment_stratified_variance.py`.
