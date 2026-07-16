# H-101 — Teste decisivo de pares casados (proposto pelo Fable): resíduo continua caindo até m=29, sem platô confirmado — um "platô" inicial se desfez com mais precisão

Status: resultado negativo honesto (não confirma platô; não fecha a
questão) — inclui uma autocorreção metodológica registrada
Criada em: 2026-07-16
Origem: teste decisivo proposto pelo Fable em resposta à pergunta sobre
a extrapolação frágil de H-100. Ideia: gerar pares (v1, v2=v1+t·3^m)
que compartilham os m primeiros dígitos 3-ádicos por construção, com
v1 grande o suficiente para que a diferença de magnitude entre v1 e v2
seja desprezível (~1%). Var(log G(v2)−log G(v1))/2 estima a variância
não explicada pelos m primeiros dígitos — **sem precisar computar
μ_M nem montar arrays mod 3^m**, evitando por completo o limite de
M≤18 (risco de overflow) da abordagem anterior. Alcança profundidades
m até 29, bem além de qualquer teste anterior desta linha.

## Resultado (versão final, de alta precisão)

`experiments/E-090-syracuse-measure-vs-density/experiment_deep_pairs.py`
+ `experiment_deep_pairs_extend.py` + `experiment_deep_pairs_precision.py`
(headroom=20.000, 2.000-2.300 pares por ponto):

| m | resid_var | resid_std |
|---|---|---|
| 8 | 0,032717 | 0,1809 |
| 11 | 0,020145 | 0,1419 |
| 14 | 0,015156 | 0,1231 |
| 17 | 0,011269 | 0,1062 |
| 20 | 0,007393 | 0,0860 |
| 23 | 0,005077 | 0,0713 |
| 26 | 0,004362 | 0,0660 |
| 29 | 0,002626 | 0,0512 |

**Decaimento monotônico limpo até m=29** — sem sinal de platô. Ajuste
de 3 modelos em escala de variância (busca em grade, conforme
recomendado pelo Fable): piso+geométrico tem menor SSE (5,04×10⁻⁶),
mas zero+geométrico (6,82×10⁻⁶) e zero+lei-de-potência (8,78×10⁻⁶)
ficam próximos — com 8 pontos e um parâmetro a mais (piso), a vantagem
do modelo com piso não é estatisticamente convincente.

## Autocorreção registrada (importante para o histórico)

Uma primeira rodada com **apenas 500 pares** em m=26 e m=29 (ver
`experiment_deep_pairs_extend.py`, resultado original: var=0,003132 em
m=26, var=0,003247 em m=29 — praticamente empatados) pareceu mostrar o
primeiro sinal real de platô. **Isso se desfez** ao aumentar a amostra
para ~2.300 pares por ponto (`experiment_deep_pairs_precision.py`):
a variância batch-a-batch (lotes de 200 pares) variou por um fator de
até ~3,7× (de 0,0015 a 0,0084), revelando que 500 pares era amostra
pequena demais para essa estatística nesta escala de m — o "empate"
inicial era ruído, não sinal. Com mais precisão, m=26 (var=0,00436) e
m=29 (var=0,00263) mostram queda clara, na mesma proporção das etapas
anteriores. Registrado como lição: com poucos pares (~500) nesta
faixa de m, a estimativa de variância residual não é confiável o
suficiente para comparações ponto-a-ponto.

## Interpretação

A questão original (H-100: "há um piso real, ou converge a zero?")
**continua em aberto**, mas a evidência atual pende para "continua
caindo", não para "platô confirmado". O argumento estrutural do Fable
(a combinatória da árvore reversa é puramente 3-ádica; as únicas
entradas não-3-ádicas são o corte de headroom, já medido em
~0,0044 dex, e correções de magnitude O(1/v) de ordem 10⁻⁵-10⁻⁷ dex —
ambas muito menores que o resíduo atual) prevê que o piso teórico
deveria ser ≈ ruído de headroom (var≈0,0000194), não os ~0,0026-0,033
observados. Extrapolando a taxa geométrica média observada (razão
≈0,87-0,88 por unidade de m) até alcançar esse piso teórico, seriam
necessárias mais ~35-40 unidades de m (m≈65-70) — provavelmente
inviável computacionalmente por este método (custo por par ainda é
barato, mas 3^70 excede em muito qualquer v testável com headroom
suficiente, e a variância intrínseca do teste por par torna esse
alcance impraticável de verificar com confiança estatística).

## O que fica como conclusão honesta

Sem evidência de um platô real até m=29; a hipótese de que o resíduo
converge a zero (compatível com a existência plena do limite de escala
G, previsão do argumento estrutural do Fable) continua mais bem
sustentada pelos dados do que a hipótese de um piso positivo — mas a
questão não está fechada, e não será fechada por este método sem
recursos computacionais muito além do que é razoável investir aqui.

## Referências

- H-100 (extrapolação inicial, frágil, que motivou este teste).
- Experimentos: `experiment_deep_pairs.py`, `experiment_deep_pairs_extend.py`,
  `experiment_deep_pairs_precision.py` (todos em
  `experiments/E-090-syracuse-measure-vs-density/`).
