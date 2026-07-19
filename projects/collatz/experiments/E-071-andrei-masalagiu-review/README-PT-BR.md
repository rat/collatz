# E-071 — Revisão de Andrei & Masalagiu, "About the Collatz conjecture" (1998)

Hipótese relacionada: [`H-071-andrei-masalagiu-review.md`](../../hypotheses/H-071-andrei-masalagiu-review.md)

## O que foi feito

Verificação computacional dos resultados centrais do paper (item 101 da
coleção, `literature/papers/101_About-the-Collatz-Conjecture.pdf`):

1. Teorema 3.1 (fórmula de atalho para 2p passos consecutivos) — 458 casos, 0 falhas.
2. Lema 4.1 (família explícita simples) — 21 casos, 0 falhas.
3. Teorema 4.2 (família explícita geral) — 110 casos, 0 falhas, após
   corrigir um erro de precedência de parênteses na minha própria
   primeira tentativa de reimplementar a fórmula.
4. Teorema 3.2 parte (1) (limite inferior Racc≥1,5) — 99.998 casos, 0 falhas.
5. Teorema 3.2 parte (2) (limite superior Racc≤i) — **refutado**, 5
   contraexemplos até n=10.000.
6. Conjectura 2 (limite assintótico=3, não provada pelo paper) — testada
   até n=2^16-2^17, consistente com convergência lenta a 3.

## Resultado

Ver H-071 para o veredito completo. Resumo: paper correto e honesto na
maior parte, com um erro real contido — Teorema 3.2 parte (2) tem prova
ausente (uma frase não-demonstrada) e é refutável com contraexemplos
pequenos (menor: n=5).

## Reproduzir

```
python3 experiment.py
```

Sem argumentos de linha de comando — os limites de busca (max_p, max_t,
n_max, max_power) estão fixos no código, escolhidos para rodar em menos
de um minuto.
