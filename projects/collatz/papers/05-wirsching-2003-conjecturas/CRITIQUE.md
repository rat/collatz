# CRITIQUE: paper 05 (`main.tex`)

Arquivo único de crítica deste paper (Regra 8/15). A tabela de status no
topo é leitura obrigatória do produtor a cada passada; as seções datadas
abaixo são o histórico completo, consultadas sob demanda.

Primeira rodada, então não há coluna "Origem": o paper nasceu em
2026-08-10 da divisão de `01-syracuse-qx1-endogenia` §9.2+§9.3, e não
vale a pena separar o que veio de lá do que a divisão introduziu antes
de alguém decidir consertar.

Nenhum achado foi consertado nesta rodada (o crítico não conserta).

## Tabela de status

| ID | Rodada | Resumo | Severidade | Status |
|----|--------|--------|------------|--------|
| C-001 | 2026-08-10 | Abstract diz "a matching nonequivalence theorem at linear precision"; o corpo prova não equivalência só para os vetores de custo latentes e nega explicitamente a versão projetada | alta | fixed |
| C-002 | 2026-08-10 | Discussão diz que `thm:ensemble-divergence` "shows why" há não equivalência; o teorema é uma dominação (cota superior) e o corpo já diz que a direção é insuficiente | alta | fixed |
| C-003 | 2026-08-10 | As condições da fonte são (⋆1)-(⋆5), não (?1)-(?5): o "?" é artefato de extração de texto do PDF, propagado ~15 vezes no main.tex | alta | fixed |
| C-004 | 2026-08-10 | `prop:fabius` reproduz, sem prova e sem citação, os Corolários 7 e 8 e a fórmula (7.7) de Wirsching (2003), inclusive a constante `2^{-n+1}` | alta | fixed |
| C-005 | 2026-08-10 | Berg-Krüppel citados nominalmente em §5 sem `\bibitem`, com o paper registrado como não lido nesta linha; "atomic functions of Rvachev" idem | alta | fixed |
| C-006 | 2026-08-10 | `fixed_precision_projection.py` não roda no repositório citado (importa pasta inexistente); é o script que sustenta três teoremas e um resultado empírico | alta | fixed |
| C-007 | 2026-08-10 | §2: "The only bridge offered between the two is Wirsching's Theorem 3" é falso; a p.14 da fonte oferece também `lim ∫ g̃_ℓ(x,a)da = φ(x)` | média | fixed |
| C-008 | 2026-08-10 | §2 define as funções Elka como "paths of length k+ℓ"; a fonte pede exatamente k passos `T_0` e ℓ passos `T_1` | média | fixed |
| C-009 | 2026-08-10 | §3 apresenta como próprio o que a fonte já dá: `ē_ℓ(k)` é a fórmula (1.4) e a leitura de urnas está na p.8; o conteúdo novo é a cauda, não o cancelamento | média | fixed |
| C-010 | 2026-08-10 | Objetos centrais nunca definidos: `g_ℓ(k,a)`, `E_{ℓ,k}(a)`, `Ã_δ`, `x_ℓ^+`, `φ_0`; (?5) nunca enunciada; `ḡ_ℓ` usado em §3 e definido em §4 | média | fixed |
| C-011 | 2026-08-10 | Colisões de notação: `μ` (constante) contra `μ_ℓ`/`μ_r` (medida), com `μ_1` nos dois sentidos; `c_j` definido de dois modos; `u` em três sentidos | média | fixed |
| C-012 | 2026-08-10 | Multiplicidade mínima zero no custo central em todo nível computado falsifica a hipótese de `thm:microcanonical` e `prop:complex-deconditioning` nesses níveis, sem nenhuma ressalva junto aos teoremas | média | fixed |
| C-013 | 2026-08-10 | "delimit exactly how far local-limit methods reach" (Discussão e Introdução) contra "The linear-precision residue and Fourier problems remain open" (corpo) | média | fixed |
| C-014 | 2026-08-10 | `sec5-conjecture3-numerical/README.md` é byte-idêntico ao do `sec4`, e o título de ambos ainda é "§9.3", numeração do paper 01 | média | fixed |
| C-015 | 2026-08-10 | Treze números empíricos do paper não aparecem como resultado esperado em nenhum README do repositório | média | fixed |
| C-016 | 2026-08-10 | "certified ... error bounded by 10^{-8}" no abstract cobre a avaliação de φ, não as extrapolações (±0.015 sistemático) que de fato testam a Conjectura 3; "(stat)" em cálculo determinístico | média | fixed |
| C-017 | 2026-08-10 | Dois em dashes no corpo (linhas 91 e 632); Regra 3 pede zero | média | fixed |
| C-018 | 2026-08-10 | Regra 4b: orçamento de "X, not Y"/"rather than" estourado (≥8); "precisely", "decisive", "honest range"; título é tricolon | média | fixed |
| C-019 | 2026-08-10 | Frases cujo sujeito é o próprio paper em §2 e narração do processo interno do projeto no abstract, sem identificar a que se refere | média | fixed |
| C-020 | 2026-08-10 | Abstract, 1ª frase: "three conjectures about the base-3 analogue of the Fabius function"; só a Conjectura 3 é sobre φ | média | fixed |
| C-021 | 2026-08-10 | "imprecisely characterized in the literature that cites it" sem nenhuma citação; Lagarias, Dragičević et al. e Hafouta afirmados sem registro de leitura no projeto | média | fixed |
| C-029 | 2026-08-10 | A equação (5) é atribuída a `thm:ensemble-divergence` ("the theorem gives"); ela decorre de `thm:sublinear-precision-ensemble`, não de uma cota de entropia | média | fixed |
| C-030 | 2026-08-10 | Os dois passos estruturais que carregam §4 inteira (dobra dos expoentes pela ordem aplicável; bloco terminal determina o resíduo módulo `3^r`) são afirmados em uma frase cada, sem prova | média | fixed |
| C-031 | 2026-08-10 | `thm:quantile-diagnosis` reporta dados até ℓ=17 sem dizer que `thm:microcanonical-finite` só cobre suporte até ℓ=16 | alta | fixed |
| C-032 | 2026-08-10 | Parágrafo de composição do bucket inferior não normaliza pela taxa-base de inteiros pequenos; a razão observada/esperada é >1, oposto ao que o texto concluía | alta | fixed |
| C-033 | 2026-08-10 | Mecanismo do Remark ("bijeção sobre resíduo inteiro") não fecha o argumento; `a_old(j,a)` nunca definido | alta | fixed |
| C-034 | 2026-08-10 | Evidência de conjunto fixo só existe em `d=+5`; abstract generaliza para "through the levels tested" sem essa ressalva | alta | fixed |
| C-035 | 2026-08-10 | Ilustração do decaimento em `d=+12` usa quantil `q=1e-4`, que o próprio H-168 registra como contaminado por estatística de extremos em `ℓ` baixo, dentro de um parágrafo que alega imunidade a esse viés | média | fixed |
| C-036 | 2026-08-10 | Abstract/Discussão davam a entender que a leitura de "estatística de extremos" tinha sido descartada; o corpo é mais cauteloso | média | fixed |
| C-037 | 2026-08-10 | Citação específica ao teorema do companion paper (`in preparation`) sem hedge sobre verificabilidade externa | baixa | rejected (prática padrão citar um companion desta mesma linha; status "in preparation" já revelado na bibliografia; ver rodada abaixo) |
| C-038 | 2026-08-10 | "Eight levels, no trend" e depois "no deterioration at all" sobrestimam uma série cujos últimos quatro pontos caem a taxa comparável à decadência real alhures | baixa | fixed |
| C-039 | 2026-08-10 | Regra 12: os dois novos scripts que sustentam o Remark (fração exata de `m_ell`, assimetria de peso `S_ell`) ainda não estavam no repositório companheiro no momento da crítica | baixa | fixed |
| C-022 | 2026-08-10 | (?4) chamada de "target" da Conjectura 2 no abstract e na Discussão; na fonte é a hipótese, e (?3) é a conclusão | baixa | fixed |
| C-023 | 2026-08-10 | §3 descreve a janela da Conjectura 3 como `A_δ` inteira; (⋆5) é sobre `Ã_{δ_5}` e a fonte exige `δ_5 > δ` na implicação | baixa | fixed |
| C-024 | 2026-08-10 | Prefixo `thm:` nos quatro ambientes `empirical`; `\choose` de plain TeX em §3 contra `\binom` em §5 (aviso do amsmath) | baixa | fixed |
| C-025 | 2026-08-10 | Discussão chama (2) de "The support identity"; é identidade de massa | baixa | fixed |
| C-026 | 2026-08-10 | "The distances decrease over the computed levels" com um único nível exibido | baixa | fixed |
| C-027 | 2026-08-10 | `main-pt-br.tex` não existe (Regra 5) | baixa | rejected (mesma tensão de política dos papers 01/04/06, deixado para o pesquisador decidir; ver rodada abaixo) |
| C-028 | 2026-08-10 | `BarrierCompanion`, "in preparation" e sem URL, sustenta duas afirmações de conteúdo | baixa | fixed |

Rodadas abaixo (R1 em diante) usam o critério de convergência explícito do
pesquisador: 4 níveis (crítico/maior/moderado/menor, definições no prompt
da tarefa), parada em 3 rodadas consecutivas 100% limpas (crítico=0,
maior=0, moderado=0, menor<3), sem crédito parcial.

