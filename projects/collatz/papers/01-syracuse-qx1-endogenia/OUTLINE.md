# Outline — paper 01 (qx+1 / medida de Syracuse / barreira de endogenia)

Status: `main.tex` é um rascunho completo (35 páginas, compila limpo,
bibliografia consistente). Dividido em 2026-08-10: §3 (equação de
pressão), §6 (Kontorovich-Lagarias vs. Volkov) e §9.2+§9.3 (Wirsching
2003) saíram para os papers 04, 06 e 05 respectivamente (ver
`papers/README.md`); 01 mantém versões condensadas (enunciados sem
prova, citando o companion paper) dos resultados de lá que outras
partes de 01 ainda usam. `main-pt-br.tex`, `main.pdf` e
`main-pt-br.pdf` continuam removidos, só regenerar sob pedido explícito
do diretor científico. Escopo: H-109 a H-169 (H-166 novo, prova
incondicional `beta_eff<=1.882712`).

Este arquivo existe para que uma sessão futura não precise reler
`STATE.md` inteiro nem `main.tex` do zero para saber o que já está
prosa, o que é teorema versus conjectura versus resultado empírico, e
onde está o código de verificação de cada um.

Repositório de reprodutibilidade: `github.com/faculdade/collatz-endogeny`
para o que ainda está em 01; `collatz-qx1-pressure`, `collatz-kl-volkov`,
`collatz-wirsching-2003` para o que migrou (ver seção "Papers
companheiros" abaixo).

## 1. Introdução (§1)

Motivação (Collatz, medida de Syracuse de Tao 2022), enquadramento
deliberado como "caracterização precisa de uma barreira", não
"tentativa de prova". A lista de contribuições precisa ser conferida
contra o corpo atual (pode ainda citar §3/§6/§9.2-9.3 como se
estivessem no corpo completo; ajustar para "resumido aqui, provado no
companion paper X" na próxima passada de crítica).

## 2. Setup (§2)

Mapa $qx+1$ acelerado e sua árvore reversa. Sem teoremas próprios;
define notação usada no resto do paper — inclusive pelos três papers
companheiros, que reproduzem esta seção de forma autocontida.

## 3. Equação de pressão fechada — CONDENSADA (§3) — prova completa em `collatz-qx1-pressure`

Enunciados mantidos (sem prova, citando `\cite{PressureCompanion}`):
`thm:pressure`, `prop:always-frozen`, `thm:transition-model`,
`prop:transition-fine`, `conj:transition-arithmetic`,
`thm:qadic-martingale`, `thm:lp-collision`, `conj:tail-index`,
`thm:iid-tail`. Mantidos porque §4, §9.1, e o resto do paper referenciam
`alpha_-(q)`/`alpha_+(q)` e os rótulos diretamente. Ver paper 06 para
provas, tabela completa de raízes, discussão da transição de
congelamento, e toda a bateria empírica do índice de cauda em $q=5$.

## 4. Barreira de endogenia (§4) — H-110, H-128, H-150

- **Proposição (liberdade de gauge)** `prop:gauge`: $G=W\cdot Y$
  resolve a mesma recursão que a solução canônica.
- **Lema (sem memória 2-ádica)** `lem:2adic`.
- **Teorema (a recursão não força endogenia)** `thm:barrier`.
- **Teorema (acoplamento máximo de dígitos frescos)**
  `thm:fresh-digit-coupling` — H-150: independência par a par é
  impossível (TV$=1-3^{-s}$). Alvo correto passa a ser cancelamento
  após agregação sobre os índices de caminho = **O1**. E-129/E-133
  testaram rotas de agregação (gap de irmãos; funcional diagonal de
  Fourier) e mostraram que nenhuma fecha sozinha — ver H-159, H-162.
- Verificação: `[sec4-endogeny-barrier]`, `[sec8-fresh-digit-coupling]`.

(A antiga subseção "Precise regime of the tail exponent" §4.2 foi
removida daqui e incorporada ao paper 06, onde encaixa melhor junto à
classificação do segundo root de $q=3$.)

## 5. Calibração empírica do acoplamento residual (§5) — H-111

Experimento de controle de 3 braços: $\rho_{eff}\lesssim0.06$ (IC95%).
Verificação: `[sec5-rho-eff-control-experiment]`.

## 6. Kontorovich-Lagarias vs. Volkov — CONDENSADA (§6) — prova completa em `collatz-kl-volkov`

Mantidos `thm:kl` (leitura de janela fixa, 0.639, não decide) e
`thm:kl-calibrated` (achado novo de O8: com controles casados, a árvore
lê 0.64926, separada do controle a 0.678 por dez larguras de banda).
Ver paper 04 para o lema da congruência de irmãos, a calibração
completa, e a discussão de escopo (testa o valor 0.678, não o modelo de
Volkov em si).

## 7. Teste computacional direto da WCC (§7) — H-114

**Empirical Result** `thm:wcc` (Weak Covering Conjecture, `conj:wcc` =
Wirsching 1998 Conj. 3.9). DP de bitset validado até $\ell=20$.
Verificação: `[sec7-weak-covering-conjecture]`.

## 8. Três regimes de precisão para a extensão bivariada de Tao (§8) — H-115

Por que o argumento bivariado ingênuo falha; reformulação não
circular; os três regimes de precisão (par fixo / $\ell=O(\log D)$ /
$\ell\asymp D$, onde vive a WCC). O ataque a O4 (2026-08-09) mostrou
que o alvo de O4 implica a condição L² de O7 (mesma ponte de H-155) e
não se reduz a O2 — ver H-115 (seção datada), H-163.

## 9. Triangulação: três formulações do mesmo obstáculo (§9)

### 9.1 β=1 (Tao 2020) e o problema de cobertura ponderada — H-124, H-131, H-148, H-158, H-161, H-166

- **Proposição (identidade de suporte e custo geométrico)**
  `prop:beta-wcc` — H-131: identifica o suporte comum de WCC e β=1 =
  **O2**.
- **Teorema (barreira de grande desvio no custo da WCC)**
  `thm:wcc-large-deviation` — H-148.
- H-158/H-161: reformulação via órbita afim; **H-166 (novo, 2026-08-09):
  prova incondicional `beta_eff<=1.882712`** via monotonicidade do
  fator de cascata entre níveis, certificada em aritmética exata,
  melhorando a cota anterior (2.306270). Programa de somas de Weyl para
  a desigualdade de par fecha como insuficiente (motivo estrutural).
- Verificação: `[sec9-wcc-beta-bridge]`; H-166 em
  `experiments/E-134-weyl-sum-pair-anticoncentration/` (repo principal,
  ainda não espelhado em `collatz-endogeny`).

### 9.2+9.3 Wirsching 2003 — CONDENSADA — prova completa em `collatz-wirsching-2003`

Enunciados mantidos (sem a maioria das provas): `prop:fabius`,
`thm:wirsching-conj1`, `thm:conjecture3`, `thm:microcanonical`,
`prop:complex-deconditioning`, `thm:fixed-precision-ensemble`,
`thm:sublinear-precision-ensemble`, `thm:linear-block-nonequivalence`,
`thm:ensemble-divergence`, `thm:fixed-precision-finite`,
`thm:microcanonical-finite`, `thm:microcanonical-fourier`. Ver paper 05
para as provas completas, a leitura corrigida da Conjectura 2 direto da
fonte primária (achado de O3, 2026-08-09), e o achado ainda não escrito
sobre zeros de custo central (H-167/H-168).

## 10. Dois candidatos a lema, executados até o fim (§10)

### 10.1 Lema de regime 2: teorema de estrutura + teste finito — H-126, H-140, H-149, H-154 a H-157, H-169

- **Lema (identidade espectral de covariância)** `lem:cov-spectral`.
- **Proposição (endogenia grosseira exata)** `prop:exact-endogeny`.
- **Empirical Results**: `thm:l2-finite`, `thm:lp-spectrum`.
- **Proposição (buraco primitivo grosseiro)** `prop:primitive-hole` —
  H-149/H-154: um buraco de suporte sozinho não produz coeficiente de
  Fourier primitivo = **O5**.
- **Proposição (energia primitiva = desequilíbrio de fibra)**
  `prop:primitive-fibre-energy` — H-154.
- **Teorema (decomposição multiescala de Parseval)**
  `thm:multiscale-parseval` — H-155: conecta **O5** e **O7**.
- **Teorema (renormalização logarítmica de colisão em $q$-ádico)**
  `thm:logarithmic-collision` — H-156/H-157: crescimento exponencial
  incondicional $K_{q,\ell}\ge(35/27)^\ell$ para $q\ge5$. **H-169
  (novo, O7, 2026-08-09) prova `K_(q,ell)>=(q/3)^ell` incondicional
  sem hipótese de levantamento maximal, melhorando H-157**; em $q=3$
  reduz a margem que falta a uma única colisão deslocada afim, medida
  mas não fechada.
- Verificação: `[sec10-l2-refutation-and-jensen]`,
  `[sec10-primitive-spectral-analysis]`; H-169 em
  `experiments/E-138-diagonal-shifted-collision/` (ainda não espelhado
  em `collatz-endogeny`).

### 10.2 Redução Z-number: dicotomia condicional + Proposição C — H-127, H-164, H-165

- **Conjectura (alvo de concentração primitiva encadeada)** `lem:B`.
- **Proposição (déficit de Halász irrestrito)** `prop:halasz-deficit`.
- **Teorema (identidade de Jensen)** `thm:jensen`: déficit de fator
  $\approx1.88\times$ no orçamento de Fourier $\ell^1$ anelado.
  **Corrigido (O5, 2026-08-09): o ponto de inversão real é
  `gamma~3.31`, não `gamma=3`** (a identidade de Jensen exige `p>=1/2`).
  Toda a família $\ell^r$ ($r\ge1$) foi testada, nenhuma fecha o hiato
  (H-164).
- **Proposição (orçamento anelado para um buraco difuso)**
  `thm:propC`.
- Verificação: `[sec10-l2-refutation-and-jensen]` (inclui agora Part 5,
  família $\ell^r$).

## 11. Contextualização na literatura mais ampla (§11) — H-128, H-135, H-136

- **Proposição (rigidez de $\mathbb{Z}_3^\times$)** `prop:rigidity`.
- **Teorema (a teoria geral não se transfere)** `thm:no-transfer`.
- Teste do estatístico de módulo fixo de Chang (2026): auditoria
  fechada (H-136) = **O6**, não é mais problema matemático em aberto.
- Verificação: `[sec11-chang-one-bit-mixing]`.

## 12. Discussão (§12)

Por que uma barreira precisamente caracterizada é uma contribuição
legítima.

## 13. Conclusão e direções em aberto (§13) — a lista O1-O8

Precisa de uma passada de atualização (não feita ainda nesta sessão):
os números da tabela abaixo são de antes do ataque paralelo a O1-O8
(2026-08-09) e não refletem H-166 (O2 quase fechado, cota
1.882712), H-169 (O7, nova cota incondicional), a ponte O4→O7 (H-115),
nem a correção de `gamma` em O5.

| # | Alvo | Status pré-2026-08-09 (desatualizado, ver seções acima) |
|---|------|----------------------------------------------------------|
| O1 | Cancelamento de correlações de frequência fina | Aberta, alvo restrito a funcional de momento/Fourier (E-129, E-133). |
| O2 | WCC + estimativa de cobertura ponderada (β=1) | **H-166 prova beta_eff<=1.882712 incondicional**; desigualdade de par de H-161 continua aberta. |
| O3 | Wirsching Conjectura 2 | Aberta; leitura corrigida da fonte primária (O3), condição de H-134 refutada por H-160 pelo motivo certo agora. |
| O4 | Controle exponencial da cauda de frequência fina | Aberta; implica condição L² de O7 (nova ponte, H-115); não se reduz a O2. |
| O5 | Exclusão de falhas espectralmente difusas primitivas | Aberta; família $\ell^r$ inteira testada, nenhuma fecha; `gamma` corrigido para 3.31. |
| O6 | Balanço de resíduos de módulo fixo (Chang) | Fechada como auditoria. |
| O7 | Continuidade absoluta e índice de cauda | Aberta; **H-169 prova K_(q,ell)>=(q/3)^ell incondicional**, melhora H-157. |
| O8 | Transição do expoente na árvore aritmética genuína | Aberta desde 1995; **paper 04 dá separação calibrada forte em q=5** (não é prova). |

## Papers companheiros (split de 2026-08-10)

- `04-kontorovich-lagarias-volkov/` — §6 completo, repo
  `collatz-kl-volkov`.
- `05-wirsching-2003-conjecturas/` — §9.2+§9.3 completo, repo
  `collatz-wirsching-2003`.
- `06-pressao-qx1-ramificacao/` — §3 completo (+ a antiga §4.2), repo
  `collatz-qx1-pressure`.

01 mantém enunciados condensados (sem prova) de tudo o que ainda
referencia por rótulo, citando o companion paper correspondente. Ver
`papers/README.md` para o mapeamento completo.

## Apêndice: metodologia de validação numérica

Sem teoremas próprios; documenta práticas de validação usadas em todo
o paper (comparação DP vs. força bruta, etc.). Pode ter referências
resolvidas a scripts que migraram para os repos companheiros — conferir
na próxima revisão.

## Zeladoria (2026-08-10)

- **Divisão em quatro papers** (pedido do diretor científico, "divida
  o paper de forma que todos tenham sua importância e possam receber
  citações"): feita nesta sessão. Cada novo paper compila limpo e tem
  repositório próprio populado e verificado (Regra 12). `main.tex` de
  01 caiu de 45 para 33 páginas; bibliografia reconferida (nenhum
  `\cite` órfão, nenhum `\bibitem` não citado).
- ~~Tabela O1-O8 na Conclusão desatualizada~~ — corrigida (2026-08-10):
  adicionados `thm:cascade-factor` (H-166) e `thm:diagonal-collision`
  (H-169) com enunciado e esboço de prova no corpo de §9.1/§10.1 (antes
  só existiam nos arquivos de hipótese, nunca tinham entrado no
  `main.tex`), e a lista O1-O8 reescrita citando os dois mais a leitura
  corrigida de Wirsching Conj. 2, a ponte O4→O7, a família $\ell^r$
  esgotada, e a separação calibrada de O8. 35 páginas agora (era 33).
- ~~H-166/H-169 sem espelho em `collatz-endogeny`~~ — corrigido:
  `sec9-worst-cylinder-cascade/` e `sec10-diagonal-shifted-collision/`
  criados, cada script rerrodado no novo local antes do commit.
- **Pendência real**: as citações `\cite{PressureCompanion}`,
  `\cite{KLVolkovCompanion}`, `\cite{WirschingCompanion}` (nos quatro
  papers) apontam para "in preparation" — trocar pelo arXiv ID real
  assim que cada companion for submetido (ordem sugerida: 06 primeiro,
  depois 04/05 em paralelo, 01 por último).
- Não existe ainda `CRITIQUE.md` para nenhum dos quatro papers (Regra
  8/15). Recomendável antes de qualquer submissão real.
- H-158 (passo 4, a desigualdade de par de H-161) continua aberta: é a
  questão de pesquisa real por trás do que falta de O2.
