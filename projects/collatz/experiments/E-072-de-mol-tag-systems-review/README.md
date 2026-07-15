# E-072 — Revisão de De Mol, "Tag systems and Collatz-like functions" (2008)

Hipótese relacionada: [`H-072-de-mol-tag-systems-review.md`](../../hypotheses/H-072-de-mol-tag-systems-review.md)

## O que foi feito

Implementamos literalmente o sistema de tag T_C do Teorema 2.1 do paper
(item 102, `literature/papers/102_Tag-Systems-and-Collatz-Like-Functions.pdf`)
— μ=3 símbolos {α,c,y}, shift v=2, regras α→cy, c→α, y→ααα — e verificamos
que ele simula corretamente a função acelerada de Collatz C'(2m)=m,
C'(2m+1)=3m+2.

## Resultado

Confirmado sem exceção: 200 casos diretos (n=1 a 200), 4 trajetórias
iteradas completas (sementes 7, 27, 97, 871, até convergirem a {1,2,4}),
e o exemplo introdutório do próprio paper (período 6). Ver H-072 para o
veredito completo. Paper não faz nenhuma alegação sobre a Conjectura de
Collatz em si — é um resultado de teoria da computabilidade sobre
sistemas de tag, usando Collatz como caso de estudo.

## Nota de performance

Implementação inicial usava concatenação de string (O(n) por passo);
para n grandes isso deu O(n²) total e estourou timeout. Reimplementado
com `collections.deque` (O(1) por passo) — ver `experiment.py`.

## Reproduzir

```
python3 experiment.py
```
