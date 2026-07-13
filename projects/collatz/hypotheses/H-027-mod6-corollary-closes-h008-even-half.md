# H-027 — Corolário de H-007 para N≡4 mod 6 (fecha a metade par de H-008)

Status: confirmada (prova completa + verificação exaustiva); corolário
direto de H-007, não um resultado independente novo
Criada em: 2026-07-13

## Contexto

H-008 ficou com a metade par (N≡4 mod18) em aberto depois de H-022 provar
a metade ímpar (N≡13 mod18) via uma relação multiplicativa de 2 passos
acelerados. O registro em H-008 explicava a metade par como bloqueada
porque "passos acelerados só alcançam ímpares". Essa hipótese tentou uma
ideia estruturalmente diferente para a metade par: em vez de usar a órbita
acelerada, usar diretamente H-007 depois de UM único passo de halving.

## Enunciado (teorema)

Para todo N ≡ 4 (mod 6), N ≥ 10, existe P < N ímpar com
total_stopping_time(P) = total_stopping_time(N) + 1. Logo N nunca pode ser
recordista.

**Nota importante (correção durante a revisão)**: a primeira versão desta
derivação foi parametrizada como N=18j+4 (pensando em fechar
especificamente a metade par de H-008, mod9/mod18). Ao revisar a prova,
percebi — com ajuda do advisor — que ela **nunca usa mod 9 em lugar
nenhum**: a única condição necessária é N par com N/2 ≡ 2 (mod 3), que é
exatamente N ≡ 4 (mod 6), uma classe **estritamente mais ampla** que
N≡4 mod18. Isso significa que a metade par de H-008 nunca foi
estruturalmente difícil — ela é só um caso particular (k=3j) de um fato
mais simples e mais geral, que decorre de H-007 em uma linha. A parte
genuinamente difícil de H-008 sempre foi a metade **ímpar** (resolvida em
H-022, com uma técnica de fato nova).

## Prova

Seja N = 6k+4 (k≥1; N≥10; N par por construção).

1. M := N/2 = 3k+2. Como N par, total_stopping_time(N) = total_stopping_time(M) + 1
   (um único passo de halving).
2. M ≡ 2 (mod 3) sempre, pois 3k ≡ 0 (mod 3).
3. Por H-007 (aplicável pois M=3k+2 > 2 para k≥1): existe
   P = (2M−1)/3, ímpar, P < M, com total_stopping_time(P) = total_stopping_time(M) + 2.
4. Substituindo: P = (2(3k+2)−1)/3 = (6k+3)/3 = **2k+1**.
5. Encadeando os passos 1 e 3:
   total_stopping_time(P) = total_stopping_time(M)+2 = (total_stopping_time(N)−1)+2 = total_stopping_time(N)+1.
6. P = 2k+1 < N = 6k+4 para todo k≥0 (verificação trivial).

Logo P é menor que N e tem stopping time estritamente maior — N nunca
pode ser recordista. QED.

## Verificação computacional

`E-027-mod9-even-half-closure/experiment.py`: testado exaustivamente
k=1 a 500.000 (classe geral N=6k+4), usando `total_stopping_time` direto
(sem assumir a fórmula, calculando ambos os lados do zero). **Zero
exceções.** Confirmado também por conta própria à mão para os primeiros
casos (N=10→P=3: tst(10)=6, tst(3)=7; N=16→P=5: tst(16)=4, tst(5)=5;
N=22→P=7: tst(22)=15, tst(7)=16; N=40→P=13: tst(40)=8, tst(13)=9 —
todos batendo exatamente com tst(P)=tst(N)+1).

## Honestidade sobre o significado do resultado

Isto **fecha H-008 completamente** (a metade par cai como caso especial,
k=3j, de um fato mais geral sobre N≡4 mod6). Mas é importante ser direto:
**isto não é um resultado novo independente** — é um corolário de uma
linha de álgebra aplicada a H-007, que só não tinha sido notado porque a
metade par de H-008 foi erroneamente enquadrada (em H-022) como bloqueada
por depender de passos acelerados. Não requer nenhuma técnica nova. O
valor real está em completar a família de exclusões (H-007, H-014, H-015,
H-022, H-027) para uma caracterização íntegra de quais classes residuais
nunca contêm recordistas — não em ser, por si só, um avanço matemático de
peso.

## Conexão com literatura externa (2026-07-13)

Ao ler [Reyes Jiménez (2026), "A Fibonacci theorem for Collatz
trajectories via modular graph structure"](https://arxiv.org/abs/2606.02621)
(sobre uma questão diferente — quantas órbitas *evitam* visitar o resíduo
4 mod6 ao longo do caminho), notei que o grafo de transição mod6 que eles
constroem (Proposition 2.8: resíduo 4 transiciona para {2,5}) é
**exatamente** o mecanismo algébrico usado nesta prova: N≡4 mod6 é par,
e N/2 cai sempre em resíduo {2,5} mod6 (a classe que H-007 exclui) —
verifiquei isso de forma independente antes de anotar (N=6k+4, N/2=3k+2;
k par dá 3k+2≡2 mod6, k ímpar dá 3k+2≡5 mod6, batendo exatamente com as
transições 4→2 e 4→5 do grafo deles). Duas investigações independentes
(a deles sobre "quais órbitas evitam o resíduo 4", a nossa sobre "por que
resíduo 4 nunca é recordista") convergem na mesma estrutura de grafo mod6
— uma coincidência estrutural agradável, não uma nova prova ou resultado.

## Atualizações

- 2026-07-13: derivado, corrigido (generalização de mod9/18 para mod6
  após revisão), e verificado exaustivamente sem exceção em 500.000 casos.
  Fecha H-008 completamente. Framing honesto registrado: corolário, não
  breakthrough.
- 2026-07-13: **cross-check contra os 148 recordistas reais (OEIS
  A006877, dado já baixado em E-004)**: zero violações de H-007 (nenhum
  ≡2 mod3 exceto n=2) e zero violações de H-027 (nenhum ≡4 mod6). Mais
  interessante: isso revela uma caracterização limpa e completa mod 6 —
  distribuição real é {mod6=0: 15, mod6=1: 62, mod6=2: 1 (só n=2),
  mod6=3: 70, mod6=4: 0, mod6=5: 0}. Ou seja: **recordistas só existem em
  {0, 1, 3} mod 6, nunca em {2, 4, 5} mod 6 (exceto o caso trivial n=2 em
  mod6=2)** — as três classes excluídas têm prova completa (H-007 cobre
  2 e 5 mod6 diretamente; H-027 cobre 4 mod6). É uma afirmação curta,
  completa, com prova, e validada contra 100% dos dados reais conhecidos
  sem exceção — o tipo de resultado limpo que vale destacar mesmo não
  sendo, por si só, um avanço sobre a conjectura completa.
