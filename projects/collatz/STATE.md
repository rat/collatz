# Estado atual — Collatz

Última atualização: 2026-07-14

## Coleção de papers (nova, 2026-07-14)

`literature/papers/INDEX.md` — 100 resultados do Google Scholar
(busca "Collatz", ordenado por data), 15 PDFs baixados, tabela com
flags Lido/Corrigido/Implementado para o diretor científico preencher
manualmente conforme formos processando um por um. **Não iniciar a
leitura/incorporação sem pedido explícito** — ver nota no
`BACKLOG.md` item 0.

**Item 001 processado (H-039)**: paper de Ruiz Castillo ("Geometría
Residual..."), sem PDF local, lido inteiramente via navegador (39
páginas). Matemática de base correta (formalismo termodinâmico
clássico, Ruelle/Ellis, aplicado honestamente ao observável de
dissipação 2-ádica), mas com problemas reais: mesmo fato trivial
("convexa ⟹ f''≥0") repetido 4x como resultado maior; identidade
central apresentada como derivada no corpo mas admitida como
conjectura só na conclusão; zero conteúdo numérico (única figura é
explicitamente "conceptual"); 100% autocitação nas 13 referências
(zero literatura de Collatz ou de formalismo termodinâmico clássico).
Fizemos o cálculo explícito que o paper nunca faz (P_RC(t), g_RC(t),
K_RC(t) em forma fechada para o modelo i.i.d. padrão, verificado
contra E[a]=2/Var[a]=2 já estabelecidos) — achado limpo: singularidade
real em t=log(2). Nenhuma hipótese nova sobre a conjectura em si
emergiu — ver H-039 para avaliação honesta completa.

**Item 004 processado (H-040), achado importante**: paper de Seymour
("Steiner Sentence Length Distribution"), PDF local, muito melhor
qualidade que o 001 (cita Steiner 1977/Terras 1976/Lagarias, valida
empiricamente, alega verificação formal Lean 4/Mathlib sem `sorry`).
Teorema 2.1 (matriz de transição mod8) confirmado independentemente.
Mas **o teorema principal (P(comprimento)=3^(k-1)/4^k) parece
incorreto**: reimplementação própria + contraexemplo de aritmética
exata (n=68567: resíduos 7→3→5, uma só palavra Steiner, sentença de
comprimento 1 com b₀≡7, não b₀≡5 como a prova do paper assume) +
simulação em larga escala (300k amostras) batem com (1/2)^k — o
modelo "ingênuo" que o paper argumenta estar errado. Mecanismo do erro
identificado: conflação entre matriz de 1-passo e transição
palavra-a-palavra. Não temos o código Lean para confirmar onde a
formalização diverge da prosa. **Ordem de leitura da coleção**:
priorizar os 15 papers já baixados localmente antes dos que exigem
navegador (preferência do diretor científico, 2026-07-14).

