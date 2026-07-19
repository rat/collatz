# H-127 — Falha da WCC como dicotomia espectral: redução condicional a configurações de Bohr pós-wrap

Status: em revisão — redução real mas mais fraca do que o esboço de
H-115 sugeria; inclui um resultado negativo próprio (Proposição C, com
identidade exata via fórmula de Jensen, agora com verificação Monte
Carlo formal em E-106) explicando por que a técnica não fecha no
regime da WCC. Atualização 2026-07-19: o Lema B (a redução em si, não
a Proposição C) está mais fraco do que se pensava — a Etapa 6
("upgrade diagonal⟹segmento contínuo") não é lacuna técnica de rotina,
é o conteúdo todo do lema, e não fecha por nenhuma das duas rotas
tentadas (mesma parede de constantes da Prop. C, terceira aparição); a
Definição 2 sem esse upgrade é vazia (verificado, E-107). Ver seção
"Lema B" para a análise completa.
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

**ATUALIZAÇÃO (2026-07-19) — Etapa 6 investigada a fundo (consulta ao
Fable + verificação numérica própria): a lacuna é mais séria do que
"detalhe técnico a preencher". Três achados, em ordem de importância.**

**(i) Correção ao meu próprio diagnóstico**: a multiescala da Def. 2
NÃO precisa de estabilidade em j. Os geradores do produto de Riesz são
w_i=2^{α_i}·3^i, e ‖ξ·w_i/3^ℓ‖=‖ξ·2^{α_i}/3^{ℓ-i}‖ — pondo t=ℓ-i, um
ÚNICO ξ já produz a condição em todas as escalas t=1,...,ℓ
simultaneamente, porque a condição na escala t só depende de ξ mod 3^t
(a graduação 3-ádica interna da soma fornece as escalas de graça). Isso
simplifica o quadro, mas não fecha a lacuna — só muda onde ela mora.

**(ii) Achado principal: a Definição 2, como está escrita, é VAZIA —
satisfeita por ξ genérico, incluindo ξ=1.** Verificado numericamente
(`experiments/E-107-h127-def2-vacuity-check/`, s=300, γ=γ₀, ξ∈{1,5,7,
5 aleatórios ~2^200}): em δ=1/6 e δ=1/10, fração de escalas com "hit"
= 0,97-0,997 para TODOS os ξ testados, sem diferença entre ξ=1 e ξ
aleatório. O conteúdo de rigidez não está em "ter um hit por escala"
(típico, sem custo), mas num **segmento contínuo encadeável** — um run
de escalas consecutivas com expoentes a_t monótonos e incrementos
limitados (B=⌊log₂(1/2δ)⌋). O maior run encadeável medido ficou em 5-9
para TODO ξ testado (incluindo ξ=1), consistente com o Θ(log s)
previsto para ξ genérico (log 300≈5,7) — sem vantagem para ξ
estruturado. **Conclusão**: o Lema B, usando a Def. 2 tal como
escrita, não exclui nada — conclui algo que vale para quase todo ξ.
O objeto com conteúdo é o segmento encadeado de comprimento ≫log ℓ, e
é exatamente esse upgrade que a Etapa 6 precisaria fornecer.

**(iii) As duas rotas para fechar a Etapa 6, e por que nenhuma fecha
com as ferramentas em jogo**:

- *Rota estabilidade-em-j* (a que eu tinha em mente originalmente):
  **não fecha**. A relação entre μ_{ℓ,j} e μ_{ℓ,j+1} não é convolução
  por medida fixa — é a divisão de Pascal C(j+ℓ+1,ℓ)=C(j+ℓ,ℓ)+C(j+ℓ,
  ℓ-1), dando μ_{ℓ,j+1}=(1-q)μ_{ℓ,j}+q·(translação/imagem por ×3 de
  μ_{ℓ-1,j+1}), q=ℓ/(j+ℓ+1)≈1/γ. Em Fourier isso é MÉDIA CONVEXA com
  pesos Θ(1), não produto — com coeficientes de ordem 3^{-εℓ}, o ξ que
  concentra massa em j pode migrar livremente para j+1 sem controle;
  nada no produto de Riesz, Halász ou modelo tilted restringe essa
  migração. SC(ε) é fraca demais para dar essa rigidez.
