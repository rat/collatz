# H-002 — Estrutura residual em outliers de stopping time

Status: aberta (planejada — depende do resultado de H-001)
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
