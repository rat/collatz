# CRITIQUE: paper 04 (Kontorovich-Lagarias vs. Volkov)

Formato conforme Regra 8/15: tabela de status no topo (o que ainda exige
atenção agora), seções datadas abaixo (histórico completo, apensado,
nunca reescrito). O produtor lê a tabela **inteira** a cada passada, não
só a rodada mais recente.

Alvo: `main.tex` (rascunho de 4 páginas, split do §6 do paper 01 em
2026-08-10). Fontes primárias consultadas nesta rodada:
`experiments/E-139-kl-volkov-window-calibration/README.md`,
`experiments/E-097-qx1-empirical-gate/`,
`hypotheses/H-113-*.md`, `papers/06-pressao-qx1-ramificacao/main.tex`,
`literature/papers/127_Stochastic-Models-3x1-5x1-Problems-Kontorovich-Lagarias.pdf`
(o PDF de KL, lido diretamente), e o repositório de reprodutibilidade
`/home/rat/Google/Projetos/Claude/collatz-kl-volkov`.

## Tabela de status

| ID | Rodada | Resumo em uma linha | Severidade | Status |
|----|--------|---------------------|------------|--------|
| C-01 | 2026-08-10 | O terceiro controle de expoente 0,650919 (`iid`, 0,64751) foi omitido do `thm:kl-calibrated`, e é justamente ele que torna falso o limiar "within 0,003" e verdadeiro o "matches controls" | alta | fixed |
| C-02 | 2026-08-10 | O expoente de contagem $\eta$ nunca é definido, e o estimador (raiz, janela, buffer de truncamento, slope) também não: o leitor não consegue reconstruir a medição principal | alta | fixed |
| C-03 | 2026-08-10 | "At truncation depth $10^9\to10^{10}$" rotula errado uma década de checkpoint como profundidade de truncamento, colidindo com o uso de $10^9$–$10^{13}$ como buffers no §4 | alta | fixed |
| C-04 | 2026-08-10 | "ten interval-widths": a distância real é 13,5 larguras (13,0 da borda); nenhuma leitura de "interval" no texto dá dez | média | fixed |
| C-05 | 2026-08-10 | O intervalo $[0{,}64818,\,0{,}65027]$ cobre só reamostragem de raízes; três sistemáticos reconhecidos (0,004 implementação, 0,002 buffer, 0,0014 dispersão entre controles) excedem sua largura de 0,00209, e a separação é cotada nessa unidade | média | fixed |
| C-06 | 2026-08-10 | Paráfrase infiel de KL: eles escrevem que o dado *que Volkov apresenta* é insuficiente, não que o dado numérico disponível seja; e nunca atribuem a dificuldade à proximidade $\Delta=0{,}027$ | média | fixed |
| C-07 | 2026-08-10 | §5 afirma que as slopes se aproximam de 0,6509 monotonicamente; as quatro slopes exibidas extrapolam ingenuamente para ~0,647, e o dado profundo que sustentaria 0,6509 foi cortado do paper | média | fixed |
| C-08 | 2026-08-10 | O viés de 0,038 (§6, parágrafo 1) e o resíduo de 0,003 (`thm:kl-calibrated`) são o mesmo estimador em profundidades diferentes, e o texto nunca reconcilia os dois | média | fixed |
| C-09 | 2026-08-10 | "four test roots": `validate_vs_python.py` usa cinco (103, 1237, 4441, 7919, 9973) | média | fixed |
| C-10 | 2026-08-10 | A introdução chama $u$ de "fixed residue", o §2 define $u$ como inteiro ímpar coprimo a $q$: são objetos diferentes | média | fixed |
| C-11 | 2026-08-10 | "sharing every feature of the arithmetic tree except the ultimate value of $q$" é falso: os controles *sorteiam* a classe de ramo, a árvore aritmética usa o resíduo verdadeiro | média | fixed |
| C-12 | 2026-08-10 | Três travessões (`---`) nas linhas 162, 180, 200: violação direta da Regra 3, que os proíbe em qualquer lugar | média | fixed |
| C-13 | 2026-08-10 | Nove construções antitéticas "X, not Y"/"rather than" contra o orçamento de duas do documento inteiro (Regra 4b §2) | média | fixed |
| C-14 | 2026-08-10 | §4 narra o processo de pesquisa (piloto, run contaminado, correção, "failure mode anticipated in advance") e a linha 259 é meta-honestidade explícita ("checked rather than assumed before trusting") | média | fixed |
| C-15 | 2026-08-10 | "shrinking by a factor of roughly $0.4$–$0.5$": as razões reais são 0,374, 0,445 e 0,388 | baixa | fixed |
| C-16 | 2026-08-10 | Colisão de notação: $w_a$ (indexado pelo expoente) no §2 e $w_j$ (indexado pela ordem do irmão) no lema são a mesma letra com índices distintos | baixa | fixed |
| C-17 | 2026-08-10 | $A_0$ é introduzido sem definição e nunca reutilizado; "odd integer $q\ge3$ coprime to $2$" é redundante | baixa | fixed |
| C-18 | 2026-08-10 | "unlike $q=3$, there is no further parity condition beyond integrality mod $5$" está errado como escrito: em $q=3$ a condição $a\equiv a_0\pmod d$ *é* a paridade, não uma condição extra | baixa | fixed |
| C-19 | 2026-08-10 | O `\bibitem` de KL não traz páginas nem o arXiv:0910.1944 efetivamente consultado; a chave diz 2009 e a entrada diz 2010 | baixa | fixed |
| C-20 | 2026-08-10 | Vocabulário proibido pela Regra 4b §1: "clearly" (l. 50), "precisely" (l. 77), "genuine" (l. 181) | baixa | fixed |
| C-21 | 2026-08-10 | "measurement with calibrated controls, not a proof" aparece idêntico no resumo e na discussão; o §3 repete o parágrafo de abertura quase palavra por palavra | baixa | fixed |
| C-22 | 2026-08-10 | Os "6,4 standard errors" do piloto não reproduzem sob a convenção que valida 12,6 e 4,1 (dá 6,7) | baixa | fixed |
| C-23 | 2026-08-10 | `\cite{PressureCompanion}` sustenta um "provably" e é "in preparation": externamente inverificável até o paper 06 sair | baixa | rejected |

