# CRITIQUE: paper 01 (`main.tex`)

Arquivo único de crítica deste paper (Regra 8/15). A tabela de status
no topo é leitura obrigatória do produtor a cada passada; as seções
datadas abaixo são o histórico completo, só consultadas sob demanda.

Convenção da coluna "Origem": `hoje` = defeito introduzido ou agravado
pela sessão de edição de 2026-08-09/10 (ataque paralelo O1-O8 + divisão
em quatro papers); `prévio` = defeito anterior a essa sessão, que a
checagem final apanhou (Regra 8d: consertar não é obrigação desta
rodada, mas registrar é).

**A partir de C-026 (2026-08-10, loop de convergência)**: as rodadas
seguem um critério de parada explícito pedido pelo diretor científico:
3 rodadas de crítica adversarial CONSECUTIVAS "limpas" (0 crítico, 0
maior, 0 moderado, <3 menor), contexto fresco a cada rodada, sem
crédito parcial. A coluna "Severidade" nessas rodadas usa a escala de 4
níveis (crítico/maior/moderado/menor) definida para esse loop, em vez
da escala alta/média/baixa usada nas rodadas anteriores; o histórico
antigo (C-001 a C-025) permanece como está, sem reclassificação
retroativa.

## Tabela de status

| ID | Rodada | Resumo | Severidade | Origem | Status |
|----|--------|--------|------------|--------|--------|
| C-001 | 2026-08-10 | Abstract diz "We prove" para quatro resultados cujas provas saíram para os companions; os métodos citados não existem mais no corpo | alta | hoje | fixed |
| C-002 | 2026-08-10 | Abstract contradiz o corpo e O8 sobre KL-Volkov (diz que o intervalo não decide; corpo/O8 afirmam separação de dez larguras) e apresenta resultado do paper 04 como próprio | alta | hoje | fixed |
| C-003 | 2026-08-10 | `thm:cascade-factor` rotulado Theorem com etapa provada só empiricamente (ℓ≤8); O2 chama a cota resultante de "unconditional" | alta | hoje | fixed |
| C-004 | 2026-08-10 | O1 e O4 afirmam resultados sem nenhuma âncora no corpo (cancelamento do coeficiente diagonal; espectro primitivo até ℓ=15; ponte O4→O7) | alta | hoje | fixed |
| C-005 | 2026-08-10 | §9.2 condensada não é autocontida: (?1)-(?5) nunca enunciadas e `g_ℓ` nunca definido, logo `thm:wirsching-conj1` é ininterpretável | alta | hoje | fixed |
| C-006 | 2026-08-10 | §3 condensada usa `Z_k(α;·)`, `F_k` (q geral) e "tilted" sem definição; `M_k^{(α)}` definido duas vezes de formas diferentes | média | hoje | fixed |
| C-007 | 2026-08-10 | "the previous unconditional bound 2.306270 recorded above" não está registrada em lugar nenhum do paper; `β_eff` nunca é definido | média | hoje | fixed |
| C-008 | 2026-08-10 | §1.2 (lista de contribuições) desatualizada: itens (i) e (iv) são material dos companions; os dois teoremas novos não aparecem | média | hoje | fixed |
| C-009 | 2026-08-10 | Título anuncia como resultado principal a equação de pressão, agora provada em outro paper | média | hoje | fixed |
| C-010 | 2026-08-10 | §12: "two ... results" seguido de três itens (um deles Empirical Result chamado de "rigorous"); "four vocabularies" seguido de lista com cinco | média | prévio | fixed |
| C-011 | 2026-08-10 | §12 chama `thm:kl` (não calibrado) de "statistically calibrated" e de maior contribuição "of the paper", sendo resultado do companion 04 | média | hoje | fixed |
| C-012 | 2026-08-10 | Data Availability e Apêndice fora de sincronia: omitem os dois teoremas novos, ainda documentam material migrado, e citam repos companheiros sem URL | média | hoje | fixed |
| C-013 | 2026-08-10 | Rótulos O2/O3/O5/O7 usados no corpo (§9-§10) antes de serem definidos (§13), sem label nem ponteiro | média | prévio | fixed |
| C-014 | 2026-08-10 | Frase quebrada e parêntese desbalanceado dentro do enunciado de `thm:propC` | média | prévio | fixed |
| C-015 | 2026-08-10 | "threefold empirical support ... counting-exponent confirmation below" não existe mais abaixo; três listas de "três medições" divergentes entre si; medições sem citação | média | hoje | fixed |
| C-016 | 2026-08-10 | Violações mecânicas das Regras 3 e 4b: 47 linhas com em dash, "genuine" 10x (inclusive abstract), "pre-registered" 2x, narração de processo em O7, §12 inteira defendendo o próprio paper | média | misto | fixed |
| C-017 | 2026-08-10 | Cosméticos de rotulagem: prefixo `thm:` em ambientes `empirical`/`remark`/`proposition`; 7 labels nunca referenciados; pasta `sec4-endogeny-barrier` do repo nunca citada | baixa | prévio | fixed |
| C-018 | 2026-08-10 | Bibliografia: anos de chave divergentes dos itens, URLs de blog truncadas, KL sem páginas, "Wirsching 1998, Conj. 3.9" vs "Corollary II.5.8" (checar fonte primária) | baixa | prévio | fixed |
| C-019 | 2026-08-10 | "identity checked to 2×10⁻¹³" no paper contra "2.3e-13 absolute at worst" no repositório | baixa | hoje | fixed |
| C-020 | 2026-08-10 | O5: "not the γ=3 stated above" é redação confusa (γ=3 aparece acima já como o valor corrigido), não contradição factual | baixa | hoje | fixed |
| C-021 | 2026-08-10 | `prop:always-frozen` repete literalmente o parágrafo anterior; seu título cobre só um dos dois roots que enuncia | baixa | hoje | fixed |
| C-022 | 2026-08-10 | §6 e §2 mantêm frases de posicionamento ("we highlight it early", "stands entirely on its own", "whose implementation") que a divisão tornou falsas | baixa | hoje | fixed |
| C-023 | 2026-08-10 | Abstract não reflete H-166/H-169: ignora os dois teoremas novos e ainda anuncia como melhor resultado de colisão o enunciado que `thm:diagonal-collision` superou | média | hoje | fixed |
| C-024 | 2026-08-10 | `thm:kl-calibrated` (linhas 726, 2367) diz "ten interval-widths"; o número certificado no companion paper 04 (`thm:kl-calibrated`, linhas 247-248, banda medida em três construções independentes = 0,0037, não a tolerância a priori 0,003) é "seven band-widths". C-002 desta mesma rodada corrigiu a contradição abstract/corpo sobre este resultado sem checar o número em si contra o paper 04, blindando o valor errado ao deixá-lo consistente internamente | média | hoje | fixed |
| C-025 | 2026-08-10 | §3 (evidência de `conj:tail-index`) e O7 na Conclusão atribuíam as baterias de raízes reais amostradas (Hill/EVT em q=3, bateria de 100.000 raízes em q=5) diretamente a `conj:tail-index` (a martingale $W_q$); na verdade medem o fator de escala de crescimento da árvore real, uma conjectura formalmente separada (`conj:real-tree-tail`) no companion paper 06. Achado feito e corrigido pela sessão de redação final do paper 06 (ver C-31 em `../06-pressao-qx1-ramificacao/CRITIQUE.md`), propagado aqui para manter os dois papers consistentes | alta | prévio | fixed |
| C-026 | loop R1 | Abstract, §1.2 e O3 dizem "we prove"/"Conjecture 1 is proved in Theorem X" para `thm:wirsching-conj1`, mas a prova está só no companion paper 05 (`WirschingCompanion`); o teorema em 01 é um `\begin{theorem}...\end{theorem}` sem `\begin{proof}`, recorrência exata do padrão já corrigido em C-001 | maior | prévio | fixed |
| C-027 | loop R1 | Colisão de notação: `K(\ell)` (função de cobertura sub-exponencial de Wirsching, `conj:wcc`) e `K_\ell`/`K_{q,\ell}` (collision mass da medida de Syracuse, definida linha ~1466) usam a mesma letra sem nenhuma frase de desambiguação nas seções que tratam da mesma família de conjecturas | moderado | prévio | fixed |
| C-028 | loop R1 | Construção "not merely P but Q"/"P, not Q" da família de antítese (Regra 4b) ocorria pelo menos 7 vezes (linhas 240, 875, 1085, 1437, 1551, 1985, 2496), acima do orçamento de duas por documento | menor | prévio | fixed |
| C-029 | loop R2 | Abstract e §3 atribuíam a Growth Exponent Conjecture (Kontorovich-Lagarias/Applegate-Lagarias, expoente $1$) à raiz não-trivial $\alpha_+=2$ em $q=3$, e diziam "The root is always unfrozen" para essa mesma raiz; `conj:transition-arithmetic` e `prop:always-frozen` já deixavam claro no próprio corpo que é $\alpha_-=1$ que reproduz a GEC e é sempre descongelada, e que $\alpha_+$ é sempre congelada | maior | prévio | fixed |
| C-030 | loop R2 | Construção de antítese "X, not Y" (forma simples, sem "merely") ocorria em pelo menos 26 lugares adicionais além das 2 já sancionadas no orçamento da Regra 4b | menor | prévio | fixed |
| C-031 | loop R2 | Três resíduos de narração de processo (Regra 4b §3): "the entropy implication previously asserted here is invalid" (linha ~971, termo nunca definido em outro lugar); "a reading that corrects how this project's own earlier attempt on Conjecture 2 had been framed" (§9.2); "not the one originally supposed" (O3 da Conclusão) | menor | prévio | fixed |
| C-032 | loop R3 | `prop:gauge` (a construção de gauge freedom que sustenta `thm:barrier`, o único Teorema não-migrado da "endogeny barrier") tinha 2 de suas 4 alegações, (b) mesmo índice de cauda e (c) mesmo coeficiente de regressão, sem prova, sem citação e sem verificação computacional, apesar de `rem:barrier-reading` declará-la "fully rigorous and independently verified"; notação `M_q(\alpha)` usada uma única vez, nunca definida; "regression slope $b$" nunca definido em nenhuma das 4 ocorrências | crítico | prévio | fixed |
| C-033 | loop R3 | `thm:conjecture3` (teste numérico da Conjectura 3 de Wirsching) era apresentado no abstract/§1.2 como computação própria deste paper ("we test the third"), mas a Data Availability já o classificava como material restatado do companion 05, que tem a derivação idêntica com mais detalhe; mesmo padrão de C-026, não pego para a Conjectura 3 | maior | prévio | fixed |
| C-034 | loop R3 | A subseção "Certified numerical test of Wirsching's Conjecture 3" continha, sem nova quebra de subseção, material sem relação com o título (decomposição microcanônica, ponte de limite local, tetracotomia de equivalência de ensembles) | moderado | prévio | fixed |
| C-035 | loop R3 | "precise/precisely" usado 3 vezes fora de sentido técnico (Regra 4b §1) | menor | prévio | fixed |

