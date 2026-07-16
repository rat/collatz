# H-100 — Teste de refinamento em altíssima precisão (N=30.000, headroom=1.000.000×, M até 18): resid_std continua caindo mas desacelera, extrapolação sugere piso não-zero (~0,04 dex)

Status: resultado observacional, extrapolação preliminar **refutada** —
ver H-101 (teste decisivo proposto pelo Fable, pares casados até
m=29): a extrapolação para piso~0,042 dex era estatisticamente frágil
(criticado pelo Fable) e os dados de H-101, com muito mais
profundidade e precisão, mostram queda contínua sem platô confirmado
até m=29 — mais compatível com convergência a zero do que com um piso
real.
Criada em: 2026-07-16
Origem: versão "recursos não são problema" do teste de refinamento de
H-091 Parte 2, rodada pausada e retomada nesta sessão
(`experiments/E-090-syracuse-measure-vs-density/experiment_refinement_deep.py`).
10× mais amostras (29.943 v's vs. 2.997) e 10× mais headroom (1.000.000×
vs. 100.000×) que o teste anterior, M estendido até 18 (vs. 14) via
`syrac_fast.py` (versão vetorizada numpy).

## Resultado

Teste B (convergência pareada por-v, headroom crescente até 1.000.000×,
4.997 v's): desvio de Δ(v) entre níveis sucessivos de headroom
continua encolhendo geometricamente até o nível mais alto testado:

| H1→H2 | desvio(Δ) dex |
|---|---|
| 200→2000 | 0,0596 |
| 2000→20000 | 0,0245 |
| 20000→100000 | 0,0102 |
| 100000→1.000.000 | 0,0044 |

Confirma e fortalece a evidência de existência do limite de escala (E)
já reportada em H-091 Parte 2.

Teste A (refinamento por-v, headroom=1.000.000×, 29.943 v's, M=4 a 18):

| M | b | resid_std | corr |
|---|---|---|---|
| 4 | 0,948 | 0,265 | 0,837 |
| 8 | 0,972 | 0,187 | 0,922 |
| 12 | 0,982 | 0,141 | 0,957 |
| 16 | 0,988 | 0,111 | 0,973 |
| 18 | 0,989 | 0,099 | 0,979 |

resid_std continua caindo suavemente até M=18 (sem platô visível), mas
o **incremento por unidade de M desacelera** de forma consistente: de
−0,0135 (M=8→9) para −0,0057 (M=17→18), com razão geométrica média
entre incrementos sucessivos de ≈0,91 (ruidosa: variando 0,84–1,04
entre passos individuais).

## Extrapolação (preliminar, não confirmada)

Assumindo que os incrementos de resid_std decaem geometricamente com
razão ≈0,91 indefinidamente, a soma da série residual dá um piso
estimado de **resid_std → ≈0,042 dex** conforme M→∞ (não zero).

**Esta extrapolação é frágil**: baseada em só 10 pontos de incremento,
com razões individuais bastante ruidosas (uma delas até >1). Não é
evidência forte de um piso real — é uma hipótese de trabalho a favor
de "há um componente genuíno não explicado por μ", mas não descarta
que o resíduo continue caindo (mais devagar) rumo a zero em M ainda
maior, que não testamos (M=19+ arrisca overflow de int64 na
implementação vetorizada atual e custo de memória/tempo crescente:
M=18 já levou ~5 min só para construir μ).

## Próximos passos (ver STATE.md)

Investigar, com as 5 abordagens sugeridas por uma IA externa consultada
sobre este exato problema (análise multifractal, espectro do operador
de transferência, interferência 2-ádica cruzada, covariável de
topologia local, termo residual 1/v), se alguma delas explica a origem
do resíduo de ~0,04-0,10 dex que sobra mesmo em M=18/headroom=1M — ou
se aponta para uma extrapolação mais confiável de para onde ele tende.

## Referências

- H-091 (Partes 1 e 2) — testes anteriores desta linha, amostra e
  headroom menores.
- Experimento: `experiments/E-090-syracuse-measure-vs-density/experiment_refinement_deep.py`.
