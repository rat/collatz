# E-002 — Estrutura residual em outliers de stopping time

Hipótese relacionada: [`H-002-stopping-time-outliers.md`](../../hypotheses/H-002-stopping-time-outliers.md)

## O que foi testado

Números com stopping time anormalmente alto para o tamanho ("outliers") — os top
0.5% por `total_steps(n) / log2(n)` num intervalo — foram comparados a uma amostra
típica do mesmo intervalo quanto a: (a) resíduo mod potências de 2 (4 a 64), (b)
resíduo mod potências de 3 (3 a 27), (c) comprimento da corrida inicial de passos
com valuação a_i=1 ("run1").

`total_steps` = número de passos do mapa padrão (n/2 se par, 3n+1 se ímpar) até
atingir 1, calculado de forma barata a partir da órbita acelerada.

## Resultados (n até 2.000.000, top 0.5% = ~5.000 outliers, testado com 2 seeds)

- **Resíduo mod 4/8/16/32/64**: diferença enorme e extremamente significativa
  (p < 10^-40) entre outliers e grupo típico.
- **Resíduo mod 3/9/27**: nenhuma diferença significativa em nenhuma configuração
  testada (p sempre > 0.05, mesmo sem correção para múltiplos testes).
- **Corrida inicial de a_i=1**: outliers têm em média ~1.95 passos iniciais com
  a=1, contra ~1.0 no grupo típico — quase o dobro.

## Interpretação — por que o sinal mod-2^k NÃO é uma descoberta nova

O resíduo de n módulo 2^k determina (de forma essencially determinística) os
primeiros valores da sequência de valuações a_1, a_2, ... até que a soma delas
ultrapasse k — e vice-versa. Como um outlier é, por definição, um número cuja
descida inicial é lenta (valuações pequenas por vários passos seguidos), ele
**necessariamente** cai em classes de resíduo mod 2^k específicas. Ou seja: o
teste de resíduo mod 2^k está essencialmente testando a mesma coisa que a
definição de outlier já garante — é uma tautologia codificada de outra forma, não
uma estrutura nova descoberta.

Para verificar isso, rodamos um controle: condicionar ambos os grupos ao **mesmo**
comprimento de corrida inicial (`run1` fixo em 1 ou 2), removendo a explicação
mais óbvia. Mesmo assim, mod 16/32/64 continuaram fortemente significativos
(p < 10^-13) — o que mostra que a tautologia não se limita ao "run1": residuo mod
2^k carrega informação sobre os valores *exatos* de a_2, a_3, ... (não só se são
1 ou não), e essa informação continua mecanicamente ligada ao stopping time. Ou
seja, o sinal mod-2^k é real, mas é **estrutura já conhecida e esperada** (a
própria definição de stopping time via valuações), não uma descoberta.

## Resultado genuíno: ausência de estrutura mod-3^k

O teste de resíduo mod 3/9/27 **não tem** essa relação determinística com a
sequência de valuações (o "3" em 3n+1 entra de forma distinta do "2"). A ausência
de qualquer sinal aqui — inclusive após condicionar em run1 — é um resultado
negativo genuíno: outliers de stopping time não parecem ter nenhuma assinatura
residual módulo potências de 3, na faixa e escala testadas.

## Status de H-002

**Suportada apenas na parte tautológica** (estrutura mod-2^k, já esperada pela
própria definição de stopping time) e **refutada na parte mais interessante**
(nenhuma estrutura mod-3^k detectada). Não hà evidência de assinatura estrutural
"nova" nos outliers além do que a definição de valuação já implica.

Próxima extensão possível (não prioritária agora): testar estruturas mais sutis
que não sejam redutíveis a residuo mod 2^k — por exemplo, features baseadas na
sequência completa de valuações normalizada por comprimento, ou comparação com
os recordistas reais catalogados na literatura (Roosendaal) em vez de outliers
definidos localmente na nossa amostra.
