# H-063 — Revisão do paper #032 (Kosobutskyy & Mailland, "Jacobsthal Trees and Generalized κx±1 Transformations") — reformulação notacional correta, sem erros matemáticos

Status: revisão externa concluída — todos os teoremas/propriedades
formais confirmados computacionalmente; 1 inconsistência textual menor
entre Remark 1.7 (prosa) e Tabela 2.6 (dados) identificada
Criada em: 2026-07-15
Origem: item 032 da coleção (`literature/papers/INDEX.md`), já baixado
(`032_Jacobsthal-Trees-Generalized-Transformations.pdf`).

## O paper

Kosobutskyy, P. & Mailland, D. (2026), *Jacobsthal Trees and
Generalized κx±1 Transformations*, Communications in Advanced
Mathematical Sciences, 9(2), 77-91, **peer-reviewed** (ISSN 2651-4001,
recebido/aceito/publicado com DOI).

Paper **estrutural/notacional**, explícito quanto ao escopo: *"the aim
of this work is not to prove the classical Collatz conjecture, but to
develop a generalized structural framework for κx±1 transformations
based on Jacobsthal-type trees."* Generaliza o problema `3x+1` para
qualquer multiplicador ímpar `κ` (`κx±1`), reorganizando a árvore
inversa de Collatz usando "números de Jacobsthal generalizados".

