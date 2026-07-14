# E-042 — Verificação do paper #014 (Williams, "A Coordinate System for Collatz Dynamics")

Hipótese relacionada: [`H-042-williams-coordinate-system-review.md`](../../hypotheses/H-042-williams-coordinate-system-review.md)

## O que foi testado

Paper de boa qualidade acadêmica (afiliação institucional real,
literatura extensa, declaração honesta de uso de IA, código público no
GitHub). Testamos os dois resultados centrais:

- **Teorema 3.6** (dinâmica diagonal: para n=λ·2^a·3^b−1 com a≥2, o
  próximo ímpar na trajetória é λ·2^(a−1)·3^(b+1)−1) — confirmado em
  20.000 casos aleatórios, sem exceção.
- **Teorema 4.1** (Zero-Prime Rows: linhas k≡2 mod4, k≥6, do esqueleto
  principal L₁ não contêm primos) — confirmado exaustivamente para
  k=6,10,...,58 (14 linhas, até 58 elementos cada, nenhum primo
  encontrado). Exceção k=2 confirmada (contém 3 e 5, ambos primos,
  como o próprio paper nota explicitamente). Controle: linhas fora
  desse padrão (k=7,8,9,12,15,16) contêm primos, como esperado.

## Resultado

**Ambos os teoremas confirmados sem exceção.** Ao contrário dos itens
001 e 004 (H-039, H-040), não encontramos erros neste paper.

## Reproduzir

`python3 experiment.py` (~0,2s)

## Status

Revisão concluída, sem erros encontrados — um ponto de calibração
importante para a crítica cumulativa (nem todo paper da coleção tem
problemas).