- *Rota encadeamento intra-j*: fecha só até comprimento O(1/η(ε)) —
  uma CONSTANTE, não crescente com ℓ. O conteúdo começa em runs ≫log ℓ;
  entre O(1) e log ℓ há um abismo que exigiria ε→0 com ℓ, fora do
  regime SC(ε) com ε constante. **É a mesma parede de constantes da
  Proposição C, aparecendo pela terceira vez.**

**Erro adicional identificado no item (4) do esboço** (registrado por
honestidade): o quantificador "fração ≥1-O(√ε) das bases" é do regime
clássico de Halász (|μ̂|≥1-ε). No regime SC(ε) (|μ̂|≥3^{-εℓ}, massa
exponencialmente pequena, não próxima de 1), Markov só dá um conjunto
de bases boas de medida ≥~3^{-εℓ} — **exponencialmente raro**, não
típico. Consequência: propriedades em escala fina (a janela t^{2/3} da
Def. 2) não são herdáveis contra um conjunto 3^{-εℓ}-raro; só
sobrevivem propriedades de grandes desvios com taxa >ε·log3 — corredor
de largura ~√ε·ℓ, não t^{2/3}. Ou seja: mesmo os itens 1-5 "já feitos"
provam uma versão mais fraca da Def. 2 do que a escrita.

**Coerência que fortalece o diagnóstico**: a barra de encadeamento
δ<2^{-γ}/2≈0,144 e a barra de abundância já existente em H-127 (δ<1/6≈
0,167, seção "Heurística de abundância" abaixo) são essencialmente o
mesmo número por caminhos diferentes — a heurística de abundância já
estava, sem dizer, contando o objeto ENCADEADO, não o objeto que os
itens 1-5 realmente provam. A distância entre esses dois objetos É a
Etapa 6.

**Veredito (recomendação do Fable, aceita)**: não tentar escrever essa
prova — não é questão de redação, é um obstáculo estrutural (parede de
constantes pela terceira vez). **Etapa 6 reclassificada de "lacuna
técnica, plausível" para "problema em aberto explícito, com mecanismo
de por-que-não-fecha identificado para ambas as rotas tentadas."**

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
1,0986**. Confirmado por Monte Carlo (8×10⁶ amostras): 0,58344±0,0005
no modelo tilted — script promovido a experimento formal em
[`E-106-h127-jensen-lambda-monte-carlo`](../experiments/E-106-h127-jensen-lambda-monte-carlo/README.md)
(2026-07-19; sobrevivia só em scratchpad de sessão até então). Um
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
   **Etapa 6 (upgrade diagonal⟹segmento contínuo)** — investigada a
   fundo em 2026-07-19 (ver seção "Lema B" acima): não é lacuna
   técnica de rotina, é a etapa que carregaria todo o conteúdo do
   lema, e não fecha por nenhuma das duas rotas tentadas (estabilidade
   em j esbarra na média convexa de Pascal; encadeamento intra-j só dá
   comprimento O(1/η), constante) — mesma parede de constantes da
   Proposição C, terceira aparição. A Definição 2 sem esse upgrade é
   vazia (verificado numericamente, E-107); quenched vs anelado na
   Prop. C(b) (benchmark é anelado; pior caso quenched é onde
   moram as configurações — coerente com a lógica da dicotomia, mas
   deve ser dito no paper).

## Addendum (2026-07-18, busca literária dirigida + consulta ao Fable — H-128)

**Baker & Banaji (2026), "Self-similar and self-conformal measures with
slow Fourier decay" (arXiv:2602.05593)**: provam a existência de
medidas autossimilares/autoconformais Rajchman SEM taxa uniforme de
decaimento de Fourier, para qualquer taxa-alvo arbitrariamente lenta.
Consulta ao Fable para avaliar se essa maquinaria (ou o critério de
Brémont subjacente) se transfere para a medida de Syracyse — resultado
mais rico e mais honesto do que a primeira leitura sugeria:

