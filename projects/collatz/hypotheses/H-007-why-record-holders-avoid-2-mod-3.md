# H-007 — Prova: por que recordistas nunca são ≡2 mod 3 (exceto n=2)

Status: confirmada (prova completa + verificação computacional exaustiva)
Criada em: 2026-07-13

## Contexto

H-004 encontrou (com dados oficiais, n=148) que recordistas reais de stopping
time praticamente nunca são ≡2 mod 3 — só a exceção trivial n=2. H-005 deu uma
peça de estrutura relacionada (resíduo de termos subsequentes de uma órbita),
mas não explicava o número **inicial**. Esta hipótese fecha essa lacuna com
uma prova completa.

Depois de descobrir (via busca na literatura) que essa exclusão já é usada como
otimização conhecida em buscadores de "delay records" (ex. repositório
`cuda-collatz`: *"All N of the form 3k+2 are skipped because these numbers are
not potential Delay Records"*), mas sem prova publicada facilmente acessível,
derivamos a prova abaixo.

## Enunciado (teorema)

Para todo N ≡ 2 (mod 3) com N > 2, existe M < N com
total_stopping_time(M) = total_stopping_time(N) + 2. Logo N nunca pode ser um
recordista (M já o supera, e M < N). O único caso em que o argumento não se
aplica é N = 2, onde M colapsaria em 1 — o estado terminal, fora do domínio da
recursão normal.

## Prova

Seja N ≡ 2 (mod 3), N > 2. Defina M = (2N − 1) / 3.

1. **M é inteiro**: N ≡ 2 (mod 3) ⟹ 2N ≡ 4 ≡ 1 (mod 3) ⟹ 2N − 1 ≡ 0 (mod 3).
2. **M é ímpar**: separando por paridade de N —
   - N ímpar e ≡2 mod 3 ⟺ N ≡ 5 (mod 6). Escrevendo N = 6j+5:
     2N−1 = 12j+9 = 3(4j+3), logo M = 4j+3, que é ímpar.
   - N par e ≡2 mod 3 ⟺ N ≡ 2 (mod 6). Escrevendo N = 6j+2:
     2N−1 = 12j+3 = 3(4j+1), logo M = 4j+1, que é ímpar.
   - Em ambos os casos, M é ímpar.
3. **M < N**: M/N = (2N−1)/(3N) < 2/3 < 1 para todo N > 0.
4. **A órbita de M passa por N exatamente 2 passos depois**: como M é ímpar,
   o passo de Collatz dá S(M) = 3M+1 = 3·(2N−1)/3 + 1 = (2N−1)+1 = 2N.
   Como 2N é par, o passo seguinte é S(2N) = N. Logo M → 2N → N em exatamente
   2 passos, e o restante da órbita de M a partir daí é idêntico ao restante
   da órbita de N. Portanto total_stopping_time(M) = total_stopping_time(N) + 2.
5. **Exceção N=2**: aqui M = (2·2−1)/3 = 1. Mas n=1 é o estado terminal (por
   definição, stopping time 0, sem continuar a recursão) — o passo 4 não se
   aplica a M=1 (não existe "S(1) = 3·1+1" na definição de parada). Por isso o
   argumento falha exatamente e só exatamente neste caso, explicando por que
   N=2 é a única exceção observada em H-004.

## Como testar

Verificação computacional: para todo N ≡ 2 (mod 3) num intervalo, calcular M =
(2N−1)/3, confirmar que é inteiro, ímpar, menor que N, e que
total_stopping_time(M) − total_stopping_time(N) = 2 exatamente (exceto N=2).

## Atualizações

- 2026-07-13: teorema formulado e verificado computacionalmente para todo
  N ≡ 2 (mod 3) de 2 a 200.000 (66.665 casos, par e ímpar) — 100% de acordo
  com a fórmula, única exceção N=2 como previsto. Fecha completamente a
  pergunta em aberto de H-004.
