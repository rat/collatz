# H-108 — Teoria de Valores Extremos confirma α=2 por um método independente do estimador de Hill

Status: confirmado — terceira confirmação independente do expoente
universal (teoria + Hill + EVT)
Criada em: 2026-07-17
Origem: sugestão #5 da terceira rodada de consulta a uma IA externa.
Motivação: como α*=2 (H-104) coloca a variância de G(v) na fronteira
da divergência, estimadores baseados em variância/segundo momento são
inerentemente problemáticos nesse regime (H-106 já mostrou ruído de
cauda pesada substancial). A Teoria de Valores Extremos (Teorema de
Fisher-Tippett-Gnedenko) usa máximos de blocos em vez de momentos —
imune a esse problema específico.

## Previsão testada

Se P(G>x) ~ C·x^{-α} (cauda regularmente variante, α=2 já confirmado
via estimador de Hill em H-104), o máximo de um bloco de tamanho n,
devidamente normalizado, converge a uma distribuição de Fréchet com
parâmetro de forma ξ=1/α=0,5. Duas consequências testáveis: (a) a
escala típica do máximo de blocos de tamanho n cresce como n^{1/α}=n^0,5
(testável via regressão log-log simples); (b) o parâmetro de forma
ajustado da distribuição GEV (Generalized Extreme Value) aos máximos
de blocos deveria ser ≈0,5.

## Resultado

`experiments/E-090-syracuse-measure-vs-density/experiment_evt_frechet.py`:
99.822 valores de G(v) (amostra global, headroom=2000), particionados
em blocos de tamanho 10 a 2000.

- **Regressão log-log** (mediana do máximo do bloco vs. tamanho do
  bloco, 8 tamanhos de bloco testados): inclinação = **0,5575**
  (previsão teórica: 0,5000).
- **Ajuste GEV** (scipy, blocos de tamanho 200, 499 blocos): parâmetro
  de forma ξ = **0,4836** (previsão teórica: 0,5000).

As duas estimativas independentes cercam o valor teórico previsto
(0,5) de perto, uma ligeiramente acima e outra ligeiramente abaixo —
consistente com ruído estatístico normal em torno do valor correto,
não com um desvio sistemático.

## Interpretação

Esta é a **terceira confirmação independente** do expoente de cauda
universal α=2: (1) derivação teórica (Fable, raiz de equação espectral
de pressão, estável em 4 níveis de refinamento); (2) estimador de Hill
(H-104, ~1,97 no topo da cauda global, 1,74-2,17 por classe); (3) agora
teoria de valores extremos (máximos de blocos, imune ao problema de
variância na fronteira α=2). Três métodos estatisticamente
independentes, calculados de formas totalmente diferentes, convergindo
para o mesmo valor — esse é o tipo de robustez que torna α=2 um
resultado sólido desta linha de investigação, provavelmente o mais
citável isoladamente se a checagem de novidade (ainda pendente)
confirmar que é inédito.

## Referências

- H-104 (derivação teórica e primeira confirmação via Hill).
- H-106 (motivação: ruído de cauda pesada nos estimadores baseados em
  variância, que a EVT contorna).
- Experimento: `experiments/E-090-syracuse-measure-vs-density/experiment_evt_frechet.py`.
