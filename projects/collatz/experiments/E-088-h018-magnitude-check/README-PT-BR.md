# E-088 — Testa se a obstrução de H-018 tem o mesmo confound de magnitude de H-024

Hipótese relacionada: [`H-088-h018-branch-decay-not-magnitude-confounded.md`](../../hypotheses/H-088-h018-branch-decay-not-magnitude-confounded.md)

## O que foi feito

O Fable, consultado sobre H-026, apontou uma terceira suspeita: a
"taxa de decaimento entre galhos férteis" de H-018 (73×–680×) poderia
ter o mesmo confound de magnitude que H-024/H-086 já corrigiram para
D(v) bruto. Testamos diretamente usando 18 pares de galhos já
decompostos (t=10,13,16,17): calculamos o termo trivial esperado
w_{i+3}/w_i e verificamos se ele varia (o que permitiria confusão) ou
é constante (o que não permite).

## Resultado

w_{i+3}/w_i = 64 exatamente em todos os 18 pares (consequência
algébrica de "3 posições" sempre multiplicar por 4³). Dividir por uma
constante fixa não muda a dispersão — confirmado numericamente
(desvio-padrão em log10 idêntico antes e depois, 0,5674 dex). A
suspeita do Fable não se aplica aqui: reforça a conclusão original de
H-018 em vez de exigir correção. Ver H-088 para a análise completa.

## Reproduzir

```
python3 experiment.py
```
