# H-102 — Abordagens #3 (interferência 2-ádica) e #5 (termo 1/v acumulado) testadas e descartadas

Status: ambas descartadas — sem sinal, consistente com a previsão
teórica do Fable
Criada em: 2026-07-16
Origem: sugestões #3 e #5 da lista de 5 abordagens (IA externa),
priorizadas pelo Fable como "quase grátis, prior baixo, rodar mesmo
assim como detector de bug".

## Teste #3 — interferência 2-ádica cruzada

`experiment_2adic_and_magnitude.py`: 3000 pares casados (m=17,
headroom=20000), Δ² como proxy de variância local, agrupado por
v₁ mod 2^K para K=2,3,4,5.

Resultado: razões (variância local / variância geral) ficam quase
todas entre 0,72 e 1,17 — sem padrão sistemático dependente de K ou r.
Um único grupo (r=9 mod 32, n=192) mostrou razão 2,01 — consistente com
ruído esperado dado ~30 comparações no total e a variabilidade já
estabelecida nesta escala de amostra (H-101 mostrou spread de até 3,7×
em lotes de 200 pares). **Sem dependência 2-ádica real detectada** —
confirma a previsão do argumento estrutural do Fable (a combinatória
da árvore reversa é puramente 3-ádica; v mod 2^K não entra em lugar
nenhum da recursão, só via correções O(1/v) já mostradas desprezíveis).

## Teste #5 — termo residual 1/v acumulado

Mesma amostra, particionada por magnitude de v₁ (faixa baixa: log₁₀v₁
< 13,00; faixa alta: ≥13,00). Um termo O(1/v) preveria razão de
variância baixa/alta ≫1 (proporcional ao quadrado da razão de
magnitudes entre as faixas). Resultado: razão = 1,245 — muito próxima
de 1. **Descartado com confiança**: confirma quantitativamente o
argumento do Fable de que a correção de magnitude acumulada é da ordem
10⁻⁵-10⁻⁷ dex, cinco ordens abaixo do resíduo observado (~0,1-0,2 dex).

## Avaliação

Ambos os testes são resultados negativos esperados (o Fable já havia
previsto isso pelo argumento estrutural), mas valiam a pena rodar como
checagem de bugs — nenhum bug encontrado. Restam para investigar: #2
(espectro do operador de transferência, reformulado como decomposição
hierárquica de variância por dígito) e #4 (covariável de topologia
local, reformulada como avaliação podada em profundidade >18, já que
a versão original era redundante com o próprio condicionamento em μ_M).

## Referências

- Experimento: `experiments/E-090-syracuse-measure-vs-density/experiment_2adic_and_magnitude.py`.
- H-101 (mesma infraestrutura de pares casados).
