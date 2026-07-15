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
- **Hercher (2023, arXiv:2201.00406)**: estende a exclusão de Simons & de Weger
  para k≤91 — não existe ciclo não-trivial com até 91 "subidas" (bound ATUAL
  para este parâmetro, verificado via WebSearch/WebFetch em 2026-07-14, ver
  `hypotheses/H-057-continued-fraction-cycle-exclusion.md`). **Não confundir
  com o "estado da arte" abaixo** — são parâmetros diferentes: k/a aqui é o
  número de passos ímpares (subidas), o "estado da arte" abaixo é o
  comprimento TOTAL do ciclo (incluindo divisões), uma quantidade bem maior.
- **Eliahou (1993)**: qualquer ciclo não-trivial hipotético tem período (comprimento
  total, incluindo divisões) de uma forma específica
  (p = 301994a + 17087915b + 85137581c, com a,b,c ≥0 inteiros, b≥1, ac=0) — o que
  implica um mínimo de 17.087.915 elementos.
- **Estado da arte (2025)**: o melhor limite inferior conhecido é 217.976.794.617
  elementos mínimos para qualquer ciclo não-trivial (comprimento total, não o
  mesmo parâmetro k/a de Simons & de Weger/Hercher acima — não re-verificado
  nesta sessão).

Essas provas usam aproximações por frações contínuas de log(3)/log(2) (ou
log(2)/log(3)) — a mesma ideia por trás da equação de ciclo que usamos em
`experiments/E-009-nontrivial-cycle-search/`, mas com técnicas muito mais refinadas
que busca por força bruta. Testamos essa conexão diretamente em H-057/E-057
(convergentes + semiconvergentes de log₂(3), aplicados ao nosso próprio muro
combinatório de H-009/H-034) — nenhum ciclo novo, resultado consistente.

## Fontes

- [Eliahou — "The 3x+1 problem: new lower bounds on nontrivial cycle lengths"](https://www.semanticscholar.org/paper/The-3x+1-problem:-new-lower-bounds-on-nontrivial-Eliahou/74776cf36405d70c2230613bf1416ac141013599)
- [Hercher (2023) — arXiv:2201.00406](https://arxiv.org/abs/2201.00406)
- [Wikipedia — Collatz conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture) (seção sobre ciclos)
