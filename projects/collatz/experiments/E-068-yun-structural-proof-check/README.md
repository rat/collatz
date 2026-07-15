# E-068 — Verificação do paper #076 (Yun, "A Structural Proof of the Collatz Conjecture") — ALEGAÇÃO DE PROVA

Hipótese relacionada: [`H-068-yun-structural-proof-review.md`](../../hypotheses/H-068-yun-structural-proof-review.md)

## Paper

Yun, Y.H. (2026). *A Structural Proof of the Collatz Conjecture via
non-repeating trajectory and Recursive Decay*. osf.io (não
peer-reviewed). PDF local:
`literature/papers/075_Structural-Proof-Collatz-nonrepeating.pdf`.

## Veredito

**NÃO é uma prova válida** — mais fraco que o item 049 (Boyle, H-065).
Contém três argumentos circulares independentes:

1. **Gap mais grave** (Seção 8): a "função de posto"
   `r(x):=min{n : f^(n)(x)=1}` só está definida para `x` cuja órbita
   já atinge 1 — presume a própria conclusão. Demonstrado por
   analogia com um mapa que provadamente diverge (`g(x)=2x`), cuja
   "função de posto" análoga também fica indefinida.
2. Teorema 6.1: "o único ponto fixo conhecido é 1" — apresenta a
   conclusão (ausência de outros ciclos) como premissa.
3. Seção 5/9.2.3: falácia sobre cardinalidades infinitas
   (não-injetividade não implica convergência dinâmica).

Erro aritmético concreto também encontrado (Equação 9.8): `f(5)` e
`f(21)` calculados com expoentes de 2 errados, chegando a um
resultado (2) que nem é ímpar.

## O que foi testado

1. Lema 6.1 (distinção de vizinhos) — correto.
2. Erro aritmético na Equação 9.8 — confirmado.
3. Contraexemplo de método para a função de posto (Parte 3).
4. Busca computacional por ciclos não-triviais até 2 milhões — nenhum
   encontrado (não prova a ausência, só não a contradiz).

## Como reproduzir

```
python3 experiment.py
```

Sem dependências além da stdlib. Roda em alguns segundos.
