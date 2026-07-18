# H-127 — Falha da WCC como dicotomia espectral: redução condicional a configurações de Bohr pós-wrap

Status: em revisão — redução real mas mais fraca do que o esboço de
H-115 sugeria; inclui um resultado negativo próprio (Proposição C, com
identidade exata via fórmula de Jensen) explicando por que a técnica
não fecha no regime da WCC
Criada em: 2026-07-17
Origem: execução do segundo dos dois "próximos passos declarados" de
H-115 — formalizar "falha da WCC em escala ℓ ⟹ configuração tipo
Z-number para ×2 mod 3^s", via a técnica de Littlewood-Offord/Bohr sets
citada em H-124. Consulta ao Fable para dar rigor de "lema de paper".

## Correção de referência (item verificado pelo Fable)

"Tao 2011" não é um paper — é o **post de blog** "The Collatz
conjecture, Littlewood-Offord theory, and powers of 2 and 3"
(terrytao.wordpress.com, 25/08/2011). Conteúdo relevante: Prop. 4
(reformulação da conjectura fraca de Collatz via evitação de
paralelepípedos em Z/qZ), Prop. 6/7 (condicionais, via Fourier +
produtos de Riesz + concentração em conjuntos de Bohr, dão
2^a-3^k ≫ (1+ε)^k para ε>0 absoluto PEQUENO — guardar este "ε
pequeno", é a mesma parede de constantes da Proposição C abaixo).
Lema 5 do próprio post: Baker dá incondicionalmente algo mais forte,
então o próprio Tao trata o exercício como metodológico, não como
resultado novo. Máquinaria importada: desigualdade de concentração de
Esséen e método de Halász (Halász 1977); teoria inversa de
Littlewood-Offord (Tao-Vu, Annals of Math. 169, 2009; Nguyen-Vu, Adv.
Math. 226, 2011). "Z-numbers" clássicos são de Mahler (1968, problema
em aberto sobre potências de 3/2); resultado parcial relevante:
Flatto-Lagarias-Pollington (1995). O parente estrutural mais próximo do
NOSSO objeto (×2 mod 3^s, não ×3/2 mod 1) é Erdős (1979) e Lagarias
(J. London Math. Soc. 79, 2009, "Ternary expansions of powers of 2").
**Nenhuma destas referências foi baixada/lida nesta sessão** — vieram
do conhecimento do Fable; candidatas a checagem futura se este lema for
usado no paper, mesmo tratamento dado às referências de H-115 (Mauduit-
Rivat et al.).

## Definições formais

Notação de H-114 (WCC de Wirsching): para j≥ℓ, R_{j-1,j} mod 3^ℓ =
2^{j-ℓ}·R_{ℓ-1,j} mod 3^ℓ (twist de unidade), R_{ℓ-1,j} = somas
Σ2^{α_i}3^i com expoentes decrescentes em [0,j+ℓ-1], |R_{ℓ-1,j}| =
C(j+ℓ,ℓ). μ_{ℓ,j} := lei de Y=ΣR mod 3^ℓ; μ̂(ξ) seus coeficientes de
Fourier.

**Def. 1 (falha-(ℓ,c))**: para c>0, a WCC falha na escala ℓ com margem
c se para j=⌈(1+c)·log₄3·ℓ⌉ existe b∈(Z/3^ℓZ)* fora da imagem de
R_{j-1,j}. Por monotonicidade em j (R_{ℓ-1,j}⊆R_{ℓ-1,j+1}), falha com
margem c implica falha para todo j′≤j.

**Parâmetro de inclinação**: γ_c := (j+ℓ)/ℓ = 1+(1+c)·log₄3 ≈
1,7925+0,7925c.

**Def. 2 (configuração diagonal (γ,δ,η) de profundidade s)**: ξ∈Z,
3∤ξ, tal que em ≥(1-η)s escalas t∈{1,...,s} existe a∈[γt-t^{2/3},
γt+t^{2/3}] com ‖ξ·2^a/3^t‖<δ.

**Lema 0 (trivialidade pré-wrap)**: para ξ=1, ‖2^a/3^s‖<δ vale
trivialmente para a ≤ log₂3·s+log₂δ (representante ainda não deu a
volta). O conteúdo aritmético começa em a>log₂3·s≈1,585s. **Nossa
inclinação γ_c≥1,7925>log₂3 para todo c≥0** — a configuração forçada
vive inteiramente no regime pós-wrap não-trivial, por folga
estrutural vinda da contabilidade de entropia 4^j vs 3^ℓ.

**Def. 4 (concentração espectral SC(ε))**: μ_{ℓ,j} satisfaz SC(ε) se
existe ξ≢0 mod 3^ℓ com |μ̂_{ℓ,j}(ξ)| ≥ 3^{-εℓ}.

## Lema B — a redução, honesta

**Lema B (redução condicional)**: para c>0 e ε<ε₀(c) existem
δ(ε,c)<1/2, η(ε,c)<1 tais que: falha-(ℓ,c) da WCC **e** SC(ε) ⟹ existe
(γ_c,δ,η)-configuração diagonal de profundidade s≥(1-O(ε))ℓ.
Contrapositiva: ausência de configurações diagonais de inclinação γ_c
em profundidade grande ⟹ toda falha-(ℓ,c), se existir, é
espectralmente DIFUSA (viola SC(ε) para todo ε).

**Esboço**: (1) buraco ⟹ Σ_{ξ≠0}|μ̂(ξ)|≥1 por inversão de Fourier;
SC(ε) promove isso a existência de UM ξ com massa ≥3^{-εℓ}. (2) modelo
de gaps tilted (parâmetro p_c=1/γ_c) transfere estimativas do modelo
i.i.d. para μ_{ℓ,j} com perdas polinomiais. (3) extração de
paralelepípedos (dispositivo do post de 2011): gaps≥2 são
"alternáveis" (trocar α_i↦α_i+1 soma w_i=2^{α_i}3^i), densidade
ρ≈0,25-0,3 sob p_c; produto de Riesz dá |μ̂(ξ)| ≤ E_v
exp(-2Σ‖ξw_i/3^ℓ‖²). (4) Halász: SC(ε) ⟹ para fração ≥1-O(√ε) das
bases, no máximo η·ρℓ geradores têm ‖·‖≥δ — exatamente a Def. 2 após
reindexar por escala. (5) descida de escala (rotina). (6) upgrade
diagonal⟹segmento contínuo: **lacuna declarada** — precisa de
estabilidade do espectro sob j′↦j′+1, plausível mas não escrita.

## Proposição C — a parede das constantes (o resultado negativo próprio desta hipótese)

**(a) Halász puro**: incondicionalmente só τ≥3^{-ℓ} (não SC(ε)), dando
orçamento Σ‖·‖²≤0,549ℓ contra teto necessário 0,25ℓ (δ=1/2,
d=ℓ geradores) — **déficit ≥2,2×**; com densidade realista ρ≈0,3,
déficit ≈7×. No post de 2011 isso fecha porque lá log q ≪ d
(razão ilimitada); na WCC log₂q/d ≥1,6 — **a técnica não degrada,
inverte de sinal**.

**(b) Identidade exata via fórmula de Jensen**: fatorando por escalas
(esqueleto da Seção 7 de Tao 2022), o expoente de decaimento
"anelado" (fases independentes, benchmark pseudoaleatório) satisfaz

> Λ = E_U log|p·e(U)+(1-p)Z′| = log p sempre que |Z′|≤p/(1-p)
> (que vale automaticamente para p≥1/2, i.e. γ≤2) — identidade EXATA
> de Jensen, não estimativa.

Logo **Λ = log γ_c ≈ 0,5834+O(c), contra o necessário log 3 ≈
1,0986**. Confirmado por Monte Carlo nesta sessão (8×10⁶ amostras):
0,58344±0,0005 no modelo tilted (script `lambda_mc.py`, gerado pelo
Fable no scratchpad da sessão — **não persistido como experimento
formal**; promover a E-0xx se este resultado entrar no paper). Um
buraco espectralmente difuso satisfaz o orçamento de Fourier com folga
de fator 1,88 — é auto-consistente do ponto de vista ℓ¹, e nenhuma
contagem tipo Littlewood-Offord o exclui. O critério anelado só
inverteria em γ=3 (j≥2ℓ), bem acima do regime da conjectura (j*(ℓ)/ℓ≈
1,2 medido em H-114).

## Heurística de abundância (restrição adicional sobre δ)

Contagem ingênua: não-existência de configurações só é plausível se
(1-η)·log(1/2δ) > log 3, i.e. δ<½·3^{-1/(1-η)} (≈1/6 para η pequeno).
O Lema B só tem conteúdo quando ε é pequeno o bastante para δ(ε,c)
ficar abaixo dessa barra.

## Fragilidades (honestas, na ordem de importância)

1. **É implicação, não equivalência**, e duplamente condicional
   (margem c fixa + SC(ε)). A recíproca não segue.
2. **Não recupera a WCC plena nem β=1**: exclui só falhas com margem
   c fixa; a conjectura de Wirsching vive em j=(1+o(1))log₄3·ℓ, onde
   c→0 degenera os parâmetros (δ→1/2, η→1). O ramo pseudoaleatório —
   o núcleo de β=1 — fica intocado.
3. **Não é o problema de Mahler**: ×2 mod 3^s (profundidade finita,
   janela δ) ≠ ×3/2 mod 1 (órbita infinita, janela 1/2).
   Flatto-Lagarias-Pollington 1995 não se aplica diretamente. A
   ancoragem honesta é Erdős 1979/Lagarias 2009 (ξ=1, pós-wrap) e
   Furstenberg ×2×3 efetivo (ξ geral) — devolvendo ao MESMO endereço
   que H-115 já tinha dado ao regime 3 por outra via. **Nome
   recomendado**: "configuração de Bohr pós-wrap" no enunciado
   formal; "tipo-Z" só na discussão informal, com ressalva explícita.
4. **Lacunas técnicas remanescentes**: tilt/CLT local (rotina);
   estabilidade de ξ em j (não rotina, Etapa 6); quenched vs anelado
   na Prop. C(b) (benchmark é anelado; pior caso quenched é onde
   moram as configurações — coerente com a lógica da dicotomia, mas
   deve ser dito no paper).

## Veredito final e conexão com o resto da linha

O ramo espectralmente difuso — o que a Proposição C mostra ser
inacessível a métodos ℓ¹ tipo Littlewood-Offord — "é exatamente o
núcleo de β=1" (H-124) e da condição L² refutada em H-126/E-100.
**Quarta e quinta articulação independente do mesmo ingrediente que
falta**: endogenia (H-110), WCC (H-112/H-114), β=1 (H-124), condição
L² (H-126), e agora esta dicotomia espectro-concentrado/difuso — todas
convergem no mesmo objeto, nunca provado. Não perseguir o ramo difuso
por esta via: a resposta já é conhecida (mesma parede que H-115
identificou para o regime 3).

## Recomendação para o paper

Enunciar três peças: (i) Lema B com SC(ε) explícita (dicotomia); (ii)
Proposição C com as duas contas (déficit 2,2-7× + identidade de
Jensen Λ=log γ_c) — upgrade real sobre H-124: não só "a técnica de
2011 transfere estruturalmente", mas "transfere e falha por um fator
exato, pela mesma parede que o ε da Prop. 7 do post de 2011 já
denunciava"; (iii) Lema 0 + barra de abundância como sanidade da
definição. **Não** alegar "redução da WCC a Z-numbers" — alegar
"redução do ramo espectralmente concentrado à família
Erdős-Lagarias-Furstenberg, e prova de que o ramo difuso é inacessível
a métodos ℓ¹ tipo Littlewood-Offord".

## Referências

- H-110/H-112/H-114 — endogenia, WCC, teste computacional direto.
- H-115/H-124 — três regimes de precisão, triangulação β=1=WCC.
- H-126 — condição L² (irmã espectral desta dicotomia).
- Tao, post de blog 2011 (Littlewood-Offord/potências de 2 e 3) —
  lido/conferido pelo Fable, não baixado/arquivado nesta sessão.
- Halász (1977), Tao-Vu (2009), Nguyen-Vu (2011), Mahler (1968),
  Flatto-Lagarias-Pollington (1995), Erdős (1979), Lagarias (2009) —
  citados pelo Fable a partir de conhecimento, NÃO verificados/lidos
  nesta sessão; checagem futura se este lema for usado no paper.

## Atualizações

- 2026-07-17: hipótese criada a partir da consulta ao Fable; redução
  formalizada como dicotomia condicional, com resultado negativo
  próprio (Proposição C, identidade de Jensen) explicando o limite da
  técnica.