1. **Correção de enquadramento**: a medida de Syracuse É literalmente
   uma medida autossimilar em Z_3 — desenrolando a recursão de
   renovação, X = Σ_{k≥1} 3^{k-1}·2^{-S_k} (S_k = a_1+...+a_k), ponto
   fixo do IFS afim contável φ_a(x)=2^{-a}(1+3x) em Z_3, todos os mapas
   com razão ultramétrica |3·2^{-a}|_3=1/3. "Não é um IFS" (leitura
   inicial) era impreciso; é IFS 3-ádico contável, com overlaps
   massivos.
2. **Por que a ponte não ajuda mesmo assim**: o mecanismo de
   Teo. 1.11/Cor. 1.12 (fase estacionária arquimediana, f''≠0) daria no
   máximo Rajchman qualitativo — estritamente mais fraco que o
   decaimento super-polinomial já garantido pela Prop. 1.17 de Tao. E o
   critério de Pisot de Brémont, no análogo 3-ádico, **trivializa por
   rigidez estrutural**: todo subgrupo fechado infinito de Z_3^× tem
   índice finito (subgrupos fechados de (Z_3,+) são 3^kZ_3) — não há
   espaço para uma "órbita multiplicativa fina" tipo Pisot. Como 2 é
   raiz primitiva mod 3^n para todo n, as fases unitárias 2^{-a} se
   espalham ao máximo — exatamente o input aritmético que a prova de
   Tao já explora. Nenhuma classificação tipo Brémont 3-ádica publicada
   foi encontrada; a literatura de Fourier p-ádico existente (Salem
   sets em corpos locais, Fuglede em Q_p) é de outra natureza.
3. **Status da Prop. C, com ressalva honesta**: Baker-Banaji é citável
   como "taxa uniforme de decaimento não é de graça, mesmo para medidas
   estruturadas" (legitima a moldura: qualquer prova de β=1/WCC precisa
   do input aritmético específico, não vem de suavidade genérica). MAS
   não deve ser sobre-interpretado como suporte ao cenário: o fenômeno
   deles vem de sintonia fina de um parâmetro (tipo Liouville — denso
   na família, excepcional em medida; típico dá decaimento polinomial,
   Solomyak/Varjú-Yu); a medida de Syracuse é um objeto aritmético
   RÍGIDO sem parâmetro sintonizável, e a rigidez de Z_3^× do item 2
   mostra que o mecanismo habilitador (aproximação diofantina fina em
   R) simplesmente não existe do lado 3-ádico — o que corta CONTRA o
   cenário da Prop. C tanto quanto a favor. Citar com a disanalogia
   explícita, não como evidência.
4. **Subproduto que vale registrar** (não um lema, meia página no
   paper): a reformulação autossimilar de X acima + a observação de
   rigidez (subgrupos fechados de Z_3^× de índice finito ⟹ não existe
   obstrução tipo Pisot 3-ádica ⟹ por que a maquinaria arquimediana de
   decaimento lento não transporta) posiciona a Prop. C corretamente no
   mapa da literatura e antecipa a objeção óbvia de um referee de
   análise harmônica.

Ver H-128 para a busca completa (inclui também Chang 2026, sétima
articulação independente do mesmo ingrediente faltante, testada
computacionalmente em E-102).

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

**Atualizada em 2026-07-19 após a investigação da Etapa 6** (ver seção
"Lema B" acima): o Lema B como originalmente enunciado (Def. 2 sem o
encadeamento) **não deve ir para o paper como está** — é vazio de
conteúdo (E-107). Duas opções honestas: (a) reformular o Lema B usando
a definição correta, com o segmento ENCADEADO em vez da configuração
diagonal solta, e declarar a Etapa 6 (existência desse segmento
encadeado de comprimento ≫log ℓ) como problema em aberto explícito,
com o mecanismo de por-que-não-fecha documentado (rota j-estabilidade:
média convexa de Pascal; rota intra-j: comprimento O(1/η) constante);
ou (b) não incluir o Lema B no paper por ora, e reportar só a
Proposição C (que não depende da Def. 2 e permanece válida como
resultado negativo próprio, incluindo agora a identidade de Jensen
verificada em E-106).

