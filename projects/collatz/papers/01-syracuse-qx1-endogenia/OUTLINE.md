# Outline — paper 01 (qx+1 / medida de Syracuse / barreira de endogenia)

Status: `main.tex` é um rascunho completo (45 páginas, compila limpo,
bibliografia consistente). `main-pt-br.tex`, `main.pdf` e
`main-pt-br.pdf` foram removidos ao incorporar o lote H-131 a H-160 e
só devem ser regenerados sob pedido explícito do diretor científico
(ver `papers/README.md`). Escopo: H-109 a H-160.

Este arquivo existe para que uma sessão futura não precise reler
`STATE.md` inteiro nem `main.tex` (3400+ linhas) do zero para saber o
que já está prosa, o que é teorema versus conjectura versus resultado
empírico, e onde está o código de verificação de cada um. Regenerado em
2026-08-08 a partir do `main.tex` real (a versão anterior deste arquivo
cobria só H-109-128 e foi deletada quando o paper foi reescrito).

Repositório de reprodutibilidade: `github.com/faculdade/collatz-endogeny`,
organizado por seção (`secN-nome/`). Cada apontamento abaixo no formato
`[secN-nome]` é literal: o texto do paper aponta para essa pasta.

## 1. Introdução (§1)

Motivação (Collatz, medida de Syracuse de Tao 2022), enquadramento
deliberado como "caracterização precisa de uma barreira", não
"tentativa de prova" (retomado em §12, Discussão). Lista as 8
contribuições (i)-(viii) que mapeiam 1:1 nas seções abaixo.

## 2. Setup (§2)

Mapa $qx+1$ acelerado e sua árvore reversa. Sem teoremas próprios;
define notação usada no resto do paper.

## 3. Equação de pressão fechada (§3) — H-109, H-138, H-139, H-141

- **Teorema (identidade de pressão anelada exata)**
  `thm:pressure`: $\rho_{ann}(\alpha)=q^{\alpha-1}/(2^\alpha-1)$, via
  bijeção de fibra (corrige o argumento de autômato finito original).
- **Teorema (martingale de densidade q-ádica)** `thm:qadic-martingale`
  — H-138.
- **Teorema (critério de colisão $L^p$)** `thm:lp-collision` — H-141.
- **Teorema (singularidade na raiz congelada)** `thm:frozen-singular`
  — H-139.
- **Proposição (a raiz maior é sempre congelada)** `prop:always-frozen`.
- **Teorema/Conjectura (transição estrutural em $q=5$)**
  `thm:transition-model` (provado no modelo iid),
  `conj:transition-arithmetic` (conjectural na árvore real) = **O8**.
- **Conjectura (índice de cauda)** `conj:tail-index`; **Teorema (índice
  de cauda no modelo iid)** `thm:iid-tail` — H-132, prova via Liu
  (2000) Teorema 2.2 (citação conferida contra o original). Sua
  transferência aritmética é **O7** (ver H-159, ainda aberta).
- Verificação: `[sec3-pressure-equation]`.

## 4. Barreira de endogenia (§4) — H-110, H-128, H-150

- **Proposição (liberdade de gauge)** `prop:gauge`: $G=W\cdot Y$
  resolve a mesma recursão que a solução canônica.
- **Lema (sem memória 2-ádica)** `lem:2adic`.
- **Teorema (a recursão não força endogenia)** `thm:barrier`.
- **Teorema (acoplamento máximo de dígitos frescos)**
  `thm:fresh-digit-coupling` — H-150: independência par a par é
  impossível (TV$=1-3^{-s}$). Alvo correto passa a ser cancelamento
  após agregação sobre os índices de caminho = **O1**. E-129 (2026-08-08)
  testou a rota mais óbvia de agregação (promediar sobre o gap de
  irmãos) e mostrou que ela sozinha não restaura independência em
  TV/informação mútua — descarta essa rota específica, não fecha O1.
  Ver H-159.
