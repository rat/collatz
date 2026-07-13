# Correção — a anomalia p₅>p₄ não é um efeito simples de "mod 3 de J_t"

## O que eu disse antes (e estava incompleto)

Ao registrar a anomalia p₅>p₄ em H-013, especulei que poderia estar "ligada
ao resíduo mod 3 de cada J_t" — sugerindo que talvez a classe J_t≡2 (mod 3)
capturasse sistematicamente mais densidade que a classe adjacente J_{t-1}≡1
(mod 3). Isso era baseado em amostragem aleatória com poucos dados nas
classes raras (t≥10).

## O que a varredura exaustiva mostrou

Rodando `experiment_exhaustive.py` (não amostragem — contagem exata de
TODOS os n ímpares até 80 milhões), a razão entre pares adjacentes
(t com J_t≡1 mod3, t+1 com J_{t+1}≡2 mod3):

| par | razão (contagem t+1 / contagem t) |
|---|---|
| t=4 vs t=5 | 1.594 |
| t=7 vs t=8 | 5.972 |
| t=10 vs t=11 | **0.072** |
| t=13 vs t=14 | **0.200** |

**A razão cresce nos dois primeiros pares e depois inverte** — t=10 tem
~14× mais ocorrências que t=11, e t=13 tem 5× mais que t=14. Isso contradiz
diretamente a hipótese de que "mod3=2 sempre domina mod3=1 adjacente".

## Conclusão honesta

A anomalia é **real** (confirmada, não é ruído de amostragem — verificada
com contagem exata em duas escalas, 20M e 80M) mas **não tem uma explicação
simples via resíduo mod 3 de J_t**. O comportamento é não-monotônico e mais
complexo do que a primeira hipótese sugeria. Continua genuinamente em
aberto — provavelmente requer uma análise mais sofisticada da estrutura de
ramificação da árvore reversa de Collatz (algo no estilo de processos de
ramificação/Galton-Watson), que não tentamos ainda.

Retiro a especulação anterior. A pergunta certa agora é: **por que a razão
entre classes adjacentes oscila em vez de seguir um padrão simples?**
