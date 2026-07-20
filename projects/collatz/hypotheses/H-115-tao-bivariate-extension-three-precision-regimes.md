# H-115 — Por que a extensão bivariada de Tao não cruza a barreira: três regimes de precisão, e onde cada um vive

Status: fechada — obstrução identificada com precisão matemática; os
dois lemas de próximo passo (regime 2, redução Z-number) foram
executados (ver H-126/H-127) e convergem, por vias independentes, no
mesmo ingrediente faltante do regime 3 — problema aberto reconhecido
da área, não mais perseguido
Criada em: 2026-07-17
Origem: depois de fechar o pacote de publicação (H-109 a H-113) e
esgotar 7 rodadas de tentativas de "importar maquinaria de outra área"
(Kesten, Furstenberg, Martin, conspiração 2-ádica, Bourgain-Garaev-
Konyagin, Breiman sem independência, Bilu/Chambert-Loir, Bourgain-
Gamburd — todas refutadas), o diretor científico pediu uma tentativa
séria (não mais uma rodada de consulta) de avaliar a extensão bivariada
de Tao (2022) — a única rota que sobreviveu a todas as rodadas
anteriores como "genuinamente viva". Isso exigiu ler a Seção 7 inteira
da prova de Tao (o mecanismo real, não só o enunciado da Proposição
1.17) e formular uma pergunta precisa ao Fable a partir dessa leitura.

## O que a leitura da Seção 7 revelou

O mecanismo de Tao (caracteres χ_ξ, pares de valuações b_j~Pascal
i.i.d., fase θ(j,l) evoluindo multiplicativamente por log9/log2,
"conjunto preto" = união de triângulos bem separados, processo de
renovação bidimensional com holding time, indução decrescente com
monotonicidade) opera INTEIRAMENTE sobre Syrac(ℤ/3ⁿℤ), definida como
i.i.d. Geom(2)ⁿ **por construção** (equação 1.22 do paper) — não uma
aproximação. A ligação com inteiros reais é feita em outro lugar do
paper (Prop. 1.9: aproximação em variação total, erro exponencial,
válida só para profundidade n≲log(N); Remark 1.10: identidade exata no
limite de Haar 2-ádico).

## A percepção central (formulada nesta sessão, confirmada e aprofundada pelo Fable)

Para o NOSSO problema (árvore reversa, um único v fixo, duas folhas
irmãs w_1(v), w_2(v)), as "duas folhas" NÃO são duas amostras i.i.d. de
um processo — são duas FUNÇÕES DETERMINÍSTICAS DIFERENTES da MESMA
variável v. Isso é qualitativamente diferente do objeto de Tao.

