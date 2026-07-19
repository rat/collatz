# E-086 — Separação magnitude/resíduo em D(v), testando a crítica do Fable a H-024

Hipótese relacionada: [`H-086-density-magnitude-factorization.md`](../../hypotheses/H-086-density-magnitude-factorization.md)

## O que foi feito

O modelo Fable, consultado para ideias criativas sobre H-013/H-018/
H-024, apontou que o desenho experimental de H-024 (fixar resíduo mod
3⁶, deixar magnitude variar livremente por ~860×) não separa o efeito
de magnitude do efeito de resíduo. Testamos isso diretamente: medimos
D(v) para muitos v com o mesmo resíduo mod 729, variando magnitude
livremente, e fizemos a regressão log-log.

## Resultado

D(v) ≈ C/v quase exatamente (inclinação da regressão log-log =
−0,9971, R²=0,9991). Removendo esse termo, a variância "inexplicada"
cai de ~300× (H-024 original) para ~1,26× — mais de duas ordens de
magnitude de redução. A conclusão formal de H-024 continua correta
(não existe K finito que explique D(v) sozinho), mas a magnitude do
fenômeno restante é muito mais modesta do que parecia. Ver H-086 para
a análise completa.

## Reproduzir

```
python3 experiment.py
```

Ou, para reproduzir a regressão específica citada em H-086, ver o
código inline usado na investigação (medir D(v) para v com resíduo
fixo mod 729 e magnitude log-uniforme entre 10² e 10⁷, depois regredir
log10(D) contra log10(v)).
