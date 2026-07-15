# Síntese do programa de pesquisa Ruiz Castillo

Data: 2026-07-15. Consolida sete revisões técnicas individuais
(H-039, H-050, H-052 a H-056) mais uma leitura contextual (item 055,
sem H-0XX próprio) de papers do mesmo autor — Juan Carlos Ruiz
Castillo, ScD., Universidad de San Carlos de Guatemala. Este documento
não revisa nenhum paper novo; organiza o que já sabemos sobre o
conjunto, algo que nenhuma revisão individual capturava sozinha.

## Escopo coberto

`literature/papers/INDEX.md` cataloga **~17 papers** deste autor
(items 001, 008, 010, 013, 017, 020, 026, 033, 035, 039, 048, 054, 055,
059, 063, 065, 066) — número inflado pelo próprio padrão editorial do
autor de publicar o mesmo trabalho em espanhol e inglês como entradas
separadas (059/063 e 065/066 são, cada par, o mesmo paper nas duas
línguas), então a contagem de trabalhos *distintos* é menor que a
contagem de itens. Desses, **8 têm PDF acessível** e foram lidos por
completo (7 técnicos + o de filosofia); os outros **9 estão bloqueados**
por download automatizado no ResearchGate e nunca foram lidos — esta
síntese cobre apenas o subconjunto acessível, cerca de metade do total
catalogado. Dado que o padrão se repete de forma consistente nos 7
papers técnicos lidos (ver abaixo), é razoável esperar — mas não
confirmar sem leitura — que os 9 restantes sigam arquitetura
semelhante.

| Item | H-0XX | Paper | Veredito |
|---|---|---|---|
| 001 | H-039 | Geometría Residual | correto, elementar, muito repetitivo |
| 008 | H-050 | Dissipative Bounds and Residual Decomposition | correto, elementar |
| 010 | H-052 | Teorema Central del Límite Residual | correto; título mais forte que o corpo (honesto) |
| 013 | H-053 | Operador de Transferencia Residual | **1º erro real** — Proposición 5.3 |
| 017 | H-054 | Medidas de Gibbs Residuales | correto |
| 020 | H-055 | Principio Variacional Residual | correto, análise convexa padrão |
| 026 | H-056 | Grandes Desviaciones Residuales | **2º erro real** — Conjetura 7.3 vs. Proposición 3.4 |
| 055 | — | Platonismo y realismo en matemáticas y física | contexto filosófico (não é Collatz) |

## A arquitetura comum: um conceito clássico por paper, uma única quantidade

Os sete papers técnicos formam uma sequência deliberada. O próprio
paper #001 (H-039, p.3) desenha a cadeia que os precede:

```
deuda residual ⟹ drift residual ⟹ presión residual ⟹ entropía disipativa
⟹ dimensión disipativa ⟹ grandes desviaciones ⟹ medidas de Gibbs
⟹ operador de transferencia ⟹ teorema central del límite residual
```

e se apresenta como uma "segunda etapa" que constrói geometria (métrica,
curvatura) sobre esse alicerce. Ou seja: cada paper pega **um** conceito
diferente de teoria ergódica/mecânica estatística clássica (grandes
desvios, medidas de Gibbs, operador de transferência, TCL, princípio
variacional, geometria diferencial) e o aplica à **mesma quantidade**:
a "deuda residual"

```
L_k(n) = k·log₂(3) − A_k(n),      A_k(n) = soma das k primeiras valuações 2-ádicas
```

que é exatamente o drift logarítmico padrão / "equação de ciclo" já
conhecida deste projeto (H-001/H-011) e de outros papers da coleção sob
notação diferente (Fu-Liu-Wang/H-044, Mohammed/H-045). Nenhum dos sete
papers introduz uma quantidade Collatz-específica genuinamente nova —
cada um reveste a mesma identidade com um vocabulário formal diferente.

## O que é matematicamente correto (a maior parte)

Em 5 dos 7 papers (001, 008, 010, 017, 020), toda identidade concreta
verificada está correta — geralmente reescrita algébrica trivial da
definição de `L_k`, ou aplicação padrão e correta de análise
convexa/teoria de grandes desvios de livro-texto (sup de afins é
convexo, Legendre-Fenchel, Chernoff-Markov). Nenhum desses cinco
contém um erro real. O aparato é sempre honestamente rotulado: todo
resultado genuinamente em aberto aparece como "Conjetura", nunca
"Teorema"/"Proposición" — inclusive quando o **título** do paper diz
"Teorema" (item 010) mas o resultado central, no corpo, é rotulado
"Conjetura 4.2" com as hipóteses técnicas faltantes listadas
explicitamente. Todos os sete terminam com uma negação explícita de
provar Collatz.

## Os dois erros reais encontrados

Ambos são **erros de consistência interna** (enunciado contradiz
demonstração/resultado já provado no mesmo texto), não erros de cálculo
isolados nem tentativas de prova malsucedidas:

1. **Item 013 (H-053)**: Proposición 5.3 afirma `lim_{t→∞} L_t(1) = 0`;
   a própria demonstração, na linha anterior, deriva que a quantidade
   **cresce exponencialmente** (`e^{(log₂3−1)t}`, com `log₂3−1>0`) e
   usa essa observação para justificar a necessidade de normalização
   futura — o símbolo `□` aparece sem o enunciado ser corrigido.
   Confirmado numericamente (`L_t(1)` cresce de 2,84 em t=1 a 6,4×10⁵⁰
   em t=200). Contido: nenhum resultado posterior depende do valor.

