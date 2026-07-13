# E-037 — Verificação da Conjectura 10.4 de Pratiher (2026)

Hipótese relacionada: [`H-037-pratiher-form-off-by-one.md`](../../hypotheses/H-037-pratiher-form-off-by-one.md)

## O que foi testado

Objetivo original: verificar se Freq_a(N) (fração assintótica de {1,...,N}
cuja órbita atinge, pela primeira vez, uma potência de 2 ≡8 mod9, "forma
𝔞" na notação de Pratiher) converge para α≈0,9762 como o paper afirma
(Conjecture 10.4), e se esse valor é derivável por métodos de
equidistribuição/operador de transferência.

Implementação: para cada n∈[1,N], simula a trajetória de Collatz direta
(não acelerada) até encontrar a primeira potência de 2 (checagem via bit
trick `n & (n-1) == 0`), extrai o expoente M, e classifica `M mod 6` na
tabela do próprio Pratiher (Teorema 4.3: 0↔𝔡, 1↔𝔠, 2↔𝔟, 3↔𝔞, 4↔𝔣, 5↔𝔢).
Memoiza por convergência de trajetórias (múltiplos n compartilham cauda).

## Resultado

**A distribuição numérica bate quase exatamente com a tabela de Pratiher
(Observação 10.2) — mas sob os rótulos ERRADOS.**

| N | minha forma dominante (M par) | Pratiher relata |
|---|---|---|
| 10^6 | 𝔣 = 0,976082 | Freq_a(10^6) — paper não lista, mas tendência bate |
| 10^7 | 𝔣 = 0,9761136 | Freq_a(10^7) = 0,97611 |
| 10^7 | 𝔟 = 0,0238808 | Freq_c(10^7) = 0,02388 |

Todas as 6 formas conferem **exatamente** sob um deslocamento cíclico de
1 posição na correspondência (M mod6 ↔ letra): o valor que Pratiher
relata para a forma X é, número por número (inclusive nas caudas raras:
4, 4, 4, 44 em 10^7), o que este script calcula para a forma em
M ≡ (X's M + 1) mod 6. Ver `hypotheses/H-037...md` para a tabela completa
de correspondência e o argumento teórico (paridade, idêntico ao mecanismo
de H-012) que prova que a forma dominante REAL tem que ter M par — nunca
ímpar como a Tabela 10.2 do paper alega.

Verificação adicional (exata, não só numérica): as 3 formas de "cauda"
com M ímpar (as únicas que podem vir de n JÁ sendo uma potência de 2 com
expoente ímpar, já que nenhuma trajetória não-trivial pode entrar num
expoente ímpar) têm contagem EXATA de 4 cada em N=10^7 — batendo
exatamente com a contagem teórica de potências de 2 de expoente ímpar
≤10^7 distribuídas por resíduo mod6 (12 expoentes ímpares ≤23, 4 em cada
classe mod6). Ver seção "Verificação exata" em H-037.md.

## Reproduzir

`/home/rat/.venv/bin/python3 experiment.py [N]` (sem argumento, roda
N=10,100,...,10^7 em sequência; ~8s para N=10^7 em single-thread com
memoização).

## Status de H-037

**Refutada a pergunta original** (não foi isso que motivou a
investigação de fato — a pergunta "dá para derivar α por
equidistribuição" ficou em suspenso), mas **encontrado algo mais
concreto**: evidência muito forte (correspondência exata, não
aproximada, em todas as 6 classes) de um erro de rotulagem
off-by-one no paper de Pratiher — os números (0,9762 / 0,0238) estão
corretos, a atribuição de qual "forma" carrega cada número está
deslocada em 1 posição no ciclo de 6.