**Item 005 processado (H-041)**: segundo paper de Seymour ("A Regular
Expression Language for the Collatz Graph"), mesmo autor do item 004
mas de boa prática epistêmica — explicitamente "working paper",
separa provado de conjecturado. Proposição 3.1 e Teorema 3.6
confirmados corretos (20k e 50k casos). Corolário 2.2 (exit ping-pong
mod24) tem erro pequeno e sistemático (afirma 11/23 conforme
paridade de t; na verdade é sempre 11) — mas não consta na lista
"what is proved" do próprio paper, gravidade baixa. Conjectura central
(caracterização via regex) tratada honestamente como conjectura.

**Item 014 processado (H-042), sem erros**: Williams ("A Coordinate
System for Collatz Dynamics", Univ. of Southampton, arXiv:2607.01718)
— qualidade acadêmica claramente superior aos itens anteriores:
literatura extensa e genuína, código público no GitHub, declaração
honesta de uso de IA (Claude Opus 4.8, verificação humana integral
declarada), agradecimento a colega que já pegou um erro menor antes
da publicação. Teorema 3.6 (dinâmica diagonal, 20k casos) e Teorema
4.1 (linhas k≡2mod4 k≥6 sem primos, 14 linhas até 58 elementos) ambos
confirmados corretos, sem exceção. Ponto de calibração importante para
a crítica cumulativa: nem todo paper da coleção tem problemas.

**Item 016 processado (H-043), achado importante — prova completa
inválida**: Halemane ("CTUHSK Theorem", engrxiv.org, 35 páginas) —
diferente dos itens anteriores, alega uma **prova completa** da
Conjectura de Collatz. Reformulação notacional (Binary-Exponential-
Ladders) da árvore reversa de Collatz padrão, nada estruturalmente
novo. "Condição necessária" da prova é tautológica (o conjunto definido
como quem alcança o ciclo trivial, por definição, alcança o ciclo
trivial). "Condição suficiente" (que excluiria ciclos extras/cadeias
divergentes — todo o conteúdo real) tem furo decisivo: assume que o
predecessor de um elemento mínimo de ciclo hipotético usa o expoente
v=1 especificamente, entre infinitas soluções válidas da própria
fórmula do paper (uma por expoente ímpar v=1,3,5,7,...); só v=1 dá a
contradição alegada, todo v≥3 dá um valor maior (sem contradição
nenhuma). Confirmado computacionalmente (`experiments/E-043-ctuhsk-cycle-proof-check/`)
que é padrão algébrico geral, não acidente do exemplo do paper.
Catalogado em `literature/unverified-proof-claims.md` junto ao Santos
(2018). Verificado com `advisor()` antes de finalizar a análise.

**Item 019 processado (H-044), sem erros — contraste didático com
H-043**: Fu, Liu & Wang ("Emergence of Gamma-Type Upward-Phase
Statistics", arXiv:2606.26811) — qualidade acadêmica alta (afiliação
real, financiamento chinês legítimo). Propõe mecanismo de Poisson para
a distribuição Gamma de N↑; usa a mesma condição de fechamento de
ciclos do CTUHSK, mas aqui os autores afirmam **corretamente** que isso
não prova ausência de ciclos não-triviais. Verificado: E[h]=2/Var(h)=2
(H-001/H-011), Eq.6 exata em 100% dos casos testados (incl. órbita
longa de 27), média de N↑ a ~2% da previsão. θ empírico ~8,5% abaixo do
teórico em nossa escala menor — consistente com o próprio paper, não é
erro. Verificado com `advisor()`.

## Onde estamos

**Setenta hipóteses testadas (H-001 a H-070)**. **H-070**: item 099
(Lodders, "Selection Rules and Channel Structure in a Base–Octave Model
of Collatz Dynamics", arXiv:2604.20181, 60 páginas, não peer-reviewed —
**ALEGAÇÃO DE PROVA COMPLETA**, a mais sofisticada tecnicamente das três
já revisadas). O paper reformula Collatz num modelo "base-octava"
(h=B+8(A-1)), deriva 16 regras de transição entre 8 classes de base e
identifica B=7 (A par) como único canal de crescimento persistente —
tudo isso verificado e CORRETO (16 regras: 31.992 pares testados, 0
falhas; Proposition 8.4 [comprimento do episódio ≤ v2(A_entrada)]:
515.342 episódios, 0 falhas). Mas o Theorem 9.6.8 (confinamento de toda
trajetória à bacia {1,2}) depende do Corollary 9.6.7 (v2(A) deve
decrescer estritamente entre episódios sucessivos de persistência
base-7), apoiado numa enumeração de "22 caminhos de retorno" num sistema
de 128 estados. **Corollary 9.6.7 é falso** — o próprio exemplo citado
pelo paper na Introdução (n=27, "requer substancialmente mais passos que
vizinhos") já o viola (v2 vai de 1 para 3 entre episódios, quando
deveria decrescer); em escala (N até 500.000), 56,7% dos pares de
episódios sucessivos violam a alegação. Ironia notável: o monovariante
proposto falha exatamente no número que o paper usa para motivar a
análise. Ver `hypotheses/H-070-lodders-base-octave-review.md`.

Anteriormente, **sessenta e nove hipóteses testadas (H-001 a H-069)**. **H-069**: item
084 (Mailland & Kosobutskyy, "Modelling the Collatz Problem from a
Jacobsthal Viewpoint", CDS 8(1) 2026, peer-reviewed). Versão pedagógica,
restrita a κ=3, do mesmo framework do item 032 (mesmos autores, ordem
reversa — ver H-063). O framework geral já havia sido verificado
exaustivamente em E-063; este item cobre apenas o conteúdo numérico
específico do paper 084 ainda não testado (árvore geradora completa da
Fig. 1 e as 10 colunas da Fig. 2), em `E-069`, 4 partes, 0 falhas.
Nenhum erro matemático — nota de metodologia própria: uma leitura visual
inicial da Fig. 1 sugeriu incorretamente que os nós 57/229 estariam
ligados a 85 (na verdade vêm de θ=43), provável erro de transcrição da
figura, não do paper. Ver
`hypotheses/H-069-mailland-kosobutskyy-jacobsthal-viewpoint-review.md`.

Anteriormente, **sessenta e oito hipóteses testadas (H-001 a H-068)**. **H-068**:
item 076 (Yun, "A Structural Proof of the Collatz Conjecture via
non-repeating trajectory and Recursive Decay" — **ALEGAÇÃO DE PROVA
COMPLETA**, osf.io, não peer-reviewed). Veredito: **não é uma prova
válida** — mais fraco até que o item 049 (Boyle, H-065). Contém TRÊS
argumentos circulares independentes: (1) gap mais grave — a "função de
posto" `r(x):=min{n:f^(n)(x)=1}` só está definida para x cuja órbita
já atinge 1, presumindo a própria conclusão (demonstrado por analogia
com um mapa que provadamente diverge, cuja função de posto análoga
também fica indefinida — expõe que o "embasamento em ZFC" do Apêndice
A é retórica sobre uma definição vazia); (2) Teorema 6.1 afirma "o
único ponto fixo conhecido é 1" como se isso fosse prova, quando é
exatamente a conclusão apresentada como premissa; (3) argumento de
"compressão informacional" é uma falácia sobre cardinalidades
infinitas. Erro aritmético concreto também encontrado (Eq. 9.8: f(5)
e f(21) calculados com expoentes de 2 errados, resultado alegado nem
é ímpar). Busca computacional (até 2 milhões) não encontra
contraexemplo, mas isso não resgata os argumentos do paper. Ver
`hypotheses/H-068-yun-structural-proof-review.md`.

Anteriormente, **sessenta e sete hipóteses testadas (H-001 a H-067)**. **H-067**:
item 074 (Carelli, "Loop Termination and Generalized Collatz
Sequences", arXiv:2605.15094, CISPA Helmholtz Center, financiamento
ERC). Paper de ciência da computação teórica (STACS/LICS/CAV/ICALP)
— conecta decidibilidade de terminação de loops lineares de uma
variável a "sequências de Collatz generalizadas" (framework
Matthews/Watts/Möller). Não tenta resolver a conjectura clássica.
Resultado condicional honesto: termination é decidível SE a
"Reachability Conjecture" vale — provada apenas para d=2, com d>2
explicitamente em aberto (Exemplo 19 dá uma instância concreta não
resolvida). Mecanismo algébrico central (ponto fixo único por classe
residual) verificado algebricamente e empiricamente (~20.000
trajetórias, 0 exceções). Exemplo 19 testado até n=2.000.000 sem
contraexemplo (não resolve a questão aberta, só não a refuta na faixa
testada). Revisão escopada ao conteúdo Collatz-relevante (a maquinaria
geral de SLCs fica fora do escopo, como em H-060). Nenhum erro
encontrado. Ver
`hypotheses/H-067-carelli-loop-termination-review.md`.

Anteriormente, **sessenta e seis hipóteses testadas (H-001 a H-066)**. **H-066**:
item 057/089 (Reyes Jiménez, "A Fibonacci theorem for Collatz
trajectories via modular graph structure", arXiv:2606.02621).
Diferente da maioria dos papers desta fila, é **pesquisa matemática
genuína e tecnicamente sofisticada** (doutorando UPC Barcelona) — não
uma tentativa amadora nem alegação de prova. Prova um resultado
combinatório EXATO e incondicional sobre um objeto finito (o grafo de
transição mod 6 do mapa acelerado): exatamente F(m+1) dos 2^m inteiros
ímpares em {1,...,2^m} evitam o resíduo 4 mod 6 nos passos 2..m — via
uma "lacuna espectral" φ/2<1 entre raios espectrais φ (razão áurea) e
2. Onze partes verificadas computacionalmente, incluindo reprodução
exata da contagem de Fibonacci por força bruta para m=1 a 22
(F(2)=1 até F(23)=28.657). Conexão com trabalho próprio: H-027
(2026-07-13) já havia verificado independentemente a mesma tabela de
transição mod 6 (Proposição 2.8) antes de conhecermos este paper.
Nenhum erro do paper encontrado (2 bugs de indexação/normalização no
próprio script de verificação, corrigidos). Ver
`hypotheses/H-066-reyes-jimenez-fibonacci-review.md`.

Anteriormente, **sessenta e cinco hipóteses testadas (H-001 a H-065)**. **H-065**:
item 049 (Boyle, "The Collatz Conjecture is True" — **ALEGAÇÃO DE
PROVA COMPLETA**, rxiverse.org, não peer-reviewed). Veredito: **não é
uma prova válida**. Gap fatal localizado no Lemma 4.2 ("a sequência
gerada por n+1 não diverge"): deriva `e=2/3, o=1/3` sob a hipótese de
"n aleatório" (Teorema 3.2 — argumento de densidade/ensemble sobre
paridade), depois substitui esses valores diretamente numa alegação
sobre UMA trajetória hipotética específica e fixa — a clássica
falácia do "argumento do passeio aleatório" (heurística útil para
intuição, não prova; a própria referência citada para a técnica é um
post de fórum, não uma prova publicada). Demonstração quantitativa: a
fração de passos pares realizada por trajetórias individuais completas
(3.000 amostras) tem desvio-padrão 0,031 e 10,2% desviam de 2/3 por
mais de 0,05 — "2/3" é média de ensemble, não restrição por
trajetória. Gap secundário: Lemma 4.3 não trata o caso `n+1` ímpar na
fatoração diofantina (a conclusão numérica sobrevive, a demonstração
tem lacuna). Partes verificáveis (exclusão de ciclos curtos, aritmética
da série geométrica) estão corretas — o problema é estrutural/lógico,
não erro de cálculo. Ver
`hypotheses/H-065-boyle-collatz-proof-review.md`.

Anteriormente, **sessenta e quatro hipóteses testadas (H-001 a H-064)**. **H-064**:
item 038 (Kayadibi, "A Modular Classification of Pre-Descent Resistance
in Accelerated Odd Collatz Dynamics", SSRN 6918258) — predecessor mais
simples do item 015 (H-058, mesma autora), referenciado lá como `[11]`.
Define a "espinha de resistência modular" `S_m={n: n≡-1 mod 2^m}` e
prova 4 fatos algébricos sobre ela (valuation, expansão de primeiro
passo, persistência, cota inferior determinística) — todos confirmados.
Reprodução computacional **completa** (não amostrada) em `N=10⁷,
L=5000`, idêntica à do próprio paper: 4.999.999 descidas, 0
não-resolvidos, os dois casos extremos citados (τ=155 em n=8.088.063;
ρ=3.033.050,2686 em n=6.631.675), estatísticas módulo 64, e as Tabelas
2-3 completas (40 valores, m=6..15) — tudo bate exatamente. Rodou em
~9s (framework 100% determinístico, sem amostragem aleatória). Nenhum
erro encontrado. Ver
`hypotheses/H-064-kayadibi-pre-descent-resistance-review.md`.

Anteriormente, item 036 (Damnjanovic, Ha & Stevanovic, "Upper Bounds for the Laplacian
Spectral Radius", arXiv:2606.14550) processado e descartado: **falso-
positivo puro de busca por sobrenome** — as 5 menções a "Collatz" no
texto são todas "Collatz–Wielandt comparison" (ferramenta de teoria de
Perron-Frobenius, sem relação com a conjectura 3x+1; Lothar Collatz
contribuiu para ambas, mas são resultados distintos). Sem H-0XX/E-0XX
próprio — nada do escopo deste projeto para verificar. Ver anotação
`*****` em `literature/papers/INDEX.md`.

**Sessenta e três hipóteses testadas (H-001 a H-063)**. **H-063**: item
032 (Kosobutskyy & Mailland, "Jacobsthal Trees and Generalized κx±1
Transformations", Communications in Advanced Mathematical Sciences
9(2), peer-reviewed). Paper estrutural/notacional — generaliza a árvore
inversa de Collatz para `κx±1` (κ ímpar qualquer) via "números de
Jacobsthal generalizados"; explícito que não visa provar a conjectura
clássica. O "Teorema da Periodicidade" central é exatamente o fato
padrão de teoria dos números de que `T_κ` = ordem multiplicativa de 2
mód κ — confirmado para κ=1..199 e byte-a-byte contra um número de 52
dígitos (κ=181) da Tabela 2.2. Todas as 8 partes testadas (definições,
teorema central, 2 tabelas, propriedades de unicidade/recorrência,
pontos-atratores) sem falhas. Achado menor: o Remark 1.7 (prosa) diz
PA={1,27,35} para κ=181, mas a própria Tabela 2.6 (dados) já mostra que
`q0=1` diverge sob κ=181 — inconsistência textual entre seções do
mesmo paper, não erro matemático. Relacionado ao item 084 (mesmos
autores, versão pedagógica restrita a κ=3, revisão cross-referenciada
em H-069 em vez de duplicada). Ver
`hypotheses/H-063-jacobsthal-trees-review.md`.

Anteriormente, **sessenta e duas hipóteses testadas (H-001 a H-062)**. **H-062**:
item 031 (Melas & Poulios, "Predicting Extreme Stopping Time Behavior
in the Collatz System", Journal of Dynamics and Games/AIMS,
peer-reviewed, Univ. de Atenas). Paper estatístico (logit + árvore de
decisão) para prever tempo de parada extremo, não para provar Collatz
(explícito: "does not solve the Collatz conjecture"). Identidade
logarítmica fundamental confirmada exatamente (via `Fraction`); as 6
contagens de densidade citadas (janelas de 10.000 inteiros em
potências de 10 e de 3, até 10¹⁵) reproduzidas de forma EXATA e
determinística — todas batem. Modelos logit/árvore não reproduzidos
byte-a-byte (dependem de amostragem aleatória sem semente/biblioteca
totalmente especificada — limitação de reprodutibilidade, não erro).
Ver `hypotheses/H-062-melas-poulios-stopping-time-review.md`.

Anteriormente, **sessenta e uma hipóteses testadas (H-001 a H-061)**. **H-061**: item
029 (Alic, "Collatz Progressions Reframed", IEEE Access,
peer-reviewed). Paper de algoritmos/engenharia (Diretor do Photonics
Lab, Qualcomm Institute/UCSD) — não faz alegação matemática sobre
Collatz (explícito: "the conjecture remains unproven"). Propõe P2ER
(representar n como vetor de expoentes de potências de 2), com o passo
ímpar como concatenação+consolidação via carry binário e o passo par
como deslocamento em bloco. Álgebra central verificada correta (20.000
passos, 500 trajetórias até 4000 bits, mais todos os exemplos
numéricos do próprio paper reproduzidos exatamente). "Computação
recorde" (2^1.024.001-1, 13,8 milhões de passos) não reproduzida —
inviável nesta sessão. Ver `hypotheses/H-061-alic-p2er-review.md`.

Anteriormente, **sessenta hipóteses testadas (H-001 a H-060)**. **H-060**: item 028
(Csikos, "A Continuous Multi-Component Measure of Directed Acyclicity
(DAG-ness)", arXiv:2606.22205) — **não é um paper sobre Collatz**, é
teoria de grafos/ciência de redes (Binghamton + Moravian University);
Collatz aparece só como exemplo ilustrativo de meia página. Revisão
limitada a esse trecho (o framework geral de teoria de grafos está
fora do escopo do projeto). Achado: o texto descreve o ciclo trivial
como "1→2→4→1", mas pelas arestas reais do próprio mapa `T(n)` que
definem (`T(1)=4,T(4)=2,T(2)=1`) a direção correta é "1→4→2→1" — erro
de descrição textual, sem consequência nos cálculos numéricos do
paper. Ver `hypotheses/H-060-csikos-dag-ness-review.md`.

Anteriormente, **cinquenta e nove hipóteses testadas (H-001 a H-059)**. **H-059**:
item 021 (Amirian & Amirian, "A Generalization of 3x+1 Problem to
3x+4y+1", SSRN 6993335). Paper curto (3 páginas, sem provas), propõe
`x_{i+1}=3x_i+4y+1` (ímpar) / `x_i/2-y` (par) como "generalização" de
Collatz. Achado: a mudança de variável `z=x+2y` transforma o mapa
proposto EXATAMENTE no Collatz padrão em `z` (mesma fórmula, símbolo a
símbolo) — não é uma generalização, é o mesmo problema reparametrizado.
Consequência quantificada: a varredura numérica alegada ("~640 bilhões
de pontos") cobre, na melhor das hipóteses, ~2,4 milhões de instâncias
distintas de Collatz padrão, já coberto por verificações exaustivas
publicadas (`2^68`-`2^71`). Ver
`hypotheses/H-059-amirian-3x4y1-review.md`.

Anteriormente, **cinquenta e oito hipóteses testadas (H-001 a H-058)**. Retomamos a
tarefa de revisar todos os papers já baixados (não só a série Ruiz
Castillo) até esgotar a fila — 15 itens identificados como baixados
mas não processados (item 014 acabou sendo um já revisado por engano
de leitura do índice, ver H-042; os outros 14 são novos).

**H-058**: item 015 (Kayadibi, "Canonical Shells and Residue-Cover
Trees in a Conditional First-Descent Approach to the Collatz
Problem", Victoria University Melbourne). Framework condicional denso
(45 páginas) que reduz "primeira descida universal" a duas condições
estruturais não provadas em geral (dyadic gap diofantino + fechamento
de "residue-cover trees"), verificadas só computacionalmente em faixa
finita pelo próprio paper. Honestidade epistêmica exemplar — Conclusão
explícita: "does NOT prove the Collatz conjecture unconditionally...
remain finite evidence only." Toda a maquinaria algébrica PROVADA
(Persistence Identity, First-Exit Formula, Certified Exact Descent,
Cumulative Affine Formula, Residue Cylinder) confirmada sem exceção
contra simulação real de Collatz, incluindo reprodução exata dos
valores da Tabela 1 do próprio paper (convergentes de log₂3:
5,41,306,15601; K_m: 8,65,485,24727). Nenhum erro encontrado. Constrói
sobre dois papers anteriores da mesma autora — um deles é o item 038
desta coleção, ainda não revisado. Ver
`hypotheses/H-058-kayadibi-canonical-shells-review.md`.

Anteriormente, **cinquenta e sete hipóteses testadas (H-001 a H-057)**. **H-057**:
testamos o candidato #1 do backlog (seção 6) — conectar nosso muro
combinatório de ciclos (H-009/H-034) com a técnica clássica de exclusão
via frações contínuas de log₂(3) (Steiner/Simons/de Weger/Hercher).
Reaproveitando `compositions`/`candidate_n0`/`check_self_consistency` de
E-034: convergentes + semiconvergentes de log₂(3) (necessários porque é
aproximação unilateral) dão 12 candidatos `(a,S)` até a≤2000. Nenhum
ciclo novo — para a=3,5,17 (nosso alcance), resultado mais forte que
H-034: nenhuma composição sequer produz um n₀ inteiro no S ótimo (não só
"nenhum autoconsistente"). Corrigimos nossa própria citação desatualizada
"Simons & de Weger, a≤68" para o bound atual — **Hercher (2023,
arXiv:2201.00406): a≤91** — verificado via WebSearch/WebFetch antes de
escrever qualquer código, não de memória. **Autocorreção via `advisor()`**
antes de fechar: a primeira versão do experimento afirmava "menor excesso
L(a,S) ⟹ menor n₀ possível" — invertido. Para a composição que minimiza
n₀ (forma fechada, confirmada por enumeração exaustiva): n0_min≈1/(L·ln2),
ou seja, menor excesso ⟹ n0_min MAIOR (cresce de 3,8 em a=3 até ~1069 em
a=1636). Mas isso é só o mínimo sobre composições — uma composição
"ruim" no mesmo par (a=306,S=485) dá n₀~10²⁵ em vez de ~978. L(a,S)
pequeno mede dificuldade ANALÍTICA de exclusão (cotas de Baker), não
tamanho de ciclo. Conexão de projeto (não matemática nova): L(a,S) é
exatamente a mesma "deuda residual" L_k(n) de todos os papers de Ruiz
Castillo revisados (H-052 a H-056), aplicada a um par abstrato em vez de
uma trajetória real. Ver `hypotheses/H-057-continued-fraction-cycle-exclusion.md`
e `BACKLOG.md` seção 1/seção 6 item 1.

Anteriormente, **cinquenta e seis hipóteses testadas (H-001 a H-056)**. **H-056**:
sétimo paper de Ruiz Castillo (item 026, "Grandes Desviaciones
Residuales", localizado via Zenodo DOI 10.5281/zenodo.20767811 —
ResearchGate bloqueava) — **segundo erro real** encontrado na série
(após item 013/H-053). Seções 1-5 (identidades concretas, drift
residual negativo, cota de Chernoff do Teorema 5.2) inteiramente
corretas. Erro: a Proposición 3.4 (já provada) mostra que I_RC(x) —
definida via o evento de cauda UNILATERAL {L_k/k≥x} — é monótona
não-decrescente, o que força I_RC(x)=0 para todo x abaixo do drift
típico x*=log₂3−2, não só nesse ponto. Mas a Figura 1, a Conjetura 7.3
("zero único em x*") e a Conjetura 7.5 (sup_{t∈ℝ} irrestrito — as três
mutuamente consistentes entre si) descrevem I_RC como uma função
BILATERAL em V, positiva nos dois lados de x* — contradizendo a
Proposición 3.4. Confirmado por três métodos independentes (fórmula
restrita a t≥0, Monte Carlo, Binomial Negativa exata). Não é alegação
de prova de Collatz (negado 2x no texto) nem erro de cálculo isolado —
conjectura (Seção 7) inconsistente com proposição já demonstrada no
mesmo texto (Seção 3), erro contido (Conclusión não depende disso).
Nota de integridade dupla: (a) confirmado diretamente contra o PDF que
um rascunho anterior atribuiu errado a restrição de sinal correta à
Conjetura 7.5 (na verdade irrestrita, mesmo erro que 7.3/Figura 1) —
corrigido; (b) bug de unpacking de tupla no código de verificação
relatado como corrigido em sessão anterior, sem histórico de git para
confirmar a forma exata — registrado como relatado, não re-verificado.
Ver `hypotheses/H-056...md` e `BACKLOG.md` item 026.

Anteriormente, **cinquenta e cinco hipóteses testadas (H-001 a
H-055)**. **H-055**:
sexto paper de Ruiz Castillo (item 020, "Principio Variacional
Residual") — sem erros. Unifica deuda residual, drift, presión,
entropía, grandes desviaciones e dimensión sob um único princípio
variacional. Identidades Collatz-específicas concretas confirmadas
(mesma quantidade de sempre); aparato de análise convexa abstrata
(sup de afins é convexo, Legendre-Fenchel) é matemática padrão
corretamente aplicada, confirmado via verificação toy não-Collatz-
específica. Onde a derivação é só formal, o texto admite isso
explicitamente. Todo resultado aberto rotulado "Conjetura". Sexto
paper consecutivo sem erro real (única exceção: item 013/H-053).
Processando os ~16 papers de Ruiz Castillo em lote sequencial.

**Achado-chave para a síntese final (item 055, leitura contextual, sem
H-0XX próprio)**: lido o paper de filosofia "Platonismo y realismo en
matemáticas y física" (Ruiz Castillo & Moreno Sanabria, 2026, revista
*Diotima*, 18 páginas) — não é um paper de Collatz, é filosofia da
matemática (platonismo de Gödel/Penrose vs. realismo científico,
hipótese do universo matemático de Tegmark, efetividade irrazoável de
Wigner). Ele se revela explicitamente **platonista/realista**: acredita
que estruturas matemáticas têm existência objetiva e que teorias
físicas descrevem uma realidade genuína. Crucialmente, o próprio paper
descreve seu trabalho em Collatz como "un modelo conceptual que ilustra
la profunda interrelación entre lo discreto y lo continuo, lo
determinista y lo caótico, lo formal y lo físico" — ou seja, **Collatz
não é o objetivo, é um estudo de caso filosófico**. Isso explica o
padrão observado em H-039/H-050/H-052/H-053/H-054/H-055: cada paper
aplica UM conceito clássico diferente (drift, pressão, Gibbs, TCL,
operador de transferência, princípio variacional) à MESMA quantidade
L_k(n), não como tentativa de resolver Collatz, mas como mais um "ponto
de dados" demonstrando que formalismos consagrados (originalmente da
física/mecânica estatística) "também se aplicam" a um problema
aritmético acessível — evidência, para sua tese platonista, de que
estruturas matemáticas revelam algo real. Isso também explica a
honestidade epistêmica consistente (rotular "Conjetura" vs "Teorema",
disclaimers explícitos de não-prova): como o objetivo real nunca foi
provar Collatz, admitir isso não custa nada ao propósito filosófico
mais profundo. Formação do autor: doutorado em Física e Matemática,
mas também licenciado em Ensino de Matemática e Física — a tese de
doutorado (citada em todos os outros papers) usa o "Enfoque
Ontosemiótico" (EOS), um referencial de EDUCAÇÃO matemática, sugerindo
que a linha de pesquisa nasce da didática/filosofia da matemática, não
de teoria dos números pura. Material direto para task #21 (síntese
final do programa Ruiz Castillo).

Anteriormente, **cinquenta e quatro hipóteses testadas (H-001 a
H-054)**. **H-054**: quinto paper de Ruiz Castillo (item 017, "Medidas
de Gibbs Residuales") — sem erros, volta ao padrão elementar mas
correto após o erro do item anterior. Todas as identidades concretas
(interpretação logarítmica, identidade fundamental S_kφ=−L,
semiconjugação, partição por cilindros, equivalência Gibbs-residual)
confirmadas. Todo resultado em aberto (cuasi-Bernoulli,
Gibbs-implica-equilíbrio, dualidade grandes desvios, fórmula de
dimensão) honestamente rotulado "Conjetura". Sem consequência empírica
diretamente testável.

Anteriormente, **cinquenta e três hipóteses testadas (H-001 a H-053)**.
**H-053**: quarto paper de Ruiz Castillo (item 013, "Operador de
Transferencia Residual") — **primeiro erro real** encontrado nesta
série de 4 papers do autor. Proposición 5.3 afirma lim_{t→∞}L_t(1)=0,
mas sua própria demonstração deriva L_t(1)=e^{(log₂3−1)t}/(1−e^{-t}) e
observa corretamente que isso "crece exponencialmente" — o oposto
exato do enunciado (verificado numericamente: L_t(1) vai de 2,84 a
6,4×10⁵⁰ entre t=1 e t=200). `advisor()` consultado: é uma
inconsistência enunciado-vs-demonstração (mesma categoria do erro de
rotulagem Pratiher/H-037), não erro de cálculo — o autor deriva a
assintótica certa, só não atualizou o enunciado formal. Erro contido
(pertence a um cálculo preliminar da Seção 5, nada posterior depende
dele). Resto do paper (fórmula de Gelfand, conjecturas 6.6/7.1/8.4
honestamente rotuladas) correto.

Anteriormente, **cinquenta e duas hipóteses testadas (H-001 a H-052)**.
**H-052**: terceiro paper de Ruiz Castillo (item 010, "Teorema Central
del Límite Residual") — resultado central honestamente rotulado
"Conjetura 4.2" no corpo apesar do título dizer "Teorema"; identidades
algébricas corretas mas triviais. Testamos a consequência empírica
(normalidade assintótica de Z_k) em trajetórias reais de Collatz até
k=300: variância estabiliza perto de 2, assimetria→0, curtose→3 —
previsão empiricamente plausível, mesmo sem as hipóteses técnicas
(medida de Gibbs residual, brecha espectral) construídas no paper.
Nota de integridade: bug de amostragem no nosso código (processo
ficou preso 17 min por contaminação de trajetórias curtas) corrigido
antes de reportar.

Anteriormente, **cinquenta e uma hipóteses testadas (H-001 a H-051)**.
**H-051**: nota curta de Olgac (item 009) — sem conteúdo específico de
Collatz verificável (a única afirmação sobre Collatz é tautológica); o
resto é sobre a Conjectura de Goldbach, fora do escopo, e não rigoroso
o suficiente para avaliar.

Anteriormente, **cinquenta hipóteses testadas (H-001 a H-050)**. **H-050**: segundo
paper de Ruiz Castillo (item 008) — matemática elementar correta
(mesma "equação de ciclo" já vista em H-044/H-045, dressed em
terminologia própria), mas zero verificação numérica real (mesmo
padrão do primeiro, H-039). 75% autocitação, revelando ~12 outros
papers quase idênticos do mesmo autor ainda não processados. Provável
que os próximos Ruiz Castillo (010, 013, 017, 020) sigam o mesmo padrão.

Anteriormente, **quarenta e nove hipóteses testadas (H-001 a H-049)**. **H-049**: paper
de Hikawa (item 007) — sem erros, puramente combinatório sobre vetores
de paridade finitos, explicitamente independente da verdade/falsidade
do Collatz. Teoremas centrais e tabelas numéricas confirmados
exatamente.

Anteriormente, **quarenta e oito hipóteses testadas (H-001 a H-048)**. **H-048**: paper
de Anthony (item 006) — sem erros, honestidade epistêmica exemplar.
Muito aparato sofisticado (equação P de Riemann, monodromia, digamma,
hipergeometria) que o próprio paper trata como analogia decorativa; o
"Collapse Theorem" (14.1) é explicitamente rotulado condicional, não
prova. Autor corrige a própria reivindicação equivocada dentro do
texto. Todas as reivindicações testadas confirmadas corretas.

Anteriormente, **quarenta e sete hipóteses testadas (H-001 a H-047)**. **H-047**: paper
de Gilbert (item 003) — sem erros, alta qualidade. Conjugação explícita
entre o grafo de Collatz podado e todos os inteiros não-nulos (sinal
codifica classe residual mod 3). Todos os teoremas testados corretos,
incluindo a conexão com OEIS A254046 (WebFetch bloqueia oeis.org, mas
`curl` com User-Agent de navegador funciona — ver
`feedback_oeis_access_method.md`).

Anteriormente, **quarenta e seis hipóteses testadas (H-001 a H-046)**. **H-046**: paper
de Adnan & Dar (item 002) — não alega provar nada, propõe extensão ad
hoc do Collatz a decimais via "paridade do último dígito". Aritmética
correta, mas a regra não é definida fora de um subconjunto contável de
(0,1), e a divergência observada é artefato trivial sem mecanismo
estrutural análogo ao Collatz real.

Anteriormente, **quarenta e cinco hipóteses testadas (H-001 a H-045)**. **H-045**
(achado importante): paper de Abdullah Mohammed (item 011, baixado
manualmente pelo diretor científico) alega prova completa da
Conjectura de Collatz via sieve geométrico + Teorema de Baker. Furo:
a equação de ciclo do próprio paper força M/P→log₂(3)≈1,585 para um
ciclo real, mas a Eq.48 usa M≈2P (expectativa ERGÓDICA/média de número
genérico, não a restrição de um ciclo) — checagem vazia. Mesma
categoria de erro do CTUHSK (H-043): confundir "em média"/"quase todo"
com afirmação universal sobre o objeto hipotético específico.
Catalogado em `literature/unverified-proof-claims.md`.

Anteriormente, **quarenta e quatro hipóteses testadas (H-001 a H-044)**. **H-044**:
paper de Fu/Liu/Wang sobre estatística Gamma de N↑ — sem erros, ver
seção "Coleção de papers" acima.

Anteriormente, **quarenta e três hipóteses testadas (H-001 a H-043)**. **H-039 a H-043**
são revisões da coleção de papers do Google Scholar (ver seção "Coleção
de papers" acima para o detalhe de cada uma) — destaque para **H-043**
(achado importante): o paper #016 (Halemane, "CTUHSK Theorem") alega uma
**prova completa** da Conjectura de Collatz, mesma categoria do PDF do
Santos já catalogado. Furo lógico encontrado na condição suficiente da
prova: o argumento de redução ao absurdo fixa arbitrariamente um
expoente (v=1) entre infinitas escolhas válidas ao calcular o
predecessor de um elemento mínimo de um ciclo hipotético — só essa
escolha específica gera a contradição alegada; qualquer outro expoente
ímpar (v≥3) não gera contradição nenhuma. Confirmado computacionalmente
que isso é um padrão algébrico geral, não um acidente do exemplo do
paper. Catalogado também em `literature/unverified-proof-claims.md`.

Anteriormente, **trinta e oito hipóteses testadas (H-001 a H-038)**. **H-038**: uma
segunda resposta da mesma IA externa (mesmo "Project PHI"/H-036)
propôs um "campo vetorial" Δ(n)=Φ(T(n))-Φ(n) em embedding rico — a
generalização não-linear da ideia já descartada. Testei com mutual
information (não só correlação linear como H-025): achei dependência
real (peso de Hamming, janelas de bits vs segunda valuação, z-score até
~2448). Mas um experimento de controle (substituir 3n+1 por 5n+1, 7n+3,
9n+5 — nada a ver com Collatz) mostrou que a MESMA classe de
dependência aparece nessas transformações sintéticas — é um fenômeno
genérico de propagação de carry em aritmética binária (popcount(m) =
popcount(3n+1) sempre, verificado exato), não estrutura nova do
Collatz. Estende H-025 por um método diferente, mesma conclusão de
fundo.

Anteriormente, **trinta e sete hipóteses testadas (H-001 a H-037)**. As três últimas
(2026-07-13, depois de H-034): **H-035** checou se a obstrução de H-024
(densidade por-nó D(v) exige precisão 3-ádica ilimitada) se aplica à
Conjectura 10.4 de Pratiher (α≈0,9762) — resposta: não, são objetos
categoricamente diferentes (D(v) é por-nó; Freq_r(N) de Pratiher é média
de conjunto). **H-036**: ao tentar escrever uma síntese própria ("uma
obstrução, N confirmações independentes") a partir de H-013/H-024/H-025/
H-026/H-030/H-032, a checagem de novidade revelou que essa narrativa
geral já é o resultado central de um survey de 216 páginas do mesmo
autor do paper usado em H-030 (Chang 2026, arXiv:2603.11066, "Paradigm
Exhaustion Theorem", 29 paradigmas testados) — recalibrado com
honestidade em vez de reivindicado como nosso. **H-037** (importante):
ao investigar se α de Pratiher seria derivável por equidistribuição,
um argumento de paridade (mecanismo idêntico a H-012) revelou que a
forma dominante que ele relata ('a', expoente ímpar) é matematicamente
impossível como classe de massa positiva — só expoentes pares podem
dominar. Verificação computacional encontrou correspondência **exata**
entre os números relatados por Pratiher e os corretos, sob um
deslocamento de rótulo de exatamente 1 posição no ciclo de 6 formas:
os números do paper (~0,9762/~0,0238) parecem certos, a atribuição de
qual forma carrega cada número parece ter um erro off-by-one.
Validado cruzado contra nossos próprios dados de H-013 (medidos
independentemente, antes de conhecer este paper) — bate.

Levantamento inicial da literatura concluído (ver `literature/00-index.md`).
Mais um PDF externo e
quatro listas de ideias de outras IAs revisadas criticamente (a maioria dos
itens especulativos — sem ponte concreta — descartada conscientemente; ver
`literature/external-ideas-review.md`). **H-024**: prova computacional de
que a densidade do subárvore reverso exige precisão 3-ádica infinita,
fechando com clareza a via "operador de transferência de dimensão finita"
para H-013. **H-025**: busca de invariantes lineares em bits refutada com
mecanismo identificado (toda correlação se reduz ao valor de a, já
conhecido, e ao bias clássico de carry em adição binária). **H-026**:
taxa de divergência da aproximação de memória finita parece independer de
K (sinal real mas não estatisticamente robusto). **H-008 agora RESOLVIDA
POR COMPLETO** (H-022 + H-027 novo): a classe 4 mod9 está totalmente
excluída de recordistas, com prova — H-027 fechou a metade par como
corolário direto de H-007 (na verdade válido para toda a classe mais
ampla N≡4 mod6), verificado sem exceção em 500.000 casos. **H-028**:
consolidação via CRT de H-007+H-014+H-022+H-027 mod 72 — 45 de 72
resíduos (62,5%) provavelmente excluídos, zero violações contra os 148
recordistas reais. **Checagem de novidade feita (importante, honesta)**:
2 dos 4 ingredientes (mod3, mod8) já são folclore conhecido e usado pela
comunidade prática de busca de recordistas (`cuda-collatz` documenta
ambos quase literalmente), cuja técnica genérica de sieve provavelmente já
supera nossos 62,5% de exclusão computacionalmente. H-028 reclassificado
de "candidato forte a paper" para consolidação majoritariamente já
conhecida — só H-022 (mod9) permanece como possível peça nova, não
confirmada como inédita. Ver seção "Checagem de novidade" em H-028.md.
Também lido e catalogado o paper de Winkler (2026, arXiv:1709.03385) sobre
"coefficient stopping time" — tópico diferente, não resolve a dúvida de
H-022. **H-029**: checagem rápida (não profunda) mostra que a classe
1 mod6 (única sem exclusão) não tem sub-estrutura óbvia até mod48 — sem
motivo para insistir aí sem ideia algébrica nova. **H-030**: lido e
verificado independentemente o paper de Chang (2026, arXiv:2603.25753,
"one-bit orbit mixing") — três lemas centrais confirmados sem exceção
(pegos 2 bugs próprios no processo, corrigidos antes de reportar).
Conexão real com H-024: a "Rota A" do paper trava na mesma obstrução de
resolução finita insuficiente. Extensão com nossos 148 recordistas reais
mostrou desvio ~0,61 vs 0,5 esperado, mas identificamos e neutralizamos
corretamente uma armadilha de pseudo-replicação (órbitas de recordistas
colidem, confirmado 8/45 pares) — resultado consistente com o que o
próprio paper já documenta, não achado novo. Também lido (e descartado
por hallucinação do resumo automático, não por conteúdo real) o paper de
Pratiher (2026) sobre finite state decomposition — tópico diferente do
nosso, catalogado como lição de sempre checar a fonte primária. Também
lidos e catalogados (sem conexão nova): Angermund (2025, cálculo de dois
operadores), Bouhamidi (2026, família modulo 2^p+2^q), Carelli (2026,
decidibilidade de terminação de loops), Yolcu/Aaronson/Heule (2021-2022,
reescrita de strings — paper respeitado, área distante do nosso toolkit).
**H-031**: varredura sistemática de primos nunca testados (5,7,11,13,17,
19,23) e potências maiores de 3 (27,81) contra os 148 recordistas reais —
nenhuma exclusão nova encontrada (poucos candidatos em mod81 confirmados
como ruído estatístico via cálculo de Poisson antes de descartar).
Reforça que a família de exclusão conhecida (só primos 2 e 3) está
completa nos moduli pequenos. **Conexão real e verificada** entre H-027 e
Reyes Jiménez (2026, arXiv:2606.02621): o grafo de transição mod6 dele
(resíduo 4→{2,5}) é exatamente o mecanismo algébrico da nossa prova —
duas investigações independentes convergindo na mesma estrutura,
documentado em H-027.md. Diretor científico perguntou sobre conexões
geométricas/dimensionais — investigado a fundo (Kionke, Alvarado, Siegel,
Honarvar Shakibaei Asli): generalizar para dimensão maior (Z^n, inteiros
de Gauss) **piora** o comportamento em vez de ajudar, com explicação
aritmética limpa derivada (3<2² dá contração no caso clássico; 5>2² dá
expansão no análogo de Gauss). **H-032**: testada e refutada a conexão
entre frações contínuas de log₂(3) (a ferramenta clássica de limites de
ciclo) e a anomalia de H-013 — sem correlação. **H-033**: estendida a
verificação empírica do problema aberto de Chang (H-030) usando os 8
maiores recordistas reais (3× mais observações por órbita que o testado
no paper original) — desvio persiste (~0,55-0,64), consistente com
H-021/H-030, sem resolver nem contradizer o problema aberto original.
**H-034**: diretor científico trouxe transcrição de vídeo informal que
redescobriu a técnica clássica de equação de ciclo (Steiner/Simons/de
Weger). Achado específico do vídeo (n=13 quase fecha ciclo com 3 mult+5
div) **refutado tecnicamente** com a fórmula correta (nenhum candidato
inteiro existe para essa configuração). H-009 **estendido de a=14 para
a=16** (janela mais estreita, S=S_min). Parede combinatória quantificada
com precisão (bilhões de composições por par a partir de a≈20) — explica
por que Simons & de Weger precisaram de frações contínuas de log₂(3),
não só mais poder computacional, para chegar a a=68.
## Avaliação estratégica (2026-07-13, importante)

Depois de consolidar a família de exclusão (H-028) e investigar sua
novidade a fundo, cheguei a uma conclusão honesta que muda a expectativa
sobre "encontrar algo importante para publicar" nesta linha específica:
**H-022 (mod9, nossa peça mais nova) é, na prática, uma instância de
"colisão de caminhos"** — M's órbita passa por N depois de exatamente 5
passos. Isso é *precisamente* o que a técnica genérica de sieve já usada
por caçadores de recordistas (`cuda-collatz`: "checks whether paths come
together...") já detecta e explora computacionalmente, mesmo sem a fórmula
fechada escrita em lugar nenhum. Ou seja: mesmo nossa melhor peça é, na
melhor das hipóteses, uma instância elegante e provada de um fenômeno já
conhecido — não uma descoberta de algo novo na prática. Ver nota em
`H-022-mod9-multiplicative-exclusion.md`.

Combinado com H-029 (a única classe sem exclusão, 1 mod6, não mostra
sub-estrutura óbvia até mod48), a conclusão honesta é: **a linha de
"exclusão de recordistas por classe residual" está substancialmente
esgotada** — não há mais um caminho óbvio daqui para um resultado
genuinamente novo sobre Collatz por essa via específica. Isso não
significa parar o loop de pesquisa (instrução permanente do diretor
científico), mas sim que a próxima iteração produtiva provavelmente
precisa de um ângulo diferente (não mais "achar mais uma classe mod k
excluída").

**Resultado central do projeto**: recordistas reais
de stopping time nunca são ≡2 mod 3 (exceto o caso trivial n=2) — confirmado
empiricamente (H-004, n=148, p<10^-13) e **provado algebricamente** (H-007).
Generalizamos a técnica de exclusão por empate (H-014→H-015): 2374 classes
residuais mod 2^d excluídas, 69.3% de mod 2^16. **H-008 (mod 9) agora
parcialmente resolvida**: H-022 provou a metade ímpar da classe 4 mod 9 via
uma técnica multiplicativa nova; metade par segue aberta. A lista completa
de brainstorm do modelo Fable sobre padrões binários (H-012 a H-021) foi
**totalmente testada**, incluindo um mecanismo qualitativo (Galton-Watson)
para a anomalia de H-013 (ainda sem fórmula fechada) e quatro confirmações
teóricas precisas no estilo "derivar → confirmar" (H-010, H-011, H-017,
H-023 — Lei de Benford, inspirada por um vídeo trazido pelo diretor
científico). Backlog em `BACKLOG.md`. **Duas tarefas pendentes** (mesma
regra para as duas — só fazer quando o diretor científico pedir
explicitamente, por último; ele pediu para ser lembrado): (1) escrever
um paper curto apontando os erros do PDF de Santos 2018
(`BACKLOG.md` item 5); (2) escrever um paper curto apontando o erro de
rotulagem off-by-one encontrado na Conjectura 10.4 de Pratiher 2026
(`BACKLOG.md` item 7, análise pronta em H-037/E-037).

## O que o levantamento estabeleceu

- Não existe prova aceita. Resultado mais forte e rigoroso: Tao (2019) — quase
  todas as órbitas atingem valores quase limitados (afirmação de densidade, não a
  conjectura completa).
- Verificação computacional sem contraexemplo até 2^71 (Barina, 2025).
- Três famílias de abordagem mapeadas: 2-ádica/ergódica, estocástica/heurística
  (Kontorovich–Lagarias), e "provas" completas não verificadas (tratar com
  ceticismo — ver `literature/unverified-proof-claims.md`).
- Obstáculo estrutural comum a todas: nenhum método conhecido certifica que o
  conjunto residual de "sobreviventes" é vazio. Qualquer hipótese nova deveria
  endereçar isso explicitamente ou já nasce redundante com tentativas anteriores.
- Existe um paper metodológico direto sobre colaboração humano-LLM neste problema
  (`literature/resources-and-tools.md`) — reforça que toda hipótese/experimento
  aqui precisa de verificação clara, não "a IA disse que funciona".

## Hipóteses abertas

(nenhuma no momento — ver "Próximos passos" para candidatas)

## Hipóteses confirmadas

- `H-004` — recordistas reais de stopping time (não outliers locais). **Achado
  principal do projeto até agora**: entre os 148 recordistas reais oficiais
  (OEIS A006877/Roosendaal, de n=1 até ~1.47×10^19), 85 são ≡0 mod 3, 62 são
  ≡1 mod 3, e **apenas 1 é ≡2 mod 3** (esperado uniforme: ~49 cada). O único
  caso ≡2 é n=2 (trivial/borda) — excluindo-o, **0 de 147** recordistas
  restantes são ≡2 mod 3. p=5.2×10^-14 (mod 3), 3.2×10^-19 (mod 9), 1.8×10^-22
  (mod 27), todos com amostra válida. **Explicação mecanicista completa em
  H-007** (ver abaixo). Ver `hypotheses/H-004-true-record-holders.md` e
  `experiments/E-004-true-record-holders/README.md`.
  **Nota de integridade**: a análise original usava uma lista de 57
  recordistas reconstruída de memória, com 4 valores incorretos — corrigido
  usando a sequência oficial completa (ver `CORRECTION.md` no experimento).
  O código de busca de recordistas em si sempre esteve correto (validado
  termo a termo contra a fonte oficial).
- `H-007` — **prova** de por que recordistas nunca são ≡2 mod 3 (exceto n=2).
  Teorema: para todo N≡2 mod 3 com N>2, M=(2N−1)/3 é inteiro ímpar menor que N
  cuja órbita passa por N exatamente 2 passos depois (M→2N→N), logo
  total_stopping_time(M) = total_stopping_time(N)+2 — N nunca pode ser
  recordista. N=2 é a única exceção porque M colapsaria em 1 (estado
  terminal, fora da recursão normal). Verificado sem exceção em 333.332 casos
  até 1M. Fecha completamente o achado de H-004 — deixa de ser um padrão
  empírico sem explicação e passa a ser teorema provado. Ver
  `hypotheses/H-007-why-record-holders-avoid-2-mod-3.md`.
- `H-005` — lema: T(n) mod 3 é determinado inteiramente pela paridade de a(n)
  (a valuação 2-ádica do passo), nunca pelo resíduo de n mod 3. Prova algébrica
  curta + verificação computacional sem exceção em 777.748 passos (ver
  `experiments/E-005-mod3-valuation-parity/`). Consequência derivada e também
  confirmada: entre termos subsequentes de qualquer órbita, resíduo mod 3 nunca
  é 0, e a proporção 1 vs 2 é 1:2 (não 1:1) — confirmado com 33.47% vs 33.33%
  previsto. Primeira peça de estrutura **exata** (não estatística) do projeto.
  Não explica o achado de H-004 (esse é sobre o número inicial da órbita, não
  sobre termos subsequentes) — continua em aberto. Ver
  `hypotheses/H-005-mod3-valuation-parity-lemma.md`.
- `H-010` — constante assintótica do stopping time. Derivamos K≈7.2283
  (total_stopping_time(n) ≈ K·log₂n) a partir de fatos já estabelecidos por
  nós (E[a]=2, H-001), e confirmamos empiricamente: K empírico=7.1833
  (diferença 0.62%). R²=0.03 — log₂(n) sozinho explica pouco da variância
  individual. Ver `hypotheses/H-010-stopping-time-asymptotic-constant.md`.
- `H-011` — a variância residual de H-010 é ruído previsto, não estrutura
  escondida. Derivamos que Var(total_stopping_time) deveria crescer linear
  em log₂n (coeficiente teórico 186.93, via aproximação de tempo de primeira
  passagem). Confirmado empiricamente em 8 ordens de magnitude (log₂n de 10.5
  a 45.5): coeficiente empírico 181.53, diferença de 2.9%. Resolve a pergunta
  em aberto de H-010. Ver `hypotheses/H-011-variance-scaling.md`.
- `H-017` — cauda do pico da órbita. A sequência de valores ímpares é um
  martingale multiplicativo exato (E[3/2^a]=1, verificado analiticamente),
  o que implica via equação de Cramér um expoente de decaimento exato
  θ*=1 (sem parâmetro livre) para a cauda do pico: P(pico≥n·2^Δ)~C·2^(−Δ).
  Confirmado empiricamente: inclinação da cauda distante −1.0045 vs. teórico
  −1.0 (diferença 0.45%, 2M amostras, duas seeds). Ver
  `hypotheses/H-017-peak-excursion-tail.md`.
- `H-012` — estrutura de predecessores de potências de 2 (a partir de
  observação do diretor científico sobre 32/64 na árvore reversa). Provado:
  2^k tem predecessor ímpar genuíno sse k é par, e nesse caso o predecessor é
  Σ4^i (sempre ímpar). Conecta diretamente com o lema de H-005. Verificado
  para k=1..60. Ver `hypotheses/H-012-powers-of-2-predecessor-structure.md`.
- `H-013` — todo órbita termina no último valor ímpar J_t=(4^t−1)/3
  (consequência de H-012). Classes estéreis (t múltiplo de 3) explicadas por
  H-005 (J_t divisível por 3 nunca reaparece). Confirmado sem exceção em
  300k amostras (e depois em varredura exaustiva até 80M). Anomalia real e
  ainda não-explicada: fração para t=5 (341) maior que para t=4 (85), e para
  t=8 maior que t=7 — mas **hipótese inicial (ligada a mod 3 de J_t)
  refutada**: a razão entre classes adjacentes inverte em t=10/11 e t=13/14
  (varredura exaustiva). Não é um padrão simples — continua em aberto. Ver
  `hypotheses/H-013-last-odd-value-structure.md` e
  `experiments/E-013-last-odd-value-structure/CORRECTION.md`.
- `H-014` — recordistas nunca são ≡5 mod 8. Segunda técnica de exclusão
  (empate exato: N=4u+1 com u ímpar tem total_stopping_time igual, não
  menor, ao de N−1, via coalescência de trajetórias — diferente do domínio
  estrito de H-007). Confirmado em 200k casos + nenhum dos 148 recordistas
  oficiais é ≡5 mod 8. Ver `hypotheses/H-014-tie-exclusion-mod8.md`.
- `H-015` — busca sistemática de coalescências mod 2^d (generalização de
  H-014). Encontrou 2374 classes residuais novas, excluindo cumulativamente
  69.3% dos resíduos mod 2^16. Verificado válido para K grande o suficiente
  (efeito de borda em K pequeno, análogo ao N=2 de H-007 — só 6 dos 148
  recordistas, todos muito pequenos, "violam" alguma exclusão). **Não
  resolve H-008** por limitação estrutural (mod 2^d e mod 9 são coprimos).
  Ver `hypotheses/H-015-systematic-coalescence-search.md`.
- `H-018` — mecanismo qualitativo (Galton-Watson) por trás da anomalia de
  H-013. Construção explícita da árvore reversa (após corrigir um bug de
  poda por magnitude) revela: geração do primeiro checkpoint é constante
  (1 para t≡2mod3, 2 para t≡1mod3, insuficiente sozinho); o "orçamento"
  log₂(n_max/J_t) encolhe 2 bits por unidade de t — explica por que a
  vantagem geracional domina para t pequeno mas é dominada por flutuações
  de árvore finita para t grande. Sem fórmula fechada. Ver
  `hypotheses/H-018-reverse-tree-branching.md`.
- `H-019` — tempo de mistura da densidade de bits. Razão passos/k estabiliza
  em ~1.3-1.5 (denso) e ~1.0-1.23 (esparso) de k=8 a 1024 — confirma
  crescimento linear, consistente com 3n+1 ser operação local. Ver
  `hypotheses/H-019-bit-density-mixing.md`.
- `H-021` — erosão de runs de 1s terminais. Regra confirmada sem exceção
  (50k testes). Recordistas têm runs de subida mais longos (2.512 vs 2.035
  típico, que bate com previsão teórica de H-001) — registrado como
  parcialmente tautológico. Ver `hypotheses/H-021-terminal-run-erosion.md`.

## Hipóteses parcialmente confirmadas (com ressalva)

- `H-020` — controle bits altos vs. baixos. F-estatística: baixos=50.7,
  altos=1.80, controle aleatório=0.94. Assimetria forte confirmada, mas
  "zero informação" nos bits altos não confirmada com exatidão — resíduo
  provavelmente explicado por H-010/H-011 (média/variância dependem de
  log₂n), não por informação nova. Ver
  `hypotheses/H-020-high-bits-no-information.md`.

## H-008 — RESOLVIDA PARCIALMENTE (avanço real)

- `H-022` — **prova parcial de H-008** via relação multiplicativa (2 passos
  acelerados, não deslocamento aditivo como H-015/H-016). Provado: todo
  N=18j+13 (metade ímpar de N≡4 mod9) tem M=16j+11<N com
  total_stopping_time(M)=total_stopping_time(N)+5 — exclusão rigorosa,
  verificada sem exceção em 100.000 casos, confirmada não-redundante com
  H-007/H-014 (75% dos casos não eram já cobertos). A metade **par**
  (N≡4 mod18) continua sem prova — passos acelerados só alcançam ímpares,
  a mesma técnica não se aplica diretamente. Ver
  `hypotheses/H-022-mod9-multiplicative-exclusion.md`.

## Hipóteses refutadas relacionadas a H-008 (tentativas negativas registradas)

- `H-016` — tentativa de estender a coalescência para módulo conjunto
  9·2^d, tentando atacar H-008 diretamente. Encontrou candidatos aparentes
  para excluir a classe 4 mod 9, mas todos se mostraram genéricos (funcionam
  para os 9 resíduos mod 9 igualmente — testado até d=7, k=100) — são
  fenômenos mod-2^d disfarçados, não achados mod-9 genuínos. Explicação
  teórica: T(n) mod 9 depende só de n mod 3, não do valor completo mod 9,
  então fixar mod 9 não adiciona restrição real. Resolvido parcialmente
  depois em H-022 com uma técnica diferente (multiplicativa). Ver
  `hypotheses/H-016-mod9-coalescence-search.md`.

- `H-001` — independência entre valuações 2-ádicas consecutivas (a_1, a_2) na
  órbita acelerada. Testada em `experiments/E-001-parity-independence/`: com
  desenho experimental correto (amostras independentes, sem colisão de órbitas),
  independência **não foi rejeitada** — consistente com o modelo i.i.d. padrão da
  literatura e com o teorema de Terras/Everett. Ver detalhes em
  `hypotheses/H-001-parity-independence.md`.
- `H-002` — estrutura residual em outliers de stopping time. Testada em
  `experiments/E-002-stopping-time-outliers/` (n até 2M, top 0.5%, 2 seeds).
  Resíduo mod 2^k mostra diferença enorme, mas é **tautológico** (decorre
  mecanicamente da definição de stopping time via sequência de valuações, não é
  estrutura nova). Resíduo mod 3^k **não mostrou nenhum sinal** — resultado
  negativo genuíno. Hipótese parcialmente refutada: nenhuma estrutura "nova"
  encontrada. Ver `hypotheses/H-002-stopping-time-outliers.md`.
- `H-003` — dependência de longo alcance entre valuações (lags 1-6). Testada em
  `experiments/E-003-long-range-dependency/`: nenhuma dependência significativa
  em nenhum lag (500k amostras cada, todos p > 0.2). Reforça a suposição i.i.d.
  padrão para além do lag 1. Hipótese refutada. Ver
  `hypotheses/H-003-long-range-dependency.md`.
- `H-004` (autocorrelação interna, parte da hipótese) — sinal inicial não
  sobreviveu ao controle de confounder de comprimento de órbita — não
  suportada. (A parte mod-3 de H-004 é o principal achado confirmado do
  projeto, ver "Hipóteses confirmadas" acima.)
- `H-006` — viés mod-3 replicado via "top-K por valor bruto" em vez de
  recordistas estritos. Não suportada como formulada (nenhum viés no top-K
  bruto), mas o diagnóstico foi valioso: top-K bruto e recordista estrito são
  populações diferentes, e isso ajudou a descobrir o erro de transcrição
  corrigido em H-004. Ver `hypotheses/H-006-top-k-stopping-time-mod3.md`.
- `H-009` — busca por ciclo não-trivial em inteiros positivos (pergunta do
  diretor científico, por analogia aos 3 ciclos conhecidos em negativos).
  Busca própria por força bruta (a=1 até 14) não encontrou nada além do ciclo
  trivial — consistente com Steiner (1977), Simons (2005) e Simons & de Weger
  (2005, que já provaram rigorosamente até a=68, muito além do nosso
  alcance). Não é descoberta nova, é verificação própria de resultado já
  estabelecido. Ver `hypotheses/H-009-nontrivial-cycles.md`.

## Questões em aberto (sem prova nem refutação)

- `H-008` — por que a classe 4 mod 9 nunca aparece em recordistas (mesmo não
  sendo excluída pela prova de H-007). Tentei generalizar a técnica de H-007
  e não encontrei uma relação algébrica curta. Ver
  `hypotheses/H-008-mod9-class4-open-question.md`.

## Descobertas recentes

- 2026-07-13: levantamento de literatura inicial (5 notas temáticas em
  `literature/`), cobrindo estado da arte, abordagens conhecidas e recursos de
  referência (bibliografias de Lagarias, projeto ccchallenge.org).
- 2026-07-13: **lição metodológica importante** — órbitas de Collatz colidem, e
  agregar estatísticas por posição-em-órbita ao longo de múltiplas trajetórias
  causa pseudo-replicação severa (o mesmo trecho de caminho é contado várias
  vezes), inflando artificialmente significância estatística. Documentado em
  `protocols/new-experiment.md` como armadilha conhecida para todo experimento
  futuro que agregue múltiplas órbitas.
- 2026-07-13: H-001 testada e refutada na forma simples (ver acima).
- 2026-07-13: H-002 testada. Achado metodológico irmão do de H-001: um sinal
  aparentemente forte (mod-2^k) pode ser tautológico em vez de uma descoberta —
  residuo mod 2^k é quase-determinístico em função da sequência de valuações, que
  é a própria definição de outlier. Sempre verificar se um sinal "óbvio" não é só
  a definição reformulada antes de comemorar.
- 2026-07-13: **lição de integridade importante** — uma lista de recordistas
  usada para caracterizar H-004 foi digitada de memória em vez de vinda da
  saída real do script, e continha 4 valores incorretos que distorceram a
  conclusão inicial. Corrigido usando a sequência oficial (OEIS A006877). O
  código em si estava correto o tempo todo. Lição documentada em
  `protocols/new-experiment.md`: nunca reconstruir dados de memória — sempre
  usar a saída real ou uma fonte externa salva no repositório.
- 2026-07-13: com dados corrigidos, o achado mod-3 de H-004 ficou **mais
  forte**, não mais fraco (n=148 em vez de 57, p<10^-13 em três módulos).
- 2026-07-13: **achado de H-004 completamente explicado** — H-007 prova
  algebricamente (não só estatisticamente) por que recordistas nunca são ≡2
  mod 3. Descoberto ao pesquisar a literatura: essa exclusão já era usada como
  otimização conhecida em buscadores de "delay records" (repositório
  cuda-collatz), mas sem prova publicada facilmente acessível — derivamos a
  prova nós mesmos.
- 2026-07-13: **outro bug pego a tempo** — uma função "acelerada"
  (`total_steps_only`) assume implicitamente que a entrada é sempre ímpar;
  chamá-la com um número par dá resultado errado sem avisar. Nunca afetou os
  scans principais (sempre iteravam só sobre ímpares), mas pegou uma
  verificação ad-hoc de surpresa. Lição documentada em
  `protocols/new-experiment.md`.
- 2026-07-13: diretor científico pediu para atacar o problema por múltiplos
  ângulos simultaneamente (não só provar, também tentar desprovar/refutar).
  Registrado backlog em `BACKLOG.md`: ciclos não-triviais em positivos,
  distribuição de stopping times, análise de padrões binários. Escolhi
  ciclos não-triviais como próximo passo (H-009) — mais tratável e com
  literatura séria para comparar.
- 2026-07-13: revisado e catalogado um PDF externo enviado pelo usuário
  ("Proving the Collatz Conjecture with Binaries Numbers", Santos 2018,
  periódico de baixo rigor) — não é uma prova válida; falha identificada com
  precisão (Seção 2.6 assume uma sequência fixa de passos e generaliza
  ilegitimamente). Catalogado em `literature/unverified-proof-claims.md`.
- 2026-07-13: H-009 testada — busca própria por ciclo não-trivial (a até 14)
  não encontrou nada além do trivial, consistente com Steiner/Simons/de
  Weger.
- 2026-07-13: diretor científico pediu para registrar uma tarefa pendente:
  escrever um paper curto apontando os erros do PDF de Santos (2018) —
  registrado em `BACKLOG.md`, ainda não iniciado.
- 2026-07-13: H-010 testada — derivamos e confirmamos empiricamente a
  constante assintótica do stopping time (K≈7.23·log₂n, diferença de 0.62%
  entre teoria e dados). R²=0.03 é o achado lateral interessante: pouquíssimo
  da variância individual vem do tamanho de n.
- 2026-07-13: diretor científico pediu para deixar o paper sobre o PDF por
  último e continuar as análises.
- 2026-07-13: H-011 testada — resolvida a pergunta em aberto de H-010:
  derivamos que a variância de total_stopping_time deveria crescer linear em
  log₂n (não quadraticamente), coeficiente teórico 186.93. Confirmado
  empiricamente em 8 ordens de magnitude (log₂n de 10.5 a 45.5): coeficiente
  empírico 181.53, diferença de 2.9%. O R² baixo de H-010 é ruído previsto
  pela própria heurística, não estrutura escondida.
- 2026-07-13: diretor científico trouxe uma observação da árvore reversa de
  Collatz (potências de 2 como 32/64 se comportam diferente) e pediu para
  explorar padrões binários, sugerindo consultar um modelo de IA (Fable) para
  brainstorm de hipóteses novas. H-012 testada — a observação virou um
  teorema curto e provado (conecta com H-005): 2^k tem predecessor ímpar na
  árvore reversa sse k é par. Um agente rodando o modelo Fable foi consultado
  em paralelo para gerar mais hipóteses de padrão binário (resultado a
  incorporar quando o agente terminar).
- **Lembrete permanente**: só escrever o paper sobre os erros do PDF de
  Santos quando o diretor científico pedir explicitamente — não fazer por
  iniciativa própria, mesmo que pareça um bom momento.
- 2026-07-13: agente Fable retornou brainstorm de padrões binários. Relatório
  bem calibrado (já avisou da armadilha tautológica de H-002 antes de propor
  ideias). Verifiquei de forma independente as duas hipóteses mais fortes
  (nunca aceitar afirmação de agente sem checar):
  - **H-013** (confirmada): toda órbita termina em J_t=(4^t−1)/3
    (consequência de H-012). Classes estéreis explicadas por H-005. Achou
    uma anomalia real (t=5 mais frequente que t=4) — deixada em aberto.
  - **H-014** (confirmada): recordistas nunca ≡5 mod 8 — segunda técnica de
    exclusão (empate exato por coalescência, diferente do domínio de H-007).
  - Ideias mais ambiciosas do Fable (busca sistemática de coalescências que
    poderia resolver H-008; cauda do pico da órbita; mistura de densidade de
    bits) registradas em `BACKLOG.md` item 3 para sessões futuras.
- 2026-07-13: H-015 testada (busca sistemática de coalescências mod 2^d,
  generalizando H-014) — 2374 classes novas, 69.3% de mod 2^16 excluído.
  Confirmado válido para N grande o suficiente. **Não resolve H-008** —
  limitação estrutural clara (mod 2^d e mod 9 são coprimos), documentada
  para não repetir a tentativa nessa forma no futuro.
- 2026-07-13: diretor científico pediu para tentar uma versão mod-9 da
  técnica, atacando H-008 diretamente. H-016 testada: encontrou candidatos
  aparentes usando módulo conjunto 9·2^d, mas todos se revelaram genéricos
  (funcionam para os 9 resíduos mod 9 igualmente, não só o 4) ao testar
  explicitamente a exclusividade — resultado negativo, mas com explicação
  teórica clara (T(n) mod 9 depende só de n mod 3, não do valor completo mod
  9). H-008 continua sem solução.
- 2026-07-13: escolhi H-017 (cauda do pico da órbita) como próximo passo —
  ideia do Fable com previsão sem parâmetro livre. Verifiquei a equação de
  Cramér antes de implementar (θ*=1 exato). Confirmado empiricamente com
  grande precisão (0.45% de diferença na cauda distante). Terceira vitória
  no estilo "derivar teoria → confirmar nos dados" (depois de H-010/H-011).
- 2026-07-13: diretor científico expressou compromisso de longo prazo com o
  projeto ("nunca vamos parar"). Respondi com calibração honesta: Collatz
  resistiu a ~90 anos de matemáticos profissionais (incluindo Tao), é
  extremamente improvável que seja "resolvido" por completo por este
  laboratório — mas o trabalho incremental real (teoremas verificados, erros
  corrigidos, resultados negativos documentados) já é ciência genuína e vale
  a pena continuar sessão após sessão.
- 2026-07-13: investiguei a anomalia p₅>p₄ de H-013 mais a fundo. Especulei
  que fosse ligada ao resíduo mod 3 de J_t — **refutei minha própria
  hipótese** com varredura exaustiva até 80M: a razão entre classes
  adjacentes cresce em (4,5) e (7,8) mas inverte em (10,11) e (13,14). A
  anomalia é real (confirmada em duas escalas) mas não segue um padrão
  simples de mod 3 — continua genuinamente em aberto.
- 2026-07-13: diretor científico pediu para testar tudo em sequência,
  começando pela análise de ramificação (Galton-Watson) da árvore reversa.
  H-018: construí a árvore reversa explicitamente, corrigi um bug real de
  poda por magnitude no caminho, e encontrei um mecanismo qualitativo
  (competição entre vantagem geracional constante e orçamento de bits que
  encolhe 2 bits por t) que explica coerentemente a não-monotonicidade,
  sem fórmula fechada.
- 2026-07-13: completei toda a lista restante do brainstorm Fable em
  sequência: H-019 (mistura de densidade de bits, confirmada — crescimento
  linear), H-020 (controle bits altos, parcialmente confirmada — assimetria
  forte mas resíduo não-nulo explicado por H-010/H-011), H-021 (erosão de
  runs terminais, confirmada + achado tautológico sobre recordistas). Lista
  do Fable totalmente esgotada — 10 hipóteses (H-012 a H-021) a partir de
  uma única consulta ao modelo.
- 2026-07-13: diretor científico pediu para continuar com H-008 e H-013.
  **H-022 — avanço real em H-008**: abordagem multiplicativa (2 passos
  acelerados, não aditiva) provou rigorosamente a exclusão da metade ímpar
  da classe 4 mod 9 (N=18j+13), verificada sem exceção em 100k casos e
  confirmada não-redundante com H-007/H-014. Metade par continua em aberto
  (limitação estrutural: passos acelerados só alcançam ímpares).
- 2026-07-13: diretor científico trouxe transcrição de vídeo do Veritasium
  sobre Collatz, pedindo novas ideias. **H-023 (Lei de Benford)**: testada
  e confirmada — valores de órbitas seguem Benford com excelente precisão
  prática, consequência do passeio aleatório multiplicativo já estabelecido
  (H-001/H-010/H-011/H-017). No caminho, achei e corrigi um viés
  metodológico real (amostras que atingiam n=1 antes do fim da janela de
  passos inflavam artificialmente o dígito 1). Nota sobre Fractran/Conway
  (indecidibilidade) adicionada à literatura como contexto conceitual.
- 2026-07-13: retomei a medição quantitativa da anomalia de H-013 (pedido
  do diretor científico) com um multiplicador de busca bem menor (5× em vez
  de 100× — essa era a causa real dos travamentos, não o n_max). Consegui
  escalar até n_max=10¹¹. **A razão (10,11) convergiu e estabilizou** (0.0655
  em 10¹⁰ vs 0.0656 em 10¹¹) — confirma que a inversão é um fato assintótico
  real e permanente, não ruído de amostra pequena como eu havia sugerido
  antes. Ainda sem fórmula fechada para o valor exato de convergência.
- 2026-07-13: diretor científico pediu uma derivação teórica fechada,
  lembrando que há 16 núcleos e ~55GB de RAM disponíveis. Tentei via a
  relação recursiva exata D(v)=D(2v)+D(ramo), que leva a uma soma infinita
  D(J_t)=Σ D(w_i) — **não consegui fechar numa fórmula finita** (exigiria
  resíduos mod 3^k para k arbitrário, recursivamente; possivelmente um
  problema genuinamente difícil/em aberto). Reportei essa limitação com
  honestidade em vez de forçar uma fórmula frágil. Usei o paralelismo
  oferecido para melhorar a precisão numérica: no caminho, cometi (e
  corrigi) um erro de comparar t=10 e t=11 em n_max DIFERENTES (razão
  inflada 10×); depois disso, uma tentativa de escalar ainda mais foi morta
  pelo OOM killer do sistema (limite de memória prático menor que os 62GB
  nominais — registrado para o futuro). Resultado final: **(10,11)
  confirmado em ~0.065 com alta confiança** (três escalas, 1e10-1e12,
  variação <1.5%); **(13,14) em ~0.27-0.28 com confiança moderada**.

## Próximos passos

**Trinta e sete hipóteses testadas (H-001 a H-037)**. O achado central do
projeto — por que recordistas evitam resíduo 2 mod 3 — está **completamente
resolvido** (H-007), com uma técnica irmã generalizada em larga escala
(H-014→H-015), e consolidado via CRT em H-028 (45/72 resíduos mod72
excluídos — mas ver ressalva de novidade abaixo). **H-008 (classe 4 mod9)
está agora RESOLVIDA POR COMPLETO** (H-022 metade ímpar + H-027 metade
par). A pergunta da variância de H-010 está **resolvida** (H-011), assim
como a cauda do pico da órbita (H-017) e a Lei de Benford (H-023). A
fórmula fechada para a anomalia de H-013 **não foi encontrada, mas H-024
explica rigorosamente por quê** (densidade exige precisão 3-ádica
ilimitada — não é falta de tentativa, é uma obstrução real, com paralelo
independente na "Rota A" do paper de Chang 2026, ver H-030).

**Avaliação estratégica importante (ver seção acima)**: a checagem de
novidade de H-028/H-022 revelou que boa parte da família de exclusão já é
folclore conhecido pela comunidade prática de busca de recordistas
(cuda-collatz) — a linha de "excluir recordistas por classe residual"
está substancialmente esgotada como fonte de resultado genuinamente novo.

**Segunda avaliação estratégica (2026-07-13, depois de H-036/H-037)**:
a OUTRA linha mais desenvolvida do projeto — a "obstrução de precisão
3-ádica ilimitada" (H-013/H-018/H-024/H-025/H-026/H-030/H-032) — também
não é mais nova no nível geral: é o resultado central de um survey de
216 páginas contemporâneo (Chang 2026, arXiv:2603.11066, ver H-036).
**As duas linhas mais desenvolvidas do projeto estão, portanto, ambas
sabidamente esgotadas como fonte de resultado geral novo** — continuar
gerando H-0XX dentro de qualquer uma das duas tem valor de verificação/
aprendizado, mas não deve ser confundido com progresso rumo a algo
publicável. Isso não invalida nenhum resultado nosso (H-024 continua
válido como instância específica; a família CRT de H-028 continua válida
como consolidação), só recalibra a expectativa. Questões genuinamente em
aberto que restam:

1. **Fórmula fechada para a anomalia de H-013** — valores de convergência
   bem medidos numericamente ((10,11)≈0.065, (13,14)≈0.27-0.28), mas sem
   teoria que os derive a partir de primeiros princípios. H-024 explica
   por que a recursão exata D(v)=D(2v)+D(ramo) não fecha (exige precisão
   3-ádica ilimitada) — provavelmente um problema genuinamente difícil,
   não um branco de tentativa. H-037 mostrou que α de Pratiher (uma vez
   corrigido o rótulo) é essa MESMA quantidade agrupada por t mod3 —
   dominada por poucos termos pequenos (p_2=D(5) sozinho é 93,77%), o que
   dá uma razão estrutural para mais tratabilidade que o D(v) genérico,
   mas ainda não fechada.
2. **H-037 em aberto**: reportamos ao diretor científico um provável erro
   de rotulagem no paper de Pratiher (números corretos, forma errada) —
   decidir se/como isso deveria ser comunicado externamente é uma decisão
   do diretor científico, não algo para agir sozinho.

**Sobre o loop autônomo**: o diretor científico pediu (2026-07-13) para
operar em loop contínuo (backlog → brainstorm → repete), e mais tarde na
MESMA sessão pediu explicitamente para **cancelar** esse loop. A partir
de agora, não retomar o modo autônomo por conta própria — ver memória
`feedback_autonomous_research_loop.md` (CANCELLED). Trabalhar sessão a
sessão, a partir do que for pedido.

Tarefas pendentes (**só fazer quando o diretor científico pedir
explicitamente**, por último — lembrar de avisar quando for feito):
paper sobre os erros do PDF de Santos (`BACKLOG.md` item 5) e paper
sobre o erro de rotulagem de Pratiher (`BACKLOG.md` item 7, pedido
2026-07-13 "assim como o outro"). Outras candidatas:

1. Tentar resolver a metade par de H-008 com uma ideia nova.
2. Se alguém quiser retomar a fórmula fechada de H-013: a recursão
   D(v)=D(2v)+D(ramo) é exata e correta, só não fecha sem mais alguma ideia
   (talvez truncamento controlado, ou uma transformação diferente).
3. Considerar formalizar os teoremas já provados (H-005, H-007, H-009,
   H-012, H-014, H-015, H-017, H-019, H-021, H-022) em Lean/SageMath se o
   projeto crescer nessa direção (fora de escopo por enquanto, ver
   `ROADMAP.md`).
4. Continuar revisando qualquer nova alegação de prova externa que o diretor
   científico receber, seguindo o padrão já estabelecido em
   `literature/unverified-proof-claims.md`.
5. **Só quando pedido explicitamente**: escrever o paper curto sobre os
   erros do PDF de Santos (`BACKLOG.md` item 5).
6. **Só quando pedido explicitamente**: escrever o paper curto sobre o
   erro de rotulagem de Pratiher (`BACKLOG.md` item 7).