Peças que SOBREVIVEM intactas e valem para o paper independente do
destino do Lema B: (i) Proposição C com as duas contas (déficit 2,2-7×
+ identidade de Jensen Λ=log γ_c, agora com verificação Monte Carlo
formal em E-106) — upgrade real sobre H-124: não só "a técnica de
2011 transfere estruturalmente", mas "transfere e falha por um fator
exato, pela mesma parede que o ε da Prop. 7 do post de 2011 já
denunciava, e que reaparece uma terceira vez na Etapa 6 do Lema B";
(ii) Lema 0 + barra de abundância como sanidade da definição; (iii) o
próprio achado da vacuidade da Def. 2 (E-107) é, honestamente, mais
uma articulação quantitativa da mesma parede — vale registrar no paper
como tal. **Não** alegar "redução da WCC a Z-numbers" — alegar
"redução do ramo espectralmente concentrado à família
Erdős-Lagarias-Furstenberg, e prova de que o ramo difuso é inacessível
a métodos ℓ¹ tipo Littlewood-Offord" (isso continua correto,
independente do destino do Lema B).

## Referências

- H-110/H-112/H-114 — endogenia, WCC, teste computacional direto.
- H-115/H-124 — três regimes de precisão, triangulação β=1=WCC.
- H-126 — condição L² (irmã espectral desta dicotomia).
- Tao, post de blog 2011 (Littlewood-Offord/potências de 2 e 3) —
  lido/conferido pelo Fable, não baixado/arquivado nesta sessão.
- Halász (1971 — não 1977, ver correção abaixo), Tao-Vu (2009),
  Nguyen-Vu (2011), Mahler (1968), Flatto-Lagarias-Pollington (1995),
  Erdős (1979), Lagarias (2009) — ver "Atualizações" para o resultado
  da verificação bibliográfica (2026-07-18).

## Atualizações

- 2026-07-17: hipótese criada a partir da consulta ao Fable; redução
  formalizada como dicotomia condicional, com resultado negativo
  próprio (Proposição C, identidade de Jensen) explicando o limite da
  técnica.
- **2026-07-18: verificação bibliográfica das 7 referências citadas de
  memória pelo Fable, concluída.** Diretor científico baixou 6 PDFs;
  arquivados em `literature/papers/` (itens 139-144 do INDEX.md).
  Resultado:
  - **Tao-Vu (2009), Nguyen-Vu (2011), Flatto-Lagarias-Pollington
    (1995), Mahler (1968), Lagarias (2009)**: confirmados contra o
    texto primário. Destaque: a definição exata de Z-number no Mahler
    (α é Z-number sse 0≤r_n<1/2 para todo n, α(3/2)ⁿ=q_n+r_n) bate
    exatamente com a descrição usada aqui; a citação de Erdős (1979)
    foi confirmada não pelo PDF dele diretamente (não localizado como
    paper independente), mas por estar corretamente listada como
    referência [4] no próprio Lagarias (2009): "P. Erdős, Some
    unconventional problems in number theory, Math. Mag. 52(2) (1979),
    67-70" — ano e atribuição do Fable estavam certos.
  - **Halász**: o ANO estava errado na citação original desta hipótese
    ("1977") — o correto é **1971** (Studia Scientiarum Mathematicarum
    Hungarica 6, 211-233), o que só percebemos ao tentar verificar.
    O PDF baixado (item 144) é na verdade um adendo/errata de 1972 do
    próprio Halász ao paper de 1971 ("Remarks to my paper..."), não o
    original — **ainda falta obter o paper de 1971 de verdade** antes
    de citar com segurança. Este episódio é o exemplo concreto de por
    que a verificação valia a pena: um erro real (ano) só apareceu ao
    tentar confirmar.