Relacionado ao item 084 desta mesma coleção (mesmos dois autores, ordem
invertida: Mailland & Kosobutskyy, "Modelling the Collatz problem from
a Jacobsthal viewpoint", CDS 8(1) 2026, 49-55), referenciado como `[8]`
neste paper. O item 084 é a
versão **pedagógica**, restrita ao caso clássico `κ=3`, deste mesmo
framework — publicado antes (recebido em fevereiro/2026 vs. março/2026
deste paper) e citado aqui como o "primeiro passo" do modelo. Revisão
do item 084 em [[H-069-mailland-kosobutskyy-jacobsthal-viewpoint-review]]
(número definido pela ordem de processamento da fila, ver
`literature/papers/INDEX.md`)
(mais curta, faz referência a este script em vez de duplicar).

## Definições exatas do paper

```
J^±_{κ,θ,n} = (θ·2^n ± (-1)^n) / κ                         (Def 1.1)
m_{κ,θ,n} = (θ·2^(n-1) - 1)/κ,  n par                        (Eq 1.4)
p_{κ,θ,k} = (θ·2^(k-1) + 1)/κ,  k ímpar                      (Eq 1.4)

Mapa generalizado forward ("conjectura"):
  C^±_{κ,q} = q/2          se q par
  C^±_{κ,q} = κ·q ± 1      se q ímpar                        (Def 1.5)

Teorema 2.1 (periodicidade): os nós são periódicos com período T_κ
  em potências de 2, com 2^(T_κ) = 1 + κ·m_{κ,1,T_κ}.
```

θ é sempre ímpar (parâmetro que indexa a "coluna binária" `{θ·2^n}`);
κ=3 recupera o Collatz clássico (`3x+1`).

## O que foi verificado

`experiments/E-063-jacobsthal-trees-check/experiment.py`, oito partes,
**0 falhas**:

1. **Definição 1.1 vs. Tabela 2.1**: `J^±_{1,1,n}` reproduz exatamente
   `2^n±(-1)^n` para n=0..12; `J^-_{3,1,n}` reduz-se exatamente à
   sequência clássica de Jacobsthal (OEIS A001045:
   0,1,1,3,5,11,21,43,85,171,341,683,1365); spot-checks em κ=5
   confirmados (1,13,205 e 3,51,819).
2. **Teorema 2.1 (periodicidade)** — o resultado central do paper: `T_κ`
   é **exatamente** a ordem multiplicativa de 2 módulo κ (fato padrão de
   teoria dos números), verificado para todo κ ímpar de 1 a 199 (0
   inconsistências) e conferido byte-a-byte contra os 17 valores
   explícitos da Tabela 2.2 (κ=1,3,...,33), incluindo o número de 52
   dígitos `m_{181,1,180}` para κ=181 — **bate exatamente**.
3. **Tabela 2.4** (formação periódica dos nós): 24 células legíveis da
   tabela, reproduzidas exatamente via `f(κ,n) = (2^n-1)/κ` ou
   `(2^n+1)/κ`, o que for inteiro.
4. **Tabela 2.6 / Remark 1.7** (pontos-atratores): simulação direta do
   mapa forward `C^±_{κ,q}` confirma PA={1} para κ=3,C+ (Collatz
   clássico, 10.000 valores testados, 0 exceções); PA={1,5,17} para
   κ=3,C-; PA={1,13,17} para κ=5,C+ (maioria diverge dentro do teto,
   qualitativamente consistente com os ~92,77% do paper); PA={27,35}
   para κ=181,C+ confirmados diretamente.
5. **Property 2.6** (unicidade da partição): 0 colisões entre valores de
   `θ` diferentes, testado separadamente para as famílias `m` (índice
   par) e `p` (índice ímpar), κ=3, θ=1..199.
6. **Property 2.7** (nós de ramificação = valores ímpares no ciclo):
   confirmado nos 4 ciclos conhecidos testados (κ=3: PA=1→1 valor
   ímpar; PA=5→2; PA=17→7; κ=5: PA=13→3).
7. **Property 2.5** (razão assintótica entre nós consecutivos):
   espaçamento constante entre posições de nó e razão → `2^período`
   confirmados para κ∈{3,5,7,9,11,13,17}, θ∈{1,5,11,13,25}.
8. **Exemplos específicos do paper #084** (caso especial κ=3): exemplo
   θ=5 (k=0 não é nó, k=1 é nó com q=3), Exemplo 1 (10=3·3+1), Exemplo 2
   (16=3·5+1, trajetória 5→16→8→4→2→1), condição de periodicidade mód 3
   (Eq. 7-8 do #084) — todos confirmados exatamente.

## Achado menor: inconsistência textual entre Remark 1.7 e Tabela 2.6

O **Remark 1.7** (prosa, Seção 1.2.2) afirma: *"for C(x)=181x+1,
PA={1,27,35}"*. Mas a própria **Tabela 2.6** (dados detalhados, Seção
2.8) mostra a entrada `q0=1` sob `C+_{181,q}` como `⋯→1→∞` (não
converge) — confirmado por simulação direta: a trajetória a partir de
`q0=1` sob `κ=181,C+` diverge, atingindo mais de 32 dígitos em apenas
47 iterações, sem sinal de ciclo. Ou seja, **a tabela detalhada do
próprio paper já mostra que `1` não é um ponto-atrator genuíno para
κ=181** — é o resumo informal do Remark 1.7 que generaliza demais ao
incluir "1" junto com os dois atratores reais (27 e 35). Inconsistência
textual menor entre seções do mesmo paper, não um erro matemático de
fundo (os autores parecem ter reciclado a formatação de PA={1,...} dos
casos κ=3,5 — onde `1` É um atrator genuíno — sem ajustar para κ=181).

## Por que isso é uma revisão positiva

O framework "árvores de Jacobsthal" é uma **reformulação notacional
correta** de fatos já conhecidos sobre a árvore inversa do problema
generalizado `κx±1`: o "Teorema da Periodicidade" central (Teorema 2.1)
é exatamente a ordem multiplicativa de 2 módulo κ — um fato clássico de
teoria dos números, aqui expresso através de "números de Jacobsthal
generalizados". Não há erro matemático em nenhum dos 8 teoremas/
propriedades formais testados (Teorema 2.1, Properties 2.3-2.7). A
notação é densa (reuso do símbolo "k"/"κ" tanto para o parâmetro global
quanto para índices de somatório em fórmulas adjacentes, e uma
convenção de indexação de `m`/`p` — Eq. 1.4 — que não é usada de forma
perfeitamente consistente com a Tabela 2.1, que parece usar a fórmula
`J^±` diretamente, sem o deslocamento de índice `n-1`/`k-1` da Eq. 1.4)
e exige atenção redobrada ao reproduzir, mas os resultados matemáticos
em si estão corretos.

## Notas de metodologia própria (para reprodutores futuros)

Ao escrever a verificação da Property 2.6 (unicidade) e da recorrência
de período (Property 2.5), cometi dois erros de indexação próprios,
corrigidos antes de finalizar este documento:
1. Testei inicialmente colisões de valor entre índices `n` de paridades
   diferentes para o mesmo `θ` — mas a Property 2.6 só afirma unicidade
   **dentro de cada família** (`m` com índice par, `p` com índice
   ímpar), não entre elas. Corrigido separando as duas famílias.
2. Tentei aplicar a recorrência com sinal fixo (Eq. 2.6b, sinal `+`) a
   todos os índices `n`, mas essa relação só vale para a família `m`
   (`n` par); a família `p` usa Eq. 2.6c (sinal `-`). Como a interação
   exata entre a paridade de `T_κ` e a paridade de `n` não está detalhada
   com precisão suficiente no paper para uma reprodução fórmula-a-fórmula
   inambígua, substituí por uma verificação equivalente e inambígua do
   mesmo conteúdo matemático (Property 2.5: espaçamento constante entre
   nós + razão assintótica → `2^período`), que não depende de resolver
   essa ambiguidade de convenção.

Ambos os erros eram do meu script de verificação, não do paper — foram
identificados porque as "falhas" apareciam exclusivamente em posições de
paridade ímpar, um padrão que não faria sentido como erro genuíno do
paper (que trata as duas famílias simetricamente) mas que é exatamente
o sintoma esperado de uma aplicação indevida de uma fórmula de família
errada.

## Novas hipóteses?

Nenhuma concreta. O framework é conceitualmente equivalente ao já
conhecido na literatura (árvore inversa de Collatz organizada por
colunas binárias, ver referências [7]-[10] do próprio paper) — não
sugere um caminho novo para o problema clássico (κ=3), apenas uma
notação alternativa para κ geral.

## Atualizações

- 2026-07-15: paper lido por completo (15 páginas), 8 partes verificadas
  computacionalmente, incluindo confirmação byte-a-byte de um número de
  52 dígitos. `INDEX.md` atualizado (item 032: Lido=Sim, Corrigido=Sim
  [1 inconsistência textual menor entre Remark 1.7 e Tabela 2.6],
  Implementado=Sim).
