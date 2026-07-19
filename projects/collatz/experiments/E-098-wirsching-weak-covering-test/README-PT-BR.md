# E-098 — Teste computacional direto da Weak Covering Conjecture (Wirsching 1998)

Hipótese relacionada: [`H-114-wirsching-weak-covering-computational-test.md`](../../hypotheses/H-114-wirsching-weak-covering-computational-test.md)

## O que foi feito

Primeiro teste computacional direto (até onde sabemos) da "Weak
Covering Conjecture for Mixed Power Sums" de Wirsching (1998, Cap. V),
a conjectura em aberto há ~30 anos identificada em H-112 como
estruturalmente equivalente ao "ingrediente que falta" da barreira de
endogenia (H-110/H-111). Implementa DP de bitset com rotação cíclica
para calcular, para cada ℓ, o menor j*(ℓ) tal que R_{j-1,j} (somas
mistas de potências de 2 e 3, definição exata do livro) cobre todos os
resíduos invertíveis mod 3^ℓ.

## Resultado

j*(ℓ) existe e é finito para ℓ=1 a 17 (validado exatamente contra
tabela de referência independente). Regime assintótico do excesso
e(ℓ)=j*(ℓ)-ℓ·log₄3 ainda indeterminado com 17 pontos (rejeitado apenas
o cenário mais pessimista de crescimento linear rápido). Ver H-114
para a análise completa.

## Reproduzir

```
python3 experiment_wcc.py
```