- Verificação: `[sec4-endogeny-barrier]`, `[sec8-fresh-digit-coupling]`.

## 5. Calibração empírica do acoplamento residual (§5) — H-111

Experimento de controle de 3 braços: $\rho_{eff}\lesssim0.06$ (IC95%).
Verificação: `[sec5-rho-eff-control-experiment]`.

## 6. Kontorovich-Lagarias vs. Volkov (§6) — H-113

Enumeração exata da árvore reversa de $5x+1$ + extrapolação de Aitken
$\Delta^2$: expoente $0.639$, IC95% $[0.633,0.645]$, excluindo Volkov
(0.678) com folga. Resultado empírico com menor dependência de framing
teórico do paper. Verificação: `[sec6-kontorovich-lagarias-vs-volkov]`.

## 7. Teste computacional direto da WCC (§7) — H-114

**Empirical Result** `thm:wcc` (Weak Covering Conjecture, `conj:wcc` =
Wirsching 1998 Conj. 3.9). DP de bitset validado até $\ell=20$.
Verificação: `[sec7-weak-covering-conjecture]`.

## 8. Três regimes de precisão para a extensão bivariada de Tao (§8) — H-115

Por que o argumento bivariado ingênuo falha; reformulação não
circular; os três regimes de precisão (par fixo / $\ell=O(\log D)$ /
$\ell\asymp D$, onde vive a WCC). Sem verificação computacional própria
nesta seção (os regimes 2/3 são desenvolvidos em §9-10).

## 9. Triangulação: três formulações do mesmo obstáculo (§9)

### 9.1 β=1 (Tao 2020) e o problema de cobertura ponderada — H-124, H-131, H-148

- **Proposição (identidade de suporte e custo geométrico)**
  `prop:beta-wcc` — H-131: identifica o suporte comum de WCC e β=1 =
  **O2**.
- **Teorema (barreira de grande desvio no custo da WCC)**
  `thm:wcc-large-deviation` — H-148: multiplicidade ideal dentro da
  fatia de custo da WCC ainda deixa massa exponencialmente
  insuficiente.
- H-158 (em andamento): mede diretamente `3^ell*c_ell` para o pior
  cilindro sem depender do DP de custo; estendido a `ell=18`
  (`beta_eff` decrescendo a 1.162241) e decomposto por faixa de custo
  (E-130). Passo 4 (desigualdade recursiva subexponencial) é a questão
  de pesquisa real, ainda aberta.
- Verificação: `[sec9-wcc-beta-bridge]`.

### 9.2 Função de Fabius base-3 de Wirsching (2003) — H-125, H-133

- **Proposição (função de Fabius base-3)** `prop:fabius`.
- **Teorema (Conjectura 1 de Wirsching)** `thm:wirsching-conj1` — H-133:
  prova por cancelamento de função geradora.
- Verificação: `[sec9-wirsching-conjecture1]`.

### 9.3 Teste certificado da Conjectura 3 de Wirsching — H-125, H-134, H-142 a H-147, H-153

- **Teorema (decomposição microcanônica)** `thm:microcanonical` — H-143:
  seu alvo `(?3)` implica a estimativa de cilindro ponderada de **O2**.
- **Proposição (ponte local-limite condicional)**
  `prop:complex-deconditioning` — H-144.
- **Teorema (equivalência de ensembles em precisão fixa)**
  `thm:fixed-precision-ensemble` — H-145.
- **Teorema (equivalência de ensembles em precisão sublinear)**
  `thm:sublinear-precision-ensemble` — H-146.
- **Teorema (não equivalência de blocos lineares)**
  `thm:linear-block-nonequivalence` — H-153.
- **Teorema (divergência canônica/microcanônica em precisão total)**
  `thm:ensemble-divergence` — H-147: hiato de verossimilhança no
  máximo polinomial, na direção oposta à necessária. Isso é
  Wirsching Conjectura 2 = **O3**, acima da Conjectura 3 já testada
  numericamente.
