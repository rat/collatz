# E-066 — Verificação do paper #057/089 (Reyes Jiménez, "A Fibonacci theorem for Collatz trajectories via modular graph structure")

Hipótese relacionada: [`H-066-reyes-jimenez-fibonacci-review.md`](../../hypotheses/H-066-reyes-jimenez-fibonacci-review.md)

## Paper

Reyes Jiménez, M-A. (2026). *A Fibonacci theorem for Collatz
trajectories via modular graph structure*. arXiv:2606.02621 [math.NT].
PDF local: `literature/papers/056_Fibonacci-theorem-Collatz-modular-graph.pdf`.

Pesquisa matemática genuína e tecnicamente sofisticada (não uma
tentativa amadora de resolver a conjectura). Item 089 é duplicata
confirmada.

## O que foi testado

11 partes, cobrindo toda a estrutura do paper:

1. Lemma 2.1 (resíduo corretivo) + Exemplo 2.2.
2. Proposição 2.3 (bijetividade/periodicidade).
3. Lemmas 2.4-2.5 (antissimetria/translação).
4. Proposição 2.8 (transição mod 6 — já verificada em H-027).
5. Proposições 3.1/3.3 (SCCs e ciclos simples do grafo).
6. Cinco raios espectrais (Proposições 3.4, 4.10, 4.11, 4.13, Teorema 4.15).
7. Corolário 4.5 (confinamento a {1,2,4,5}).
8. **Teorema 4.7 (resultado principal)**: contagem de Fibonacci exata.
9. Exemplo 4.8.
10. Teorema 4.1 + Corolário 4.4 (teorema do caminho modular).
11. Proposição 4.18/Corolário 4.19 (distribuição em ciclos positivos).

## Resultado

**0 falhas em todas as 11 partes.** A contagem de Fibonacci (Teorema
4.7) foi reproduzida por força bruta exatamente para m=1 a 22
(F(2)=1 até F(23)=28.657). Nenhum erro matemático encontrado — o
paper de maior rigor técnico revisado nesta sessão.

Dois bugs foram encontrados e corrigidos no PRÓPRIO script de
verificação (não no paper): uma comparação de ciclos sem normalização
de rotação consistente (Parte 5), e um erro de indexação off-by-one
ao extrair (h₂,h₃,h₄) (Parte 9) — ver H-066 para detalhes.

## Como reproduzir

```
python3 experiment.py
```

Requer `numpy` (para autovalores na Parte 6; sem numpy, essa parte é
pulada e não conta como falha). Roda em alguns segundos.