Todos os 23 achados foram lidos de volta nesta mesma rodada (2026-08-10) e corrigidos no main.tex, exceto C-23, marcado `rejected` com razao registrada (decisao de ordem de submissao ja tomada no OUTLINE.md de 01: paper 06 primeiro; nao e bug de texto). C-13: o orcamento estrito da Regra 4b e de duas construcoes antiteticas no documento inteiro; apos a reescrita ficaram tres, todas com funcao desambiguadora real (residuo sorteado vs. verdadeiro; vies vs. ruido de amostra; largura de banda vs. separacao), nao floreio retorico -- marcado `fixed` com essa ressalva em vez de forcar uma reescrita que perderia precisao.

---

## 2026-08-10, rodada 1 (crítico, primeira passada completa sobre `main.tex`)

### Severidade alta

**C-01. O controle omitido, e o limiar que depende dele.**

`thm:kl-calibrated` diz: "where the calibrated controls read their target
exponent to within $0.003$ [...] a control built to exponent $0.650919$
reads $0.64981$ and $0.65122$ on two independent constructions".

O E-139 tem **três** processos de expoente 0,650919 nessa mesma década
(`1e9 -> 1e10`, grade `b15`), e o próprio README do experimento os lista
juntos: `cycq 5.00000` lê 0,64981, `cyc` lê 0,65122, e `iid` lê 0,64751.
O paper reporta dois e cala o terceiro. Duas consequências, e é preciso
que as duas apareçam, porque a primeira sozinha tem defesa:

