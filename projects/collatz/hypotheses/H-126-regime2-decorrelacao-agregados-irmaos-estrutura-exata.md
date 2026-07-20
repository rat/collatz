# H-126 — Decorrelação de agregados de subárvore irmãos: o "lema do regime 2" refeito

Status: refutada (como esboçada em H-115) — substituída por um teorema
de estrutura exata (positivo, demonstrado) mais um lema condicional
cuja hipótese foi refutada empiricamente (E-100)
Criada em: 2026-07-17
Origem: execução do primeiro dos dois "próximos passos declarados" de
H-115. Consulta ao Fable para formalizar com rigor de "lema de paper"
a decorrelação de agregados de subárvore irmãos em módulos grosseiros
3^{O(log D)}. Fable identificou que o esboço original está errado —
não é um gap de adaptação, é uma premissa falsa — e propôs a
reformulação correta, que este documento registra.

## O que o esboço de H-115 alegava (e por que está errado)

H-115 esboçava um orçamento "|ρ(ξ)| ≤ C_A·D^{-A} uniformemente em
ξ≠0", com a soma sobre as 3^ℓ-1 frequências fechando se 3^ℓ ≪ D^{2A}.
Isso está errado por uma identidade EXATA do próprio Tao (2022), não
por uma estimativa perdida:

> **Eq. (1.23) de Tao** (conferida verbatim no PDF, item 106 do
> INDEX, linha 491 do texto extraído): Syrac(Z/3ⁿZ) mod 3^k ≡
> Syrac(Z/3^kZ) — auto-similaridade exata.

Consequência: para qualquer frequência ξ de nível primitivo ℓ′ (i.e.
ξ = 3^{ℓ-ℓ′}·ξ₀ com 3∤ξ₀) e qualquer profundidade D ≥ ℓ′,
E[e(ξF_D/3^ℓ)] = φ_{ℓ′}(ξ₀) — **independente de D**. A profundidade D
é um parâmetro mudo no regime grosseiro: não há "mais mistura" a
extrair de profundidade extra, porque a ultrametricidade 3-ádica corta
a série exatamente nas ℓ primeiras coordenadas (adjacentes à raiz, na
ordenação de Tao eq. 1.29). O orçamento correto por frequência é
C_A·ℓ′^{-A} (Prop. 1.17, que exige **3∤ξ** — conferida verbatim,
linha 637: "let ξ ∈ Z/3ⁿZ be not divisible by 3"), não C_A·D^{-A}.

Exemplo fechado, nível ℓ′=1: Syrac₁ = 2^{-a} mod 3 vale 2 com prob 2/3,
1 com prob 1/3 (nunca 0). |φ(1)| = |ω/3 + 2ω²/3| = 1/√3 ≈ 0,577 para
TODO D — sem decaimento algum em D.

Mesmo com a correção (ℓ′^{-A} em vez de D^{-A}), o orçamento L∞ diverge:
Σ_{ℓ′≤ℓ} 3^{ℓ′}·(C_A ℓ′^{-A})² ≍ 3^ℓ·ℓ^{-2A}, nunca o(1). Fechar por
contagem de frequências exigiria cancelamento de raiz quadrada
(decaimento ~3^{-ℓ′/2-ε}) — o próprio regime 3 (H-115), reaparecendo
dentro do que deveria ser o regime "fácil".

## O que sobrevive: teorema de estrutura exata

A parte não-circular do esboço original (expansão do segundo momento
em pares de caminhos) está correta e vira um lema de verdade.

**Setup.** F_n(a) = Σ_j 3^{j-1}2^{-a_{[1,j]}} mod 3^n (eq. 1.22/1.29 de
Tao), Syrac(Z/3ⁿZ) := F_n(Geom(2)ⁿ). **Lema-ponte** (H-111, verificado
por indução direta via a recursão de F): a ∈ (ℕ₊)^ℓ é o vetor de
expoentes de um caminho reverso de profundidade ℓ abaixo de u sse
F_ℓ(a) ≡ u (mod 3^ℓ); a₁ é o passo adjacente à raiz. Para irmãs com
expoentes admissíveis α₁<α₂ em v, Δ:=α₂-α₁ (par): w₂ = 2^Δ·w₁ + c_Δ,
c_Δ:=(2^Δ-1)/3 — vínculo afim com multiplicador unitário mod 3^ℓ.

**Lema 1 (identidade espectral da covariância).** Para agregados
Z_i := N_{η_i}^{(m)}(w_i(v)) (populações ponderadas de subárvore
truncadas em precisão m, η_i: (ℕ₊)^D→[0,1]), com v uniforme nas
classes admissíveis mod 3^{m+1}:

> Cov(Z₁,Z₂) = 3^{-2m} Σ_{ξ≠0 mod 3^m} e(-ξc_Δ/3^m)·S₁(-2^Δξ)·S₂(ξ)

