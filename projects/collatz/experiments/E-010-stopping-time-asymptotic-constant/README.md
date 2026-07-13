# E-010 — Constante assintótica do stopping time

Hipótese relacionada: [`H-010-stopping-time-asymptotic-constant.md`](../../hypotheses/H-010-stopping-time-asymptotic-constant.md)

## O que foi testado

Derivamos K≈7.2283 a partir de fatos já estabelecidos por nós mesmos (E[a]=2
para a distribuição geométrica das valuações, H-001), prevendo
total_stopping_time(n) ≈ K·log₂(n). Ajustamos regressão linear simples nos
dados reais (~1 milhão de n ímpares, 3 até 2.000.000).

## Resultado

- **K empírico = 7.1833** vs. **K teórico = 7.2283** — diferença relativa de
  apenas **0.62%**. Ótima concordância entre a derivação teórica (a partir de
  fatos que já tínhamos estabelecido em H-001) e os dados reais.
- **R² = 0.0307** — log₂(n) sozinho explica só ~3% da variância de
  total_stopping_time(n). A grande maioria da variação **não** vem do
  tamanho de n, vem de estrutura fina (a sequência específica de valuações).
  Isso é consistente com — e ajuda a explicar por que — conseguimos achar
  recordistas e exceções estruturais (H-004, H-007): a média se comporta
  como previsto, mas o desvio individual é enorme.
- O desvio padrão dos resíduos cresce lentamente com log₂(n) (54.5 → 60.2 ao
  longo da amostra) — consistente com a teoria clássica de tempos de
  passagem de passeios aleatórios com deriva, onde a variância cresce
  aproximadamente linear no número de passos (aqui, em log(n)).

Reproduzir: `python3 experiment.py 2000000` (~7s).

## Conclusão

A heurística de passeio aleatório está corretíssima **em média** — nossa
derivação própria bate com os dados dentro de <1%. Mas o R² baixo é o ponto
mais interessante: confirma quantitativamente que a magnitude de n diz muito
pouco sobre o stopping time individual, o que é exatamente o tipo de
variância residual que pode esconder estrutura (como a que achamos em
H-004/H-007). Não é uma descoberta nova — reproduz um resultado clássico —
mas fizemos a derivação e verificação nós mesmos, com nossos próprios dados
e fatos já estabelecidos, em vez de só citar a literatura.

## Status de H-010

**Confirmada** (derivação teórica bate com dados empíricos dentro de <1%).