**Achado do Fable, mais forte que a percepção original**: para um PAR
FIXO de caminhos-irmãos (profundidade D), a congruência de existência
(bridge exato de H-111) pina v numa única classe mod 3^D — escrevendo
v=v₀+3^D·t, as duas folhas viram FUNÇÕES AFINS da MESMA variável livre
t, com multiplicadores unitários: w_i = w_i(v₀) + 2^{A_i}·t. Consequência:
o par (w_1,w_2) mod 3^ℓ vive numa RETA de tamanho 3^ℓ dentro de
(ℤ/3^ℓ)² — dependência determinística PERFEITA em TODA precisão ℓ≥1,
com uma reta inteira de frequências ressonantes onde a correlação tem
módulo exatamente 1. **"Aplicar Prop. 1.17 duas vezes + independência
condicional dado o ancestral" não é só circular — é FALSO como
enunciado, em qualquer precisão.** Nenhuma rodada anterior (incluindo a
validação do Fable na rodada 5, que chamou isso de "a melhor ideia da
linha") tinha articulado isso com essa precisão.

## Mas existe uma reformulação correta, não-circular — só que com alcance limitado

A quantidade que realmente importa (decorrelação de AGREGADOS de
subárvore entre irmãs, não folha-a-folha) é um enunciado de SEGUNDO
MOMENTO, que se expande em soma sobre PARES DE CAMINHOS:

> E_v[Z₁·Z₂] ∝ #{(a,a′) : a₁∈B₁, a′₁∈B₂, Syrac(a)≡Syrac(a′) mod 3^D}

e por Fourier, Cov ∝ Σ_{ξ≠0} S₁(ξ)·S₂(ξ)*, com S_i somas de caracteres
tipo-Syracuse condicionadas no primeiro passo. Aqui NÃO há
circularidade — os dois índices de caminho são independentes por
tautologia da expansão do quadrado, não por hipótese aritmética.

## Três regimes de precisão (o resultado central desta hipótese)

1. **ℓ arbitrário, par FIXO de caminhos**: dependência perfeita, sem
   decaimento possível. Decorrelação só pode vir de média sobre
   caminhos, nunca folha-a-folha.
2. **ℓ = O(log D)**: PROVÁVEL, com a maquinaria da Seção 7 quase
   inalterada (orçamento: |ρ(ξ)|≤C_A·D^{-A} controla a soma sobre
   3^ℓ-1 frequências só se 3^ℓ≪D^{2A}, i.e. módulos polinomiais em D).
   Um lema honesto e alcançável, ainda não escrito.
3. **ℓ≍c·D** (onde vivem a barreira de endogenia, os dígitos frescos e
   a Weak Covering Conjecture de Wirsching, H-112/H-114): exigiria
   decaimento de Fourier EXPONENCIAL (power-saving) uniforme em ξ — a
   Prop. 1.17 dá só super-polinomial, e o método da Seção 7
   estruturalmente não dá mais (as perdas dos triângulos pretos estão
   amarradas às propriedades diofantinas de log3/log2 via a inclinação
   log9/log2). **Este regime é equivalente a um problema aberto
   reconhecido da área**: os análogos estruturais honestos identificados
   pelo Fable são (i) correlações de funções digitais (Mauduit-Rivat/
   Fouvry-Mauduit/Spiegelhofer), (ii) rigidez efetiva ×2×3 de
   Furstenberg (o par (w₁,w₂) é v observado por dois elementos do
   semigrupo afim gerado por x↦(2^a·x−1)/3) — aberto na generalidade
   necessária, e (iii) decaimento de Fourier de medidas auto-similares
   (Syrac é uma medida auto-similar 3-ádica; o decaimento exponencial
   pedido é o análogo 3-ádico de resultados tipo Breuillard-Varjú,
   conhecidos só em casos algébricos especiais). Correlações de funções
   multiplicativas (Elliott/MRT) NÃO são o lar certo (nossos funcionais
   são dirigidos por dígitos/valuações, não multiplicativos).

## Veredito final

A validação anterior do Fable ("extensão bivariada = melhor ideia da
linha", rodada 5) permanece correta EM RELAÇÃO às alternativas
(Kesten, Furstenberg-ingênuo, etc.), mas estava mal escopada: era uma
boa ideia para um lema em precisão logarítmica (regime 2), não uma
rota através da barreira (regime 3). A percepção desta sessão é a
correção que faltava articular.

**Recomendação disciplinada (Fable + concordância)**:
1. **Não perseguir mais o regime 3 por analogia** — a resposta já é
   conhecida (território ×2×3-efetivo/Breuillard-Varjú, ferramenta que
   não existe hoje). Sete rodadas + esta análise convergem nisso.
2. **Trabalho empírico continua valendo** (extensão de H-114 a ℓ≥18-20)
   — dado primário sobre o objeto em precisão plena, exatamente o
   regime que a teoria disponível não alcança.
3. **Opcional, com prazo limitado**: escrever o lema do regime 2
   (decorrelação de agregados irmãos em módulos 3^{O(log D)}) — seria
   o primeiro enunciado teórico POSITIVO e não-refutado desta linha
   inteira, risco baixo, valor modesto mas real, companheiro rigoroso
   do ρ_eff≲0,06 empírico (H-111).

## Pacote final desta linha de pesquisa (estado da arte alcançável)

ρ_eff≲0,06 empírico (H-111) + quadro teórico de três regimes de
precisão, com a obstrução do regime 3 identificada com precisão em vez
de deixada vaga (esta hipótese) + dados diretos sobre a WCC de
Wirsching até ℓ=17, regime assintótico indeterminado (H-114) — coerente,
honesto, e defensável como o limite do que esta investigação alcança
sem resolver um problema aberto reconhecido da área.

## Adendo (2026-07-17, ver H-124): forma mínima nomeada do regime 3

Busca literária dirigida encontrou que o próprio Tao (post de blog,
janeiro 2020, "Equidistribution of Syracuse random variables and
density of Collatz preimages") propôs uma conjectura — **β=1**
(c_n:=inf_b P(Syrac(ℤ/3ⁿℤ)=b) = 3^{-n+o(n)}) — que é, após
verificação estrutural, o MESMO objeto algébrico da Weak Covering
Conjecture de Wirsching (H-112/H-114), numa forma um degrau mais fraca
(WCC ⟹ β=1 essencialmente; β=1 sozinho só dá uma WCC enfraquecida).
β=1 é uma barra mais baixa que o power-saving exigido pelo regime 3
aqui descrito, e MESMO ASSIM está aberta há 6 anos, nunca virou paper.
Isso dá ao regime 3 sua testemunha mais limpa possível: em vez de só
"equivalente por analogia a território ×2×3/Breuillard-Varjú", agora
também "sua forma mínima útil é uma conjectura nomeada do próprio Tao,
não provada". Três articulações quase-equivalentes do mesmo
ingrediente faltante: endogenia (H-110), WCC (H-112), β=1 (H-124) —
nenhuma provada. Ver H-124 para a análise completa.

## Próximos passos declarados (2026-07-17) — antes de escrever o paper

Dois lemas concretos, de baixo risco/custo, identificados ao longo
desta hipótese mas ainda não escritos. Marcados como próxima ação
(não mais rodada exploratória — são fechamentos de pontas já
mapeadas):

1. **Lema do regime 2**: decorrelação de agregados de subárvore (não
   folha-a-folha) em módulos grosseiros 3^{O(log D)}, via contagem de
   pares de caminhos + Prop. 1.14 de Tao (condicionada no primeiro
   passo, uniforme em ξ) — maquinaria da Seção 7 quase inalterada.
   Seria o primeiro enunciado teórico POSITIVO e demonstrado (não só
   medido) desta linha inteira.
2. **Lema de redução Z-number** (da análise de Littlewood-Offord de
   Tao 2011, ver adendo acima): formalizar "falha da WCC em escala ℓ
   com j acima do limiar ⟹ concentração de Bohr dos geradores de
   potências de 2 ⟹ configuração tipo Z-number para ×2 mod 3^s" —
   upgrade de "analogia com problema aberto" para "redução explícita
   a problema aberto nomeado".

Ambos "dias, não semanas" segundo o Fable. Fazer os dois antes de
começar a redação do paper — depois disso, parar de investigar.

## Execução dos dois próximos passos (2026-07-17) — ambos concluídos, ambos com resultado diferente do esperado

**Lema do regime 2 → H-126.** Refutado como esboçado: o orçamento
"|ρ(ξ)|≤C_A·D^{-A} uniforme em ξ" contradiz uma identidade EXATA de
Tao (eq. 1.23, auto-similaridade — não uma estimativa perdida). O que
sobrevive é um teorema de estrutura POSITIVO (a componente grosseira
da covariância de irmãs é exata, não-nula, independente de D — Prop.
2 de H-126, endogenia convertida em fórmula fechada) mais um lema
condicional cuja hipótese (K_∞<∞, medida de Syracuse em L²(Z_3)) foi
testada e **refutada computacionalmente** em E-100 (K_ℓ diverge
linearmente até ℓ=17, incrementos convergindo a ≈0,47 sem sinal de
saturação). Regime 2 não é um degrau mais fácil que o regime 3 — é
irmão dele, com o mesmo ingrediente faltante, agora com refutação
direta em vez de "em aberto".

**Lema de redução Z-number → H-127.** Não é a equivalência limpa
esperada — é uma dicotomia condicional (Lema B): falha da WCC +
concentração espectral ⟹ configuração de Bohr pós-wrap (parente de
Erdős-Lagarias-Furstenberg, não do problema clássico de Mahler); o
ramo espectralmente difuso é inacessível a métodos ℓ¹ tipo
Littlewood-Offord, por uma parede de constantes EXATA (Proposição C,
identidade de Jensen Λ=log γ_c≈0,58 contra o necessário log3≈1,10,
folga de fator 1,88, confirmada por Monte Carlo em E-101). O ramo
difuso inacessível é "exatamente o núcleo de β=1" — mesma parede do
regime 3 e da condição L² de H-126, vista por uma quarta via
independente.

**Consequência para o pacote final**: em vez de dois lemas positivos
fechando pontas, o resultado é uma quinta e sexta articulação
independente do MESMO ingrediente faltante (endogenia H-110, WCC
H-112/H-114, β=1 H-124, condição L² H-126, dicotomia espectral H-127)
— nenhuma provada, todas convergindo. Isso é, honestamente, um
resultado mais forte para o paper do que dois lemas soltos teriam
sido: a convergência de cinco/seis formulações independentes no mesmo
ponto é evidência estrutural de que o ingrediente é real e único, não
um artefato de uma abordagem específica. Ver H-126/H-127 para os
teoremas de estrutura positivos que sobrevivem em cada caso (Prop. 2
de H-126; Prop. C de H-127) — ambos citáveis por si mesmos.

**Próximo passo agora**: nenhum lema pendente. Parar de investigar e
começar a escrever o paper (escopo H-109 a H-127, conforme já
decidido).

## Adendo (2026-07-20): checagem da direção reversa da redução do regime 3

Terceira auditoria do paper apontou que "equivalente em dificuldade"
(thm:regime3) não é uma relação matemática definida, e o paper foi
corrigido para uma redução unidirecional precisa ("Regime 3 é ao menos
tão difícil quanto [Spiegelhofer / rigidez de Furstenberg /
Breuillard–Varjú]"). Isso deixou em aberto, explicitamente, se a
implicação reversa vale (o que fecharia uma equivalência de verdade).
Busca literária dirigida (WebSearch) não achou nenhuma redução
conhecida na direção reversa — nem um resultado que derive decaimento
de Fourier exponencial 3-ádico a partir de correlações de dígitos
base 2/3 tipo Spiegelhofer, nem o inverso. Isso é consistente com o
veredito já registrado nesta hipótese há 7 rodadas: "não perseguir
mais o regime 3 por analogia — a resposta já é conhecida (território
sem ferramenta hoje)". A direção reversa permanece genuinamente aberta
— não é uma lacuna de busca bibliográfica, seria trabalho matemático
novo (uma prova de redução de verdade), fora do escopo de uma
auditoria de correção de texto. A reformulação unidirecional do paper
("ao menos tão difícil quanto") é, portanto, a mais forte alegação
defensável no estado atual do conhecimento — não uma perda de rigor,
mas o reflexo exato do que é conhecido.

## Referências

- H-110/H-111 — a barreira de endogenia e sua calibração empírica.
- H-112 — checagem de novidade, conexão com a Weak Covering Conjecture.
- H-114 — teste computacional direto da WCC.
- Tao (2022), Seção 7 (item 106 do INDEX) — mecanismo completo lido
  integralmente nesta sessão.
- Análogos estruturais citados pelo Fable (não lidos nesta sessão,
  candidatos a checagem futura se o regime 2 for perseguido):
  Mauduit-Rivat, Fouvry-Mauduit, Spiegelhofer (correlações de funções
  digitais); Bourgain-Lindenstrauss-Michel-Venkatesh e sucessores
  (rigidez efetiva ×2×3); Breuillard-Varjú (decaimento de Fourier de
  medidas auto-similares).
