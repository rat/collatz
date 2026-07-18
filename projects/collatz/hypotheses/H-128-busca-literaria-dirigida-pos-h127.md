# H-128 — Busca literária dirigida em ângulos não visitados (pós-H-127)

Status: fechada — os dois testes pedidos pelo diretor científico (Baker-Banaji via consulta ao Fable; Chang via experimento computacional E-102) foram realizados; nenhum "mata a charada", mas ambos produziram achados honestos e citáveis
Criada em: 2026-07-18

## Enunciado

Depois de fechar H-126/H-127 (os dois lemas pendentes de H-115) sem
lema positivo limpo, o diretor científico pediu uma busca na web em
ângulos ainda não tentados atrás de algo que ajude a explicar a linha
G(v)/qx+1/endogenia. Buscas cobriram: decaimento de Fourier de medidas
autossimilares sem condição de separação (Hochman-Shmerkin e
descendentes), Breuillard-Varjú (entropia de convoluções de Bernoulli),
a resolução da conjectura ×2×3 de Furstenberg (Wu 2019, Shmerkin 2019),
progresso recente citando Tao (2022)/Wirsching, e a própria Weak
Covering Conjecture.

## Achado 1 (o mais citável): Baker & Banaji (2026), "Self-similar and
self-conformal measures with slow Fourier decay" (arXiv:2602.05593)

Prova a EXISTÊNCIA de medidas autossimilares e autoconformais C^∞ que
são Rajchman (coeficientes de Fourier → 0) mas SEM taxa uniforme de
decaimento — para qualquer taxa-alvo φ(ξ)→0 arbitrariamente lenta,
existe uma medida legítima da classe com |μ̂(ξ)| ≥ c·φ(ξ) para
infinitos ξ. Ou seja: "Rajchman sem taxa uniforme" é um fenômeno
GENÉRICO e sistemático na literatura de dinâmica/análise harmônica, não
uma patologia isolada.

**Por que isso importa para H-127**: a Proposição C mostra, via
identidade de Jensen, que o orçamento de Fourier anelado da nossa
medida (no regime da WCC) cabe sem estrutura extra — um "buraco"
espectralmente difuso é auto-consistente do ponto de vista ℓ¹. Até
agora essa era uma conclusão isolada de um cálculo específico. Baker &
Banaji dão o contexto geral: mostram que medidas Rajchman com
decaimento arbitrariamente lento REALMENTE EXISTEM como construções
explícitas noutras famílias (autossimilares/autoconformais gerais) —
não prova nada sobre a medida de Syracuse especificamente, mas remove
qualquer suspeita de que nosso resultado negativo seja um artefato
numérico: o tipo de falha que Prop. C exibe tem precedente estrutural
sólido e recente na literatura de referência. Citação a adicionar em
H-127 (seção de fragilidades/heurística de abundância).

## Achado 2: Chang (2026), "A Structural Reduction of the Collatz
Conjecture to One-Bit Orbit Mixing" (arXiv:2603.25753, Stanford)

Reduz a conjectura de Collatz — por via puramente combinatória/modular
(mapa comprimido ímpar-a-ímpar, decomposição exata em profundidades
K=3,4,5, sem Fourier nem medida nenhuma) — a uma condição de "balanço"
de duas classes residuais mod 32 ao longo de uma subsequência esparsa
da órbita ("bit 4 do valor da órbita em tempos de fim-de-rajada").
Prova um "Map Balance Theorem" (o viés é todo de nível-órbita, não de
nível-mapa — as contagens ao nível do mapa diferem por exatamente 1).
A condição remanescente é conjecturada, não provada.

**Por que isso importa**: é uma SÉTIMA articulação independente do
mesmo tipo de ingrediente faltante (equidistribuição/balanço de
resíduos ao longo da órbita real, não da medida ensemble) — via uma
técnica completamente diferente (contagem combinatória exata em vez de
Fourier/Littlewood-Offord/endogenia). Reforça a tese central do pacote
de publicação: não é artefato de uma abordagem, aparece em qualquer
formalismo que se tente. Vale uma menção en passant no paper final
(nota de rodapé ou parágrafo de "outras articulações independentes"),
sem precisar avaliar/validar o teorema técnico do paper em si (fora do
escopo desta linha).