Checagens mecânicas que passaram, registradas para não serem refeitas:
34 chaves `\cite` contra 34 `\bibitem`, sem órfãos nem pendentes nas
duas direções; todo `\ref`/`\eqref` tem `\label` correspondente; nenhum
label duplicado.

---

## Rodada 2026-08-10: checagem pós-divisão e pós-ataque paralelo

Escopo: leitura integral de `main.tex` (2664 linhas) do início ao fim,
com atenção às costuras deixadas pela divisão em quatro papers e pela
inserção dos dois teoremas novos. Verificações independentes rodadas:
grep `\cite`↔`\bibitem`, grep `\ref`↔`\label`, leitura dos READMEs de
`collatz-endogeny/sec9-worst-cylinder-cascade` e
`collatz-endogeny/sec10-diagonal-shifted-collision`, conferência da
existência das quatro pastas de repositório citadas e dos três repos
companheiros.

### C-001 (alta): o abstract ainda promete provas que saíram do paper

O abstract descreve, na primeira pessoa e com o método explícito,
quatro provas que não estão mais no documento:

- linha 52-59: "We prove an exact identity, ρ_ann(α) = q^{α-1}/(2^α-1)
  ... via an exact fibre-counting bijection, correcting a
  finite-automaton argument for the same identity that we show is not
  well posed."
- linha 74-76: "We prove that the corresponding tilted q-adic measure
  is singular at every frozen root by an entropy identity and a
  fractional-moment estimate."
- linha 76-77: "We prove the tail index for the matching i.i.d. model
  by an implicit renewal theorem."
- linha 77-80: "For the coherent q-adic environment, we prove
  martingale convergence and identify the limit with the density of
  the absolutely continuous component."

O corpo correspondente (§3, linhas 317-322) agora abre com "This
section summarizes, without proof, the pressure-equation results a
companion paper establishes in full". As expressões "fibre-counting
bijection", "finite-automaton argument", "entropy identity",
"fractional-moment estimate" não ocorrem em nenhum outro ponto do
arquivo: são descrições de máquinas de prova que migraram inteiras
para o paper 06. Um parecerista que leia o abstract e procure a
bijeção não a encontra.

Por que importa: é a forma canônica do bug da Regra 8b, e cai na parte
do documento com maior densidade de leitura. Além disso, "We prove"
para um resultado cuja única prova está num manuscrito "in preparation"
sem DOI nem URL é overclaim sob a Regra 10b.

### C-002 (alta): o abstract contradiz o corpo e a Conclusão sobre KL vs. Volkov

Abstract, linhas 117-127: "We complement this theoretical package with
a fully independent, purely empirical result: implementing the exact
reverse tree of the 5x+1 map and applying Aitken Δ² extrapolation to a
sequence of nested-window measurements, we compare two competing
predictions ... measuring 0.639 (bootstrap interval [0.633,0.645]). The
remaining monotone finite-window drift prevents this interval from
deciding between the two asymptotic predictions."

Corpo, `thm:kl-calibrated` (linhas 725-735): "the arithmetic tree reads
0.64926 (95% interval [0.64818,0.65027]), separated from a control
built to exponent 0.678 by ten interval-widths ... The separation
widens, not narrows, as bias is calibrated away with depth."

Conclusão, O8 (linhas 2341-2348): "separated from a competing
prediction ... by ten interval-widths once the estimator's own bias is
calibrated out".

São três leituras incompatíveis do mesmo experimento no mesmo
documento. O abstract ficou parado na versão pré-E-139 (medição crua,
não decide) enquanto corpo e conclusão foram atualizados para a versão
calibrada (decide, por dez larguras). Um parecerista que compare
abstract e conclusão encontra isso em trinta segundos.

Agravante independente: o abstract descreve o experimento em primeira
pessoa ("implementing the exact reverse tree ... we compare"), mas §6
(linhas 695-698) agora diz "a companion paper \cite{KLVolkovCompanion}
reports an exact finite enumeration". O abstract reivindica como
próprio um resultado que o corpo atribui a outro paper.

### C-003 (alta): `thm:cascade-factor` é Theorem com uma etapa não provada

Enunciado nas linhas 1081-1091, esboço de prova nas linhas 1093-1115. O
passo em questão (linhas 1101-1105):

> "Since $t_0$ and $k_0$ are compatible between adjacent levels (an
> elementary but non-trivial fact, checked exhaustively for $\ell\le8$:
> zero exceptions), the scale factors cancel in the ratio"

Essa compatibilidade é o que faz a razão `R_ℓ` estar bem definida como
`W_ℓ(k)/W_{ℓ-1}(k mod 3^{ℓ-2})`, ou seja, é uma dependência estrutural
da tese, não um detalhe de verificação. Ela é sustentada por uma
enumeração exaustiva até ℓ=8.

