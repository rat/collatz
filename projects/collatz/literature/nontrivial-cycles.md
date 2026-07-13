# Ciclos não-triviais (a segunda metade clássica da conjectura)

## O que já é conhecido

A Conjectura de Collatz tem, na prática, duas partes: (1) toda órbita eventualmente
atinge 1 [convergência]; (2) o único ciclo é o trivial 1→4→2→1 [unicidade de ciclo].
Para inteiros **negativos**, o mapa estendido tem 3 ciclos conhecidos — o que motivou
a pergunta do diretor científico: existe um análogo positivo?

- **Steiner (1977)**: não existe ciclo de 1 elemento (1 "subida") além do trivial.
- **Simons (2005)**: não existe ciclo de 2 elementos.
- **Simons & de Weger (2005)**: estenderam a prova até k=68 — não existe ciclo
  não-trivial com até 68 "subidas" (passos ímpares).
- **Eliahou (1993)**: qualquer ciclo não-trivial hipotético tem período (comprimento
  total, incluindo divisões) de uma forma específica
  (p = 301994a + 17087915b + 85137581c, com a,b,c ≥0 inteiros, b≥1, ac=0) — o que
  implica um mínimo de 17.087.915 elementos.
- **Estado da arte (2025)**: o melhor limite inferior conhecido é 217.976.794.617
  elementos mínimos para qualquer ciclo não-trivial.

Essas provas usam aproximações por frações contínuas de log(3)/log(2) (ou
log(2)/log(3)) — a mesma ideia por trás da equação de ciclo que usamos em
`experiments/E-009-nontrivial-cycle-search/`, mas com técnicas muito mais refinadas
que busca por força bruta.

## Fontes

- [Eliahou — "The 3x+1 problem: new lower bounds on nontrivial cycle lengths"](https://www.semanticscholar.org/paper/The-3x+1-problem:-new-lower-bounds-on-nontrivial-Eliahou/74776cf36405d70c2230613bf1416ac141013599)
- [Wikipedia — Collatz conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture) (seção sobre ciclos)
