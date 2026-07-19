# E-054 — Verificação do paper #017 (Ruiz Castillo, "Medidas de Gibbs Residuales")

## Objetivo

Verificar "Medidas de Gibbs Residuales de Ruiz Castillo y estados de
equilibrio en la dinámica acelerada de la Conjetura de Collatz" (Juan
Carlos Ruiz Castillo, 62 páginas). Quinto paper deste autor revisado
na coleção (após item 001/H-039, item 008/H-050, item 010/H-052, item
013/H-053). Introduz "Medidas de Gibbs Residuales" atribuindo pesos
termodinâmicos aos cilindros realizáveis via
`μ_t([ω]_C) ≍ exp(tL(ω) − kP_RC(t))`, usando a mesma identidade
fundamental `S_k(φ)(ω) = −L(ω)` de sempre.

## O que fizemos

Verificamos computacionalmente todas as proposições/teoremas/corolários
concretos e verificáveis:

1. **Proposición 1.1** (U(n) bem definido, ímpar→ímpar): confirmada.
2. **Proposición 1.3** (interpretação logarítmica L_k=log₂(3^k/2^Ak))
   e **Corolario 1.4** (L_k<0 ⟺ 2^Ak>3^k, via `Fraction` exata para
   evitar falsos positivos de ponto flutuante perto do limiar — lição
   já aplicada em H-050/E-050): confirmadas.
3. **Teorema 3.6 / Proposición 1.5** (identidade fundamental
   S_k(φ)(ω)=−L(ω)): confirmada — 39×5 casos, 0 falhas.
4. **Proposición 2.6** (semiconjugação simbólica π(U(n))=σ(π(n))):
   confirmada.
5. **Proposición 2.11/2.13** (partição por cilindros realizáveis):
   confirmada (checagem finita, sem ambiguidade).
6. **Proposición 9.1** (equivalência Gibbs-residual, identidade
   pontual de eventos): confirmada.

## Resultado

**Nenhum erro real encontrado** — ao contrário do item 013 (H-053, que
continha a Proposición 5.3 **falsa**, contradita pela própria
demonstração), este paper volta ao padrão "elementar mas correto" de
H-039/H-050/H-052. Toda derivação concreta é correta (reescrita
algébrica trivial da mesma identidade fundamental de sempre), e todo
resultado genuinamente em aberto é honestamente rotulado **"Conjetura"**,
não "Teorema" ou "Proposición":

- Conjetura 7.3 (propriedade cuasi-Bernoulli residual)
- Conjetura 8.4 (Gibbs implica equilíbrio residual)
- Conjetura 9.3 (dualidade Gibbs–grandes desviaciones)
- Conjetura 10.4 (fórmula de dimensão Gibbs residual)

**Sem consequência empírica diretamente testável** (diferente do item
010/H-052): as conjecturas deste paper tratam da **existência** de uma
família de medidas μ_t nunca construída explicitamente — diferente do
operador de transferência do item 013, que tinha fórmula fechada sobre
o espaço irrestrito e permitia teste numérico direto. Não há
estatística computável em trajetórias reais para testar diretamente
estas conjecturas de existência, então não escrevemos uma "Parte 2"
empírica para este paper.

**Nota estilística (não é erro)**: Proposición 4.4 ("interpretación
normalizadora") é argumentada de forma retórica/informal, sem cota
quantitativa efetivamente verificável — mas, diferente da Proposición
5.3 do item 013, não faz nenhuma afirmação numérica concreta que seja
falsa.

Ver `hypotheses/H-054-ruiz-castillo-gibbs-measures-review.md`.

## Como rodar

```
/home/rat/.venv/bin/python3 experiment.py
```
