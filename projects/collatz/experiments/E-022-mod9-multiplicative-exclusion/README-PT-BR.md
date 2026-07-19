# E-022 — Prova parcial de H-008 via relação multiplicativa (2 passos)

Hipótese relacionada: [`H-022-mod9-multiplicative-exclusion.md`](../../hypotheses/H-022-mod9-multiplicative-exclusion.md)

## O que foi testado

Depois de H-015/H-016 falharem (buscavam M=N−k, deslocamento aditivo, que
nunca poderia isolar mod 9), tentamos uma construção **multiplicativa**:
M tal que 2 passos acelerados a partir de M levam exatamente a N. Resolvendo
a congruência para N≡4 (mod 9), achamos a solução mais simples: valuações
(a,b)=(1,2), dando M=(8N−5)/9.

## Resultado

Para N=18j+13 (a metade **ímpar** de N≡4 mod9), M=16j+11 satisfaz M<N
sempre, e a cadeia M→M₁→N (2 passos acelerados, valuações exatas 1 e 2)
vale para todo j — **verificado sem exceção para j=0 a 100.000** (N até
~1.8 milhões).

Confirmado que 0 dos 148 recordistas oficiais são ≡13 mod18 (consistente
com a prova) e também 0 são ≡4 mod18 (a metade par, ainda não provada).

**Novidade confirmada**: de 1000 casos testados, 750 (75%) não eram já
cobertos por H-007 (mod3=2) nem H-014 (mod8=5) — não é uma redescoberta
disfarçada.

Reproduzir: `python3 experiment.py 100000`.

## O que falta

A metade **par** de N≡4 mod9 (N≡4 mod18) não pode ser excluída pela mesma
técnica — passos acelerados só alcançam números ímpares, então N par nunca
é o "alvo" direto de uma cadeia a partir de outro M. Precisaria de um
argumento diferente. Fica como questão em aberto (mas empiricamente também
nunca observada nos 148 recordistas reais).

## Status de H-022

**Confirmada** (metade ímpar de H-008 provada rigorosamente). H-008 (a
questão original completa) fica **parcialmente resolvida**: metade
provada, metade (par) ainda em aberto.
