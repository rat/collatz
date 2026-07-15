# Índice de papers — busca Google Scholar "Collatz" (ordenado por data) + adições de outras buscas

Itens 001-100 coletados em 2026-07-13/14, a partir de:
`https://scholar.google.com/scholar?hl=pt-BR&as_sdt=0,5&q=Collatz&scisbd=1`
(10 primeiras páginas de resultados, ~100 itens, ordenados por data de
adição mais recente). Itens 101+ vêm de buscas posteriores (EBSCO,
ScienceDirect) feitas pelo diretor científico, não do Scholar — incluem
tanto papers novos quanto clássicos/referências importantes que a busca
por data recente do Scholar nunca teria capturado (ex: Tao 2022, Barina
2021/2025, De Mol 2008, Andrei & Masalagiu 1998).

## Resumo

- **100 resultados processados** da busca original do Scholar, todas as
  10 páginas navegadas sem nenhum bloqueio/CAPTCHA da própria busca.
  **+14 itens (101-114)** de uma busca posterior via EBSCO/ScienceDirect
  (2026-07-15) — 10 relevantes, 4 excluídos por falso positivo (ver
  abaixo).
- **50 PDFs baixados** com sucesso (arquivo local na tabela; coluna Link
  mostra "BAIXADO" em vez do link original, já que o link só serve para
  indicar onde baixar) — 15 pela automação do navegador/Scholar, +16
  baixados manualmente pelo diretor científico em 2026-07-14, +1 em
  2026-07-15 (item 001), +7 em 2026-07-15 (itens 022, 023, 024, 025, 030,
  035, 037), +10 em 2026-07-15 via EBSCO/ScienceDirect (itens 101-110,
  incluindo o paper de Tao 2022 e os dois de Barina 2021/2025 já citados
  em `literature/00-index.md` sem PDF arquivado até agora, e um novo
  ALEGAÇÃO DE PROVA de Getachew 2025, item 109) — todos os lotes
  manuais organizados a partir de `/home/rat/Downloads/pepers/`
  (identidade de cada arquivo confirmada contra o conteúdo real, e contra
  hash MD5 para descartar duplicatas exatas, antes de renomear — já que
  vários nomes de download não batiam com o título do paper).
