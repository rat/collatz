# H-022 — Prova parcial de H-008: exclusão de N≡13 (mod 18) via 2 passos acelerados

Status: confirmada (prova + verificação exaustiva, 100.000 casos) — resolve metade de H-008
Criada em: 2026-07-13
Origem: nova abordagem pedida pelo diretor científico para H-008, após duas
tentativas de coalescência por deslocamento pequeno (H-015, H-016) falharem.

## Por que essa abordagem é genuinamente diferente

H-015 e H-016 buscaram M=N−k (deslocamento **aditivo** pequeno, mesmo "K"
livre). Essa família nunca poderia isolar mod 9 especificamente (ver
H-016). Em vez disso, aqui construímos M via uma relação **multiplicativa**:
M tal que aplicar o passo acelerado **duas vezes** a M leva exatamente a N
— isto é, M = (9·N_final − constante)/3² em vez de M = N − k. Isso muda a
proporção M/N para algo perto de 8/9 (não 1 − k/N), e permite isolar
condições mod 9 de verdade.

## Enunciado (teorema)

Para todo N = 18j+13 (j≥0) — ou seja, N ímpar com N≡4 (mod 9) — o número
M = 16j+11 satisfaz:

1. M < N sempre (diferença N−M = 2j+2 > 0).
2. M é sempre ímpar.
3. Aplicando o passo acelerado a M duas vezes, com valuações exatas a=1
   depois b=2, chega-se exatamente em N.
4. Logo total_stopping_time(M) = total_stopping_time(N) + 5 (2+3 passos
   padrão) — **M sempre domina N**, excluindo N=18j+13 como recordista.

## Prova

Seja M=16j+11 (ímpar, pois 16j é par). Passo 1 (M ímpar): 3M+1 = 48j+34 =
2(24j+17). Como 24j+17 é sempre ímpar (24j par, +17 ímpar), a valuação é
exatamente a=1, dando M₁=24j+17.

Passo 2 (M₁ ímpar): 3M₁+1 = 72j+52 = 4(18j+13) = 4N. Como N=18j+13 é
sempre ímpar (18j par, +13 ímpar), a valuação é exatamente b=2, dando
exatamente N.

Portanto M → M₁ → N em exatamente 2 passos acelerados (2+3=5 passos
padrão), e total_stopping_time(M) = 5 + total_stopping_time(N) > 
total_stopping_time(N), com M < N sempre. Isso prova que N=18j+13 nunca
pode ser recordista.

## O que fica em aberto

Esta prova cobre apenas a **metade ímpar** da classe 4 mod 9 (N≡13 mod 18).
A metade par (N≡4 mod 18) **não pode** ser excluída pela mesma técnica —
passos acelerados só alcançam números ÍMPARES por construção, então um N
par nunca pode ser "o alvo" de uma cadeia de passos acelerados a partir de
outro M. A exclusão da metade par precisaria de um argumento
estruturalmente diferente (talvez relacionando N ao seu registro ímpar
imediatamente anterior na sequência de recordes). Continua em aberto, mas
com evidência empírica (nenhum dos 148 recordistas reais é ≡4 mod 18
tampouco).

## Verificação

Confirmado sem exceção para j=0 a 100.000 (N até ~1.8 milhões).

## Atualizações

- 2026-07-13: teorema formulado, provado e verificado. Resolve a metade
  ímpar de H-008. Metade par permanece em aberto.
- 2026-07-13: **metade par resolvida em H-027** (corolário de H-007, na
  verdade mais amplo: N≡4 mod6). H-008 agora completamente fechada.
- 2026-07-13: **reavaliação crítica de novidade (importante)**. Ao
  consolidar a família de exclusão em H-028 e checar se já era conhecida,
  percebi (com o advisor) algo que deveria ter sido óbvio antes: **este
  teorema é exatamente uma instância de "colisão de caminhos"** — M's
  orbit passa por N depois de exatamente 5 passos (2 passos acelerados,
  a=1 então b=2). Isso é *precisamente* o mecanismo que a técnica genérica
  de "sieve" usada por caçadores de recordistas na prática (`cuda-collatz`:
  *"checks whether paths come together. If two paths join then the upper
  one can never yield a Delay Record"*) já detecta e explora
  computacionalmente — sem precisar conhecer a fórmula algébrica fechada
  (M=16j+11 em termos de j). Colisões de 5 passos estão bem dentro da
  profundidade que qualquer sieve razoável varre (a fonte reporta ~80% de
  exclusão via essa técnica, mais que nossos 62,5%).

  **Conclusão honesta**: o EFEITO PRÁTICO deste teorema (quais N são
  excluídos) quase certamente já é alcançado computacionalmente pela
  comunidade de busca de recordistas, mesmo que a FÓRMULA FECHADA
  específica (M=16j+11) talvez não esteja escrita em lugar nenhum como
  teorema nomeado. Isso rebaixa a expectativa de "novidade publicável"
  deste resultado — é, na melhor das hipóteses, uma instância elegante e
  provada de um fenômeno já conhecido/explorado genericamente, não uma
  descoberta de algo que a comunidade não sabia. Ver `H-028.md` (seção
  "Checagem de novidade") para o contexto completo.
