# H-071 — Revisão: Andrei & Masalagiu, "About the Collatz conjecture" (1998)

Status: revisão externa concluída (maioria correta e provada; um erro real encontrado — limite superior não-provado e refutado)
Criada em: 2026-07-15
Origem: item 101 da coleção de literatura (`literature/papers/INDEX.md`),
arquivado via busca EBSCO/ScienceDirect em 2026-07-15.

## O paper

Ştefan Andrei, Cristian Masalagiu (Universidade "Al.I.Cuza", Iaşi,
Romênia). *Acta Informatica* 35, 167-179 (1998), Springer-Verlag —
periódico revisado por pares estabelecido. Paper clássico, anterior à
maioria da literatura moderna sobre Collatz catalogada neste projeto.

Constrói a **mesma árvore reversa de Collatz** que usamos em H-018/E-018
(Algorithm 1: nó v tem filho 2v sempre, e filho extra (v−1)/3 quando
v≡4 mod6) — coincidência notável, o mesmo objeto matemático foi
redescoberto de forma independente 28 anos antes deste projeto. Deriva
uma fórmula fechada para "pular" blocos de passos consecutivos do mesmo
tipo (Teorema 3.1), usa isso para construir um "Algoritmo 2" acelerado, e
prova uma família explícita infinita de números para os quais a
conjectura vale por construção (Teoremas 4.1-4.2).

## Resultados verificados

Todos testados em `experiments/E-071-andrei-masalagiu-review/experiment.py`:

1. **Teorema 3.1** — f^(2p)(2^p·r+2^p−1) = 3^p·r+3^p−1, para todo p,r≥0.
   **Confirmado, 458 casos, 0 falhas.**
2. **Lema 4.1** — f^(2t+3)((2^(2t+2)−1)/3) = 1, para todo t≥0.
   **Confirmado, 21 casos, 0 falhas.**
3. **Teorema 4.2** (família geral) —
   f^(3^m·n+2m+2)(2^(m+1)·((2^(3^m·n)+1)/3^(m+1))−1) = 1, para
   n∈{6t+1,6t+5}. **Confirmado, 110 casos, 0 falhas** (após corrigir um
   erro de precedência de parênteses na minha própria primeira
   implementação — a divisão por 3^(m+1) é interna, só sobre
   2^(3^m·n)+1, garantida exata pelo próprio Teorema 4.1c do paper; não
   é (2^(m+1)·(...)−1)/3^(m+1) como eu havia montado inicialmente).
4. **Teorema 3.2, parte (1)** — Racc(n)≥1,5 para todo n>2, onde
   Racc(n)=niv(n)/pas(n) é a razão entre passos do algoritmo padrão
   (niv) e do algoritmo acelerado do paper (pas). **Confirmado, 99.998
   casos (n=3 a 100.000), 0 falhas.** Reimplementação do Algorithm 2
   validada contra o próprio exemplo do paper (n=23: niv=15, pas=4,
   Racc=3,75 — bate exatamente).

## Erro real encontrado

**Teorema 3.2, parte (2)**: "Racc(n)≤i, para todo n, 2^i≤n<2^(i+1), i≥2."
A prova do paper para esta parte é **uma única frase não-demonstrada**:
"(ii) The most 'convenient' case (n=2^k) yields Racc(n)=k (k iterations
are also enough for numbers n, 2^k<n<2^(k+1))" — em contraste direto com
a parte (1), que tem prova explícita completa por casos (n=4m, 4m+1,
4m+2, 4m+3).

**Refutado computacionalmente**: 5 contraexemplos até n=10.000 — n=5
(i=2, Racc=2,5), n=6 (i=2, Racc=2,667), n=7 (i=2, Racc=2,667), n=15
(i=3, Racc=4,25), n=151 (i=7, Racc=7,5). Menor contraexemplo verificado
manualmente: n=5 tem órbita padrão [5,16,8,4,2,1] (niv=5); n=151 tem
órbita padrão [151,454,227,682,341,1024,512,256,128,64,32,16,8,4,2,1]
(niv=15) — ambos rastreados independentemente do código de `racc()`,
confirmando que a falha não é bug de implementação.

**Gravidade**: contida — o próprio paper já sinaliza fraqueza ("this
'fastening' rate is not a real one because the iterations of Algorithm 2
'hide' other concrete computation steps", Example 3.1) e a Conjectura 2
subsequente (limite assintótico da razão média = 3) é apresentada como
conjectura, não teorema, então o erro não contamina nenhuma conclusão
posterior mais forte. Ainda assim é um erro real: um enunciado rotulado
"Teorema" (não "Conjectura") com contraexemplo explícito.

## Conjectura 2 (não provada pelo paper) — testada, consistente

"O limite assintótico da razão média de aceleração é 3." Calculamos
Pmed(n) = média de Racc(k) para k∈[2^n,2^(n+1)) até n=16: sequência
2,250 → 2,458 → 2,705 → ... → 2,957 → 2,960, consistente com convergência
lenta a 3, sem evidência contrária. Not provado nem refutado — como o
próprio paper reconhece.

## Avaliação geral

Paper matematicamente sólido e honesto (usa "Conjectura" corretamente para
o resultado não-provado, "Teorema" para os provados) com um erro real
mas contido — um caso claro de "teorema com prova ausente para uma das
duas partes", pego porque testamos cada cláusula separadamente em vez de
confiar no rótulo do enunciado inteiro. Conexão de interesse histórico
para este projeto: o Algorithm 1 é a mesma árvore reversa de H-018,
publicada 28 anos antes, sem que os autores parecessem estar cientes de
conexões com processos de ramificação/densidade assintótica (o foco do
paper é aceleração computacional, não densidade estatística).

## Atualizações

- 2026-07-15: revisão externa concluída. PDF lido por completo (14
  páginas). Teoremas 3.1, 4.1, 4.2 e Lema 4.1 confirmados sem exceção.
  Teorema 3.2 parte (1) confirmada; parte (2) refutada com 5
  contraexemplos até n=10.000, gravidade contida (o próprio paper já
  reconhecia a fraqueza do resultado numa nota textual).
