# E-055 — Verificação do paper #020 (Ruiz Castillo, "Principio Variacional Residual")

## Objetivo

Verificar "Principio Variacional Residual de Ruiz Castillo y
formalismo termodinámico para la dinámica acelerada de la Conjetura de
Collatz" (Juan Carlos Ruiz Castillo, 58 páginas). Sexto paper deste
autor revisado na coleção (após item 001/H-039, item 008/H-050, item
010/H-052, item 013/H-053, item 017/H-054). Propõe unificar deuda
residual, drift residual, presión residual, entropía disipativa,
grandes desviaciones e dimensión disipativa sob um único princípio
variacional `P_RC(t) = sup_{μ∈M_RC}{H_RC(μ) − tD_RC(μ)}`. Não alega
provar Collatz.

## Caráter do paper

Majoritariamente **análise convexa abstrata** (sup de funções afins é
convexo, subgradientes, dualidade de Legendre–Fenchel) aplicada a
`P_RC(t)` e `I_RC(x)` — fatos clássicos de livro-texto, corretamente
derivados, mas sem conteúdo Collatz-específico adicional (M_RC e suas
medidas nunca são construídas explicitamente, como no item 017/H-054).

## O que fizemos

**Parte 1 — identidades Collatz-específicas concretas** (todas
confirmadas, 0 falhas):
1. Proposición 1.2 (interpretação multiplicativa da deuda residual:
   2^{L_k(n)}=3^k/2^{A_k(n)}, e critério de sinal via `Fraction` exata).
2. Proposición 2.5 / Corolario 2.6 (semiconjugação simbólica e
   invariância hacia adelante).
3. Proposición 3.3 (classificação local do potencial via a₀: a₀=1⟹φ<0,
   a₀≥2⟹φ>0).
4. Proposición 3.4 / Teorema 3.5 / Corolario 3.6 (soma ergódica e
   identidade fundamental — a mesma de sempre, verificada mais uma vez
   para este paper específico).

**Parte 2 — verificação toy (não Collatz-específica)** do aparato de
análise convexa: geramos 20 retas afins aleatórias, definimos
`P(t)=sup_i F_i(t)`, e confirmamos numericamente (200 pares
`(t1,t2,λ)`) que a desigualdade de convexidade se sustenta — confirma
que a Proposición 5.4/6.2 (sup de afins é convexo) foi corretamente
aplicada.

## Resultado

**Nenhum erro real encontrado.** Todas as identidades concretas são
reescritas triviais e corretas. O aparato de análise convexa abstrata é
matemática padrão corretamente aplicada. Onde a derivação é apenas
formal/estrutural (Proposición 8.6, dualidade presión–tasa), o próprio
texto admite isso explicitamente: *"Este razonamiento no constituye por
sí solo una demostración completa del principio de grandes desviaciones
para la dinámica determinista real de Collatz."* Todo resultado
genuinamente em aberto (Conjetura 7.6 existência de medidas de
equilíbrio, Conjetura 10.1 Triângulo Residual) é honestamente rotulado
"Conjetura", não "Teorema"/"Proposición".

Diferente do item 013 (H-053), sem inconsistências enunciado-vs-
demonstração. Volta ao padrão "elementar mas correto" da maioria dos
papers Ruiz Castillo revisados.

Ver `hypotheses/H-055-ruiz-castillo-variational-principle-review.md`.

## Como rodar

```
/home/rat/.venv/bin/python3 experiment.py
```