## Achado 3 (tangencial, baixo valor direto): Siegel, série "The Collatz
Conjecture & Non-Archimedean Spectral Theory" (arXiv:2007.15936,
2111.07883, 2208.11082, 2020-2023)

Programa de pesquisa real e independente: "(p,q)-adic analysis" (funções
dos p-ádicos para os q-ádicos) aplicado à família qx+1, incluindo teoria
espectral não-arquimediana e teorema tauberiano de Wiener adaptado.
Nenhuma menção explícita à WCC, a β=1, ou à medida de Syracuse de Tao —
aparato técnico diferente do nosso, sem sobreposição direta detectável
nos abstracts/introduções. Permanece como série de preprints (arXiv
apenas, sem publicação revisada por pares até a versão checada). Não
adotar como referência de apoio direto; mencionar apenas se for útil
mostrar que outros grupos tentam análise espectral 3-ádica/q-ádica
nesta família de mapas.

## Nota de cautela (não investigada a fundo, fora de escopo aqui)

A busca também trouxe à tona um cluster de alegações de "prova
completa algébrica" da Collatz (hospedado em ccchallenge.org,
mecanismo chamado "Fresh 3-Bit Constraint", "seis obstruções
independentes", "rank exhaustion determinístico") — mesmo padrão
recorrente já refutado várias vezes nesta linha (H-043, H-079, H-081,
H-093, H-096, H-123, item 123/Barghout): argumento de contagem
determinística que tipicamente esconde uma etapa estatística/média
confundida com garantia pontual. **Não foi verificado** — decisão
deliberada de não seguir agora, pois cabe no "paper cumulativo de
críticas" (BACKLOG.md item 8), só quando pedido explicitamente. Registro
aqui só para não perder o rastro caso vire relevante depois.

## Como testar

Não há teste computacional novo a rodar aqui — é revisão literária. A
ação concreta é: (1) adicionar a citação Baker & Banaji (2026) à seção
de fragilidades/discussão de H-127; (2) mencionar Chang (2026) na
síntese do paper final como sétima articulação independente, sem
validar seu teorema técnico.

## Teste 1 (Baker & Banaji): consulta ao Fable sobre a ponte 3-ádica

Pedido explícito do diretor científico: "vale testar para confirmar a
falta de explicação — talvez eles matem a charada?". Consultado o
Fable com o enunciado exato dos Teoremas 1.11/1.12/1.2/1.3 do paper e a
recursão da medida de Syracuse. Resultado (detalhado, ver addendum em
H-127):

- A avaliação inicial ("não aplica, IFS finito vs. recursão infinita")
  era imprecisa por um motivo interessante: a medida de Syracuse É uma
  medida autossimilar 3-ádica genuína (IFS contável φ_a(x)=2^{-a}(1+3x)
  em Z_3). O que realmente bloqueia a transferência é mais profundo:
  o mecanismo de Baker-Banaji (curvatura arquimediana / critério de
  Pisot de Brémont) **trivializa 3-adicamente** — todo subgrupo fechado
  de Z_3^× tem índice finito, não há "órbita fina" tipo Pisot possível,
  e 2 ser raiz primitiva mod 3^n é exatamente o oposto estrutural do
  que habilitaria o fenômeno deles.
- **Não mata a charada**: nem ajuda a provar, nem ajuda a refutar nada
  novo — o resultado geral deles (decaimento lento é possível em
  medidas Rajchman estruturadas) exige sintonia fina de um parâmetro
  livre que a medida de Syracuse simplesmente não tem (é um objeto
  aritmético rígido). Citável só como contexto/moldura, com a
  disanalogia declarada — não como evidência a favor do cenário da
  Prop. C.
- **Subproduto real, pequeno**: a reformulação autossimilar explícita
  da medida de Syracuse + o argumento de rigidez de Z_3^× é uma
  observação nova, correta, que vale meio parágrafo no paper (não um
  lema) — explica precisamente por que a "receita genérica" da
  literatura de decaimento lento não se aplica aqui, antecipando a
  objeção óbvia de um referee.

## Teste 2 (Chang): experimento computacional E-102

Testada diretamente a condição de "one-bit orbit mixing" em órbitas
reais (definições exatas extraídas do paper: mapa comprimido
ímpar-a-ímpar, indicador de burst, Prop. 5.1-5.5). Dois desenhos:
ensemble de muitas órbitas moderadas agregadas, e poucas órbitas ÚNICAS
muito longas (até 16000 bits, ~4761 eventos numa só trajetória).

