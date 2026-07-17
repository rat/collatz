# H-112 — Checagem de novidade para H-109/H-110/H-111: Kontorovich-Lagarias (2009), Gonçalves-Greenfeld-Madrid (2022), Applegate-Lagarias (1995) e Wirsching (1998) contra a generalização qx+1 e a barreira de endogenia

Status: concluído — novidade recalibrada, dois achados importantes de prior art
Criada em: 2026-07-17
Origem: 5 papers/livro identificados em `literature/papers-to-download-qx1-novelty-check.md`
(pendente desde H-109), baixados manualmente pelo diretor científico e
arquivados como itens 127-131 do INDEX.md. Analisados via 3 forks em
paralelo (Applegate-Lagarias juntos; Kontorovich-Lagarias +
Gonçalves-Greenfeld-Madrid juntos; capítulos II/III/V do livro de
Wirsching, os únicos indicados como relevantes na nota original).

## Enunciado

Checar se a generalização qx+1 (H-109: equação de pressão em forma
fechada ρ(M_q(α))=q^(α−1)/(2^α−1), virada estrutural de densidade
positiva para densidade zero em q≥5) e a barreira de endogenia
(H-110/H-111: recursão sozinha não força colapso de variância; falta
uma afirmação de quase-independência aritmética entre subárvores) já
estavam, total ou parcialmente, na literatura.

## Resultado — dois achados de prior art que recalibram a novidade

### 1. Kontorovich & Lagarias (2009) já tinham o valor numérico exato de α₂(q=5)

**Achado mais direto**: o Teorema 8.10 deles define η₅,BP como o expoente
da função de contagem da árvore reversa de 5x+1 (I*(x;ω)=x^(η5,BP+o(1)),
via teoria de grandes desvios sobre um branching random walk) e reporta
**η₅,BP≈0,650919** — idêntico, a 6 casas decimais, ao nosso α₂=0,650919
(segunda raiz de q^(α−1)=2^α−1 para q=5, H-109). É a mesma quantidade,
calculada por método completamente diferente (grandes desvios vs.
autovalor de pressão em forma fechada), 15+ anos antes.

**O que sobrevive como novo**: a forma fechada ρ(M_q(α))=q^(α−1)/(2^α−1)
válida para QUALQUER q (eles fazem 3x+1 e 5x+1 separadamente, sem
generalizar nem unificar); a identificação da virada estrutural em q=5
como fenômeno de família (ver item 2 abaixo — mesmo isso tem prior art
parcial); e uma resolução de uma disputa em aberto da própria literatura
(ver a seguir).

**O "≈0,68" da nossa nota não resolvida está agora identificado**: NÃO é
dimensão de Hausdorff — é η*₅,BP≈0,678, a previsão de um modelo
ESTOCÁSTICO CONCORRENTE (Volkov, árvore binária completa com codificação
diferente), citado pelos próprios Kontorovich-Lagarias como discrepante
do deles, com uma nota explícita de que é uma questão em aberto não
resolvida por dados empíricos insuficientes (seção 8.10, "Remark").
**Nossos dados (enumeração exata de árvores 5x+1 reais, Hill estimator
batendo em 0,650919, H-109) são evidência empírica nova a favor da
predição de Kontorovich-Lagarias sobre a de Volkov** — uma contribuição
genuína e citável, se apresentada com essa moldura (resolvendo uma
disputa de 2009, não descobrindo o número).

### 2. Wirsching (1998), Capítulo III, já previu heuristicamente a virada estrutural em q≥5

Wirsching generaliza seu formalismo de médias 3-ádicas para T_p(n) (nosso
qx+1 com p=q) na seção final do Capítulo III ("Why 3n+1 and not pn+1?"),
derivando lim ℓ_p(n)/n = 1/(2−log₂p) — **negativo para p>4**, com a
conclusão explícita (não provada, "presumably"): para p≥5 a densidade
assintótica positiva é impossível. **Mesmo limiar exato que o nosso**
(nosso drift log q−2log2 muda de sinal em q=4; dele, a fórmula fica
negativa em p>4) — a descoberta QUALITATIVA da virada estrutural em
q≥5 já estava heuristicamente antecipada há 27 anos, apoiada apenas em
evidência indireta (primos de Wieferich, Brocco 1995), nunca provada.

**O que sobrevive como novo**: a prova/derivação rigorosa da equação de
pressão fechada, os valores numéricos exatos para q=5,7,9 e a
confirmação empírica direta em árvores reais (slopes de contagem, Hill
estimator) — Wirsching tinha a heurística correta mas não os números
nem uma derivação.

### 3. Wirsching (1998), Capítulo V, tem uma conjectura de cobertura estruturalmente idêntica ao "ingrediente que falta" de H-110/H-111

O "reduction theorem" (3.10) do Cap. V prova densidade assintótica
positiva uniforme dos predecessores CONDICIONALMENTE à "Weak Covering
Conjecture for Mixed Power Sums" (3.9) — uma conjectura sobre se
conjuntos finitos de somas mistas de potências de 2 e 3 (construídas de
vetores admissíveis) cobrem as classes de resíduo mod 3^ℓ de forma
suficientemente uniforme. Estrutura lógica **idêntica** à barreira de
H-110: recursão + uma afirmação de equidistribuição/cobertura
aritmética não provada ⟹ densidade positiva. Não há evidência, nos
capítulos lidos, de que essa conjectura tenha sido resolvida desde 1998
— permanece em aberto no livro.

