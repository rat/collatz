# E-064 — Verificação do paper #038 (Kayadibi, "A Modular Classification of Pre-Descent Resistance in Accelerated Odd Collatz Dynamics")

Hipótese relacionada: [`H-064-kayadibi-pre-descent-resistance-review.md`](../../hypotheses/H-064-kayadibi-pre-descent-resistance-review.md)

## Paper

Kayadibi, S.Y. (2026). *A Modular Classification of Pre-Descent
Resistance in Accelerated Odd Collatz Dynamics*. SSRN 6918258. PDF
local: `literature/papers/038_Modular-Classification-Pre-Descent-Resistance.pdf`.

Predecessor mais simples do paper #015 desta coleção (mesma autora, já
revisado como H-058) — referenciado como `[11]` naquele paper.

## O que foi testado

Framework de classificação de "resistência à pré-descida" para o mapa
acelerado ímpar `T(n)=(3n+1)/2^v2(3n+1)`. Não alega provar Collatz.

1. Lemma 3.3, Proposição 3.4, Lemma 3.6, Proposição 3.8 — 4 resultados
   algébricos sobre a "espinha de resistência modular" `S_m`.
2. Reprodução computacional completa em `N=10⁷, L=5000` (idêntico ao
   maior experimento do próprio paper).
3. Os dois casos extremos citados nominalmente (maior τ, maior ρ).
4. Estatísticas módulo 64 (Seção 5.4).
5. Tabelas 2 e 3 (espinha de resistência, `m=6..15`, 40 valores).

## Resultado

**0 falhas em todas as 8 partes.** Reprodução exata e completa — a
componente computacional do paper é 100% determinística (sem
amostragem aleatória) e barata o bastante (~9s para `N=10⁷`) para
reproduzir integralmente, não só por amostragem. Todas as ~50
alegações numéricas específicas checadas batem exatamente.

## Como reproduzir

```
python3 experiment.py [N] [L]
```

Argumentos opcionais: `N` (padrão 10.000.000) e `L`, limite de passos
acelerados (padrão 5000) — usar valores menores (ex. `100000 2000`)
para um teste rápido de sanidade/performance antes da rodada completa.
Sem dependências além da stdlib. Roda em ~10s para `N=10⁷`.
