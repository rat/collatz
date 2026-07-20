# Estado atual — Collatz

Última atualização: 2026-07-20

## Iniciado paper 03: catálogo de alegações de prova/refutação completa

Pedido do diretor científico: "vamos iniciar o paper sobre erros dos papers
ao tentar provar a conjectura?". Havia ambiguidade real de escopo entre 3
itens do BACKLOG (5, 7, 8) — perguntei diretamente e o diretor confirmou:
**apenas alegações de prova/refutação completa**, não qualquer paper
Collatz-adjacente (isso continua sendo o item 8, aberto, não iniciado) nem
o erro de rotulagem do Pratiher (item 7, categoria diferente — fica de
fora). Levantamento (BACKLOG.md item 8, `literature/unverified-proof-claims.md`,
`literature/papers/INDEX.md`) encontrou **12 casos** já revisados a fundo:
Getachew/H-079, Spencer×2/H-081+H-085, Santos 2018, Halemane(CTUHSK)/H-043,
Mohammed/H-045, Boyle/H-065, Roif/H-096, Yun/H-068, Tynski/H-093, disputa
Syzdykov×2/H-094+H-098 (+ nota crítica Lafontaine & Cheong), Barghout/H-116
— nenhum é prova válida. Criado `papers/03-alegacoes-de-prova-refutadas/`
com `OUTLINE.md`: estrutura em 5 seções, com uma **taxonomia de 7 padrões
de erro recorrentes** (A-G) como contribuição central, não só a lista de
casos. Absorve o item 5 (Santos) — atualizado no BACKLOG.md. Item 9 novo
no BACKLOG.md registra o paper como "em andamento". Duas decisões deixadas
em aberto no OUTLINE.md para o diretor: idioma (dual EN/PT-BR como o paper
01, ou só um) e nível de formalidade (nota curta vs. paper completo por
caso). Nenhuma redação do corpo do paper começou ainda — só a estrutura.

## H-130 entrou no paper como nota de rodapé compacta

Diretor científico perguntou se H-130/H-126 agregariam valor ao paper.
H-126 já estava incorporada (Remark de ortogonalidade, rodada
anterior). Para H-130, ofereci 3 opções (nota compacta / subseção
completa / não incluir agora); escolhida: **nota compacta**. Estendida
a nota de rodapé já existente sobre a família de escala (E-103
Estágio 4, §3, discussão da Conjectura do índice de cauda) com 2-3
frases sobre o colapso de posto 1 e a menção a Artin (com citação real,
Hooley 1967, verificada). `E-109` mirrorado em
`collatz-endogeny/sec3-pressure-equation/` (`experiment_type_rescaling_sterility.py`
+ `tree_lib_sterility.py`), com seção de resultado nos dois READMEs.
PDFs recompilados limpos (main.pdf: 31 páginas; main-pt-br.pdf: 33
páginas — nota coube no espaço já existente, sem página nova).

## H-130 resolvida (a favor da opção (i)) — cálculo de autovalor de posto 1

Pedido "tente resolver as hipóteses em aberto" (após 2 confirmações
empíricas, q=7 e q=15, para a família de escala por tipo). Consulta ao
Opus (máximo esforço) entregou o argumento analítico que faltava: a
matriz média multitipo do smoothing transform, restrita aos tipos
férteis ($\langle2\rangle$), é de **posto 1**. O autovalor de
Perron-Frobenius dessa matriz restrita colapsa, por um cancelamento
$d$-independente ($a_0$ é bijeção $\langle2\rangle\to\{1,\ldots,d\}$),
para exatamente $\rho(s)=q^{s-1}/(2^s-1)$ — **a mesma equação de
pressão do Teorema 3.3**, independente de quantos tipos extras são
estéreis. **Verifiquei a álgebra por conta própria** (o fator
$(1-2^{-ds})$ cancela mesmo, re-derivei à mão) antes de aceitar.
Consequência: expoente θ e a direção do autovetor
$C_i\propto2^{-a_0(i)\theta}$ sobrevivem intactos à esterilidade
extra — exatamente a opção (i). A opção (ii) (estrutura por coset) foi
descartada estruturalmente, não só empiricamente: só existe UM coset
fértil (o próprio $\langle2\rangle$); os demais são inteiramente
estéreis, então "comparar cosets" não tem conteúdo.

**O que ficou de fora (ressalva, não invalida o veredito)**: o
posto-1 é exato no MODELO i.i.d.; para a árvore aritmética real, ainda
depende da mesma hipótese de equidistribuição já registrada como
lacuna padrão do projeto (`rem:transfer-basis`) — não é uma lacuna
nova, específica de H-130. H-130 agora está com status "resolvida a
favor da opção (i)" no arquivo, com a seção "Resolução" documentando
o argumento completo em três camadas (expoente provado; razão de
escala exata no modelo + empírica em 3 casos; forma/W* comum exata no
modelo + empírica de cauda em q=5).

## Dois testes adicionais (pedido: "testar ambos, um por vez"), um deles rendendo a melhor resolução do item 1 até agora

Depois do quase-erro de reticulado (autocorrigido), diretor científico
pediu para testar mais duas pontas: o passo 2 de H-130 (q=7) e o
seguimento do item 1 (braço de calibração dependente de Δ).

- **H-130, passo 2 (`E-109`)**: a família de escala por tipo
  ($W_i\sim2^{-a_0(i)\theta}W^*$, já confirmada para q=5 em E-103
  Estágio 4) sobrevive entre os 3 tipos não-estéreis de q=7
  ($\langle2\rangle=\{1,2,4\}$) apesar da esterilidade extra em
  $\{3,5,6\}$? **Sim** — 5000 raízes por tipo, todas as razões
  $W_i/W_j$ batem com a previsão a 2–4% (mesma faixa de precisão do
  achado original para q=5). q=31 (caso mais extremo de H-130) foi
  descartado como inviável ($\theta\approx0{,}0552$ exigiria
  $H\sim10^{36}$).
- **Item 1, seguimento (`E-110`) — resultado melhor do que o esperado**:
  ao tentar construir um braço de calibração com acoplamento
  dependente de Δ, descobri algo mais forte: no próprio simulador de
  H-111, o TIPO do filho (`(rho_phase+k)%3`, exatamente Z_i em
  precisão ℓ=1 da Prop.2) é função determinística só da fase da raiz e
  do índice do ramo, **independente do parâmetro ρ** que o Braço 2
  varia (testado em 2000 seeds, 0 divergências) — e essa estrutura
  determinística reproduz a correlação exata +1/-1/2 de Prop.2 até a
  4ª casa decimal. **Isso substitui a "diluição" como resolução
  primária**: a correlação grosseira e o acoplamento medido por ρ_eff
  não competem porque medem eixos ortogonais (resíduo determinístico
  vs. conteúdo/magnitude aleatório) — ρ_eff≲0,06 nunca poderia ter
  detectado nem deixado de detectar a correlação de Prop.2. O Remark
  do paper (`rem:calibration-consistency`) foi reescrito para liderar
  com esse argumento estrutural, mantendo a diluição e o E-108 (-3/7)
  como pontos secundários.

**Correção de bookkeeping**: a citação do E-108 no paper apontava para
`collatz-endogeny/sec4-endogeny-barrier/`, mas a Proposição que ele
verifica (Prop. 2, "Endogenia grosseira exata") vive na §10 do paper,
não na §4. Corrigido nos dois idiomas; `delta_weighted_correlation.py`
movido para `sec10-l2-refutation-and-jensen/` no mirror; `E-110`
(`verify_orthogonality.py`) colocado em `sec5-rho-eff-control-experiment/`
(onde o simulador que ele testa realmente vive).

PDFs recompilados limpos (main.pdf: 31 páginas; main-pt-br.pdf: 33
páginas).

## Quase-erro autocorrigido: reticulado vs. coset na Proposição condicional (prop:transition-fine)

Ao perguntar "existe algo mais a testar?", verifiquei por conta própria
(Python) a estrutura de deslocamentos do passeio aleatório ramificado
usado em `prop:transition-fine` e cheguei a uma conclusão ERRADA: que
o processo seria reticulado (span log2), contradizendo a frase já
escrita no paper ("hipótese não-reticulada vale já que log(q)/log(2) é
irracional"). Ia "corrigir" o paper baseado nisso.

**O erro era meu, não do paper.** Consultei o Opus (máximo esforço)
antes de agir, e ele identificou o deslize com precisão: confundi
"os deslocamentos estão contidos num único coset do reticulado log(2)ℤ"
(verdade) com "o processo é aritmético/reticulado" (falso) — a
definição de Feller de aritmeticidade é sobre o MENOR SUBGRUPO FECHADO
gerado pelos deslocamentos (que passa pela origem), não sobre estar
contido num coset qualquer. Aqui esse subgrupo é
log(q)ℤ+log(2)ℤ — denso em ℝ porque log(q)/log(2) é irracional. O
texto original estava certo; a irracionalidade É o fato operante.

Confirmado também que isso é totalmente consistente (não em tensão)
com a análise diferente já feita em H-129/E-103 Estágio 2 (dicotomia
aritmético/não-aritmético de Goldie para os multiplicadores A_a^θ na
cauda de W, um objeto distinto de N(x) mas que consome a mesma
irracionalidade log(q)/log(2) como input).

**Ação**: Opus fortaleceu a justificativa no paper (nos dois idiomas)
para blindar contra um revisor que cometesse o mesmo deslize
coset-vs-subgrupo — sem remover nem enfraquecer nenhuma alegação.
PDFs recompilados limpos (31/33 páginas).

**Lição**: ao "verificar" uma alegação matemática já escrita, não
bastava reproduzir um cálculo parcial (a estrutura de coset) e concluir
— era preciso checar a definição exata do critério relevante (aqui,
aritmeticidade de Feller) antes de declarar contradição. Bom sinal:
não apliquei a "correção" sem antes consultar o Opus, mesmo com alta
confiança na própria derivação.

## Quatro pontas de pesquisa abertas pela auditoria, testadas nesta sessão

Depois da 4ª rodada de auditoria, diretor científico perguntou se as
correções abriram margem para pesquisa nova. Identifiquei 4 pontas
concretas e testei todas, na ordem escolhida (mais barata primeiro).
Fable ficou indisponível no meio do processo (confirmado pelo diretor
científico — ver `feedback_fable_unavailable_use_opus.md` na memória);
uma chamada isolada ainda funcionou (usada para o item 2), mas Opus é
agora o substituto padrão para julgamento matemático externo.

- **Item 1 (resolvido, resultado exato novo)**: a soma ponderada por Δ
  da correlação grosseira de H-126/Prop.2, sob a medida natural de
  segundo momento (peso ∝ 2^-a_i·2^-a_j), dá **E[Corr] = -3/7 exato**
  (P(Δ≡0 mod6)=1/21, P(Δ≢0 mod6)=20/21) — confirma o sinal negativo
  previsto para a reconciliação com a calibração de H-110, com
  magnitude não-trivial. Novo experimento `E-108`, mirrorado em
  `collatz-endogeny/sec4-endogeny-barrier/`. O Remark do paper
  (`rem:calibration-consistency`) atualizado para citar o valor exato
  em vez de só "plausivelmente negativo". H-126 atualizada.
- **Item 2 (resolvido, citação melhorada)**: busca dirigida + Fable
  (única chamada que funcionou) confirmaram que não existe extensão
  pronta de Nerman (1981) para reprodução bilateral que dê N(x)~Wx^α;
  a distinção entre "renovação de contagem cumulativa" e "cauda de
  equação de ponto fixo" é real (confirmada via fetch dos PDFs de
  Jelenković-Olvera-Cravioto 2012 e Alsmeyer-Biggins-Meiners 2012).
  Veredito: não rebaixar para Conjectura (não há evidência contra o
  enunciado, só uma lacuna técnica real com ferramentas padrão
  disponíveis) — reescrita a Proposição condicional (`prop:transition-fine`)
  citando a maquinaria vizinha certa em vez de "estendendo Nerman"
  vagamente, e um preprint recente (Villemonais–Zalduendo 2025,
  arXiv:2512.07653) registrado como pista a verificar, não como
  resolução confirmada.
- **Item 3 (nova hipótese aberta)**: a esterilidade extra da árvore
  reversa quando 2 não é raiz primitiva mod q (achado da correção da
  §2) conecta à Conjectura da Raiz Primitiva de Artin — tabela para
  q=3..61 mostra que mesmo q primos às vezes falham (q=7,17,23,31,...),
  com q=31 como caso extremo (25/30 resíduos estéreis). Registrada como
  `H-130`, aberta — não afeta o Teorema 3.3, mas levanta pergunta sobre
  se a esterilidade extra introduz estrutura por coset de ⟨2⟩ na
  constante W_u. Nenhum experimento formal ainda, só exploração
  numérica preliminar.