| ID | Rodada | Resumo | Severidade | Status |
|----|--------|--------|------------|--------|
| R1-01 | 2026-08-10 (R1) | `rem:no-monotone-certificate`: "Haar average of $S_\ell$ equals 1" é falso (9/7+12/7=3, não 2; média é 3/2) | crítico | fixed |
| R1-02 | 2026-08-10 (R1) | §5 não reproduzível: script parava em $\ell=300$ não 500, "60-digit" vs `mp.dps=100` real, nenhum código commitado calculava $L$/incerteza sistemática/dispersão | maior | fixed |
| R1-03 | 2026-08-10 (R1) | Déficit $\ell(2/3-L_\ell)\to0.580$ só vale em $u=0$; diverge como $\sqrt\ell$ fora do centro, mas o texto atribuía à janela inteira | maior | fixed |
| R1-04 | 2026-08-10 (R1) | `prop:complex-deconditioning`: "both hypotheses open at $k=\ell$ pela mesma razão" é falso para a 1ª hipótese (não depende de $k$, não é violada por multiplicidade zero) | maior | fixed |
| R1-05 | 2026-08-10 (R1) | Resumo diz "only a strong-convergence theorem"; corpo e Discussão dizem "two bridges" | maior | fixed |
| R1-06 | 2026-08-10 (R1) | `prop:fabius`: unicidade do ponto fixo requer $\int\varphi=1$, omitido | moderado | fixed |
| R1-07 | 2026-08-10 (R1) | `prop:fabius`: $f_n,f_1,f_0$ nunca definidos; cota deveria ser $f_\infty=\lambda\varphi$, não $\varphi$ | moderado | fixed |
| R1-08 | 2026-08-10 (R1) | $\varphi_0$ descrito como assintótica de solução da equação truncada satisfeita por $\varphi$; $\varphi$ satisfaz a equação não-truncada (7.9), não a truncada (7.10) | moderado | fixed |
| R1-09 | 2026-08-10 (R1) | `\cite[p.16]{Wirsching2003}` usa paginação da versão preliminar (18pp, PDF local), não da versão publicada DCDS | moderado | fixed |
| R1-10 | 2026-08-10 (R1) | Lacunas de autossuficiência: $\eta$ colide entre prova de `thm:wirsching-conj1` e §4; $\mu$ (constante de Wirsching) colide com $\mu_\ell$ (lei de Syracuse); $\delta_1$, $\bar g_\ell$/$\bar e_\ell$/$q_\ell$ usados em §3 antes de definidos; $S_\ell,S_\infty,\widehat u_\ell,D_\infty$ nunca definidos; $\phi_{m,\sigma^2}$ visualmente colide com $\varphi_0$ | moderado | fixed |
| R1-11 | 2026-08-10 (R1) | `rem:no-monotone-certificate` chama \eqref{eq:microcanonical} (identidade de massa) de "recursion"; a recursão real é a de §2, sem label | moderado | fixed |
| R1-12 | 2026-08-10 (R1) | "Interior of the window" (Discussão e `thm:quantile-diagnosis`) ambíguo com o interior literal de $|k-\ell|\le\delta\sqrt\ell$, que inclui $d=0$ | moderado | fixed |
| R1-13 | 2026-08-10 (R1) | Prova de `thm:wirsching-conj1`: estimativa de cauda enunciada em termos absolutos, deveria ser relativa a $\bar e_\ell(k)$; passo $\bar g_\ell\le\bar e_\ell$ omitido | moderado | fixed |
| R1-14 | 2026-08-10 (R1) | "of which only the first has since been settled" sugere resolução externa; a Conjectura 1 é resolvida por este próprio paper | moderado | fixed |
| R1-15 | 2026-08-10 (R1) | Título "Conjectures on the Base-3 Fabius Function" implica que as 3 conjecturas são sobre $\varphi$; só a 2 e a 3 são | moderado | fixed |
| R1-16 | 2026-08-10 (R1) | `\cite{Wirsching1998Urns}` citado diretamente para um conteúdo que só foi verificado via Wirsching (2003) §2, que credita [5] | moderado | fixed |
| R1-17 | 2026-08-10 (R1) | "Three facts... matter for what follows": o terceiro fato nunca é reusado no resto do paper | moderado | fixed |
| R1-18 | 2026-08-10 (R1) | Vocabulário banido residual: "a genuine convex combination" | menor | fixed |
| R1-19 | 2026-08-10 (R1) | Tricolons: lista de hipóteses de Dragičević/Hafouta; "increasing, concave, and uniform" | menor | fixed (a 2ª caiu como subproduto do fix de R1-03; a 1ª avaliada como conteúdo técnico genuíno, não decoração retórica, e mantida) |
| R1-20 | 2026-08-10 (R1) | Suposta família de auto-auditoria epistêmica banida em 5 frases de resultados empíricos | menor | rejected (nenhuma das frases usa as expressões literais da lista da Regra 4b; são frases de escopo exigidas pela Regra 10b, não meta-honestidade sobre o processo) |
| R1-21 | 2026-08-10 (R1) | Variância de comprimento de frase insuficiente na Discussão (só 1 frase <10 palavras em 9) | menor | fixed |
| R1-22 | 2026-08-10 (R1) | Fragmentos gramaticais: prova de `thm:sublinear-precision-ensemble` ("Since... while... ." sem oração principal); frase da Introdução difícil de pontuar | menor | fixed |
| R1-23 | 2026-08-10 (R1) | Repositório companheiro: título desatualizado no README raiz, README de sec5 chama Resultado Empírico de "the Theorem", travessões residuais em 4 READMEs, `(?3)` remanescente de extração de PDF | menor | fixed |
| R1-24 | 2026-08-10 (R1) | Resumo: "an exact equivalence-of-ensembles theorem" no singular para dois teoremas distintos | menor | fixed |

**Contagem da Rodada 1**: crítico=1, maior=4, moderado=12, menor=7. Não limpa. Contagem de rodadas limpas consecutivas: 0.

## Checagens que passaram, registradas para não serem refeitas

Contra a fonte primária (`literature/papers/132_Wirsching-2003-Positive-Predecessor-Density.pdf`,
lido diretamente nesta rodada, pp. 1-18, não pela nota):

- Quantificador de δ. Teorema 1 (p.5) e Conjectura 1 (p.8) são ambos
  "If there are real numbers δ, μ > 0 such that ...". A ressalva "with a
  possibly smaller central-limit window" em `thm:wirsching-conj1` é
  portanto inofensiva, e o teorema prova de fato a Conjectura 1. Não é
  achado.
- `A_δ` (1.5), a fórmula (1.4) de `ē_ℓ`, a recursão (2.1), `e_ℓ = p_ℓ * g_ℓ`
  (2.3), `ē_ℓ = p_ℓ * ḡ_ℓ` (2.4), as moedas `c_0 = 1`, `c_j = 2·3^{j-1}`
  (2.2): todos conferem com o que o main.tex usa.
- Enunciado literal de (⋆4) na p.14, com `χ_0 = 1_{[0,2/3]}` e
  `χ_1 = 1_{[1/3,1]}`: bate com o display de §2.
- `X = I_3 × Z_3^×`, `I_3 ≅ {0,1,2}^N`, `g̃_ℓ(x,a) = γ_ℓ g_ℓ(⌊3^ℓ x⌋, a)`
  com `γ_ℓ` independente de `a`, Teorema 3 (convergência forte, uniforme
  em famílias equicontínuas limitadas): conferem com pp. 9-11.
- O primeiro dos três achados de §2 está certo, e é o melhor material do
  paper: (5.1) diz literalmente que `(S_∞f)(x,a)` não depende de
  `a ∈ Z_3^×`. O segundo ((?2) e (?3) são a mesma desigualdade) confere
  com o Teorema 2 (p.10); o terceiro (Teorema 1 só consome `a ∈ N`)
  confere com o Teorema 1 (p.5) e com (1.2)/(1.3).
- `L_ℓ := 3^{1-ℓ} φ(3x_ℓ^+)/φ(x_ℓ^+)` é, via (7.7), exatamente o
  quociente `(2/3^{ℓ+1})·φ'(x_ℓ^+)/φ(x_ℓ^+)` de (7.5), e o valor 2/3 é
  (7.13). A matemática de §5 está correta; o defeito ali é só de
  exposição (C-010).

Álgebra conferida à mão:

- Prova da Conjectura 1: `Σ q_ℓ(k)z^k = Π(1-z^{c_j})/(1-z)`,
  `Σ p_ℓ(m)z^m = Π(1-z^{c_j})^{-1}`, cancelamento dando `(1-z)^{-(ℓ+1)}` e
  daí `ē_ℓ(k) = binom(k+ℓ,ℓ)/(2·3^{ℓ-1})`; razão binomial
  `≤ (k/(k+ℓ))^m`; a escolha `δ+η<δ_1` põe `j=k-m` na janela de (?2).
  Fecha. (O passo `ḡ_ℓ ≤ ē_ℓ`, usado implicitamente para comparar a
  cauda com `ē_ℓ(k)`, é imediato mas não está escrito.)
- `thm:microcanonical`: `Pr(J_i=j) = 2^{-(j+1)}/(1-2^{-c_i})` soma 1; o
  produto dá (2); o teto `k ≤ 3^ℓ-ℓ-1 = Σ(c_i-1)` confere;
  `E K_ℓ = ℓ+O(1)`, `Var = 2ℓ+O(1)`, `2Φ(δ/√2)-1`; a cadeia final fecha.
