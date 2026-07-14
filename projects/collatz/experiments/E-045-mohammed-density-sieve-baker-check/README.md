# E-045 — Verificação do paper #011 (Abdullah Mohammed) — alegação de prova completa

## Objetivo

Verificar "Structural Analysis, Dynamic Density Sieve, and Logarithmic
Contraction of Collatz Sequences" (Abdullah Mohammed, Kafr El-Sheikh
University, Egito) — alega prova completa da Conjectura de Collatz via
sieve de densidade geométrica + Teorema de Baker (formas lineares em
logaritmos).

## Resultado

**Seções 2-5 corretas** (mas não-novas): sieve geométrico P(M=m)=1/2^m,
E[M]=2 (nosso próprio H-001/H-011), exclusão elementar de 1-ciclos
(n=1/(2^m-3), única solução positiva é m=2,n=1), sequência de "special
numbers" 1,5,21,85,341,... (OEIS A002450, números que atingem 1 em um
passo).

**Furo decisivo na Seção 7.1 (Eq.48)**: para usar o Teorema de Baker e
excluir ciclos não-triviais, é preciso comparar o limite inferior de
Baker contra o valor de M/P que um ciclo REAL forçaria. A própria Seção
6 do paper deriva a equação de ciclo 2^M=∏(3+1/n_i), que força M/P →
log₂(3)≈1,585 para elementos grandes (provado aqui elementarmente: para
qualquer P≥2, 3^P < ∏(3+1/n_i) < 4^P, logo M∈(P·log₂3, 2P) estritamente
— nunca igual a 2P). Mas a Eq.48 substitui M≈2P — a expectativa
ERGODICA/MÉDIA E[M]=2 da Seção 3, que descreve o número ímpar
TÍPICO/ALEATÓRIO, não a restrição que um ciclo autoconsistente
específico precisaria satisfazer. Essa substituição errada produz
Λ≈0,288·P (cresce linearmente, confirmado bate exatamente com o número
do paper), que trivialmente satisfaz o limite fraco de Baker — a
"checagem" não restringe nada. A comparação que importaria (Λ→0 quando
M/P→log₂3) é exatamente onde estaria a dificuldade genuína.

Este é o mesmo método usado de verdade por Simons & de Weger (2005) com
constantes de Baker explícitas para excluir ciclos até certos
comprimentos — mas não "todos os ciclos" em geral, porque não fecha
para P arbitrariamente grande com as constantes efetivas conhecidas.
O paper de Mohammed nem chega a esse nível (não computa C, κ
explicitamente) e ainda usa a substituição errada.

Ver `hypotheses/H-045-mohammed-density-sieve-baker-flaw.md`.

## Como rodar

```
/home/rat/.venv/bin/python3 experiment.py
```
