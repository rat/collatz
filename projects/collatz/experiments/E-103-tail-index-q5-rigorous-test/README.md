# E-103 — Teste rigoroso do índice de cauda de W_v para q=5 (Conjectura 4.x do paper)

Hipótese relacionada: [`H-109-generalized-qx1-pressure-equation-exact-closed-form.md`](../../hypotheses/H-109-generalized-qx1-pressure-equation-exact-closed-form.md)

## O que foi feito

Depois de corrigir a §3 do paper (equação de pressão anelada +
transição de congelamento) e rebaixar o índice de cauda do martingale
para q≥5 a uma Conjectura sem apoio empírico sólido (a medição
original de H-109/H-113, Hill com 600 raízes, já tinha sido sinalizada
como estatisticamente não-confirmatória), o diretor científico pediu
um teste mais robusto. Consultado o Fable para desenho estatístico —
identificou um risco específico de q=5 (transiente lento H^{-0,22} de
uma raiz complexa subdominante da equação de pressão) e recomendou uma
bateria de estimadores em vez de Hill isolado.

## Desenho

- 5000 raízes (vs. 600 antes), amostradas em faixa ampla (1001-200001).
- 4 níveis de headroom (H=10^5, 10^6, 10^7, 10^8) medidos numa ÚNICA
  passada de DFS por raiz (via checkpoints do `count_tree`, já
  validado em E-097), para checar estabilidade da estimativa conforme
  H cresce — o mesmo espírito do portão KL-vs-Volkov.
- Hill estimator em 4 frações da cauda (1%, 2%, 5%, 10%), com bootstrap
  (300 reamostragens sobre raízes) para intervalo de confiança.
- Estimador complementar independente: regressão log-log rank-size
  (tipo Zipf plot) no mesmo top-fração.

**Nota de limitação**: por falta de tempo, não implementamos a bateria
completa que o Fable recomendou como padrão-ouro (regressão
Gabaix-Ibragimov com correção rank−½, Hill com correção de viés/duplo
bootstrap, MLE de GPD com gráfico de estabilidade de limiar, e o teste
Clauset-Shalizi-Newman + Vuong contra lognormal). O que rodamos é um
Hill/Zipf mais cuidadoso que o original (amostra 8x maior, com IC via
bootstrap, em múltiplos headrooms), não a bateria completa.

## Resultado

**Estabilidade entre headrooms**: excelente — as estimativas mudam
muito pouco entre H=10^5 e H=10^8 (ex. Hill em frac=5%: 1,5803 →
1,5829 → 1,5808 → 1,5793). O transiente lento específico de q=5 que o
Fable temia não aparece como problema visível nesta faixa de headroom.

**Instabilidade clássica do Hill entre frações da cauda**: o valor
muda bastante conforme quantos pontos da cauda se usa —
frac=1%→2,10; frac=2%→1,81; frac=5%→1,58; frac=10%→1,39 (valores em
H=10^8). Na fração de 5% (a mais equilibrada, nem poucos pontos
demais nem bulk demais), o valor bate quase exatamente com o
previsto (1,536), dentro do IC bootstrap [1,4106; 1,7967]. Nas frações
extremas (1% e 10%), o IC não cobre confortavelmente o valor previsto.

**Veredito honesto**: encorajador mas não conclusivo. É uma medição
genuinamente mais forte que a original (amostra 8x maior, IC via
bootstrap, checagem de estabilidade em headroom que a original não
tinha) e não refuta a Conjectura — mas a instabilidade entre frações
mostra exatamente o tipo de fragilidade que fez o Fable recomendar uma
bateria de estimadores mais robusta. Não promovemos isso a "confirmação"
no paper — fica registrado como evidência parcial, mais forte que
antes, ainda aquém de um teste decisivo.

## Arquivos

- `experiment_tail_index_q5.py` — script único.
- `results.json` — resultados brutos (Hill/Zipf/bootstrap em cada
  combinação de headroom × fração).

## Reproduzir

```
python3 experiment_tail_index_q5.py
```

Custo: ~20 minutos (5000 raízes × 4 níveis de headroom até 10^8).

## Próximos passos (se a linha for retomada)

Implementar a bateria completa recomendada pelo Fable — em particular
o teste Clauset-Shalizi-Newman + Vuong, que é o análogo direto do
portão KL-vs-Volkov (H-113) para esta pergunta: decide de forma
pré-registrada se "power law com índice ≈1,536" é estatisticamente
defensável contra alternativas (lognormal, poder truncado).
