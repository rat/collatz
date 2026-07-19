# E-060 — Verificação do conteúdo Collatz-específico do paper #028 (Csikos, "DAG-ness")

Hipótese relacionada: [`H-060-csikos-dag-ness-review.md`](../../hypotheses/H-060-csikos-dag-ness-review.md)

## Paper

Csikos, E. (2026). *A Continuous Multi-Component Measure of Directed
Acyclicity (DAG-ness)*. arXiv:2606.22205, 22 páginas. **Paper de teoria
de grafos, não de Collatz** — Collatz aparece só na Seção 5.2 (meia
página) como um exemplo ilustrativo. PDF local:
`literature/papers/027_Continuous-Multi-Component-Measure-DAG-ness.pdf`.

## O que foi testado (escopo limitado ao conteúdo Collatz-específico)

1. Restringindo o mapa padrão de Collatz aos primeiros 2228 inteiros
   positivos: existe exatamente um SCC cíclico (`{1,2,4}`), todo
   `n=1..2228` o atinge.
2. Direção do ciclo, conferida contra as arestas reais do mapa `T(n)`
   definido no próprio paper.
3. Aritmética do Composite Score `D(G)=0.875` (Tabela 1).

## Resultado

Conteúdo Collatz-específico correto, exceto: o paper descreve o ciclo
como "1→2→4→1", mas pelas arestas reais de `T(n)` (`T(1)=4, T(4)=2,
T(2)=1`) o ciclo correto é **1→4→2→1**. Não afeta nenhum resultado
numérico (`A`,`F`,`M`,`S`,`D` não dependem da ordem textual). Erro de
descrição, não de cálculo. O restante do paper (Seções 2-4, framework
geral de teoria de grafos) está fora do escopo desta revisão — não é
específico de Collatz.

## Como reproduzir

```
python3 experiment.py
```

Sem dependências além da stdlib. Roda em <1s.
