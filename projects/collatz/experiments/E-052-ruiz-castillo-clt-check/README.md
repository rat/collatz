# E-052 — Verificação do paper #010 (Ruiz Castillo, "Teorema Central del Límite Residual")

## Objetivo

Verificar "Teorema Central del Límite Residual de Ruiz Castillo para la
dinámica acelerada de la Conjetura de Collatz" (Juan Carlos Ruiz
Castillo, 29 páginas). Terceiro paper deste autor revisado na coleção
(o primeiro foi item 001/H-039, o segundo item 008/H-050). Propõe um
Teorema Central do Limite para as flutuações da "deuda residual"
L_k(n) = k·log₂(3) − A_k(n) — a mesma quantidade elementar de sempre
(drift logarítmico padrão), agora sob a lente de convergência em
distribuição.

**Achado central da leitura**: o resultado principal é formalmente
rotulado "Conjetura 4.2" (não "Teorema") no CORPO do paper, apesar do
TÍTULO dizer "Teorema" — o próprio autor lista honestamente 5 hipóteses
não estabelecidas (existência de medida de Gibbs residual,
ergodicidade, espaço funcional adequado, brecha espectral do operador
de transferência residual, variância residual positiva) das quais o
resultado depende, e nunca as prova ou constrói. A conclusão do próprio
paper diz explicitamente: "Este marco no demuestra la Conjetura de
Collatz."

## O que fizemos

**Parte 1 — identidades algébricas provadas no corpo do paper**
(elementares, corretas): Teorema 2.3 (L_k(n) = −S_k(φ), reescrita
direta da definição) e Proposición 2.5 (Var(L_k)=Var(−S_k φ), trivial)
— testados em 27 valores de n × 5 valores de k, 0 falhas.

**Parte 2 — consequência empírica testável da "Conjetura 4.2"**: como
as hipóteses técnicas da conjectura (medida de Gibbs residual, brecha
espectral) nunca são construídas no paper, testamos diretamente a
PREVISÃO observável — normalidade assintótica de
Z_k = (L_k(n) − k·m_RC)/√k, com m_RC = log₂(3)−2 — em trajetórias REAIS
de Collatz (não um modelo i.i.d. abstrato), para k = 5, 20, 50, 100, 300.

## Nota de integridade: bug de amostragem corrigido antes de reportar

A primeira versão amostrava n uniformemente em `range(3, 10**15, 2)`
para todo k, exigindo (via `require_no_fixed_point=True`) que a
trajetória não atingisse o ponto fixo n=1 antes de completar k passos.
O comprimento médio de uma trajetória Syracuse para n de ~50 bits é
log₂(n)/(2−log₂3) ≈ 120 passos; para k=300 (~4,9 desvios-padrão acima
da média) a taxa de rejeição ficava tão próxima de 100% que o loop de
retry nunca completava — o processo em background ficou preso por 17
minutos sem progredir. Corrigido escalando a faixa de amostragem com
k: o número de bits de n é escolhido de modo que o comprimento
ESPERADO da trajetória seja ~3k+50, garantindo alta taxa de aceitação
mesmo para k=300 (rodagem completa em ~5 segundos após a correção).
Foi adicionado também um teto de tentativas (`max_attempts`) que
levanta erro explícito em vez de rodar indefinidamente, caso a taxa de
rejeição volte a ser inesperadamente alta no futuro.

## Resultado

**Nenhum erro matemático real encontrado.** Parte 1 confirma as
identidades algébricas (reescritas triviais de definições). Parte 2
mostra que os momentos empíricos de Z_k convergem exatamente como uma
gaussiana padrão preveria conforme k cresce:

| k   | média Z_k | var Z_k | assimetria | curtose |
|-----|-----------|---------|------------|---------|
| 5   | -0,0201   | 2,0163  | -0,9590    | 4,3795  |
| 20  | 0,0037    | 1,9703  | -0,4592    | 3,3472  |
| 50  | 0,0081    | 1,9882  | -0,2916    | 3,1821  |
| 100 | 0,0070    | 1,9680  | -0,2366    | 3,0770  |
| 300 | -0,0031   | 1,9832  | -0,1002    | 2,9843  |

Variância estabiliza perto de 2 (= σ²_RC = Var(a_j), já estabelecido em
H-001/H-011), assimetria → 0 e curtose → 3 conforme k cresce — ou seja,
a PREVISÃO da conjectura é **empiricamente plausível em dados reais**,
mesmo que as hipóteses técnicas que a sustentariam nunca sejam
construídas ou provadas neste paper. Esta é a primeira verificação
numérica real desta previsão (o próprio paper não contém nenhuma).

**Rotulagem "Teorema" vs. "Conjetura"**: consistente com o padrão de
honestidade parcial já visto nos outros papers Ruiz Castillo revisados
(H-039, H-050) — corretude elementar no que é de fato provado, sem
verificação numérica própria, mas o autor é honesto ao rotular o
resultado central como conjectural no corpo do texto.

**Padrão de citação**: ~20 referências, todas autocitações do próprio
Ruiz Castillo — confirma o padrão já visto em H-039/H-050 de aplicar,
um de cada vez, um conceito clássico diferente (drift, pressão, cotas,
dimensão, entropia, medidas de Gibbs, princípio variacional, operador
de transferência, teoria espectral, TCL, grandes desvios) à MESMA
quantidade L_k(n).

Ver `hypotheses/H-052-ruiz-castillo-clt-review.md`.

## Como rodar

```
/home/rat/.venv/bin/python3 experiment.py
```
