# H-140: auditoria da alegada refutação L2

Status: fechada-confirmada; sobrealegação removida

Criada: 2026-08-07

## Achado

O paper concluía `K_infinity=infinity` a partir de valores exatos apenas
para `ell=1,...,17`, cujos incrementos pareciam aproximar `0.47`.
Comportamento em um conjunto finito de níveis não prova divergência.

H-138 identifica

```text
K_ell = E_Haar[M_ell^2].
```

Como `M_ell` é martingale, `K_ell` é não decrescente. Isso ainda não
exclui convergência para um valor finito depois dos níveis calculados.

## Correção

O antigo teorema foi convertido em resultado empírico de nível finito.
A recursão exata e sua validação permanecem. Foram removidas as frases
que tratavam L2 como refutado, o corolário de “escada de flatness” e as
consequências que usavam `K_infinity=infinity` como fato.

## Estado matemático

`K_infinity<infinity` continua sendo uma condição suficiente aberta.
O crescimento quase linear até `17` é evidência contra ela. A cauda
crítica prevista em O7 explicaria crescimento limítrofe, mas essa cauda
também permanece conjectural.

