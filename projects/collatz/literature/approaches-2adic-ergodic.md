# Abordagens 2-ádicas e ergódicas

## Ideia central

Estender o mapa de Collatz para os inteiros 2-ádicos (Z₂). Nesse domínio, o mapa é
mensurável e, com respeito à medida 2-ádica natural, **ergódico** — as órbitas
"exploram" resíduos de forma suficientemente aleatória. Isso dá uma linguagem formal
para a intuição de que o comportamento de Collatz é "aleatório o bastante".

## Resultados relevantes

- Não existem pontos periódicos 2-ádicos irracionais conhecidos para o mapa de
  Collatz — isso restringe o espaço de comportamentos possíveis das órbitas.
  [Karger — A 2-adic extension of the Collatz function](https://www.math.uchicago.edu/~may/VIGRE/VIGRE2011/REUPapers/Karger.pdf)
- [Chris Smith — The Collatz Step and 2-adic Integers](https://cdsmithus.medium.com/the-collatz-step-and-2-adic-integers-6f003efaf81c)
  — introdução acessível à conexão entre o passo de Collatz e Z₂.

## Limitação conhecida

Ergodicidade 2-ádica dá uma linguagem para "quase toda órbita se comporta bem", mas
— como em Tao — não elimina a possibilidade de um conjunto de medida zero de
exceções, nem prova que a órbita especificamente converge a 1 em vez de a outro
ciclo. Ver o "obstáculo estrutural" em `overview-and-known-results.md`.

## Nota de cautela

Há múltiplos preprints recentes alegando "prova via análise 2-ádica" completa
(ex.: combinando decaimento de entropia termodinâmica + 2-ádica). Nenhum foi aceito
pela comunidade. Ver `unverified-proof-claims.md` antes de levar essas alegações a
sério como ponto de partida.