- `prop:complex-deconditioning`: a identidade (3) fecha por cancelamento
  e `Q̄_ℓ` é de fato a lei de `K_ℓ`.
- Identidade de redução de tampa
  `Σ_{j<C, j≡s (d)} 2^{-(j+1)}/(1-2^{-C}) = 2^{-(s+1)}/(1-2^{-d})`:
  confere. A divisibilidade `d | C` vale com o pareamento correto
  (`J_{ℓ-1-i}` reduzido módulo `2·3^{r-1-i}`) para todo `r ≤ ℓ`.
- `thm:linear-block-nonequivalence`: média e variância condicionais `ρu`
  e `2ρ(1-ρ)`; cruzamento em `|x| = √(-2(1-ρ)ln(1-ρ))`; a fórmula
  fechada para `u=0` recomputada dá 0.06934, 0.16608, 0.32272 para
  `ρ = 0.25, 0.5, 0.75`.
- `thm:ensemble-divergence`: dominação, `D_KL ≤ D_∞ ≤ -log Pr(K_ℓ=k)`, e
  `½log ℓ + O(1)` na janela central.
- `thm:microcanonical-fourier`: `min_a p/(1/(2·3^{ℓ-1})) ≥ 1 - (2/3)Σ|p̂-û|`
  é a inversão correta em `Z/3^ℓ`.
- `μ_1 = (1/3, 2/3)` sobre as unidades módulo 3 e `|μ̂_1| = 1/√3`.
- Recursão de momentos `M_i = (3^i-1)^{-1} Σ binom(i,k) (2^k/(k+1)) M_{i-k}`,
  derivada de `X = (2U+X')/3`.
- Os dois passos estruturais que o paper afirma sem provar (C-030) são
  verdadeiros. Da recursão (2.1), `a = (3a' + 1)·2^{-(j+1)}`, logo
  `a mod 3^r` fica determinado por `a' mod 3^{r-1}` e por `j` módulo a
  ordem de 2 em `(Z/3^r)^×`, que é `2·3^{r-1}`. Descendo, `a mod 3^r` é
  função de `(J_{ℓ-1} mod 2·3^{r-1}, …, J_{ℓ-r} mod 2·3^0)`: é o bloco
  terminal, e o emparelhamento correto é `J_{ℓ-1-i}` com tampa reduzida
  `2·3^{r-1-i}`, cuja divisibilidade `2·3^{r-1-i} | 2·3^{ℓ-1-i}` vale
  para todo `r ≤ ℓ`.
- Item 3 da tarefa: os quatro teoremas de ensembles são mutuamente
  consistentes. `thm:sublinear-precision-ensemble` prova, no caminho,
  proximidade em nível de bloco para `r = o(ℓ)`, e
  `thm:linear-block-nonequivalence` mostra falha em nível de bloco para
  `r ~ ρℓ`: são o mesmo objeto em regimes disjuntos, e portanto a
  afirmação de que `r = o(ℓ)` é nítida se sustenta.
  `thm:ensemble-divergence` é unilateral e não colide com nenhum dos
  outros. O corpo delimita isso corretamente; o abstract e a Discussão é
  que escorregam (C-001, C-002).
- Não há alegação, em nenhum lugar do paper, de ter fechado a Conjectura
  2. §5 e a Discussão dizem que continua aberta. O item 4 da tarefa
  passa.
- Bibliografia: 5 chaves `\cite`, 5 `\bibitem`, sem órfãos nas duas
  direções. Compila limpo, 9 páginas.

Repositório `collatz-wirsching-2003`, executado nesta rodada:

- Rodam: `check_generating_identity.py` (reporta `ok` para ℓ=2..12),
  `validate_canonical_decomposition.py`, `microcanonical_multiplicity.py`,
  `microcanonical_fourier.py`, `support_threshold.py`,
  `linear_block_tv.py`. `experiment_conjecture3.py` roda (validação
  interna passa, `M_1 = 1/2`, `M_2 = 7/24`, `φ(1/2) = 1.5`, e produz os
  níveis iniciais), mas não foi executado aqui até ℓ=500.
- `linear_block_tv.py` reproduz 0.0695, 0.1661, 0.3227, batendo com a
  fórmula fechada recomputada à mão.
- `support_threshold.py` em ℓ=10 dá `exact_first=15 = ℓ+5`, coerente com
  o que o paper afirma para 10 ≤ ℓ ≤ 16.
- Não roda: `fixed_precision_projection.py` (C-006).

---

## Rodada 2026-08-10 (primeira crítica; produtor: sessão da divisão do paper 01)

### C-001 (alta). O abstract promete uma não equivalência que o corpo nega

O abstract encadeia, na mesma frase: "an exact equivalence-of-ensembles
theorem at fixed and sublinear precision, a matching nonequivalence
theorem at linear precision". Os dois primeiros são sobre a projeção de
`p_{ℓ,k}` módulo `3^r`. O terceiro, `thm:linear-block-nonequivalence`, é
sobre o bloco terminal de custos, e o parágrafo logo abaixo dele diz o
contrário do que "matching" sugere:

> It does not prove nonequivalence after projection modulo `3^r`: the
> residue map can discard the block sum, and total variation can
> decrease under that projection. The linear-precision residue and
> Fourier problems remain open.

A Discussão acerta ("shows the latent cost vectors provably fail"). O
abstract é o único lugar onde a distinção some, que é exatamente o
padrão da Regra 8b.

### C-002 (alta). A Discussão inverte a direção de `thm:ensemble-divergence`

Discussão: "`thm:linear-block-nonequivalence` shows the latent cost
vectors provably fail to converge at linear precision, and
`thm:ensemble-divergence` shows why: the likelihood gap between the
microcanonical and canonical ensembles degrades only logarithmically, in
the direction opposite to what Conjecture 2 needs."

`thm:ensemble-divergence` é `p^{(r)}_{ℓ,k}(E) ≤ Pr(K_ℓ=k)^{-1} μ_r(E)`,
isto é, uma cota superior de `D_∞`. Uma cota superior na razão de
verossimilhança não explica não equivalência nenhuma. O corpo já diz
isso, três parágrafos acima:

> Theorem ... applies at full precision, but its direction is
> insufficient for condition (?3). ... the unresolved part is the lower
> tail of the likelihood ratio.

Ou a Discussão está errada, ou o parágrafo do corpo está. São
incompatíveis.

### C-003 (alta). (?1)-(?5) não existem em Wirsching (2003)

Wirsching escreve `(⋆1)` a `(⋆5)`, com estrela, em todo o artigo
(Teorema 1 p.5, Conjectura 1 p.8, Teorema 2 p.10, Conjectura 2 p.14,
Conjectura 3 p.17). O `?` é o que a extração de texto do PDF produz no
lugar da estrela, e foi para a nota de leitura
(`literature/notes/wirsching-2003-positive-predecessor-density.md`) e de
lá para o main.tex, onde aparece cerca de quinze vezes, inclusive na
tabela que o paper apresenta como transcrição direta da fonte. Num paper
cujo subtítulo é "A Corrected Reading", atribuir à fonte uma notação que
ela não usa é o pior lugar possível para esse defeito.

### C-004 (alta). `prop:fabius` é Wirsching sem citação

Comparação linha a linha:

| `prop:fabius` | Fonte |
|---|---|
| "unique `L^1([0,1])` fixed point of the averaging operator `W_3 f(x) := (3/2)∫_{3x-2}^{3x} f`" | Corolário 7, p.14, com `W_3` definido em (6.1), p.13 |
| "`C^∞`, piecewise polynomial away from the standard Cantor set" | Corolário 7: "φ is a `C^∞`-function which is a polynomial on each interval lying outside the classical Cantor set" |
| "`‖f_n-φ‖_1 ≤ 2^{-n+1}‖f_1-f_0‖_1`" | Corolário 8, p.14, literalmente a mesma constante |
| "`φ'(x) = (9/2)φ(3x)` on `[0,2/3]`" | (7.7), p.16 |

A proposição é numerada, não tem prova, e não tem uma única citação. O
único item que parece próprio é a representação `X = Σ 2U_j 3^{-j}`
(conferida aqui e correta). Como está, o texto lê como se os resultados
de Wirsching fossem folclore.

### C-005 (alta). Atribuições nominais sem fonte

§5: "a coefficient independently reproduced by Berg-Krüppel's own
asymptotic `φ_0`". `φ_0` é (7.11) de Wirsching, que remete a
"Berg, L., and Krüppel, M., *On the Solution of an Integral-Functional
Equation with a Parameter*, J. Anal. Appl. **17** (1998), 159-181"
(referência [1] da fonte). O main.tex nomeia os autores, usa o objeto
deles, e não tem `\bibitem` para eles. A nota de leitura registra esse
paper na lista "referências que o artigo usa e que ainda não foram lidas
aqui". Regra 11: afirmação sobre o que autores nomeados fizeram, baseada
em paráfrase de segunda mão.

Mesma forma, menor peso: "a member of the family of 'atomic functions'
of Rvachev" em `prop:fabius`, sem citação e sem aparecer na fonte.

### C-006 (alta). O Data Availability Statement é falso

`sec4-microcanonical-ensembles/fixed_precision_projection.py` carrega,
na linha 54:

```python
REPO / "sec10-l2-refutation-and-jensen" / "experiment_k_ell.py",
```

Essa pasta não existe em `collatz-wirsching-2003` (é do
`collatz-endogeny`, o repositório do paper 01). Executado aqui:

