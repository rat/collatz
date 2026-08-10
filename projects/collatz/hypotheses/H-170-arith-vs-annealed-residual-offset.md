# H-170 — O resíduo "logo abaixo de 0,650919" na leitura profunda da árvore aritmética é um efeito real ou ruído dentro do orçamento sistemático já medido?

Status: fechada-inconclusiva (o padrão observado não é distinguível de
zero dentro do orçamento de erro sistemático já quantificado; a
pergunta teórica mais funda que o motivaria continua aberta, mas
pertence a outra frente já rastreada, não a este paper).

Criada em: 2026-08-10.

Origem: Regra 8e. `main.tex` do paper 04
(`04-kontorovich-lagarias-volkov`), na Discussão (§`sec:calibrated`,
parágrafo final), sinaliza duas observações explicitamente como "fora
do escopo deste paper", nunca registradas como hipótese própria:

> "the deep arithmetic-only run above sits systematically at or just
> below $0.650919$, a pattern the data here cannot yet distinguish
> from a slowly converging extrapolation."

Esta é a segunda das duas (Lead B). A primeira (Lead A, sobre a
diferença de viés `0,038` do controle iid contra `0,013` da árvore
aritmética na mesma profundidade) não abre entrada própria: é uma
restatement quantitativa do resultado de variância já fechado em
H-169 ("a congruência de irmãos dá conta da redução de flutuação; não
sobra efeito residual detectável", ver a seção "Separação entre-raízes
versus dentro-de-raiz" daquele arquivo). Os dois números batem com a
tabela da grade `b13` de H-113 §4 (coluna "window estimator", mesma
profundidade para os cinco processos): `0,650919 - 0,61308 = 0,038`
(iid) e `0,650919 - 0,63824 = 0,013` (arith). Nenhuma investigação nova
necessária para Lead A; registrado aqui só para não deixá-la como
menção solta.

## Enunciado (Lead B)

Na tabela de décadas profundas de H-113 §4 (árvore aritmética sozinha,
checkpoints até `1e12`, buffers até `1e17`):

| década | slope | bootstrap | distância a 0,650919 |
|--------|-------|-----------|----------------------|
| 1e7→1e8 | 0,6465 | [0,6425, 0,6506] | 0,0044 |
| 1e8→1e9 | 0,6487 | [0,6467, 0,6506] | 0,0022 |
| 1e9→1e10 | 0,6490 | [0,6479, 0,6499] | 0,0020 |
| 1e10→1e11 | 0,6506 | [0,6502, 0,6510] | 0,0003 |
| 1e11→1e12 | 0,6505 | [0,6503, 0,6508] | 0,0004 |

As duas últimas décadas não continuam encolhendo geometricamente na
direção de zero (0,0020 → 0,0003 → 0,0004): platô, não convergência
contínua. Pergunta: esse platô em `~0,0003-0,0004` abaixo de 0,650919 é
um sinal real (um deslocamento sistemático entre o expoente da árvore
aritmética verdadeira e a raiz da equação de pressão anelada) ou está
dentro do ruído/viés sistemático já quantificado noutro lugar deste
mesmo experimento?

## Investigação (limitada, conforme Regra 8e)

**1. O orçamento de erro sistemático já existe e já cobre esse
tamanho.** `buffer_squeeze.py` (E-139) limita o erro de extrapolação de
truncamento em `0,002`. H-113 §4 já usa esse número para a mesma
tabela: "leia as décadas profundas como `0,6505 ± 0,002` contra
`0,650919` e `0,678`". O platô de `0,0003-0,0004` está um fator de 5 a
6 **dentro** dessa barra de erro. Não há caso estatístico para tratar o
platô como um efeito distinto de zero.

**2. O mecanismo qualitativo já é conhecido e aponta na direção certa,
não contra ela.** H-113 §4 (parágrafo final antes da tabela por
década): a árvore aritmética flutua um pouco menos que os controles de
expoente `0,650919` (`sd` de `log10 N(1e8)`: `0,594` em `arith` contra
`0,629`-`0,801` nos controles); como o viés residual do estimador cresce
com a flutuação do processo, isso implica que o viés próprio da árvore
aritmética deveria ser um pouco *menor* que o dos controles — logo, ler
o mesmo valor absoluto que os controles corresponderia, se alguma
coisa, a um expoente verdadeiro um fio *abaixo* de `0,650919`, não
acima. O texto já registra isso: "o `0,6505` da rodada profunda é
consistente com isso, dentro da incerteza de extrapolação de `0,002`."
Ou seja, o próprio mecanismo que explicaria um deslocamento residual já
prevê um deslocamento pequeno o bastante para estar dentro do mesmo
orçamento de `0,002` do item 1. Não há tensão entre os dois; são a
mesma explicação vista de dois ângulos.

**3. Por que não fechar isso com um teorema de teoria de branching
random walk (quenched = anelado, Biggins/Kingman).** Cogitado e
descartado, com consulta ao advisor. Dois problemas, ambos fatais:

- **Erro de categoria**: teoremas de quenched=anelado (Biggins 1992,
  Kingman) valem para o *modelo estocástico* (branching random walk
  i.i.d.), não para a árvore aritmética, que é determinística — não há
  espaço de probabilidade sobre o qual "quenched" seria sequer
  definido para ela. A transferência do modelo para a árvore aritmética
  é exatamente a lacuna já nomeada neste projeto como O1/O7
  (H-159/H-162, H-157/H-159), não uma ferramenta disponível para
  fechar H-170.
- **H-109 já teve exatamente essa ideia e já documentou por que ela não
  fecha**: "Fable confirmou que Biggins (1992) é genuinamente o
  teorema certo para a região não-congelada de um branching random
  walk genuíno (i.i.d.), mas NÃO cobre nossa recursão aritmética
  diretamente — a lacuna é a mesma independência que já nomeávamos no
  Teorema da barreira". Reaproveitar esse teorema aqui repetiria um
  caminho já fechado como insuficiente noutro lugar do projeto.

Consultar novamente teria sido rodar em círculo; a resposta já estava
escrita em H-109, só não indexada sob este nome.

## Veredito

O platô residual de `0,0003-0,0004` abaixo de `0,650919` nas décadas
mais profundas da árvore aritmética **não é distinguível de zero**
dentro do orçamento de erro sistemático de `0,002` já quantificado em
`buffer_squeeze.py` e já citado em H-113 §4. A frase da Discussão do
`main.tex` ("a pattern the data here cannot yet distinguish from a
slowly converging extrapolation") está certa e não precisa de reforço:
não há aqui evidência de um deslocamento genuíno entre o expoente da
árvore aritmética e a raiz da equação de pressão anelada. A pergunta
teórica mais funda, se um deslocamento desse tipo poderia existir em
princípio para uma recursão não-i.i.d. como esta, é exatamente a lacuna
de transferência já rastreada como O1/O7 nas hipóteses H-159/H-162 e
H-157/H-159 (papers 05/06), fora do escopo deste paper. Fechado como
inconclusivo aqui; não reaberto como pergunta nova nem duplicado nas
frentes O1/O7 já existentes.

## Referências

- H-113 (tabela de décadas profundas, `buffer_squeeze.py`, o mecanismo
  de flutuação menor).
- H-169 (Lead A: redução de variância pela congruência de irmãos, já
  fechada).
- H-109 (Addendum 1, Teste 3): por que Biggins/Kingman não cobre a
  recursão aritmética; a mesma lacuna de independência do Teorema da
  barreira.
- H-159/H-162 (O1), H-157/H-159 (O7): a lacuna de transferência
  modelo-para-árvore em aberto, fora do escopo do paper 04.
