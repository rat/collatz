# H-004 — Recordistas reais de stopping time: estrutura além do tautológico

Status: suportada (estrutura mod-3/9/27 confirmada com dados oficiais completos, n=148, p<10^-13); autocorrelação não suportada
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
  3. **Achado inicial mod-3** (amostra de 57 recordistas calculados
     localmente). **Correção (mesmo dia)**: a caracterização dessa amostra
     usou uma lista digitada de memória, com 4 valores incorretos (ver
     `experiments/E-004-true-record-holders/CORRECTION.md`) — o código de
     busca de recordistas estava correto (validado termo a termo contra OEIS
     A006877 até 4M), só a lista usada depois para o `Counter` estava errada.
     Refeito com a sequência oficial completa (OEIS A006877/Roosendaal, 148
     termos, até ~1.47×10^19): o achado se confirma e fica **mais forte**, não
     mais fraco — mod 3: 85≡0, 62≡1, apenas 1≡2 (o único caso é n=2, trivial;
     excluindo-o, 0 de 147 recordistas restantes são ≡2 mod 3). p=5.2×10^-14
     (mod 3), 3.2×10^-19 (mod 9), 1.8×10^-22 (mod 27) — todos com amostra
     estatisticamente válida. Tentativa de replicar com "top-K por valor bruto"
     em vez de recordistas estritos (E-006) não mostrou o mesmo viés — mas
     isso reflete que são populações diferentes (top-K bruto inclui números
     que nunca bateram recorde), não uma refutação. Hipótese agora
     **suportada** com evidência forte e dados verificados — ainda sem
     explicação mecanicista completa (H-005 explica termos subsequentes de uma
     órbita, não o número inicial).