- **Item 4 (fechado, negativo mas registrado)**: busca dirigida não
  achou redução conhecida na direção reversa do Regime 3 (nem
  Spiegelhofer⟹decaimento de Fourier, nem o inverso). Consistente com
  o veredito já registrado em H-115 há 7 rodadas ("não perseguir mais
  por analogia"). A reformulação unidirecional do paper ("ao menos tão
  difícil quanto") já é a alegação mais forte defensável — não precisa
  de mudança adicional. H-115 atualizada com o adendo.

PDFs recompilados limpos (main.pdf: 31 páginas; main-pt-br.pdf: 32→33
páginas).

## Quarta rodada de auditoria: 4 defeitos lógicos estruturais corrigidos (Fable indisponível, Opus consultado)

Uma quarta auditoria (focada em estrutura lógica, não aritmética) achou
7 problemas, ranqueados por gravidade. A consulta ao Fable falhou por
limite de sessão (reset 3:30am); diretor científico pediu para
consultar o Opus no lugar. Itens 1-4 (os "defeitos lógicos reais",
segundo a auditoria) foram decididos com o Opus; itens 5 e 7 resolvidos
sozinho, com verificação computacional própria.

- **Item 1 (o mais grave): tensão §5 (calibração, ρ_eff≲0.06, "nenhum
  acoplamento detectado") vs. Proposição 10.2 (correlação grosseira
  exata ±1/-1/2, provada, persistente).** Veredito do Opus: NÃO é
  contradição, é lacuna de exposição — as duas seções medem objetos
  diferentes (correlação de par único em precisão grosseira vs.
  variância agregada de contagens reais) e a correlação grosseira,
  embora exata e persistente por par, é diluída a uma fração
  evanescente da variância agregada conforme a profundidade cresce
  (exatamente a taxa do sinal observado). Adicionado um Remark
  (`rem:calibration-consistency`) explicando a ponte, nos dois idiomas.
- **Item 2: dupla contagem no argumento de "sete rotas
  independentes".** Procedente parcialmente: WCC≅β=1 é identidade
  provada (não analogia), e a condição L² + dicotomia espectral de
  Prop C partem da mesma decomposição de Fourier de segundo momento —
  confirmei isso eu mesmo relendo §8.2. Recontado 7→5 vocabulários
  genuinamente distintos, propagado por todo o paper: título, resumo,
  lista de contribuições da introdução, `thm:propC`, a subseção de
  Chang (agora "quinto vocabulário"), e o parágrafo principal da
  Discussão — em ambos os idiomas.
- **Item 3: teoremas de "barreira" sem classe de argumentos
  formalizada** (`thm:barrier`, `thm:regime3`). Veredito: o problema é
  a precisão do enunciado, não o rótulo do ambiente (ao contrário do
  caso `empirical` da rodada anterior). `thm:barrier` dividido em
  Teorema (só o que é rigoroso: gauge + exclusão 2-ádica) + Observação
  `rem:barrier-reading` (a leitura informal de barreira, com aviso
  epistêmico explícito de que "usa apenas (i),(ii)" não é uma classe
  formalizada). `thm:regime3` reformulado de "equivalente em
  dificuldade" para uma redução direcional precisa ("é ao menos tão
  difícil quanto"). `thm:no-transfer` mantido intacto (cada item já é
  verificável).
- **Item 4: hipótese não verificada dentro do corpo de um Teorema**
  (a extensão de Nerman em `thm:transition-model`). Confirmado como
  problema de rigor real. Dividido em Teorema (só Biggins, log N/log x
  → α, sem cláusula não verificada) + Proposição condicional nomeada
  `prop:transition-fine` (a assíntota fina via Nerman, com a hipótese
  não verificada explicitamente isolada como a condição da proposição).
- **Item 5 (resolvido sozinho, com verificação computacional)**:
  confirmei em Python que TODAS as 4 raízes usadas no teste de
  congelamento de q=5 (não só a de q=3) tocam o ciclo trivial {1,3} do
  mapa T5. Reescrito o parágrafo para declarar isso e apontar para onde
  está a evidência genuína de ambiente genérico.
- **Item 6 (ligado ao item 1): ρ_eff≲0.06 é relativo à família de
  acoplamento do Braço 2, não a toda forma de acoplamento.** Escopo
  declarado explicitamente em §5, com referência cruzada ao Remark do
  item 1.
- **Item 7 (resolvido sozinho)**: Conjectura 3.7 (q=3) "implica e
  refina estritamente" a Growth Exponent Conjecture (que afirma só o
  expoente, x^(1+o(1))), não é "exatamente" ela — nossa conjectura
  afirma também uma constante assintótica específica.

PDFs recompilados limpos nas duas versões (main.pdf: 30→31 páginas;
main-pt-br.pdf: 31→32 páginas). Escopo desta rodada foi maior que as
três anteriores — tocou título, resumo, introdução, 3 seções internas,
a Discussão, e a Conclusão.

## Terceira rodada de auditoria externa: erro matemático real na §2 + 2 correções menores

Uma terceira auditoria (rederivação analítica + reimplementação
computacional independente de tudo verificável) confirmou o núcleo
matemático como sólido, mas achou um erro real na §2 e duas
correções bibliográficas/terminológicas menores:

- **Erro real, corrigido — admissibilidade na §2**: o texto afirmava
  "existe um único a₀(u) com 2^a₀(u) u ≡ 1 (mod q)" para todo u
  coprimo com q. Falso quando 2 não é raiz primitiva mod q: para q=7,
  ord₇(2)=3 < φ(7)=6, e verifiquei eu mesmo (Python) que u≡3,5,6
  (mod 7) não têm expoente admissível algum — são estéreis também,
  não só u≡0. **Boa notícia**: o código real usado para gerar os
  números de q=7 (`E-097-qx1-empirical-gate/empirical_qx1_tree.py`,
  linha 38-39) já tratava isso corretamente (`if a0 is None: continue
  # classe sem filhos (r fora de <2>)`) — o erro era só na prosa da
  §2, nenhum resultado numérico precisa ser refeito. Também confirmei
  que a prova do Teorema 3.3 (identidade de pressão) não depende da
  alegação errada — ela usa a bijeção na direção reversa (sequência
  de expoentes → raiz única), nunca a existência de a₀(u) para todo
  u. Reescrito o parágrafo da §2 para descrever a condição correta
  (⟨2⟩ ≤ (Z/qZ)˟, sterility fora do subgrupo), citando explicitamente
  q=7 como exemplo e explicando por que Teorema 3.3 e a enumeração de
  §6.2 não são afetados.
- **Referência bibliográfica errada, corrigida**: a citação de Halász
  apontava para o paper de 1971 sobre valores médios de funções
  multiplicativas (com uma ressalva no Agradecimento admitindo não
  ter sido possível verificar a fonte), mas a ferramenta realmente
  usada no paper (Proposição do déficit de Halász, §10/lemmas) é a
  estimativa de função de concentração — Halász (1977), Periodica
  Mathematica Hungarica 8, 197-211. Verifiquei via WebSearch que este
  paper existe exatamente com esse título/volume/páginas (DOI
  10.1007/BF02018403). Bibitem e Agradecimento corrigidos nos dois
  idiomas.
- **Terminologia**: "Richardson extrapolation" (4 ocorrências em cada
  idioma) renomeado para "Aitken Δ² extrapolation", consistente com o
  método realmente descrito no texto (§6.3 já dizia "Aitken's Δ²
  extrapolation" numa passagem, as outras 4 diziam "Richardson"
  inconsistentemente). Não mexi no repositório collatz-endogeny (o
  script `experiment_gate_richardson.py` e seus READMEs mantêm o nome
  "Richardson" — decisão deliberada de não renomear arquivo/histórico
  git por uma nomenclatura cosmética; o comentário do próprio script
  já esclarece "Richardson (Aitken Delta^2)").
- **Confirmado correto** (nesta auditoria, sem correção necessária):
  Teorema 3.3, Proposição 3.5, raízes/limiares, Lema 4.2, Proposições
  8.1/10.2/11.1, Teorema 10.12, recursões de §9.3/§10.1, tabela j*,
  aritmética de §6, e a fidelidade das citações a Kontorovich-Lagarias,
  Baker-Banaji e Chang (2026) — auditor rederivou/recomputou tudo de
  forma independente (sem usar nosso código) e bateu em todos os
  casos verificáveis em tempo razoável.
- **Repositório**: não foi contestado desta vez — a auditoria confirma
  que existe, é público, e a estrutura de pastas corresponde
  seção a seção às alegações do paper.

PDFs recompilados limpos (main.pdf: 29 páginas; main-pt-br.pdf: 30→31
páginas).

## Segunda rodada de auditoria externa: 9 correções adicionais aplicadas

Uma segunda auditoria (verificação linha a linha da primeira rodada de
correções) confirmou as duas correções matemáticas de fundo (Teorema
3.6/Conjectura 3.7, Teorema 10.12) como corretas, mas achou defeitos
novos e pendências reais:

- **Repositório**: a auditoria insistiu, pela segunda vez, que
  `github.com/faculdade/collatz-endogeny` não existe/é placeholder.
  Reconfirmado (de novo) via `curl`/API do GitHub: HTTP 200,
  `private: false`. A auditoria está errada — provavelmente busca sem
  indexação de um repo pushado no mesmo dia. Nada a corrigir.
- **Vazamento de português no `main.tex` em inglês** (real, corrigido):
  "cauda"→"tail" (2x, Resultado Empírico de Wirsching Conjectura 3) e
  "roupagens"→"guises".
  Ambos no bloco de teoria de Wirsching.
- **Grafia inconsistente** (real, corrigido): "Goldie/Guivar'ch" →
  "Goldie/Guivarc'h" (a própria bibliografia já grafava certo).
- **Arredondamento** (real, corrigido): "Λ≈0,5834" → "0,5836" (log γc =
  0,583600...; o Monte Carlo do paper, 0,58344±0,0005, já era
  consistente com o valor certo).
- **Contagem inconsistente** (real, mas só num lugar — não em todo o
  paper como a auditoria sugeriu): "six independent angles" no
  parágrafo final da §12 deveria ser "seven" (a mesma seção já tinha
  estabelecido 7 rotas duas páginas antes). Corrigido.
- **Referência cruzada quebrada** (real, corrigido): "§sec:regimes"
  (que é a seção dos 3 regimes de Tao, sem relação) apontava
  erroneamente para a medição Hill/EVT de q=3 → corrigido para
  "§sec:pressure" (onde essa medição realmente é discutida).
- **Ciclos na enumeração de T₅/T₇** (real, corrigido): §6.2 não
  declarava que a árvore reversa tem ciclos genuínos (ex.: {1,3} em
  q=5: w₄(1)=3, w₁(3)=1 — verifiquei isso eu mesmo e confirmei contra
  o código real do mirror, que já exclui `CYCLE5 =
  {1,3,13,33,83,17,27,43}` via um set `seen`). Adicionado parágrafo
  explicando o mecanismo real usado.
- **Precisão do Teorema 3.6/modelo i.i.d.** (real, corrigido após
  consulta ao Fable): o enunciado dizia "N(x)~x" em q=3 sem fator
  aleatório W, mas com W_u explícito em q≥5 — inconsistente, já que a
  degenerescência de W é propriedade da lei de reprodução (variância
  genuína em ambos os casos), não do valor de α₋. Fable também apontou
  que Biggins 1992 sozinho só sustenta a transferência ao nível do
  *expoente*; a assíntota fina N(x)~W·x^α exige o teorema de renovação
  de Nerman (1981, C-M-J), agora citado. Reescrito em dois níveis
  (expoente via Biggins; assíntota fina via Nerman, com W não-degenerado
  em todo q≥3 incluindo q=3), com duas ressalvas honestas: condição
  não-reticulada favorável (log q/log 2 irracional), e deslocamentos
  negativos exigindo a extensão padrão de Nerman (hipóteses não
  verificadas em detalhe).
- **Rótulos "Theorem" em resultados empíricos** (mudança de decisão,
  após segunda consulta ao Fable): na primeira rodada mantive
  Teoremas 6.1/7.2/9.4 como estavam (título já autodeclarava
  "empirical"/"numerical test"). Fable mudou de veredito na segunda
  consulta: a autodeclaração no título mitiga engano mas não corrige o
  erro de categoria ("Theorem" com IC/AIC/p-valor dentro do enunciado é
  incoerente com a disciplina epistêmica que o próprio paper acabou de
  aplicar ao rebaixar o Teorema 3.6). Custo de correção é trivial
  (contador compartilhado, numeração 6.1/7.2/9.4 preservada). Criado
  ambiente `\newtheorem{empirical}{Empirical Result}` e migrados os 3
  ambientes + ~5 referências cruzadas. O Teorema 10.3 (refutação L²,
  `thm:l2-refutation`) foi mantido como Teorema — é dedução exata via
  recursão fechada, não medição estatística, categoria diferente.

PDFs recompilados limpos nas duas versões (main.pdf: 29 páginas;
main-pt-br.pdf: 30 páginas).

## Auditoria externa do paper (pré-envio ao Igor): 3 correções aplicadas

Diretor científico rodou uma auditoria sistemática externa do paper
(matemática, referências, código) antes de enviar a Igor. Achados
verificados de forma independente e triados:

- **Falso**: a auditoria afirmou que o repositório
  `github.com/faculdade/collatz-endogeny` "não aparece em nenhuma
  busca" / parecia placeholder. Confirmado via `curl`/API do GitHub
  que o repo existe, é público e está com o conteúdo certo — a busca
  do auditor só não indexou ainda porque o push foi feito nesta mesma
  sessão. Nada a corrigir.
- **Correto e corrigido — Teorema 10.12 (identidade de Jensen)**: a
  prova usa `p≥1/2` explicitamente, mas o enunciado não tinha essa
  hipótese. Adicionada. Sem impacto downstream (aplicado em
  $p_c\approx0{,}558\ge1/2$).
- **Correto e corrigido, após consulta ao Fable — Teorema 3.6
  ("Structural transition: density")**: rotulava como Teorema uma
  afirmação (densidade positiva/nula da árvore reversa real) que para
  q=3 é *literalmente* a Conjectura do Expoente de Crescimento de
  Applegate–Lagarias (aberta desde 1995) e para q≥5 não tem prova para
  a árvore aritmética — só para o modelo estocástico i.i.d. + suporte
  empírico. O Fable apontou a inconsistência decisiva: o próprio paper
  já usa esse critério para rebaixar a conjectura irmã do tail-index
  (`conj:tail-index`) a Conjectura, então o Teorema 3.6 tinha que
  seguir o mesmo padrão. Dividido em `thm:transition-model` (rigoroso,
  só para o modelo i.i.d., via Biggins 1992) +
  `conj:transition-arithmetic` (árvore real, conjectura, com a conexão
  a Applegate–Lagarias tornada explícita — ganho de framing, não
  fraqueza). Novo item (O8)/(A8) na lista de problemas abertos. Todas
  as referências cruzadas no `main.tex`/`main-pt-br.tex` atualizadas.
