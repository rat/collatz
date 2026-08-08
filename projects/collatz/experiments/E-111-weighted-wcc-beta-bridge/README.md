# E-111 — Cobertura ponderada WCC/beta=1

Hipótese relacionada:
[`H-131-wcc-ponderada-ponte-beta-one.md`](../../hypotheses/H-131-wcc-ponderada-ponte-beta-one.md).

## Pergunta

A cobertura não ponderada de Wirsching controla o menor custo geométrico
das representações da variável de Syracuse de Tao? Esse controle é o passo
necessário para justificar a implicação WCC para beta=1 usada no paper 01.

## Método

O script calcula exatamente a existência de tuplas por resíduo e custo.
Ele usa a transformação

`W_m = 2^a_m W_(m-1) + 3^(m-1)`

e converte de volta por `Syrac_n = 2^-B W_n`. Antes de produzir a tabela,
a recursão inteira é comparada com uma enumeração independente de todas as
composições do custo em quatro casos pequenos.

## Reproduzir

```bash
python3 weighted_bridge.py --max-level 12
```

## Resultado

As quatro comparações DP versus força bruta passaram sem divergência.
Para `ell=1,...,12`, o maior custo mínimo foi exatamente

`B_max(ell)=ell+j*(ell)`.

```text
ell  Bmax  j_equiv  jstar  Bmax-ell*log2(3)
  1     2        1      1            0.415037
  2     6        4      4            2.830075
  3     9        6      6            4.245112
  4    11        7      7            4.660150
  5    14        9      9            6.075187
  6    16       10     10            6.490225
  7    18       11     11            6.905262
  8    20       12     12            7.320300
  9    22       13     13            7.735337
 10    25       15     15            9.150375
 11    27       16     16            9.565412
 12    29       17     17            9.980450
```

A igualdade possui uma prova bijetiva independente do experimento,
registrada em H-131. Ela mostra que WCC, pela estratégia de escolher uma
única representação por resíduo, alcança apenas `beta<=1.130929...`, não
`beta=1`. O próximo teste deve medir a massa ponderada acumulada de todas
as representações, pois somente a multiplicidade pode suprir o expoente
que falta.

A segunda parte do script mede essa massa completa. Ela reproduz os
valores exatos `c_1=1/3` e `c_2=2/63`. Até `ell=12`, o expoente efetivo
`-log(c_ell)/(ell log 3)` cai para `1.222938`, enquanto
`3^ell*c_ell=0.052915`. O comportamento é compatível com beta=1, mas não
fornece uma implicação a partir da WCC.
