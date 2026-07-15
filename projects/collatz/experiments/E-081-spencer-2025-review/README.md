# E-081 — Revisão de Spencer, "Finite Block Exhaustion and Rooted Occupancy..." (2025)

Hipótese relacionada: [`H-081-spencer-2025-review.md`](../../hypotheses/H-081-spencer-2025-review.md)

**ALEGAÇÃO DE PROVA COMPLETA — REFUTADA.**

## O que foi feito

Constrói a mesma árvore reversa de H-018/E-018, com aparato combinatório
sofisticado (contador ternário de classes residuais mod 2·3^J). Alega
provar que toda classe residual primitiva está "ocupada" em cada escala
finita, e conclui (Teorema 15.3) que todo inteiro ímpar tem endereço
reverso finito.

## O furo lógico

"Classe residual ocupada" (afirmação sobre resíduos, objetos abstratos)
não implica "inteiro específico atingido" — o paper nunca conecta as
duas coisas. Confirmamos isso concretamente: construímos a árvore real
até profundidade 6 e 8 e mostramos que a classe residual de 27 está
ocupada, mas por representantes muito maiores (ordem de 10⁶-10⁸),
nunca 27 em si.

## Resultado

Não é uma prova válida — mesma anatomia de erro do item 109
(Getachew/H-079), por um caminho diferente. Ver H-081 para a análise
completa.

## Reproduzir

```
python3 experiment.py
```
