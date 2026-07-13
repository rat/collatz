# E-016 — Busca de coalescência mod 9 para H-008 (resultado negativo)

Hipótese relacionada: [`H-016-mod9-coalescence-search.md`](../../hypotheses/H-016-mod9-coalescence-search.md)

## O que foi testado

Generalizamos o simulador simbólico de E-015 para módulo conjunto 9·2^d
(informação completa mod 9 + d bits binários), buscando alguma coalescência
N vs. N−k que excluísse a classe 4 mod 9 (questão em aberto de H-008).

## Resultado — encontramos candidatos, mas nenhum é genuíno

A busca (d=1 a 6, k=1 a 100) encontrou várias coalescências aparentes para
N≡4 mod9 (ex: d=3, N≡13 mod72, M=N−1, verificado contra órbitas reais: 10/10
K's confirmados). **Mas ao testar se essas relações são exclusivas da classe
4 mod 9** — repetindo a mesma busca (mesmo d, mesmo resíduo mod 2^d, mesmo
k) para os outros 8 resíduos possíveis mod 9 — **todas funcionaram para os 9
resíduos igualmente**. Ou seja: nenhuma dessas coalescências depende de fato
do resíduo mod 9 — são fenômenos puramente mod-2^d (já cobertos pela busca
mais ampla de H-015), que só "aparecem" na classe 4 mod 9 por coincidência
aritmética (o r1 escolhido também satisfaz ≡4 mod9, sem que isso seja
relevante ao mecanismo).

Repetimos a busca com k até 100 e nenhum achado exclusivo de mod9=4 apareceu.

## Por que isso não funciona (explicação técnica)

Derivamos: T(n) mod 9 = (3r+1)·5^a mod 9, onde r = n mod 3 (não n mod 9!) e
a é a valuação do passo. Ou seja, a evolução do resíduo mod 9 **só depende
de n mod 3**, não do valor completo de n mod 9 — o resíduo mod 9 de n
carrega informação "extra" que não influencia em nada a trajetória futura
mod 9. Isso explica por que fixar o módulo conjunto 9·2^d não cria nenhuma
restrição nova além do que já vem do mod-2^d puro: a parte "mod 9 além de
mod 3" é irrelevante para qualquer coalescência baseada em subtrair k
pequeno.

## Conclusão

**Esta técnica não resolve H-008.** É um resultado negativo, mas instrutivo:
mostra que a via "coalescência tipo H-014/H-015, só que com módulo mod 9
junto" está estruturalmente fadada a não encontrar nada específico de mod 9,
porque a mecânica de coalescência por subtração de k pequeno é dirigida
inteiramente pela estrutura binária (mod 2^d), e a informação relevante mod 3
que de fato afeta a dinâmica (H-005) é mais grosseira que mod 9 inteiro.

Se H-008 tiver solução, provavelmente precisa de uma ideia diferente — não
uma busca por coalescência com deslocamento pequeno, mas talvez uma relação
multiplicativa (não aditiva) entre N e M, ou uma análise de ciclo/período
usando diretamente a fórmula T(n) mod 9 = (3r+1)·5^a mod9 de forma mais
elaborada (ex: olhando toda a órbita, não só um passo).

## Status de H-016

**Refutada como abordagem para H-008** (tecnicamente funciona como
coalescência, mas não é específica de mod 9 — não avança a questão em
aberto). Explicação teórica documentada para não repetir a tentativa nesta
forma exata no futuro.