- Corrigido também: "fifteen-year-old dispute"/"disputa de quinze
  anos" (Volkov 2006, KL 2010 — em 2026 são 16-20 anos, não 15) →
  "long-standing"/"de longa data", para não ficar datado.
- **Avaliado e mantido como estava** (discordância da auditoria):
  Teorema 7.2 ("Regime 3 is a recognized open problem") é uma
  afirmação de equivalência de dificuldade, não overclaim; Teoremas
  6.1 e 9.4 (resultados empíricos) já se autodeclaram "empirical"/
  "numerical test" no próprio título do teorema, sem informação
  enganosa.

PDFs recompilados limpos nas duas versões (main.pdf: 28→29 páginas;
main-pt-br.pdf: 29→30 páginas). Nenhum código novo foi necessário —
edições são só de enunciado/enquadramento, sem nova alegação
computacional.

## Nota de rodapé sobre família de escala (E-103 Estágio 4) adicionada ao paper

Diretor científico pediu avaliação de 3 achados da sessão como
candidatos a citação no paper: gap espectral (E-105), família de
escala por tipo (E-103 Estágio 4), constante de Bramson (H-129/E-104).
Avaliação: só a família de escala resolve o critério "agrega ao paper"
— os outros dois não resolvem nenhum problema já declarado em aberto
(O1-O7) e/ou dependem de framing nunca integrado ao texto. Adicionada
como nota de rodapé (a primeira do paper) em `main.tex`/`main-pt-br.tex`,
§3.3, logo após a citação da transformada de suavização multitipo na
Conjectura do índice de cauda. PDFs recompilados limpos (28/29 páginas).
Ver `hypotheses/H-129-q-adic-pole-analog-seymour.md`, seção (b) do
esforço final.

## H-127 — avançada (2026-07-19): duplicação E-106/E-101 corrigida, Lema B fica mais fraco (E-107)

Pedido explícito do diretor científico para avançar H-127 depois de
fechar H-129. Duas ações:

1. **Erro cometido e corrigido**: acreditei numa nota do próprio
   H-127 dizendo que `lambda_mc.py` "não estava persistido como
   experimento formal", sem checar a pasta de experimentos primeiro —
   criei um E-106 duplicado. Uma auditoria de reprodutibilidade
   posterior (pedida pelo diretor científico) revelou que
   `E-101-jensen-constant-annealed-fourier-budget` JÁ EXISTIA (criado
   na sessão original de H-127, 2026-07-17) com o mesmo script, e já
   estava espelhado em `collatz-endogeny/sec10-l2-refutation-and-jensen/`.
   E-106 removido; H-127 corrigida para referenciar E-101. Lição:
   checar a pasta de experimentos antes de confiar numa nota interna.

