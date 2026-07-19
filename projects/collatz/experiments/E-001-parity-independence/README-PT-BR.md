# E-001 — Independência entre valuações 2-ádicas consecutivas

Hipótese relacionada: [`H-001-parity-independence.md`](../../hypotheses/H-001-parity-independence.md)

## O que foi testado

Se a_i (valuação 2-ádica de 3n+1 na órbita acelerada) e a_{i+1} (a valuação do
passo seguinte) são estatisticamente independentes, como os modelos estocásticos
padrão da literatura assumem.

## Tentativa 1 — `experiment.py` (com falha metodológica identificada)

Agregou pares (a_i, a_{i+1}) de **todas as posições de todas as órbitas** para os
primeiros N números ímpares. Resultado inicial: qui-quadrado enorme, aparentando
forte dependência.

**Problema descoberto**: órbitas de Collatz colidem — uma vez que duas
trajetórias diferentes atingem o mesmo valor intermediário, toda a cauda seguinte
é idêntica entre elas. Agregar por posição-em-órbita conta o mesmo trecho de
caminho múltiplas vezes, violando a suposição de amostras independentes
(pseudo-replicação). Um filtro simples por "n mínimo" (para excluir a cauda final
universal ...→8→4→2→1) reduziu mas não eliminou o efeito — colisões acontecem bem
antes da cauda final, sempre que órbitas distintas convergem para o mesmo valor.

**Esse problema em si é um achado útil**: qualquer experimento futuro que agregue
estatísticas ao longo de múltiplas órbitas precisa considerar colisão de órbitas
como fonte de pseudo-replicação. Ver nota adicionada em `protocols/new-experiment.md`.

## Tentativa 2 — `experiment_v2_clean.py` (desenho corrigido)

Amostra K números ímpares **distintos e aleatórios** num intervalo grande
(10^9–10^12), olhando apenas para os 2 primeiros passos (a_1, a_2) de cada um.
Com números iniciais grandes e espalhados, a chance de duas trajetórias colidirem
em 1-2 passos é desprezível — cada par é uma observação genuinamente independente
(confirmado: 0 colisões em m1 detectadas em ambas as rodadas).

### Resultados

| K (amostras) | seed | Pearson r | p (Pearson) | qui-quadrado | dof | p (qui-quadrado) |
|---|---|---|---|---|---|---|
| 300.000 | 42 | -0.00376 | 0.039 | 42.0 | 49 | 0.75 |
| 1.000.000 | 7 | -0.00035 | 0.72 | 39.5 | 49 | 0.83 |

Reproduzir: `python3 experiment_v2_clean.py 1000000 1000000000000 7`

## Conclusão

Com o desenho experimental correto (sem pseudo-replicação por colisão de órbitas),
**a independência entre a_1 e a_2 não é rejeitada** — os dados são consistentes com
o modelo i.i.d. usado pela literatura estocástica padrão. O sinal de "dependência"
da Tentativa 1 era um artefato metodológico, não um fenômeno real.

Isso é consistente com o teorema clássico de equidistribuição de Terras (1976) /
Everett (1977), que já estabelece formalmente que blocos finitos da sequência de
paridade são equidistribuídos conforme n varia — ou seja, este experimento
**reproduz empiricamente um resultado já conhecido**, em vez de descobrir algo
novo. Valor do exercício: validar nossa própria metodologia (e a armadilha de
colisão de órbitas) antes de tentar algo mais original.

## Status de H-001

**Refutada** (na forma testada aqui — independência simples de 2 passos, n grande).
Não suportada pelos dados. Extensão natural (dependência de longo alcance, ou
efeitos condicionados a estrutura residual) fica registrada como possível
próximo passo, mas não é prioridade imediata dado que o caso simples já é
conhecido/confirmado.
