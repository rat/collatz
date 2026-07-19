# E-058 — Verificação do paper #015 (Kayadibi, "Canonical Shells and Residue-Cover Trees")

Hipótese relacionada: [`H-058-kayadibi-canonical-shells-review.md`](../../hypotheses/H-058-kayadibi-canonical-shells-review.md)

## Paper

Kayadibi, S.Y. (2026). *Canonical Shells and Residue-Cover Trees in a
Conditional First-Descent Approach to the Collatz Problem*. Victoria
University, Melbourne. PDF local:
`literature/papers/015_Canonical-Shells-Residue-Cover-Trees.pdf`.
Constrói sobre dois papers anteriores da mesma autora (um deles é o
item 038 desta coleção).

## O que foi testado

Framework condicional (reduz "primeira descida universal" a duas
condições estruturais não provadas em geral: dyadic gap + fechamento de
residue-cover trees). Verificamos tudo que o paper efetivamente PROVA
(não a parte condicional em si):

1. Persistence Identity (Lemma 3.1) + Corolário 3.2 (sem descida
   precoce) — 3120+2730 casos, contra simulação real de Collatz.
2. First-Exit Formula (Lemma 4.1) + Certified Exact Descent (Teorema
   4.5) — 1414 casos, 191 certificados, `τ(n)=m` exato confirmado.
3. Dyadic Gap Condition (Definição 5.1) — `2≤m≤20.000` com inteiros
   nativos exatos; valores da Tabela 1 do paper reproduzidos exatamente.
4. Cumulative Affine Formula (Teorema 7.3) + Residue Cylinder (Teorema
   8.2) — 2000+500 casos aleatórios.
5. Reprodução em escala menor da Tabela 2/3 (`N=10⁶`, `L=2000`) — 0
   descidas precoces, 0 casos não resolvidos.

## Resultado

**Nenhum erro encontrado.** Toda a maquinaria provada resistiu à
verificação sem exceção, incluindo reprodução exata dos valores
específicos do paper (Tabela 1: convergentes 5,41,306,15601 e seus
K_m: 8,65,485,24727). O paper é explícito (Seção 15) que NÃO prova
Collatz incondicionalmente — a parte condicional (dyadic gap global +
fechamento de árvores) permanece genuinamente aberta, e esta revisão
não tentou resolvê-la (fora de escopo).

## Como reproduzir

```
python3 experiment.py
```

Sem dependências além da stdlib. Roda em ~6s (a Parte 3, dyadic gap até
m=20.000, e a Parte 5, N=10⁶, são as mais custosas).