- Validação: nenhum evento fora dos resíduos previstos (9, 25 mod 32)
  em nenhum dos dois testes — bate com Prop. 5.1-5.5.
- Ensemble: desvio de balanço cresce e estabiliza num platô de
  1,2%-1,9% — mas isso é aparentemente artefato de agregar muitas
  órbitas curtas dominadas pela fase inicial, não um viés assintótico
  real.
- Órbita única longa (o teste mais fiel ao enunciado do paper, T→∞
  dentro de UMA trajetória): o desvio acompanha de perto a curva de
  ruído estatístico ~1/√i, sem tendência sistemática, terminando bem
  próximo de zero. **Suporte empírico qualificado à conjectura do
  Chang** na escala testada — não uma prova, mesmo padrão epistêmico
  dos outros testes empíricos desta linha (H-111, H-114).

Ver `experiments/E-102-chang-one-bit-orbit-mixing-test/README.md` para
o relato completo.

## Segunda rodada de busca (pedido explícito: "mais buscas, talvez ache mais contribuição")

Ângulos novos: Fuglede/Salem sets em Q_p (Fan-Fan-Liao-Shi;
Hambrook-Fraser), decaimento de Fourier via renovação quantitativa
(Li-Sahlsten), e transformação de suavização crítica (Kolesko-
Mentemeier 2015). Avaliação:

1. **Fuglede/Salem em Q_p**: análise de Fourier p-ádica real, mas sobre
   problemas diferentes (conjuntos espectrais/tiling, construções via
   aproximação diofantina) — mesma conclusão de sempre, área adjacente
   sem transferência.
2. **Li-Sahlsten (renovação quantitativa)**: mecanismo precisa de DUAS
   razões de contração distintas com relação diofantina entre logs. Na
   medida de Syracuse, todo ramo tem a MESMA razão 3-ádica (1/3) — só a
   fase 2^{-a} varia — então o passeio de escalas é determinístico
   (lattice puro, S_n=n·log3), sem overshoot, sem flutuação: o
   mecanismo degenera pela mesma rigidez de Z_3^× que já matou
   Baker-Banaji. Confirmado pelo Fable, inclusive a variante "usar
   a_i~Geom(2) como passeio" — controla a FASE, não a escala, e cai de
   volta em equidistribuição elementar já conhecida (2 raiz primitiva).
3. **Kolesko-Mentemeier (caso crítico)**: verificação explícita — a
   função de momento m(α)=3^(α-1)/(2^α-1) tem raízes DISTINTAS em α=1 e
   α=2, com m'(2)≈+0,174>0 — não é o caso crítico m'(α)=0 (log-
   convexidade de m implica que duas raízes distintas excluem
   criticidade). O regime correto de α*=2 é "segunda raiz/cauda de
   Goldie", não "boundary case". Mesmo se fosse crítico, o teorema de
   unicidade deles PRESSUPÕE a independência entre subárvores que é
   exatamente o gap aritmético de H-110 — teorema dentro da classe que
   a barreira já cobre condicionalmente, não uma ferramenta nova.

**Veredito da segunda rodada**: nenhuma via nova — os três candidatos
confirmam, por razões técnicas específicas e verificadas (não por
intuição), que a barreira é a mesma em todo lugar que se olha. Único
item acionável (registrado em addendum de H-110): fixar a terminologia
correta de regime (segunda raiz/Goldie, não caso crítico) para não
reavaliar no futuro uma classe de papers (Kolesko-Mentemeier,
Aïdékon-Shi) estruturalmente irrelevante para q=3.

## Atualizações

- 2026-07-18: busca realizada, três achados avaliados, nota de cautela
  registrada. Nenhuma mudança de rumo na linha principal — reforça o
  enquadramento já decidido (barreira bem caracterizada, convergente
  por múltiplas vias independentes) em vez de abrir nova investigação.
- 2026-07-18: pedido explícito de "testar os dois para ver se matam a
  charada". Ambos testados (Fable para Baker-Banaji, experimento E-102
  para Chang). Nenhum resolve nada — confirma, com mais detalhe e
  rigor, que a barreira é real e que os achados de hoje são
  contribuições marginais honestas (uma observação de rigidez 3-ádica
  citável, um teste empírico qualificado a favor de mais uma
  formulação), não um atalho para fechá-la.