(demonstração: ortogonalidade de caracteres + w₂=2^Δw₁+c_Δ; a
independência dos dois índices de soma vem da tautologia da expansão
do quadrado, não de hipótese aritmética — este ponto do esboço
original estava certo). **Mas** a dependência via o v comum NÃO é
cancelada por essa expansão — sobrevive integralmente como o
emparelhamento diagonal de frequências ξ₁=-2^Δξ₂.

**Proposição 2 (endogenia exata, contraexemplo fechado).** Para
populações completas (η_i≡1) e precisão m=1: se 2·3^ℓ|Δ então
Corr(Z₁,Z₂)=1 (para todo D); em precisão ℓ=1 geral, Corr = +1 se
Δ≡0 (mod 6), = -1/2 caso contrário — **independente de D e de
qualquer truncamento**. Agregar folhas não decorrelaciona: agregar
PROJETA na σ-álgebra grosseira gerada por w_i mod 3^ℓ, e nessa
σ-álgebra o vínculo entre irmãs é o vínculo determinístico afim do
regime 1 (H-115) — que ressurge intacto, não desaparece. Isto converte
a barreira de endogenia (H-110) de argumento qualitativo em fórmula
fechada. **Resultado positivo, mas com sinal oposto ao esperado**: o
que é demonstrável é a persistência exata da correlação grosseira, não
seu desaparecimento.

## Lema 2 / 2′: o que seria salvável, e por que a hipótese que precisa foi refutada

Decompondo a soma do Lema 1 por nível primitivo e usando
Cauchy-Schwarz + Parseval: Cov = C_exato(ℓ₀;Δ) + Err, com C_exato
finito/exato/independente de D (calculável, Prop. 2), e

> |Err| / (E[Z₁]E[Z₂]) ≤ K_m - K_{ℓ₀}, onde K_ℓ := 3^ℓ·Σ_y p_ℓ(y)²
> (massa de colisão normalizada da medida de Syracuse).

O **Lema 2′ condicional** proposto pelo Fable: se K_∞:=lim K_ℓ < ∞
(equivalentemente, f=dμ/d(Haar) ∈ L²(Z_3)), a covariância fina
(descontada da componente grosseira exata) é ≤ K_∞-K_{ℓ₀} → 0,
uniformemente em m, D, Δ.

**Esta hipótese foi testada e refutada em E-100.** K_ℓ foi calculado
exatamente (recursão derivada da propriedade memoryless de Geom(2) e
da identidade eq. 1.23, resolvida por série geométrica ao longo da
órbita cíclica de multiplicação-por-2 mod 3^ℓ) até ℓ=17: cresce de
forma limpa e consistentemente **linear**, incrementos ΔK_ℓ convergindo
monotonicamente a ≈0,47, sem qualquer sinal de saturação. **K_∞=∞ —
L² falha.** O Lema 2′ é vazio pela mesma parede do regime 3: não é um
degrau mais fácil, é irmão dele, e agora com refutação computacional
direta (não apenas "em aberto") do ingrediente extra que o salvaria.

**Conexão com dados do próprio projeto**: H-104 mediu expoente de
cauda α≈2 para razões de população de subárvore — exatamente o
expoente crítico da condição L² (α>2 ⟹ K_∞<∞; α<2 ⟹ K_ℓ diverge
polinomialmente; α=2 é o caso limítrofe). Os dados já apontavam,
sem que se soubesse, para a fronteira exata desta hipótese — e o
resultado de E-100 (crescimento linear limpo) é consistente com
α ligeiramente abaixo de 2 ou exatamente no limiar com log-correção,
não seria improvável revisitar H-104 com essa lente.

## Escada de "flatness" da medida de Syracuse (situando o ingrediente que falta)

- **L¹ (provado)**: Prop. 1.14 de Tao (Osc_{m,n} ≪_A m^{-A}) ⟹ μ é
  limite em variação total de medidas absolutamente contínuas.
- **L² (refutado nesta sessão, E-100)**: K_∞<∞ — falso.
- **L∞ / β=1 (H-124, em aberto)**: sup p_ℓ ≪ 3^{-ℓ(1-o(1))} — nem
  comparável nem implicado por L², mas mora no mesmo andar
  "além-TV" da escada.

## Veredito final

O "lema do regime 2" de H-115 não é demonstrável como esboçado, e sua
versão salvável (condicional a L²) tem a hipótese refutada
computacionalmente. O que sobra, e que é genuinamente novo e citável:
(i) um teorema de estrutura exato mostrando que a correlação grosseira
de agregados irmãos NÃO desaparece — é uma fórmula fechada,
independente de profundidade (Prop. 2); (ii) uma nova caracterização,
mais limpa que endogenia/WCC/β=1, do ingrediente que falta: a condição
L² sobre a medida de Syracuse, agora com refutação computacional
direta em vez de "em aberto"; (iii) uma predição falsificável nova
(correlação sistematicamente maior para pares Δ≡0 mod 6) para checar
contra o pipeline de H-111 se algum dia for útil — não perseguida
agora, seria trabalho novo, não fechamento de ponta.

