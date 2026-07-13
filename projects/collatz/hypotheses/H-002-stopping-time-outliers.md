# H-002 — Estrutura residual em outliers de stopping time

Status: parcialmente refutada (ver experimento E-002 — sinal real é tautológico, sem estrutura mod-3 nova)
Criada em: 2026-07-13

## Enunciado

Números com stopping time (tempo de queda) anormalmente alto em relação ao seu
tamanho ("recordistas", já catalogados na literatura, ex. base de Roosendaal)
compartilham características estruturais — padrões de resíduo módulo pequenas
potências de 2/3, ou um perfil atípico na sequência de valuações 2-ádicas — que os
diferenciam da população típica de números do mesmo tamanho.

## Motivação

- Complementa H-001: se H-001 encontrar correlação real entre valuações
  consecutivas, os outliers de stopping time são o lugar mais provável para essa
  correlação se manifestar de forma extrema (sequências de a_i anormalmente baixos
  por muitos passos seguidos, por exemplo).
- Conecta-se ao "obstáculo estrutural" da literatura: entender os outliers é
  entender candidatos ao conjunto residual que nenhum modelo hoje descarta.

## Como testar

1. Computar stopping time para todos os n num intervalo grande.
2. Definir "outlier" via alguma métrica relativa (ex: stopping time / log(n) acima
   de um percentil alto, ou comparação com os recordistas já catalogados na
   literatura).
3. Comparar a distribuição de resíduos (mod 2^k, mod 3^k) e o perfil da sequência de
   valuações desses outliers com uma amostra típica do mesmo intervalo.
4. Testar se a diferença é estatisticamente significativa.

## Atualizações

- 2026-07-13: hipótese registrada, execução adiada até termos o resultado de H-001
  (ver `protocols/new-hypothesis.md` — não pular etapas).
- 2026-07-13: testada em `experiments/E-002-stopping-time-outliers/` (n até
  2.000.000, top 0.5% como outliers, 2 seeds). Resíduo mod potências de 2 mostrou
  diferença fortíssima (p < 10^-40), mas identificamos que isso é **tautológico**
  — residuo mod 2^k é quase determinístico em função da sequência de valuações
  iniciais, que por sua vez é a própria definição de "descida lenta" que torna
  um número outlier. Controle condicionando em run-length fixo confirmou que a
  tautologia persiste além do óbvio (mod 16/32/64 continuam significativos mesmo
  após remover o confounder mais simples). **Resíduo mod potências de 3 não
  mostrou nenhum sinal em nenhuma configuração** — resultado negativo genuíno:
  outliers não têm assinatura 3-ádica distinguível da população típica.
  Hipótese considerada parcialmente refutada: não há estrutura "nova" além do
  que a definição de stopping time via valuações já implica.