- **10 sem PDF livre restantes** (2026-07-15: reduzido de ~51 — ver
  "Limpeza de itens não revisados por pares" abaixo), majoritariamente
  porque o host bloqueia download automatizado (ver "Limitações
  técnicas" abaixo) — **não** porque o conteúdo é necessariamente pago;
  a tabela mantém o link original nessas linhas para o diretor
  científico baixar manualmente.
- **12 excluídos** por serem falsos-positivos (nada a ver com a
  conjectura — em geral "Collatz" é sobrenome de um coautor, ou parte de
  outro conceito matemático do mesmo Lothar Collatz, num contexto sem
  relação): 8 do Scholar original (itens 001-100, ex: estudos
  hospitalares dinamarqueses) + 4 do lote EBSCO/ScienceDirect (itens
  111-114: "Collatz-Wielandt" é teoria de Perron-Frobenius/matrizes, não
  a conjectura; "método multiponto de Collatz" é técnica de diferenças
  finitas; "Nestler-Collatz" é sobrenome de coautora num paper de
  psicologia).
- **1 duplicado** (item 089 = mesmo paper do item 057, indexado duas vezes
  pelo Scholar via fontes diferentes).

## Limpeza de itens não revisados por pares (2026-07-15)

Pedido do diretor científico: dos itens "sem PDF livre" (nunca baixados,
portanto nunca revisados), remover os que não são de fontes revisadas
por pares e que ainda não foram analisados de nenhuma forma — mantendo
tudo que já foi baixado/lido, independente da fonte.

**Removidos: 38 itens** hospedados só em plataformas de auto-arquivamento
sem journal/conferência citado (researchgate.net, academia.edu,
philarchive.org, philpapers.org, Cambridge Open Engage — confirmado por
busca que é um servidor de preprints sem revisão por pares própria, não
a Cambridge University Press), mais 1 revista de divulgação científica
(New Scientist, não é publicação acadêmica) e 1 capítulo de livro técnico
(sobre SIMD/Java, revisão editorial não é revisão por pares acadêmica).
Nenhum desses tinha sido lido, corrigido ou implementado — colunas
Lido/Corrigido/Implementado vazias em todos, já que não havia PDF para
revisar. Os números originais desses itens **não foram reaproveitados**
(mantidos como lacunas na numeração), para não invalidar referências a
números específicos em outros arquivos do projeto (hipóteses, STATE.md).

**Mantidos por decisão explícita do diretor científico, apesar de não
serem revisados por pares**: as 6 alegações de prova/refutação (itens
050, 086, 087, 092, 093, 094) — candidatas a revisão futura, seguindo o
padrão já estabelecido neste projeto de encontrar erros reais em
alegações não revisadas por pares (Boyle/H-065, Yun/H-068, Lodders/H-070,
todos preprints).

**Mantidos por incerteza genuína sobre o status de revisão por pares**
(não removidos por precaução, não por confirmação positiva): item 027
("Arya Bhatta Journal of Mathematics and Informatics" — o próprio journal
alega processo de revisão por pares duplo-cego, mas tem sinais de
qualidade duvidosa, ex. fator de impacto de 5,856 não verificável em
bases como Web of Science/Clarivate, típico de journals de baixa
qualidade ou predatórios — mantido porque a alegação de revisão por
pares em si não foi refutada, só sua confiabilidade está em dúvida).

**Confirmados como revisados por pares (mantidos com confiança)**: item
071 (Mathematics, MDPI — revisão por pares formal), item 072 (EPJ
Special Topics, Springer/EDP Sciences — journal de física estabelecido),
item 098 (ACM Digital Library — revisão por pares de conferência/journal
formal).

## Limitações técnicas encontradas (importante ler antes de usar a tabela)

- **ResearchGate** (a maioria dos "sem PDF livre"): todo link direto para
  PDF do ResearchGate está atrás de uma verificação de segurança
  Cloudflare ("Security check required"). Em navegador real ela passa
  sozinha depois de alguns segundos (não é CAPTCHA interativo, não
  precisei contornar nada) — mas depois disso, tanto o botão de download
  do visualizador de PDF do Chrome quanto um download disparado via
  JavaScript (blob + link) abrem um **diálogo nativo do sistema
  operacional** ("Salvar como") que as ferramentas de automação não
  conseguem completar (a screenshot trava, teclas não chegam ao diálogo).
  Não é um bloqueio de bot-detection que eu não devesse contornar — é uma
  limitação de automação de diálogos nativos do SO. Não tentei driblar
  isso reconfigurando o Chrome do diretor científico (fora de escopo,
  exigiria mexer em configurações do navegador real).
- **academia.edu, SSRN, philpapers.org, philarchive.org, mdpi.com,
  IEEE Xplore**: bloqueiam requisição direta (HTTP 403) mesmo com
  user-agent de navegador real.
- **preprints.org**: bloqueado por Akamai Bot Manager (403).
- Nenhum desses são "CAPTCHA" no sentido de exigir resolução interativa
  minha — são bloqueios automáticos de rede que retornam erro antes de
  qualquer desafio aparecer, então não há nada para "contornar", só um
  limite real do que dá para baixar sem navegação humana manual.
- **Dois papers do arXiv não puderam ser baixados**: um foi **retirado
  pelo autor** (item 078, arXiv:2605.13886 — só resta o abstract com aviso
  de retirada).

## Achados que valem destaque para quando formos ler

- **Vários papers alegam prova ou refutação completa** da conjectura
  (marcados "[ALEGAÇÃO DE PROVA]" ou "[ALEGAÇÃO DE REFUTAÇÃO]" na
  tabela) — itens 049, 050, 051, 076, 087, 092, 093, 094. Candidatos
  naturais para `literature/unverified-proof-claims.md` quando lidos.
- **Item 057/089**: "A Fibonacci theorem for Collatz trajectories via
  modular graph structure" (Reyes Jiménez, arXiv:2606.02621) — já
  catalogado no nosso `STATE.md` como lido apenas parcialmente; agora
  temos o PDF completo (`056_Fibonacci-theorem...pdf`).
- **Item 030/043/045**: três papers diferentes de "X Wang" sobre exclusão
  de m-ciclos do Collatz até m≤93-95 (INTEGERS journal / ResearchGate) —
  diretamente relacionado à nossa linha H-009/H-034. Vale tentar achar
  via INTEGERS (revista open-access de verdade) numa sessão futura, já
  que o ResearchGate bloqueou.
- **JCR Castillo / SDJCR Castillo** (Juan Carlos Ruiz Castillo, USAC
  Guatemala) aparece como autor de **~20 dos 100 resultados** — uma
  linha pessoal extensa de "dinâmica residual" aplicada ao Collatz
  (drift residual, dissipação, medidas de Gibbs, etc.), toda no
  ResearchGate. Confirmado como acadêmico real (item 055 é sobre
  filosofia da matemática, não Collatz, e tem afiliação/ORCID
  verificáveis) — não necessariamente crank, mas um volume de output
  que vale ler com ceticismo normal antes de incorporar qualquer ideia.
- **Alguns títulos parecem pseudociência/spam** (itens 069, 088 —
  linguagem tipo "SNSFT Discovery Engine", "Prime Lattice Coherence
  Theorem" misturando Collatz com constante cosmológica e QED) — não
  testados a fundo, marcados como suspeitos na tabela.

## Tabela

Preencha **Lido**, **Corrigido**, **Implementado** manualmente conforme
formos processando um por um.

`*` no item 055: paper de filosofia da matemática (não é sobre
Collatz especificamente, sem alegação matemática verificável) — lido
por completo para contexto sobre o programa de pesquisa Ruiz Castillo
(ver `STATE.md`), sem H-0XX/E-0XX próprio pois não há nada
computacional para verificar.

`****` no item 028: paper de teoria de grafos/ciência de redes (não é
sobre Collatz especificamente), com Collatz aparecendo só como um
exemplo ilustrativo de meia página (Seção 5.2) entre vários. Revisão
(H-060) cobriu apenas esse conteúdo Collatz-específico, não o
framework geral de teoria de grafos (fora do escopo deste projeto).

`*****` no item 036: **falso-positivo puro de busca por sobrenome**.
Paper de teoria espectral de grafos (raio espectral Laplaciano,
arXiv:2606.14550, math.CO) que menciona "Collatz" cinco vezes no
texto — todas como parte do termo **"Collatz–Wielandt comparison"**
(uma ferramenta clássica e completamente distinta, da teoria de
Perron-Frobenius para autovalores de matrizes não-negativas). Lothar
Collatz contribuiu tanto para a conjectura 3x+1 quanto para essa
fórmula, mas são resultados matemáticos sem relação alguma entre si.
O paper não contém nenhuma menção à conjectura de Collatz (3x+1) nem a
qualquer conceito relacionado. Sem H-0XX/E-0XX próprio — não há nada
do escopo deste projeto para verificar.

`**` no item 026: o PDF (`026_Grandes-Desviaciones-Residuales-Ruiz-Castillo.pdf`)
foi baixado por um subagente lançado para revisar este item (2026-07-14),
via navegador, antes de o diretor científico estabelecer a regra de que
Claude/subagentes nunca devem baixar PDFs por conta própria (ver memória
`feedback_never_download_pdfs.md`). A análise (H-056) foi verificada com
rigor e o achado é válido; o arquivo permanece no repositório por decisão
explícita do diretor científico (2026-07-15) — mantido em vez de removido,
com esta ressalva documentada para transparência. Nenhum outro item da
coleção foi baixado dessa forma.

| # | Título | Autores/Ano | Link | Arquivo local | Lido | Corrigido | Implementado |
|---|---|---|---|---|---|---|---|
| 001 | Geometría Residual de Ruiz Castillo para la dinámica acelerada de la Conjetura de Collatz | SDJCR Castillo - researchgate.net | BAIXADO (DOI 10.5281/zenodo.21271452) | `001_Geometria-Residual-Ruiz-Castillo.pdf` | Sim | Sim | Sim |
| 002 | Behavior of a Decimal-Parity-Based 3n+1 Mapping | J Adnan, SA Dar - Global Journal of Pure and Applied, 2026 | BAIXADO | `002_Decimal-Parity-Based-3n1-Mapping.pdf` | Sim | Sim | Sim |
| 003 | A Collatz-Equivalent Map on the Nonzero Integers | JS Gilbert - 2026 - preprints.org | BAIXADO | `003_Collatz-Equivalent-Map-Nonzero-Integers.pdf` | Sim | Sim | Sim |
| 004 | First-Principles Derivation of the Steiner Sentence Length Distribution | J Seymour - 2026 - wildducktheories.github.io | BAIXADO | `004_First-Principles-Derivation-Steiner-Sentence-Length-Distribution.pdf` | Sim | Sim | Sim |
| 005 | A Regular Expression Language for the Collatz Graph | J Seymour - 2026 - wildducktheories.github.io | BAIXADO | `005_A-Regular-Expression-Language-for-the-Collatz-Graph.pdf` | Sim | Sim | Sim |
| 006 | A Two-Field Propagation Model for the Collatz Map | MM Anthony - 2026 - researchgate.net | BAIXADO | `006_Two-Field-Propagation-Model.pdf` | Sim | Sim | Sim |
| 007 | Finite-Dimensional Combinatorial and Arithmetic Structures of Parity Vectors for the Accelerated Collatz Map | K Hikawa - researchgate.net | BAIXADO | `007_Parity-Vector-Structures-Accelerated-Collatz.pdf` | Sim | Sim | Sim |
| 008 | Dissipative Bounds and Ruiz Castillo Residual Decomposition in the Accelerated Dynamics of the Collatz Conjecture | SDJCR Castillo - researchgate.net | BAIXADO | `008_Dissipative-Bounds-Ruiz-Castillo.pdf` | Sim | Sim | Sim |
| 009 | Structural Dualism in Integer Architectures | E Olgac - researchgate.net | BAIXADO | `009_Structural-Dualism-Integer-Architectures.pdf` | Sim | Sim | Sim |
| 010 | Teorema Central del Límite Residual de Ruiz Castillo para la dinámica acelerada de la Conjetura de Collatz | SDJCR Castillo - researchgate.net | BAIXADO | `010_Teorema-Central-Limite-Ruiz-Castillo.pdf` | Sim | Sim | Sim |
| 011 | Structural Analysis, Dynamic Density Sieve, and Logarithmic Contraction of Collatz Sequences | A Mohammed - 2026 - researchgate.net | BAIXADO | `011_Structural-Analysis-Density-Sieve-Logarithmic-Contraction.pdf` | Sim | Sim | Sim |
| 013 | Operador de Transferencia Residual de Ruiz Castillo y estructura espectral en la dinamica acelerada de la Conjetura de Collatz | SDJCR Castillo - researchgate.net | BAIXADO | `013_Operador-Transferencia-Ruiz-Castillo.pdf` | Sim | Sim | Sim |
| 014 | A Coordinate System for Collatz Dynamics | J Williams - arXiv:2607.01718, 2026 | BAIXADO | `014_A-Coordinate-System-for-Collatz-Dynamics.pdf` | Sim | Sim | Sim |
| 015 | Canonical Shells and Residue-Cover Trees in a Conditional First-Descent Approach to the Collatz Problem | SY Kayadibi - researchgate.net | BAIXADO | `015_Canonical-Shells-Residue-Cover-Trees.pdf` | Sim | Sim | Sim |
| 016 | Collatz-Thwaites-Ulam-Hasse-Syracuse-Kakutani (CTUHSK) Theorem | KP Bikarnakatte - engrxiv.org | BAIXADO | `016_CTUHSK-Theorem.pdf` | Sim | Sim | Sim |
| 017 | Medidas de Gibbs Residuales de Ruiz Castillo y estados de equilibrio en la dinamica acelerada de la Conjetura de Collatz | SDJCR Castillo - researchgate.net | BAIXADO | `017_Medidas-Gibbs-Residuales-Ruiz-Castillo.pdf` | Sim | Sim | Sim |
| 019 | Emergence of Gamma-Type Upward-Phase Statistics in the Collatz Map: An Effective Poisson Process Mechanism | W Fu, X Liu, Y Wang - arXiv:2606.26811, 2026 | BAIXADO | `018_Emergence-of-Gamma-Type-Upward-Phase-Statistics.pdf` | Sim | Sim | Sim |
| 020 | Principio Variacional Residual de Ruiz Castillo y formalismo termodinamico para la dinamica acelerada de la Conjetura de Collatz | SDJCR Castillo - 2026 - researchgate.net | BAIXADO | `020_Principio-Variacional-Ruiz-Castillo.pdf` | Sim | Sim | Sim |
| 021 | A GENERALIZATION OF 3x+1 PROBLEM TO 3x+4y+1 | R Amirian, A Amirian - SSRN 6993335 | BAIXADO | `021_Generalization-3x1-to-3x4y1.pdf` | Sim | Sim | Sim |
| 022 | A NO-ALTERNATIVE PROOF VIA TERNARY COUNTERS, PRIMITIVE CARRY, AND FORCED THREAD DISPLACEMENT | ME Spencer - academia.edu | BAIXADO | `022_Finite-Block-Exhaustion-Rooted-Occupancy-Inverse-Collatz.pdf` |  |  |  |
| 023 | Los castores en el limite de la computacion | SM Iglesias - La Gaceta de la RSME, 2026 - researchgate.net | BAIXADO (DOI 10.63427/QJWR5276) | `023_Los-Castores-en-el-Limite-de-la-Computacion.pdf` |  |  |  |
| 024 | The Coordinate System as Ontological Foundation: Why Existence Requires a Frame Before It Can Change [filosofia/metafisica, Collatz citado apenas como analogia tangencial] | Z Charrat - 2026 - researchgate.net | BAIXADO | `024_Coordinate-System-Ontological-Foundation.pdf` |  |  |  |
| 025 | Exact and Delayed Descent in Accelerated Odd Collatz Spines with AAS-Based Metamorphic Separation | SY Kayadibi - Zenodo v1, 2026 - researchgate.net | BAIXADO | `025_Exact-Delayed-Descent-Accelerated-Odd-Collatz-Spines-AAS.pdf` |  |  |  |
| 026 | Grandes Desviaciones Residuales de Ruiz Castillo en la dinamica acelerada de la Conjetura de Collatz | SDJCR Castillo - researchgate.net | BAIXADO (via Zenodo, DOI 10.5281/zenodo.20767811 -- ResearchGate bloqueia mas o mesmo paper esta espelhado aberto no Zenodo) | `026_Grandes-Desviaciones-Residuales-Ruiz-Castillo.pdf`** | Sim | Sim | Sim |
| 027 | On the Proof of Collatz Conjecture | S Sharma, M Rani - Arya Bhatta Journal of Mathematics, 2026 - indianjournals.com | (sem link PDF detectado pelo Scholar) | sem PDF livre (journal pago) |  |  |  |
| 028 | A Continuous Multi-Component Measure of Directed Acyclicity (DAG-ness) | E Csikos - arXiv:2606.22205, 2026 | BAIXADO | `027_Continuous-Multi-Component-Measure-DAG-ness.pdf`**** | Sim | Sim | Sim |
| 029 | Collatz Progressions Reframed: Exponent Representation, Algorithmic Hierarchies, and Record Computations | N Alic - IEEE Access, 2026 | BAIXADO | `029_Collatz-Progressions-Reframed.pdf` | Sim | Sim | Sim |
| 030 | NON-EXISTENCE OF COLLATZ m-CYCLES FOR m<=95 | X Wang - INTEGERS, 2026 - researchgate.net | BAIXADO | `030_Non-Existence-Collatz-m-Cycles-m-leq-95.pdf` |  |  |  |
| 031 | Predicting extreme stopping time behavior in the Collatz system | E Melas, NC Poulios - Journal of Dynamics and Games, 2026 - aimsciences.org | BAIXADO | `031_Predicting-Extreme-Stopping-Time.pdf` | Sim | Sim | Sim |
| 032 | Jacobsthal Trees and Generalized Transformations | P Kosobutskyy, D Mailland - dergipark.org.tr | BAIXADO | `032_Jacobsthal-Trees-Generalized-Transformations.pdf` | Sim | Sim | Sim |
| 035 | Disipacion Promedio de Ruiz Castillo y medidas de equilibrio en la dinamica acelerada de la Conjetura de Collatz | JCR Castillo - researchgate.net | BAIXADO (DOI 10.5281/zenodo.20636301) | `035_Disipacion-Promedio-Ruiz-Castillo.pdf` |  |  |  |
| 036 | Upper bounds for the Laplacian spectral radius: Proofs and counterexamples | I Damnjanovic, T Ha, D Stevanovic - arXiv:2606.14550, 2026 | BAIXADO | `036_Upper-bounds-Laplacian-spectral-radius.pdf`***** | Sim | N/A | N/A |
| 037 | ROOTED SURJECTIVITY FROM THE INVARIANT E/O REFINEMENT SYSTEM | ME Spencer - academia.edu | BAIXADO | `037_Rooted-Surjectivity-Invariant-EO-Refinement-System.pdf` |  |  |  |
| 038 | A modular classification of pre-descent resistance in accelerated odd Collatz dynamics | SY Kayadibi - SSRN 6918258, 2026 | BAIXADO | `038_Modular-Classification-Pre-Descent-Resistance.pdf` | Sim | Sim | Sim |
| 040 | (Não relacionado - ruído do Scholar: ECG/troponina cardíaca) | A Knudsen et al - Journal of.., 2026 - Elsevier | -- | excluído (não é sobre Collatz, falso positivo do Scholar) |  |  |  |
| 041 | (Não relacionado - ruído do Scholar: detecção de afogamento por IA) | CK Ostenfeldt et al - Scandinavian J, 2026 - Springer | -- | excluído (não é sobre Collatz, falso positivo do Scholar) |  |  |  |
| 049 | The Collatz Conjecture is True [ALEGAÇÃO DE PROVA - ver nota] | DG Boyle - 2026 - rxiverse.org | BAIXADO | `049_The-Collatz-Conjecture-is-True.pdf` | Sim | Não | Sim |
| 050 | On the Convergence of the Collatz Function [ALEGAÇÃO DE PROVA - ver nota] | A Roif - academia.edu | [link](https://www.academia.edu/) | sem PDF livre (academia.edu bloqueia download automatizado) |  |  |  |
| 055 | Platonismo y realismo en matematicas y fisica: un estudio ontologico y epistemologico | JCR Castillo, AFM Sanabria - Diotima, 2026 - usac.edu.gt | BAIXADO | `055_Platonismo-realismo-matematicas-fisica.pdf` | Sim | Sim* | Sim* |
| 056 | (Não relacionado - ruído do Scholar: não-transporte de pacientes pré-hospitalares na Dinamarca) | S Kondrup et al - 2026 - sdu.dk | -- | excluído (não é sobre Collatz, falso positivo do Scholar - "Collatz" é sobrenome de coautora) |  |  |  |
| 057 | A Fibonacci theorem for Collatz trajectories via modular graph structure | MAR Jimenez - arXiv:2606.02621, 2026 | BAIXADO | `056_Fibonacci-theorem-Collatz-modular-graph.pdf` | Sim | Sim | Sim |
| 071 | Parity-Based Level-Set Approach to the Collatz Conjecture | S Koyuncu et al - Mathematics (MDPI), 2026 | [link](https://www.mdpi.com/2227-7390/14/10/1763) | sem PDF livre (mdpi.com bloqueou download automatizado, 403) |  |  |  |
| 072 | Polar recurrence plots on Collatz sequences devoid of exact recurrences | CL Webber Jr - EPJ Special Topics, 2026 - Springer | (sem link PDF detectado pelo Scholar) | sem PDF livre (Springer, pago) |  |  |  |
| 074 | Loop Termination and Generalized Collatz Sequences | M Carelli - arXiv:2605.15094, 2026 | BAIXADO | `073_Loop-Termination-Generalized-Collatz.pdf` | Sim | Sim | Sim |
| 075 | (Não relacionado - ruído do Scholar: afogamento na Dinamarca) | N Breindahl et al - Clinical.., 2026 - tandfonline | -- | excluído (não é sobre Collatz, falso positivo do Scholar) |  |  |  |
| 076 | A Structural Proof of the Collatz Conjecture via non-repeating trajectory and Recursive Decay [ALEGAÇÃO DE PROVA] | YH Yun - osf.io | BAIXADO | `075_Structural-Proof-Collatz-nonrepeating.pdf` | Sim | Não | Sim |
| 079 | (Não relacionado - ruído do Scholar: emergências oftalmológicas na Dinamarca) | N Jensen et al - Scandinavian J, 2026 - Springer | -- | excluído (não é sobre Collatz, falso positivo do Scholar) |  |  |  |
| 081 | (Não relacionado - ruído do Scholar: doença de Ménière na Dinamarca) | C Gronlund et al - European Archives, 2026 - Springer | -- | excluído (não é sobre Collatz, falso positivo do Scholar) |  |  |  |
| 084 | MODELLING THE COLLATZ PROBLEM FROM A JACOBSTHAL VIEWPOINT | D Mailland, P Kosobutskyy - 2026 - lpnu.ua | BAIXADO | `084_Modelling-Collatz-Jacobsthal-Viewpoint.pdf` | Sim | Sim | Sim |
| 086 | The Axiom of Bijective Causality: Natural Numbers via Wave Processes and the Resolution of the Collatz Conjecture | S Hamaji - researchgate.net | [link](https://www.researchgate.net/) | sem PDF livre (ResearchGate bloqueia download automatizado) |  |  |  |
| 087 | A Common Proof of the Riemann Hypothesis and the Collatz Conjecture [ALEGAÇÃO DE PROVA] | K Tynski - 2026 - academia.edu | [link](https://www.academia.edu/) | sem PDF livre (academia.edu bloqueia download automatizado) |  |  |  |
| 089 | A Fibonacci theorem for Collatz trajectories via modular graph structure [DUPLICADO - já temos, ver item 057] | MA Reyes Jimenez - arXiv e-prints, 2026 - adsabs | [link](https://arxiv.org/abs/2606.02621) | `056_Fibonacci-theorem-Collatz-modular-graph.pdf` (duplicado do item 057) | Sim | Sim | Sim |
| 091 | (Não relacionado - ruído do Scholar: bioinformática, "M Collatz" é sobrenome de coautor) | T Eulenfeld, M Collatz et al - bioRxiv, 2026 | -- | excluído (não é sobre a conjectura, falso positivo do Scholar) |  |  |  |
| 092 | Continued Disproof Sentence towards Collatz Conjecture [ALEGAÇÃO DE REFUTAÇÃO] | M Syzdykov - 2026 - cambridge.org | [link](https://www.researchgate.net/) | sem PDF livre (ResearchGate bloqueia download automatizado) |  |  |  |
| 093 | A Note on a Claimed Disproof of the Collatz Conjecture [RESPOSTA CRÍTICA a outra alegação] | M Lafontaine, G Cheong - researchgate.net | [link](https://www.researchgate.net/) | sem PDF livre (ResearchGate bloqueia download automatizado) |  |  |  |
| 094 | RESOLUTION OF THE COLLATZ CONJECTURE VIA THE AXIOM OF BIJECTIVE CAUSALITY [ALEGAÇÃO DE PROVA] | S Hamaji - researchgate.net | [link](https://www.researchgate.net/) | sem PDF livre (ResearchGate bloqueia download automatizado) |  |  |  |
| 095 | (Não relacionado - ruído do Scholar: hospital domiciliar na Dinamarca) | MB Hagi-Pedersen et al - 2026 - regsj.dk | -- | excluído (não é sobre Collatz, falso positivo do Scholar) |  |  |  |
| 098 | Teaching Theory of Computation in STEM K-12 Curricula Through Impossibility and Undecidability Problems (Collatz mencionado como exemplo) | R del Vado Virseda - ACM, 2026 | (sem link PDF detectado pelo Scholar) | sem PDF livre (ACM Digital Library, pago) |  |  |  |
| 099 | Selection Rules and Channel Structure in a Base Octave Model of Collatz Dynamics | K Lodders - arXiv:2604.20181, 2026 | BAIXADO | `098_Selection-Rules-Channel-Structure-Base-Octave.pdf` | Sim | Não | Sim |
| 101 | About the Collatz conjecture | Ş Andrei, C Masalagiu - Acta Informatica 35, 167-179, 1998 | BAIXADO | `101_About-the-Collatz-Conjecture.pdf` | Sim | Sim | Sim |
| 102 | Tag systems and Collatz-like functions | L De Mol - Theoretical Computer Science 390, 92-101, 2008 | BAIXADO | `102_Tag-Systems-and-Collatz-Like-Functions.pdf` | Sim | Sim | Sim |
| 103 | An Artificial Life View of the Collatz Problem | H Sayama - Artificial Life 17, 137-140, 2011 | BAIXADO | `103_Artificial-Life-View-Collatz-Problem.pdf` | Sim | Sim | Sim |
| 104 | A Novel Image Encryption Scheme Based on Collatz Conjecture | DM Ballesteros, J Peña, D Renza - Entropy 20(901), 2018 | BAIXADO | `104_Image-Encryption-Scheme-Based-Collatz.pdf` | Sim | Sim | Sim |
| 105 | Convergence verification of the Collatz problem (verificado até 10^20) | D Barina - Journal of Supercomputing 77, 2681-2688, 2021 | BAIXADO | `105_Convergence-Verification-Collatz-Problem.pdf` | Sim | Sim | Sim |
| 106 | Almost all orbits of the Collatz map attain almost bounded values [resultado mais forte já estabelecido, já citado em `literature/00-index.md`] | T Tao - Forum of Mathematics, Pi 10:e12, 2022 | BAIXADO | `106_Almost-All-Orbits-Almost-Bounded-Values-Tao.pdf` | Sim | Sim | Sim |
| 107 | The Long Search for Collatz Counterexamples | OK Clay - Journal of Humanistic Mathematics 13(2), 2023 | BAIXADO | `107_Long-Search-Collatz-Counterexamples.pdf` |  |  |  |
| 108 | Reduced Collatz dynamics is periodical and the period equals 2 to the power of the count of x/2 | W Ren - Research in Mathematics 12(1), 2025 | BAIXADO | `108_Reduced-Collatz-Dynamics-Periodical.pdf` |  |  |  |
| 109 | Unfolding the Collatz Tree: An Indirect Structural Proof of the Collatz Conjecture [ALEGAÇÃO DE PROVA - constrói árvore reversa explícita, técnica próxima de H-018 deste projeto] | ES Getachew - Research in Mathematics 12(1), 2025 | BAIXADO | `109_Unfolding-Collatz-Tree-Structural-Proof.pdf` |  |  |  |
| 110 | Improved verification limit for the convergence of the Collatz conjecture (verificado até 2^71, já citado em `literature/00-index.md`) | D Barina - Journal of Supercomputing 81:810, 2025 | BAIXADO | `110_Improved-Verification-Limit-2-71.pdf` |  |  |  |
| 111 | (Não relacionado - coincidência de sobrenome: "Collatz-Wielandt sets" é teoria de Perron-Frobenius/matrizes, não a conjectura) | BS Tam, SF Wu - Linear Algebra and its Applications 125, 1989 | -- | excluído (falso positivo, busca EBSCO/ScienceDirect fora do Scholar) |  |  |  |
| 112 | (Não relacionado - mesma coincidência de sobrenome: "Collatz-Wielandt numbers", teoria de operadores) | KH Förster, B Nagy - Linear Algebra and its Applications 120, 1989 | -- | excluído (falso positivo, busca EBSCO/ScienceDirect fora do Scholar) |  |  |  |
| 113 | (Não relacionado - "método multiponto de Collatz" é técnica de diferenças finitas do mesmo Lothar Collatz, não a conjectura) | I Jaworska, J Orkisz - Engineering Analysis with Boundary Elements 50, 2015 | -- | excluído (falso positivo, busca EBSCO/ScienceDirect fora do Scholar) |  |  |  |
| 114 | (Não relacionado - "Nestler-Collatz" é sobrenome de coautora, paper de psicologia sobre reconhecimento facial) | C Dobel, B Nestler-Collatz et al - Psychological Research 84, 2020 | -- | excluído (falso positivo, busca EBSCO/ScienceDirect fora do Scholar) |  |  |  |
