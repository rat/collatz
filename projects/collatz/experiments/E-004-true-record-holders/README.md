# E-004 — Recordistas reais de stopping time

Hipótese relacionada: [`H-004-true-record-holders.md`](../../hypotheses/H-004-true-record-holders.md)

## O que foi testado

Recordistas reais (n tal que total_stopping_time(n) supera todo m < n — mesma
definição usada nas tabelas de Roosendaal) até o limite de 20-50 milhões,
calculados diretamente (não copiados de tabela externa). Os primeiros valores
batem com os recordistas conhecidos na literatura (ex: 27, 703, 871, 6171,
77031, 837799, 8400511 — este último é um recordista famoso e bem documentado),
o que valida nossa implementação.

Três testes:
(a) resíduo mod 2^k / 3^k / primos não relacionados (5,7,11,13), como em E-002;
(b) autocorrelação lag-1 **interna** da própria órbita de cada recordista
(não redutível a resíduo mod 2^k), comparada a uma amostra típica de órbita
igualmente longa.

## Resultado (a) — resíduo

Com apenas ~40-57 recordistas reais, a maioria das tabelas mod 2^k, mod 27, mod
11, mod 13 tem células com contagem esperada abaixo de 5 — **estatisticamente
inválidas**, e o script agora detecta e reporta isso em vez de imprimir um
p-valor enganoso.

O que sobrou válido e testável:

- **mod 3 e mod 9: sinal forte e robusto** (chi2=26-29, p ~ 10^-6 a 10^-8,
  confirmado com duas seeds diferentes de amostra típica). Composição real dos
  57 recordistas até 20M: **30 são ≡0 mod 3, 25 são ≡1 mod 3, e só 2 são ≡2 mod
  3** — uma sub-representação forte da classe residual 2 mod 3 (esperado seria
  ~19 em cada classe sob distribuição uniforme).
- mod 5, mod 7 (primos não relacionados à aritmética 3n+1): nenhum sinal — bom
  controle negativo, como esperado.

### Por que isso NÃO é tautológico (diferente do achado mod-2^k de E-002)

3n+1 mod 3 é sempre ≡ 1 mod 3, **independente do valor de n mod 3** — não existe
o mesmo vínculo mecânico direto que liga resíduo mod 2^k à sequência de
valuações. Então esse sinal, se real, não é uma reformulação da definição de
stopping time — seria uma regularidade genuinamente nova sobre QUE números se
tornam recordistas.

### Ressalva importante

Amostra de 57 recordistas é **pequena** para uma alegação forte — recordistas de
stopping time são raríssimos (crescem de forma extremamente lenta/logarítmica
com o range: só 57 num intervalo de 20 milhões). O sinal é estatisticamente
válido dentro dessa amostra e replicou com duas seeds, mas isso ainda é um
candidato promissor, não uma conclusão estabelecida. Precisaria de mais
recordistas (limite muito maior, o que é caro computacionalmente em Python
puro) ou de uma tabela publicada mais extensa (Roosendaal) para confirmar em
escala maior.

## Resultado (b) — autocorrelação interna, com controle de confounder

Primeira rodada (sem controle): recordistas com autocorrelação lag-1 média
0.076-0.106, típico 0.038-0.046, diferença "significativa" (p ~0.001-0.0001).

**Mas identificamos um confounder real antes de aceitar isso**: recordistas têm
órbitas sistematicamente mais longas (média 149 passos vs 73 do grupo típico
filtrado), e a estimativa de autocorrelação amostral tem viés conhecido
dependente do comprimento da série (~-1/(L-1) para séries i.i.d. curtas — séries
mais curtas têm viés mais negativo). Isso por si só poderia gerar toda a
diferença observada, sem nenhum fenômeno real.

**Controle**: ajustamos um modelo `autocorr ~ a + b/(L-1)` usando só o grupo
típico (que sabemos, por H-001/H-003, ser consistente com i.i.d.), e testamos se
o resíduo dos recordistas (autocorr observado menos o previsto pelo próprio
comprimento) é diferente de zero.

Resultado: resíduo médio = 0.023, p = 0.053 — **não significativo** ao nível de
corte de 0.01 usado no resto do projeto. Conclusão: a diferença "ingênua" era
majoritariamente (não necessariamente totalmente) explicada pelo viés de
comprimento de amostra curta, não por uma dinâmica realmente diferente dentro
das órbitas de recordistas.

## Status de H-004

**Resultado misto**:
- Parte da hipótese (estrutura mod-2^k) não pôde ser testada de forma válida
  (amostra insuficiente).
- Autocorrelação interna: sinal inicial não sobrevive ao controle de
  confounder — **não suportada**.
- **Achado genuíno e não-tautológico**: recordistas reais mostram sub-
  representação forte da classe residual 2 mod 3, robusta a duas seeds
  diferentes. Candidato promissor para investigação futura, mas com amostra
  pequena (57) — registrar como pista, não como conclusão fechada.