- **2026-07-18 (fechamento)**: diretor científico buscou o original de
  1971 em HathiTrust, Internet Archive, JSTOR e acervos institucionais
  húngaros — não encontrado em digitalização aberta. Fica como
  **irresolvível por ora**: a referência bibliográfica em si (título,
  ano, volume, páginas) segue independentemente corroborada por várias
  fontes secundárias (catálogos, citações), mas o texto primário nunca
  foi lido por nós. `main.tex` atualizado para refletir isso com
  honestidade (nota explícita, não apagada). Nesta mesma passada,
  identificadas e corrigidas mais duas referências sem precisar de
  novo download: **Gonçalves-Greenfeld-Madrid (2022)** tinha título
  inventado/errado na bibliografia do paper (corrigido contra o PDF já
  arquivado, item 128 do INDEX); **Brémont (2021)** teve volume/páginas
  confirmados e o Teorema 2.5 citado pelo Fable verificado
  integralmente contra o texto completo (arXiv:1910.03463) — bate
  exatamente. Zeladoria bibliográfica de H-127 **encerrada**: 8 de 9
  referências verificadas, 1 (Halász 1971) documentada como
  inacessível, não como esquecida.

- **2026-07-19 — Duas pendências executadas: `lambda_mc.py` promovido
  a experimento formal (E-106); Etapa 6 investigada a fundo, resultado
  é um retrocesso real e bem entendido, não um avanço.**

  Pedido explícito do diretor científico para avançar H-127. Duas
  ações:

  1. **Promoção de `lambda_mc.py`** (Monte Carlo da identidade de
     Jensen da Proposição C(b), até então só em scratchpad de sessão)
     para [`E-106-h127-jensen-lambda-monte-carlo`](../experiments/E-106-h127-jensen-lambda-monte-carlo/README.md).
     Reproduz exatamente o valor já citado (Λ=0,5834±0,0005 vs.
     log(γ₀)=0,5836 previsto). Mecânico, sem novidade matemática.

  2. **Tentativa de fechar a Etapa 6** (upgrade "configuração
     diagonal"⟹"segmento contínuo" no Lema B, marcada como "plausível
     mas não escrita"). Consultei o Fable com contexto completo antes
     de tentar escrever a prova — a resposta, verificada numericamente
     por mim de forma independente (script reproduzido, mesmos
     números), foi mais séria do que uma lacuna técnica:
     - A Definição 2 (configuração diagonal), como estava escrita, é
       **vazia** — satisfeita por ξ genérico, incluindo ξ=1 (agora
       [`E-107-h127-def2-vacuity-check`](../experiments/E-107-h127-def2-vacuity-check/README.md)).
       O objeto com conteúdo real é um segmento ENCADEADO de
       comprimento ≫log ℓ, não a configuração diagonal solta.
     - As duas rotas possíveis para fornecer esse upgrade **não
       fecham** com as ferramentas em jogo: estabilidade em j esbarra
       numa média convexa de Pascal (não uma convolução — o ξ
       maximizante pode migrar livremente entre j e j+1, sem controle
       do produto de Riesz/Halász); encadeamento intra-j só dá
       comprimento O(1/η(ε)), uma constante, não crescente com ℓ.
     - Isso é a mesma "parede de constantes" da Proposição C,
       aparecendo pela terceira vez — não uma falha isolada.
     - Um erro adicional de quantificador no item (4) do esboço
       original (regime SC(ε) dá bases boas de medida
       exponencialmente rara ~3^{-εℓ}, não a fração ≥1-O(√ε) do regime
       clássico de Halász) também foi identificado e documentado.

  **Avaliação honesta**: isso é um retrocesso real no Lema B
  especificamente (não na Proposição C, que permanece intacta e agora
  mais bem verificada) — mas é um retrocesso BEM ENTENDIDO, com
  mecanismo exato identificado para ambas as rotas tentadas, e não fica
  como "não tive tempo de escrever" e sim como "tentei, e há uma razão
  estrutural específica para não fechar". Seguindo a recomendação do
  Fable (não insistir em escrever a prova nesta sessão — o problema não
  é de redação), reclassifiquei a Etapa 6 de "lacuna técnica plausível"
  para "problema em aberto explícito" e atualizei a seção "Recomendação
  para o paper" para não propor mais o Lema B como está.

  **Status de H-127**: continua "em revisão". A Proposição C (o
  resultado negativo, agora com E-106) segue como a peça mais sólida
  desta hipótese. O Lema B precisa ou de reformulação (definição
  correta + Etapa 6 como problema aberto explícito) ou de não entrar no
  paper por ora — ambas as opções são honestas, nenhuma é um
  fechamento.
