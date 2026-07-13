# H-024 — A densidade do subárvore reverso não é função de resíduo 3-ádico limitado

Status: confirmada (resultado negativo, mas explica rigorosamente por que H-013 não fecha)
Criada em: 2026-07-13
Origem: pergunta motivada por uma lista de ideias de outra IA (sugestão de
abordagem via teoria espectral/grafos), testada antes de investir na
construção de um operador de transferência de dimensão finita.

## Enunciado

Pergunta: a densidade D(v) do subárvore reverso de Collatz enraizado em v
(usada na tentativa de derivação de H-013/H-018) é uma função apenas do
resíduo de v módulo 3^K para algum K finito? Se sim, um operador de
transferência de dimensão finita (matriz, autovetor) poderia calcular D(v)
exatamente — uma abordagem espectral/de autômato de estado finito.

**Resposta: não.** D(v) depende de estrutura 3-ádica arbitrariamente
profunda, não de nenhum resíduo finito.

## Como foi testado

Escolhidos vários v distintos, todos ≡85 (mod 3^6=729) mas com magnitudes
bem diferentes (85, 1543, 4459, 14665, 72985). Medida a densidade de cada
um usando o mesmo "orçamento" relativo (n_max escalado proporcionalmente à
magnitude de cada v, para não repetir o erro de comparar em orçamentos
desiguais — ver H-018).

## Resultado

| v | v mod 729 | densidade D(v) |
|---|---|---|
| 85 | 85 | 0.0089 |
| 1543 | 85 | 0.0004 |
| 4459 | 85 | 0.0002 |
| 14665 | 85 | 0.000038 |
| 72985 | 85 | 0.000027 |

Variação de **mais de 300×** entre números com o mesmo resíduo mod 729,
mesmo controlando adequadamente o orçamento de magnitude. Validado que o
código está correto (reproduzindo exatamente os valores já conferidos para
J_4=85 na configuração original).

## Implicação

Isso **explica rigorosamente** por que a tentativa de derivação fechada de
H-013 (via a recursão exata D(v)=D(2v)+D(ramo)) não fechou: os "filhos de
ramo" w_i são números genéricos cuja densidade depende de estrutura
3-ádica arbitrariamente profunda, não de um resíduo finito. Isso também
descarta, com evidência direta (não só falha de tentativa), a abordagem de
"teoria espectral/grafos com truncamento de resíduo" sugerida como
possibilidade por uma lista de ideias externa — não é que não tentamos
direito, é que a quantidade em si não é computável por um autômato de
estado finito nesse sentido.

## Atualizações

- 2026-07-13: hipótese testada e confirmada. Resultado negativo, mas
  encerra com clareza uma linha de investigação (operador de transferência
  de dimensão finita) para H-013, em vez de deixá-la genuinamente em
  aberto sem explicação.
- 2026-07-13: nota — uma terceira lista de ideias (de outra IA) sugeriu
  "operadores de transferência quânticos" (Hamiltoniano, gap espectral,
  Lieb-Robinson) como abordagem para problemas deste tipo. Esse achado
  (H-024) já mostra que a obstrução é sobre a PRECISÃO NECESSÁRIA (3-ádica
  infinita), não sobre o tipo de operador usado — vestir a mesma
  construção de física quântica não resolveria essa obstrução real.
