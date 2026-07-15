# E-083 — Revisão de Wang, "Non-Existence of Collatz m-Cycles for m≤95" (2026)

Hipótese relacionada: [`H-083-wang-2026-review.md`](../../hypotheses/H-083-wang-2026-review.md)

## O que foi feito

Não alega prova completa — exclui ciclos não-triviais específicos
(m≤95), estilo Simons–de Weger/Hercher (mesmo território de H-057
deste projeto). Verificamos as identidades algébricas centrais
verificáveis sem reproduzir o aparato computacional pesado do autor:
Lemma 1 (transição de mínimo local), Lemma 3 (estimativa elementar
T(n)<3/n), Lemma 9 (monotonicidade de expoentes de sufixo), e a
aritmética do Lemma 13 (U(49)<7×10¹¹).

## Resultado

Tudo confirmado sem exceção. Os valores numéricos específicos da
Tabela do Lemma 12 e as buscas finitas para m=92-95 não foram
reproduzidos (exigiriam replicar o "affine a-ladder" completo). Ver
H-083 para o veredito completo.

## Reproduzir

```
python3 experiment.py
```
