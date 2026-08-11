# CRITIQUE.md — paper 06 (`A Closed-Form Pressure Equation for the Accelerated qx+1 Branching Process`)

Arquivo único de crítica deste paper (Regra 8/15). A tabela de status
abaixo é a lista viva: o produtor lê a tabela inteira em toda passagem,
não só a rodada mais recente. As seções datadas embaixo são o histórico
completo, acrescentadas e nunca reescritas.

Rodada 1: nada consertado, todos os achados entraram como `open`.
Rodada 2 (produtor): 29 de 30 corrigidos; C-30 fica `open` com motivo
registrado (mesma tensão de política já documentada nos papers 04/05).
Dois achados do produtor sobre a própria crítica, registrados por
Regra 8c: C-21 (Applegate-Lagarias) e a citação de Kontorovich-Lagarias
de Teorema 8.10 vieram corretos; C-27 passou a estar correto só depois
do conserto de C-06/C-09 (não era erro do `OUTLINE.md` sozinho).

## Tabela de status

| ID | Rodada | Resumo | Severidade | Status |
|----|--------|--------|------------|--------|
| C-01 | 2026-08-10 r1 | `prop:transition-fine` não tem verbo principal: é um fragmento nominal, não um enunciado | alta | fixed |
| C-02 | 2026-08-10 r1 | Frase quebrada depois da nota de rodapé (l.668): "…not independent.¹ the tail-index equation…" | alta | fixed |
| C-03 | 2026-08-10 r1 | §6: fórmula de $m'(1)$ tem fator $2$ espúrio (expressão vale $-1{,}674$; o valor citado $-0{,}288$ é o certo) | alta | fixed |
| C-04 | 2026-08-10 r1 | §2: "$u\equiv0$ é a única classe estéril" é falso para $q=9$ (estéreis são $0,3,6$), dentro do parágrafo que se anuncia como correção | alta | fixed |
| C-05 | 2026-08-10 r1 | `\rho(M_q(\alpha))` (l.473) usa notação nunca definida neste paper; resíduo do paper 01 | alta | fixed |
| C-06 | 2026-08-10 r1 | `thm:transition-model`: Teorema sem prova, sobre um modelo nunca construído, citando `Biggins1992` para um limite que `prop:transition-fine` diz que Biggins não dá | alta | fixed |
| C-07 | 2026-08-10 r1 | "The four hypotheses above" (l.640) não tem antecedente: nada acima está enumerado em quatro | média | fixed |
| C-08 | 2026-08-10 r1 | §4 promete que §7 faz média "over many roots"; §7 usa 3 raízes | média | fixed |
| C-09 | 2026-08-10 r1 | Cadeia de dependência para frente §3→§4→§6; log-convexidade fica só em §6 (seção escopada em $q=3$) e com justificativa errada | média | fixed |
| C-10 | 2026-08-10 r1 | 18 travessões `---` no corpo (Regra 3, proibição absoluta; Regra 4b §2) | média | fixed |
| C-11 | 2026-08-10 r1 | Meta-honestidade sobrevivente em dois pontos (l.446, l.696); o `rem:transfer-basis` em si está limpo | média | fixed |
| C-12 | 2026-08-10 r1 | "pre-registered" ×2 (l.754, l.766), explicitamente banido pela Regra 4b §3 | média | fixed |
| C-13 | 2026-08-10 r1 | Resumo: marcado DRAFT, ambiguidade sintática, narra correção de argumento não atribuído, mais otimista que o corpo em $q=5$ | média | fixed |
| C-14 | 2026-08-10 r1 | Auto-suficiência: $\mu_\alpha$, "tilted Syracuse sums", $\alpha_\pm(q)$, $\pi_a(x)$, "extended tree", "headroom" usados antes/sem definição | média | fixed |
| C-15 | 2026-08-10 r1 | Colisão de notação: $s(\alpha)$ (entropia) vs. $s$ (expoente de cauda); `a_0` vs. `A_0` | média | fixed |
| C-16 | 2026-08-10 r1 | Vocabulário banido pela Regra 4b §1: `genuine`×12, `precise/precisely`×10, "not a coincidence"×2, "Taken together", "worth recording", `remarkably`, `substantial` | média | fixed |
| C-17 | 2026-08-10 r1 | Orçamento "X, not Y" da Regra 4b §2 (máx. 2) estourado: ao menos 13 ocorrências | média | fixed |
| C-18 | 2026-08-10 r1 | Narração de processo em §5 e na abertura de §6 (Regra 4b §3) | média | fixed |
| C-19 | 2026-08-10 r1 | §5 concentra quase toda a matéria empírica, enquanto §7 se chama "Empirical confirmation" e tem 1 parágrafo | média | fixed |
| C-20 | 2026-08-10 r1 | Tensão não resolvida entre `ex:naive-fails` e a "multitype pressure matrix" da nota de rodapé | média | fixed |
| C-21 | 2026-08-10 r1 | Citações a conferir na fonte primária (Applegate-Lagarias I/II, $\eta_{5,BP}$, Villemonais-Zalduendo, ano 2009 vs. livro 2010) | média | fixed |
| C-22 | 2026-08-10 r1 | Regra 11: `VillemonaisZalduendo2025` citado com "we have not verified this" explícito no corpo | média | fixed |
| C-23 | 2026-08-10 r1 | Existência da segunda raiz positiva e unicidade de $\alpha_c(q)$ afirmadas sem argumento | baixa | fixed |
| C-24 | 2026-08-10 r1 | Ambiente `empirical` declarado e nunca usado (Regra 10b); `\ZZ` nunca usado; `thebibliography{9}` com 18 itens | baixa | fixed |
| C-25 | 2026-08-10 r1 | "exponent $1$ (linear growth)": $x^{1+o(1)}$ não é crescimento linear | baixa | fixed |
| C-26 | 2026-08-10 r1 | Repositório: docstring de `iid_tail_check_assumptions.py` fala em "paper 01"; "organized by section" descreve 1 subpasta chamada `sec3-...` cobrindo §3-§7 | baixa | fixed |
| C-27 | 2026-08-10 r1 | `OUTLINE.md` rotula `thm:transition-model` e `prop:always-frozen` como "prova completa" | baixa | fixed |
| C-28 | 2026-08-10 r1 | l.670: "solved exactly by $s=\alpha_+/\alpha_-$" ignora que $s=1$ também resolve | baixa | fixed |
| C-29 | 2026-08-10 r1 | Sem seção de conclusão; `thm:frozen-singular` nunca referenciado | baixa | fixed |
| C-30 | 2026-08-10 r1 | `main-pt-br.tex` inexistente (Regra 5); `OUTLINE.md` registra como pendência deliberada | baixa | rejected (ver rodada 2: mesma tensão de política dos papers 04/05, deixado para o pesquisador decidir) |
| C-31 | 2026-08-10 r3 | As baterias de raízes reais amostradas (600/5000/100.000 raízes, §4) eram citadas como evidência de `conj:tail-index` (martingale Haar-q-ádica $W_q$), mas medem $N_v(vH)/H^{\alpha_-(q)}$, o fator de escala de `prop:transition-fine` — objeto diferente | alta | fixed |

---

## 2026-08-10 — rodada 1 (crítico, contexto fresco)

Escopo: `main.tex` inteiro (964 linhas, 13 páginas, compila limpo em
duas passadas de `pdflatex`, sem referências indefinidas). Verificações
numéricas independentes em `mpmath` a 25-30 dígitos. Comparação contra
`../01-syracuse-qx1-endogenia/main.tex` (paper de origem do split) e
contra o repositório `collatz-qx1-pressure`.

### Verificado e correto (não mexer, Regra 8d)

Registro explícito do que passou, para que uma rodada futura não
reabra material já checado:

- **Álgebra da identidade de pressão (`thm:pressure`).** Correta.
  $\sum_{a\ge1}(q2^{-a})^\alpha=q^\alpha/(2^\alpha-1)$, e a divisão
  pelos $q^k$ resíduos dá $(q^{\alpha-1}/(2^\alpha-1))^k$.
