# H-014 — Recordistas nunca são ≡5 mod 8 (exclusão por empate, não domínio)

Status: confirmada (prova + verificação em 200k casos + nos 148 recordistas oficiais)
Criada em: 2026-07-13
Origem: brainstorm assistido pelo modelo Fable (consultado a pedido do diretor
científico sobre padrões binários), verificado de forma independente.

## Enunciado

Nenhum recordista de total stopping time N>2 satisfaz N≡5 (mod 8) (ou seja,
terminação `101` em binário).

## Prova

Seja N=4u+1 com u ímpar (isso é exatamente a condição N≡5 mod 8). N é
ímpar, então o passo de Collatz dá 3N+1 = 4(3u+1).

Considere também M=N−1=4u. M é par: aplicando 2 divisões por 2,
M → 2u → u (u é ímpar por hipótese, então paramos aqui).

Como u é ímpar, 3u+1 é par; seja 3u+1 = 2^s·q com q ímpar (s = valuação
2-ádica de 3u+1). Então:

- Órbita de M=4u: 4u → (2 divisões) → u → (passo ímpar) → 3u+1 = 2^s·q →
  (s divisões) → q. Total: 2+1+s = s+3 passos padrão até chegar em q.
- Órbita de N=4u+1: N → (passo ímpar) → 4(3u+1) = 4·2^s·q = 2^(s+2)·q →
  (s+2 divisões) → q. Total: 1+(s+2) = s+3 passos padrão até chegar em q.

**Os dois caminhos chegam ao mesmo q, no mesmo número de passos (s+3)** — a
partir daí as órbitas são idênticas. Logo total_stopping_time(N) =
total_stopping_time(M) = total_stopping_time(N−1) **exatamente** (empate,
não apenas proximidade). Como empate não é "superar estritamente todo m<N"
(a definição de recordista usada no projeto, ver H-004), N nunca pode ser um
recordista — N−1 já empata com ele.

## Diferença em relação a H-007

H-007 exclui N≡2 mod 3 via **domínio estrito** (um M<N com stopping time
estritamente maior). H-014 exclui N≡5 mod 8 via **empate exato** — uma
técnica ligeiramente diferente (coalescência de trajetórias), útil como
segunda ferramenta no arsenal para futuras exclusões de classes residuais.

## Como testar

1. Verificar a identidade total_stopping_time(4u+1) = total_stopping_time(4u)
   para u ímpar, numa amostra grande.
2. Verificar que nenhum dos recordistas oficiais (OEIS A006877) é ≡5 mod 8.

## Atualizações

- 2026-07-13: confirmada. Identidade verificada sem exceção em 200.000 casos
  aleatórios (u ímpar até ~10^6). Nenhum dos 148 recordistas oficiais é ≡5
  mod 8 (distribuição mod 8 observada: {7:70, 1:43, 3:19, 6:13, 2:3},
  confirmando ausência total da classe 5 — e também das classes 0 e 4, que
  são pares e portanto já esperadas como raras/impossíveis por outros
  motivos triviais).