## Correções de terminologia/citação (Fable, conferidas)

- Prop. 1.14 é o mixing fino em TV; Prop. 1.17 é o decaimento de
  Fourier (exige 3∤ξ) — não confundir os dois papéis.
- "Condicionamento no primeiro passo" está DENTRO da demonstração da
  Prop. 1.17 (Seção 7), não no enunciado de nenhuma das duas.
- Orientação de coordenadas (Tao, eq. 1.29, reversão explícita): a₁ é
  o passo adjacente à RAIZ, não o mais fundo — armadilha real para
  qualquer enunciado futuro que cite janelas mod 3^ℓ.

## Referências

- H-110/H-111 — barreira de endogenia e calibração empírica (ρ_eff).
- H-115 — três regimes de precisão, origem do esboço aqui refutado.
- H-104 — expoente de cauda α≈2 de razões de população (conexão com
  o limiar crítico de L² identificado aqui).
- Tao (2022), item 106 do INDEX — eqs. (1.22),(1.23),(1.29), Prop.
  1.14, Prop. 1.17, Remark 1.15 (todas conferidas verbatim no PDF
  nesta sessão).
- E-100 — teste computacional de K_ℓ (refutação da hipótese L²).

## Atualizações

- 2026-07-17: hipótese criada; refutação do esboço e teorema de
  estrutura formalizados via consulta ao Fable; hipótese L² do Lema 2′
  testada e refutada em E-100 (K_ℓ diverge linearmente até ℓ=17).
- 2026-07-20: predição falsificável (iii) da seção "Veredito final"
  perseguida (não mais "não perseguida agora"). Uma auditoria externa
  do paper apontou tensão aparente entre a Prop. 2 (correlação
  grosseira exata, persistente) e a calibração empírica de H-110
  (ρ_eff≲0,06, "nenhum acoplamento detectado"). Opus consultado propôs
  reconciliação por diluição (a correlação de par é exata mas
  contribui fração evanescente da variância agregada que cresce
  exponencialmente) e sugeriu computar a soma ponderada por Δ para
  verificar o sinal previsto (negativo). **E-108**: sob a medida
  natural de seleção de par pelo produto dos pesos de ramo (a mesma do
  Lema 1), E[Corr] = -3/7 exato (P(Δ≡0 mod 6)=1/21, P(Δ≢0 mod 6)=20/21) —
  confirma o sinal negativo previsto, com magnitude não-trivial. Não é
  prova de que a calibração de H-110 mede exatamente esta quantidade
  (o Braço 2 usa uma família de acoplamento funcionalmente diferente),
  mas fortalece a plausibilidade da reconciliação por diluição já
  registrada no paper (`rem:calibration-consistency`). Ver
  `experiments/E-108-delta-weighted-coarse-correlation/`.
- 2026-07-20 (mesma sessão, continuação — `E-110`): resolução MAIS
  FORTE encontrada, indo além da diluição. Verifiquei diretamente no
  código do simulador de H-111
  (`experiment_synthetic_core.py`) que `child_type = (rho_phase+k)%3`
  (o resíduo mod 3 do filho — exatamente Z_i em precisão ℓ=1 da
  Prop.2) é função determinística só da fase da raiz e do índice do
  ramo, **nunca do parâmetro `rho`** (a intensidade de acoplamento que
  o Braço 2 varia). Testado em 2000 seeds com ρ∈{0,0.3,0.7,1.0}: 0
  divergências na sequência de tipos. E a correlação de tipo do
  simulador reproduz exatamente +1/-1/2 de Prop.2 (até a 4ª casa
  decimal). **Conclusão**: a correlação grosseira de Prop.2 e o
  acoplamento medido por ρ_eff são eixos ortogonais, não a mesma coisa
  em escalas diferentes — ρ varia o conteúdo/magnitude das subárvores,
  a Prop.2 é sobre o resíduo mod 3 (determinístico, presente
  identicamente em TODOS os braços, real ou sintético). A cota
  ρ_eff≲0,06 nunca poderia ter detectado nem deixado de detectar a
  correlação de Prop.2 — ela pertence a um eixo que o experimento não
  varia. Isso substitui a diluição como explicação primária no paper
  (`rem:calibration-consistency` atualizado); a diluição (E-108)
  permanece válida como ponto secundário. Ver
  `experiments/E-110-calibration-type-structure-orthogonal-to-coarse-corr/`.
