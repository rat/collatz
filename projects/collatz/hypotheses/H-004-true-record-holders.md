# H-004 — Recordistas reais de stopping time: estrutura além do tautológico

Status: resultado misto (ver experimento E-004 — achado promissor mod-3, resto não suportado)
Criada em: 2026-07-13

## Enunciado

H-002 usou "outliers" definidos localmente (top 0.5% de uma amostra) e achou só
estrutura tautológica (mod-2^k) mais um nulo genuíno (mod-3^k). Aqui usamos a
definição padrão da literatura de **recordista**: n tal que total_stopping_time(n)
supera o de todo m < n (a mesma noção usada nas tabelas de Roosendaal). Propomos
duas coisas:

1. Replicar os testes de resíduo (mod 2^k, mod 3^k) nos recordistas reais, como
   checagem de consistência com H-002.
2. Testar algo **não redutível a resíduo mod 2^k**: será que a própria sequência
   de valuações de um recordista, olhada internamente (lag-1, dentro da mesma
   órbita), mostra correlação serial diferente da de órbitas típicas de
   comprimento comparável? H-001/H-003 mostraram que órbitas típicas não têm essa
   correlação — recordistas poderiam ser diferentes exatamente por isso.

## Motivação

- Recordistas reais são mais raros e mais extremos que percentis locais — se há
  algum sinal genuíno, é mais provável aparecer aqui.
- O teste de autocorrelação interna não depende de resíduo mod 2^k, então não
  sofre do problema tautológico identificado em H-002.

## Como testar

1. Calcular recordistas reais até um limite grande (ex: 5-10 milhões) via
   varredura de total_stopping_time.
2. Repetir testes de resíduo mod 2^k / mod 3^k (mais mod primos não relacionados
   5/7/11/13 como controle negativo adicional).
3. Para cada recordista com órbita longa o suficiente, calcular a autocorrelação
   lag-1 interna da própria sequência de valuações; comparar a distribuição desse
   valor com uma amostra de números típicos de órbita igualmente longa.

## Atualizações

- 2026-07-13: hipótese aberta.
- 2026-07-13: testada em `experiments/E-004-true-record-holders/` (recordistas
  reais até 20-50M, validados contra valores conhecidos da literatura, ex.
  8400511). Três resultados:
  1. Resíduo mod 2^k: amostra insuficiente para teste válido (poucos
     recordistas reais existem — são raríssimos).
  2. Autocorrelação interna lag-1: sinal aparente inicial (p~0.001) não
     sobreviveu ao controle de confounder de comprimento de órbita (p=0.053
     após controle) — não suportada.
  3. **Achado novo e não-tautológico**: recordistas mostram forte
     sub-representação da classe residual 2 mod 3 (2 de 57, esperado ~19),
     robusto a duas seeds de amostra típica (p~10^-6 a 10^-8). Como 3n+1 mod 3
     é sempre ≡1 independente de n mod 3, isso não decorre mecanicamente da
     aritmética como o sinal mod-2^k de H-002. Candidato promissor para
     investigação futura — amostra de 57 ainda é pequena para conclusão forte.
