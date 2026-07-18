# Outline — paper principal da linha G(v)/qx+1/endogenia

Status: hipóteses-fonte fechadas (2026-07-18); redação não iniciada.
Escopo: H-109 a H-128. Fora de escopo: paper cumulativo de críticas
(`../02-critica-cumulativa-literatura/`, BACKLOG.md item 8).

Este arquivo existe para que a sessão que começar a redação não precise
reminerar `STATE.md` (>1800 linhas) do zero. Cada seção abaixo aponta
para a(s) hipótese(s)-fonte e resume o que já está pronto para virar
prosa.

## 1. Introdução / motivação

- Generalização qx+1 da medida de Syracuse de Tao (2022). Conecta a
  Wirsching (1998, Weak Covering Conjecture) e Wirsching (2003, função
  de Fabius base-3).
- Enquadrar desde já como "caracterização precisa de uma barreira",
  não "tentativa de resolver Collatz" — ver seção 9 sobre por que esse
  enquadramento importa (discussão com o diretor científico,
  2026-07-18).

## 2. Forma fechada da equação de pressão (H-109) — CORRIGIDA 2026-07-18

ρ_ann(α) = q^(α-1)/(2^α-1), agora provada como identidade EXATA mas
ANELADA (média sobre raízes mod q^k, via Lema de bijeção de fibra —
revisão externa achou erro real no mecanismo original "automato mod
q", consertado). Raiz trivial α=1 sempre; segunda raiz α*=2
exatamente em q=3; vira <1 para q≥5 (virada estrutural, densidade
positiva vs. zero — esta parte, o expoente de CONTAGEM, sobrevive
como teorema, pois a raiz menor está sempre não-congelada). O índice
de cauda do martingale (α_+/α_-, nosso α*=2 incluso) virou
**Conjectura** separada — a raiz maior está sempre congelada
(Proposição nova, provada), então não é consequência do teorema; em
q=3 bem sustentada por 3 confirmações empíricas independentes, em
q≥5 sem apoio sólido. Ver addendum completo em H-109 e §3/§4 do
paper.

## 3. Barreira de endogenia (H-110, com addendum de H-128)

- Toy model: G(v)=W(v)·Y(v) com Y invariante é outra solução exata da
  mesma recursão — "liberdade de gauge" indistinguível por qualquer
  estatística testada.
- Formulação honesta da barreira: recursão sozinha não força colapso;
  recursão+independência-entre-subárvores força (Choquet-Deny +
  classificação de smoothing transforms) — mas a independência é
  afirmação aritmética não provada.
- **Addendum (H-128)**: α*=2 é regime de "segunda raiz/cauda de
  Goldie" (m'(2)≈+0,174>0), não "caso crítico" — precisão que evita
  cruzar com a literatura errada (Kolesko-Mentemeier e afins).

## 4. Calibração empírica ρ_eff≲0,06 (H-111)

Experimento de controle de 3 braços (i.i.d. sintético, sintético com
acoplamento ajustável, árvore real remedida). Nenhum acoplamento
positivo detectado; cota ρ_eff≲0,06 (IC95%, m=20) — converte a
barreira teórica numa medida quantitativa do seu tamanho.

## 5. Resultado empírico mais citável: disputa Kontorovich-Lagarias vs. Volkov resolvida (H-113)

Árvore reversa real de 5x+1 implementada do zero
(`experiments/E-097-qx1-empirical-gate/`). Expoente extrapolado
(Richardson/Aitken) **0,639, IC95%=[0,633,0,645]** — exclui Volkov
(0,678) com folga ampla; resíduo até Kontorovich-Lagarias (0,650919)
tem assinatura de pré-assintótica de janela fixa, mensurada. Este é o
resultado com menor dependência de framing teórico — vale destacar
cedo no paper como o "resultado duro" independente da discussão de
barreira.

## 6. Teste computacional direto da WCC de Wirsching (H-114)

DP de bitset até ℓ=20, validado contra tabela de referência. j*(ℓ)
existe e é finito em toda a faixa testada; leitura qualitativa final
(ΔAIC≈5, déficit de platôs p≈0,072) favorece crescimento lento
ilimitado de e(ℓ) — compatível com a versão fraca da conjectura,
desfavorece a forte.

## 7. Por que a extensão bivariada de Tao (2022) não cruza a barreira (H-115)

Três regimes de precisão: (1) par fixo — sem decaimento possível; (2)
ℓ=O(log D) — provável, lema real não escrito (ver H-126); (3) ℓ≍D
(onde vive a WCC) — equivalente a problema aberto reconhecido
(rigidez efetiva ×2×3 de Furstenberg / decaimento de Fourier de
medidas autossimilares tipo Breuillard-Varjú).

## 8. Triangulação via literatura (H-124, H-125)

- **H-124**: β=1 de Tao (2020, blog) é o MESMO objeto algébrico da WCC
  de Wirsching — nossos dados de H-114 (e(ℓ) sub-linear) são evidência
  direta a favor de β=1, não só da WCC.
- **H-125**: Wirsching (2003) — terceira roupagem independente da
  mesma barreira, via função de Fabius base-3 (Berg-Krüppel). Teste
  certificado até ℓ=500 (E-099): Conjectura 3 suportada
  numericamente, déficit (0,580±0,001)/ℓ reproduzido pela própria φ₀
  de Berg-Krüppel.

## 9. Os dois lemas finais executados, honestamente (H-126, H-127)

- **H-126 (regime 2)**: refutado como esboçado (premissa D^{-A}
  contradiz eq. 1.23 de Tao); sobrevive teorema de estrutura exato
  positivo (Prop. 2) + lema condicional cuja hipótese (K_∞<∞, L²) foi
  **refutada computacionalmente** (E-100: K_ℓ diverge linearmente até
  ℓ=17).
- **H-127 (redução Z-number)**: vira dicotomia condicional (Lema B),
  não equivalência limpa; inclui resultado negativo próprio
  (Proposição C: déficit de Jensen ~1,88× no orçamento de Fourier
  anelado, confirmado por Monte Carlo em E-101).
- **Framing central (discutido explicitamente com o diretor
  científico, 2026-07-18)**: nenhum lema virou prova, mas isso não
  enfraquece o paper — a convergência de 6+ articulações independentes
  (endogenia, WCC, β=1, L², dicotomia espectral, e a redução puramente
  combinatória de Chang abaixo) no MESMO ingrediente nunca provado é
  evidência de que a barreira é real e bem caracterizada, não um
  buraco de rigor. Caracterizar precisamente uma barreira é
  contribuição legítima, sobretudo com o resultado duro da seção 5 ao
  lado.

## 10. Busca literária dirigida (H-128) — contexto e correções

- **Baker & Banaji (2026)**: citável como moldura ("taxa uniforme não
  é de graça"), com disanalogia explícita (fenômeno deles depende de
  sintonia fina de parâmetro; nossa medida é rígida) — não
  sobre-interpretar como evidência a favor do cenário da Prop. C.
- **Subproduto da consulta ao Fable**: reformulação autossimilar
  explícita da medida de Syracuse (X=Σ3^{k-1}2^{-S_k}) + observação de
  rigidez de Z_3^× (todo subgrupo fechado tem índice finito ⟹ não há
  obstrução tipo Pisot 3-ádica) — meio parágrafo citável, explica por
  que a "receita genérica" da literatura de decaimento lento não se
  aplica aqui.
- **Chang (2026)**: sétima articulação independente (redução puramente
  combinatória a um balanço de resíduos mod 32), testada
  computacionalmente em E-102 — suporte empírico qualificado (órbita
  única longa, desvio acompanha ruído ~1/√i).
- Terminologia corrigida em H-110: α*=2 é "segunda raiz/Goldie", não
  "caso crítico" (evita reavaliar Kolesko-Mentemeier e afins no
  futuro).
- Candidatos avaliados e descartados com razão técnica específica
  (não repetir busca): Fuglede/Salem em Q_p, Li-Sahlsten (renovação
  quantitativa), Siegel (Non-Archimedean Spectral Theory, preprint
  isolado sem conexão explícita). Todos falham pela MESMA rigidez de
  Z_3^× (única razão de contração 3-ádica em todo ramo) — útil
  reconhecer esse padrão comum antes de gastar uma consulta inteira em
  cada novo candidato "parecido".

## 11. Zeladoria — ENCERRADA (2026-07-18)

- ~~Conferir números de equação do Wirsching (2003) contra a versão
  final da DCDS 9(3) (PDF em mãos é "preliminary version").~~
  **Confirmado pelo diretor científico: mesmas equações.**
- ~~Verificar referências externas citadas só de memória pelo Fable em
  H-127~~ (Halász, Tao-Vu, Nguyen-Vu, Mahler, Flatto-Lagarias-
  Pollington, Erdős, Lagarias, mais Brémont e Gonçalves-Greenfeld-
  Madrid que também tinham detalhes a corrigir). **8 de 9 confirmadas
  contra o texto primário; 1 (Halász 1971) documentada no próprio
  `main.tex` como inacessível por busca aberta, não esquecida.** Ver
  H-127 (addendum de 2026-07-18) e `literature/papers/INDEX.md` itens
  139-144.

Nenhuma zeladoria bibliográfica pendente resta para este paper.

## Próximo passo concreto

Escrever a Introdução (seção 1) e decidir a ordem de apresentação:
resultado duro primeiro (seção 5, KL-vs-Volkov) para estabelecer
credibilidade empírica antes de entrar na discussão de barreira
(seções 3, 9, 10), ou ordem "narrativa" (barreira → triangulação →
resultado duro como validação)? Ainda não decidido — é a primeira
escolha editorial real da redação.
