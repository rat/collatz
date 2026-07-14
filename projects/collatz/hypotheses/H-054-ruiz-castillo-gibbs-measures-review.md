# H-054 — Revisão do paper #017 (Ruiz Castillo, "Medidas de Gibbs Residuales") — sem erros, volta ao padrão elementar mas correto

Status: revisão externa concluída — matematicamente correto em tudo
verificado; todo resultado aberto honestamente rotulado "Conjetura"
Criada em: 2026-07-14
Origem: paper baixado manualmente pelo diretor científico (item 017 da
coleção, `literature/papers/017_Medidas-Gibbs-Residuales-Ruiz-Castillo.pdf`,
Juan Carlos Ruiz Castillo, 62 páginas).

## O paper

"Medidas de Gibbs Residuales de Ruiz Castillo y estados de equilibrio
en la dinámica acelerada de la Conjetura de Collatz" — quinto paper
deste autor revisado na coleção (após item 001/H-039, item 008/H-050,
item 010/H-052, item 013/H-053). Introduz "Medidas de Gibbs
Residuales" como extensão do Principio Variacional Residual, atribuindo
pesos termodinâmicos aos cilindros realizáveis via a condição
`μ_t([ω]_C) ≍ exp(−tS_k(φ)(ω) − kP_RC(t))`, reescrita — usando a
mesma identidade fundamental `S_k(φ)(ω) = −L(ω)` de sempre — como
`μ_t([ω]_C) ≍ exp(tL(ω) − kP_RC(t))`. Não alega provar Collatz:
"El marco desarrollado no demuestra la Conjetura de Collatz."

## O que foi verificado (todos confirmados)

- **Proposición 1.1** (U(n) bem definido, ímpar→ímpar).
- **Proposición 1.3** (interpretação logarítmica L_k=log₂(3^k/2^Ak)) e
  **Corolario 1.4** (L_k<0 ⟺ 2^Ak>3^k, via `Fraction` exata).
- **Teorema 3.6 / Proposición 1.5** (identidade fundamental
  S_k(φ)(ω)=−L(ω)) — 39×5 casos, 0 falhas.
- **Proposición 2.6** (semiconjugação simbólica π(U(n))=σ(π(n))).
- **Proposición 2.11/2.13** (partição por cilindros de comprimento
  fixo, e por cilindros realizáveis).
- **Proposición 9.1** (equivalência Gibbs-residual: identidade
  pontual entre os eventos {L_k/k≥x} e {S_k(φ)/k≤−x}).

Ver `experiments/E-054-ruiz-castillo-gibbs-measures-check/`.

## Volta ao padrão elementar-mas-correto (contraste com H-053)

Diferente do item 013 (H-053, que continha a Proposición 5.3 **falsa**,
contradita pela própria demonstração), este paper **não contém nenhum
erro real**. Toda derivação concreta é uma reescrita algébrica trivial
da mesma identidade fundamental já vista em H-039, H-050, H-052 (e, sob
notação diferente, em Fu-Liu-Wang/H-044 e Mohammed/H-045). Todo
resultado genuinamente em aberto é honestamente rotulado "Conjetura",
nunca "Teorema" ou "Proposición":

- Conjetura 7.3 (propriedade cuasi-Bernoulli residual)
- Conjetura 8.4 (Gibbs implica equilíbrio residual)
- Conjetura 9.3 (dualidade Gibbs–grandes desviaciones)
- Conjetura 10.4 (fórmula de dimensão Gibbs residual)

## Sem consequência empírica diretamente testável (contraste com H-052)

Diferente do item 010 (H-052, cujo TCL tinha uma previsão diretamente
simulável — normalidade assintótica de Z_k — testada em trajetórias
reais), as conjecturas deste paper tratam da **existência** de uma
família de medidas μ_t nunca construída explicitamente. Diferente do
operador de transferência do item 013 (que tinha fórmula fechada sobre
o espaço irrestrito, permitindo teste numérico direto), aqui não há
estatística computável em trajetórias reais que sirva de teste direto
para essas conjecturas de existência. Por isso não escrevemos uma
"Parte 2" empírica para este paper — a verificação se limitou às
identidades algébricas concretas (Parte 1), todas confirmadas.

## Nota estilística (não é erro)

Proposición 4.4 ("interpretación normalizadora") é argumentada de
forma retórica/informal, sem cota quantitativa efetivamente
verificável — mas, diferente da Proposición 5.3 do item 013, não faz
nenhuma afirmação numérica concreta que seja falsa, então não se
qualifica como erro, apenas como um estilo menos rigoroso que o resto
do paper.

## Novas hipóteses?

Nenhuma. Mesmo mecanismo central (identidade de drift/deuda residual)
já conhecido nosso; as conjecturas de existência de medidas de Gibbs
não sugerem uma nova linha de investigação própria sobre Collatz.

## Atualizações

- 2026-07-14: paper lido por completo (62 páginas), identidades e
  proposições concretas verificadas computacionalmente
  (`experiments/E-054-ruiz-castillo-gibbs-measures-check/`), nenhum
  erro real encontrado. Flags atualizadas em
  `literature/papers/INDEX.md` (item 017: Lido=Sim, Corrigido=Sim
  [nada a corrigir no paper], Implementado=Sim).