2. **Item 026 (H-056)**: a Definición 3.1 define a função de tasa
   `I_RC(x)` via um evento de cauda **unilateral** (`{L_k/k≥x}`). A
   Proposición 3.4 (já demonstrada, Seção 3) prova corretamente que essa
   `I_RC` é monótona não-decrescente. Mas a Figura 1, a Conjetura 7.3 e
   a Conjetura 7.5 (Seção 7, conjectural) descrevem consistentemente
   entre si a função de Cramér **bilateral clássica** (forma em V, zero
   único) — que contradiz a monotonicidade já provada. Confirmado por
   três métodos independentes (fórmula padrão restrita a t≥0,
   simulação Monte Carlo, distribuição exata via `Fraction` para k
   pequeno). Contido: a conclusão do paper não depende da forma
   específica de `I_RC`.

Ambos os erros passaram despercebidos pelo próprio autor apesar de
estarem a poucas páginas de distância da proposição que os contradiz —
sugerindo que a produção rápida desta série (~17-20 papers) não inclui
uma revisão de coerência interna entre seções.

## O que este projeto acrescentou (além de revisar)

- **H-039**: cálculo explícito de `P_RC(t)`, `g_RC(t)`, `K_RC(t)` em
  forma fechada para o modelo i.i.d. padrão — o paper nunca calcula
  nada numericamente; achamos uma singularidade real em `t=log(2)`.
- **H-052**: primeira verificação empírica de uma previsão desta série
  contra **trajetórias reais** de Collatz (não simulação i.i.d.
  abstrata) — normalidade assintótica de `Z_k` confirmada como
  plausível para k=5..300.
- **H-053, H-056**: localização exata e verificação computacional
  tripla dos dois erros reais, cada um isolado e contextualizado sem
  impacto no restante do argumento.

## A chave explicativa: o paper de filosofia (item 055)

"Platonismo y realismo en matemáticas y física" (Ruiz Castillo & Moreno
Sanabria, 2026, revista *Diotima*) não é sobre Collatz — é filosofia da
matemática (platonismo de Gödel/Penrose vs. realismo científico,
hipótese do universo matemático de Tegmark, efetividade irrazoável de
Wigner). O autor se revela explicitamente **platonista/realista**:
estruturas matemáticas têm existência objetiva, e o próprio paper
descreve o trabalho em Collatz como "un modelo conceptual que ilustra
la profunda interrelación entre lo discreto y lo continuo, lo
determinista y lo caótico, lo formal y lo físico".

Isso explica o padrão observado nos sete papers técnicos: Collatz não é
o alvo a resolver, é um **estudo de caso acessível** para demonstrar que
formalismos consagrados da física/mecânica estatística "também se
aplicam" a um problema aritmético simples de enunciar — evidência, para
a tese platonista do autor, de que estruturas matemáticas revelam algo
real e transferível entre domínios. Isso também explica:

- **Por que cada paper aplica UM conceito por vez** em vez de convergir
  para um ataque mais direto à conjectura — o objetivo é demonstrar
  *aplicabilidade repetida*, não *progresso cumulativo*.
- **A honestidade epistêmica consistente** (rotular "Conjetura" mesmo
  quando o título diz "Teorema", disclaimers explícitos de não-prova em
  todos os sete) — como o objetivo real nunca foi provar Collatz,
  admitir isso não custa nada ao propósito filosófico mais profundo.
- **A formação do autor**: doutorado em Física e Matemática, mas também
  licenciado em Ensino de Matemática e Física; a tese de doutorado
  (citada em todos os outros papers) usa o "Enfoque Ontosemiótico"
  (EOS), um referencial de **educação matemática**, não de teoria dos
  números — sugerindo que a linha de pesquisa nasce da didática/
  filosofia da matemática, não de uma tentativa de resolver Collatz.

## Avaliação geral

O programa Ruiz Castillo, na parte que lemos, é um exercício expositivo
coerente e de boa-fé: matemática elementar majoritariamente correta
(5/7 sem nenhum erro; os 2 erros restantes são contidos e de
consistência interna, não de cálculo), honestidade consistente sobre o
que é conjectura vs. resultado, e nenhuma alegação de prova. **Não é**
uma tentativa de resolver a conjectura de Collatz, nem uma fonte de
conteúdo matemático novo sobre o problema em si — é a mesma identidade
de drift/deuda residual revestida, repetidamente, por sete vocabulários
formais diferentes, publicada em Zenodo sem indicação de peer review.
O valor real, para este projeto, não veio das conjecturas do autor
(nenhuma abriu uma linha de investigação nova aqui), mas do exercício de
revisão em si: as extensões computacionais próprias (H-039, H-052) e a
localização de dois erros reais de consistência interna (H-053, H-056)
que o próprio autor não percebeu.

## Referências

- Papers: `literature/papers/INDEX.md`, items 001, 008, 010, 013, 017,
  020, 026, 055.
- Revisões: `hypotheses/H-039-*.md`, `H-050-*.md`, `H-052-*.md` a
  `H-056-*.md`.
- Experimentos: `experiments/E-039-*` a `E-056-*` (mesma numeração dos
  H-0XX correspondentes).
