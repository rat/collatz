# H-116 — Barghout, "On the Probabilistic Proof of the Convergence of the Collatz Conjecture" (2019): mesma falácia recorrente (densidade estática ≠ estatística de órbita), disfarçada por teoria dos números elementar correta

Status: ALEGAÇÃO DE PROVA REFUTADA (parcialmente — teoria de base correta, conclusão não se sustenta)
Criada em: 2026-07-17
Origem: item 123 do INDEX.md (Journal of Probability and Statistics/Hindawi
2019), baixado pelo diretor científico em 2026-07-16, parte do lote de
10 papers pendentes de revisão.

## Enunciado do paper

Constrói uma "tabela RF" (recurrent frequency) tabulando quantas vezes
um inteiro par precisa ser dividido por 2 até virar ímpar; observa
padrão determinístico alternado sobre os inteiros pares em geral e
sobre os elementos pares gerados por 3n+1; usa a razão observada
(~3:1) entre "dividir mais de uma vez" e "dividir uma vez só" para
argumentar que a trajetória de Collatz decresce em média e converge.
Título, abstract e conclusão usam a palavra "proved"/"proven".

## Avaliação

**Camada 1 (Lemas 1-4): correta e genuinamente determinística.** A
valuação 2-ádica v₂(n) segue um padrão fixo e alternado ao percorrer
os inteiros pares — é simplesmente a densidade natural de v₂=1 entre
pares ser 1/2, v₂=2 ser 1/4, etc. Fato estático sobre o CONJUNTO dos
inteiros pares (ou valores 3n+1), não sobre nenhuma órbita específica.
Provas por indução simples, corretas.

**Camada 2 ("Theory 1" e a conclusão): a mesma falácia recorrente já
catalogada neste projeto** (H-045, H-065, H-093, entre outras). O passo
crítico ("*Considering the apparent random distribution of even
integers produced by Collatz function processes... we may average
Collatz processes*") transporta uma densidade ESTÁTICA (fato sobre o
conjunto de inteiros pares) para a estatística de VISITAS de uma órbita
DINÂMICA específica — pressupõe implicitamente equidistribuição/mixing
da órbita, que é precisamente o conteúdo não-provado da conjectura, não
uma consequência dos Lemas 1-4. A alegação de novidade do abstract
("*not heuristically derived as opposed to the well-known heuristic
argument*") é falsa: os fatos de densidade são determinísticos, mas o
passo que os converte em "convergência" reimporta exatamente a
heurística de Terras/Lagarias que o autor diz evitar.

**Exclusão de ciclos não-triviais, incompleta**: Lemma 8 prova
rigorosamente que o único ciclo com UM elemento ímpar é o trivial
(1-4-2-1) — equação n=1/(2^l−3) só modela esse caso. Ciclos com k≥2
elementos ímpares exigiriam n=(soma)/(2^B−3^k) e não são tratados. A
Seção 10 ("Nontrivial Nested Cycles"), que deveria cobrir exatamente
esse caso, admite abertamente ser só probabilística ("*we may assume
with small degree of certainty... with high probability*"). A
não-existência de ciclos não-triviais nunca é demonstrada, só
conjecturada por plausibilidade estatística.

**Honestidade textual mista**: o autor concede as lacunas em vários
pontos ("*needs yet elaborative approach... to reach full proof*",
"*presuming that the function yields no other cycles*") — mas título,
abstract e conclusão reivindicam mais do que o corpo demonstra.

**Verificação empírica feita nesta revisão**: simulação de órbitas
(n=27, 703, 9663, 6171) confirma que trajetórias individuais podem
crescer centenas/milhares de vezes acima do valor inicial antes de
decrescer (n=9663 atinge ~2806× seu valor inicial) — ilustra
concretamente por que um argumento "em média" não garante descida para
todo n. Tentativa de reproduzir a "razão crítica 2,57:1" citada a
partir das fórmulas dadas (End=1,5n uma divisão, End=0,375n três
divisões) deu ≈2,42:1 — derivação subespecificada no texto, ponto
secundário de verificação.

## Relevância para a investigação atual (G(v)/Syracuse, qx+1)

**Não é irrelevante** — o argumento RF é, no fundo, uma medida de
frequência de v₂ sobre elementos pares de Collatz e de 3n+1, tocando
diretamente nossa linha G(v)/densidade de Syracuse. O autor generaliza
explicitamente para kn+1 (nota do Lemma 4) e discute 5n+1/7n+1 (Seção
8) — os ciclos de 5n+1 citados (13-83-33-13, 17-27-43-17) conferem
corretamente com a literatura (mesmos ciclos usados em nossos próprios
testes de H-109). Valor para o projeto: contraste útil de por que
densidade estática ≠ garantia dinâmica — exatamente a distinção que
nosso framework (G(v), medida de Syracuse, barreira de endogenia)
formaliza rigorosamente onde este paper só assume informalmente.

## Veredito

Não é uma prova completa nem uma alegação honesta e delimitada (do
tipo "provamos densidade zero de contraexemplos, não excluímos
exceções individuais"). É um argumento heurístico de média
(estruturalmente idêntico ao heurístico clássico) maquiado por teoria
dos números elementar correta sobre densidade estática, com hedging
textual disperso mas título/conclusão que reivindicam "prova".