```
FileNotFoundError: [Errno 2] No such file or directory:
'.../collatz-wirsching-2003/sec10-l2-refutation-and-jensen/experiment_k_ell.py'
```

O script cai antes de calcular qualquer coisa. Ele sustenta
`thm:fixed-precision-ensemble`, `thm:sublinear-precision-ensemble`,
`thm:ensemble-divergence` e a Empirical `thm:fixed-precision-finite`,
segundo o próprio README da pasta. Duas afirmações caem junto:

- Data Availability: "Code and data reproducing every claim in this
  paper ... are at ...".
- README raiz do repositório: "Every script was re-run in this
  repository's own copy before being committed, not just copied."

Os outros sete scripts citados rodam.

### C-007 (média). A fonte oferece duas pontes, não uma

§2: "The only bridge offered between the two is Wirsching's Theorem 3,
strong convergence `S_ℓ → S_∞` on equicontinuous bounded families".

Página 14 da fonte, imediatamente antes do enunciado da Conjectura 2:

> The generators for Elka functions `g_ℓ(k,a)` are linked to the function
> φ of corollary 7 via the formula `lim_ℓ ∫_{Z_3^×} g̃_ℓ(x,a) da = φ(x)`
> for any fixed `x ∈ I_3`. This formula, together with the convergence
> of the transition operators `S_ℓ` proved in Theorem 3, suggest the
> following assertion: [Conjectura 2]

São duas. A segunda é a mais próxima do que o paper discute, porque liga
a média de Haar do gerador normalizado a φ. A crítica de fundo do paper
sobrevive (nem uma nem outra é uniforme em resolução crescente), mas a
frase como está é uma afirmação factual errada sobre a fonte, dentro do
parágrafo que o paper vende como leitura corrigida.

### C-008 (média). Definição das funções Elka

§2: "`e_ℓ(k,a) := |E_{ℓ,k}(a)|`, counting paths of length `k+ℓ` in the
Collatz graph ending at `a`".

Fonte, §1, p.3: `E_{ℓ,k}(a)` são os caminhos `b → ... → a` com `k`
aplicações de `T_0` e `ℓ` aplicações de `T_1`. Não é o conjunto dos
caminhos de comprimento `k+ℓ`; é o subconjunto com essa composição
específica. A distinção é o que dá sentido às duas variáveis e à janela
`|ℓ-k_ℓ| ≤ δ√ℓ`.

### C-009 (média). O que a prova de §3 realmente acrescenta

Dois dos três ingredientes já estão na fonte:

- `ē_ℓ(k) = binom(k+ℓ,k)/(2·3^{ℓ-1})` é a fórmula (1.4), p.4, dada de
  graça.
- `q_ℓ(k) = 2·3^{ℓ-1} ḡ_ℓ(k)` como contagem de distribuições em urnas de
  capacidade `c_j` está na p.8, citando Wirsching (1998), *Balls in
  constrained urns*.

O que é novo é a estimativa de cauda da convolução (o fator
`(k/(k+ℓ))^m` contra `exp(C log²(m+2))`) e a escolha `δ+η<δ_1`. Mas o
abstract diz "We prove the first of the three by a generating-function
cancellation", e a `rem:wirsching-conj1-source` diz "The proof above
supplies the generating-function cancellation and the convolution-tail
estimate", listando o cancelamento primeiro. A ênfase está no
ingrediente emprestado.

### C-010 (média). O paper não é autocontido

Nunca definidos no main.tex, todos load-bearing:

- `g_ℓ(k,a)`. A recursão (2.1) da fonte não aparece em lugar nenhum, e
  todo §3 e todo §4 dependem dela. Esse é o mesmo defeito que a crítica
  do paper 01 registrou como C-005; a divisão não o corrigiu.
- `E_{ℓ,k}(a)`, usado na única frase que define `e_ℓ`.
- `Ã_δ`, que aparece dentro do display de (?4).
- `x_ℓ^+`, em `thm:conjecture3`. Na fonte, `x_ℓ^+ := x_ℓ + 3^{-ℓ-1}` (p.16).
- `φ_0`, usado em §3 e em `thm:conjecture3`. Na fonte, (7.11).
- A condição (?5) nunca é enunciada, só descrita de passagem.
- `ḡ_ℓ` é usado na prova de §3 e definido em §4.

### C-011 (média). Colisões de notação

- `μ` é a constante de (?1), (?3) e (?4), e `μ_ℓ`, `μ_r` são a lei de
  Syracuse em §4. `μ_1` aparece nos dois sentidos: constante da fonte na
  Conjectura 1, medida no parágrafo do buraco de Fourier.
- `c_j` em §3 é `(1, 2, 6, 18, …)`; `c_i` em `thm:microcanonical` é
  `2·3^i`. É o mesmo conjunto de tampas reindexado, mas o leitor não tem
  como saber sem refazer a conta.
- `u` é o limite de `(k_ℓ-ℓ)/√ℓ` em `thm:linear-block-nonequivalence`, o
  parâmetro da janela em `thm:conjecture3`, e `û_ℓ` é a medida uniforme
  em `thm:microcanonical-fourier`.

### C-012 (média). Os dados do próprio paper contradizem as hipóteses dos teoremas

`thm:microcanonical` supõe `g_ℓ(k,a) ≥ η ḡ_ℓ(k)` para todo `a` e todo
`|k-ℓ| ≤ δ√ℓ`. `thm:microcanonical-finite` reporta que a multiplicidade
mínima é zero no custo central em todos os níveis calculados, e que o
primeiro custo que cobre todo resíduo é `ℓ+5` para `10 ≤ ℓ ≤ 16`.
Confirmado aqui rodando `microcanonical_multiplicity.py`:
`min_over_mean=0` em `k=ℓ` para todo `ℓ ≤ 9`.

Ou seja, a hipótese dos dois resultados condicionais de §4 é falsa em
`k=ℓ` em todo nível onde alguém já olhou. Isso não refuta nada
assintoticamente, e o resultado empírico diz corretamente "These values
neither prove nor refute". O problema é que nem `thm:microcanonical`,
nem `prop:complex-deconditioning`, nem a Discussão, nem o abstract
mencionam. O abstract diz que o teorema dá "a uniform lower bound on
every cylinder ... the estimate the weighted covering formulation ...
needs", sem sinal de que a hipótese é justamente onde os dados olham
mal.

Adjacente à pendência já rastreada no `OUTLINE.md` (H-167/H-168, a seção
sobre zeros de custo central que não entrou). Registro separado porque o
que falta aqui não é a seção: é uma ressalva de duas linhas junto aos
teoremas condicionais.

### C-013 (média). "exactly" em duas afirmações que o corpo desmente

Introdução: "the equivalence- and nonequivalence-of-ensembles theorems
that delimit exactly how much of the second conjecture's target is
reachable by local-limit methods."

Discussão: "they delimit exactly how far local-limit methods reach
toward Conjecture 2".

Corpo, logo após `thm:linear-block-nonequivalence`: "The linear-precision
residue and Fourier problems remain open." Os teoremas delimitam uma
família (equivalência em nível de bloco), e mesmo aí só nos vetores
latentes. Não é "exactly".

### C-014 (média). READMEs duplicados no repositório

`md5sum`:

```
ab99c886d4344ea3a9641c1ccc71775f  sec4-microcanonical-ensembles/README.md
ab99c886d4344ea3a9641c1ccc71775f  sec5-conjecture3-numerical/README.md
```

O mesmo arquivo nas duas pastas, com título "§9.3 - Wirsching's (2003)
Conjecture 3, and the microcanonical bridge to Tao's β=1", numeração de
seção do paper 01. O Data Availability promete "organized by section
with a README per subfolder", e o README raiz manda o leitor "enter the
folder, read the local README.md (more detailed)". Quem entrar em `sec5`
lê a documentação de `sec4`.

### C-015 (média). Números do paper ausentes do repositório

Aparecem no main.tex e em nenhum README como resultado esperado:
0.04024, 0.06228, 0.04310, 0.07902, 0.12677, 0.01885, 0.04003, 12.11,
293.29, 7.61, 122.63, 0.280, 0.00682.

Documentados: 0.02050, 0.11369, 0.25195, 0.339, 0.0246, 0.2735, 0.8074,
0.9973, 0.9194, 0.99999972, 0.0695, 0.1661, 0.3227, 0.580, 0.619, 0.538.

Provavelmente saem de rodar os scripts com outros argumentos, mas a
Regra 12 pede que um estranho ache a peça relevante a uma seção
específica, e metade dos números empíricos do paper não tem âncora.

### C-016 (média). O que o `10^{-8}` certifica

Abstract: "a certified numerical test of the third conjecture with error
bounded by `10^{-8}` through depth 500". O `10^{-8}` é o certificado da
avaliação de φ. O que testa a Conjectura 3 é a extrapolação de
`ln(φ/φ_0)` para `L = -0.619 ± 0.001 (stat)`, com "tail-shape systematic
uncertainty of ± 0.015" e ajuste `0.79/√ℓ`, e o corpo diz apenas
"consistent with a finite limit". A incerteza que importa é três ordens
de grandeza maior que a certificada, e não é certificada. Além disso,
"(stat)" rotula como estatística a dispersão de um cálculo
determinístico de precisão fixa. Regra 10b.

### C-017 (média). Em dashes

