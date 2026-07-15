# H-064 — Revisão do paper #038 (Kayadibi, "A Modular Classification of Pre-Descent Resistance in Accelerated Odd Collatz Dynamics") — reprodução exata em larga escala, sem erros

Status: revisão externa concluída — 4 lemas/proposições algébricos e a
reprodução computacional completa em N=10⁷ confirmados exatamente,
0 falhas
Criada em: 2026-07-15
Origem: item 038 da coleção (`literature/papers/INDEX.md`), já baixado
(`038_Modular-Classification-Pre-Descent-Resistance.pdf`).

## O paper

Kayadibi, S.Y. (2026), *A Modular Classification of Pre-Descent
Resistance in Accelerated Odd Collatz Dynamics*, SSRN 6918258 (working
paper). Victoria University, Melbourne, Austrália. Código-fonte público
em `github.com/seymus1/collatz-pre-descent-resistance`.

Este é o predecessor mais simples referenciado como `[11]` pelo item
015 desta mesma coleção (Kayadibi, "Canonical Shells and Residue-Cover
Trees in a Conditional First-Descent Approach to the Collatz Problem",
já revisado como [[H-058-kayadibi-canonical-shells-review]]) — mesma
autora, framework mais elementar: aqui não há "canonical shells",
"dyadic gap condition" nem "residue-cover trees"; apenas a "espinha de
resistência modular" `S_m = {n : n≡-1 mod 2^m}`, que o paper #015 usa
como um dos blocos de construção do seu framework condicional mais
elaborado.

Paper **explicitamente não tenta provar Collatz**, em múltiplos pontos:
*"the aim of this work is not to prove the classical Collatz
conjecture"*; *"these computations do not prove the Collatz
conjecture"*; *"the framework does not resolve the Collatz
conjecture."*

## Definições exatas do paper

```
T(n) = (3n+1)/2^v2(3n+1)                  -- mapa acelerado ímpar
τ(n) = min{r≥1 : T^r(n) < n}                -- tempo de primeira descida
M(n) = max(n, T(n), ..., T^τ(n)(n))         -- valor máximo de pré-descida
ρ(n) = M(n)/n                               -- razão de pico relativa
R_k = {n : τ(n)=k}                          -- classes de resistência
S_m = {n : n ≡ -1 (mod 2^m)}                -- espinha de resistência modular
```

## O que foi verificado

`experiments/E-064-kayadibi-pre-descent-resistance-check/experiment.py`,
oito partes, **0 falhas**:

1. **Lemma 3.3** (`v₂(3n+1)=1` para `n∈S_m`, `m≥2`) — 3.582 casos
   (`m=2..19`, `q=1..199`), confirmado.
2. **Proposição 3.4** (`T(n)>n` para `n∈S_m`) — mesmos 3.582 casos,
   confirmado.
3. **Lemma 3.6** (persistência: `T^j(n)=3^j·2^(m-j)·q-1` e
   `T^j(n)≡-1 mod 2^(m-j)`, `0≤j≤m-1`) — 5.096 casos, confirmado.
4. **Proposição 3.8** (`τ(n)≥m` para `n∈S_m`, quando `τ(n)` existe) —
   637 casos, confirmado.
5. **Reprodução computacional completa em N=10⁷, L=5000** (idêntico ao
   maior experimento do próprio paper): 4.999.999 descidas, 0 casos
   não-resolvidos — bate exatamente. Rodou em ~9 segundos (a "espinha"
   `S_m` tem só `~N/2^m` elementos, então as Tabelas 2/3 foram
   computadas iterando diretamente sobre essas classes, não sobre todo
   o intervalo).
6. **Os dois casos extremos citados nominalmente**: maior `τ` observado
   em `n=8.088.063` (`τ=155, M=5.385.051.557, ρ=665,8024`) e maior `ρ`
   observado em `n=6.631.675` (`τ=140, M=20.114.203.639.877,
   ρ=3.033.050,2686`) — ambos batem exatamente, tanto como argmax do
   varredura completa quanto por checagem direta desses dois números.
7. **Estatísticas módulo 64** (Seção 5.4): classe `n≡63 (mod 64)`
   (`count=156.250, τ̄=15,5684, max τ=155, ρ̄=82,3772,
   max ρ=2.396.483,7836`) e as duas classes vizinhas citadas
   (`n≡27`: `τ̄=10,5626`; `n≡31`: `τ̄=10,5617`) — todas batem
   exatamente.
8. **Tabelas 2 e 3** (estatísticas da espinha `S_m` para `m=6,...,15`
   em `N=10⁷`: contagem, `τ̄`, excesso `E_m=τ̄-m`, e `ρ̄` médio) — as
   **10 linhas × 4 valores = 40 números** batem exatamente (4 casas
   decimais) contra os valores impressos no paper.

## Resultado

**Reprodução exata e completa.** Diferente de várias outras revisões
desta coleção que precisaram escopar partes do paper como "não
verificável nesta sessão" (amostragem aleatória sem semente, computação
recorde inviável, etc.), aqui **toda alegação numérica específica do
paper foi reproduzida byte-a-byte** — os quatro resultados algébricos
provados são determinísticos (sem parâmetro livre a mais que `m,q`), e
a componente computacional é 100% determinística (sem amostragem
aleatória, sem semente necessária) e barata o bastante (`N=10⁷` em
~9 segundos) para reproduzir integralmente, não apenas por amostragem.

## Por que isso é uma revisão positiva

Framework simples e honesto: define um objeto bem delimitado (a
"espinha de resistência modular"), prova 4 fatos algébricos corretos
sobre ele (valuation, expansão de primeiro passo, persistência,
cota inferior determinística), e reporta uma classificação empírica
em larga escala sem alegar mais do que os dados mostram — inclusive
notando explicitamente que a monotonicidade observada em `τ̄` ao longo
da espinha é "uma observação de amostra finita, não um teorema
assintótico" (Remark 3.10, Discussão). Nenhum erro matemático ou
numérico encontrado.

## Novas hipóteses?

Nenhuma concreta. A "espinha de resistência modular" `S_m` é
literalmente as mesmas classes residuais já centrais em vários outros
papers desta coleção sob nomes diferentes (ex.: os "canonical shells"
`S°_m` de H-058 usam exatamente `v₂(n+1)=m`, a mesma quantidade). O
achado quantitativo mais interessante — que `τ̄` cresce monotonicamente
ao longo da espinha refinada (`m=6→15`) na faixa testada — é consistente
com o padrão geral já observado neste projeto de que subclasses residuais
"resistentes" tendem a concentrar comportamento extremo (ver também a
nota de clustering em H-062).

## Atualizações

- 2026-07-15: paper lido por completo (25 páginas), 8 partes verificadas
  computacionalmente incluindo reprodução exata em N=10⁷ (matching o
  maior experimento do próprio paper). `INDEX.md` atualizado (item 038:
  Lido=Sim, Corrigido=Sim [nada a corrigir], Implementado=Sim).
