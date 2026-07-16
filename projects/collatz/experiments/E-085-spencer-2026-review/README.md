# E-085 — Revisão de Spencer, "Rooted Surjectivity from the Invariant E/O Refinement System" (2026)

Hipótese relacionada: [`H-085-spencer-2026-review.md`](../../hypotheses/H-085-spencer-2026-review.md)

**ALEGAÇÃO DE PROVA COMPLETA — veredito diferenciado (não confirmada, não refutada computacionalmente).**

## O que foi feito

Mesmo autor do item 022 (já refutado com contraexemplo em H-081) —
suspeita inicial era a mesma anatomia de erro ("classe residual
ocupada" ≠ "inteiro específico atingido"). Construímos a árvore reversa
real a partir de n=1 (grau infinito: múltiplos k admissíveis por nó,
diferente da árvore de grau≤2 do item 022) e testamos cobertura de
inteiros ímpares pequenos com orçamento computacional crescente.

## O que encontramos (diferente da suspeita inicial)

Cobertura completa até 10.000 com orçamento adequado; os "faltantes"
em rodadas com orçamento menor **convergem exatamente à raiz** quando
seguidos sem limite de magnitude (confirmado individualmente para
vários valores) — isso é o oposto do comportamento visto no item 022,
onde o gap persistia e crescia independente do orçamento.

**Mas** identificamos uma lacuna de rigor genuína na demonstração
escrita: o Teorema 14.1 argumenta sobre ocupação de *classes*
residuais, e o Teorema 14.2 conclui algo mais forte sobre *elementos
individuais* — essa passagem não é justificada explicitamente no texto.

## Resultado

Veredito honesto: a demonstração como escrita tem uma lacuna lógica
real (não é uma prova válida como está), mas a evidência computacional
disponível é consistente com a conclusão do paper, ao contrário do
item 022 do mesmo autor. Ver H-085 para a análise completa, incluindo
a autocorreção da suspeita inicial baseada em precedente.

## Reproduzir

```
python3 experiment.py
```