Verifiquei o repositório antes de escrever isto (Regra 8c). O README de
`collatz-endogeny/sec9-worst-cylinder-cascade` também não prova o
passo: escreve "Since `t0` depends only on `y mod 3` and
`k0(y mod 3^(ell-1)) = k0(y) mod 3^(ell-2)`, the `3*2^-t0` factors
cancel", afirmando a segunda igualdade sem demonstração e sem sequer
mencionar a checagem numérica que o paper cita. Não existe, nem no
paper nem no repositório, prova da compatibilidade de `k_0`. (A parte
`t_0` é trivial: `2^t y ≡ 1 (mod 3)` com `2 ≡ -1` força a paridade de
`t` a depender só de `y mod 3`. Juntar as duas sob "elementary but
non-trivial" esconde que só uma delas é o problema.)

Consequência a jusante, e é aqui que o overclaim fica explícito. O2
(linhas 2228-2230): "Theorem~\ref{thm:cascade-factor} now gives an
unconditional bound, $\beta_{\mathrm{eff}}\le1.882712$". A cota herda a
condicionalidade do passo. Chamar de "unconditional" uma cota que
depende de uma identidade verificada até ℓ=8 é exatamente o que a
Regra 10b proíbe.

Duas outras imprecisões no mesmo bloco, menores mas na mesma direção:
"Substituting $N_{\ell-1}(A^jk)=N_{\ell-2}(A^jk')R_{\ell-1}(A^jk)$"
usa `k'` sem defini-lo (é `k mod 3^{ℓ-2}`, dedutível mas não dito); e
O2 afirma que "the remaining gap to β_eff→1 is exactly a pairwise
anti-concentration inequality", enquanto o corpo (linhas 1127-1129) diz
apenas que "any fixed exponent in such a bound would already improve
β_eff ≤ 1.88 toward 1": melhorar na direção de 1 não é o mesmo que
fechar, e "exactly" transforma uma condição suficiente parcial em
caracterização.

Contraste que vale registrar: `thm:diagonal-collision` (linhas
1825-1856), o outro teorema novo, não tem esse problema. Refiz o
cálculo: `P[a'-a=s] = 2^{-|s|}/3` está certo, `H_{ℓ-1}(0)=K_{q,ℓ-1}`
está certo, a nulidade de `H(s)` para `s` ímpar em `q=3` (que sustenta
o `2Σ4^{-r}G(r)`) segue de `Y ≡ 1 mod 3`, e `G_{ℓ-1}(1)=T_{ℓ-1}(4,1)`
confere. O esboço é uma prova completa em miniatura; o rótulo "Proof
sketch" é conservador demais, não otimista demais. O único defeito
associado é C-012 (ausência na Data Availability).

### C-004 (alta): a lista O1-O8 afirma resultados que o corpo não contém

A reescrita de hoje importou achados do ataque paralelo direto para a
Conclusão sem passar pelo corpo. Três casos:

**O1 (linhas 2214-2221).** "the diagonal Fourier coefficient the
second-moment route actually consumes does cancel under that same
average, with the surviving resonance confined to the coarse affine
mode this direction already discards". Não há, em §8 nem em §10.1,
nenhum lema, proposição ou resultado empírico que estabeleça esse
cancelamento; `lem:cov-spectral` e `prop:exact-endogeny` estabelecem o
oposto (a dependência "survives entirely as the diagonal frequency
pairing", linha 1375-1376), e `rem:calibration-consistency` calcula
`E[Corr] = -3/7` exatamente sob a média pela medida de ramificação nos
gaps (linhas 1456-1460), isto é, sob "that same average" a que O1 se
refere. O item ainda se contradiz internamente em três orações: afirma
o cancelamento, depois diz "the gap is that this cancellation is over
the free arithmetic parameter of the coupling theorem, not over the two
path indices at a fixed integer". Como está, o leitor não consegue
decidir o que foi mostrado.

**O4 (linhas 2266-2269).** "Measured through $\ell=15$, the primitive
spectrum sits at the square-root scale on average but is visibly
concentrated, not flat". `\ell=15` ocorre uma única vez no arquivo,
nesta linha (grep confirmado). Não há resultado empírico no corpo, não
consta do Apêndice de validação, não consta da Data Availability. É uma
medição numérica anunciada só na conclusão, o que a Regra 11 veda.

**O4, segunda parte (linhas 2262-2265).** "O4's pointwise target would
imply, via the same Parseval identity underlying
Theorem~\ref{thm:multiscale-parseval}, the L² finiteness condition of
O7 — a bridge in the opposite direction from the one used elsewhere in
this paper, not previously recorded." Uma implicação matemática nova,
enunciada pela primeira vez na conclusão, sem prova e sem entrada no
corpo. "not previously recorded" é ainda narração de processo (Regra
4b §3).

### C-005 (alta): a §9.2 condensada não é interpretável sozinha

A extração da prova de Wirsching 2003 levou junto as definições.
Restou:

- As cinco condições `(?1)`-`(?5)` são referidas dezesseis vezes
  (linhas 1177, 1178, 1179, 1181, 1182, 1189, 1227, 1230, 1240, 1247,
  1252, 1285, 1304, 2238, 2245) e **nunca enunciadas**. A única pista é
  o parêntese em `thm:microcanonical` (linhas 1227-1229), que glosa
  `(?3)` como "a uniform lower bound $g_\ell(k,a)\ge\eta\,\overline
  g_\ell(k)$ on the central-limit window". `(?1)`, `(?2)`, `(?4)` e
  `(?5)` não recebem nem isso.
- Consequência direta: `thm:wirsching-conj1` (linhas 1188-1191) enuncia
  "Condition $(?2)$ implies condition $(?1)$, with a possibly smaller
  central-limit window." Nenhum leitor deste documento sabe o que foi
  provado. É o teorema que O3 usa para declarar "Conjecture 1 is
  proved".
- `g_\ell(k,a)` ("Wirsching's generator", linha 1221) nunca é definido,
  nem relacionado a `e_\ell(k,a):=|E_{\ell,k}(a)|`, que é o objeto de
  fato definido (linha 1157). São notações diferentes para objetos
  aparentados, e a ponte ficou no companion.
- Tensão interna adjacente: a linha 1178-1179 diz que
  "$(?3)\Rightarrow(?2)$" é um dos dois teoremas provados por
  Wirsching, e a linha 1181-1182 diz que "$(?3)$ and $(?2)$ are in fact
  the same inequality (only the quantifier changes)". Se são a mesma
  desigualdade, a implicação como teorema publicado precisa de outra
  redação.

Isso é mais grave que C-006 porque ali falta notação recuperável por
contexto; aqui falta o conteúdo dos objetos sobre os quais o paper
enuncia um teorema seu.

### C-006 (média): notação órfã na §3 condensada

- `Z_k(\alpha;\cdot)`, "the depth-$k$ partition function", aparece no
  enunciado de `thm:pressure` (linha 329) e em `thm:qadic-martingale`
  (linha 412). Nunca é definida. A definição vivia na prova removida.
- `F_k` aparece em `thm:lp-collision` (linha 421, "the law of $F_k$
  modulo $q^k$"). A única definição de `F` no paper é
  `\eqref{eq:syracuse-def}`, escrita especificamente com base 3 e
  módulo `3^n`. Para `q` geral não há definição.
- O adjetivo "tilted" ("tilted projective measure $\mu_\alpha$", linha
  415; "$p$ independent tilted Syracuse sums", linha 428; "the tilted
  $q$-adic measure", abstract linha 75) descreve uma construção de
  inclinação exponencial em `α` que o paper nunca apresenta.
- `M_k^{(\alpha)}` recebe duas definições diferentes em teoremas
  consecutivos: `M_k^{(\alpha)}(U):=Z_k(\alpha;U\bmod q^k)` (linha 412)
  e `M_k^{(\alpha)}=q^k\mu_{\alpha,k}` (linha 422). Só são compatíveis
  se `Z_k(\alpha;u)=q^k\mu_{\alpha,k}(u)`, o que não é dito em lugar
  nenhum.

### C-007 (média): cota anterior e `β_eff` sem referente

Linha 1117-1119: "At level $L=10$, exact rational arithmetic certifies
$\beta_{\mathrm{eff}}\le1.882712$, improving the previous unconditional
bound $2.306270$ recorded above."

`2.306270` ocorre uma única vez no arquivo (grep confirmado): nesta
linha. Não está "recorded above" em lugar algum. O README de
`sec9-worst-cylinder-cascade` esclarece a origem: "beating the
`2.306270` previously recorded in H-158", isto é, uma nota interna de
hipótese, não o paper. O mesmo README registra que a cota de H-158 é
"a sketch not rederived line by line", o que torna "the previous
unconditional bound" duplamente frágil.

No mesmo bloco, `\beta_{\mathrm{eff}}` é usado seis vezes (linhas 1075,
1088, 1118, 1123, 1129, e O2 em 2229/2231) e nunca definido. Pelo
contexto é `-\log_3 c_\ell/\ell`, mas o leitor tem que reconstruir isso
a partir da desigualdade da linha 1086 para conferir a aritmética.

### C-008 (média): a lista de contribuições (§1.2) não bate mais com o corpo

- Item (i), linhas 213-217: "A closed-form pressure equation for $qx+1$
  (§3). We show that the tail exponent ... satisfies the exact
  equation". Não sinaliza que a prova está no paper 06.
- Item (iv), linhas 231-234: "A finite-window empirical result (§6).
  Exact enumeration and Aitken Δ² extrapolation compare two predictions
  ..., while retaining a visible pre-asymptotic window bias." Ignora
  `thm:kl-calibrated` (mesmo problema do abstract, C-002) e não
  atribui ao paper 04.
- Nenhum dos oito itens menciona `thm:cascade-factor` nem
  `thm:diagonal-collision`, que são o conteúdo novo do dia, nem o
  programa de renormalização logarítmica da colisão
  (`thm:logarithmic-collision`, `thm:multiscale-parseval`), que é hoje
  o material mais substancial de §10.

O `OUTLINE.md` já registra essa pendência ("A lista de contribuições
precisa ser conferida contra o corpo atual"), mas ela continua aberta
em `main.tex`, que é o que o parecerista lê.

### C-009 (média): o título anuncia um resultado que migrou

"The $qx+1$ Generalization of Tao's Syracuse Measure: A Closed-Form
Pressure Equation, an Endogeny Barrier, and Complementary Viewpoints on
the Arithmetic Obstruction" (linhas 35-37).

O primeiro dos três itens do subtítulo é hoje o objeto do paper 06,
restituído aqui como enunciado sem prova. Sob a Regra 10b, o título
sugere uma categoria de contribuição (resultado próprio, provado) mais
forte que a entregue.

### C-010 (média): duas contagens erradas na Discussão

Linhas 2144-2152: "the outcome of executing both candidate lemmas was
not silence: it was **two** independent, rigorous negative/structural
results, each of which pins down precisely why a natural approach fails
— Proposition~\ref{prop:exact-endogeny}'s ...; Empirical
Result~\ref{thm:l2-finite}'s ...; Theorem~\ref{thm:jensen}'s ...".
Três itens após "two". Pior: o segundo é um Empirical Result que o
próprio corpo qualifica como "evidence against boundedness, but do not
prove $K_\infty=\infty$" (linhas 1488-1489), e aqui é chamado de
"rigorous ... result".

Linhas 2177-2182: "a barrier reached by **four** complementary
vocabularies (branching-process fixed points, integer covering/entropy
counting, a real functional equation, second-moment character sums,
and elementary residue counting)". Cinco itens no parêntese depois de
"four" (o abstract, linha 104, também diz "four"). O quinto,
"elementary residue counting", corresponde à rota Chang, que O6 fecha
explicitamente como auditoria e declara "not counted as an open problem
of this paper" (linhas 2289-2295).

### C-011 (média): a Discussão aponta o resultado errado como carro-chefe

Linhas 2184-2190: "this theoretical package sits alongside a result
(Empirical Result~\ref{thm:kl}) whose validity does not depend on any
of the above framing at all: a direct, falsifiable, statistically
calibrated finite-window measurement ... We consider this the single
most framing-independent contribution of the paper".

Três problemas empilhados. (a) `thm:kl` é justamente a medição **não**
calibrada; a calibrada é `thm:kl-calibrated`. (b) Ambas são hoje
resultados do paper 04, restituídos sem prova, de modo que "of the
paper" está errado. (c) "recommend it be weighted accordingly by a
reader assessing the paper's overall reliability" é uma frase cujo
sujeito é o próprio paper (Regra 4b §3).

### C-012 (média): Data Availability e Apêndice fora de sincronia

**Data Availability (linhas 2356-2391).** Lista nominalmente as
verificações de `thm:wcc-large-deviation`,
`thm:fresh-digit-coupling`, `prop:primitive-hole`,
`prop:primitive-fibre-energy`, `thm:multiscale-parseval` e
`thm:logarithmic-collision`. **Não** lista `thm:cascade-factor` nem
`thm:diagonal-collision`, apesar de o corpo citar explicitamente
`collatz-endogeny/sec9-worst-cylinder-cascade` (linha 1149) e
`collatz-endogeny/sec10-diagonal-shifted-collision` (linha 1879).
Confirmei que ambas as pastas existem no repositório e contêm README +
scripts, então o defeito é de sincronização da seção, não de
reprodutibilidade.

**Repos companheiros.** As linhas 2375-2391 dizem três vezes "in a
companion paper and repository \cite{...}", mas os três `\bibitem`
correspondentes (linhas 2550-2562) dizem apenas "companion paper, in
preparation", sem URL, DOI ou arXiv. Um leitor não tem como chegar aos
repositórios `collatz-qx1-pressure`, `collatz-kl-volkov` e
`collatz-wirsching-2003` (que existem localmente). Sob a Regra 12, uma
seção de disponibilidade que anuncia repositórios sem endereço é pior
que não anunciá-los.

**Apêndice (linhas 2408-2514).** Declara documentar "the validation
discipline applied to each computational result reported above", mas
está simultaneamente inflado e incompleto. Inflado: mantém entradas
para material migrado (roots da equação de pressão §3; recursão de
momentos de Wirsching 2003; multiplicidades microcanônicas; projeção de
ensemble a precisão fixa; não-equivalência de blocos lineares), todos
hoje atribuídos aos companions pela Data Availability. Incompleto:
nenhuma entrada para `thm:cascade-factor` nem para
`thm:diagonal-collision`, os dois resultados computacionais novos.

### C-013 (média): os rótulos O1-O8 são usados antes de existirem

O corpo faz referência aos itens da conclusão em pelo menos cinco
pontos, todos anteriores a §13: "sharpens the distinction between O2
and O3" (linha 1059), "This is the central microcanonical regime"
seguido de "O2's remaining content" (linha 1123), "the precise overlap
between O5 and the $L^2$ branch of O7" (linhas 1721-1722), "the
unresolved $q=3$ part of O7" (linha 1808), "O2's remaining gap" (linha
1144). A lista O1-O8 só aparece na linha 2207, sem `\label`, sem
ponteiro antecipado. Um leitor na página 18 não tem como resolver "O2".
A reescrita de hoje aumentou a densidade dessas referências sem
introduzir a lista antes.

### C-014 (média): frase quebrada dentro de `thm:propC`

Linhas 2002-2008, dentro do enunciado da proposição:

> "a further articulation, within the same second-moment Fourier
> vocabulary as the $L^2$ condition. Theorem~\ref{thm:multiscale-parseval}
> identifies their exact telescoping relation, while both enter the
> covariance sum $\Cov\propto\sum_\xi S_1(\xi)S_2(\xi)^\ast$ of
> \S\ref{sec:regimes}), of the same missing ingredient --- not a
> methodologically independent fourth or fifth route in its own right."

Há um `)` sem abertura correspondente e a oração "of the same missing
ingredient" ficou pendurada, sem regente. É resíduo de emenda: a frase
original provavelmente tinha um parêntese longo que foi partido ao
meio. Está no enunciado de um resultado formal, não em prosa corrida.

### C-015 (média): "três medições empíricas" em três versões diferentes

- Abstract, linhas 80-82: "At $q=3$ the predicted index $\alpha^\ast=2$
  matches **three empirical measurements** in earlier work on the
  classical Collatz map".
- §3, linhas 449-451: "threefold empirical support (Hill estimator,
  extreme-value theory, and **the counting-exponent confirmation
  below**)".
- §4, linhas 576-578: "measured by three independent methods (**the
  pressure equation**, Hill estimator, extreme-value theory)".

As duas listas nomeadas discordam entre si no terceiro item, e a
equação de pressão não é uma medição empírica, o que faz a versão do
abstract ("three empirical measurements") divergir de §4. Pior, "the
counting-exponent confirmation below" ficou pendurada: a única
confirmação de expoente de contagem abaixo é §6, que é `q=5` e migrou
para o paper 04. Não há confirmação de expoente de contagem para `q=3`
neste documento.

Adicionalmente, as medições de Hill e de valores extremos são
atribuídas a "earlier stages of this line of work" (linha 353) e
"earlier work on the classical Collatz map" (abstract), sem citação,
sem repositório e sem entrada no Apêndice. Sob a Regra 11, um número
que sustenta o abstract precisa de fonte verificável.

### C-016 (média): violações mecânicas das Regras 3 e 4b

Consolidado numa entrada. Contagens obtidas por grep:

- **Em dash**: 47 linhas contêm `---`, incluindo pares no abstract
  (linhas 56-58, 86-88, 117) e dentro de enunciados formais. A Regra 3
  o proíbe em qualquer lugar; a Regra 4b §2 proíbe adicionalmente os
  travessões pareados. Meta declarada: zero.
- **Vocabulário banido**: "genuine/genuinely" 10 vezes, incluindo o
  abstract ("a genuine closed-form structure theorem", linha 111) e o
  título de §12 ("why a precisely characterized barrier is a genuine
  contribution"). Também "precisely" fora de uso técnico e "rich"/
  "crucial" pontuais.
- **"pre-registered"** duas vezes (linhas 453 e 2319), banido fora de
  contexto clínico/psicométrico pela Regra 4b §3.
- **Narração de processo**, introduzida ou mantida na reescrita de
  hoje: O7, linhas 2316-2319, "Empirical support, however, has
  substantially strengthened since the original under-powered
  measurement: a $20\times$ larger sample ($10^5$ roots, the
  pre-registered comparison called for above)"; §3, linhas 452-457, na
  mesma linha; §7, linhas 812-818, "An earlier reading of the first 17
  points suggested ... which the three new points ... revealed to be an
  artifact". A Regra 4b §3 é explícita: correções acontecem antes da
  submissão e depois desaparecem.
- **§12 inteira** ("Discussion: why a precisely characterized barrier
  is a genuine contribution") é uma seção que defende o valor do
  próprio texto, abrindo com "A natural objection to the material ...
  is that ..." (linha 2137). A Regra 4b §3 proíbe as duas coisas
  nominalmente: seções defendendo o valor do texto e antecipação de
  objeção de parecerista. Mesma família: "We deliberately frame this
  paper not as an attempted proof ..." (linhas 253-258), que combina
  "we deliberately" (meta-honestidade), a antítese "not X but Y" e um
  parágrafo de instruções de leitura na Introdução; e a última frase do
  abstract, "We distinguish exact identities, conditional reductions,
  and analogies, and state the remaining estimates separately" (linhas
  134-135), cujo sujeito é a disciplina epistêmica do próprio paper.

### C-017 (baixa): cosméticos de rotulagem, consolidados

- Prefixo `thm:` em ambientes que não são teoremas: `thm:kl`,
  `thm:kl-calibrated`, `thm:wcc`, `thm:conjecture3`, `thm:l2-finite`,
  `thm:lp-spectrum`, `thm:fixed-precision-finite`,
  `thm:microcanonical-finite`, `thm:microcanonical-fourier` são
  `empirical`; `thm:regime3` é `remark`; `thm:propC` é `proposition`.
  Não afeta o PDF (o ambiente é que imprime a categoria, e a Regra 10b
  está satisfeita ali), mas cria armadilha para quem grepar `thm:`
  procurando teoremas.
- Sete labels nunca referenciados: `thm:qadic-martingale`,
  `prop:fabius`, `prop:halasz-deficit`, `rem:novelty-109`,
  `eq:pressure-closed-form`, `app:validation`, `sec:conclusion`. O caso
  de `thm:qadic-martingale` é o que incomoda: é um teorema de §3
  mantido na condensação justamente porque "o resto do paper referencia
  os rótulos diretamente" (OUTLINE), e ninguém o referencia.
- `prop:halasz-deficit` não referenciado combina mal com o título da
  subseção "Proposition C: an exact wall of constants", já que
  "Proposition C" é apelido de `thm:propC`, não dele.
- A pasta `collatz-endogeny/sec4-endogeny-barrier` existe no
  repositório e não é citada em nenhum ponto de `main.tex`, embora §4
  seja uma seção própria do paper.

### C-018 (baixa): bibliografia: itens a conferir na fonte primária

`\cite`↔`\bibitem` fecha 34 contra 34, sem órfãos nos dois sentidos, e
não há `\ref` pendente. Restam pontos de conferência, nenhum deles
verificado por mim contra a fonte primária (registro como pendência,
não como erro confirmado):

- Chave `KontorovichLagarias2009` com entrada datada de 2010 ("The
  Ultimate Challenge", AMS, 2010) e sem páginas.
- Chave `Spiegelhofer2021` com entrada "Israel Journal of Mathematics
  258 (2023), 475--502".
- `Tao2011` e `Tao2020` com URLs truncadas
  (`https://terrytao.wordpress.com/2011/08/25/`, idem 2020), sem o
  slug do post; não resolvem.
- `conj:wcc` atribui "Wirsching 1998, Conj. 3.9" enquanto a linha 749
  cita do mesmo livro "his Corollary II.5.8 and Chapter V". Os dois
  estilos de numeração são incompatíveis; um dos dois está errado, ou o
  livro usa ambos. Precisa de checagem na fonte (Regra 11).
- `Chang2026` (arXiv:2603.25753) e `ChangCompanion2026`
  (arXiv:2603.11066): não reverificados nesta rodada.

### C-019 (baixa): precisão numérica declarada abaixo do medido

Linha 1853-1854: "identity checked to $2\times10^{-13}$". O README de
`sec10-diagonal-shifted-collision` registra "the identity holds to
`2.3e-13` absolute at worst". O paper arredonda para baixo um erro
máximo, o que inverte o sentido da garantia.

### C-020 (baixa): redação confusa em O5

Linhas 2285-2288: "the deficit's true inversion point is
$\gamma\approx3.31$, not the $\gamma=3$ stated above". O corpo, na
linha 1984-1986, já diz "the actual inversion point is
$\gamma\approx3.31$ ..., not $\gamma=3$", ou seja, γ=3 aparece acima
apenas como o limiar ingênuo já corrigido, não como afirmação do paper.
Não é contradição factual; é uma frase que dá ao leitor a impressão de
que o paper se contradiz. Reescrever.

### C-021 (baixa): duplicação em `prop:always-frozen`

Linhas 360-369. O parágrafo diz "$s(\alpha_-)>0$ (\emph{unfrozen}) and
$s(\alpha_+)<0$ (\emph{frozen}) unconditionally, for every odd
$q\ge3$", e a proposição imediatamente abaixo enuncia "For every odd
$q\ge3$: $s(\alpha_-)>0$ and $s(\alpha_+)<0$." É a mesma frase duas
vezes seguidas. Além disso o título "The larger root is always frozen"
cobre só metade do enunciado.

### C-022 (baixa): frases de posicionamento que a divisão tornou falsas

- §6, linhas 737-740: "This result stands entirely on its own,
  independent of the theoretical program of §§4-10; **we highlight it
  early in the paper's overall argument** because it is the least
  framing-dependent contribution reported here." É a §6 de 13, e o
  resultado é do paper 04.
- §2, linhas 295-297: "nor the numerical enumeration of §6 below,
  **whose implementation** already excludes exactly these classes". A
  implementação migrou para o repositório do paper 04; o leitor deste
  paper não tem como inspecioná-la.

### C-023 (média): o abstract não incorporou H-166 nem H-169

Contraparte de C-008 (que trata da §1.2) no lado do abstract, e o
segundo braço do bug da Regra 8b: aqui a defasagem é por omissão, não
por excesso.

Os dois teoremas inseridos hoje no corpo não aparecem no abstract.
`thm:cascade-factor` (§9.1, `β_eff ≤ 1.882712`, a primeira cota
numérica sobre a massa do pior cilindro que o paper exibe) e
`thm:diagonal-collision` (§10.2, `K_{q,ℓ} ≥ (q/3)^ℓ`) não são
mencionados em nenhuma das linhas 48-136.

Pior que a omissão: o abstract ainda apresenta como melhor resultado de
colisão o enunciado que foi superado no mesmo dia. Linhas 104-107: "A
diagonalization in discrete-logarithm coordinates proves exponential
collision growth for every odd prime $q\ge5$ **whose order of $2$ lifts
maximally**, and reduces the critical case $q=3$ to an explicit signed
spectral balance." O corpo, linhas 1858-1874, diz que
`thm:diagonal-collision` "strictly improves
Theorem~\ref{thm:logarithmic-collision}'s constant for every $q\ge5$
where the latter applies, and it covers the exceptional (Wieferich)
primes and composite odd $q$, both excluded there", e substitui a
redução em `q=3` por outra ("a single affine shifted collision,
positivity only, no cancellation"). O abstract portanto anuncia uma
hipótese de levantamento maximal que o paper não precisa mais e uma
redução em `q=3` que o paper já trocou. É subdeclaração, não
overclaim, mas é igualmente uma dessincronia entre abstract e corpo.

Defeito de redação vizinho, na mesma frase do abstract (linhas
100-103): "two candidate lemmas suggested as natural next steps by
Tao's bivariate Fourier-decay technique \cite{Tao2022,Tao2011}, **whose
primitive Fourier energy** is the exact level increment of the $L^2$
collision mass". O antecedente de "whose" ficou impossível de
recuperar (nem os dois lemas nem a técnica de Tao têm "primitive
Fourier energy"; o objeto é a lei de Syracuse, via
`prop:primitive-fibre-energy` e `thm:multiscale-parseval`). Provável
resíduo de emenda anterior; a reescrita que C-001 já força deve
absorvê-lo.

## Rodada 2026-08-10 (produtor): correções aplicadas

Todas as 23 entradas foram lidas e verificadas independentemente
(Regra 8c) antes de qualquer correção; nenhuma foi aceita só por
confiança no crítico. 22 fixed, 1 open (C-018, ver abaixo).

**Altas (C-001 a C-005).** Abstract reescrito por completo: "We
prove" trocado por "A companion paper proves" nos quatro resultados
migrados; a leitura de KL-Volkov alinhada à versão calibrada
(`thm:kl-calibrated`) igual ao corpo e a O8; os dois teoremas novos
(`thm:cascade-factor`, `thm:diagonal-collision`) incorporados com os
enunciados corretos, substituindo a hipótese de levantamento maximal
já superada. Como efeito colateral da reescrita completa, o defeito
vizinho anotado ao final da rodada anterior ("whose primitive Fourier
energy", antecedente órfão) desapareceu junto. `thm:cascade-factor`
ganhou uma prova completa e autoderivada da compatibilidade
$t_0$/$k_0$ (não mais "checked exhaustively for $\ell\le8$"), e o
ambiente virou `\begin{proof}` normal. O1 e O4 tiveram as alegações
sem âncora (cancelamento do coeficiente diagonal; espectro primitivo
ℓ=15; ponte O4→O7 como achado "not previously recorded") reescritas
como "not reported in this paper", preservando só o que o corpo de
fato sustenta. A §9.2 condensada ganhou um bloco definicional
explícito para $(\star1)$–$(\star5)$ e para $g_\ell(k,a)$; a mesma
correção de símbolo ($(?N)\to(\star N)$) foi aplicada preventivamente
aqui, antes mesmo de a crítica do paper 05 (que tem o mesmo defeito)
ter sido processada.

**Médias (C-006 a C-015, C-023).** §3 condensada ganhou definições de
$Z_k(\alpha;u_0)$, "tilting"/$\mu_\alpha$, e a reconciliação de
$M_k^{(\alpha)}$ via $F_k$. `β_eff(ℓ)` agora tem definição explícita
e as duas cotas de aquecimento (2.523719, depois 2.306270) aparecem
no corpo antes de `thm:cascade-factor` as melhorar. §1.2 (lista de
contribuições) reescrita: item (i) e o antigo item (iv) agora
atribuem a prova ao companion certo; dois itens novos cobrem
`thm:cascade-factor` e `thm:diagonal-collision`. Título perdeu "A
Closed-Form Pressure Equation" (Regra 10b: esse resultado é do paper
06 agora). §12 reescrita inteira: contagem corrigida (três itens, não
dois; quatro rotas, não cinco, removendo a rota Chang que O6 já fecha
como auditoria), e `thm:kl` trocado por `thm:kl-calibrated` como o
resultado citado, com a atribuição correta ao companion 04 e sem a
frase de auto-avaliação ("we consider this the single most... of the
paper"). Data Availability e Apêndice sincronizados: os dois teoremas
novos entraram nos dois; cinco entradas do apêndice que documentavam
material hoje migrado (equação de pressão, recursão de momentos de
Wirsching, multiplicidades microcanônicas, projeção de precisão
fixa, não-equivalência de blocos lineares) foram removidas, com uma
nota explícita apontando para o apêndice do companion correspondente;
os três `\bibitem` de companion ganharam URL de repositório. Um
ponteiro antecipado para a lista O1-O8 foi inserido no primeiro uso
de um rótulo O\emph{n} no corpo (linha ~1050), resolvendo C-013 sem
precisar mover a lista inteira. A frase quebrada em `thm:propC` foi
reconstruída (o parêntese sem abertura e a oração "of the same
missing ingredient" pendurada agora formam uma frase completa). As
três versões divergentes de "três medições" foram unificadas: a
equação de pressão deixou de ser chamada de "medição empírica"
(ela é exata, não estatística); "the counting-exponent confirmation
below" (que apontava para nada, já que §6 é $q=5$ e migrou) foi
removida; Hill/EVT ganharam atribuição honesta ("earlier,
classical-map-only work of this project ... not detailed in this
paper") em vez de citação inventada. C-023 já estava resolvido como
efeito colateral da reescrita do abstract (C-001/C-002); confirmado
por leitura, sem edição adicional necessária.

**Baixas (C-016 a C-022).** Contagem de em dash (`---`): 47 linhas
antes, 0 agora, todas reescritas com vírgula, dois-pontos ou frase
separada, nunca apagadas sem reestruturar. "genuine/genuinely": 9
ocorrências reais encontradas (a rodada anterior contou 10; uma já
tinha sido removida por uma edição anterior desta mesma sessão),
todas trocadas por "actual", "real", "fully" ou simplesmente
cortadas. "pre-registered": as duas ocorrências (O7 e §3) removidas
junto com a narração de processo ao redor ("since the original
under-powered measurement", "for the first time in this
investigation"); o mesmo padrão em §7 ("An earlier reading ...
revealed to be an artifact") reescrito para descrever só o estado
atual dos dados. Achado extra fora do escopo original da crítica: o
parágrafo de Acknowledgments deste paper ainda dizia "used to support
literature review, mathematical analysis, numerical experimentation,
and manuscript preparation", violando diretamente a Regra 5b (a
convenção fixa do projeto é só "textual review and translation");
corrigido para o mesmo texto usado nos papers 04/05/06. Bibliografia
(C-018): páginas 131-188 e arXiv:0910.1944 confirmados para
Kontorovich-Lagarias diretamente na página do arXiv (WebFetch); URLs
completas do blog do Tao (2011 e 2020) confirmadas por busca e
inseridas; Spiegelhofer2021 conferido (ano/páginas do `\bibitem` já
batiam com a fonte, só a chave BibTeX tem o ano errado, o que não
aparece no PDF, deixado como está); Chang2026/ChangCompanion2026
conferidos, título e autor batem. **Permanece aberto**: "Wirsching
1998, Conj. 3.9" vs "Corollary II.5.8" não pôde ser verificado, o
livro não está indexado o suficiente para busca web resolver a
numeração interna; recomendo checagem manual contra o livro físico
ou uma cópia digitalizada antes da submissão. `prop:always-frozen`
não repete mais o parágrafo anterior (o parágrafo agora só
introduz a notação, sem afirmar o resultado) e seu título passou a
cobrir os dois roots ("The freezing transition is unconditional"). As
frases de posicionamento em §2 e §6 datadas pela divisão foram
reescritas ou removidas (a frase "we highlight it early... least
framing-dependent contribution" foi cortada inteira; "whose
implementation" agora aponta para o companion certo). C-017 recebeu
correção parcial deliberada: a pasta `sec4-endogeny-barrier` passou a
ser citada onde o Lema 2-ádico é enunciado; a renomeação do prefixo
`thm:` em ambientes `empirical`/`remark`/`proposition` e os labels
sem uso restantes (`prop:fabius`, `prop:halasz-deficit`,
`thm:qadic-martingale`, `eq:pressure-closed-form`, `app:validation`)
foram deixados como estão: o próprio crítico registrou que isso não
afeta o PDF, e renomear rótulos usados em dezenas de `\ref` por todo
o documento é risco desproporcional ao ganho (Regra 8d).

## Rodada 2026-08-10 (produtor, follow-up): C-018 fechado

O item sobre "Corollary II.5.8" vs "Wirsching 1998, Conj. 3.9" foi
reaberto e resolvido: o livro de 1998 está no repositório
(`literature/papers/131_Dynamical-System-3n1-Function-Wirsching-Book.pdf`,
166 páginas, texto extraído com `pdftotext`). Conferido diretamente:
`CHAPTER II` começa na linha 2059 do texto extraído e `CHAPTER V`
("Mixing and predecessor density") na linha 9312. Dentro do Capítulo
II, o item "5.8" é um `THEOREM` (não `Corollary`) sobre uma cota para
o grafo de Collatz podado, assunto não relacionado à densidade de
predecessores. Dentro do Capítulo V, a numeração de seção volta a
`1.x`, `2.x`, `3.x`; a "WEAK COVERING CONJECTURE FOR MIXED POWER SUMS"
é o item `3.9`, e o `3.10. REDUCTION THEOREM` logo depois é o
resultado que de fato reduz a propriedade de densidade uniforme à
conjectura de cobertura fraca, batendo exatamente com a frase do
paper ("identifies the following combinatorial covering property as
sufficient for uniform positive predecessor density"). Não existe
`Corollary II.5.8` no livro com esse conteúdo; a citação estava errada
desde antes desta sessão. Corrigido para "his Reduction Theorem
V.3.10, building on the Weak Covering Conjecture V.3.9" e "Wirsching
1998, V.3.9" no rótulo da conjectura (linhas ~738-751). C-018 fechado
como `fixed`.

## Rodada 2026-08-10 (verificação independente pós-varredura dos 4 papers): C-024

Verificação adversarial separada da divisão em quatro papers e das
varreduras de backlog por sub-agente dedicado (01/04/05/06), pedida
pelo diretor científico antes da redação final. Não reabriu nem
questionou nada já fechado sem evidência nova (Regra 8d); achado único,
verificado de forma independente (Regra 8c) antes de corrigir.

### C-024 (média): "ten interval-widths" sobrevivia à correção "dez→sete"

`thm:kl-calibrated` (linhas 726 e 2367 do `main.tex` de 01) dizia "ten
interval-widths" separando a leitura da árvore aritmética (0,64926) de
um controle de expoente 0,678. O número certificado é "seven
band-widths": o companion paper 04 (`thm:kl-calibrated`, linhas 237-254)
mede a banda de ruído por três construções independentes de expoente
0,650919 (leituras 0,64751/0,64981/0,65122, banda 0,0037), não pela
tolerância a priori de calibração (0,003) usada implicitamente na
redação antiga de 01; 0,0282/0,0037 ≈ 7,6 ("mais de sete"), não
0,0282/0,003 ≈ 9,4 ("dez").

A correção "dez→sete" já tinha acontecido nesta mesma sessão (commit
`90c3e2f`, "Corrige razão de larguras de banda no portão KL vs Volkov"),
mas tocou só `hypotheses/H-113...md`, o `OUTLINE.md` e o `main.tex` do
paper 04, nunca a restatement condensada em 01 (por desenho do split em
quatro papers, cada `main.tex` é editado independentemente). A rodada de
crítica anterior (C-002 desta mesma tabela) pegou uma contradição real
entre abstract e corpo sobre este mesmo resultado, mas resolveu a
inconsistência *interna* mantendo "ten interval-widths" nos dois
lugares, sem cruzar o número contra o paper 04 citado (`\cite{KLVolkovCompanion}`) — o
que blindou o valor errado ao torná-lo consistente, um modo de falha
que Regra 8b não cobre por não ser abstract-vs-corpo dentro do mesmo
documento, e sim corpo-vs-companion entre dois documentos.

Corrigido nas duas ocorrências (726, 2367): "ten interval-widths" →
"seven band-widths", igualando à redação do paper 04. Não há
`main-pt-br.tex` para 01 nesta sessão (removido deliberadamente em
`a586159` até uma rodada estável, ver `OUTLINE.md`), então não há
segunda língua a sincronizar aqui. `main.tex` recompilado limpo depois
da correção.

---

## 2026-08-10 — C-025, propagado da sessão de redação final do paper 06

Achado feito por outro agente (worktree isolado, dono do paper 06)
durante a formalização de H-129 lá: as baterias de raízes reais
amostradas citadas em §3 e em O7 (Hill/EVT em $q=3$; GPD/Hill/Vuong em
100.000 raízes de $q=5$) eram descritas como evidência de
`conj:tail-index` (a martingale Haar-q-ádica $W_q$), mas na verdade
amostram raízes inteiras reais e medem $N_v(vH)/H^{\alpha_-(q)}$, o
fator de escala de crescimento da árvore real, que o paper 06 formaliza
como conjectura própria (`conj:real-tree-tail`, distinta de
`conj:tail-index`; ver C-31 em
`../06-pressao-qx1-ramificacao/CRITIQUE.md` para o achado completo e a
verificação, incluindo consulta ao Codex antes de editar).

Propagado para cá para manter os dois papers consistentes, já que 01
restata a mesma evidência em §3 (linhas 417-427 antes da correção) e no
item O7 da Conclusão. Corrigido em ambos os lugares: o enunciado da
conjectura (`\begin{conjecture}...\label{conj:tail-index}`) não mudou,
só a atribuição de qual evidência a apoia; uma frase nova em cada local
aponta para a conjectura companheira do paper 06 e nota que o teste
exato e direto de $W_q$ (soma sobre toda a população de resíduos, não
amostra) continua inconclusivo. `main.tex` recompilado limpo (3
passadas `pdflatex`); `\cite`/`\bibitem` e `\ref`/`\label` conferidos
por script, sem órfãos em nenhuma direção.

---

## Loop de convergência (2026-08-10): critério de parada explícito

Pedido do diretor científico: rodadas de crítica adversarial repetidas,
contexto fresco a cada rodada (subagente `Agent` síncrono, nunca
`SendMessage`), até 3 rodadas CONSECUTIVAS limpas (0 crítico, 0 maior, 0
moderado, <3 menor; sem crédito parcial, qualquer achado abaixo do
padrão zera a contagem). Ponto de partida: as 25 entradas C-001 a C-025
acima, todas já `fixed`; compilação limpa confirmada antes da primeira
rodada (3 passadas `pdflatex`, sem "undefined reference" nem "undefined
citation", 34 `\cite`/34 `\bibitem`).

### Rodada 1 (subagente `general-purpose`, síncrono): NÃO limpa

Leu `main.tex` completo (2669 linhas), `CRITIQUE.md` completo, e cruzou
números/enunciados contra os companions 04, 05, 06 e o repositório
`collatz-endogeny` local. Recalculou manualmente as constantes de
`thm:wcc-large-deviation` (confirmadas) e verificou por amostragem que
C-001 a C-025 se sustentam (sete "band-widths", $\beta_{\mathrm{eff}}$,
"2.3e-13", cadeia $(\star1)$-$(\star5)$, valores de transição
$\alpha^*$: todos batem contra os companions).

Achados: 0 crítico, 1 maior (C-026), 1 moderado (C-027), 1 menor
(C-028, agregando 7 ocorrências da mesma construção sintática). Ver a
tabela de status para o resumo de cada um; detalhe:

**C-026 (maior).** `thm:wirsching-conj1` (linha 1251, sem
`\begin{proof}`) é atribuído ao próprio paper no abstract ("We prove
Wirsching's first 2003 conjecture"), em §1.2 ("also proves Wirsching's
first 2003 conjecture") e em O3 da Conclusão ("Conjecture~1 is proved
in Theorem~\ref{thm:wirsching-conj1}"), mas a Data Availability
(linhas ~2394-2404) já dizia corretamente que a prova está no
companion. Verificado independentemente contra `papers/05-wirsching-2003-conjecturas/main.tex`
(linhas 189-224): a prova completa está lá. É a mesma classe de defeito
que C-001 já corrigiu para a equação de pressão, recorrendo aqui sem
correção (o produtor da sessão de redação final tinha corrigido a
equação de pressão mas não notou o mesmo padrão aplicado a
`thm:wirsching-conj1`).

**C-027 (moderado).** `K(\ell)` (Wirsching, cobertura sub-exponencial,
`conj:wcc` linha ~727) e `K_\ell`/`K_{q,\ell}` (collision mass,
definida linha ~1466 e usada dezenas de vezes depois) compartilham a
letra sem nenhuma frase de desambiguação, nas duas seções que tratam a
mesma família de conjecturas (WCC/$\beta$=1), onde a confusão é mais
provável.

**C-028 (menor).** A construção "not merely P but Q" / "P, not Q:
it is R" da família de antítese que a Regra 4b orça em duas por
documento inteiro ocorria pelo menos 7 vezes (linhas 240, 875, 1085,
1437, 1551, 1985, 2496). Nota de escopo (Regra 8d): um grep mais amplo
por "X, not Y" simples (sem "merely" nem dois-pontos) revela dezenas de
ocorrências adicionais no documento que este achado específico não
cobriu; não foram tocadas nesta rodada porque o crítico da Rodada 1 não
as sinalizou, e a Regra 8d pede escopo restrito ao que foi de fato
achado. Se uma rodada futura sinalizar isso como achado novo (evidência
nova), será corrigido então.

**Correções aplicadas (produtor, antes da Rodada 2).** C-026: abstract
reescrito ("A companion paper proves Wirsching's first 2003 conjecture
... we test the third"), §1.2 reescrito na mesma direção, O3 reescrito
("A companion paper proves Conjecture~1 (Theorem~\ref{thm:wirsching-conj1},
\cite{WirschingCompanion})"), e a frase de abertura da subseção 9.2
fortalecida para "This subsection restates, without proof, the results
a companion paper \cite{WirschingCompanion} establishes in full",
espelhando o padrão já usado em §3 para a equação de pressão. C-027:
frase de desambiguação inserida no primeiro uso de $K_\ell$ como
collision mass, notando que é "unrelated to Wirsching's covering
function $K(\ell)$" e fixando a convenção de subscrito para o resto do
documento. C-028: 5 das 7 ocorrências reescritas sem a construção
"not merely"/"not X: Y" (linhas 240, 875, 1551, 1985, 2496); as 2
ocorrências mais informativas, onde a confusão do leitor é mais real
dado o histórico do próprio projeto (linha 1085, "proved, not merely
checked", ecoando diretamente o achado C-003 sobre a mesma passagem; e
linha 1439, "is not thereby cancelled: it survives", central ao
argumento de `lem:cov-spectral`), foram mantidas dentro do orçamento de
duas. `main.tex` recompilado limpo (3 passadas `pdflatex`), sem
referência nem citação indefinida.

### Rodada 2 (subagente `general-purpose`, síncrono, contexto fresco): NÃO limpa

Leu `main.tex` completo (2675 linhas), `CRITIQUE.md` completo (incluindo
a seção da Rodada 1), e cruzou números/enunciados contra os companions
04, 05, 06. Recalculou numericamente (Python) as constantes de
`thm:wcc-large-deviation`, os três valores $\alpha^\ast(5,7,9)$ e os
dois bounds $\beta_{\mathrm{eff}}$: todos batem. Confirmou
independentemente que C-026 e C-027 (Rodada 1) se sustentam sem quebrar
nada ao redor. Investigou por conta própria, como pedido
explicitamente no prompt, a extensão do achado C-028 além do que a
Rodada 1 tinha escopado.

Achados: 0 crítico, 1 maior (C-029), 0 moderado, 2 menor (C-030, C-031).

**C-029 (maior).** O abstract (linhas 55-63) e §3 (linhas 300-318)
diziam "Its nontrivial root equals $2$ at $q=3$, reproducing the
Growth Exponent Conjecture ... The root is always unfrozen". Mas
`conj:transition-arithmetic` (linha 354-365) já afirma, no próprio
corpo, que a GEC é o caso "exponent $1$ for $q=3$", isto é, o caso
$\alpha_-=1$, não $\alpha_+=2$; e `prop:always-frozen` (linha 326-329)
prova que $\alpha_+$ é **sempre congelada**, exatamente o oposto de
"always unfrozen". A raiz que reproduz a GEC e é sempre descongelada é
$\alpha_-(q)$ (que vale $1$ em $q=3$), não a raiz não-trivial que vale
$2$ ali. Verifiquei a matemática eu mesmo (Regra 8c) antes de aceitar:
reconferi as definições de $\alpha_-<\alpha_+$ (linha 302), a tabela de
valores $\{\alpha_-,\alpha_+\}=\{1,2\}$ em $q=3$ e $\{\alpha^\ast(q),1\}$
em $q\ge5$ (linhas 303-306), e o enunciado de `thm:transition-model`
("Since $\alpha_-(q)$ is always unfrozen, $\log N(x)/\log x\to\alpha_-(q)$"),
que fecha o caso: é $\alpha_-$, não $\alpha_+$, que transfere ao
modelo i.i.d. O item O8 da Conclusão (linhas 2353-2368) já tinha a
atribuição correta ("for $q=3$ this is the Growth Exponent Conjecture
[...]", referenciando `conj:transition-arithmetic`); só o abstract e a
prosa de abertura de §3 tinham o erro, uma inconsistência real de
Regra 8b numa afirmação substantiva (qual raiz corresponde a uma
conjectura histórica citável de 1995), na seção de maior densidade de
leitura do paper.

**C-030 (menor).** Grep amplo por "X, not Y" (sem "merely", sem
dois-pontos) confirmou o que a Rodada 1 já tinha antecipado: pelo
menos 26 ocorrências adicionais no documento inteiro, muitas
genuinamente antitéticas no sentido da Regra 4b, excedendo em muito o
orçamento de duas por documento.

**C-031 (menor).** Três resíduos de narração de processo (Regra 4b
§3): "the entropy implication previously asserted here is invalid"
(§ WCC, o termo "entropy implication" nunca é definido em nenhum outro
ponto do documento, então além de narrar o processo de edição, a frase
é ininterpretável); "a reading that corrects how this project's own
earlier attempt on Conjecture 2 had been framed" (§9.2); "not the one
originally supposed" em O3 da Conclusão.

**Correções aplicadas (produtor, antes da Rodada 3).** C-029: abstract
reescrito para distinguir explicitamente as duas raízes
($\alpha_-(q)=1$ em $q=3$ reproduz a GEC e é sempre descongelada;
$\alpha_+$, sempre congelada, vale $2$ em $q=3$ e bate separadamente
com medições de índice de cauda anteriores); §3 reescrito na mesma
direção, com ponteiro explícito para `conj:transition-arithmetic`.
C-030: todas as ~26 ocorrências adicionais reescritas (a maioria via
"rather than"/"in place of"/restruturação em duas orações), deixando
só as mesmas 2 ocorrências já sancionadas na Rodada 1 (linhas 1090 e
1443 após a renumeração desta rodada) dentro do orçamento. C-031: as
três frases removidas ou reescritas sem narrar o processo de edição,
preservando o conteúdo matemático de cada passagem (que já estava
completo sem elas). `main.tex` recompilado limpo (3 passadas
`pdflatex`), sem referência nem citação indefinida; `\cite`/`\bibitem`
conferidos por script (34/34, sem órfãos reais; um falso positivo do
script de verificação por um `\cite{Foo, Bar}` com espaço após a
vírgula, não um erro no documento).

### Rodada 3 (subagente `general-purpose`, síncrono, contexto fresco): NÃO limpa

Leu `main.tex` completo (2679 linhas) e `CRITIQUE.md` completo
(incluindo Rodadas 1 e 2). Confirmou independentemente que C-029
(α₋/α₊) e C-028/C-030 (orçamento de antítese) se sustentam: revisou as
27 ocorrências de "rather than" uma a uma e não achou nenhuma inversão
de sentido matemático. Achou 4 problemas novos, incluindo o primeiro
achado crítico do loop de convergência.

Achados: 1 crítico (C-032), 1 maior (C-033), 1 moderado (C-034), 1
menor (C-035).

**C-032 (crítico).** `prop:gauge` ("Gauge freedom", linha ~474)
enuncia quatro itens (a)-(d) sobre $X:=W\cdot Y$. O bloco vai direto
de `\end{enumerate}` para `\end{proposition}`: não há
`\begin{proof}`. Os itens (b) ("the same tail index as $W$") e (c)
("the same linear regression slope $b\approx1$... up to a fixed
additional dispersion") são fatos probabilísticos não-triviais sem
prova, sem citação de suporte, e usando notação nunca definida em
lugar nenhum do documento (`M_q(\alpha)` ocorre uma única vez, dentro
do próprio enunciado; "regression slope $b$" nunca é definido em
nenhuma das 4 ocorrências no arquivo inteiro). `rem:barrier-reading`
declara a proposição "fully rigorous and independently verified", e a
pasta do repositório correspondente
(`collatz-endogeny/sec4-endogeny-barrier/`) só verifica
`lem:2adic`, não `prop:gauge`. `thm:barrier`, o único Teorema
não-migrado que é a peça central do título do paper (a "endogeny
barrier"), cita `prop:gauge` como um dos dois ingredientes "fully
rigorous" de que depende.

Consultei o `advisor()` antes de agir (Regra 11b: julgamento
matemático real, "provar ou enfraquecer"). Resposta: provar, não
enfraquecer, porque as provas de (b) e (c) são curtas e o material já
existe no histórico do projeto. Verifiquei essa afirmação
independentemente (Regra 8c) lendo
`hypotheses/H-111-fifth-round-external-ai-Rhin-Tao-Breiman-control-experiment.md`
diretamente: confirma exatamente o esqueleto de prova sugerido
(sanduíche $c\cdot W\le WY\le C\cdot W$ para $0<c\le Y\le C$, que
herda o índice de cauda sem hipótese de independência; o Lema de
Breiman para o assintótico exato quando $Y\perp W$; e o caveat de que
só o **expoente** fica blindado, a **constante** de cauda não). Também
confirmei via `ls` no repositório que `sec4-endogeny-barrier/` de fato
só tem `lemma_no_2adic_memory.py`.

Verifiquei a referência bibliográfica de Breiman (Regra 11, via
`WebSearch`) antes de citar: L. Breiman, "On some limit theorems
similar to the arc-sin law", Theory of Probability \& Its Applications
\textbf{10}(2) (1965), 323-331, confirmado contra o índice do
periódico (mathnet.ru) e o abstract SIAM/epubs.

**C-033 (maior).** Abstract ("we test the third to certified numerical
error") e §1.2 atribuíam `thm:conjecture3` a este paper, mas a Data
Availability já classificava esse mesmo rótulo como "restated" do
companion 05, que tem a mesma fórmula e o mesmo número
($0.580\pm0.001$) com mais detalhe técnico (conferido diretamente
contra `papers/05-wirsching-2003-conjecturas/main.tex`, linhas
766-784). Mesmo padrão de C-026 (Conjectura 1), que a correção daquele
achado não tinha capturado para a Conjectura 3.

**C-034 (moderado).** A subseção "Certified numerical test of
Wirsching's Conjecture 3" (linha ~1294) continha, sem nova quebra de
subseção, ~110 linhas de material sem relação com o título: a
decomposição microcanônica (`thm:microcanonical`), a ponte de limite
local condicional (`prop:complex-deconditioning`), e a tetracotomia de
equivalência de ensembles (quatro teoremas mais três Resultados
Empíricos). Resíduo estrutural provável do processo de condensação da
divisão em quatro papers.

**C-035 (menor).** "precise/precisely" usado fora de sentido técnico
em 3 lugares (linhas ~142, ~354, ~1803 antes da correção), banido pela
Regra 4b §1.

**Correções aplicadas (produtor, antes da Rodada 4).** C-032:
`prop:gauge` reforçada com a hipótese $Y:\mathcal{Y}\to[c,C]$,
$0<c\le C<\infty$ (em vez de "bounded, non-constant... $\to(0,\infty)$",
que não garantia limitação inferior, ingrediente do sanduíche);
adicionado `\begin{proof}` provando os quatro itens (a via a equação
de pressão ser propriedade dos pesos da recursão, não da solução
particular; b via sanduíche + Lema de Breiman \cite{Breiman1965},
citação nova verificada e adicionada à bibliografia; c via
decomposição de covariância, definindo "regression slope" como
coeficiente de regressão populacional $b=\Cov(\log X,Z)/\Var(Z)$
contra qualquer estatística $Z$ mensurável em relação aos dígitos; d
como já estava, tornado explícito); item (a) perdeu a menção a
"identical operator $M_q(\alpha)$" (notação órfã, nunca definida).
`rem:barrier-reading` reescrita para não afirmar "independently
verified" para `prop:gauge` (só `lem:2adic` tem checagem numérica
contra o repositório); a Data Availability Statement reescrita para
não implicar que `prop:gauge` está verificada em script (agora diz
"proved in the text", com a lista específica de itens
script-verificados mantida como estava, sem `prop:gauge` nela, o que
já era o caso). Abstract, §1.2, e o item O1 da Conclusão conferidos
contra a nova hipótese e redação (Regra 8b): consistentes. C-033:
abstract e §1.2 reescritos para atribuir "tests the third" ao
companion, no mesmo padrão de "proves... treats... and tests" já
usado para as Conjecturas 1 e 2; a abertura da subseção 9.3 ganhou uma
frase equivalente à de 9.2 ("restates, without independent
verification of its own, a companion paper's certified numerical
test"). C-034: nova `\subsection{Microcanonical decomposition and
equivalence of ensembles}` inserida antes do bloco que não pertencia
ao título antigo. C-035: as 3 ocorrências reescritas (cortadas ou
trocadas por "exact"). `main.tex` recompilado limpo (3 passadas
`pdflatex`); `\cite`/`\bibitem` reconferidos (35/35, `Breiman1965`
incluído, sem órfãos reais); "genuine/genuinely" e em dash
reconfirmados em zero; orçamento de antítese "X, not Y" reconfirmado
em exatamente 2 ocorrências.

**Segunda opinião (Codex, `codex exec -s read-only`, modelo
independente) sobre a prova de `prop:gauge`, antes do commit desta
rodada.** Confirmou os quatro itens em substância, com três ressalvas
reais incorporadas à versão final: (a) precisa da recursão ser
homogênea (linear sem termo aditivo), o que já é o caso de
\eqref{eq:G-recursion}, tornado explícito na prova; (b) precisa que a
cauda relevante de $W$ seja de fato regularmente variante (hipótese
condicional já implícita, agora declarada) e que $W\ge0$ (verdadeiro
por \eqref{eq:G-recursion} ter pesos não-negativos, agora citado); (c)
faltavam condições padrão de regularidade ($W>0$, integrabilidade
quadrática de $\log W$ e $Z$, $0<\Var(Z)<\infty$), adicionadas ao
preâmbulo da proposição; (d) a redação antiga, "$\to\Var[\log Y]$ for
every $m$", era logicamente incoerente (convergência não se aplica
"para todo $m$"; Codex marcou este item como incorreto como escrito).
Reescrito com a decomposição correta,
$\Var[\log X\mid\mathcal F_m]=\Var[\log W\mid\mathcal F_m]+\Var[\log
Y]$ para todo $m$ finito, convergindo a $\Var[\log Y]$ quando
$m\to\infty$ porque $W$ é $\mathcal F_\infty$-mensurável por
definição (é a solução "aritmética"), o que também torna mais preciso
por que a barreira existe: para $m$ finito a dispersão extra de $Y$
soma-se à variância residual própria de $W$; só no limite sobra
exclusivamente $\Var[\log Y]$. `main.tex` recompilado limpo depois
desta segunda passada de correção; bibliografia e orçamento de
antítese reconfirmados (nenhuma mudança nesses números).