(a) O limiar de 0,003 só faz sentido com `iid` dentro. Os dois controles
casados desviam 0,00111 e 0,00030 do alvo, o que se descreveria como
"within 0,0012", não 0,003. O número 0,003 vem do README do E-139, onde
ele cobre "every control", e ali ele é falso: `iid` desvia 0,00341. O
paper herdou um limiar calibrado para um conjunto de controles e o
aplicou a um subconjunto onde ele é frouxo demais para significar algo, e
o membro que o violaria é exatamente o que sumiu.

(b) A omissão **piora** o encaixe, não melhora. A árvore aritmética lê
0,64926, abaixo dos dois controles reportados: 0,64981 e 0,65122. O
intervalo aritmético $[0{,}64818,\,0{,}65027]$ nem contém 0,65122, nem
contém a própria previsão 0,650919 (a borda superior 0,65027 fica abaixo
dela). Com `iid` (0,64751) na conta, 0,64926 cai no meio de uma banda de
0,004 e o "matches" é literal, que é como o README do E-139 formula
("Three independent processes [...] read 0.6475, 0.6498 and 0.6512. The
arithmetic tree reads 0.6493, inside that band"). Sem `iid`, "matches" é
uma afirmação que os números impressos ao lado dela não sustentam.

Isso não ameaça a conclusão: 0,64751 continua a ~14 larguras de intervalo
de 0,67748. É um problema de honestidade de apresentação, e é o tipo de
coisa que um árbitro que abra o repositório de dados encontra em cinco
minutos, já que os cinco processos estão na mesma tabela do README e nos
mesmos arquivos em `sec6-calibrated-comparison/data/`.

**C-02. O paper não é autossuficiente sobre a quantidade que mede.**

$N_u(x)$ é definido. O expoente $\eta$ **não é**. Não existe em lugar
nenhum um display do tipo $N_u(x)=x^{\eta+o(1)}$ ou $N_u(x)\asymp
Cx^\eta$; a introdução diz apenas "a counting exponent $\eta_{q,BP}$
governing the growth of $N_u(x)$", que não é uma definição. O paper
inteiro mede esse número, e o número nunca foi dito. (O subscrito `BP`
também nunca é expandido.)

O estimador está no mesmo estado. Não se define: o que é uma "root" (nem
como as raízes são amostradas, apesar de "60 roots" e "$n=300$ roots"
aparecerem no §4); o que é o "truncation buffer" e por que existe; o que
é a "measurement window" e como ela se relaciona com o buffer; e o que
exatamente é a "slope" (regressão de $\log N$ contra $\log x$ sobre
quais pontos?). O §4 diz "We implemented the exact reverse tree of $T_5$
from scratch" e passa direto para os resultados. Quem nunca leu o paper
01 nem o E-139 não consegue reconstruir a medição do título, nem julgar
se o estimador é razoável, o que é grave num paper cuja tese central é
que *o estimador tem viés*.

Falta ainda a ponte lógica que o §6 atribui ao lema: "Lemma
\ref{lem:sibling-congruence} makes this construction exact: replacing the
integer denominator $q$ by a tunable real value...". O lema dá a
recursão $w_{j+1}=2^dw_j+(2^d-1)/q$; o que a torna utilizável com $q$
real é que a recursão faz sentido sobre $\mathbb R$, enquanto a
caracterização original $(2^{a_0+jd}u-1)/q$ e a congruência mod $q$ não
fazem. O texto nunca diz isso. Do jeito que está, o papel do lema no
paper é afirmado, não mostrado.

**C-03. Erro de rótulo em "truncation depth".**

`thm:kl-calibrated` abre com "At truncation depth $10^9\!\to\!10^{10}$".
No E-139, `1e9 -> 1e10` é a **década de checkpoint** (a janela de
medição), e os buffers de truncamento dessa corrida são `1e9..1e15`
(grade `b15`, `run_deep.sh`). Não é profundidade de truncamento.

O erro é pior do que uma palavra trocada porque o §4 já usou exatamente
os mesmos numerais ($10^9$ a $10^{13}$) para nomear buffers de
truncamento. O leitor que vier do §4 lê "truncation depth $10^9\to
10^{10}$" como "dois dos buffers do §4" e entende algo que não aconteceu.
Some-se a isso que o §5 fala em "measurement window" com décadas
$10^4$–$10^8$: o paper usa três grandezas com a mesma aparência
(checkpoint, janela, buffer) e troca os nomes entre elas.

### Severidade média

**C-04. "ten interval-widths" não fecha com os números do próprio
teorema.** Largura do intervalo aritmético: $0{,}65027-0{,}64818 =
0{,}00209$. Distância entre as leituras: $0{,}67748-0{,}64926 =
0{,}02822$, ou **13,5 larguras**. Da borda superior até o controle:
0,02721, ou 13,0 larguras. Em meias-larguras dá 27. Nenhuma leitura dá
dez. A origem do "dez" é o README do E-139 ("ten times the band away"),
onde *band* é a dispersão de 0,004 entre os três controles de 0,650919,
um objeto que o paper não define e que, aliás, envolve o `iid`
omitido em C-01. O paper importou o número e trocou a unidade. O erro é
conservador (subestima a separação), mas continua sendo um número
impresso que não confere com os outros números impressos na mesma frase.

**C-05. O intervalo citado é estreito demais para servir de régua.** O
README do E-139 é explícito: "Those bootstrap bands cover root resampling
only". O paper reproduz o intervalo sem essa ressalva e depois mede a
separação em unidades dele. Três incertezas reconhecidas em outros
pontos do próprio material o excedem: o sistemático de implementação de
~0,004 (que a Discussão do paper cita!), o termo de buffer de até 0,002
(`buffer_squeeze.py`, não citado no paper), e a dispersão de 0,0014 entre
as duas construções de expoente 0,650919 reportadas. Todos maiores que os
0,00209 de largura. Cotar uma separação em "interval-widths" enquanto se
admite, dois parágrafos adiante, um sistemático de duas vezes a largura é
incoerente. A separação sobrevive a qualquer uma dessas escalas; a
*unidade escolhida para anunciá-la* é que não sobrevive.

**C-06. A paráfrase de Kontorovich-Lagarias não é o que eles escrevem.**
Verificado no PDF primário. KL escrevem: "The empirical data Volkov
presents seems insufficient to discriminate between these two predicted
exponents. It would be interesting for this problem to be investigated
further." E, no §7: "There is some controversy concerning the conjectured
value of the constant."

O paper 04 diz, na introdução: "note explicitly that the two predictions
are close enough ($\Delta=0.027$) that available numerical data could not
discriminate between them". Duas distorções. Primeira: KL falam do dado
*que Volkov apresenta*, não do dado numérico disponível em geral,
diferença que importa muito num paper cuja contribuição é apresentar dado
melhor. Segunda: a relação causal ("close enough ... that") é do autor,
não de KL, que em momento nenhum mencionam $\Delta=0{,}027$ nem apontam a
proximidade como a razão. O §3 repete a distorção em forma mais forte
ainda: "The authors themselves flag this as an open dispute, unresolved
for lack of sufficiently powerful data". Regra 11: uma alegação sobre o
que um autor nomeado e vivo escreveu tem que bater com o que ele
escreveu.

Menor, na mesma frase: "Kontorovich and Lagarias study the generalization
to $qx+1$ maps". Eles estudam $3x+1$ e $5x+1$, como diz o título do
próprio trabalho, não $qx+1$ geral.

**C-07. "Approaching $0.6509$ monotonically" não sai das slopes
exibidas.** O §5 mostra $0{,}6021\to0{,}6296\to0{,}6432\to0{,}6460$ e
conclui "approaching $0.6509$ monotonically without having reached it".
Os incrementos são 0,0275, 0,0136 e 0,0028: uma extrapolação geométrica
ingênua a partir daí dá ~0,647, não 0,651. Monotonicidade o dado mostra;
o *destino* 0,6509 é escolhido, não medido. O dado que justificaria essa
frase existe (a corrida profunda só-aritmética do E-139: 0,6487, 0,6490,
0,6506, 0,6505 nas décadas $10^8$ a $10^{12}$, lidas como
$0{,}6505\pm0{,}002$), e foi cortado do paper. Cortar a evidência e
manter a conclusão que ela sustentava é a pior das duas combinações
possíveis.

**C-08. A narrativa do viés se contradiz sem explicação.** O §6 abre
dizendo que o estimador subestima em 0,038 num processo de expoente
conhecido, mais que o $\Delta=0{,}027$ em disputa, e conclui: "Comparing
the raw reading against either theoretical prediction therefore settles
nothing." Vinte linhas depois, `thm:kl-calibrated` roda num regime onde
os controles acertam o próprio alvo dentro de 0,003, isto é, onde o viés
praticamente sumiu. As duas coisas são compatíveis (o viés cai com a
profundidade, e o E-139 mostra a tabela dessa queda), mas o paper nunca
diz isso. Lido como está, o §6 anuncia uma calibração e entrega uma
medição mais profunda quase não-enviesada: são coisas diferentes, e a
palavra "calibrated" no título do paper depende de qual delas é.

**C-09. "four test roots" são cinco.** §4: "validated byte-for-byte
against the earlier buffer-by-buffer method on four test roots".
`validate_vs_python.py`, linha 62, no repositório de reprodutibilidade e
no experimento: `roots = [103, 1237, 4441, 7919, 9973]`. Cinco. Regra 12:
o número impresso no paper tem que bater com o código que ele diz que o
sustenta.

**C-10. $u$ é resíduo ou inteiro?** Introdução: "$N_u(x)$, the number of
integers up to $x$ that eventually map to a fixed residue $u$". §2: "$u$
odd [...] coprime to $q$" e $N_u(x):=\#\{n\le x: T_q^k(n)=u\}$, isto é,
$u$ é um inteiro específico (a raiz da árvore). Um resíduo e um inteiro
não são a mesma coisa, e a confusão é ativa aqui porque o §2 usa
*genuinamente* resíduos noutro papel (a admissibilidade depende de $u
\bmod q$). Corrigir na introdução.

**C-11. Os controles não compartilham "every feature except $q$".** §6:
"sharing every feature of the arithmetic tree except the ultimate value
of $q$". Pelo README do E-139, o modo `cyc`/`cycq` **sorteia** a classe
do primeiro irmão e faz os seguintes avançarem pela congruência; a
árvore aritmética usa o resíduo verdadeiro $u\bmod q$ em cada nó. A
diferença entre resíduo endógeno e resíduo sorteado é precisamente o
objeto de toda esta linha de pesquisa, e o paper a descreve como se não
existisse. A frase precisa dizer o que os controles de fato preservam
(lei de prole e espaçamento de irmãos) e o que trocam.

**C-12. Três travessões.** Linhas 162, 180 e 200 usam `---`. A Regra 3
os proíbe em qualquer lugar, sem exceção, e a Regra 4b §2 reforça com
alvo zero por documento. Conserto mecânico: vírgula, parêntese ou frase
nova.

**C-13. Nove antíteses contra um orçamento de duas.** Linhas 52 ("not a
proof"), 53 ("rather than Volkov's branching model"), 108 ("rather than
path occurrences"), 181 ("not noise"), 201 ("not of uncorrected
truncation bias"), 232 ("rather than subtraction"), 250 ("widens, not
narrows"), 259 ("rather than assumed"), 269 ("not a proof" de novo). A
Regra 4b §2 permite duas no documento inteiro. Duas delas (52/53 e
250/269) são, ainda por cima, o mesmo par repetido.

**C-14. Narração de processo e meta-honestidade.** O §4 inteiro é o
diário do experimento: o piloto de 60 raízes, a corrida de produção que
"initially sampled roots too close to the measurement window's lower
checkpoint, contaminating the truncation buffer", a correção, e "a
failure mode anticipated in advance". A Regra 4b §3 proíbe explicitamente
essa categoria ("an earlier draft claimed...", "this was later
corrected"): correções acontecem antes da submissão e depois somem. O
método correto se descreve no presente, uma vez. A linha 259 é o caso
mais puro: "Two systematics were checked rather than assumed before
trusting Empirical Result~\ref{thm:kl-calibrated}": auditoria da própria
confiança, item 7 do checklist da Regra 4b ("Find any statement of
honesty, caution, or calibration. Delete."). Os dois sistemáticos devem
ficar; a moldura sobre tê-los checado, não. Na mesma família: "The
estimator behind Empirical Result~\ref{thm:kl} had never been run on a
process with a known exponent" (l. 219) e "\S\ref{sec:calibrated} is the
paper's contribution" (l. 80, sujeito é o próprio paper, checklist item
6).

Registro para o produtor, já que aqui há tensão real entre regras: a
Regra 10b **exige** que a categoria do resultado (medição, não prova)
seja legível desde o resumo. Isso já está garantido pelo ambiente
`empirical` e pelos verbos ("we report", "reads", "measurement"). O que
sobra a cortar é a repetição da frase-status, não o rótulo.

### Severidade baixa

**C-15.** "increments $0.0234, 0.0087, 0.0039, 0.0015$ shrinking by a
factor of roughly $0.4$–$0.5$ per decade": as razões são 0,374, 0,445 e
0,388. Duas das três estão abaixo de 0,4. Escrever 0,37–0,45.

**C-16.** O §2 define $w_a:=(2^au-1)/q$, indexado pelo expoente; o lema
usa $w_j=(2^{a_0+jd}u-1)/q$, indexado pela ordem do irmão. Mesmo símbolo,
dois índices. $w_j$ do lema é $w_{a_0+jd}$ do §2.

**C-17.** $A_0$ aparece em "$A_0=\{1\mapsto4,\dots\}$" sem ser definido
como símbolo e nunca mais é usado: ou define, ou apresenta a tabela sem
nomeá-la. E "Fix an odd integer $q\ge3$ coprime to $2$": ímpar já é
coprimo a 2.

**C-18.** "unlike $q=3$, there is no further parity condition beyond
integrality mod $5$". Em $q=3$, $d=\ord_3(2)=2$, e os expoentes
admissíveis são $a\equiv a_0\pmod 2$: a condição de paridade **é** a
condição $a\equiv a_0\pmod d$ do próprio parágrafo, não uma condição
adicional. A frase, como escrita, sugere um obstáculo extra em $q=3$ que
não existe nessa formulação, e "integrality mod $5$" não é uma expressão
bem formada (a integralidade é a condição; mod 5 é onde se testa).

**C-19.** O `\bibitem` traz o capítulo de livro (AMS, 2010) sem páginas.
A fonte de fato consultada no repositório é o arXiv:0910.1944 (2009),
cuja numeração de teoremas (Theorem 8.10, de onde vêm 0,650919 e 0,678) é
a que o E-139 cita. Chave `KontorovichLagarias2009` com entrada de 2010.
Regra 11: acrescentar arXiv e páginas, e conferir se a numeração do
capítulo publicado coincide antes de citar teorema em versão futura.

**C-20.** Regra 4b §1: "clearly" (l. 50, "separates clearly"),
"precisely" (l. 77, fora de sentido técnico), "genuine" (l. 181). Fora
isso o vocabulário está limpo: nenhum "crucial", "robust", "key",
"underscore", "highlight", "moreover", "furthermore".

**C-21.** "This is a measurement with calibrated controls, not a proof"
aparece no resumo (l. 52) e na discussão (l. 269), praticamente idêntica.
E o §3 inteiro ("The dispute", cinco linhas) reenuncia o segundo
parágrafo da introdução quase palavra por palavra: 0,650919, 0,678,
"discussed in the same reference", $\Delta=0{,}027$, a mesma alegação
sobre os autores. Uma seção que só existe por simetria estrutural
(checklist item 9); ou some, ou passa a conter algo que a introdução não
disse, por exemplo a diferença estrutural do modelo de Volkov, hoje
enterrada na discussão.

**C-22.** §4: piloto com slope 0,6433, IC $[0{,}6327,0{,}6531]$,
"excluding $0.678$ by roughly $6.4$ standard errors". Sob a convenção
$\mathrm{SE}=(\text{hi}-\text{lo})/(2\cdot1{,}96)$, que é a que
reproduz corretamente os 12,6 e os 4,1 da corrida de produção, sai
$\mathrm{SE}=0{,}00520$ e $(0{,}678-0{,}6433)/0{,}00520=6{,}67$. O IC do
piloto é assimétrico em torno de 0,6433, então o SE pode ter sido
calculado direto do bootstrap e não da largura; nesse caso o 6,4 pode
estar certo e a discrepância é de convenção. Por Regra 8c, não estou
afirmando que está errado: o produtor deve recuperar o SE de fato usado e
ou corrigir o número, ou dizer qual convenção vale. Note que 6,4 e 6,67
não mudam nada substantivo, o parágrafo inteiro cai sob C-14 de todo
jeito.

**C-23.** `\cite{PressureCompanion}` sustenta "exponent provably
$0.650919$", que é a pedra angular da medição de viés. Verifiquei o paper
06 e ele de fato prova a afirmação em substância: prova a identidade
$\rho_{\mathrm{ann}}(\alpha)=q^{\alpha-1}/(2^\alpha-1)$ e que a raiz
menor está sempre *unfrozen*, de modo que a identidade anelada transfere
rigorosamente para a função de contagem temperada do modelo i.i.d.
correspondente. O uso da citação faz sentido no lugar onde aparece e não
é sustentação circular. O que resta é a exposição: 04 cita 06 como
"in preparation" e 06 cita 04 como companion, então um árbitro externo
não pode verificar nenhum dos dois pelo outro. Decidir a ordem de
submissão, ou incluir no 04 o enunciado mínimo que ele consome.

### Verificado e correto (Regra 8c: o que foi checado e passou)

- **Lema da congruência de irmãos.** Refiz a substituição: $2^dw_j +
  (2^d-1)/q = (2^d(2^{a_0+jd}u-1)+2^d-1)/q = (2^{a_0+(j+1)d}u-1)/q =
  w_{j+1}$. Correto. $(2^d-1)/q\in\mathbb Z$ porque $d=\ord_q(2)$, a
  congruência segue de $2^d\equiv1$, e em $q=5$, $d=4$: $(16-1)/5=3=c$.
  Confere. O argumento de Wieferich também: $c=0$ com $q$ primo força
  $q^2\mid 2^d-1$ e, como $d\mid q-1$, daí $q^2\mid2^{q-1}-1$.
- **Aitken.** $\Delta^2$ sobre (0,63261, 0,63650, 0,63801) dá 0,638968,
  isto é, 0,639. Confere com a eq. (1).
- **Incrementos.** 0,02338, 0,00874, 0,00389, 0,00151, arredondam para
  os quatro valores impressos. (A razão é que erra, C-15.)
- **A equação dos controles.** $q_{\mathrm{val}}^\alpha=q(2^\alpha-1)$
  com $q=q_{\mathrm{val}}=5$ tem raiz 0,6509186, que é exatamente
  $\eta_{5,BP}\approx0{,}650919$; e $\alpha=0{,}678$ dá
  $q_{\mathrm{val}}=5{,}05398$, o valor que o `run_deep.sh` de fato usa.
  A construção é internamente coerente.
- **12,6 e 4,1 sigmas** da corrida de produção: 12,53 e 4,05. Conferem.
- **0,038 e $\Delta=0{,}027$**: $0{,}650919-0{,}6131=0{,}03782$ e
  $0{,}678-0{,}650919=0{,}027081$. Conferem.
- **"The separation widens with depth"**: 0,0229 na década $10^7\to10^8$
  (grade b13) contra 0,0282 em $10^9\to10^{10}$. Confere.
- **Atribuição a KL e a Volkov.** Lida no PDF primário: Theorem 8.10 dá
  $\eta_{5,BP}\approx0{,}650919$; o Remark seguinte dá
  $\eta^\ast_{5,BP}\approx0{,}678$ de Volkov, com a notação-estrela que o
  paper usa. A caracterização do modelo de Volkov na discussão do paper
  ("complete binary tree", "different encoding of the iterates") é fiel
  ao que KL escrevem. (O que não é fiel é a paráfrase sobre o dado:
  C-06.)
- **Bibliografia.** Duas chaves citadas, `KontorovichLagarias2009` e
  `PressureCompanion`; dois `\bibitem`, os mesmos dois. Nada órfão, nada
  pendurado.
- **Repositório de reprodutibilidade.** `collatz-kl-volkov` existe, está
  populado (`sec5-fixed-window-estimator/`, `sec6-calibrated-comparison/`
  com `data/` e README por subpasta, em EN e PT-BR), tem remoto
  `git@github.com:faculdade/collatz-kl-volkov.git` e está sincronizado
  com `origin/main`. A frase de Data Availability é verdadeira. (Um
  número dentro dela não é: C-09.)
- **Variância de comprimento de frase** (Regra 4b §2, o item que ela
  chama de mais importante): 43 frases no corpo, média 26,1 palavras,
  desvio 19,4, oito abaixo de dez palavras e nove acima de quarenta. O
  ritmo balança. Passa com folga.

### Nota de Regra 8e (caminhos que esta crítica abriu)

Não são achados; são leads que apareceram enquanto eu procurava erro e
que, por Regra 8e, não devem morrer aqui dentro. Registrar em
`HYPOTHESES.md`/`hypotheses/` como `backlog`, marcados com origem
"CRITIQUE paper 04, rodada 1":

1. **O controle `iid` é o próprio modelo de KL.** Ele é o passeio
   aleatório ramificado com classe sorteada em cada nó, que é
   literalmente o que o Theorem 8.10 analisa. Ou seja: o experimento
   mediu o quanto o *modelo de KL* subestima sob esse estimador (0,038)
   e o quanto a *árvore aritmética* subestima (0,013 na mesma corrida).
   Essa diferença de viés entre modelo e aritmética é uma medida direta
   de quanto a árvore aritmética flutua menos que o modelo que a
   pretende descrever, o que é uma quantidade de interesse próprio para
   a linha de endogenia, e não é reportada em lugar nenhum.
2. **A leitura profunda fica sistematicamente abaixo de 0,650919.** O
   E-139 registra 0,6505 contra $\alpha_-(5)=0{,}650919$ e observa que
   `arith` flutua menos que o controle, o que colocaria seu expoente "a
   hair below" a previsão. O E-139 classifica isso como caveat. Se for
   real e não ruído de extrapolação, é um desvio mensurável entre a
   árvore aritmética e o modelo de ramificação, exatamente o tipo de
   coisa que esta linha de pesquisa procura, e merece uma passada
   dedicada em vez de uma nota de rodapé.