Linha 91: `i.i.d.\ uniform on $[0,1]$ --- the base-$3$ analogue`.
Linha 632: `$\ell\cdot(2/3-L_\ell) \to 0.580\pm 0.001$ --- a coefficient`.

Regra 3 pede zero, em qualquer lugar. (A ocorrência da linha 32 está
dentro de comentário LaTeX; ignorada.)

### C-018 (média). Regra 4b, itens mecânicos

- Antítese "X, not Y" e variantes, orçamento de duas por documento:
  linhas 66, 105, 130 ("rather than a paraphrase", três vezes, duas
  delas a menos de quarenta linhas uma da outra), 565, 606, 621, 651,
  662. Oito.
- Vocabulário banido: "precisely" (66), fora de uso técnico;
  "decisive" (629); "honest range" (638), que é a família de
  meta-honestidade, banida sem exceção. ("essential likelihood ratio",
  linha 532, é supremo essencial, uso técnico, não conta; "imprecisely"
  na linha 63 também não está na lista, embora a frase caia por outro
  motivo, ver C-021.)
- Título: "A Proof, a Corrected Reading, and a Certified Numerical Test"
  é o tricolon de três substantivos coordenados. "A Corrected Reading"
  ainda vende como contribuição o conserto de uma paráfrase que era
  interna a este projeto (ver C-021).

### C-019 (média). Frases sobre o próprio paper

- §2: "Three things become visible only by reading this chain directly
  rather than a paraphrase, and matter for what follows." Sujeito é o
  paper, e a frase dá instruções de leitura.
- Introdução: "reading the primary source rather than a paraphrase";
  §2: "reading [Wirsching] directly rather than a secondary paraphrase".
  Três vezes a mesma defesa do método em duas páginas.
- Abstract: "which explains why a previously proposed sufficient
  condition failed for a reason different from the one originally
  supposed". Narra o histórico interno do projeto (H-134 refutada por
  H-160 pelo motivo errado, corrigido por H-167/H-168) e nunca diz qual
  condição é. Um leitor externo não tem como decifrar.

### C-020 (média). Primeira frase do abstract

"Wirsching (2003) reduces uniform positive predecessor density for the
`3n+1` map to a chain of three conjectures about the base-3 analogue of
the Fabius function".

Só a Conjectura 3 é sobre φ. A Conjectura 1 é sobre `g_ℓ` e `e_ℓ`, e a
Conjectura 2 é sobre `W_3^ℓ χ_1 / W_3^ℓ χ_0`. A frase de abertura
descreve mal a fonte.

### C-021 (média). Afirmações sem verificação registrada

- Introdução: "the second ... has remained open and, we find, imprecisely
  characterized in the literature that cites it". Nenhuma citação
  sustenta "the literature that cites it". Pelo que a nota de leitura
  registra, a paráfrase imprecisa era a desta própria linha de pesquisa,
  não de terceiros. Ou o paper aponta a literatura, ou tira a frase.
- `rem:wirsching-conj1-source`: "The annotated Collatz bibliography also
  lists the three implications in that paper as conjectures". Não há
  nota de leitura, nem entrada em `literature/00-index.md`, para
  Lagarias, arXiv:math/0608208.