**Leitura honesta**: o "ingrediente que falta" identificado em H-110 (via
o enquadramento moderno de endogenia/smoothing transforms, Aldous-
Bandyopadhyay 2005) pode ser, na prática, o MESMO problema em aberto há
quase 30 anos, articulado de forma diferente (combinatória direta em vez
de teoria de smoothing transforms) — não uma barreira nunca vista antes.
O enquadramento de H-110 é mais moderno e talvez mais tratável (conecta
a Tao 2022 e à classificação padrão de Durrett-Liggett/ABM), mas a
dificuldade central parece ser a mesma.

### 4. Gonçalves, Greenfeld & Madrid (2022) — confirmação independente rigorosa da virada em q≥5, e um precedente metodológico para H-111

O Teorema 1.3 (generalização de Tao para mapas C_{p,q,r}) exige, entre
outras condições, q^(p−1)<p^p — para p=2 (nossa família), isso dá q<4,
excluindo TODO q≥5 ímpar. É uma confirmação independente, via teorema
rigoroso (não heurística, não modelo estocástico) na direção FORWARD,
de que algo muda estruturalmente em q≥5 exatamente onde H-109 encontrou
densidade zero na árvore REVERSA — consistente qualitativamente, embora
não seja a mesma afirmação logicamente.

A técnica de prova modulariza a Seção 7 de Tao (o processo de renovação
bidimensional que dá o decaimento de Fourier, Prop. 1.17) como uma
"caixa-preta" reaplicável a outros (p,q) — precedente metodológico útil
para a extensão bivariada que H-111 cogitou (decorrelação entre folhas
da árvore reversa), mostrando que modularizar essa técnica é factível.
Não resolve H-111 diretamente (o resultado deles continua sendo forward,
não sobre correlação entre folhas de subárvores irmãs).

### 5. Applegate & Lagarias (1995) — sem sobreposição com α=2/qx+1

Trabalham exclusivamente com q=3 (Lagarias-Weiss 1992, modelo de
ramificação multitipo de 6 estados mod 9). Provam convergência fraca da
contagem normalizada de folhas (via Athreya-Ney 1972) — o análogo da
parte (E) da nossa decomposição, não do índice de cauda α. Nenhuma
menção a q≥5 ou generalização. Sem sobreposição com H-109/H-110/H-111,
mas citável como o precedente histórico do modelo de ramificação geral e
da parte (E).

## Veredito consolidado sobre a novidade de H-109/H-110/H-111

- **α*=2 e o valor numérico 0,650919 (q=5)**: não são descobertas novas
  isoladas — Kontorovich-Lagarias (2009) já os tinham, por outro método.
- **A forma fechada ρ(M_q(α))=q^(α−1)/(2^α−1) válida para q arbitrário,
  com derivação rigorosa**: continua nova, ninguém unificou isso numa
  fórmula fechada de família antes.
- **A virada estrutural qualitativa em q≥5**: prevista heuristicamente
  por Wirsching (1998) e confirmada independentemente (via teorema
  forward) por Gonçalves-Greenfeld-Madrid (2022) — não é nova como
  observação qualitativa, mas nossa confirmação quantitativa rigorosa
  (equação fechada + verificação empírica em árvores reais) fecha uma
  lacuna de 27 anos entre "presumably" e prova+número.
- **A barreira de endogenia / decorrelação entre folhas (H-110/H-111)**:
  estruturalmente equivalente a uma conjectura em aberto desde 1998
  (Wirsching, Weak Covering Conjecture) — não uma barreira nova.
  O enquadramento via endogenia/smoothing transforms é uma
  contribuição de linguagem/conexão a teoria mais recente, não a
  descoberta do problema em si.
- **A calibração empírica ρ_eff≲0,06 (H-111)**: não tem precedente
  direto identificado nestes 5 textos — parece ser uma contribuição
  genuína (medida quantitativa do tamanho do gap, não só sua
  existência).

## Ações de arquivo

- `literature/papers-to-download-qx1-novelty-check.md`: nota "Hausdorff
  dimension≈0,68" resolvida (era η*₅,BP de Volkov, não dimensão de
  Hausdorff) — atualizar/remover a pendência.
- `literature/papers/INDEX.md`: itens 127-131 arquivados e revisados
  (colunas Lido/Corrigido/Implementado a preencher).
- H-109 e H-110 devem referenciar este H-112 nas suas seções de
  calibração de novidade.

## Referências

- Item 127: Kontorovich & Lagarias (2009), arXiv:0910.1944.
- Item 128: Gonçalves, Greenfeld & Madrid (2022), arXiv:2111.06170.
- Item 129: Applegate & Lagarias (1995), "Density Bounds I: Tree-Search Method".
- Item 130: Applegate & Lagarias (1995), "The Distribution of 3x+1 Trees".
- Item 131: Wirsching (1998), Lecture Notes in Mathematics 1681 (Cap. II, III, V lidos).
- H-109, H-110, H-111 (hipóteses recalibradas por esta revisão).
