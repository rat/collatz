# E-087 — Continuidade 3-ádica de G(v)=D(v)·v

Hipótese relacionada: [`H-087-3adic-continuity-of-residual.md`](../../hypotheses/H-087-3adic-continuity-of-residual.md)

## O que foi feito

Continuação de H-086 (que mostrou que a maior parte da variação de
D(v) encontrada em H-024 era o termo trivial D(v)~C/v). Testamos se o
resíduo G(v)=D(v)·v tem continuidade 3-ádica: fixando progressivamente
mais dígitos base-3 de v (resíduo mod 3^K crescente, K=1 a 8, em
cadeias nested) e deixando a magnitude variar livremente, medimos se a
variância de log10(G(v)) cai com K. Repetido com 5 cadeias de resíduo
independentes para não confiar numa única coincidência.

## Resultado

Variância cai monotonicamente e de forma consistente nas 5 cadeias —
mais de 4× de redução do desvio-padrão entre K=1 e K=8. Diferente de
D(v) bruto (H-024, onde nenhum K reduzia a variância), G(v) mostra
continuidade 3-ádica real. Sinal verde qualificado para investir nas
ideias de expansão de Mahler ou medida de Syracuse em ℤ₃ propostas
pelo Fable. Ver H-087 para a análise completa e as ressalvas sobre
força da evidência.

## Reproduzir

```
python3 experiment.py
```