- `DragicevicEtAl2018` e `Hafouta2020`: o paper afirma hipóteses
  específicas ("a twisted operator cocycle acting on a fixed Banach
  space, a uniform spectral or Ruelle-Perron-Frobenius gap near zero, and
  an aperiodicity estimate away from zero") e imprime volume, páginas e
  DOI. Nenhum registro de leitura no projeto.

Nada disso é acusação de erro. É ausência de verificação, que é o que a
Regra 11 pede antes de imprimir.

### C-029 (média). A equação (5) não vem do teorema que a antecede

O parágrafo abre com "For `r = o(ℓ)` and `ξ_0 ∈ Z/3^r Z`, **the theorem
gives**", logo abaixo do parágrafo que discute
`thm:ensemble-divergence`, e o "the theorem" só pode ser lido como
aquele. Mas `thm:ensemble-divergence` dá `D_KL ≤ ½ log ℓ + O(1)`, uma
cota de entropia que não implica convergência de coeficiente de Fourier
individual. A equação (5) decorre de `thm:sublinear-precision-ensemble`,
que é justamente o teorema que dá distância de variação total `o(1)` em
precisão `r = o(ℓ)`. Trocar o nome do teorema resolve.

### C-030 (média). Os dois passos estruturais de §4 não são provados

Toda a §4 depende de dois fatos sobre a recursão de Wirsching, cada um
afirmado numa frase:

1. Prova de `thm:microcanonical`: "Folding each exponent independently by
   the applicable order leaves the Syracuse residue unchanged. Wirsching's
   recursion for `g_ℓ` counts the folded vectors with `Σ_i J_i = k`." O
   emparelhamento do índice `i` com a tampa `c_i = 2·3^i` (a ordem de 2
   módulo `3^{i+1}`) é o passo que faz (2) valer, e nada justifica que
   seja esse emparelhamento e não outro.
2. Prova de `thm:fixed-precision-ensemble`: "The terminal `r` folded
   costs determine the final residue modulo `3^r`." Contraintuitivo à
   primeira leitura (o leitor esperaria os `r` primeiros, os de tampa
   pequena) e nunca demonstrado.

Ambos foram conferidos aqui e são verdadeiros (ver "checagens que
passaram"). O defeito é que o leitor não tem como conferir: `g_ℓ` nunca
é definido (C-010), então nem sequer há objeto contra o qual verificar.
Duas ou três linhas explicitando `a = (3a'+1)·2^{-(j+1)}` resolvem as
duas de uma vez.

### C-022 (baixa). (?4) é hipótese, não alvo

Conjectura 2, p.14: "If there are real numbers δ, μ > 0 such that (⋆4)
..., then condition (⋆3) of Theorem 2 is fulfilled." O alvo é (⋆3); (⋆4)
é o que se supõe. Abstract ("its target, a pointwise bound on a
one-dimensional averaging operator") e Discussão ("Conjecture 2's own
target, condition (?4)") invertem. A crítica do paper é justamente que
(⋆4) é fraca demais como hipótese, o que fica ilegível quando (⋆4) é
chamada de alvo.

### C-023 (baixa). Janela da Conjectura 3

Fim de §3: "Conjecture 3, an asymptotic assertion on `φ(z_ℓ)/φ_0(z_ℓ)`
along the central-limit window `|ℓ-k_ℓ| ≤ δ√ℓ`". (⋆5) é sobre sequências
reais `(z_ℓ) ∈ Ã_{δ_5}`, não sobre a classe inteira `A_δ`. E a fonte
exige `δ_5 > δ` na implicação (⋆5) ⇒ (⋆4) (p.17, logo antes de (7.14)),
condição que nem §3 nem §5 mencionam, embora o teste numérico se
descreva como rodando "in the CLT window".

### C-024 (baixa). Rótulos e macros

Os quatro `empirical` (`thm:conjecture3`, `thm:fixed-precision-finite`,
`thm:microcanonical-finite`, `thm:microcanonical-fourier`) usam o
ambiente certo, e no PDF saem como "Empirical Result", o que atende a
Regra 10b. Só que o label começa com `thm:`, o que engana quem lê o
fonte ou um `\ref` fora de contexto.

§3 usa `{k+\ell\choose\ell}` (plain TeX), o que dispara
`Package amsmath Warning: Foreign command \atopwithdelims`; §5 usa
`\binom`.

### C-025 (baixa). "The support identity"

A Discussão chama a equação (2) de "The support identity". (2) é a
decomposição da massa de `μ_ℓ(a)` em custos; não diz nada sobre suporte.
Suporte é assunto de `thm:microcanonical-finite`.

### C-026 (baixa). Uma tendência com um ponto

`thm:fixed-precision-finite`: "The distances decrease over the computed
levels." Os dados exibidos são ℓ=12 (r=1,2,3) e ℓ=13 (r=1 e precisão
total). Para r=2 e r=3 há um nível só. O leitor não tem como ver queda
nenhuma.

### C-027 (baixa). Regra 5

Não existe `main-pt-br.tex`. O `OUTLINE.md` registra como "só sob pedido
explícito", mas a Regra 5 não é condicional: todo paper sai em inglês e
na língua do pesquisador, mantidos em sincronia.

### C-028 (baixa). `BarrierCompanion`

Citado duas vezes para conteúdo, não para contexto: "the estimate the
weighted covering formulation of the endogeny-barrier literature needs"
e "The conjectural weighted-covering estimate gives only a subexponential
lower bound for this factor". A entrada é "companion paper, in
preparation", sem URL, DOI ou arXiv. Um leitor não tem como checar
nenhuma das duas.

## Rodada 2026-08-10 (produtor): correções aplicadas

29 de 30 entradas fixed, 1 rejected (C-027). Cada achado foi verificado
contra a fonte primária ou o repositório antes de qualquer correção
(Regra 8c); dois erros próprios entraram e foram pegos no processo, ver
abaixo.

**Altas.** C-006 (Regra 12, urgente): `fixed_precision_projection.py`
importava `sec10-l2-refutation-and-jensen/experiment_k_ell.py` de um
repositório que não é este; copiado para
`syracuse_recursion.py` nesta mesma pasta, import corrigido, script
re-executado (`ell=3..13`, `r=1..13`) e os números batem exatamente
com os do paper. C-003: as 30 ocorrências de `(?N)` trocadas por
`(\star N)` por `sed` de string fixa (confirmado: todas dentro de modo
matemático, nenhuma precisou de `$` extra). C-004: `prop:fabius`
ganhou título com atribuição explícita ("Wirsching 2003, Corollaries 7
and 8") e três `\cite` inline; a alegação não verificada sobre
"funções atômicas de Rvachev" foi cortada (é verdadeira, confirmada via
busca, mas nenhuma citação própria estava disponível para o texto
específico usado). C-005: `\bibitem` novo para Berg-Krüppel (Z. Anal.
Anw. 17 (1998), 159-181, confirmado direto na página do editor) e para
Wirsching (1998) "Balls in constrained urns" (idem, 979-996). C-001,
C-002: abstract reescrito por completo (não apenas a frase apontada),
removendo a alegação de "matching nonequivalence" e trazendo a mesma
leitura do corpo; Discussão corrigida para não atribuir a
`thm:ensemble-divergence` uma explicação que ele não dá (é cota
superior de um lado só).

**Médias.** C-007: a frase "the only bridge" agora lista as duas
pontes que a fonte de fato oferece (a identidade `lim ∫ g̃_ℓ da = φ`,
confirmada na p.14, e o Teorema 3), confirmado por leitura direta das
pp.14-17 do PDF. C-008: `E_{\ell,k}(a)` redefinido como "k vezes
$T=T_0$, $\ell$ vezes $T=T_1$", citando a p.3. C-009: o remark de
atribuição agora lista primeiro o que a fonte já dá (identidades
geradoras, fórmula (1.4), interpretação de urnas) e só depois o que é
novo (estimativa de cauda, janela `δ+η<δ_1`). C-010: bloco definicional
novo em §2 cobre `g_ℓ(k,a)` (recursão (2.1) completa), `E_{\ell,k}(a)`,
`A_δ`/`Ã_δ`, `φ_0`; `x_ℓ^+` e `(\star5)` definidos explicitamente no
início de §5, com a constante `x_\ell^+ := x_\ell+3^{-\ell-1}`
confirmada na p.16 do PDF diretamente (não só na nota de leitura).
**Erro próprio pego em revisão**: a primeira tentativa de definir a
sequência testada em §5 inventou "a constant sequence $x_\ell=1/3$";
checado contra `experiment_conjecture3.py` (`sample_points`), a
sequência real é `x_\ell=k_\ell/3^\ell` com `k_\ell=\ell+round(u\sqrt\ell)`
para `u` em `{-2,...,2}`; corrigido antes de prosseguir. Também a
primeira tentativa de citar a fonte de `φ_0` inventou "Wirsching's
Corollary 3"; a nota de leitura já confirmada dizia (7.11); corrigido
para a equação certa. C-011: pior colisão (`μ_1` usado tanto para a
constante de Wirsching quanto para a medida de Syracuse) não existe
mais no texto atual, checado por grep; `c_j`/`c_i` agora tem uma frase
de reindexação explícita. C-012: os dois resultados condicionais
(`thm:microcanonical`, `prop:complex-deconditioning`) ganharam uma
frase cada apontando que a hipótese é falsa em `k=\ell` em todo nível
computado. C-013: linguagem de "exactly"/"delimit exactly" suavizada
em três lugares (Introdução, Discussão ×1) para "bound"/sem advérbio.
C-014, C-015: READMEs de `sec4`/`sec5` (inglês e PT-BR, quatro arquivos)
divididos de verdade em vez de duplicados; treze números antes ausentes
adicionados como resultado esperado, cada um re-executado e conferido
($\ell=12,13$; central e janela superior; `r=1,2,3` e precisão total).
C-016: "(stat)" removido, `10^{-8}` agora explicitamente restrito à
avaliação de `φ`, não à extrapolação. C-018: título trocou "A
Corrected Reading" por "A Microcanonical Decomposition" (a versão
antiga vendia como achado o conserto de uma leitura interna deste
projeto, não da literatura); antíteses "X, not Y" caíram de ≥8 para 2,
ambas dentro do orçamento da Regra 4b. C-019: as três instâncias de
"reading ... rather than a paraphrase" cortadas; narração do histórico
interno do projeto no abstract removida junto com a reescrita de
C-001. C-020: primeira frase do abstract reescrita para não atribuir
as três conjecturas a `φ`. C-021: a alegação sobre "the literature
that cites it" cortada (não verificável: tentei checar a bibliografia
anotada de Lagarias via arXiv, o PDF não é extraível por essa via, e
sem verificação não fica); `LagariasBibliographyII` removido da
bibliografia por ficar sem uso. Dragičević et al. e Hafouta conferidos
bibliograficamente (autor/título/volume/páginas/DOI batem via busca
direta); o conteúdo técnico específico das hipóteses não foi
re-verificado a fundo, mas a identidade da citação está correta.
C-029: "the theorem gives" agora nomeia
`thm:sublinear-precision-ensemble` explicitamente. C-030: as duas
passagens de uma frase só (dobra de expoentes; bloco terminal)
ganharam a justificativa algébrica de duas linhas que a rodada
anterior já tinha conferido à mão.

**Baixas.** C-017: os dois em dashes restantes couberam nas mesmas
edições de C-004/C-016. C-022: "(\star4)" corrigido de "target" para
"hypothesis" na mesma edição de C-002. C-023: `(\star5)` agora
enunciada com a classe `Ã_{δ_5}` certa e a exigência `δ_5>δ`
explícita, confirmada na p.17 do PDF (`(7.14)`, "for `δ_5 > δ`").
C-024: `{k+\ell\choose\ell}` (plain TeX) trocado por `\binom{k+\ell}{\ell}`
nos dois lugares de §3; o prefixo `thm:` nos quatro ambientes
`empirical` foi deixado como está (mesma decisão que C-017 do paper
01: não afeta o PDF, renomear é risco desproporcional ao ganho). C-025:
"support identity" virou "mass decomposition". C-026: a alegação de
tendência agora cita o intervalo real testado (`\ell=3,\ldots,13`),
verificado rodando o script no intervalo completo, não só o ponto
`\ell=12` exibido no texto. C-028: `BarrierCompanion` ganhou URL do
repositório `collatz-endogeny`.

**Rejected, tensão registrada**: C-027, `main-pt-br.tex` não existe. A Regra 5 não
é condicional, mas traduzir um paper técnico de 10 páginas é trabalho
substancial, e o `OUTLINE.md` registra uma política interna ("só sob
pedido explícito") que conflita com a letra da regra. Decidi não fazer
uma tradução apressada só para fechar a linha da tabela (o risco de
uma tradução malfeita, fora de sincronia, é pior que não ter
nenhuma); levar a tensão de volta ao pesquisador em vez de resolvê-la
sozinho.

Paper recompilado limpo (10 páginas, sem refs/citações órfãs).

## Rodada 2026-08-10 (redação final): material novo de H-168/H-171

Pedido do diretor científico: avançar para redação final (Regra 5) nos
4 papers. Nesta linha, o pedido incluiu conferir se o material fechado
nesta mesma sessão sob H-168 (`closed-inconclusive`) e H-171
(`closed-confirmed`) já aparecia no corpo do paper (não aparecia) e, se
pertinente, incorporá-lo. É pertinente: a pergunta de H-168 é
exatamente a hipótese em aberto de `thm:microcanonical`
(`g_ℓ(k,a) ≥ η ḡ_ℓ(k)`). Produzi um novo Empirical Result
(`thm:quantile-diagnosis`) e um novo Remark
(`rem:no-monotone-certificate`) em §4, mais ajustes correspondentes no
abstract, introdução e Discussão. Antes de qualquer commit, rodei uma
crítica adversarial de contexto fresco (subagente Opus, esforço
máximo, Regra 8/15) só sobre esse material novo mais o abstract, que
achou quatro problemas de severidade alta (C-031 a C-034) e cinco de
severidade média/baixa (C-035 a C-039).

**C-033, o achado mais sério**: a explicação original do Remark
("bijeção sobre o resíduo inteiro em `ℓ-1`, incluindo múltiplos de
3") não fechava o argumento e nunca definia `a_old(j,a)`. Verificação
independente mostrou que essa explicação estava errada: `g_ℓ(k,b) = 0`
para todo `b` múltiplo de 3 (decorre diretamente da recursão, o alvo
nunca é congruente a 0 mod 3), então a soma sobre resíduos inteiros
coincide exatamente com a soma sobre unidades, sem discrepância
nenhuma ali. O mecanismo certo (rederivado do zero, verificado por
script novo, `exact_weight_asymmetry.py` em
`collatz-wirsching-2003/sec4-.../`) é outro: a admissibilidade de `j`
para um `a` fixo depende só de `a mod 3` (a condição
`2^(j+1)a ≡ 1 mod 3` fixa a paridade de `j`), então o peso
`S_ell(k,a) := Σ_j ḡ_{ell-1}(k-j)/ḡ_ell(k)` sobre os `j` admissíveis só
pode assumir dois valores por nível (um por classe de `a mod 3`), e
nenhum dos dois vale 1 nos casos testados (`S_3(3,·) = 9/7, 12/7`;
`S_4(4,·) = 6/5, 9/5`; `S_4(5,·) = 5/4, 7/4`). Isso também corrigiu,
de passagem, uma lista de seis valores que o escalonamento original a
Codex (documentado em H-168) tinha citado para `S_3(3,a)`: só os dois
primeiros (`9/7`, `12/7`) sobrevivem à rederivação; os quatro
restantes exigiam quatro valores distintos dentro de só duas classes
de `a mod 3`, o que a fórmula não permite. Documentado como correção
em `hypotheses/H-168-...md` (Regra 8c) e no README do experimento.

**C-032, a composição do bucket inferior removida**: o parágrafo
original (herdado quase literalmente da nota de H-168) dizia que o
bucket inferior populacional era "quase inteiramente" resíduos novos,
não `a` fixo piorando, usando a fração bruta de resíduos pequenos no
bucket. O crítico apontou que essa fração não estava normalizada pela
taxa-base de inteiros pequenos na população total, que também cai (e
mais rápido). Recalculei a taxa-base à mão: cai de `1/3` (ℓ=9) para
`~1{,}5×10^{-4}` (ℓ=16), contra uma fração observada no bucket de
`0{,}5` a `0{,}0002`-`0{,}0008`, uma razão observada/esperada de
`1{,}3×` a `5{,}2×`, ou seja sobre-representação, não neutralidade.
Os números absolutos envolvidos são pequenos o bastante (contagens de
2 a 7 resíduos pequenos por bucket) que essa razão é compatível com
ruído de Poisson em torno de uma média esperada de ~4, não uma
correção limpa em nenhuma direção; a leitura honesta é "inconclusivo
com esse teste", não "confirma resíduos novos". Cortei o parágrafo
inteiro em vez de reescrevê-lo fraco, e reescopei a conclusão do
Empirical Result e do abstract para não generalizar além do que o
teste exaustivo de conjunto fixo (que só cobre `d=+5`) realmente
sustenta (C-034).

**C-031, C-035, C-036, C-038**: correções mecânicas, mais estreitas.
Uma frase nova explicita que a série de conjunto fixo em `ℓ=17` é uma
extensão de um nível além do que `thm:microcanonical-finite` relata
para o cálculo de suporte. A ilustração do decaimento em `d=+12`
trocou de `q=10^{-4}` (que H-168 já registrava como contaminado por
estatística de extremos em `ℓ` baixo) para `q=10^{-3}` (mesmo quantil
usado no resto do parágrafo, sem essa contaminação), com os números
recomputados diretamente do log primário. Abstract e Discussão
reescritos para não sugerir que a hipótese de "estatística de
extremos" foi descartada de forma limpa; ela sobrevive parcialmente
(no limite de suporte `d=+5`) e falha no interior da janela, sem que
isso resolva se a causa é algum `a` fixo piorando. "Eight levels, no
trend" ganhou justificativa (inclinação por mínimos quadrados uma
ordem de grandeza abaixo da dispersão da própria série) e a frase
categórica "no deterioration at all" foi cortada.

**C-037, rejected**: citar o teorema específico do companion paper
(`\cite{BarrierCompanion}`), já listado como "in preparation" na
bibliografia, é prática padrão para um companion desta mesma linha de
pesquisa; o status de verificabilidade já está exposto ao leitor pela
entrada da bibliografia, e não pareceu justificar um hedge adicional
no corpo do texto.

**C-039**: os dois scripts novos (`exact_min_ratio.py`,
`exact_weight_asymmetry.py`) e seus logs foram commitados e
empurrados em `collatz-wirsching-2003` antes deste commit no paper,
com o README do experimento atualizado para apontar para eles e para
registrar a correção de C-033.

Depois das correções: reconferi abstract, introdução e Discussão
contra o corpo final (Regra 8b), recompilei (`pdflatex` ×2, limpo, sem
`undefined reference`) e reconferi `\cite`/`\bibitem`/`\ref`/`\label`
(script Python, sem órfãos em nenhuma direção). Todas as entradas
C-031 a C-039 fecham nesta mesma rodada; nenhuma ficou `open`.

---

## Rodada de convergência R1, 2026-08-10

Pedido do pesquisador: loop de crítica adversarial até 3 rodadas
consecutivas limpas por um critério de 4 níveis (crítico/maior/
moderado/menor), sem crédito parcial, contexto fresco a cada rodada.
Subagente crítico: `Agent` síncrono, modelo `opus`, esforço máximo,
sem acesso ao histórico deste arquivo além do que foi colado no
prompt (achados anteriores C-001 a C-039, todos fechados).

**Achados**: crítico=1, maior=4, moderado=12, menor=7 (tabela acima,
R1-01 a R1-24). Não limpa; contagem de rodadas limpas consecutivas
volta a 0.

**O achado mais sério (R1-01)**: a explicação do
`rem:no-monotone-certificate` afirmava que a média de Haar de
$S_\ell(k,\cdot)$ era 1; os próprios números impressos duas linhas
acima ($9/7$ e $12/7$) somam 3, não 2, logo a média é $3/2$. Verificado
à mão e rodando `exact_weight_asymmetry.py` do repositório. A
conclusão do remark (o contraexemplo de não monotonicidade) permanece
correta; só a frase de explicação estava errada. Reescrita para não
alegar que o mecanismo de combinação convexa "sobrevive para vetores
de probabilidade somados", já que nem isso é verdade.

**O achado mais trabalhoso (R1-02/R1-03)**: nada no repositório
`collatz-wirsching-2003` reproduzia a alegação central da §5
(profundidade $\ell=500$, coeficiente $L=-0.619\pm0.001$, incerteza
sistemática $\pm0.015$, dispersão em $u$, ausência de modulação
log-periódica): o script commitado parava em $\ell=300$ e não continha
nenhum código de ajuste. Em vez de reduzir a alegação do paper para o
que já existia, estendi `experiment_conjecture3.py` de verdade
(`ELL_LIST` até $\ell=500$, `N_MAX=510`) e rodei a computação completa
(momentos exatos até grau 510: ~332s; sweep completo: ~405s). Os
números resultantes confirmam parte do que já estava escrito
($L\approx-0.619$, $c\approx0.539$) mas refutam duas alegações
específicas: (1) o déficit $\ell(2/3-L_\ell)\to0.580$ só converge em
$u=0$; nos outros seis valores de $u$ testados ele diverge como
$\sqrt\ell$ (de $-32.4$ a $+28.1$ em $\ell=500$), então "measured...
in the CLT window ($u\in[-2,2]$)" atribuía à janela inteira algo que só
vale no centro. (2) A incerteza sistemática de $\pm0.015$ nunca esteve
em nenhum script commitado; o bracket que de fato calculei (ajuste só
com $\ell\ge350$, e um modelo alternativo com termo extra $1/\ell$)
dá uma sensibilidade real de $2\times10^{-4}$, quase duas ordens de
grandeza menor. Troquei o $\pm0.015$ não verificável pelo número que
realmente meço, e cortei a alegação "no log-periodic modulation is
detected" (nunca testada com rigor, só 7 pontos, insuficiente para
qualquer teste de periodicidade). A dispersão de $\ln(\varphi/\varphi_0)$
em $u$ ($<10^{-4}$), por outro lado, se confirmou genuína
($6\times10^{-5}$ em $\ell=500$) e ficou mantida. Script, README (raiz
e `sec5-conjecture3-numerical/`) e `main.tex` foram todos sincronizados
com os números reais.

**Achados moderados/menores**: lacunas de autossuficiência ($\eta$
colidindo entre duas seções, $\mu$ colidindo com $\mu_\ell$, `S_\ell`,
`D_\infty`, `\hat u_\ell` nunca definidos), uma citação de página que
apontava para a paginação da versão preliminar do PDF em vez da versão
publicada (trocada por referência de seção), atribuição de conteúdo a
`Wirsching1998Urns` via paráfrase de segunda mão (corrigida para citar
via Wirsching 2003 §2, que foi lido diretamente), e uma leitura
incorreta da equação truncada de Berg-Krüppel (§7 da fonte, conferida
diretamente no PDF): $\varphi$ satisfaz a equação não truncada (7.9),
não a truncada (7.10) que $\varphi_0$ resolve. Todos verificados contra
a fonte primária ou o repositório antes de corrigir (Regra 8c).

**Um achado rejeitado (R1-20)**: o crítico classificou 5 frases de
resultados empíricos ("this finite test checks the implementation and
is not used in the proof", etc.) como pertencentes à família banida de
meta-honestidade da Regra 4b. Verificação: nenhuma das frases usa
qualquer expressão da lista literal da regra ("honestly", "we are
careful to", etc.); são frases de escopo em terceira pessoa sobre o
que um resultado empírico mostra ou não mostra, exigidas pela Regra
10b e pela própria Regra 4b ("Concentrate the uncertainty... rather
than a qualifier in every paragraph"). Mantidas como estão.

Depois das correções: recompilado (`pdflatex` ×2, 12 páginas, sem
`undefined reference`, dois avisos cosméticos de `Overfull \hbox` nos
títulos em negrito de dois ambientes, sem overflow visível checado
página por página em render de 100dpi); `\cite`/`\bibitem` sem
órfãos; zero em/en dashes; vocabulário banido da Regra 4b varrido
mecanicamente, zero ocorrências fora de uso técnico; antíteses "X, not
Y" em 2/2. Repositório `collatz-wirsching-2003` sincronizado: script
de §5 estendido e re-executado do zero, READMEs de `sec3`, `sec4`
(microcanonical) e `sec5` corrigidos (travessões, título desatualizado,
"the Theorem" para "Empirical Result", numeração `§9.2` obsoleta).
PT-BR não tocado (instrução da tarefa).

---

## Rodada de convergência R2, 2026-08-11

Segunda rodada do loop, contexto totalmente fresco (subagente `opus`,
esforço máximo, sem acesso a este arquivo além do resumo colado no
prompt). Regra: 3 rodadas consecutivas limpas (crítico=0, maior=0,
moderado=0, menor<3), sem crédito parcial; R1 não foi limpa, então a
contagem começou em 0.

**Achados**: crítico=2, maior=3, moderado=11, menor=7. Não limpa;
contagem de rodadas limpas consecutivas permanece 0.

| ID | Rodada | Resumo | Severidade | Status |
|----|--------|--------|------------|--------|
| R2-01 | 2026-08-11 (R2) | Prova de `thm:wirsching-conj1`: a desigualdade da janela estava invertida ("$\delta+\tau<\delta_1$", implicando $\delta_1>\delta$, contra o próprio enunciado "$\delta_1\le\delta$"); correta é $\delta_1+\tau<\delta$ | crítico | fixed |
| R2-02 | 2026-08-11 (R2) | Script de §5 calculava em $x_\ell$, não $x_\ell^+$ como o paper define $L_\ell$; o déficit real em $x_\ell^+$ é $\approx0.802$, não $0.580$ | crítico | fixed |
| R2-03 | 2026-08-11 (R2) | Sensibilidade do ajuste de $L$ ao modelo alternativo é $4\times10^{-4}$ (script imprime "0.0004"), não $2\times10^{-4}$ como escrito | maior | fixed |
| R2-04 | 2026-08-11 (R2) | "$10^{-8}$" no abstract e corpo não é produzido por nenhuma computação; é a tolerância do `assert` de validação de $\varphi(1/2)$, não das avaliações em $\ell=500$ | maior | fixed |
| R2-05 | 2026-08-11 (R2) | "coefficient matching the asymptotic $\varphi_0$" não verificado; nenhum script calcula o lado $\varphi_0$ do déficit | maior | fixed |
| R2-06 | 2026-08-11 (R2) | Ambiguidade sobre qual recursão cobre qual faixa de $\ell$ (multiplicidade exata até 12, suporte booleano até 16, uma terceira recursão restrita a conjunto fixo até 17, esta última descrita erradamente como "a mesma" da primeira) | moderado | fixed |
| R2-07 | 2026-08-11 (R2) | "immune to the set-size confound by construction" superestimava o que o quantil fixo realmente garante (só imune à estatística de extremos, não à mudança de composição) | moderado | fixed |
| R2-08 | 2026-08-11 (R2) | Colisões de notação: $S_\ell$ (operador de Wirsching) vs $S_{\ell,r}$ (soma de bloco, idêntica a $B_{\ell,r}$ já definida alhures) vs $S_\ell(k,a)$ (soma de coeficientes do Remark); $A_\delta$ (classe de sequências) vs $A_i$ (variável geométrica local) | moderado | fixed |
| R2-09 | 2026-08-11 (R2) | "Syracuse law/measure" central a §4, usado 10+ vezes, nunca definido nem atribuído a Tao | moderado | fixed |
| R2-10 | 2026-08-11 (R2) | Argumento de não aproximação a Haar exibia só o coeficiente de Fourier de $\mu_1$ (1/√3), sem o valor de comparação da lei uniforme sobre unidades (1/2) | moderado | fixed |
| R2-11 | 2026-08-11 (R2) | `prop:complex-deconditioning`: a primeira hipótese é exatamente a conclusão do `thm:microcanonical` (via $G_{\ell,a}(1/2)/\bar G_\ell(1/2)=2\cdot3^{\ell-1}\mu_\ell(a)$), não um insumo independente; não sinalizado | moderado | fixed |
| R2-12 | 2026-08-11 (R2) | Teorema 3 do Wirsching citado como §4 da fonte; está no §5 (§4 só define $S_\ell$) | moderado | fixed |
| R2-13/14 | 2026-08-11 (R2) | "the conjectural weighted-covering estimate" e "predicted value 2/3" usados sem definição/derivação no ponto de uso | moderado | fixed |
| R2-15 | 2026-08-11 (R2) | `thm:fixed-precision-finite` e `thm:microcanonical-fourier` nunca referenciados via `\ref` na prosa | moderado | fixed |
| R2-16 | 2026-08-11 (R2) | `rem:wirsching-conj1-source` repetia a desigualdade invertida de R2-01 com o símbolo errado ($\eta$ em vez de $\tau$) | moderado | fixed (junto com R2-01) |
| R2-17/18 | 2026-08-11 (R2) | Orçamento de antítese "X, not Y" e tricolons: recontagem usando só os padrões literais da Regra 4b (ver nota abaixo) | menor | fixed |
| R2-19 | 2026-08-11 (R2) | Abstract: "across fit sub-ranges and tail models" descrevia mal o que foi testado; "interior offset" ambíguo (mesmo padrão de R1-12) | menor | fixed |
| R2-20 | 2026-08-11 (R2) | `thm:linear-block-nonequivalence`: "holds without the $o(1)$" pouco claro sobre o que contrasta | menor | fixed |
| R2-21 | 2026-08-11 (R2) | Suporte de $\Gamma_i$ (a variável geométrica local) não enunciado ($m\ge1$) | menor | fixed |
| R2-22 | 2026-08-11 (R2) | Cabeçalho de `prop:fabius` atribuía a Wirsching (Corollaries 7-8) a identificação com a função de Fabius, que não está na fonte | menor | fixed |
| R2-23 | 2026-08-11 (R2) | "well above the extreme order statistic too" ambíguo, repetido 2x | menor | fixed |

**Os dois achados críticos**, ambos verificados de forma independente
antes de corrigir (Regra 8c) e ambos confirmados corretos:

**R2-01**: refiz a álgebra da prova de `thm:wirsching-conj1`. Para $k$
na janela de $(\star1)$ (raio $\delta_1$) e $0\le m<\tau\sqrt\ell$,
$|k-m-\ell|\le(\delta_1+\tau)\sqrt\ell$; para isso caber na janela de
$(\star2)$ (raio $\delta$), precisa-se de $\delta_1+\tau<\delta$, não
$\delta+\tau<\delta_1$ (que implicaria $\delta_1>\delta$, o oposto do
que o próprio enunciado do teorema diz, "raio possivelmente menor").
Erro de escrita puro (o teorema é verdadeiro, a prova só tinha a
desigualdade de cabeça para baixo); corrigido em três lugares
(enunciado do teorema, que agora nomeia $\delta_1$ explicitamente; a
prova; o Remark que repetia a mesma desigualdade com o símbolo errado).

**R2-02**: o script `experiment_conjecture3.py` calculava em
$x_\ell=k_\ell/3^\ell$ desde a rodada R1, mas o `main.tex` sempre
definiu $L_\ell$ em termos de $x_\ell^+:=x_\ell+3^{-\ell-1}$. Corrigido
o script (`sample_points()` agora devolve $x_\ell^+$), re-executada a
computação completa até $\ell=500$ (momentos exatos até grau 510,
~415s), e todos os números de §5 recomputados do zero: o déficit
$\ell(2/3-L_\ell)$ em $u=0$ vai de $0.5807\to0.5800$ (em $x_\ell$,
errado) para $0.8026\to0.8021$ (em $x_\ell^+$, correto). Os números que
não dependem sensivelmente da escolha $x_\ell$ vs $x_\ell^+$
($\ln(\varphi/\varphi_0)$, o ajuste $L=-0.619$, $c=0.539$) mudaram
apenas na sexta casa decimal, dentro do esperado (a correção
$3^{-\ell-1}$ é exponencialmente pequena e $\ln$ é suave; $L_\ell$ em
si é mais sensível por envolver uma razão entre pontos vizinhos). De
passagem, adicionei a derivação de uma linha (via (7.7)) de por que o
valor previsto é $2/3$ (R2-13/14), que não estava em lugar nenhum do
texto antes.

**R2-17/18, nota de contagem**: o crítico contou 7 antíteses "X, not
Y" usando qualquer ocorrência de ", not"; usando só os padrões literais
da Regra 4b ("not P: it is Q", "not merely P but Q", "P, not Q",
antítese corretiva "rather than"), "not even in the mean" (uma
intensificação, não uma correção) e "rather than every unit residue"
(uma descrição, não uma correção comparativa) não contam. As 3 que
contam foram reduzidas a 2 (orçamento da regra), cortando a antítese
introduzida nesta própria rodada em `prop:complex-deconditioning` e
mantendo as duas ligadas à Regra 10b ("not this extrapolation", "not
the conjecture itself"). Julgamento registrado aqui para a próxima
rodada não reabrir.

Depois das correções: `\cite`/`\bibitem` reconferidos (`BergKruppel1998`
ficou órfão ao cortar a frase antiga de §5; restaurado citando
Proposition 9.1, pp.178-179 do PDF, verificado diretamente contra a
fonte); recompilado (`pdflatex` ×2, 12 páginas, sem `undefined
reference`); zero em/en dashes; abstract reconferido contra o corpo
depois de todas as correções (Regra 8b), incluindo um problema que eu
mesmo introduzi e peguei nesta checagem: "unique $L^1$ fixed point" no
abstract não carregava a ressalva de normalização que R1-06 já tinha
corrigido no corpo (`prop:fabius`), corrigido para "unique fixed point
of unit mass". Repositório `collatz-wirsching-2003` sincronizado:
script de §5 corrigido e re-executado do zero, READMEs (raiz e `sec5`)
atualizados com os números reais em $x_\ell^+$.