2. **Etapa 6 do Lema B investigada a fundo** (upgrade "configuração
   diagonal"⟹"segmento contínuo", marcada como "plausível mas não
   escrita"). Consulta ao Fable + verificação numérica independente
   (reproduzi os números do script dele antes de aceitar a conclusão)
   revelou algo mais sério que uma lacuna técnica: a Definição 2
   (configuração diagonal), como estava escrita, é **VAZIA** —
   satisfeita por ξ genérico, incluindo ξ=1
   (`E-107-h127-def2-vacuity-check`). O objeto com conteúdo real é um
   segmento ENCADEADO de comprimento ≫log ℓ, e as duas rotas possíveis
   para prová-lo **não fecham** com as ferramentas em jogo:
   estabilidade em j esbarra numa média convexa de Pascal (não
   convolução — o ξ maximizante migra livremente entre j e j+1, sem
   controle); encadeamento intra-j só dá comprimento O(1/η(ε)),
   constante, não crescente com ℓ. **Mesma parede de constantes da
   Proposição C, terceira aparição.**

**Avaliação honesta**: isso é um retrocesso real no Lema B
especificamente — mas bem entendido, com mecanismo exato identificado,
não "faltou tempo". Seguindo a recomendação do Fable, a Etapa 6 foi
reclassificada de "lacuna técnica plausível" para "problema em aberto
explícito", e a recomendação para o paper foi atualizada: o Lema B não
deve entrar como estava. A Proposição C (o resultado negativo,
independente do Lema B) permanece sólida e agora mais bem verificada.

**Status de H-127**: continua "em revisão". Ver
`hypotheses/H-127-reducao-z-number-dicotomia-espectral-wcc.md` para o
registro completo, `experiments/E-101-jensen-constant-annealed-fourier-budget/`
e `experiments/E-107-h127-def2-vacuity-check/`.

## H-129 — status final da sessão de 2026-07-19 (consolidado)

Sessão inteira dedicada a H-129 a pedido explícito do diretor
científico ("puxar o H-129 primeiro", depois "tente fechar a H-129
usando todos os recursos disponíveis"). Sequência completa de achados,
do primeiro ao último:

1. **Gap espectral do operador de transferência — FECHADO, PROVADO**
   (E-105). Consulta ao Fable formalizou o operador certo (dual M_α,
   pai→filho, distinto do Koopman L_α já provado impossível como
   estado finito): espectro de M_α é EXATAMENTE {Λ,0} em qualquer nível
   de truncamento — gap perfeito, sem autovalor subdominante isolado.
   Verificado numericamente (q=5 e q=7). O mecanismo Manneville-Pomeau/
   Sarig-Iommi (sem-gap) NÃO se aplica. Corrigida em H-109/E-103/paper
   a frase antiga errada "raiz complexa subdominante".
2. **Hipótese log-periódica para o transiente k^-0,222 — TESTADA,
   NÃO SUPORTADA** (E-103 Estágio 2). Fable derivou o período teórico
   antes do teste: sistema é não-aritmético (log₂5 irracional,
   dicotomia de Goldie) — sem log-periodicidade assintótica esperada.
   Periodograma pré-registrado confirmou: potência no nível de ruído
   em todos os 4 headrooms.
3. **Checagem de oscilação no eixo k — sem sinal, dados insuficientes
   para mais** (E-103 Estágio 3). Razão de incrementos de M_k(p)
   monotônica em k=5..11 (só 5-7 pontos, teto de memória 5^k). Uma
   tentativa de ajuste para localizar a origem de "0,222" foi feita e
   descartada por sub-poder (revisão do advisor). Origem de "0,222"
   segue sem localização.
4. **Pergunta LITERAL de H-129 (análogo do polo de Seymour) — FECHADA,
   REFUTADA.** Já estava resolvida desde 2026-07-18 (mecanismos
   categoricamente distintos); só precisava ser reconhecida como tal.
5. **Família de escala exata por tipo de resíduo do raiz — CONFIRMADA,
   mas não testa κ** (E-103 Estágio 4). Previsão do Fable
   (W_i =_d 2^(−a₀(i)θ)·W\*) bate com 2-9% de desvio em 4 headrooms
   independentes e 3 níveis de cauda. Revelou que κ cancela
   algebricamente nesse tipo de teste — confirma θ e a estrutura
   multi-tipo, não o índice de cauda.
6. **Tentativa de usar (5) para melhorar o teste de κ — sem ganho**
   (E-103 Estágio 5). Pool reescalado deu o mesmo padrão de sempre
   (consistente, não confirmatório); um sinal aparente de "lognormal"
   foi identificado como artefato de limiar caindo no corpo da
   distribuição, não na cauda.
7. **Amostra 20x maior (100.000 raízes) — evidência do índice de
   cauda passa de INCONCLUSIVA para FORTEMENTE FAVORÁVEL** (E-103
   Estágio 6, o resultado mais forte da sessão). GPD com platô de
   limiar limpo pela primeira vez em toda a investigação (ξ≈0,65 em
   todos os 9 limiares e 4 headrooms); Huisman muito estável cobrindo
   o previsto 1,536290; Vuong deixa de favorecer lognormal (era 3/4
   casos antes). Duas calibrações de sanidade (nulo sintético Pareto
   exato; invariância a um θ' deliberadamente errado) não revelaram
   artefato. **NÃO é confirmação/fechamento**: Vuong deu não-rejeição,
   não "lei de potência vence"; e W provadamente ainda não convergiu
   (mediana cai monotonicamente com o headroom mesmo com índice de
   cauda estável). Refletido no paper (`main.tex`/`main-pt-br.tex`,
   §3.3 e item O7 da conclusão, recompilados).

**Status final: H-129 permanece aberta**, mas em estado muito mais
claro que no início da sessão — a pergunta original tem resposta
(refutada), o mecanismo espectral está provado (gap perfeito), duas
hipóteses candidatas para o transiente k^-0,222 foram eliminadas
(log-periodicidade, oscilação em k), um resultado estrutural novo e
real foi estabelecido (família de escala por tipo), e a Conjectura do
índice de cauda — o núcleo que resta — tem agora a evidência mais
forte já reunida, embora ainda não seja uma prova. Único fio solto sem
ação identificada: a origem numérica de "0,222" nunca foi localizada.
Ver `hypotheses/H-129-q-adic-pole-analog-seymour.md` para o registro
completo (inclui dois erros de processo autocorrigidos com
advisor+Fable antes de reportar como confirmados) e
`experiments/E-103-tail-index-q5-rigorous-test/README.md` (Estágios
2-6) e `experiments/E-105-transfer-operator-spectral-gap/README.md`.

**Próximos passos concretos, se a linha for retomada**: (a) headroom
maior que 10⁸ na amostra de 100k, se o custo de DFS por raiz permitir;
(b) localizar a derivação original de "0,222" (busca, não cálculo); (c)
avançar H-127 (Etapa 6, promover `lambda_mc.py` a experimento formal) —
não tocada nesta sessão, ver "Hipóteses abertas" abaixo.

## Índice de cauda q≥5: investigação fechada como inconclusiva (paper atualizado)

Depois da bateria de 4 testes (ver seção abaixo), o diretor científico
pediu a bateria COMPLETA de estimadores (Gabaix-Ibragimov, Huisman,
GPD, CSN+Vuong) sobre o teste de índice de cauda q=5 — resultado misto
(Huisman estável perto do previsto, mas GPD sem platô e CSN+Vuong
favorecendo lognormal em 3 de 4 headrooms). Autorizada calibração
adicional (até 12h se necessário, ou k grande em enumeração exata).

Descartamos a ideia inicial de calibração (árvore i.i.d. de fase
aleatória) por dois motivos: (1) circular — o s* dela cai exatamente
na identidade de pressão anelada já provada, no ponto que já sabemos
estar sempre congelado; (2) e pior, a contagem BRUTA de nós explode
combinatoriamente sob fase i.i.d. (headroom=100: árvore real=42 nós,
sintética i.i.d.>200000 nós) — ver
`experiments/E-103.../stage0_iid_power_check.ABANDONED.py`.

**Teste decisivo executado**: momento populacional exato via DP
`Z_k(θ=0,650919; u)` sobre TODOS os resíduos mod 5^k (não amostra),
até k=11 (teto seguro de memória). M_k(1,0)=1,0 exato em todo k
(confirma implementação). M_k(p) satura para p≤1,6 e diverge para
p≥1,7 — mas a razão entre incrementos sucessivos ainda não estabilizou
para p≤1,6 (ao contrário de p≥1,7, já estável): assinatura de
desaceleração crítica, não evidência de índice mais alto. O transiente
conhecido de q=5 (k^-0,222 — ver correção de terminologia de 2026-07-19
abaixo, não é mais atribuído a uma "raiz complexa subdominante") cai só
~7% entre k=8 e k=11; k≈250 seria necessário para reduzi-lo pela metade —
inalcançável por enumeração exaustiva. **Veredito final: inconclusivo,
não desconfirmatório** — parado aqui, sem Estágio 2 (Markov-modulado,
~12h), conforme a regra de decisão combinada com o advisor.

**Paper atualizado** (`main.tex`/`main-pt-br.tex`, §3.3, e o problema
aberto O7 na conclusão): reescrito para reportar as duas rodadas
(bateria estatística + momento exato) honestamente, nem confirmando
nem refutando, com o motivo específico (transiente de convergência
lenta) em vez de deixar vago. Ambos os scripts espelhados em
`collatz-endogeny/sec3-pressure-equation/` (`full_battery.py`,
`exact_moment_test.py`). Ambos os PDFs recompilados limpos (28/29 pág).

**Frente paralela (H-129, aberta, não fechada)**: inspirada por um
paper externo (Jon Seymour, "Rigidity of the Syracuse Transition
Matrix", 2026, achado pelo diretor científico) sobre rigidez 2-ádica
do mapa Syracuse padrão (forward). A transcrição literal para nossa
árvore reversa NÃO funciona (mecanismo diferente — nosso "precisa de
mais um dígito" é universal, o dele é localizado numa sequência rara
convergindo a um polo). Mas abriu um reframing teórico do congelamento
via otimização ergódica/formalismo termodinâmico a zero (Mañé, Bousch,
Contreras-Lopes-Thieullen, Jenkinson), com confirmação parcial já
verificada por força bruta (a dinâmica gulosa nos resíduos recupera
exatamente o ciclo real mais simples de q=5 e q=7, mas não os ciclos
secundários de q=5). Ver `hypotheses/H-129-*.md` — não integrada ao
paper, próximo passo (Perron-Frobenius espectral) não executado.

## Bateria de 4 testes de acompanhamento à correção da §3 (H-109, addendum 2)

Depois de corrigir o erro da §3 (ver seção abaixo), o diretor científico
pediu "faça todos os testes, se precisar chame Fable. sejam
criteriosos e podem usar vou a vontade" — 4 testes, cada um com
consulta ao Fable + verificação independente minha:

1. **Índice de cauda q=5, teste mais robusto** (novo experimento
   `experiments/E-103-tail-index-q5-rigorous-test/`): amostra 8x maior
   (5000 raízes), 4 headrooms, Hill+bootstrap+Zipf. Resultado:
   estável entre headrooms, ponto na fração de 5% quase exato
   (1,58 vs 1,536 previsto), mas instável entre frações (1,39–2,10) —
   encorajador, não conclusivo. A Conjectura do índice de cauda para
   q≥5 continua conjectura, agora com evidência mais forte mas ainda
   não decisiva.
2. **Mais raízes/profundidade para o congelamento** (q=3 até k=22,
   q=5 até k=17, interrompido em k=20 por segurança de memória — memo
   crescia ~15x por passo): resíduo C_k confirmado O(1) (2,6–3,4 para
   q=3, 2,0–3,0 para q=5), como previsto pela fórmula assintótica do
   Fable.
3. **Teorema tipo Biggins**: confirmado que Biggins (1992) cobre a
   região não-congelada só para BRW genuíno (i.i.d.), não a recursão
   aritmética — mesma lacuna já nomeada no Teorema da barreira, agora
   quantitativa. Adicionado como Remark no paper.
4. **Por que os números de congelamento não batiam com a previsão
   ingênua**: resolvido — crescimento é log Z_k = A·k − B·log(k) + O(1),
   termo log(k) não-desprezível em k raso (cruzamento k≈139 para q=3,
   k≈407 para q=5). Não é bug, é regime pré-assintótico esperado.

Detalhes completos: addendum 2 de
`hypotheses/H-109-generalized-qx1-pressure-equation-exact-closed-form.md`.
Limitação reconhecida: o estimador de índice de cauda no Teste 1 não
inclui a correção rank−½ de Gabaix-Ibragimov recomendada pelo Fable;
bateria completa (GI, MLE de GPD, Clauset-Shalizi-Newman+Vuong) fica
como próximo passo se a linha for retomada.

**Ainda pendente**: decidir com cuidado se/como incorporar o resultado
do Teste 1 na Conjectura do índice de cauda em `main.tex`/`main-pt-br.tex`
(hoje o paper diz "sem teste empírico forte para q≥5" — o correto agora
é "teste maior existe, encorajador mas não decisivo", sem exagerar).

## Erro real na §3 do paper encontrado por revisão externa e corrigido (H-109)

Revisão externa achou um erro matemático concreto e correto na equação
de pressão qx+1 (§3 do paper): o mecanismo descrito ("automato de
resíduos mod q") não está bem definido — contraexemplo verificado
(q=3, u=1 vs u=7, mesmo resíduo mod 3, mesmo a, filhos em resíduos
diferentes). Consultei o Fable, verifiquei tudo independentemente (2
rodadas, scripts próprios, não copiados) e achei um conserto real: a
equação é uma identidade EXATA, mas sobre a média entre raízes (pressão
anelada), via um Lema de bijeção de fibra — provado e verificado por
força bruta. Achado extra (também verificado por mim, não só o Fable):
a raiz MAIOR da equação está **sempre congelada** (quenched≠anelado),
para todo q — fato estrutural provado (não numérico). Isso rebaixa o
índice de cauda do martingale (nosso α*=2 para q=3, e o análogo para
q≥5) de teorema a **conjectura** — bem sustentada empiricamente em
q=3 (3 confirmações independentes), mas **sem apoio sólido em q≥5**
(a medição de Hill já tinha sido sinalizada como não-confirmatória em
H-113). `main.tex`/`main-pt-br.tex` reescritos com Lema, Teorema,
Proposição e Conjectura novos; H-109 tem o addendum completo. Também
adicionada seção "Code and data availability" no paper apontando para
o repositório `collatz-endogeny` (GitHub). E-mail para o dono do canal
que originou este projeto (Igor Vinicius, Corre de PhD) fica em espera
até o diretor científico revisar esta correção.

## Estrutura nova: pasta `papers/` para resultado final (pedido do diretor científico)

Criada `papers/` (distinta de `literature/`, que é sobre papers de
terceiros): `papers/01-syracuse-qx1-endogenia/OUTLINE.md` tem o esboço
completo do paper principal (escopo H-109 a H-128, seção por seção,
apontando para as hipóteses-fonte) para a sessão que começar a redação
não precisar reminerar este STATE.md do zero. `papers/02-critica-
cumulativa-literatura/` é um stub apontando para BACKLOG.md item 8
(não iniciar sem pedido explícito). Também criado `protocols/
literature-search.md` (codifica o padrão de busca dirigida usado
repetidamente em H-112, H-116-125, H-124, H-128) e uma seção "Consultando
o Fable" em `CLAUDE.md` (o erro `subagent_type: "fable"` já foi
cometido antes — registrado para não repetir).

## Verificação bibliográfica das 7 referências de H-127 concluída (2026-07-18)

Diretor científico baixou 6 dos 7 papers citados de memória pelo Fable
em H-127 (`/home/rat/Downloads/papers`, arquivados em
`literature/papers/` itens 139-144). 5 confirmados exatamente contra o
texto primário (Tao-Vu 2009, Nguyen-Vu 2011, Flatto-Lagarias-Pollington
1995, Mahler 1968, Lagarias 2009 — inclusive a citação de Erdős 1979,
confirmada via referência [4] do próprio Lagarias). **Um erro real
encontrado**: Halász estava citado com o ano errado ("1977"; o certo é
1971) — e o PDF obtido é um adendo de 1972, não o paper original, que
ainda falta conseguir. `main.tex` e H-127 atualizados. Depois, resolvidas sem precisar de download novo (arquivos já em mãos
ou de acesso livre): **Gonçalves-Greenfeld-Madrid (2022)** — a
bibliografia do paper tinha um título INVENTADO/errado; corrigido para
o real ("Generalized Collatz Maps with Almost Bounded Orbits",
arXiv:2111.06170), conferido contra o PDF já arquivado (item 128); e
**Brémont (2021)** — volume/páginas confirmados (Annales Henri
Lebesgue 4, 973-1004) e o Teorema 2.5 citado pelo Fable verificado
palavra por palavra contra o texto completo (arXiv:1910.03463).
**Fechamento (mesmo dia)**: diretor científico buscou o Halász 1971
original em HathiTrust/Internet Archive/JSTOR/acervos húngaros — não
encontrado em digitalização aberta. Zeladoria bibliográfica de H-127
**encerrada**: 8 de 9 referências verificadas contra o texto primário,
1 (Halász 1971) documentada como inacessível por ora (não esquecida —
`main.tex` tem nota explícita). **A outra zeladoria também fechada (2026-07-18)**: diretor científico
confirmou que as equações do Wirsching (2003) são as mesmas entre a
versão preliminar em mãos e a versão final publicada na DCDS. **Toda a
zeladoria bibliográfica do paper está encerrada** — nenhuma pendência
de citação restante além da nota já documentada sobre Halász (1971,
inacessível, não esquecida).

## Segunda rodada de busca literária: nenhuma via nova, uma correção de terminologia útil (H-128)

Pedido explícito de continuar buscando. Três candidatos novos
avaliados com o Fable (Fuglede/Salem em Q_p, Li-Sahlsten renovação
quantitativa, Kolesko-Mentemeier caso crítico de smoothing transform)
— todos confirmam a mesma barreira, por razões técnicas específicas
verificadas (não intuição): a medida de Syracuse tem razão de
contração 3-ádica ÚNICA (1/3) em todo ramo, o que faz degenerar
qualquer técnica que dependa de múltiplas razões distintas ou de
sintonia fina de parâmetro. Único ganho real: confirmado que α*=2 é
"segunda raiz/cauda de Goldie" (m'(2)>0), não "caso crítico" — corrige
terminologia em H-110, evita reavaliar no futuro uma classe de papers
irrelevante para q=3. Ver H-128 para os detalhes. Não muda o próximo
passo.

## Os dois testes pedidos ("será que matam a charada?") foram feitos — não mataram, mas renderam achados honestos (H-128/E-102)

Pedido explícito: testar se Baker-Banaji ou Chang resolvem algo. Não
resolvem, mas: (1) Fable identificou que a medida de Syracuse É uma
medida autossimilar 3-ádica genuína, e que a maquinaria de decaimento
lento de Baker-Banaji trivializa nesse caso por rigidez de Z_3^× (todo
subgrupo fechado tem índice finito, sem espaço para "Pisot 3-ádico") —
observação nova, pequena, citável (meio parágrafo, não lema), vira
addendum em H-127. (2) A conjectura de "one-bit mixing" de Chang foi
testada computacionalmente em E-102: numa órbita única muito longa
(16000 bits, ~4761 eventos), o desvio de balanço acompanha ruído
~1/√i sem viés sistemático — suporte empírico qualificado, não prova.
Ver H-128 para os detalhes completos. Não muda o próximo passo.

## Busca literária dirigida em ângulos novos, pós-H-127 (H-128)

Pedido explícito: buscar na web algo que ajude a explicar a linha, em
lugares ainda não visitados. Três achados: (1) **Baker & Banaji (2026,
arXiv:2602.05593)** — medidas Rajchman sem taxa uniforme de decaimento
de Fourier são fenômeno genérico na literatura, não patologia; reforça
a Proposição C de H-127 (adicionado como addendum). (2) **Chang (2026,
arXiv:2603.25753)** — redução puramente combinatória (sem Fourier) da
Collatz a um balanço de resíduos mod 32 numa subsequência esparsa:
sétima articulação independente do mesmo ingrediente faltante. (3)
Siegel (série "Non-Archimedean Spectral Theory", 2020-2023) — programa
relacionado mas sem sobreposição direta, só preprints. Nota de cautela
registrada (não investigada): cluster de alegações de prova completa
via "Fresh 3-Bit Constraint" (ccchallenge.org) — mesmo padrão já
refutado várias vezes nesta linha, fora de escopo agora (cabe no paper
cumulativo de críticas, só quando pedido). Ver **H-128** para a análise
completa. Não muda o próximo passo: nenhuma investigação nova aberta,
seguir para escrever o paper.

## ✅ Os dois lemas pendentes foram executados (H-126, H-127) — nenhum ficou como esperado, mas ambos deram resultado citável

Os dois "próximos passos" declarados em H-115 foram concluídos
(2026-07-17), com consulta ao Fable e checagem cruzada (advisor +
verificação direta contra o PDF de Tao 2022 + experimento
computacional decisivo). Nenhum dos dois virou o "lema positivo
fácil" que se esperava — ambos colapsaram, por vias independentes, no
MESMO ingrediente que já faltava no regime 3:

1. **Lema do regime 2 → H-126**: REFUTADO como esboçado (o orçamento
   D^{-A} contradiz a identidade exata eq. 1.23 de Tao — conferida
   verbatim no PDF). O que sobrevive: um teorema de estrutura exato e
   positivo (Prop. 2 — a correlação grosseira de agregados irmãos NÃO
   desaparece, é fórmula fechada independente de profundidade) mais um
   lema condicional cuja hipótese (medida de Syracuse em L²(Z_3)) foi
   **refutada computacionalmente** em E-100: K_ℓ diverge linearmente
   até ℓ=17 (incrementos → 0,47, sem saturação).
2. **Lema de redução Z-number → H-127**: vira uma dicotomia condicional
   (Lema B), não uma equivalência limpa — e inclui um resultado
   negativo próprio (Proposição C): identidade exata de Jensen mostra
   que o orçamento de Fourier anelado tem folga de fator 1,88 contra o
   necessário no regime da WCC (confirmado por Monte Carlo em E-101).
   O ramo espectralmente difuso, inacessível à técnica, "é exatamente
   o núcleo de β=1".

**Isto é bom para o paper, não ruim**: em vez de dois lemas soltos,
temos cinco/seis articulações independentes convergindo no mesmo
ingrediente faltante (endogenia H-110, WCC H-112/H-114, β=1 H-124,
condição L² H-126, dicotomia espectral H-127) — evidência estrutural
de que o ingrediente é real, não artefato de uma abordagem. Ver H-115
seção "Execução dos dois próximos passos" para o resumo, H-126/H-127
para os teoremas completos.

## 🔜 PRÓXIMO PASSO: escrever o paper — não há mais lema pendente

Nenhuma investigação nova está aberta. Escopo do paper: H-109 a H-127
(a linha G(v)/qx+1/endogenia — as refutações de alegações de prova
falsas ficam para o "paper cumulativo de críticas" separado,
BACKLOG.md item 8, só quando pedido explicitamente). Zeladoria
pendente antes de citar: conferir os números de equação do Wirsching
(2003) contra a versão final da DCDS (o PDF em mãos é "preliminary
version"); conferir as referências externas citadas só de memória
pelo Fable em H-127 (Halász 1977, Tao-Vu 2009, Nguyen-Vu 2011, Mahler
1968, Flatto-Lagarias-Pollington 1995, Erdős 1979, Lagarias 2009) se
forem usadas no texto final.

## ⭐⭐ Terceira perna de triangulação: Wirsching (2003) e a função de Fabius base-3 (H-125)

Segunda rodada da busca literária (pedido explícito: "achar coisas que
ajudem a ter algo digno de citações") encontrou e baixou (com permissão
explícita do diretor científico) Wirsching (2003), "On positive
predecessor density in 3n+1 dynamics" (DCDS 9(3), 771-787, item 132 do
INDEX) — uma rota DIFERENTE e mais refinada que a WCC do livro de 1998,
para o mesmo objetivo.

**Achado central**: a densidade invariante φ do paper (ponto fixo do
operador de médias W₃) é a marginal ARQUIMEDIANA complementar da mesma
contagem combinatória cuja marginal 3-ádica é nossa medida de
Syracuse. φ acaba sendo identificada (pelo Fable) como o análogo
BASE-3 da função de Fabius (família das "atomic functions" de
Rvachev) — conecta nosso trabalho a uma literatura analítica madura
(Berg, Krüppel, Rvachev) raramente citada pela comunidade Collatz.

A cadeia de 3 conjecturas do paper vive na MESMA janela crítica (regime
CLT k≈ℓ) que β=1 de Tao (H-124) e o regime 3 de H-115 — terceira
roupagem independente da mesma barreira (equação funcional real, em
vez de contagem inteira ou caracteres de Fourier). Não é atalho, é
triangulação.

**Experimento EXECUTADO (E-099) até ℓ=500 com erro certificado**:
Conjectura 3 SUPORTADA numericamente. Razão decisiva L_ℓ → 2/3 com
déficit (0,580±0,001)/ℓ — coeficiente reproduzido pela própria φ₀ de
Berg-Krüppel (check de consistência subleading, não só o limite).
ln(φ/φ₀) crescente/côncavo/uniforme em u∈[−2,2], consistente com
limite finito: c ≈ 0,54, intervalo honesto 0,53–0,55 (incerteza
dominada pela forma da cauda: C/√ℓ é a melhor forma, C/ln²ℓ
degenerada nesta faixa; escada ℓ∈{1000,2000} discriminaria). Sem
modulação log-periódica. Ressalva mantida: isso testa só a ponta mais
concreta da cadeia; Conjecturas 1–2 seguem abertas.

Ver **H-125** para a documentação completa.

## ⭐⭐ Busca literária dirigida encontra triangulação máxima: β=1 de Tao (2020) = mesmo objeto da WCC de Wirsching (H-124)

Pedido explícito do diretor científico: buscar literatura que pudesse
melhorar o material da linha G(v)/qx+1/endogenia para uma publicação
de respeito. 5 achados avaliados com o Fable (WebSearch/WebFetch):

1. Tao (2011, blog): técnica Littlewood-Offord+Riesz+Bohr sets,
   condicional à conjectura fraca de Collatz — sem ferramenta nova
   (o próprio post reconhece que Baker já dá bound incondicional mais
   forte), mas dá um lema de redução condicional honesto.
2. Varjú-Yu (2022): decaimento de Fourier de medidas autosimilares —
   nossa medida satisfaz nominalmente a condição, mas o teto é
   polilog (insuficiente) e colapsa no problema aberto (3/2)^n mod 1
   (Mahler, já conectado a Collatz por Lagarias).
3. Badea-Grivaux (2023): irrelevante como obstáculo (resultado sobre
   medidas genéricas de Baire, nossa medida é estruturada).
4. **Tao (2020, blog) — o achado mais importante**: conjectura β=1
   (medida de Syracuse quase-uniforme até a escala mais fina) é,
   verificado estruturalmente, o MESMO objeto algébrico da Weak
   Covering Conjecture de Wirsching (H-112/H-114), um degrau mais
   fraca. Consequência direta: o excesso e(ℓ) medido em H-114 é
   literalmente o o(n) do expoente de β=1 — nossos dados (e(ℓ)
   sub-linear) são evidência computacional DIRETA a favor de β=1, não
   só da WCC. E: a rota de Tao mostra que dá para evitar a
   decorrelação bivariada de H-110 substituindo por controle L^∞
   marginal — mas bate na MESMA parede. Três articulações
   quase-equivalentes do mesmo ingrediente faltante (endogenia,
   WCC, β=1), nenhuma provada, é a forma mínima nomeada da barreira,
   aberta há 6 anos, nunca virou paper.
5. Spiegelhofer (2021/2023): mesmo limiar log₄3 (estrutural, não
   coincidência), mas é resultado abaixo-do-limiar (contagem/média),
   não worst-case — fila condicional para um eventual lema de regime 2.

**Não reabre o regime 3 de H-115** (nenhuma ferramenta nova), mas
fortalece o pacote de publicação: H-114 e H-115 reenquadrados com a
triangulação e a forma mínima nomeada (β=1). Ver **H-124** para a
análise completa.

## Fila de 10 papers pendentes (itens 116-125) esgotada — H-116 a H-123

Os 10 papers baixados pelo diretor científico em 2026-07-16 mas nunca
revisados foram lidos e analisados em paralelo (3 agentes). Nenhuma
alegação de prova completa da conjectura clássica sobrevive — o único
candidato próximo (item 123, Barghout, "Probabilistic Proof of
Convergence") foi REFUTADO: mesma falácia recorrente do projeto
(densidade estática de v₂ sobre inteiros pares, corretamente
demonstrada, confundida com estatística de visitas de uma órbita
dinâmica específica — hipótese de mixing nunca provada; exclusão de
ciclos não-triviais admitidamente só probabilística no próprio texto).
Achado extra: o argumento RF do Barghout toca diretamente nossa linha
G(v)/Syracuse (é uma medida de frequência de v₂), e generaliza para
kn+1 — conexão útil de contraste (H-116).

Demais papers, sem erro de prova (a maioria sem nenhum erro
matemático):
- **H-117/H-118**: aplicações (esteganografia, blockchain) — sem
  alegação matemática sobre a conjectura, sem erros.
- **H-119**: Getachew (mesmo autor do H-079, já refutado antes) —
  desta vez SEM prova disfarçada, mas com falhas reais de rigor
  (complexidade O(1) falsa para bignums de 2^100000 bits, curve-fit
  com 2 pontos, novidade superestimada — técnica CTZ padrão).
- **H-120/H-121**: Aliyev, generalização algébrica de ciclos racionais
  (diferente da nossa qx+1) — teorema confirmado por teste de estresse
  independente (200 casos aleatórios, 0 violações); um erro de
  copy-paste sem consequência.
- **H-122**: Ito & Nakano, verificação exaustiva por FPGA (par
  116/120) — engenharia sólida, sem erros.
- **H-123**: Ren et al., verificação de um único número gigante +
  autômato de classes residuais (par 118/122) — computação correta
  mas alegação central mal enquadrada (confunde "checar um número" com
  "verificação exaustiva"); bug de rotulação secundário no apêndice.

Nenhum destes 10 papers tem sobreposição relevante com a linha
G(v)/Syracuse/qx+1/endogenia (H-090 a H-115), exceto o contraste
conceitual do item 123 (densidade estática vs. dinâmica). INDEX.md
atualizado, fila de literatura pendente zerada novamente.

## ⭐⭐ Duas frentes de pesquisa genuína (não mais rodadas de consulta): teste direto da WCC (H-114) e por que a extensão de Tao não cruza a barreira (H-115)

Depois de fechar o pacote de publicação (H-109-H-113) e esgotar 7
rodadas de "importar maquinaria de outra área" (todas refutadas —
Kesten, Furstenberg, Martin, conspiração 2-ádica, Bourgain-Garaev-
Konyagin, Breiman sem independência, Bilu/Chambert-Loir, Bourgain-
Gamburd), o diretor científico pediu duas tentativas sérias e diretas,
não mais rodadas de consulta:

**H-114 — primeiro teste computacional direto (até onde sabemos) da
Weak Covering Conjecture de Wirsching (1998)**: lida a definição exata
do livro (Cap. V), implementado DP de bitset com rotação cíclica,
validado 100% contra tabela de referência independente. Estendido até
ℓ=20 (custo cresceu ~3,3×/passo, ℓ=20 sozinho levou ~27min — extensão
adicional descartada por custo/benefício). Resultado final: j*(ℓ)
existe e é finito em toda a faixa; a leitura intermediária
("desaceleração monotônica até ≈0,77, perto do limiar") era artefato
de um platô isolado em ℓ=16 — os 3 pontos novos (incrementos todos +1,
sem novos platôs) mostram a inclinação local oscilando em 0,74-0,86 em
torno do limiar teórico log₄3≈0,7925, não convergindo de forma limpa.
Leitura qualitativa final (duas estatísticas independentes
concordantes: ΔAIC≈5 e déficit de platôs p≈0,072): **favorece
crescimento lento ilimitado de e(ℓ) sobre estabilização pura** —
compatível com a versão fraca da conjectura (3.9), desfavorece a
versão forte (3.8). Discriminação fina (log ℓ vs. √ℓ vs. linear muito
lento) permanece inacessível nesta faixa — precisaria de ℓ~40, que
exigiria reescrever o algoritmo, não mais Python puro.

**H-115 — por que a extensão bivariada de Tao (2022) não cruza a
barreira**: lida a Seção 7 inteira da prova de Tao (o mecanismo real).
Percepção central (formulada nesta sessão, confirmada e aprofundada
pelo Fable): para um par FIXO de folhas irmãs, a congruência de
existência pina v numa única classe, e as duas folhas viram funções
AFINS da MESMA variável livre — dependência determinística PERFEITA em
qualquer precisão. "Aplicar Tao duas vezes + independência condicional"
não é só circular, é FALSO como enunciado. Existe uma reformulação
correta (segundo momento, soma sobre pares de caminhos, sem
circularidade), mas com alcance limitado: **três regimes de precisão**
— (1) par fixo: sem decaimento possível; (2) ℓ=O(log D): provável com
a maquinaria de Tao quase inalterada, lema real ainda não escrito;
(3) ℓ≍D (onde vive a barreira/WCC): exigiria decaimento de Fourier
exponencial uniforme, equivalente a um problema aberto reconhecido da
área (rigidez efetiva ×2×3 de Furstenberg / decaimento de Fourier de
medidas auto-similares tipo Breuillard-Varjú — ferramenta que não
existe hoje).

**Recomendação disciplinada resultante**: não perseguir mais o regime 3
por analogia (a resposta já é conhecida); o trabalho empírico (estender
H-114 a ℓ≥18-20) continua valendo; o lema do regime 2 fica como opção
de baixo risco/valor modesto, não perseguida ainda. Pacote final desta
linha: ρ_eff≲0,06 (H-111) + quadro teórico de três regimes (H-115) +
dados diretos sobre a WCC (H-114) — estado da arte defensável sem
resolver um problema aberto reconhecido da área.

## ⭐ Portão estatístico fechado: disputa Kontorovich-Lagarias vs. Volkov resolvida (H-113)

Sexta rodada de consulta externa recomendou consolidar um pacote de
publicação; o Fable identificou que a peça mais citável (resolver
empiricamente a disputa KL-2009-vs-Volkov sobre o expoente de 5x+1,
0,650919 vs 0,678) não estava de fato fechada — a citação anterior em
H-109 ("Hill batendo em 0,650919") não tinha IC e acabou **corrigida
para não-confirmatória** (erro padrão real do estimador ≈0,45; a
concordância de 2 casas era coincidência estatística).

Implementado do zero (código nunca antes persistido no repo, só
descrito em H-109): árvore reversa real de 5x+1 (regra de
admissibilidade derivada pelo Fable — sem condição de paridade, só
integralidade mod 5), com duas autocorreções pelo caminho: (1) bug de
amostragem meu (raízes ultrapassando a janela de medição, corrigido);
(2) o modo de falha previsto pelo Fable ("com n grande o IC bilateral
do estimador enviesado exclui os dois candidatos") realmente aconteceu
e foi resolvido com uma reescrita do DFS (rastreio de path-max, uma
única passada dá todos os buffers) + extrapolação de Richardson
(Aitken Δ²).

**Resultado final**: expoente extrapolado **0,639, IC95%=[0,633,
0,645]** — exclui Volkov (0,678) com folga ampla (~10+ erros-padrão); o
resíduo até Kontorovich-Lagarias (0,650919) tem assinatura de
pré-assintótica de janela fixa (mensurada, não um viés remanescente
não-corrigido). Ver **H-113** e `experiments/E-097-qx1-empirical-gate/`.

Nesta mesma rodada, avaliamos e descartamos uma proposta da IA externa
de atacar a barreira de endogenia via medida de Mahler/equidistribuição
de raízes (Teoremas de Bilu/Chambert-Loir) — o Fable encontrou um
contraexemplo direto e decisivo (P(X)=Xⁿ−1 tem raízes perfeitamente
equidistribuídas mas P(2) mod 3^ℓ fica preso numa órbita minúscula:
equidistribuição de raízes NÃO implica cobertura de resíduos, como
princípio geral). A IA externa concordou integralmente e endossou o
fechamento da linha exploratória — próximo passo é consolidar o pacote
de publicação (H-109, H-110, H-111, H-112, H-113).

## ⭐ Checagem de novidade concluída: recalibração honesta de H-109/H-110 (H-112)

O diretor científico baixou os 5 papers/livro pendentes desde H-109
(itens 127-131 do INDEX.md). Análise via 3 forks em paralelo revelou
dois achados importantes de prior art:

1. **α₂=0,650919 (q=5) NÃO é novo** — Kontorovich-Lagarias (2009) já
   tinham essa quantidade exata (η5,BP, Teorema 8.10, via grandes
   desvios), 15+ anos antes. A nota não resolvida "≈0,68" está
   identificada: é η*5,BP≈0,678, previsão de um modelo estocástico
   CONCORRENTE (Volkov), citada pelos próprios Kontorovich-Lagarias como
   disputa em aberto desde 2009 — nossos dados empíricos (enumeração
   real + Hill estimator batendo em 0,650919) são evidência nova a favor
   da predição deles.
2. **A virada estrutural qualitativa em q≥5 também NÃO é nova** —
   Wirsching (1998, Cap. III) já previu isso heuristicamente
   ("presumably", nunca provado), mesmo limiar exato. Confirmada
   independentemente por Gonçalves-Greenfeld-Madrid (2022, Teorema 1.3,
   prova forward rigorosa que exclui q≥5 para p=2).
3. **A barreira de endogenia (H-110) tem precedente direto**: Wirsching
   (1998, Cap. V) prova densidade positiva condicionalmente a uma "Weak
   Covering Conjecture" estruturalmente idêntica ao nosso "ingrediente
   que falta" — ainda em aberto no livro, sem evidência de resolução
   desde então. Pode ser o mesmo problema em aberto há ~30 anos.

**O que sobrevive como contribuição real**: a forma fechada exata
ρ(M_q(α))=q^(α−1)/(2^α−1) válida para q arbitrário (ninguém unificou
isso numa fórmula de família antes), a confirmação quantitativa+empírica
rigorosa, e a calibração ρ_eff≲0,06 de H-111 (sem precedente
identificado). Ver **H-112** para a análise completa, e H-109/H-110
atualizados com as respectivas notas de recalibração.

## ⭐ Experimento de controle de 3 braços concluído: ρ_eff≲0,06, nenhum acoplamento positivo detectado (H-111)

Implementado e rodado o experimento de controle desenhado pelo Fable
(braço 1 sintético i.i.d., braço 2 sintético com acoplamento de
conteúdo ρ ajustável, braço 3 árvore aritmética real remedida no mesmo
mult=2000) para calibrar quantitativamente a barreira de endogenia de
H-110. Percurso completo com dois desvios interessantes:

1. **Autocorreção do Fable durante o checklist**: a criticidade medida
   (E[G|tipo]) não batia com a previsão original dele (1,00/2,00) —
   ficava ~2,6× mais alta, consistentemente. Diagnóstico: erro na
   *derivação teórica* dele (omitiu um fator do teorema de renovação de
   Markov), não bug de implementação — confirmado por um oráculo de
   programação dinâmica exata que ele mesmo escreveu, batendo com os
   dados dentro do erro amostral.
2. **Braço 1 vs. braço 3**: variâncias residuais quase idênticas em
   toda a grade m=8-29 — nenhum sinal de acoplamento positivo entre
   subárvores irmãs da árvore real.
3. **Rodada de forma do braço 2** confirmou o mecanismo funciona (var
   cresce com ρ), mas descobriu contaminação por saturação em ρ
   alto+m profundo (até 91% dos pares) — perseguir essa região seria
   inviável (mult da ordem de milhões) e desnecessário.
4. **Slope final + bootstrap de excesso** (n=4000, ρ pequeno, m=11-20):
   excesso (real−sintético) converge monotonicamente a zero com a
   profundidade — assinatura de descasamento residual do null (mais
   persistente em profundidade do que o Fable havia estimado), não
   sinal aritmético real, e por ter sinal oposto ao acoplamento
   procurado, só reforça a conclusão.

**Resultado final**: nenhum acoplamento aritmético positivo detectado;
cota **ρ_eff≲0,06 (IC95%, em m=20)** — o acoplamento aritmético efetivo
entre folhas da árvore reversa real é, no máximo, ~6% do acoplamento
máximo simulável. Converte a barreira teórica de H-110 (existência do
gap) numa medida empírica quantitativa do seu tamanho. Ver **H-111**
para a documentação completa, incluindo os dois desvios/autocorreções.

## Quinta rodada de consulta externa avaliada: uma direção viva, um experimento a rodar (H-111)

Pedimos à IA externa caminhos reais para atacar a decorrelação entre
folhas identificada em H-110. Resposta mais tecnicamente densa que as
anteriores — quatro alegações, avaliadas pelo Fable com o mesmo
ceticismo das rodadas passadas (esta já é a quarta correção
substantiva a essa IA nesta linha):

1. **Baker/fase arquimediana**: meio-certo — núcleo real, mas o
   teorema certo para taxa polinomial é Rhin (1987, mesma cota da
   literatura de exclusão de m-ciclos, H-057), não Baker genérico; e
   ataca a metade do problema que já estava resolvida (Choquet-Deny em
   H-110), não o gargalo.
2. **Somas exponenciais cruzadas** (decorrelação 3-ádica entre
   folhas): **a melhor sugestão desta IA em toda a linha** — extensão
   bivariada correta e verificável da Proposição 1.17 de Tao (2022).
   Citação Bourgain-Garaev-Konyagin errada de regime, mas a redução em
   si tem superfície de ataque real. Próxima ação barata: checar na
   demonstração de Tao (PDF já arquivado, item H-076) se o decaimento
   de Fourier é uniforme no resíduo inicial.
3. **Lema de Breiman** (blindagem do expoente α*=2 contra a crise de
   endogenia): conclusão correta, justificativa errada (Breiman exige
   independência que não temos) — a blindagem real vem de sanduíche +
   equação de pressão. Caveat que a IA omitiu: só o expoente é
   blindado, a CONSTANTE de cauda não.
4. **Experimento de "falsificação de controle"**: núcleo bom, as duas
   implementações propostas quebram em direções opostas (acoplar
   valuações entre irmãos → nenhum piso aparece; acoplar tempos de
   parada entre gerações → o próprio α se move). Desenho corrigido de
   3 braços (controle i.i.d. + controle com conteúdo de subárvores
   acoplado por ρ ajustável + árvore aritmética real) daria uma curva
   de calibração piso(ρ), convertendo as cotas de H-101/H-107 sobre σ_Y
   numa medida quantitativa interpretável — barato, vale rodar.

Ver **H-111** para os detalhes completos de cada item.

## ⭐⭐ A peça teórica mais importante desta linha: barreira de endogenia (H-110)

Quarta rodada de consulta à IA externa: perguntamos se a linha G(v)/μ
estava madura para uma nota técnica. Veredito dela: sim, parar de
explorar e fechar a questão da existência do limite com uma "barreira
teórica" honesta em vez de deixá-la vaga — sugeriu um mecanismo
específico ("conspiração 2-ádica"). Pedido ao Fable para avaliar com
ceticismo (ele já tinha corrigido essa IA duas vezes antes). Resultado:

1. **Existe um modelo "toy" real** (não espantalho) onde a recursão de
   pressão da árvore (mesma equação exata de H-109) tem "liberdade de
   gauge" — por ser linear, qualquer G(v)=W(v)·Y(y) com Y invariante
   ao longo da árvore é OUTRA solução exata da mesma recursão, com a
   MESMA pressão, MESMA cauda α=2, MESMO slope contra μ — mas com
   variância residual que NUNCA colapsa a zero. Nenhuma estatística
   que medimos nesta linha inteira distingue as duas soluções. Nome
   técnico: "endogenia" (Aldous–Bandyopadhyay 2005) — literatura
   estabelecida, não invenção do Fable.
2. **Mas o mecanismo específico proposto pela IA ("conspiração
   2-ádica") está refutado** por um lema de duas linhas: w_a mod 2^a é
   uma CONSTANTE UNIVERSAL, independente de v (3·w_a≡−1 mod 2^a) — a
   árvore reversa destrói toda informação 2-ádica sobre a raiz a cada
   geração. **Verificado numericamente nesta sessão** (a=1 a 10,
   500+ v's cada, bate exatamente). Terceira correção do Fable à mesma
   IA externa (depois de "Kesten local" e "Furstenberg/Martin").
3. **A barreira real está em outro lugar**: recursão sozinha não força
   colapso; recursão+independência-entre-subárvores força (via
   classificação padrão de smoothing transforms + Choquet–Deny) — mas
   essa independência é uma afirmação ARITMÉTICA não provada sobre os
   inteiros reais (os "dígitos 3-ádicos frescos das folhas" se
   comportarem como independentes entre subárvores), não uma
   propriedade automática do modelo. Formulação honesta registrada em
   H-110 para uso em qualquer texto futuro.
4. Reabilitação parcial: a sugestão anterior de Fronteira de Martin
   (H-109, descartada como "empréstimo de prestígio") tinha um núcleo
   real (o espaço de gauge É a fronteira de Poisson relativa ao fator
   3-ádico) — diferente de Kesten/Furstenberg, que não tinham núcleo
   salvável.

Ver **H-110** para a documentação completa (o toy, o lema, a
formulação da barreira, e o que pode/não pode ser afirmado com rigor
de nota técnica).

## Achado mais forte da linha G(v)/Syracuse: generalização qx+1 (H-109)

Terceira rodada de consulta à IA externa (após H-099-H-107 abaixo)
levou ao resultado mais forte desta linha inteira. Pedida uma
generalização do expoente universal α*=2 (H-104) para mapas qx+1, o
Fable derivou que a equação de pressão espectral tem **forma fechada
exata**: ρ(M_q(α))=q^(α−1)/(2^α−1) — não apenas numericamente estável
como parecia em H-104, mas uma identidade algébrica. A equação
q^(α−1)=2^α−1 tem raiz trivial α=1 sempre, e uma segunda raiz que é
**2 exatamente para q=3** (nosso α*=2), mas cai **abaixo de 1 para
q≥5** — uma virada estrutural completa (densidade positiva vs. zero,
confirmada por drift log q − 2log2 mudando de sinal). Verificado
independentemente nesta sessão (bisseção: α₂=0,650919 para q=5,
0,373501 para q=7, 0,258108 para q=9) e confirmado empiricamente pelo
Fable em árvores reais de 5x+1/7x+1 (slopes de contagem e Hill sobre a
cauda do "martingale" batendo com a previsão). Nova previsão
falisificável para o teste EVT (H-108): ξ=α₁/α₂, dá 0,5 para q=3
(consistente com H-108: 0,4836/0,5575) e 0,651 para q=5 (não testado
ainda). **H-109** documenta tudo, com ressalva de calibração: uma
busca rápida achou território relacionado na literatura (Wirsching,
Kontorovich-Lagarias, uma "dimensão de Hausdorff≈0,68" para q=5 em
outro trabalho, próxima mas não idêntica ao nosso 0,651) — checagem de
novidade rigorosa ainda pendente antes de qualquer alegação de
publicação. As outras 3 sugestões da mesma rodada (Fronteira de
Martin, Tauberiano, Furstenberg ×2×3) foram descartadas como direções
de pesquisa pelo Fable — a de Furstenberg em particular era empréstimo
de prestígio sem conexão rigorosa real, confirmando ceticismo prévio.
Também: **H-108** confirmou α=2 por Teoria de Valores Extremos (máximo
de blocos, imune ao problema de variância na fronteira de divergência)
— terceira via independente de confirmação (teoria + Hill + EVT).

## Consultas a IA externa sobre G(v) vs. medida de Syracuse (H-099 a H-107) — concluído

O diretor científico consultou uma IA externa duas vezes (prompts de
contexto completo, arquivos em scratchpad) sobre a linha G(v)/μ de
Tao. **Rodada 1** (5 abordagens): #1 Jensen → **H-099** (identidade
algébrica exata confirmada; revela gap variando ~46× entre classes
finas). #3 interferência 2-ádica e #5 termo 1/v → **H-102** (ambas
descartadas, sem sinal, como previsto). #2 espectro do operador de
transferência (reformulado como variância estratificada) → **H-103**
(heterogeneidade de taxa só modesta em mod 9, ~1,8×, bem menor que os
46× — sugere que a heterogeneidade real está em escalas mais finas).
#4 (topologia local) foi superada pelo teste de pares casados abaixo.

**Teste decisivo paralelo** (proposto pelo Fable, não uma das 5): pares
casados (v1,v2=v1+t·3^m) compartilhando dígitos 3-ádicos até
profundidade m, sem precisar computar μ → **H-100/H-101**, alcançou
m=29 (muito além do M=18 anterior). Resíduo continua caindo até m=29
sem platô confirmado — inclui autocorreção registrada (um "platô"
aparente com 500 pares se desfez ao aumentar para ~2300 pares/ponto).

**Rodada 2** (5 abordagens novas, pedidas com os resultados da rodada
1): a IA sugeriu "expoente de Kesten local por classe" para explicar o
gap de 46×. O Fable **refutou essa formulação** (teoria errada para
pesos determinísticos por prefixo) e calculou uma previsão exata
própria: expoente de cauda **universal α*=2** (raiz de uma equação
espectral, estável em 4 níveis de refinamento) — confirmado
empiricamente via estimador de Hill (**H-104**: ~1,97 no topo da
cauda global; 1,74-2,17 por classe, sem variar como a IA previa). A
quantidade local correta do Fable (razão de participação PR(r) da
árvore-prefixo) **explica ~34% da variância do gap de Jensen**
(**H-105**, correlação -0,58) — e um bootstrap de verificação (alerta
do próprio Fable sobre ruído de cauda pesada) mostrou que a
heterogeneidade é majoritariamente sinal real (razão sinal/ruído ~2,0)
e que a correlação **fortalece para -0,74** ao filtrar classes ruidosas
(**H-106**) — confirma PR(r) como preditor mecanístico genuíno.

A última ponta pendente (Ideia B da rodada 2 — espectro via DFT/
"Chrestenson", reformulada pelo Fable como ANOVA aninhada com correção
de viés de Bessel) foi implementada e fechada em **H-107**: 2 blocos
densos de 3¹¹ pontos consecutivos (magnitudes de v 5× diferentes)
concordam com diferença <1% em toda a faixa t=1-7, e são consistentes
com a curva de H-101 na profundidade comparável — validação cruzada
forte entre dois métodos independentes (enumeração exaustiva vs.
amostragem de pares).

**Estado final desta linha (encerrada, todas as pontas fechadas)**:
existência do limite de escala G tem evidência forte (agora reforçada
por 3 métodos independentes); exatidão total (resíduo→0) não fechada
formalmente, mas toda a evidência disponível (pares até m=29 + ANOVA
em blocos densos) pende para "converge", não "platô real"; a
heterogeneidade de forma da distribuição condicional (gap de Jensen)
tem explicação mecanicista sólida via cauda universal α=2 (H-104) +
razão de participação da árvore-prefixo (H-105/H-106, correlação
reforçada a -0,74 após controle de ruído).

## Coleção de papers (nova, 2026-07-14)

`literature/papers/INDEX.md` — 100 resultados do Google Scholar
(busca "Collatz", ordenado por data), 15 PDFs baixados, tabela com
flags Lido/Corrigido/Implementado para o diretor científico preencher
manualmente conforme formos processando um por um. **Não iniciar a
leitura/incorporação sem pedido explícito** — ver nota no
`BACKLOG.md` item 0.

**Item 001 processado (H-039)**: paper de Ruiz Castillo ("Geometría
Residual..."), lido inteiramente via navegador (39 páginas) e depois
re-confirmado/refinado contra o PDF completo (baixado pelo diretor
científico em 2026-07-15, arquivado em
`literature/papers/001_Geometria-Residual-Ruiz-Castillo.pdf`). Matemática
de base correta (formalismo termodinâmico clássico, Ruelle/Ellis,
aplicado honestamente ao observável de dissipação 2-ádica), mas com
problemas reais: mesmo fato trivial ("convexa ⟹ f''≥0") repetido pelo
menos 5x como resultado nomeado independente, mais 10 quadros coloridos
redesenhando repetidamente a mesma cadeia conceitual; a identidade
central (`g_RC=σ²_RC`) é corretamente rotulada "Conjetura" já na sua
primeira introdução (não só na conclusão, correção feita após leitura
direta) — mas os quadros ilustrativos ao redor dela usam tom mais
assertivo que o aparato formal, uma inconsistência retórica menor; zero
conteúdo numérico (as duas figuras são explicitamente "conceptual");
100% autocitação nas 13 referências (zero literatura de Collatz ou de
formalismo termodinâmico clássico). Fizemos o cálculo explícito que o
paper nunca faz (P_RC(t), g_RC(t), K_RC(t) em forma fechada para o
modelo i.i.d. padrão, verificado contra E[a]=2/Var[a]=2 já
estabelecidos) — achado limpo: singularidade real em t=log(2). Nenhuma
hipótese nova sobre a conjectura em si emergiu — ver H-039 para
avaliação honesta completa.

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

**Fila de 17 papers pendentes totalmente esgotada (2026-07-15)** —
todos os itens `BAIXADO` do INDEX.md agora têm Lido/Corrigido/
Implementado preenchidos (confirmado por grep, zero linhas
remanescentes). Além dos 10 já descritos abaixo (itens 101-110), os 7
restantes (itens 022-037, baixados numa sessão anterior):
**H-081 (item 022, Spencer 2025) — ALEGAÇÃO DE PROVA REFUTADA**: mesmo
furo que H-079, por caminho diferente ("classe residual ocupada" ⇏
"inteiro específico atingido", confirmado com contraexemplo em n=27);
itens 023 (Iglesias, divulgação sobre Busy Beaver) e 024 (Charrat,
filosofia especulativa) marcados como lidos sem conteúdo técnico
verificável sobre Collatz (Collatz citado só tangencialmente); **H-082
(item 025, Kayadibi 2026)** — correto, honesto, não alega prova; **H-083
(item 030, Wang 2026, INTEGERS)** — exclusão Diofantina de m-ciclos
(m≤95), correto nas identidades verificáveis, mesmo território de
H-057; **H-084 (item 035, Ruiz Castillo)** — oitavo paper da mesma
série já sintetizada, mesmo padrão (deuda residual revestida agora com
dinâmica simbólica/teoria ergódica); **H-085 (item 037, Spencer 2026) —
veredito diferenciado**: mesmo autor do item 022, suspeita inicial de
mesmo furo **não confirmada** pela investigação — a árvore real
(estrutura diferente, grau infinito) mostrou cobertura completa em
todas as escalas testadas, mas uma lacuna de rigor real foi identificada
na demonstração (Teorema 14.1→14.2, passagem classe→elemento não
justificada) sem contraexemplo computacional encontrado — caso
documentado de autocorreção de uma suspeita baseada em precedente de
autor, não confirmada cegamente.

**10 papers novos arquivados via EBSCO/ScienceDirect (2026-07-15,
`literature/papers/INDEX.md` itens 101-110)** — busca do diretor
científico fora do Scholar original, trouxe referências importantes que
o projeto já citava sem ter o PDF: **Tao (2022)**, "Almost all orbits of
the Collatz map attain almost bounded values" (o resultado mais forte já
estabelecido, H-076); **Barina (2021)**, verificação até 10^20 (H-075).
Todos os 10 itens revisados no mesmo dia (H-071 a H-079 + H-070 já
existente): Andrei & Masalagiu 1998 (H-071, correto, um erro real
contido no Teorema 3.2 parte 2); De Mol 2008 sobre tag systems (H-072,
sem erros, não é sobre a conjectura em si); Sayama 2011 visão de "vida
artificial" (H-073, correto); Ballesteros 2018 sobre criptografia
(H-074, correto); Barina 2020/21 (H-075, sem erros); Tao 2022 (H-076,
sem erros — verificação de exemplos, não "caça a erros"); Clay 2023
(H-077, correto); Wei Ren 2025 (H-078, correto mas condicional, honesto
sobre não fechar a conjectura); e **Getachew 2025 (H-079) — ALEGAÇÃO DE
PROVA REFUTADA**: constrói a mesma árvore reversa de H-018, mas o furo
lógico é que a relação "pai" definida é idêntica ao mapa de Collatz
direto, então "terminação finita do caminho de volta" é logicamente
equivalente à própria conjectura, não uma consequência de
"acíclico+pai único" como a prova alega — petição de princípio
disfarçada por linguagem de teoria dos grafos. Mais 4 falsos-positivos
identificados e descartados (coincidência de sobrenome com outros
conceitos matemáticos do mesmo Lothar Collatz, ou de coautoria).

**H-013/H-018: gargalo de memória quebrado e a oscilação da razão
totalmente explicada (2026-07-15)**. O BFS original de E-018 guardava
todo nó visitado em memória (O(nós), não O(profundidade)) — daí o OOM em
33-61GB registrado antes. Prova de que isso é desnecessário: Collatz é
uma função, então na árvore reversa cada nó tem no máximo um pai; para
raízes J_t com t≥4 a busca nunca reentra no ciclo trivial {1,2,4}, logo
nenhum nó é redescoberto. Reescrito como DFS com pilha explícita
(`experiments/E-018-reverse-tree-branching/experiment_dfs.py`): t=10 com
n_max=1e13 (266M nós) agora usa 9,8MB de RAM. Validado em 3 frentes antes
de confiar em qualquer resultado novo (bate com o BFS antigo nó a nó;
bate com o forward-scan exato de H-013; razão estável a <0.1% variando o
multiplicador de busca e o n_max) — um teste sugerido pelo advisor que
valeu a pena: a primeira leitura (6 pontos) sugeria falsamente um padrão
mod9, que 3 pontos seguintes derrubaram. Com o gargalo resolvido, medi 9
pares (t=4 a 29): a razão entre classes adjacentes **não converge a um
limite único** — oscila por ~2 ordens de magnitude (0.046 a 5.97), sem
padrão periódico simples.

Avancei no "por quê" com dois teoremas provados sobre a estrutura dos
galhos: (1) um nó ímpar w tem subárvore trivial (contribui exatamente 1
nó ímpar para sempre) sse w≡0 mod3 (generaliza H-005 a qualquer nó, não
só à família J_t); (2) os galhos sucessivos de primeiro nível têm
resíduo mod3 exatamente periódico com período 3 (ord₉(4)=3) — 1 em cada
3 é estéril, em posição fixa determinada por t mod9. Isso explica por
que a soma exata D(J_t)=ΣD(w_i) converge rápido na prática (2-3 termos
capturam >97%) e por que medir só o primeiro termo engana.

Por fim, pedido explícito para gerar (via agente rodando Opus) uma lista
de ângulos novos e testar o melhor: uma primeira tentativa teve um erro
metodológico real (pego pelo advisor: comparava decaimento
dentro-de-uma-raiz com a razão entre-duas-raízes que queríamos, com
parâmetro livre e n=9 cujo erro padrão era grande demais para a
coincidência encontrada significar algo). Corrigido: como J_{t+1}=4·J_t+1
exatamente, o teste certo é medir D(4m+1)/D(m) para m ímpar aleatório —
mesmo objeto das 9 razões medidas, sem parâmetro livre. Resultado
(n=500): média geométrica (0.542) e desvio-padrão (0.758 dex) batem com
os 9 valores reais (0.432 e 0.715±0.179 dex) dentro do erro esperado.
**A oscilação de ~2 ordens de magnitude não é especial à família J_t —
é o ruído típico de qualquer processo de ramificação 3-ádico deste
tipo.** Não fecha H-024 (sem fórmula fechada), mas dissolve a pergunta
do "por quê" em vez de deixá-la aberta — o melhor desfecho possível dado
a obstrução já conhecida. Ver `hypotheses/H-018-reverse-tree-branching.md`
e `experiments/E-018-reverse-tree-branching/README.md`.

**Síntese da cadeia H-024→H-091 concluída (2026-07-16)**
(`density-3adic-obstruction-synthesis.md`, raiz do projeto): consolida
a jornada completa desde a obstrução original de densidade 3-ádica
(H-024) até a proporcionalidade quase exata com a medida de Syracuse de
Tao (H-090/H-091), passando pela crítica do Fable que separou magnitude
de resíduo (H-086), continuidade 3-ádica confirmada (H-087), uma
suspeita testada e descartada em H-018 (H-088) e uma correção real e
documentada em H-026 (H-089, revertida). Ver também
`literature/00-index.md` item 8.

**H-091 (mesmo dia, aprofundamento pedido explicitamente)**: as 3
perguntas em aberto de H-090 foram respondidas a fundo. A correlação
G(v)~μ_m não convergia a 1 — na verdade degradava com m (0,998→0,973
até m=12). Descartadas 2 hipóteses (ruído amostral, deslocamento de
janela) e uma terceira testada e refutada por mim mesmo (quebra da
i.i.d. das valuações 2-ádicas sob resíduo fino — autocorrelação medida
diretamente, ficou achatada em ~0 sempre). Escalado ao Fable com a
derivação teórica própria da ponte forward↔reverso: ele confirmou a
ponte (identidade combinatória exata, não heurística) e apontou a causa
real da degradação — `measure_G` usava headroom fixo (`n_max=v·20`),
insuficiente para resolver resíduos finos, com previsão quantitativa de
onde o pico deveria se deslocar (m≈7 com headroom 200, m≈11-12 com
2000). **Previsão confirmada**: com headroom corrigido, a correlação
sobe monotonicamente até m=14 e o expoente ajustado fica perto de 1,00.

**Segunda rodada no mesmo dia (pedido explícito de testar a fundo)**:
uma análise de poder estatístico do Fable mostrou que "converge a
~1,00 exato" era otimista — os dados certificam só b=1,000±0,012 (IC
95%). Dois testes por v individual (evitando defeito de pareamento de
um stress test anterior) deram o resultado mais forte da linha: G(v)
individual **converge claramente** conforme o headroom cresce
(dispersão de Δ(v) cai geometricamente, ~2,5×/década de headroom) —
evidência direta a favor da existência do limite de escala. Mas o
resíduo, embora caia com mais resolução (M até 14), não zera —
exatidão total não certificada, e depende de afirmações de densidade
no grafo de Collatz estritamente mais fortes que densidade positiva
simples (esclarecido pelo Fable), todas em aberto. Ver `hypotheses/H-091-*.md` (Parte 2).

**Noventa e cinco hipóteses testadas (H-001 a H-095), 2026-07-16**: o
diretor científico baixou manualmente 4 dos 10 itens "sem PDF livre"
pendentes (071, 087, 092, 093), reduzindo a fila a 6 (050, 072, 086,
094, 098). **H-092**: item 071 (Koyuncu et al., "Parity-Based Level-Set
Approach", Mathematics/MDPI, peer-reviewed) — sem erros, fórmula exata
do Lemma 1 verificada contra trajetórias reais (incl. n=27), Tabela 1
reproduzida quase byte-a-byte. **H-093 (achado importante)**: item 087
(Tynski, "A Common Proof of the Riemann Hypothesis and the Collatz
Conjecture", 99 páginas, academia.edu) — **ALEGAÇÃO DE PROVA REFUTADA**.
Sob um andaime extenso de terminologia não-padrão (álgebra de Clifford,
"Merkaba", "Logos section", "27 formulações equivalentes"), a exclusão
de órbitas divergentes depende inteiramente de um "axioma (W6)" — limite
de Lyapunov determinístico alegado "forçado" mas justificado de forma
circular e só verificado numericamente até n₀≤3×10⁴ (C≤5). Refutado
computacionalmente: o C mínimo necessário já excede 5 pouco além dessa
faixa e chega a 8,34 para recordistas de atraso conhecidos — mesmo
padrão de erro (média confundida com garantia determinística por
trajetória) já visto em H-045/H-065. **H-094**: item 092 (Syzdykov,
"Continued Disproof Sentence") — réplica a uma crítica (H-095) que não
rebate o ponto técnico, reafirma o mesmo erro categorial redefinindo
O(f(n)) como se fosse um escalar. **H-095**: item 093 (Lafontaine &
Cheong, "A Note on a Claimed Disproof") — crítica curta e correta:
O(f(n))≤n é malformado (classe de funções comparada a escalar), não
apenas incorreto; confirmado pela própria reação defensiva do autor
criticado (H-094).

**Noventa e oito hipóteses testadas (H-001 a H-098), 2026-07-16 —
fila de "sem PDF livre" esgotada**: o diretor científico baixou mais
2 dos 6 itens ainda pendentes (050, 098) e localizou por busca a fonte
primária da disputa 092/093 (item novo, 115). Os 4 restantes (027,
072, 086, 094) não foram encontrados na internet apesar de busca
extensiva — marcados como removidos, não serão mais buscados.
**H-096 (achado importante)**: item 050 (Roif, "On the Convergence of
the Collatz Function", V4) — **ALEGAÇÃO DE PROVA REFUTADA** por erro
elementar: a "Lemma 4.3" do paper afirma que "conjunto de densidade
zero ⟹ conjunto vazio", falso como fato geral (contraexemplo trivial:
quadrados perfeitos, densidade zero mas infinitos) — usada para
"fechar" o conjunto excepcional de Tao (2022) e completar a "prova".
**H-097**: item 098 (del Vado Vírseda, ACM/ITiCSE 2026) — paper de
pedagogia/educação, Collatz só como exemplo didático; a única
afirmação factual (indecidibilidade do Collatz GENERALIZADO,
Conway/Kurtz-Simon 2007) é correta e distinta da conjectura clássica.
**H-098**: item 115 (Syzdykov 2025, "Disproof of Collatz Conjecture by
using O-notation") — a fonte primária nunca antes catalogada da
disputa 092/093; confirma diretamente, na origem, o mesmo erro
categorial já identificado por Lafontaine & Cheong (H-095): usa
O(f(n))≤n tratando uma classe de funções como escalar, e declara
"3^m>2^m−1" uma contradição sem derivar nenhuma.

**Síntese do programa Ruiz Castillo concluída**
(`literature/ruiz-castillo-research-program.md`): consolida as sete
revisões técnicas (H-039, H-050, H-052 a H-056) mais a leitura
contextual do paper de filosofia (item 055). Achado central: cada um
dos sete papers aplica um conceito clássico diferente de teoria
ergódica/mecânica estatística à mesma quantidade (deuda residual
L_k(n) = k·log₂3 − A_k(n)); 5/7 sem nenhum erro, 2 com erros reais mas
contidos e de consistência interna (item 013: enunciado contradiz sua
própria demonstração; item 026: conjectura da Seção 7 contradiz
proposição já provada na Seção 3). O paper de filosofia (item 055,
citação conferida verbatim contra o PDF) revela a motivação real:
Collatz como "modelo conceptual" para uma tese platonista/realista, não
como alvo a resolver — explica o padrão de honestidade epistêmica
consistente e a repetição de uma vocabulário por vez sem convergência
cumulativa.

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

- `H-129` — originalmente: existe análogo q-ádico do polo −1/3 de
  Seymour para a árvore reversa qx+1? **Essa pergunta literal está
  FECHADA, REFUTADA** (mecanismos categoricamente distintos: perda
  uniforme de 1 dígito vs. blow-up raro localizado de valuação). A
  investigação evoluiu para atacar o "congelamento" quenched-vs-anelado
  da equação de pressão (§3.2 do paper) via otimização ergódica —
  aqui SIM continua aberta. Achados sólidos ao longo da sessão: a
  constante de Bramson B=3/2 aparece exatamente (citável por si só);
  gap espectral do operador de transferência linear provado e
  verificado numericamente (E-105, espectro exato {Λ,0}); hipótese
  log-periódica para o transiente k^-0,222 testada e não suportada
  (E-103 Estágio 2, consistente com derivação teórica de
  não-aritmeticidade); família de escala exata por tipo de resíduo do
  raiz confirmada (E-103 Estágio 4, W_i=2^(−a₀(i)θ)·W* — mas não testa
  κ, cancela algebricamente). O que NÃO se sustentou: a previsão
  numérica a* (erro de processo corrigido antes de reportar); usar a
  família de escala para melhorar o teste de κ (Estágio 5, sem ganho).
  **Atualização (mesma sessão, item 3 executado)**: amostra de 100.000
  raízes (20x, paralelizada) muda o quadro do índice de cauda κ de
  INCONCLUSIVO para FORTEMENTE FAVORÁVEL — GPD com platô de limiar
  limpo pela primeira vez (ξ estável 0,63-0,68 em todos os limiares e
  headrooms), Huisman muito estável cobrindo o previsto, Vuong deixa de
  favorecer lognormal. Duas calibrações (nulo sintético, invariância a
  θ') não revelaram artefato. AINDA NÃO é confirmação/fechamento: Vuong
  ficou "indistinguível" (não "lei de potência vence"), e W provadamente
  ainda não convergiu (mediana cai monotonicamente com headroom). Origem
  numérica de "0,222" segue sem localização (não testada nesta rodada).
  Nada disso integrado ao paper. Ver
  `hypotheses/H-129-q-adic-pole-analog-seymour.md` para o registro
  completo (inclui dois erros de processo autocorrigidos com
  advisor+Fable antes de reportar como confirmados).
- `H-130` (nova, 2026-07-20) — a árvore reversa de qx+1 tem
  esterilidade extra (além de u≡0) quando 2 não é raiz primitiva mod q
  (ex.: q=7, ord₇(2)=3<φ(7)=6) — achado durante a correção da §2 do
  paper (auditoria, 3ª rodada). Conecta à Conjectura da Raiz Primitiva
  de Artin (tabela para q=3..61: mesmo entre q primos, 2 nem sempre é
  primitivo — q=7,17,23,31,41,43,47 são contraexemplos na faixa
  testada; q=31 é o caso extremo, 25/30 dos resíduos estéreis). Não
  afeta o Teorema 3.3 (confirmado). Pergunta aberta: a esterilidade
  extra só reescala W_u, ou introduz estrutura por coset de ⟨2⟩? Só
  exploração numérica preliminar feita, nenhum experimento formal
  ainda. Ver `hypotheses/H-130-esterilidade-extra-2-nao-raiz-primitiva.md`.
- `H-127` — redução condicional da falha da WCC (Wirsching) a
  configurações de Bohr pós-wrap, via Littlewood-Offord/Halász. Status
  do próprio arquivo diz "em revisão". Zeladoria bibliográfica (8 de 9
  referências verificadas contra o texto primário) encerrada em
  2026-07-18. Duas peças distintas, destinos diferentes:
  - **Proposição C** (resultado negativo próprio: a técnica falha por
    um fator exato — déficit 2,2-7× no orçamento de Fourier, identidade
    de Jensen Λ=log γ_c≈0,5834) permanece SÓLIDA — verificação Monte
    Carlo formal já existente desde 2026-07-17 em
    `E-101-jensen-constant-annealed-fourier-budget` (já espelhada em
    `collatz-endogeny`; um E-106 duplicado foi criado por engano em
    2026-07-19 e removido no mesmo dia após auditoria de
    reprodutibilidade).
  - **Lema B** (a redução condicional em si): investigação a fundo da
    Etapa 6 pendente ("upgrade diagonal⟹segmento contínuo",
    2026-07-19) revelou que a Definição 2 usada, como estava escrita,
    é VAZIA (satisfeita por ξ genérico incluindo ξ=1 — verificado,
    `E-107-h127-def2-vacuity-check`), e que a Etapa 6 não fecha por
    nenhuma das duas rotas tentadas (estabilidade em j esbarra numa
    média convexa de Pascal; encadeamento intra-j só dá comprimento
    constante) — mesma parede de constantes da Proposição C, terceira
    aparição. Reclassificada de "lacuna técnica plausível" para
    "problema em aberto explícito". Recomendação para o paper
    atualizada: Lema B não deve ir como estava; ou reformular com a
    Etapa 6 como problema aberto declarado, ou reportar só a Proposição
    C. Nada disso foi integrado ao paper (confirmado — a seção WCC do
    paper é só H-114/H-124, distintas de H-127).
  Convergência com H-110/H-112/H-114/H-124/H-126: todas apontam para o
  mesmo ingrediente faltante, nunca provado. Ver
  `hypotheses/H-127-reducao-z-number-dicotomia-espectral-wcc.md`.

(H-008, citada aqui numa versão anterior deste arquivo como "questão em
aberto", foi na verdade RESOLVIDA POR COMPLETO em 2026-07-13 — ver seção
"Hipóteses confirmadas" abaixo, H-022+H-027. Ver "Próximos passos" para
candidatas não iniciadas.)

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
  (varredura exaustiva). Não é um padrão simples. **Atualização
  2026-07-15**: com o gargalo de memória de E-018 resolvido (BFS→DFS),
  medimos 9 pares (t=4 a 29) — a razão **não converge a um limite único**,
  oscila por ~2 ordens de magnitude (0.046 a 5.97). Fórmula fechada
  continua em aberto. Ver `hypotheses/H-013-last-odd-value-structure.md`,
  `experiments/E-013-last-odd-value-structure/CORRECTION.md` e
  `experiments/E-018-reverse-tree-branching/README.md`.
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
  de árvore finita para t grande. Sem fórmula fechada. **Atualização
  2026-07-15**: o BFS original guardava todo nó visitado (O(nós) memória,
  causa do OOM registrado antes); reescrito como DFS sem esse set — provado
  seguro porque Collatz é função (cada nó tem no máximo um pai) e as
  raízes J_t usadas (t≥4) nunca reentram no ciclo trivial {1,2,4} — memória
  cai para O(profundidade) (9,8MB para 266M nós, vs. OOM em dezenas de GB
  antes). Validado (idêntico ao BFS antigo; bate com forward-scan exato;
  razão estável a <0.1% variando busca e n_max) e usado para medir 5 pares
  novos: a razão entre classes adjacentes **não converge**, oscila por ~2
  ordens de magnitude (0.046 a 5.97) sem padrão periódico simples (uma
  suspeita de padrão mod9 foi levantada e depois derrubada pelos próprios
  dados). Ver `hypotheses/H-018-reverse-tree-branching.md` e
  `experiments/E-018-reverse-tree-branching/README.md`.
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

## H-008 — RESOLVIDA POR COMPLETO (H-022 + H-027)

(Título desta seção corrigido em 2026-07-19 — dizia "RESOLVIDA
PARCIALMENTE", desatualizado desde que a metade par foi fechada em
H-027 no mesmo dia da criação de H-022, 2026-07-13.)

- `H-022` — **prova parcial de H-008** via relação multiplicativa (2 passos
  acelerados, não deslocamento aditivo como H-015/H-016). Provado: todo
  N=18j+13 (metade ímpar de N≡4 mod9) tem M=16j+11<N com
  total_stopping_time(M)=total_stopping_time(N)+5 — exclusão rigorosa,
  verificada sem exceção em 100.000 casos, confirmada não-redundante com
  H-007/H-014 (75% dos casos não eram já cobertos). Ver
  `hypotheses/H-022-mod9-multiplicative-exclusion.md`.
- `H-027` — fecha a metade **par** (N≡4 mod18) como corolário direto de
  H-007: um único passo de halving (N par → N/2) já cai em M≡2 mod3,
  ao qual H-007 se aplica de imediato. Mostra que a condição correta é
  N≡4 mod6 (mais ampla que mod9/18). Verificado sem exceção em 500.000
  casos. Ver `hypotheses/H-027-mod6-corollary-closes-h008-even-half.md`.

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

(nenhuma no momento — H-008, que ficava aqui, foi RESOLVIDA POR COMPLETO
em 2026-07-13 via H-022+H-027; a entrada antiga foi removida em
2026-07-19 por estar desatualizada. Ver "Hipóteses abertas" acima para
H-129/H-127, as investigações genuinamente ativas no momento.)

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

1. **Fórmula fechada para a anomalia de H-013 — status final desta linha
   (2026-07-15)**: o gargalo de memória que limitava a medição numérica
   foi quebrado (BFS→DFS, ver `experiments/E-018-reverse-tree-branching/`),
   permitindo medir 9 pares (t=4 a 29) em vez de só 4. A razão **não
   converge a um limite único** — oscila por ~2 ordens de magnitude
   (0.046 a 5.97), sem padrão periódico simples (mod9 testado e
   descartado duas vezes). Dois teoremas provados sobre a estrutura dos
   galhos (esterilidade generalizada de H-005; periodicidade mod3 com
   período 3, via ord₉(4)=3) explicam por que a soma exata
   D(J_t)=ΣD(w_i) converge rápido na prática. E, testado contra o null
   correto (D(4m+1)/D(m) para m ímpar aleatório, n=500), confirmou-se que
   **a oscilação é ruído genérico de um processo de ramificação 3-ádico
   — não um padrão especial da família J_t** (centro e dispersão da
   distribuição nula batem com as 9 razões medidas dentro do erro
   esperado). Isso **não fecha uma fórmula exata** — H-024 continua
   explicando por que a recursão D(v)=D(2v)+D(ramo) exige precisão
   3-ádica ilimitada, um problema genuinamente difícil — mas dissolve a
   pergunta do "por quê oscila assim" em vez de deixá-la aberta; é o
   melhor desfecho alcançado nesta linha, e não vale mais a pena
   perseguir mais pares/módulos mais finos atrás da mesma coisa. H-037
   mostrou que α de Pratiher (uma vez corrigido o rótulo) é essa MESMA
   quantidade agrupada por t mod3 — dominada por poucos termos pequenos
   (p_2=D(5) sozinho é 93,77%), o que dá uma razão estrutural para mais
   tratabilidade que o D(v) genérico, mas ainda não fechada.
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

1. ~~Tentar resolver a metade par de H-008 com uma ideia nova~~ —
   **obsoleto**: H-008 já foi RESOLVIDA POR COMPLETO em 2026-07-13
   (H-022 metade ímpar + H-027 metade par, ambas provadas e verificadas
   em 500.000+ casos). Este item ficou na lista por engano depois da
   resolução; removido da próxima revisão.
2. Se alguém quiser retomar a fórmula fechada de H-013: a recursão
   D(v)=D(2v)+D(ramo) é exata e correta, e agora (2026-07-15) sabemos por
   que ela não fecha em algo simples — a oscilação da razão é ruído
   genérico de ramificação 3-ádica, confirmado estatisticamente contra o
   null correto (D(4m+1)/D(m)), não um padrão escondido esperando ser
   achado. Perseguir mais pares/módulos mais finos não deve ajudar (já
   tentado e descartado duas vezes). Uma fórmula fechada de verdade
   exigiria uma ideia teórica genuinamente nova (não mais medição) —
   talvez conectada à literatura de branching random walks/smoothing
   transforms (ver as 6 direções propostas por um agente rodando Opus em
   `experiments/E-018-reverse-tree-branching/README.md`, das quais só a
   primeira foi testada).
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
