# E-067 — Verificação do paper #074 (Carelli, "Loop Termination and Generalized Collatz Sequences")

Hipótese relacionada: [`H-067-carelli-loop-termination-review.md`](../../hypotheses/H-067-carelli-loop-termination-review.md)

## Paper

Carelli, M. (2026). *Loop Termination and Generalized Collatz
Sequences*. arXiv:2605.15094 [cs.LO]. CISPA Helmholtz Center. PDF
local: `literature/papers/073_Loop-Termination-Generalized-Collatz.pdf`.

Paper de ciência da computação teórica (decidibilidade de terminação
de loops lineares). Não tenta resolver a conjectura clássica —
"Collatz generalizado" é uma família mais ampla da qual o Collatz
clássico é um caso particular (d=2, m=3).

## O que foi testado (escopo limitado ao conteúdo Collatz-relevante)

1. Mecanismo algébrico da Proposição 17 (ponto fixo por classe residual).
2. Teste empírico do conteúdo prático da Proposição 17 (~20.000 trajetórias).
3. Exemplo 19 — questão explicitamente ABERTA no paper, testada até n=2.000.000.
4. Teorema 14 (cota de ciclo ≤2 para SLCs 1D) — checagem pontual.
5. Proposição 11 (construção combinatória) — checagem pontual.

## Resultado

**0 falhas.** Nenhum erro encontrado no conteúdo relacionado a
sequências de Collatz generalizadas. A maquinaria de geometria
computacional mais ampla (Minkowski-Weyl, Lemas 21/23/24/25) fica fora
do escopo desta revisão — é sobre SLCs em geral, não sobre Collatz.

## Como reproduzir

```
python3 experiment.py
```

Sem dependências além da stdlib (scipy não disponível neste ambiente;
a Parte 5 usa um fallback combinatório sem LP). Roda em alguns segundos.