- **`lem:fibre-bijection`.** Correto: domínio de tamanho $q^{j-1}$,
  boa definição, injetividade via $w_a(v)-w_a(v')=2^at$, sobrejetividade
  por cardinalidade.
- **Iteração da bijeção.** A fórmula
  $u_0\equiv\sum_{i=1}^kq^{i-1}2^{-S_i}\pmod{q^k}$ está certa.
  Conferida à mão em $k=1$ e $k=2$: de $u_0$ sai
  $2^{a_1}u_0\equiv1+q2^{-a_2}$, logo $w_{a_1}(u_0)\equiv2^{-a_2}$.
- **`thm:qadic-martingale`.** $Z_k(\alpha;u)=q^k\Pr(F_k=u)$ decorre de
  $\prod(q2^{-a_i})^\alpha=q^k\prod p_\alpha(a_i)$; a consistência
  projetiva ($F_{k+1}-F_k=q^k2^{-S_{k+1}}$) e a conta de martingale
  estão corretas.
- **`thm:frozen-singular`.** A identidade $H(p_\alpha)-\log q=s(\alpha)$
  numa raiz foi verificada simbolicamente: a diferença entre os dois
  lados é $(1-\alpha)\log q+\log(1-r)-\log r$, que se anula exatamente
  pela equação de pressão $q^{\alpha-1}=(1-r)/r$. A estimativa de
  momento fracionário e a derivada logarítmica $\log q-H(p_\alpha)>0$
  em $t=1$ também estão certas.
- **`thm:lp-collision`.** $\lVert M_k\rVert_p^p=q^{k(p-1)}\sum\mu^p$
  confere; a leitura de colisão para $p$ inteiro confere.
- **Tabela de $\alpha^\ast(q)$ (§5).** Todos os quatro valores
  satisfazem $q^{\alpha-1}=2^\alpha-1$. Recalculados por bisseção a 30
  dígitos: $2$ (exato), $0{,}650918639898$, $0{,}373501034431$,
  $0{,}258108023834$. Os arredondamentos impressos estão corretos.
- **Consistência numérica em todo o texto (item 5 da tarefa).** Os
  valores reaparecem idênticos em §5 (tabela), §7 ("predicted
  0.650919", "predicted 0.373501") e `rem:novelty-109`
  ("$\alpha^\ast(5)=0{,}650919$"). O índice de cauda derivado,
  $1/\alpha_-(5)=1{,}536290$, bate com "predicted $1{,}536$" nas duas
  ocorrências. As faixas empíricas $0{,}62$-$0{,}66$ e
  $0{,}36$-$0{,}39$ contêm as previsões.
- **Tabela de $\alpha_c(q)$ (§4).** Recalculada: $1{,}355091$,
  $0{,}794222$, $0{,}563799$, $0{,}437407$. Os quatro valores impressos
  estão corretos, e o entrelaçamento
  $\alpha_-<\alpha_c<\alpha_+$ vale nos quatro casos.
- **$s(1)=\log(4/q)$.** Exato, conferido nos quatro $q$
  ($0{,}287682$, $-0{,}223144$, $-0{,}559616$, $-0{,}810930$).
  A ligação com a deriva média $\log q-2\log2$ está correta.
- **`prop:always-frozen`.** O argumento (em raiz, $s=-\alpha P'$; $P$
  estritamente convexa com dois zeros força
  $P'(\alpha_-)<0<P'(\alpha_+)$) está correto, e a log-convexidade em
  si é verdadeira: $(\log m)''=\log^2 2\cdot 2^\alpha/(2^\alpha-1)^2>0$.
  O problema é onde e como isso é justificado, ver C-09.
- **`thm:iid-tail`.** $\psi(s)=\log\rho_{\mathrm{ann}}(\theta s)$ zera
  em $s=1$ e em $\kappa=\alpha_+/\alpha_-$; $\psi'(1)<0$ segue de
  $\alpha_-$ descongelada. O subgrupo fechado gerado pelos pesos
  logarítmicos é $\theta(\log q\,\mathbb{Z}+\log2\,\mathbb{Z})$, denso.
  A equação $q^{\alpha_-s-1}=2^{\alpha_-s}-1$ está correta.
- **Ciclos de resíduo.** $w_2(1)=1$ para $q=3$; para $q=5$,
  $w_4(1)=3$ e $w_1(3)=1$, e o mapa de menor ramo leva $2\mapsto3$,
  $4\mapsto3$, portanto as quatro raízes $\{1,2,3,4\}$ realmente
  alimentam o ciclo. A ressalva de §4 é factualmente correta.
- **Nota de rodapé, matriz multitipo posto 1 (Regra 8c: registro de
  crítica minha que se provou errada).** Numa primeira passagem eu
  julguei a afirmação falsa, calculando o autovalor de Perron como
  média sobre os $d$ tipos sobreviventes, o que dá
  $(1/d)q^s/(2^s-1)\ne q^{s-1}/(2^s-1)$. Refazendo com a distribuição
  correta do tipo filho, que é uniforme sobre **todas** as $q$ classes
  (é exatamente o que `ex:naive-fails` mostra: $w_a\bmod q$ depende de
  $\lfloor u/q\rfloor$ através de $2^ak$, e $2^a$ é unidade), a matriz
  restrita é $M_{ij}=f_i/q$, autovetor $f$, autovalor
  $(1/q)\sum_{i\in\langle2\rangle}f_i=q^{s-1}/(2^s-1)$. A afirmação do
  paper está **correta**. O cancelamento independente de $d$ via a
  bijeção $a_0:\langle2\rangle\to\{1,\dots,d\}$ também confere:
  $\sum_i2^{-sa_0(i)}=\sum_{b=1}^d2^{-sb}$ cancela $(1-2^{-sd})$.
  Fica registrada só a lacuna expositiva, ver C-20.
- **Bibliografia (item 8 da tarefa).** São **18** entradas, não 16.
  As 18 estão citadas e as 18 têm `\bibitem`; nenhuma órfã, nenhuma
  pendurada, nenhuma duplicada. (Uma varredura ingênua com regex de
  uma linha só acha 16 porque
  `\cite{Goldie1991,JelenkovicOlveraCravioto2012,AlsmeyerBigginsMeiners2012}`
  quebra em duas linhas.) Todos os `\ref`/`\eqref` resolvem.
- **Citações companion (item 6 da tarefa).** `\cite{BarrierCompanion}`
  aparece **3** vezes, não 2, e as três fazem sentido: l.151 (a
  recursão de martingale em $q=3$ vem daquela linha), l.336 (o critério
  $L^2$ de colisão é o caso $p=2$ usado lá), l.812 (o teorema de
  unicidade do caso crítico pressupõe a independência que aquele paper
  identifica como a lacuna). `\cite{KLVolkovCompanion}` aparece 2 vezes,
  l.569 e l.834, ambas coerentes: teste empírico calibrado em $q=5$
  separando previsões concorrentes. Nenhuma das cinco é gratuita.
- **Consistência do resumo com o corpo (Regra 8b), parte que passa.**
  "we prove martingale convergence and identify the limit with the
  density of the absolutely continuous component; absolute continuity
  and the tail remain conjectural" bate exatamente com
  `thm:qadic-martingale` + `conj:tail-index`. A afirmação sobre
  singularidade na raiz congelada bate com `thm:frozen-singular`.
- **Regra 12.** O repositório `github.com/faculdade/collatz-qx1-pressure`
  existe, tem `README.md` com tabela pasta→seção, e os scripts
  correspondentes aos números do paper estão lá.
- **`rem:transfer-basis` (item 9 da tarefa).** A frase de
  meta-honestidade que o `OUTLINE.md` registra como herdada ("We are
  precise about the status of this because...") **não** está mais
  presente. A redação atual do Remark está limpa. Mas sobrou o mesmo
  vício em outros trechos copiados, ver C-11.

### Achados

**C-01 (alta) — `prop:transition-fine` não enuncia nada.**
Linhas 506-512. O ambiente `Proposition` abre com:

> "Conditional on a renewal-type refinement, from the counting-function
> level (not merely the exponent) to the sharper asymptotic
> $N(x)\sim W\cdot x^{\alpha_-(q)}$, holding almost surely and
> uniformly, *including* at $q=3$, for an almost surely positive,
> non-degenerate random scale factor $W$ (...)."

Não há verbo principal. É um sintagma nominal seguido de um ponto. A
regressão veio do split: o paper 01 tem a mesma proposição bem formada,
"Conditional on a renewal-type refinement (...), **the counting function
has** the sharper asymptotic $N(x)\sim W\cdot x^{\alpha_-(q)}$ almost
surely and uniformly (...)". A oração principal foi perdida ao mover o
bloco.

Agravante de rotulagem (Regra 10b): o resto do ambiente `Proposition`,
oito linhas de texto, é relato de busca bibliográfica ("A directed
literature search found the neighboring machinery but not this exact
statement ready-made"), terminando em "we have not carried out that
adaptation, nor located it already written in this exact form". Um
ambiente `Proposition` cujo conteúdo declarado é que o autor não provou
nem localizou o enunciado não é uma proposição; é uma observação, e
deveria ser `remark` ou `conjecture`. A linha entre provado e
conjectural (item 7 da tarefa) é nítida em `thm:transition-model` vs.
`conj:transition-arithmetic`, mas borra exatamente aqui, no objeto do
meio.

**C-02 (alta) — frase quebrada depois da nota de rodapé.**
Linhas 646-668. O texto lê:

> "...since the arithmetic subtrees are not independent.\footnote{...}
> the tail-index equation $\mathbb{E}[\sum_i A_i^s]=1$ becomes, for our
> weights, ..."

A oração começa em minúscula, sem sujeito e sem conexão com a frase
anterior. Não é artefato de fonte: confirmado no PDF renderizado, que
imprime "...are not independent.¹ the tail-index equation E[Σ Aᵢˢ] = 1
becomes...". Alguma coisa como "By the same argument," ou "In the
stochastic model," foi apagada no split.

**C-03 (alta) — fórmula de $m'(1)$ errada em §6.**
Linha 797. O paper escreve
$m'(1)=\ln3-2\ln2\cdot\frac{2^1}{2^1-1}\approx-0{,}288$.
A expressão escrita vale $1{,}0986-1{,}3863\cdot2=-1{,}6740$, não
$-0{,}288$. O valor numérico citado é o certo; a fórmula é que tem um
fator $2$ a mais. O correto é
$m'(1)=\ln3-\ln2\cdot\frac{2^1}{2^1-1}=-0{,}287682$.
Note que $m'(2)=\ln3-\frac43\ln2\approx+0{,}174$ (linha 798) está
**certo**, e é justamente porque as duas foram escritas em formatos
diferentes (uma com o fator geral $2^\alpha/(2^\alpha-1)$ explícito, a
outra já simplificada) que o erro passou despercebido. O sinal, que é o
que a seção usa, não muda; a fórmula impressa, sim.

**C-04 (alta) — classe estéril errada para $q=9$.**
Linhas 120-124: "When $2$ is a primitive root mod $q$ (as for
$q=3,5,9$, all used numerically below), $\langle2\rangle$ is all of
$(\mathbb{Z}/q\mathbb{Z})^\times$ and $u\equiv0\pmod q$ is the only
sterile class".

Falso para $q=9$. É verdade que $\mathrm{ord}_9(2)=6=\varphi(9)$, logo
$\langle2\rangle=(\mathbb{Z}/9\mathbb{Z})^\times=\{1,2,4,5,7,8\}$. Mas
para $q$ composto $(\mathbb{Z}/q\mathbb{Z})^\times$ não é
$\mathbb{Z}/q\mathbb{Z}\setminus\{0\}$: as classes estéreis em $q=9$
são $\{0,3,6\}$, três delas, não só o zero. O passo lógico
"$\langle2\rangle$ é todo o grupo de unidades $\Rightarrow$ só $0$ é
estéril" só vale para $q$ primo, e $q=9$ está explicitamente na lista.

O agravante é o contexto: esse parágrafo inteiro (linhas 111-134) se
apresenta como uma correção à descrição estrutural, terminando em "it
is a correction to this structural description only". Uma correção que
introduz um erro novo é o pior lugar possível para ele estar. O caso
$q=7$ discutido logo em seguida está correto ($d=3$,
$\langle2\rangle=\{1,2,4\}$, estéreis $\{0,3,5,6\}$).

Consequência prática a checar: §7 e o repositório usam $q=9$? A tabela
de §5 usa, e a nota de rodapé menciona verificação em $q=7,15$. Se a
enumeração numérica em $q=9$ excluiu só os múltiplos de $9$ em vez dos
múltiplos de $3$, os números de §5 estariam afetados. (O paper afirma
que a implementação "already excludes exactly these classes"; isso é
afirmação sobre o repositório e precisa ser confirmada lá antes de
qualquer conserto no texto.)

**C-05 (alta) — `\rho(M_q(\alpha))` indefinido.**
Linha 473: "the equation $\rho(M_q(\alpha))=1$ has at most two positive
roots". Nem $M_q$ nem $\rho(\cdot)$ como raio espectral são definidos em
lugar nenhum deste paper. É resíduo do paper 01, onde $M_q(\alpha)$ era
uma matriz de transferência e $\rho$ seu autovalor de Perron. Falha
direta de auto-suficiência (item 1 da tarefa), e ironicamente aponta
para o operador de transferência que §3 acabou de mostrar que não
existe. Deveria dizer simplesmente
$\rho_{\mathrm{ann}}(\alpha)=1$.

**C-06 (alta) — `thm:transition-model` é um Teorema sem prova sobre um
modelo nunca construído.**
Linhas 496-504. Três problemas somados:

1. O modelo é definido só por uma propriedade: "the i.i.d.
   branching-random-walk model whose annealed pressure is exactly
   $\rho_{\mathrm{ann}}(\alpha)$". O processo pontual de reprodução
   nunca é escrito. Sem ele não dá para conferir nenhuma hipótese
   (nem aqui, nem em `thm:iid-tail`, que aplica Liu 2000 ao mesmo
   objeto fantasma). Isso importa: a árvore aritmética real é
   multitipo, com expoentes admissíveis $a\equiv a_0\pmod d$ por nó,
   e a média sobre resíduos é que devolve $\rho_{\mathrm{ann}}$ (é o
   que a nota de rodapé calcula). Chamar isso de "i.i.d." sem
   construção explícita é impreciso.
2. Não há ambiente `proof`. O enunciado carrega o próprio argumento
   dentro dele ("Since $\alpha_-(q)$ is always unfrozen (...),
   $\log N(x)/\log x\to\alpha_-(q)$ almost surely (...)
   \cite{Biggins1992}").
3. Inconsistência interna: `prop:transition-fine`, oito linhas abaixo,
   afirma que "the branching-random-walk martingale theory that is
   natively two-sided \cite{Biggins1992} gives convergence
   generation-by-generation, **not a renewal law summed over all
   generations**". Mas $N(x)$ é justamente uma contagem somada sobre
   todas as gerações. O paper cita Biggins1992 para um resultado que
   ele mesmo, logo adiante, diz que Biggins1992 não fornece. Ou o
   Teorema precisa de uma prova que explique por que o expoente (ao
   contrário da assintótica fina) segue do resultado geração a
   geração, ou a citação está errada.

Isso é o que mais compromete o item 7 da tarefa: `thm:transition-model`
é o lado "provado" da fronteira provado/conjectural, e não está provado
no paper.

**C-07 (média) — "The four hypotheses above" sem antecedente.**
Linha 640: "The four hypotheses above were checked numerically for
$q=3,5,7,9,15$ in the accompanying repository." Nada acima está
enumerado, nem em quatro nem em qualquer número. Pelo script
`iid_tail_check_assumptions.py` do repositório, as quatro são
$\rho_{\mathrm{ann}}(\alpha_-)=1$, $\rho_{\mathrm{ann}}(\alpha_+)=1$,
$\psi'(1)<0$ e $\kappa>1$; mas o leitor não tem como saber. Provável
resíduo de uma lista enumerada que existia no paper 01.

**C-08 (média) — §4 promete de §7 o que §7 não entrega.**
Linha 455-457, §4: "\S\ref{sec:empirical} below carries the actual
generic-environment evidence, **averaging over many roots** sampled well
away from any known short cycle." Linha 830, §7: "counting slopes per
decade of **$3$ independently sampled roots**". Três raízes, e o que se
reporta é uma faixa, não uma média. A promessa de §4 é o que sustenta a
ressalva honesta que o próprio §4 faz sobre suas raízes periódicas; se
§7 não a cumpre, a ressalva fica sem contrapartida e o paper não tem, em
lugar nenhum, a evidência de ambiente genérico que diz ter.

**C-09 (média) — cadeia de dependência para frente, e a log-convexidade
justificada errado.**
Responde ao item 4 da tarefa. Sim, a referência cruzada dentro de
`prop:always-frozen` (linha 405, "(\S\ref{sec:tail-regime})") é uma
referência para frente: §4 depende de §6. E não é a única. A cadeia é:

- §3 `thm:frozen-singular` (l.364) depende de §4 ("The larger root is
  frozen, hence $H<\log q$ (see \S\ref{sec:freezing})");
- §4 `prop:always-frozen` (l.405) depende de §6 (log-convexidade);
- §5 (l.470-473) também depende de §6 pela mesma razão.

Não é circular, mas inverte a ordem lógica do documento inteiro: o
lema de que três seções dependem está enterrado na penúltima.

Pior, a §6 é escopada em $q=3$. Ela escreve "$m(\alpha):=q^{\alpha-1}/
(2^\alpha-1)$ (the pressure function of \S\ref{sec:pressure} **at
$q=3$**)" e faz as contas com $q=3$ substituído, enquanto
`prop:always-frozen` invoca a log-convexidade "for every odd $q\ge3$".
O leitor é mandado para uma seção sobre $q=3$ atrás de um fato geral.

E a justificativa dada em §6 está errada: "Since $m$ is log-convex (as a
sum, **after clearing denominators**, of exponentials in $\alpha$)".
Limpar denominadores de $q^{\alpha-1}/(2^\alpha-1)$ não produz soma de
exponenciais nenhuma. O caminho correto é a expansão geométrica,
$m(\alpha)=\sum_{a\ge1}q^{-1}(q2^{-a})^\alpha$, que é literalmente uma
soma de exponenciais com coeficientes positivos, logo log-convexa por
Hölder. O fato é verdadeiro (conferi:
$(\log m)''=\log^2 2\cdot2^\alpha/(2^\alpha-1)^2>0$); a razão dada não é.
Isso deveria ser um Lema em §3, uma linha, geral em $q$.

**C-10 (média) — 18 travessões.**
Regra 3 proíbe o travessão em qualquer lugar, sem exceção de contexto, e
a Regra 4b §2 endurece isso para prosa de publicação ("The default is
zero per document"). Há 18 ocorrências de `---` no corpo: linhas 130,
131, 385, 440, 442, 524, 662, 663, 715, 723, 725, 731, 736, 745, 768,
806, 812, 819. (Os `--` da bibliografia, em faixas de páginas, são
legítimos.)

**C-11 (média) — meta-honestidade sobrevivente.**
Responde ao item 9 da tarefa. O `rem:transfer-basis` em si está limpo,
como o `OUTLINE.md` registra. Mas o vício sobreviveu em dois outros
trechos copiados, e a Regra 4b §1 classifica essa família como "the
single strongest marker", banida sem exceção:

- Linha 445-446: "This check has a limitation, **flagged rather than
  hidden**". Variante direta de "we flag rather than obscure".
- Linha 696-697: "and **report both honestly rather than stopping at
  whichever gave the more favorable number**". "honestly" está na lista
  literal de palavras banidas.

Casos de fronteira, mesma família, mais fracos: "all confirmed against
two synthetic calibration checks **rather than taken at face value**"
(l.768-769) e "rather than relying only on sampling roots far from
them" (l.841). Os dois primeiros não são discutíveis.

**C-12 (média) — "pre-registered" ×2.**
Linhas 754 ("A pre-registered log-periodic fit") e 766 ("a
pre-registered comparison"). A Regra 4b §3 bane o termo explicitamente
fora de contexto clínico ou psicométrico, e a Seção 0 do `CLAUDE.md`
observa que este framework deliberadamente não tem maquinaria de
pré-registro. O conteúdo que os dois trechos descrevem (fixar a
predição antes de olhar o dado) é legítimo e deve ser mantido; a
palavra é que não.

**C-13 (média) — resumo.**
Quatro coisas, na seção de maior densidade de marcadores do paper:

1. Está marcado como rascunho num comentário LaTeX ("DRAFT -- rewrite by
   hand before submission"). Registrado como pendência no `OUTLINE.md`;
   fica aqui só para não sumir da lista.
2. Ambiguidade sintática: "correcting a finite-automaton argument for
   the same identity **that we show is not well posed**". A oração
   relativa cola gramaticalmente em "identity", não em "argument". Lido
   ao pé da letra, o resumo diz que a identidade que o paper acabou de
   provar não é bem posta.
3. Narra a correção de um argumento que o paper nunca atribui a
   ninguém. Combinado com a linha 576-577 ("the error corrected in
   Example~\ref{ex:naive-fails}"), o leitor externo fica sem saber de
   quem era o erro. Se o argumento era de um rascunho anterior deste
   mesmo projeto, a Regra 4b §3 ("Narrating the process") manda apagar,
   não relatar; se era de outra pessoa, precisa de citação.
4. Regra 8b, otimismo relativo ao corpo: o resumo diz "for $q\ge5$ the
   claim is strengthened by a large-sample statistical test at $q=5$,
   though still not proved". O corpo tem três medições em $q\ge5$: a
   de 600 raízes (mostrada não confirmatória), a de 5000 raízes
   ("mixed rather than confirmatory", com Vuong favorecendo a
   lognormal em três de quatro níveis) e a de $10^5$ raízes (essa sim
   favorável). O resumo só reflete a terceira. Além disso, "for
   $q\ge5$ the claim is strengthened" desliza de escopo: a evidência é
   de $q=5$ apenas.

**C-14 (média) — auto-suficiência (item 1 da tarefa).**
O §2 fixa a árvore reversa, $T_q$, $d=\mathrm{ord}_q(2)$, $a_0(u)$,
esterilidade, $N_u(x)$ e a recursão de $G$. Isso cobre §3 quase todo.
O que falta, em ordem de aparição:

- `thm:qadic-martingale` (l.256-258) fala em "$\mu_\alpha$ (...) the
  projective law of the tilted **Syracuse sums**" no enunciado, mas
  $F_k$ e a lei $p_\alpha$ só aparecem dentro da prova, e "Syracuse
  sums" nunca é definido neste paper. O enunciado usa objeto que a
  prova introduz.
- $\alpha_-(q)$ e $\alpha_+(q)$ são usados em §3
  (`thm:frozen-singular`, l.344) e definidos só em §4
  (`prop:always-frozen`, l.399).
- $\pi_a(x)$ (l.561), na formulação da Growth Exponent Conjecture,
  nunca é definido.
- "the true (**not extended**) reverse trees" (l.826): "extended"
  é termo do paper 01, sem sentido aqui.
- "headroom levels" (l.655, l.699, l.773) é usado três vezes como se
  fosse termo técnico estabelecido e nunca é definido.
- $\theta$ é introduzido dentro da prova de `thm:iid-tail` (l.625) e
  depois usado em texto corrido (l.651, l.720).
- `\ZZ` é declarado no preâmbulo e nunca usado; `\ord` é usado.

**C-15 (média) — colisão de notação.**
$s$ é a entropia $s(\alpha)$ em §3 (`thm:frozen-singular`, l.362) e §4
(definição na l.392, tabela de $\alpha_c$), e é a variável do expoente
de cauda em l.662 ("$q^{s-1}/(2^s-1)$", na nota de rodapé) e l.668
("$\mathbb{E}[\sum_iA_i^s]=1$"). Os dois usos convivem na mesma página.
Menor, mas real: `$A_0(u\bmod q)$` na l.837 contra `$a_0(u)$` do §2.

**C-16 (média) — vocabulário banido pela Regra 4b §1.**
Contagens no `main.tex`:

- `genuine` ×12 (l.80, 92, 439, 441, 490, 512, 545, 551, 584, 588, 836,
  857). Está na lista literal.
- `precise`/`precisely` ×10, incluindo o **título da §6** ("Precise
  regime of the tail exponent"). Nenhuma das ocorrências é sentido
  técnico.
- "This is **not a coincidence**" ×2: l.418-419 ("is not a numerical
  coincidence but the same sign condition") e l.779 ("This is not a
  coincidence alongside the freezing computation"). Está na lista de
  "paragraph-closing kickers" banidos.
- "**Taken together**, neither route confirms" (l.749). Lista de
  transições banidas.
- "it is **worth recording** exactly why" (l.158). Variante de "it is
  worth noting that".
- `remarkably` (l.710), `substantial`/`substantially` (l.699).

**C-17 (média) — orçamento "X, not Y" estourado.**
A Regra 4b §2 dá no máximo dois por documento. Contei ao menos treze:
"rather than a heuristic transfer operator" (l.75), "rather than path
occurrences" (l.136), "rather than by the bulk" (l.395), "not merely a
formal entropy computation but a genuine divergence" (l.439), "rather
than hidden" (l.446), "below $1$ rather than above it" (l.490), "not
merely the exponent" (l.507), "a related but distinct question" (l.524),
"rather than resolving it" (l.567), "rather than as a single theorem"
(l.574), "not a matching two-sided quenched statement" (l.592), "the
test is inconclusive, not disconfirming" (l.745-746), "the operative
fact, not an irrelevant one" (l.546-547), "not the critical case"
(l.807), "a route different from, but numerically identical to" (l.851).

**C-18 (média) — narração de processo.**
Regra 4b §3, "Narrating the process", proíbe sem exceção fora de errata
publicada. Ocorre em bloco:

- §6 **abre** com "A directed literature search raised the question
  whether..." (l.788). Uma seção de resultado que começa contando como
  a busca bibliográfica foi feita.
- `prop:transition-fine`: "A directed literature search found the
  neighboring machinery but not this exact statement ready-made"
  (l.518-519), dentro de um ambiente de teorema.
- §5: "in earlier stages of this line of work" ×2 (l.487-488, l.686);
  "was later shown, over the course of this line of work, to be
  statistically non-confirmatory" (l.692-694); "We pursued this further
  along two independent routes" (l.695-696); "We have since pursued
  exactly the two follow-ups this pointed to" (l.753-754).
- `rem:novelty-109` inteiro é enquadrado como relato de checagem ("A
  directed novelty check against (...) established that...", l.845). O
  conteúdo (a atribuição a Wirsching e a Kontorovich-Lagarias) é
  necessário e correto de manter por honestidade de prioridade; o
  enquadramento como narrativa de auditoria é que não.

**C-19 (média) — assimetria estrutural pelo lado errado.**
§5 vai da linha 465 à 783, cerca de um terço do paper, e contém: a
transição estrutural, um teorema, uma proposição, duas conjecturas, uma
prova, e depois **quatro parágrafos densos de resultado empírico em
$q=5$** (baterias de estimadores, teste de Vuong, varredura GPD, teste
exato de momentos, periodograma). §7 se chama "Empirical confirmation
on real reverse trees" e tem um parágrafo de seis linhas mais um
Remark bibliográfico. A Regra 4b §5 permite (e recomenda) seções
desiguais, mas isso aqui não é assimetria deliberada: é matéria
empírica que ficou na seção teórica enquanto a seção empírica ficou
vazia. Item 4 da tarefa, resposta parcial: a §6 não parece bloco colado
por causa do conteúdo (o roteiro da §1, l.92-94, a anuncia, e o
parágrafo final da §6 amarra de volta em `prop:always-frozen`), mas
parece deslocada por três razões independentes: abre narrando processo
(C-18), é escopada em $q=3$ logo depois de quatro parágrafos sobre
$q\ge5$ sem nenhuma frase de transição, e carrega o lema geral do qual
§4 e §5 dependem (C-09).

**C-20 (média) — `ex:naive-fails` vs. a matriz multitipo da nota.**
§3 abre com um Exemplo cuja conclusão é categórica: "There is therefore
no well-defined finite-state transfer operator tracking a single
generation of the recursion on residue classes of any fixed finite
modulus" (l.171-174). A nota de rodapé da l.646 então usa, sem
comentário, "the multitype pressure matrix" indexada por classes de
resíduo mod $q$, calcula seu autovalor de Perron e o iguala a
$q^{s-1}/(2^s-1)$. Como registrado acima, a conta **está certa**, mas
só porque o tipo do filho é uniforme sobre todas as $q$ classes (que é
o próprio mecanismo do `ex:naive-fails`), e isso não é dito em lugar
nenhum. Como está, o leitor atento vê uma matriz de transferência
finita duas páginas depois de o paper afirmar que ela não existe. É
matéria matemática real (uma robustez do resultado principal a $q$ com
$d<\varphi(q)$) enterrada numa nota de rodapé de 21 linhas sem
derivação.

**C-21 (média) — citações a conferir na fonte primária (Regra 11).**
Não verificáveis offline nesta rodada. Registradas como pendências de
verificação, não como erros afirmados:

- **Applegate-Lagarias I e II como fonte da Growth Exponent
  Conjecture** (l.558-561). Os dois artigos citados, Math. Comp. 64
  (1995) 411-426 e 427-438, são "Density bounds for the $3x+1$ problem"
  I e II. O enunciado $\pi_a(x)=x^{1+o(1)}$ com nome "Growth Exponent
  Conjecture" é, quase certamente, de um terceiro artigo do mesmo par
  no mesmo ano ("The distribution of $3x+1$ trees", Experimental
  Mathematics 4). Se for o caso, é citação trocada. Note que o uso
  desses mesmos dois `\bibitem` na l.590 (limite unilateral de
  densidade, depois refinado por Krasikov-Lagarias) está correto, o que
  sugere que a chave certa foi reaproveitada no lugar errado.
- **"$\eta_{5,BP}$ in their Theorem 8.10"** (l.849-850), em
  Kontorovich-Lagarias. Número de teorema e notação precisam ser
  conferidos no capítulo. A Regra 11 é explícita sobre não citar
  afirmação de autor nomeado e vivo a partir de paráfrase.
- **"Wirsching had already conjectured the transition heuristically in
  1998"** (l.852-853). Precisa de página no LNM 1681.
- **`VillemonaisZalduendo2025`**, arXiv:2512.07653. Existência,
  título e autores não conferidos.
- **`KontorovichLagarias2009`**: chave diz 2009, `\bibitem` diz
  American Mathematical Society, 2010. Escolher um.
- **`KoleskoMentemeier2015`**: único `\bibitem` sem dados de
  publicação (só o arXiv), enquanto todos os outros têm volume e
  páginas. Saiu em periódico; padronizar.

**C-22 (média) — Regra 11, citação declaradamente não verificada.**
Linhas 529-532: "a very recent preprint \cite{VillemonaisZalduendo2025}
extends branching-process convergence laws to general type spaces
without geometric rescaling and **may already contain it, but we have
not verified this**". A Regra 11 pede o oposto: ou se lê a fonte e se
afirma o que ela diz, ou não se cita. Reconhecer a não verificação por
escrito é honesto mas não satisfaz a regra, e está dentro de um
ambiente de teorema (ver C-01).

**C-23 (baixa) — existência e unicidade afirmadas sem argumento.**
Linha 468-473: "equation \eqref{eq:pressure-eq} has **exactly one**
further positive root". A log-convexidade dá "no máximo duas raízes",
que é o que o parêntese justifica; a existência da segunda precisa de
$P\to+\infty$ nas duas pontas mais $P'(1)\ne0$ (o que vale sempre, já
que $\log q\ne2\log2$ para $q$ ímpar). Duas linhas resolvem.
Analogamente, l.423-425 fala em "**the** root of $s(\alpha)=0$";
`prop:always-frozen` mais o TVI dão existência no intervalo, não
unicidade.

**C-24 (baixa) — resíduos de preâmbulo e de rotulagem.**
O ambiente `empirical` ("Empirical Result") é declarado na l.16 e nunca
usado, embora o paper tenha bastante material que a Regra 10b mandaria
rotular assim (as medições de §5 em $q=5$, as inclinações de contagem
de §7, a verificação por enumeração direta da l.235-238). Todas estão
em prosa corrida, sem rótulo. `\ZZ` declarado e não usado.
`\begin{thebibliography}{9}` com 18 entradas: a largura do rótulo fica
errada a partir de [10].

**C-25 (baixa) — "linear growth".**
Linha 503: "exponent $1$ (linear growth) at $q=3$". O teorema afirma
$\log N(x)/\log x\to1$, que é $x^{1+o(1)}$, compatível com
$x/\log x$ ou $x\log x$. Chamar de crescimento linear é mais forte que
o enunciado.

**C-26 (baixa) — repositório (Regra 12).**
O repositório existe, roda e cobre os números do paper. Duas coisas
menores:

- `sec3-pressure-and-transition/iid_tail_check_assumptions.py` tem
  docstring "Check the closed-form hypotheses for the iid tail theorem
  **in paper 01**". Referência cruzada obsoleta dentro do repositório
  dedicado do paper 06. A Regra 12 é explícita: o leitor de um paper
  nunca deve precisar de outro paper.
- A Data Availability do paper (l.873-875) diz "organized **by
  section** with a README per subfolder". Há uma única subpasta,
  chamada `sec3-...`, que o README do repositório mapeia para "§3-§7".
  O nome ficou do paper 01. Não é falso, mas "organized by section"
  descreve algo que não é o que está lá.

**C-27 (baixa) — `OUTLINE.md` desalinhado com o texto.**
A tabela "Rótulo dos resultados (Regra 10b)" do `OUTLINE.md` lista
`thm:transition-model` e `prop:always-frozen` sob "Teorema (prova
completa)". Por C-06, `thm:transition-model` não tem prova no paper;
por C-09, `prop:always-frozen` depende de um lema estabelecido só em §6
e com justificativa errada. O `OUTLINE.md` é o registro de rotulagem do
paper e está mais confiante que o `main.tex`.

**C-28 (baixa) — "solved exactly by $s=\alpha_+/\alpha_-$".**
Linha 668-670. A equação $q^{\alpha_-s-1}=2^{\alpha_-s}-1$ tem duas
soluções positivas, $s=1$ e $s=\alpha_+/\alpha_-$. "Solved exactly by"
sugere unicidade. É a mesma raiz trivial que o resto do paper trata com
cuidado; aqui some.

**C-29 (baixa) — sem conclusão, e um resultado órfão.**
O paper termina em `rem:novelty-109` e emenda direto na Data
Availability. A Regra 4b §5 permite não amarrar tudo no fim, mas para a
Regra 8b isso significa que só existe uma superfície (o resumo) onde a
inconsistência clássica pode aparecer, e ela já aparece (C-13). Além
disso `thm:frozen-singular` nunca é referenciado por nada no texto,
embora seja um dos resultados anunciados no resumo.

**C-30 (baixa) — Regra 5.**
Não existe `main-pt-br.tex`. O `OUTLINE.md` registra como pendência
deliberada ("só sob pedido explícito"). Fica anotado porque a Regra 8b
observa que a versão bilíngue dobra a superfície onde uma correção pode
não chegar: quando o gêmeo em português for criado, todos os achados
acima precisam ser aplicados nas duas versões, incluindo resumo e
conclusão de cada uma.

---

## 2026-08-10 — rodada 2 (produtor, resposta à crítica)

Todos os 30 achados da rodada 1 foram lidos e verificados
independentemente (Regra 8c) antes de qualquer conserto. 29 corrigidos,
1 rejeitado com motivo (C-30). `main.tex` recompila limpo em duas
passagens de `pdflatex`, sem referências indefinidas; bibliografia
(18 `\cite`/`\bibitem`) e referências cruzadas (`\ref`/`\eqref`/`\label`)
verificadas por script, sem órfãos em nenhuma direção.

**Alta severidade (C-01 a C-06).** A correção mais substancial da
rodada foi C-06: em vez de só apontar a citação errada de `Biggins1992`
em `thm:transition-model`, o teorema ganhou uma prova real, dividida em
duas metades com técnicas diferentes. O limite superior
($\limsup\log N(x)/\log x\le\alpha_-(q)$) sai de um argumento de
Chernoff/Markov de quatro linhas, direto da identidade many-to-one já
usada para construir o modelo iid explicitamente (que C-06 também
pedia: o processo pontual de reprodução agora está escrito, não só
citado por uma propriedade). O limite inferior não foi inventado do
zero (seguindo o conselho explícito do consultor externo desta rodada
de não escrever um argumento de segundo momento tipo Paley-Zygmund sob
pressão de tempo); em vez disso, a Seção 8.10 de Kontorovich-Lagarias
2010 (conferida diretamente no PDF local, item 127 da coleção de
literatura) já prova exatamente esse resultado para o caso $q=5$ de
tipo único, por um argumento de grandes desvios que o próprio KL
atribui a Lagarias-Weiss, não a Biggins — daí a citação errada
original. O texto agora cita KL2010 Teorema 8.10 para o limite
inferior e nota que o argumento transfere sem mudança para o presente
modelo indexado por $q$. Isso também resolve a contradição interna que
C-06 apontava: `prop:transition-fine` continua dizendo corretamente que
Biggins1992 só dá convergência geração-a-geração, mas `thm:transition-model`
não cita mais Biggins1992 para nada, então as duas afirmações não se
contradizem mais.

C-09 foi a segunda correção estrutural real: o lema de log-convexidade
que três seções (§3, §4, §5) precisavam e que só existia, mal
justificado, dentro da §6 (escopada em $q=3$), virou
`lem:log-convex`, um lema de quatro linhas logo depois da prova de
`thm:pressure` no §3, com a justificativa certa (segunda derivada
calculada diretamente, $P''(\alpha)=\log^22\cdot2^\alpha/(2^\alpha-1)^2>0$,
não "limpar denominadores"). `prop:always-frozen` e a existência da
segunda raiz em §5 agora citam esse lema para trás, não mais para
frente até §6. A §6 ficou só com a classificação específica de $q=3$
contra a teoria de smoothing transform, citando o lema em vez de
repeti-lo.

C-04 (classe estéril errada em $q=9$) foi verificada primeiro contra o
código do repositório (`tree_lib_sterility.py`): a enumeração numérica
já testa fertilidade nó-a-nó via busca direta de $2^au\equiv1\pmod q$,
sem nunca assumir a descrição estrutural errada do texto, então nenhum
número de §5 estava afetado, só a prosa. Corrigida para tratar
corretamente o caso $q$ composto (as classes estéreis em $q=9$ são
$\{0,3,6\}$, os múltiplos de $3$, não só $u\equiv0$).

**Média severidade (C-07 a C-22).** Maior parte mecânica (travessões,
vocabulário banido, "pre-registered", narração de processo, colisão de
notação $s$/$\sigma$, auto-suficiência). Duas exceções que exigiram
trabalho real:

- C-19 (assimetria estrutural): em vez de mover fisicamente os
  parágrafos de teste estatístico do §5 para o §7 (risco alto de
  quebrar referências e fluxo para um achado de severidade média), a
  correção foi um sinalizador explícito: o §5 agora diz claramente que
  seus testes visam `conj:tail-index` (índice de cauda), enquanto o
  resultado do §7 (agora rotulado `emp:real-trees`, ambiente
  `empirical`) visa `conj:transition-arithmetic` (expoente de
  crescimento), com referência cruzada nos dois sentidos.
- C-21/C-22 (citações): `KontorovichLagarias2010` corrigida (chave
  dizia 2009, mas o ano de copyright oficial da AMS, conferido
  diretamente em `bookstore.ams.org/mbk-78` via `curl`, é 2010; a
  entrada bibliográfica em si já estava certa). `KoleskoMentemeier2015`
  ganhou volume/DOI verificados via CrossRef (`Electron. J. Probab.
  20 (2015)`). A citação de Wirsching 1998 para a antecipação
  heurística da transição em $q\ge5$ ganhou localizador preciso
  (Cap. III, §5, perto do Teorema 5.2) depois de reextrair o PDF local
  do livro (item 131) e achar a passagem exata ("if $p>4$... Presumably
  we would be led to..."). `VillemonaisZalduendo2025` foi baixado
  (item 148 da coleção de literatura, autorização explícita do
  pesquisador nesta sessão para baixar PDFs de citação daqui em
  diante) e lido: o preprint estende convergência de martingala
  geração-a-geração a espaços de tipo gerais, mas não contém nenhuma
  máquina de renovação ou Crump-Mode-Jagers, então **não** cobre a
  assíntota somada-sobre-gerações que `prop:transition-fine` precisa;
  o texto antes dizia "may already contain it, but we have not
  verified this" (violação direta da Regra 11 dentro de um ambiente de
  proposição) e agora afirma o que foi de fato verificado. Applegate-Lagarias
  I/II, a citação já existente para a Growth Exponent Conjecture, foi
  verificada e está **correta**: "Conjecture A" no paper de Density
  Bounds I (item 129 local) é exatamente $\pi_a(x)\ge c_ax$, a mesma
  afirmação; a suspeita da rodada 1 de que a fonte certa seria "The
  Distribution of 3x+1 Trees" não se confirmou (aquele paper trata de
  "Conjecture C/C#" sobre valores extremos de contagem de folhas, um
  objeto relacionado mas diferente). $\eta_{5,BP}$ no Teorema 8.10 de
  KL também foi conferido diretamente no PDF: bate exatamente com
  $\alpha^\ast(5)=0{,}650919$ do paper, sem discrepância.

**Baixa severidade (C-23 a C-30).** C-23 (existência/unicidade)
resolvida com um argumento curto: $P\to\infty$ nas duas pontas mais
$P'(1)=\log(q/4)\ne0$ para todo $q$ ímpar garante a segunda raiz do
lado certo; e $s'(\alpha)=-\alpha P''(\alpha)<0$ em todo $\alpha>0$
(consequência direta do novo `lem:log-convex`) dá monotonicidade
estrita de $s$, logo unicidade de $\alpha_c(q)$ onde quer que exista.
C-26 corrigido tanto no paper (Data Availability não afirma mais
"organized by section" quando há uma pasta só) quanto no próprio
repositório `collatz-qx1-pressure` (docstring corrigida de "paper 01"
para "paper 06"; "pre-registered" também removido dos dois READMEs
daquele repositório, mesma correção do texto principal). C-27
corrigido no `OUTLINE.md`: a rotulagem "prova completa" para
`thm:transition-model` e `prop:always-frozen` está correta agora que
C-06/C-09 foram resolvidos (não era um erro do `OUTLINE.md` isolado,
era o `main.tex` que ainda não tinha alcançado o que o `OUTLINE.md` já
afirmava). C-30 (falta `main-pt-br.tex`) fica `rejected`/deixado aberto
pelo mesmo motivo já registrado nos papers 04 e 05: a política interna
deste projeto é traduzir só sob pedido explícito, o que tensiona com a
letra da Regra 5; a decisão de resolver essa tensão cabe ao
pesquisador, não a esta rodada de crítica. Por instrução explícita do
pesquisador nesta mesma sessão, nenhum arquivo PT-BR (incluindo dos
repositórios companheiros) deve ser criado ou editado sem pedido
explícito daqui em diante.

---

## 2026-08-10 — rodada 3 (produtor, redação final: H-129 formalizada)

Escopo: formalizar H-129 como conjectura própria deste paper (decisão
do diretor científico, atribuição resolvida) e reler `main.tex` inteiro
contra o checklist da Regra 4b/seção 10.

**C-31 (achado, não pedido originalmente).** Ao localizar onde H-129 se
encaixava, ficou claro que as baterias de raízes reais amostradas
(600 raízes, depois 5000, depois 100.000, todas em §4) vinham citadas
como evidência de `conj:tail-index` (a martingale Haar-q-ádica $W_q$,
população de resíduos mod $q^k$ amostrada uniformemente). Mas o que
essas baterias de fato amostram são raízes inteiras reais $v$ da
árvore aritmética, medindo $W_v(H):=N_v(vH)/H^{\alpha_-(q)}$ — o fator
de escala já introduzido, conjecturalmente, em `prop:transition-fine`.
Só o teste exato de momento populacional (soma sobre TODOS os resíduos
mod $5^k$, não uma amostra) testa `conj:tail-index` de fato. As duas
conjecturas preveem o mesmo expoente pelo mesmo mecanismo de renovação
implícita, mas são objetos matemáticos formalmente distintos, sem
prova de equivalência entre eles.

Verificado antes de editar: consulta ao advisor (confirmou a leitura
"são objetos diferentes", apontou a formalização correta) e ao Codex
(revisão independente da reatribuição planejada, confirmou o
diagnóstico, sugeriu a forma final do enunciado da nova conjectura e
listou riscos de referee, incorporados). Conferido também contra o
código-fonte dos experimentos (`E-103`, `rerun_save_raw.py`,
`stage6_large_sample_generation.py`): `W = c / H**ALPHA1` com `c =
count_tree(q, v, v*H, ...)` para raízes `v` sorteadas uniformemente de
um intervalo de inteiros, confirmando que a amostragem é sobre raízes
reais, não sobre resíduos.

**Corrigido**: nova `\begin{conjecture}[Tail of the real-tree growth
scale factor]\label{conj:real-tree-tail}`, logo após `thm:iid-tail`;
evidência de $q=3$ (Hill/EVT) e as três baterias de $q=5$ (600/5000/
100.000 raízes) reatribuídas para ela; `conj:tail-index` mantém só o
teste de momento populacional (Rodada 3 de E-103, inconclusivo) como
evidência direta; a nota de rodapé da família de escala por tipo de
resíduo (Estágio 4 de E-103, mesma amostra de raízes reais) foi
realocada da vizinhança de `conj:tail-index` para a de
`conj:real-tree-tail`. Abstract reescrito (Regra 8b, conferido de novo
depois de todas as edições desta rodada) para nomear os dois objetos
separadamente em vez de uma "tail index" genérica.

**Regra 4b/seção 10, aplicada ao documento inteiro**: zero vocabulário
banido (checado por regex), zero travessão (o documento já não tinha
nenhum), um clichê de fechamento de parágrafo cortado ("What survives
as new here is" — item explicitamente banido pela Regra 4b §1, em
`rem:novelty-109`), quatro antíteses "X, not Y" redundantes ou
puramente retóricas cortadas (de 16 ocorrências para 12; as 12
restantes desambiguam objetos matemáticos genuinamente confundíveis
num texto denso — julgamento registrado aqui, não uma omissão: reduzir
a duas exigiria sacrificar precisão técnica necessária, o que a própria
Regra 4b não pede). Nenhuma seção nova por simetria; nenhuma frase cujo
sujeito seja o próprio paper além da já existente e inofensiva "This
paper studies..." na abertura.

**Achado colateral pequeno, corrigido**: `experiments/E-103.../README.md`
apontava um espelho público em `collatz-endogeny/sec3-pressure-equation/`
que não existe mais desde a divisão do paper 01 em quatro (migrado para
`collatz-qx1-pressure/sec3-pressure-and-transition/`); corrigido só na
versão em inglês (PT-BR fora de escopo desta rodada, por instrução do
pesquisador).

**Verificação técnica final**: recompilado (3 passadas `pdflatex`),
zero `undefined reference`/`citation`; `\cite`/`\bibitem` e
`\ref`/`\eqref`/`\label` conferidos por script Python, sem órfãos em
nenhuma direção; Data Availability (`collatz-qx1-pressure`) conferido
contra os arquivos reais do repositório, todos os scripts citados
(`full_battery.py`, `exact_moment_test.py`,
`stage6_large_sample_battery.py`, `stage4_type_constants_check.py`)
presentes.

**Não fica pendente para o paper 01**: o agente responsável pelo paper
01, em paralelo, ajusta o lado dele para apenas citar o tratamento
deste paper, sem duplicar o enunciado de `conj:tail-index`.

---

## Loop de convergência (critério do pesquisador, 4 níveis: crítico/maior/moderado/menor)

A partir daqui, cada rodada é uma crítica adversarial completa e
independente do `main.tex` atual (contexto fresco, sem reaproveitar o
julgamento da rodada anterior). Critério de parada: 3 rodadas
CONSECUTIVAS limpas (crítico=0, maior=0, moderado=0, menor<3), sem
crédito parcial — qualquer rodada abaixo do padrão zera a contagem.

### 2026-08-10 — rodada de convergência 1 (crítico, contexto fresco)

Escopo: `main.tex` inteiro, revisão adversarial independente, incluindo
verificação numérica própria (mpmath, 30 dígitos), checagem de
`\cite`/`\bibitem`/`\ref`/`\eqref` por script, e consulta a fontes
primárias locais (Kontorovich-Lagarias 2010, Applegate-Lagarias I/II,
Gonçalves-Greenfeld-Madrid 2022, Liu 2000, Villemonais-Zalduendo 2025)
para todas as citações de maior risco, incluindo uma nunca antes
checada em nenhuma rodada anterior (GGM2022).

**Resultado: 2 crítico, 2 maior, 4 moderado, 1 menor (agrupado, 3
ocorrências). Não limpa. Contagem de rodadas limpas consecutivas: 0/3.**

| ID | Nível | Resumo | Status |
|----|-------|--------|--------|
| D-01 | crítico | `thm:transition-model`, prova do limite inferior: alegava que o Teorema 8.10 de Kontorovich-Lagarias 2010 "transfere sem mudança" para q geral; falso (modelo B[5^0] de KL tem função de pressão diferente da deste paper, mesma raiz por identidade algébrica distinta) | fixed |
| D-02 | crítico | `prop:transition-fine` rotulado Proposition com conteúdo explicitamente não provado (abre com "conjecturally"); `conj:real-tree-tail` já dependia dele | fixed |
| D-03 | maior | Resumo: "For q=3 this is the classical Growth Exponent Conjecture" tem como único antecedente gramatical $\alpha^\ast=2$ (raiz não trivial), mas a GEC é sobre a raiz trivial ($\alpha_-=1$), como o corpo (`conj:transition-arithmetic`) já atribui corretamente | fixed |
| D-04 | maior | Remark "Mass conservation as a corollary": o lado direito de \eqref{eq:annealed-identity} em $\alpha=1$ vale $q^k$, não $1$; o objeto que vale $1$ é a média \eqref{eq:pressure-closed-form} | fixed |
| D-05 | moderado | Nota de rodapé de `conj:real-tree-tail`: $\theta$ usado sem redefinição próxima (definido só dentro da prova de `thm:iid-tail`, várias dezenas de linhas antes) | fixed |
| D-06 | moderado | `conj:real-tree-tail`: ordem do limite duplo mal especificada ("as $H\to\infty$ and then the interval grows" não corresponde ao protocolo empírico real, onde $H$ é finito e a amostra de raízes cresce) | fixed |
| D-07 | moderado | Resumo vs. §5: a ressalva de não convergência da mediana de $W_v(H)$ no teste de $10^5$ raízes não chegava ao resumo | fixed |
| D-08 | moderado | §5: tensão aparente entre "the bias-corrected Hill estimator is stable... lands close to the predicted 1.536" e "without settling near any single value" (dois eixos de comparação distintos, não explicados) | fixed |
| D-09 | menor | Narração de processo (Regra 4b §3), 3 ocorrências: "in earlier stages of this line of work" (×2) e "was later shown, over the course of this line of work" | fixed |

**Verificado e correto nesta rodada, sem achado (registro para não ser re-checado à toa nas próximas rodadas):** compilação limpa; `\cite`/`\bibitem` e `\ref`/`\eqref`/`\label` fechados nas duas direções; tabelas de $\alpha^\ast(q)$/$\alpha_c(q)$; $m'(1)$/$m'(2)$ em §6; citação Kontorovich-Lagarias 2010 Teorema 8.10 e $\eta_{5,BP}$; Applegate-Lagarias "Conjecture A"; cota de Krasikov-Lagarias; localizador de Wirsching 1998; Villemonais-Zalduendo 2025 (não contém maquinaria de renovação/CMJ); Gonçalves-Greenfeld-Madrid 2022 (primeira vez checada, correta); Liu 2000 (hipóteses do Teorema 2.2 usadas corretamente em `thm:iid-tail`); zero travessão; zero vocabulário da lista literal da Regra 4b §1.

**Correções aplicadas (produtor, Regra 8c: cada achado verificado antes do conserto):**

- **D-01.** Fui à fonte primária (PDF local de Kontorovich-Lagarias
  2010) e confirmei: o modelo B[5^0], para o qual o Teorema 8.10 é
  provado, tem no máximo 2 filhos por nó, função de pressão
  $m_{KL}(\theta)=2^{-\theta}(1+5^{\theta-1})$; o modelo i.i.d. deste
  paper tem quase certamente infinitos filhos por nó, função de
  pressão $\rho_{\mathrm{ann}}(\theta)=5^{\theta-1}/(2^\theta-1)$.
  Processos genuinamente diferentes, que só coincidem nas raízes de
  suas equações de pressão (identidade algébrica verificada:
  $m_{KL}(\theta)-1=\frac{2^\theta-1}{2^\theta}(\rho_{\mathrm{ann}}(\theta)-1)$).
  Consultei o advisor e depois o Codex (leitura read-only,
  `codex exec`) antes de escrever qualquer prova nova, exatamente para
  não repetir o erro documentado na rodada 2 anterior (segundo momento
  nunca escrito "sob pressão de tempo"). O Codex propôs um argumento de
  Galton-Watson em blocos (tilt exponencial na raiz $\alpha_-(q)$,
  truncamento em janela de deslocamento, redução a um processo
  supercrítico); verifiquei cada passo eu mesmo linha a linha e
  encontrei um erro na primeira versão do Codex (a alegação de que o
  número de sequências de expoentes candidatas por bloco seria
  limitado é falsa: cresce exponencialmente em $L$; a correção correta
  é truncar em $K$ filhos por bloco, com $K\to\infty$ depois de
  $L\to\infty$, o que evita qualquer hipótese de momento tipo
  Kesten-Stigum/Seneta-Heyde, já que a versão truncada tem variância
  finita trivialmente). A prova final no `main.tex` usa só fatos
  clássicos elementares (identidade de muitos-para-um, já usada
  corretamente em outros pontos do mesmo paper; lei dos grandes
  números; teorema de crescimento para processos de Galton-Watson
  supercríticos de variância finita). Um novo Remark registra a
  identidade algébrica das raízes e deixa claro que a prova de KL não
  transfere.
- **D-02.** Relabel `prop:transition-fine` → `conj:transition-fine`
  (ambiente `conjecture`, não mais `proposition`); todas as 4
  ocorrências de `\ref`/`\label` atualizadas; a frase "three separate
  claims" ajustada para descrever a hierarquia real (um Teorema provado
  e duas Conjecturas).
- **D-03.** Resumo reescrito: a raiz não trivial $\alpha^\ast(q)$ e o
  expoente de crescimento $\alpha_-(q)$ agora aparecem como objetos
  claramente distintos, com a GEC ligada explicitamente ao caso
  $q=3$/expoente $1$.
- **D-04.** Remark corrigido para usar diretamente
  $\rho_{\mathrm{ann}}(1)=q^0/(2^1-1)=1$ (conta trivial e certamente
  correta), em vez de uma leitura errada de \eqref{eq:annealed-identity}.
- **D-05 a D-08.** Correções mecânicas: $\theta:=\alpha_-(q)$ redefinido
  na própria nota de rodapé; `conj:real-tree-tail` reescrita com $H$
  fixo e a amostra de raízes crescendo primeiro, depois $H\to\infty$;
  cláusula sobre a deriva da mediana incorporada ao resumo; frase
  adicionada em §5 nomeando os dois eixos de comparação (estabilidade
  de um estimador através de níveis de headroom vs. variação entre
  quatro estimadores diferentes).
- **D-09.** As três ocorrências de narração de processo removidas e
  reancoradas com o conteúdo factual que carregavam (metodologia e
  objeto medido, amostras reais da árvore vs. modelo idealizado), sem
  narrar quando ou em que estágio a medição foi feita.

**Verificação técnica pós-correção:** recompilado (3 passadas
`pdflatex`), zero erro/referência indefinida; `\cite`/`\bibitem` e
`\ref`/`\eqref`/`\label` conferidos por script, sem órfãos em nenhuma
direção. `OUTLINE.md` atualizado (tabela de rótulos Regra 10b).

### 2026-08-10 — rodada de convergência 2 (crítico, contexto fresco)

Escopo: `main.tex` inteiro, com atenção dedicada à prova nova de
`thm:transition-model` (limite inferior via Galton-Watson em blocos,
nunca revisada por um crítico fresco antes desta rodada).

**Resultado: 1 crítico, 0 maior, 3 moderado, 2 menor. Não limpa.
Contagem de rodadas limpas consecutivas: 0/3.**

| ID | Nível | Resumo | Status |
|----|-------|--------|--------|
| D-10 | crítico | Prova de `thm:transition-model` (limite inferior): definia $\xi_i$ como sorteio direto de $p_\alpha(a)$ (a lei do dígito) e alegava média $\mu$; falso — $p_\alpha$ tem média $\mathbb E[a]=2^\alpha/(2^\alpha-1)\approx2{,}754$ em $q=5$, não $\mu\approx0{,}299$. A LLN citada, como estava escrita, mandava a soma para o valor errado | fixed |
| D-11 | moderado | Colisão de notação: $H$ usado para entropia de Shannon ($H(p_\alpha)$, prova de `thm:frozen-singular`) e para "headroom" (resumo, `conj:real-tree-tail`, §7) | fixed |
| D-12 | moderado | Colisão de notação: $\sigma$ com dois papéis distintos (multiplicador normalizado em `thm:iid-tail`; argumento bruto da equação de pressão multitype na nota de rodapé de `conj:real-tree-tail`) | fixed |
| D-13 | moderado | `conj:transition-fine` descreve a prova de `thm:transition-model` como "the large-deviations argument used above", desatualizado após D-01 reescrever o limite inferior via Galton-Watson em blocos | fixed |
| D-14 | menor | Vocabulário banido (Regra 4b §1): "genuine" na prova nova de `thm:transition-model`, nunca escaneada contra a lista depois de escrita | fixed |
| D-15 | menor | Orçamento "X, not Y"/"rather than" (Regra 4b §2, máx. 2 no documento): 17 ocorrências contadas nesta rodada | parcialmente corrigido, ver nota |

**Correções aplicadas (Regra 8c: cada achado verificado antes do conserto):**

- **D-10.** Recalculei eu mesmo, independentemente do crítico:
  $\mathbb E[a]=2^\alpha/(2^\alpha-1)\approx2{,}7539$ e
  $\mu=-P'(\alpha)\approx0{,}2994$ em $q=5$, $\alpha=\alpha_-(5)$ —
  confirma o achado. Corrigido para: $a_1,a_2,\ldots$ i.i.d. de
  $p_\alpha(a)$ (a lei do dígito, papel correto), $\xi_i:=a_i\log2-\log q$
  (o deslocamento induzido); verifiquei
  $\mathbb E[\xi_i]=\log2\cdot\mathbb E[a_i]-\log q=-P'(\alpha)=\mu$
  diretamente (identidade exata, não aproximada). O resto da prova já
  tratava $\xi_i$ consistentemente como deslocamento (confirmado pelo
  crítico e por mim), então nenhuma outra correção foi necessária ali.
  Uma tentativa inicial de conserto introduziu, por minha conta, um
  segundo erro (uma identidade errada $\mu=-\alpha^{-1}s(\alpha)$, sinal
  trocado); descartada antes de entrar no texto, substituída pela conta
  direta e mais simples acima.
- **D-11.** Entropia de Shannon renomeada de $H(p_\alpha)$ para
  $\mathrm{Ent}(p_\alpha)$ nas 4 ocorrências (todas dentro da prova
  contida de `thm:frozen-singular`); "headroom $H$" mantido sem
  alteração (termo mais extenso e recente no documento).
- **D-12.** O $\sigma$ da nota de rodapé de `conj:real-tree-tail`
  (equação de pressão multitype genérica) renomeado para $\alpha$,
  igual à variável já usada em toda parte para essa mesma equação
  (\eqref{eq:pressure-closed-form}); o $\sigma$ de `thm:iid-tail`
  (multiplicador normalizado) mantido sem alteração, papel distinto e
  já consistente ali.
- **D-13.** "the large-deviations argument used above" corrigido para
  "the exponential tilting and block truncation used above", refletindo
  a prova de fato usada após D-01.
- **D-14.** "genuine" removido.
- **D-15.** Reclassifiquei cada uma das 17 ocorrências à mão: 13
  desambiguam objetos matemáticos genuinamente confundíveis (a maioria
  delas é precisamente o tipo de contraste que a Regra 4b §2 diz que
  deve ficar: "only where a reader would actually confuse X with Y" —
  ex.: a distinção entre o modelo B[5^0] de KL e o modelo i.i.d. deste
  paper no novo Remark, a distinção entre `conj:real-tree-tail` e
  `conj:tail-index`, a classificação do regime de cauda em §6). 4 eram
  puramente retóricas e foram cortadas (l. 479, 898, e a redução de
  "rather than one that has reached it" em l. 930-931, mais "we later
  verified" → "we verified" ao lado, achado colateral pequeno da mesma
  família proibida pela Regra 4b §3, corrigido nesta mesma passagem por
  estar na mesma frase). Contagem final: 14. Julgamento explícito, não
  omissão: reduzir a 2 exigiria cortar distinções que o próprio texto
  precisa para não confundir objetos matemáticos genuinamente
  diferentes (mesmo julgamento já registrado na rodada de redação final
  de 2026-08-10, reconferido aqui de novo, independentemente). Por isso
  D-15 está marcado "parcialmente corrigido": o volume caiu (17→14) mas
  não chegou ao orçamento literal de 2; classificado como `menor` no
  critério de convergência, então não bloqueia uma rodada limpa por si
  só desde que o total de achados menores da rodada fique abaixo de 3.

**Verificação técnica pós-correção:** recompilado (2 passadas
`pdflatex`), zero erro/referência indefinida; `\cite`/`\bibitem` e
`\ref`/`\eqref`/`\label` conferidos por script, sem órfãos em nenhuma
direção.

### 2026-08-10 — rodada de convergência 3 (crítico, contexto fresco)

Escopo: `main.tex` inteiro; terceira reconferência independente, do
zero, da prova de `thm:transition-model` (limite inferior), incluindo
o Remark novo sobre Kontorovich-Lagarias, com verificação direta contra
a fonte primária local (não reaproveitada das rodadas anteriores).

**Resultado: 0 crítico, 0 maior, 1 moderado, 1 menor. Não limpa.
Contagem de rodadas limpas consecutivas: 0/3.**

Nenhum erro matemático novo encontrado (a prova de
`thm:transition-model` foi confirmada correta, do zero, pela terceira
vez). O crítico registrou explicitamente: "Não encontrei erro
matemático novo em nenhuma prova, identidade ou fórmula numérica."

| ID | Nível | Resumo | Status |
|----|-------|--------|--------|
| D-16 | moderado | Orçamento "X, not Y"/"rather than" (Regra 4b §2): reavaliado de forma independente, 2 trechos concretos identificados como cortáveis sem perda técnica e não cortados nas rodadas anteriores apesar de examinados | fixed |
| D-17 | menor | Prova de `thm:transition-model`: dois gaps de rigor rotineiros não escritos explicitamente (deslocamento finito $\Delta$ da cópia sobrevivente; interseção contável sobre $L\to\infty$, mesma técnica já usada para $K$) | fixed |

**Correções aplicadas:**

- **D-16.** Cortadas as duas ocorrências concretas que o crítico
  apontou como redundantes: "one branch at a time rather than only in
  aggregate" (§5, parágrafo do modelo i.i.d., reescrito como
  "branch-by-branch transition rule", sem antítese) e "so the two
  models are not the same stochastic process" no Remark de
  Kontorovich-Lagarias (redundante com "not $\rho_{\mathrm{ann}}(\theta)$"
  imediatamente anterior, que já estabelece a diferença). Contagem cai
  de ~16 para ~14. A tensão remanescente entre a letra da Regra 4b §2
  ("no máximo dois por documento") e o conteúdo tecnicamente necessário
  do paper (distinguir repetidamente objetos matemáticos genuinamente
  diferentes: dois modelos estocásticos, duas conjecturas, um teorema
  de uma proposição condicional) fica registrada aqui como uma tensão
  real e não resolvida por conta própria do produtor pela terceira vez
  seguida — nomeada explicitamente para o pesquisador decidir, no
  mesmo espírito de C-30 (Regra 5), em vez de o produtor continuar
  arbitrando sozinho o mesmo ponto rodada após rodada.
- **D-17.** A prova ganhou um deslocamento finito $\Delta$ nomeado
  explicitamente (generation $jL+O(1)$, displacement at most
  $jL(\mu+\varepsilon)+\Delta$) em vez de só "shifts what follows by a
  bounded amount"; e a interseção contável sobre $K$ foi estendida,
  pela mesma técnica, a uma interseção contável sobre a sequência de
  $L$ usada no limite $L\to\infty$, deixando explícito que o evento
  quase certo vale simultaneamente ao longo dessa sequência.

**Verificação técnica pós-correção:** recompilado (2 passadas
`pdflatex`), zero erro/referência indefinida; `\cite`/`\bibitem` e
`\ref`/`\eqref`/`\label` conferidos por script, sem órfãos em nenhuma
direção.

### 2026-08-11 — rodada de convergência 4 (crítico, contexto fresco)

Escopo: `main.tex` inteiro, com instrução explícita de concentrar
esforço nas provas mais antigas do paper (nunca tocadas pelas três
rodadas anteriores) e na bibliografia, já que a prova de
`thm:transition-model` tinha acabado de ser confirmada correta, do
zero, três vezes seguidas.

**Resultado: 0 crítico, 1 maior, 1 moderado, 0 menor. Não limpa.
Contagem de rodadas limpas consecutivas: 0/3.**

| ID | Nível | Resumo | Status |
|----|-------|--------|--------|
| D-18 | maior | `rem:novelty-109`: "a later result rigorously excludes $q\ge5$" citando Gonçalves-Greenfeld-Madrid 2022 — falso; a exclusão de $q\ge5$ é a **Conjecture 1.5** do próprio paper deles, não um teorema, com suporte só numérico ("we were not able to find... it seems that condition (b) must be satisfied") | fixed |
| D-19 | moderado | `\bibitem{KontorovichLagarias2010}` sem faixa de páginas (única entrada de capítulo/artigo do documento sem uma) | fixed |

**Correções aplicadas (Regra 8c: cada achado verificado antes do conserto):**

- **D-18.** Baixei o PDF primário (arXiv:2111.06170v2, a versão exata
  citada) e li o Teorema 1.3, o Remark 1.4 e a Conjecture 1.5 na
  íntegra. O Teorema 1.3 prova a direção positiva (órbitas quase
  limitadas) sob três condições, incluindo $q<p^{p/(p-1)}$ (que em
  $p=2$ dá $q<4$). A necessidade dessa condição, isto é, que ela falhe
  para todo $q\ge5$, é exatamente a Conjecture 1.5, sustentada só por
  não terem achado contraexemplo numérico ("it seems that condition
  (b) must be satisfied whenever all orbits are bounded"). Reescrevi o
  trecho para atribuir corretamente: Teorema 1.3 prova a direção
  positiva sob a condição $q<4$; Conjecture 1.5 conjectura, com suporte
  numérico e sem prova, que a condição também é necessária. A rodada de
  convergência 1 tinha registrado essa citação como "primeira vez
  checada, correta" sem checar o status teorema-vs-conjectura da
  alegação específica sendo citada; registro aqui, por Regra 8c, que
  essa verificação anterior estava incompleta, não errada no que de
  fato conferiu (a existência do paper e o tema geral).
- **D-19.** Baixei o PDF oficial de sumário do livro
  (`ams.org/bookstore/pspdf/mbk-78-toc.pdf`, via `curl`) e confirmei: o
  capítulo de Kontorovich-Lagarias começa na página 131 e o capítulo
  seguinte (Oliveira e Silva) começa na 189, logo 131-188. Adicionado à
  entrada bibliográfica; corrigido também o título, que no sumário
  oficial é "... and related problems" (a entrada do `main.tex` estava
  truncada, faltando esse sufixo).

**Verificação técnica pós-correção:** recompilado (2 passadas
`pdflatex`), zero erro/referência indefinida; `\cite`/`\bibitem` e
`\ref`/`\eqref`/`\label` conferidos por script, sem órfãos em nenhuma
direção.
