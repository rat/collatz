# H-107 — ANOVA aninhada em blocos densos confirma, de forma independente e com precisão muito maior, a curva de decaimento de H-101

Status: confirmado — validação cruzada bem-sucedida entre dois métodos
completamente diferentes
Criada em: 2026-07-16
Origem: "Ideia B" da segunda rodada de sugestões externas (espectro via
"Transformada de Chrestenson"), reformulada pelo Fable como ANOVA
aninhada (matematicamente equivalente à transformada, mas mais fácil
de auditar e permite excluir classes estéreis), com a correção de viés
de amostra finita (Bessel, ddof=1) que ele identificou como obrigatória.

## Método

`experiments/E-090-syracuse-measure-vs-density/experiment_nested_anova.py`:
para cada bloco denso de 3¹¹=177.147 inteiros ímpares consecutivos
(v_j=v₀+2j, cobrindo cada resíduo mod 3^t exatamente uma vez para
qualquer t≤11, já que 2 é invertível mod 3^t), computa G(v) para TODOS
os pontos (não amostragem esparsa), exclui os ~1/3 estéreis (v≡0 mod3),
e decompõe a variância de log G por profundidade t=1..7 (parado em
M−4=7 por segurança contra o viés de amostra pequena, conforme
recomendado pelo Fable). Rodado em 2 blocos independentes, em
magnitudes de v bem diferentes (v₀~10¹¹ e v₀~5×10¹¹), para checar
consistência.

## Resultado — consistência notável entre blocos

| t | var (bloco 1) | var (bloco 2) | diferença |
|---|---|---|---|
| 1 | 0,21302 | 0,21337 | 0,17% |
| 2 | 0,12360 | 0,12397 | 0,30% |
| 3 | 0,08782 | 0,08827 | 0,52% |
| 4 | 0,06829 | 0,06885 | 0,81% |
| 5 | 0,05584 | 0,05633 | 0,88% |
| 6 | 0,04682 | 0,04718 | 0,78% |
| 7 | 0,03975 | 0,04000 | 0,62% |

(valores em dex², já convertidos de log natural via divisão por
(ln 10)²≈5,302)

**Diferença menor que 1% em todos os pontos**, apesar dos dois blocos
estarem em magnitudes de v cerca de 5× diferentes — confirma
diretamente (mais uma vez, de forma independente) que não há
dependência relevante de magnitude no resíduo (reforça H-102, que já
havia descartado o termo O(1/v) via outro método).

## Comparação com H-101 (pares casados)

Em profundidade comparável (t=7, ANOVA, ~0,0398 dex² médio) contra
m=8 (pares casados, H-101, 0,032717 dex²) — a ANOVA (que condiciona
1 dígito a menos) dá um resíduo um pouco MAIOR, na direção certa
(menos condicionamento ⟹ mais variância residual). Os dois métodos,
completamente independentes (enumeração exaustiva de bloco denso vs.
amostragem de pares esparsos em profundidades muito maiores),
**concordam dentro do esperado**.

## Interpretação

Esta é a validação cruzada mais forte desta linha de investigação: dois
métodos matematicamente distintos (um exaustivo/determinístico dentro
do bloco, outro por amostragem aleatória de pares) dão resultados
consistentes tanto em escala quanto em tendência (decaimento suave, sem
platô na faixa t=1-7, mesmo padrão qualitativo que os pares casados
mostraram até m=29). A precisão da ANOVA em blocos densos (diferença
<1% entre blocos de magnitude muito diferente) é ordens de grandeza
melhor que a precisão alcançável por amostragem de pares nesta mesma
faixa de profundidade — mas o método não escala para profundidades
maiores (um bloco de 3^29 seria computacionalmente impossível), então
os pares casados continuam sendo o único método viável para sondar
profundidades m>~12-14.

## Referências

- H-101 (pares casados, m até 29 — comparação direta).
- H-102 (termo 1/v já descartado por outro método — reforçado aqui).
- Experimento: `experiments/E-090-syracuse-measure-vs-density/experiment_nested_anova.py`.