- **Empirical Results**: `thm:conjecture3` (teste certificado, erro
  $\le10^{-8}$), `thm:microcanonical-finite`, `thm:microcanonical-fourier`,
  `thm:fixed-precision-finite`.
- H-134/H-160: defeito relativo de mistura (Wirsching Conj. 2)
  refutado como suficiente; a paridade do incremento mais novo converge
  a $2/3,1/3$, não Haar.
- Verificação: `[sec9-wirsching-2003-conjecture3]`.

## 10. Dois candidatos a lema, executados até o fim (§10)

### 10.1 Lema de regime 2: teorema de estrutura + teste finito — H-126, H-140, H-149, H-154 a H-157

- **Lema (identidade espectral de covariância)** `lem:cov-spectral`.
- **Proposição (endogenia grosseira exata)** `prop:exact-endogeny`.
- **Empirical Results**: `thm:l2-finite` (crescimento de $K_\ell$ em
  nível finito, ex-"refutação" corrigida para resultado empírico por
  H-140), `thm:lp-spectrum` (espectro de colisão $L^p$ em nível
  finito).
- **Proposição (buraco primitivo grosseiro)** `prop:primitive-hole` —
  H-149/H-154: um buraco de suporte sozinho não produz coeficiente de
  Fourier primitivo = **O5**.
- **Proposição (energia primitiva = desequilíbrio de fibra)**
  `prop:primitive-fibre-energy` — H-154.
- **Teorema (decomposição multiescala de Parseval)**
  `thm:multiscale-parseval` — H-155: conecta **O5** e **O7**.
- **Teorema (renormalização logarítmica de colisão em $q$-ádico)**
  `thm:logarithmic-collision` — H-156 (caso $q=3$) e H-157
  (generalização a todo primo $q\ge5$ com `ord_q(2)` maximal):
  crescimento exponencial incondicional $K_{q,\ell}\ge(35/27)^\ell$
  para $q\ge5$; $q=3$ reduzido a balanço espectral explícito, ainda
  sem margem de sinal uniforme.
- Verificação: `[sec10-l2-refutation-and-jensen]`,
  `[sec10-primitive-spectral-analysis]`.

### 10.2 Redução Z-number: dicotomia condicional + Proposição C — H-127

- **Conjectura (alvo de concentração primitiva encadeada)** `lem:B`.
- **Proposição (déficit de Halász irrestrito)** `prop:halasz-deficit`.
- **Teorema (identidade de Jensen)** `thm:jensen`: déficit de fator
  $\approx1.88\times$ no orçamento de Fourier $\ell^1$ anelado.
- **Proposição (orçamento anelado para um buraco difuso)**
  `thm:propC`: mostra que esse orçamento específico é insuficiente;
  não descarta outros argumentos $\ell^1$.
- Verificação: `[sec10-l2-refutation-and-jensen]` (identidade de Jensen
  e Proposição C).

## 11. Contextualização na literatura mais ampla (§11) — H-128, H-135, H-136

- **Proposição (rigidez de $\mathbb{Z}_3^\times$)** `prop:rigidity`.
- **Teorema (a teoria geral não se transfere)** `thm:no-transfer`:
  por que três mecanismos padrão de decaimento de Fourier
  (auto-similar/auto-conforme) não se aplicam diretamente aqui.
- Teste do estatístico de módulo fixo de Chang (2026): auditoria
  fechada (H-136) — retirado como problema matemático do paper (**O6**,
  fechamento de auditoria, não afirmação em aberto).
- Verificação: `[sec11-chang-one-bit-mixing]`.

## 12. Discussão (§12)

Por que uma barreira precisamente caracterizada é uma contribuição
legítima — retoma o framing da Introdução.

## 13. Conclusão e direções em aberto (§13) — a lista O1-O8

O6 é fechamento de auditoria; os outros sete contêm afirmações
matemáticas em aberto:

