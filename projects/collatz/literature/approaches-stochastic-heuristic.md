# Heurísticas estocásticas e passeio aleatório

## A heurística clássica

log(órbita) se comporta como um passeio aleatório: cada passo ímpar multiplica por
~3 e divide por 2 (fator log(3/2) > 0 mas ocorre com "peso" menor), cada passo par
divide por 2 (fator log(1/2) < 0). Assumindo passos ímpar/par como se fossem
50/50 aleatórios, a deriva esperada é negativa (log(3)/2 + log(1)/2 = log(3/2) ≈ 0.20
vs. o fator real considerando frequência — o ponto chave é que a esperança do log é
negativa), o que sugere, por "ruína do apostador", que a órbita tende a cair. Isso é
heurística, não prova: o mapa é determinístico, não literalmente aleatório.

## Trabalho sistemático — Kontorovich & Lagarias

Estudaram sistematicamente modelos aleatórios para os problemas 3x+1 e 5x+1,
mostrando que a iteração pode ser aproximada por passeios aleatórios aditivos,
passeios aleatórios enviesados (biased) ou processos de Markov. Referência central
citada na literatura de heurísticas probabilísticas do problema.

## Refinamentos recentes

- [Barghout (2019) — On the Probabilistic Proof of the Convergence of the Collatz
  Conjecture](https://onlinelibrary.wiley.com/doi/10.1155/2019/6814378) — argumento
  probabilístico de convergência (não uma prova no sentido determinístico rigoroso;
  ver ressalva de `unverified-proof-claims.md`).
- [Emergence of Gamma-Type Upward-Phase Statistics in the Collatz Map (2026)
  ](https://arxiv.org/html/2606.26811) — refina a heurística de passeio aleatório
  com um mecanismo de processo de Poisson efetivo para as fases de subida.
- Tao também explorou essa direção via teoria de Littlewood-Offord:
  [The Collatz conjecture, Littlewood-Offord theory, and powers of 2 and
  3](https://terrytao.wordpress.com/2011/08/25/the-collatz-conjecture-littlewood-offord-theory-and-powers-of-2-and-3/)

## Limitação conhecida

Toda essa família de argumentos explica **por que esperamos** que a conjectura seja
verdadeira (deriva negativa esperada), mas heurística probabilística sobre um
processo determinístico não é prova — não descarta trajetórias específicas
excepcionais nem ciclos alternativos. É o mesmo obstáculo estrutural de sempre.
