# H-040 — Revisão crítica do paper #004 (Seymour, "Steiner Sentence Length"): teorema principal provavelmente incorreto, apesar de alegada verificação formal em Lean

Status: revisão externa concluída — achado importante e bem verificado
(erro provável no teorema principal), com cautela epistêmica apropriada
Criada em: 2026-07-14
Origem: segundo paper priorizado da coleção `literature/papers/INDEX.md`
(item 004 — escolhido por já ter PDF local, a pedido do diretor
científico de priorizar os 15 já baixados).

## O paper

"First-Principles Derivation of the Steiner Sentence Length
Distribution" — Jon Seymour (wildducktheories.com, Sydney, Austrália),
julho de 2026, 20 páginas. Muito melhor que o item 001 em vários
aspectos: cita literatura real e relevante (Steiner 1977 — que já
conhecíamos via nossa própria `literature/nontrivial-cycles.md`; Terras
1976; Lagarias ed. 2010), inclui validação empírica real com testes
χ² e p-valores reportados, e alega verificação formal completa em Lean
4/Mathlib ("no `sorry`, no `admit`").

## O que está correto (verificado independentemente)

**Teorema 2.1 (matriz de transição mod 8)**: re-derivei a aritmética
na mão (para n≡1,3,7 mod8, v₂(3n+1) é uma constante exata — 2,1,1
respectivamente) e confirmei por amostragem direta (200.000 inteiros
aleatórios, `experiments/E-040-seymour-steiner-sentence-check/`). Bate
exatamente com a matriz do paper. Este resultado está correto.

## O que parece estar incorreto

**Teorema 5.1 (distribuição do comprimento de sentença =
3^(k-1)/4^k)**. O paper argumenta ativamente que o modelo "ingênuo"
P(k)=(1/2)^k está errado (χ²≈10⁶, rejeitado) e que 3^(k-1)/4^k é a
fórmula correta (p≈0,61, consistente). Nossa reimplementação
independente das mesmas definições (Def 1.2 palavra Steiner, Def 1.3
sentença Steiner) dá o resultado **oposto**: a simulação (300.000
amostras, mesmo protocolo do Apêndice B do próprio paper) bate com
**(1/2)^k** — o modelo que o paper chama de ingênuo — e não com
3^(k-1)/4^k.

**Contraexemplo concreto, aritmética exata (não depende de nenhuma
simulação aleatória)**: n=68567 (≡7 mod8). Calculando diretamente:
S(68567)=102851 (≡3 mod8); S(102851)=154277 (≡5 mod8). A sequência de
resíduos de entrada é [7,3,5], que casa com o regex `(7*3)?(1|5)` do
próprio paper como **uma única palavra Steiner** (zero setes... na
verdade um sete, um três, terminal cinco), terminando em letra 5. Por
definição do próprio paper (Def 1.3), isso é uma sentença de
comprimento k=1 — mas com b₀≡**7**, não b₀≡5. A prova do Teorema 5.1
("P(sentence length=1) = π₀(5) = 1/4... sentenças cuja primeira
palavra já é a palavra de fechamento, i.e. b₀≡5") **só conta o caso
b₀≡5** — nunca considera que uma palavra iniciada em 3 ou em 7 pode
ela mesma terminar em 5 (via P[3][5]=1/2, ou via 7*→3→5), fechando a
sentença no primeiro passo mesmo sem b₀≡5.

## Diagnóstico do mecanismo do erro

A matriz de transição do Teorema 2.1 (correta) descreve **um único
passo de Syracuse**: P[a][b] = probabilidade de que UMA aplicação de S
a partir de resíduo a resulte em resíduo b. Mas uma **palavra** Steiner
com entrada 3 ou 7 abrange **dois ou mais passos** (3→terminal em 1
passo extra; 7→...→3→terminal em 2+ passos extras), enquanto uma
palavra com entrada 1 ou 5 é sempre exatamente 1 passo (a própria
entrada já é terminal). A recursão das Seções 3–5 (`d_s^(k+1) =
Σ_t d_t^(k) P[t][s]`) usa a MESMA matriz P (de um passo) como se fosse
a transição entre entradas de palavras CONSECUTIVAS — o que é válido
apenas para entrada 1 (onde aplicar P uma vez de fato avança para a
próxima palavra). Para entrada 3 ou 7, aplicar P uma vez dá a
distribuição do **próprio terminal daquela palavra** (que pode ser 5,
fechando a sentença ali mesmo) — não a entrada de uma "próxima
palavra" que necessariamente continua. Ao tratar como se sempre
continuasse, a recursão nunca "gasta" a massa que deveria fechar via
classes 3 e 7, subestimando a taxa de fechamento real (1/2 por
palavra) pela taxa 1/4 usada na fórmula do paper.

Derivação direta do valor correto: dado que toda palavra não-fechada
(terminal=1) — venha de entrada 1, ou de 3→1, ou de 7*→3→1 — termina
num nó de resíduo exatamente 1, e a linha 1 da matriz é uniforme
(Teorema 2.1, já confirmado), a entrada da PRÓXIMA palavra é sempre
uniforme sobre {1,3,5,7}, **independente da história** (memoryless).
Logo P(uma palavra com entrada uniforme fecha) = (1/4)(0) + (1/4)(1/2)
+ (1/4)(1) + (1/4)(1/2) = 1/2 exatamente, dando P(comprimento=k) =
(1/2)^k — uma distribuição Geométrica(1/2) limpa, batendo com nossa
simulação.

## Por que isso é preocupante (e por que reporto com cautela)

O paper alega verificação formal completa em Lean 4/Mathlib sem
`sorry`. Não temos acesso ao arquivo Lean (`Paper67.lean`, mencionado
mas não anexado ao PDF que conseguimos) para apontar exatamente onde a
formalização diverge da definição matemática pretendida — é
inteiramente possível que o Lean tenha formalizado (e verificado
corretamente) uma versão **ligeiramente diferente** da definição de
"palavra"/"sentença" do que a Definição 1.2/1.3 em prosa descreve, e o
erro esteja na tradução prosa→formalização, não na lógica Lean em si.
De qualquer forma, com base exclusivamente nas definições **como
escritas no paper**, nossa verificação (aritmética exata + simulação
em larga escala, ambas reproduzíveis) diverge do resultado central.

## Novas hipóteses?

Não sobre a conjectura de Collatz em si — mas o MECANISMO usado aqui
(decompor órbitas em "palavras" via classes mod 8, usando que v₂(3n+1)
é constante para 3 das 4 classes ímpares mod 8) é genuinamente
relacionado à nossa própria família de exclusão H-007/H-014/H-022/
H-028. Vale considerar, numa sessão futura, se a estrutura de
"palavras Steiner" oferece alguma perspectiva nova sobre nossa
classificação — mas isso é especulativo, não uma hipótese concreta
ainda.

## Atualizações

- 2026-07-14: paper lido por completo, Teorema 2.1 confirmado, Teorema
  5.1 contestado com contraexemplo de aritmética exata + simulação em
  larga escala. Flags atualizadas em `literature/papers/INDEX.md`
  (item 004: Lido=Sim, Corrigido=Sim, Implementado=Sim).