| # | Alvo | Hipóteses-fonte | Status nesta sessão |
|---|------|------------------|----------------------|
| O1 | Cancelamento de correlações de frequência fina após agregação sobre pares de irmãos | H-150, H-159 | Aberta. E-129 (2026-08-08) descarta a agregação ingênua sobre o gap; alvo restrito a funcional de momento/Fourier. |
| O2 | WCC + estimativa de cobertura ponderada (β=1) | H-131, H-148, H-158 | Aberta. E-127/E-130 estenderam o pior cilindro a `ell=18` e o decompuseram por custo; passo 4 (desigualdade recursiva) não tentado. |
| O3 | Wirsching Conjectura 2 | H-134, H-147, H-160 | Aberta; condição suficiente proposta em H-134 refutada por H-160. |
| O4 | Controle exponencial da cauda de frequência fina em $\ell\asymp D$ | H-115, H-153 | Aberta; separação já falha em escala linear (H-153). |
| O5 | Exclusão de falhas espectralmente difusas primitivas da WCC | H-149, H-154, H-155 | Aberta; orçamento $\ell^1$ anelado testado (Proposição C) é insuficiente. |
| O6 | Balanço de resíduos de módulo fixo (Chang) | H-136 | Fechada como auditoria; não é mais problema matemático em aberto do paper. |
| O7 | Continuidade absoluta e índice de cauda da densidade tiltada | H-132, H-142, H-156, H-157, H-159 | Aberta para a árvore real; provada no modelo iid (H-132). Suporte empírico forte em $q=5$ (amostra $10^5$). |
| O8 | Transição do expoente na árvore aritmética genuína | (nenhuma nova nesta sessão) | Aberta desde 1995 (Kontorovich-Lagarias/Applegate-Lagarias para $q=3$); provada só no modelo iid. |

## Apêndice: metodologia de validação numérica

Sem teoremas próprios; documenta práticas de validação usadas em todo
o paper (comparação DP vs. força bruta, etc.).

## Zeladoria (2026-08-08)

- ~~`OUTLINE.md` desatualizado (cobria só H-109-128)~~ — regenerado
  agora a partir do `main.tex` real.
- ~~Data Availability Statement desatualizada~~ — corrigida: apontava
  vários teoremas do §9.3/§10 como ausentes do repositório quando o
  corpo do próprio paper já dizia o contrário; todos os 11 rótulos
  citados já estão em `collatz-endogeny` (confirmado por grep contra o
  repo real antes de editar).
- `papers/README.md` (índice de papers) também estava com o escopo
  antigo (H-109-128) e implicava que `main-pt-br.tex` ainda existe;
  corrigido para refletir o escopo atual (H-109-160) e o estado real
  dos arquivos.
- `main-pt-br.tex`/`main.pdf`/`main-pt-br.pdf`: não recriados nesta
  sessão por instrução explícita do diretor científico ("deixe o
  main-pt-br.tex só para quando pedir explicitamente"). Regenerar sob
  pedido.
- Não existe ainda `CRITIQUE.md` para este paper (Regra 8/15). Uma
  rodada de crítica externa (modelo independente ou o diretor
  científico) ainda não aconteceu sobre o `main.tex` reescrito com o
  lote H-131-160; recomendável antes de qualquer submissão.
- H-158 (passo 4) e H-159 continuam abertas: são as duas questões de
  pesquisa reais por trás de O1/O2/O7, não auditorias.
- **Escopo em um só paper (discutido com o diretor científico,
  2026-08-08)**: o paper amarra 8 direções largamente independentes
  (O1-O8) num único arco. Levantada explicitamente a possibilidade de
  dividir (ex.: a seção 6 isolada, ou a dupla WCC/Wirsching, ou a
  redução Z-number, cada uma teria substância para publicação própria)
  contra o risco oposto da Regra 10 (não fatiar um resultado coeso só
  para inflar contagem de citações). Decisão: manter como um só paper
  por ora; revisitar na rodada de crítica externa antes da submissão.
