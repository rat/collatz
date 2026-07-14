# Índice de papers — busca Google Scholar "Collatz" (ordenado por data)

Coletado em 2026-07-13/14, a partir de:
`https://scholar.google.com/scholar?hl=pt-BR&as_sdt=0,5&q=Collatz&scisbd=1`
(10 primeiras páginas de resultados, ~100 itens, ordenados por data de
adição mais recente).

## Resumo

- **100 resultados processados**, todas as 10 páginas do Google Scholar
  navegadas sem nenhum bloqueio/CAPTCHA da própria busca.
- **31 PDFs baixados** com sucesso (arquivo local na tabela; coluna Link
  mostra "BAIXADO" em vez do link original, já que o link só serve para
  indicar onde baixar) — 15 pela automação do navegador/Scholar, +16
  baixados manualmente pelo diretor científico em 2026-07-14 (via
  ResearchGate e outros hosts bloqueados para automação) e organizados
  nesta sessão a partir de `/home/rat/Downloads/pepers/`.
- **~60 sem PDF livre**, majoritariamente porque o host bloqueia download
  automatizado (ver "Limitações técnicas" abaixo) — **não** porque o
  conteúdo é necessariamente pago; a tabela mantém o link original nessas
  linhas para o diretor científico baixar manualmente.
- **8 excluídos** por serem falsos-positivos do Scholar (nada a ver com a
  conjectura — em geral "Collatz" é sobrenome de um coautor num paper de
  outra área, ex: estudos hospitalares dinamarqueses).
- **1 duplicado** (item 089 = mesmo paper do item 057, indexado duas vezes
  pelo Scholar via fontes diferentes).

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

| # | Título | Autores/Ano | Link | Arquivo local | Lido | Corrigido | Implementado |
|---|---|---|---|---|---|---|---|
| 001 | Geometría Residual de Ruiz Castillo para la dinámica acelerada de la Conjetura de Collatz | SDJCR Castillo - researchgate.net | [link](https://www.researchgate.net/profile/Juan-Carlos-Ruiz-3/publication/408622365_Geometria_Residual_de_Ruiz_Castillo_para_la_dinamica_acelerada_de_la_Conjetura_de_Collatz) | sem PDF livre (lido via navegador, ver `hypotheses/H-039...md`) | Sim | Sim | Sim |
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
| 012 | Proposed framework on Collatz conjecture | P Danesh - 2026 - cambridge.org | (sem link PDF detectado pelo Scholar) | sem PDF livre (nenhum link PDF listado) |  |  |  |
| 013 | Operador de Transferencia Residual de Ruiz Castillo y estructura espectral en la dinamica acelerada de la Conjetura de Collatz | SDJCR Castillo - researchgate.net | BAIXADO | `013_Operador-Transferencia-Ruiz-Castillo.pdf` |  |  |  |
| 014 | A Coordinate System for Collatz Dynamics | J Williams - arXiv:2607.01718, 2026 | BAIXADO | `014_A-Coordinate-System-for-Collatz-Dynamics.pdf` | Sim | Sim | Sim |
| 015 | Canonical Shells and Residue-Cover Trees in a Conditional First-Descent Approach to the Collatz Problem | SY Kayadibi - researchgate.net | BAIXADO | `015_Canonical-Shells-Residue-Cover-Trees.pdf` |  |  |  |
| 016 | Collatz-Thwaites-Ulam-Hasse-Syracuse-Kakutani (CTUHSK) Theorem | KP Bikarnakatte - engrxiv.org | BAIXADO | `016_CTUHSK-Theorem.pdf` | Sim | Sim | Sim |
| 017 | Medidas de Gibbs Residuales de Ruiz Castillo y estados de equilibrio en la dinamica acelerada de la Conjetura de Collatz | SDJCR Castillo - researchgate.net | BAIXADO | `017_Medidas-Gibbs-Residuales-Ruiz-Castillo.pdf` |  |  |  |
| 018 | The Collatz Conjecture (book chapter) | R Snytsar - Mastering SIMD with Java Vector API, 2026 - Springer | (sem link PDF detectado pelo Scholar) | sem PDF livre (capitulo de livro Springer, pago) |  |  |  |
| 019 | Emergence of Gamma-Type Upward-Phase Statistics in the Collatz Map: An Effective Poisson Process Mechanism | W Fu, X Liu, Y Wang - arXiv:2606.26811, 2026 | BAIXADO | `018_Emergence-of-Gamma-Type-Upward-Phase-Statistics.pdf` | Sim | Sim | Sim |
| 020 | Principio Variacional Residual de Ruiz Castillo y formalismo termodinamico para la dinamica acelerada de la Conjetura de Collatz | SDJCR Castillo - 2026 - researchgate.net | BAIXADO | `020_Principio-Variacional-Ruiz-Castillo.pdf` |  |  |  |
| 021 | A GENERALIZATION OF 3x+1 PROBLEM TO 3x+4y+1 | R Amirian, A Amirian - SSRN 6993335 | BAIXADO | `021_Generalization-3x1-to-3x4y1.pdf` |  |  |  |
| 022 | A NO-ALTERNATIVE PROOF VIA TERNARY COUNTERS, PRIMITIVE CARRY, AND FORCED THREAD DISPLACEMENT | ME Spencer - academia.edu | [link](https://www.academia.edu/download/133173533/collatz_conjecture_46_.pdf) | sem PDF livre (academia.edu bloqueou download, 403) |  |  |  |
| 023 | Los castores en el limite de la computacion | SM Iglesias - La Gaceta de la RSME, 2026 - researchgate.net | [link](https://www.researchgate.net/profile/Sergio-Miguens-Iglesias/publication/406892500) | sem PDF livre (ResearchGate bloqueia download automatizado) |  |  |  |
| 024 | The Coordinate System as Ontological Foundation: Why Existence Requires a Frame Before It Can Change | Z Charrat - 2026 - researchgate.net | [link](https://www.researchgate.net/profile/Zakaria-Charrat/publication/407406907) | sem PDF livre (ResearchGate bloqueia download automatizado) |  |  |  |
| 025 | Exact and Delayed Descent in Accelerated Odd Collatz Spines with AAS-Based Metamorphic Separation | SY Kayadibi - Zenodo v1, 2026 - researchgate.net | [link](https://www.researchgate.net/profile/Seyma-Yaman-Kayadibi/publication/407528640) | sem PDF livre (ResearchGate bloqueia download automatizado) |  |  |  |
| 026 | Grandes Desviaciones Residuales de Ruiz Castillo en la dinamica acelerada de la Conjetura de Collatz | SDJCR Castillo - researchgate.net | [link](https://www.researchgate.net/profile/Juan-Carlos-Ruiz-3/publication/407318083) | sem PDF livre (ResearchGate bloqueia download automatizado) |  |  |  |
| 027 | On the Proof of Collatz Conjecture | S Sharma, M Rani - Arya Bhatta Journal of Mathematics, 2026 - indianjournals.com | (sem link PDF detectado pelo Scholar) | sem PDF livre (journal pago) |  |  |  |
| 028 | A Continuous Multi-Component Measure of Directed Acyclicity (DAG-ness) | E Csikos - arXiv:2606.22205, 2026 | BAIXADO | `027_Continuous-Multi-Component-Measure-DAG-ness.pdf` |  |  |  |
| 029 | Collatz Progressions Reframed: Exponent Representation, Algorithmic Hierarchies, and Record Computations | N Alic - IEEE Access, 2026 | BAIXADO | `029_Collatz-Progressions-Reframed.pdf` |  |  |  |
| 030 | NON-EXISTENCE OF COLLATZ m-CYCLES FOR m<=95 | X Wang - INTEGERS, 2026 - researchgate.net | [link](https://www.researchgate.net/profile/Xinjun-Wang-11/publication/408104976) | sem PDF livre (ResearchGate bloqueia download automatizado) |  |  |  |
| 031 | Predicting extreme stopping time behavior in the Collatz system | E Melas, NC Poulios - Journal of Dynamics and Games, 2026 - aimsciences.org | BAIXADO | `031_Predicting-Extreme-Stopping-Time.pdf` |  |  |  |
| 032 | Jacobsthal Trees and Generalized Transformations | P Kosobutskyy, D Mailland - dergipark.org.tr | BAIXADO | `032_Jacobsthal-Trees-Generalized-Transformations.pdf` |  |  |  |
| 033 | Dimension Disipativa de Ruiz Castillo y subcilindros fractales en la dinamica acelerada de la Conjetura de Collatz | SDJCR Castillo - researchgate.net | [link](https://www.researchgate.net/profile/Juan-Carlos-Ruiz-3/publication/407029463) | sem PDF livre (ResearchGate bloqueia download automatizado) |  |  |  |
| 034 | The meme that has been amusing mathematicians for a century | J Aron - New Scientist, 2026 - Elsevier | (sem link PDF detectado pelo Scholar) | sem PDF livre (revista de divulgacao, paga) |  |  |  |
| 035 | Disipacion Promedio de Ruiz Castillo y medidas de equilibrio en la dinamica acelerada de la Conjetura de Collatz | JCR Castillo - researchgate.net | [link](https://www.researchgate.net/profile/Juan-Carlos-Ruiz-3/publication/406908855) | sem PDF livre (ResearchGate bloqueia download automatizado) |  |  |  |
| 036 | Upper bounds for the Laplacian spectral radius: Proofs and counterexamples | I Damnjanovic, T Ha, D Stevanovic - arXiv:2606.14550, 2026 | BAIXADO | `036_Upper-bounds-Laplacian-spectral-radius.pdf` |  |  |  |
| 037 | ROOTED SURJECTIVITY FROM THE INVARIANT E/O REFINEMENT SYSTEM | ME Spencer - academia.edu | [link](https://www.academia.edu/download/133063629/collatz_conjecture_44_.pdf) | sem PDF livre (academia.edu bloqueou download, 403) |  |  |  |
| 038 | A modular classification of pre-descent resistance in accelerated odd Collatz dynamics | SY Kayadibi - SSRN 6918258, 2026 | BAIXADO | `038_Modular-Classification-Pre-Descent-Resistance.pdf` |  |  |  |
| 039 | Teoria espectral de las palabras de valuacion en la dinamica acelerada de la Conjetura de Collatz | SDJCR Castillo - researchgate.net | [link](https://www.researchgate.net/profile/Juan-Carlos-Ruiz-3/publication/406439765) | sem PDF livre (ResearchGate bloqueia download automatizado) |  |  |  |
| 040 | (Não relacionado - ruído do Scholar: ECG/troponina cardíaca) | A Knudsen et al - Journal of.., 2026 - Elsevier | -- | excluído (não é sobre Collatz, falso positivo do Scholar) |  |  |  |
| 041 | (Não relacionado - ruído do Scholar: detecção de afogamento por IA) | CK Ostenfeldt et al - Scandinavian J, 2026 - Springer | -- | excluído (não é sobre Collatz, falso positivo do Scholar) |  |  |  |
| 042 | Dinamica Topologica de la Conjetura de Collatz: Un Enfoque Lagrangiano y de Integrales de Camino | BR Beltran - researchgate.net | [link](https://www.researchgate.net/publication) | sem PDF livre (ResearchGate bloqueia download automatizado) |  |  |  |
| 043 | A Corrected Suffix-Balanced Global-Minimum Certificate for Excluding Collatz m-Cycles for m<=94 | X Wang - 2026 - researchgate.net | [link](https://www.researchgate.net/) | sem PDF livre (ResearchGate bloqueia download automatizado) |  |  |  |
| 044 | HARES ALWAYS RETURN | A Fedotkin - researchgate.net | [link](https://www.researchgate.net/) | sem PDF livre (ResearchGate bloqueia download automatizado) |  |  |  |
| 045 | A REPRODUCIBLE CERTIFICATE EXCLUDING COLLATZ (m-cycles m<=93) | X Wang - researchgate.net | [link](https://www.researchgate.net/) | sem PDF livre (ResearchGate bloqueia download automatizado) |  |  |  |
| 046 | Analisis algebraico de ciclos en la funcion de Collatz | RM Rojas - academia.edu | [link](https://www.academia.edu/) | sem PDF livre (academia.edu bloqueia download automatizado) |  |  |  |
| 047 | NOT ALL COLLATZ SEQUENCES TEND TO | TQ Cong - 2026 - researchgate.net | [link](https://www.researchgate.net/) | sem PDF livre (ResearchGate bloqueia download automatizado) |  |  |  |
| 048 | Cotas disipativas y descomposicion residual de Ruiz Castillo en la dinamica acelerada de la Conjetura de Collatz | SDJCR Castillo - researchgate.net | [link](https://www.researchgate.net/) | sem PDF livre (ResearchGate bloqueia download automatizado) |  |  |  |
| 049 | The Collatz Conjecture is True [ALEGAÇÃO DE PROVA - ver nota] | DG Boyle - 2026 - rxiverse.org | BAIXADO | `049_The-Collatz-Conjecture-is-True.pdf` |  |  |  |
| 050 | On the Convergence of the Collatz Function [ALEGAÇÃO DE PROVA - ver nota] | A Roif - academia.edu | [link](https://www.academia.edu/) | sem PDF livre (academia.edu bloqueia download automatizado) |  |  |  |
| 051 | A Machine-Verified Conditional Theory of the Collatz Conjecture [checado por Lean 4] | J Park - researchgate.net | [link](https://www.researchgate.net/) | sem PDF livre (ResearchGate bloqueia download automatizado) |  |  |  |
| 052 | Sufes Conjecture: a parameterized generalization of the Syracuse/Collatz conjecture | A Khachnaoui - 2026 - researchgate.net | [link](https://www.researchgate.net/) | sem PDF livre (ResearchGate bloqueia download automatizado) |  |  |  |
| 053 | Onion, Apple, and Gate: A Theory of Recursive Stability and Recursive Failure | MD McPhetridge - philarchive.org | [link](https://philarchive.org/archive/MCPOAA-3) | sem PDF livre (philarchive.org bloqueou download, 403) |  |  |  |
| 054 | Drift residual y presion disipativa en la dinamica acelerada de la Conjetura de Collatz | SDJCR Castillo - researchgate.net | [link](https://www.researchgate.net/) | sem PDF livre (ResearchGate bloqueia download automatizado) |  |  |  |
| 055 | Platonismo y realismo en matematicas y fisica: un estudio ontologico y epistemologico | JCR Castillo, AFM Sanabria - Diotima, 2026 - usac.edu.gt | BAIXADO | `055_Platonismo-realismo-matematicas-fisica.pdf` |  |  |  |
| 056 | (Não relacionado - ruído do Scholar: não-transporte de pacientes pré-hospitalares na Dinamarca) | S Kondrup et al - 2026 - sdu.dk | -- | excluído (não é sobre Collatz, falso positivo do Scholar - "Collatz" é sobrenome de coautora) |  |  |  |
| 057 | A Fibonacci theorem for Collatz trajectories via modular graph structure | MAR Jimenez - arXiv:2606.02621, 2026 | BAIXADO | `056_Fibonacci-theorem-Collatz-modular-graph.pdf` |  |  |  |
| 058 | Generalization of Collatz-Type Conjectures | AS Bharti - researchgate.net | [link](https://www.researchgate.net/) | sem PDF livre (ResearchGate bloqueia download automatizado) |  |  |  |
| 059 | Residual Debt, Dissipative Compensation, and Descending Subcylinders in the Accelerated Dynamics of the Collatz Conjecture | JCR Castillo - 2026 - researchgate.net | [link](https://www.researchgate.net/) | sem PDF livre (ResearchGate bloqueia download automatizado) |  |  |  |
| 060 | Normalization of Natural Numbers: The Collatz Conjecture as a Case Study | S Hamaji - researchgate.net | [link](https://www.researchgate.net/) | sem PDF livre (ResearchGate bloqueia download automatizado) |  |  |  |
| 061 | A Component-wise Well-Founded Descent for the Collatz Problem via Dyadic Certificates | J Redero - academia.edu | [link](https://www.academia.edu/) | sem PDF livre (academia.edu bloqueia download automatizado) |  |  |  |
| 062 | SINGULAR DUALITY AND THE MODAL DISCIPLINE OF OBJECTIVITY | V Cabannas, D Silva - academia.edu | [link](https://www.academia.edu/) | sem PDF livre (academia.edu bloqueia download automatizado) |  |  |  |
| 063 | Deuda residual, compensacion disipativa y subcilindros descendentes en la dinamica acelerada de la Conjetura de Collatz | JCR Castillo - researchgate.net | [link](https://www.researchgate.net/) | sem PDF livre (ResearchGate bloqueia download automatizado) |  |  |  |
| 064 | Collatz Sequence Proof Easy Way | T Muhammad - 2026 - cambridge.org | (sem link PDF detectado pelo Scholar) | sem PDF livre (nenhum link PDF listado) |  |  |  |
| 065 | Valuation cylinders, residual dissipation, and dynamic contraction in the Collatz conjecture | JCR Castillo - 2026 - researchgate.net | [link](https://www.researchgate.net/) | sem PDF livre (ResearchGate bloqueia download automatizado) |  |  |  |
| 066 | Cilindros de valuacion, disipacion residual y contraccion dinamica en la Conjetura de Collatz | JCR Castillo - 2026 - researchgate.net | [link](https://www.researchgate.net/) | sem PDF livre (ResearchGate bloqueia download automatizado) |  |  |  |
| 067 | A class of numbers in the Collatz conjecture | A Petojevic - researchgate.net | [link](https://www.researchgate.net/) | sem PDF livre (ResearchGate bloqueia download automatizado) |  |  |  |
| 068 | 2-Adic Finite-Certificate Descent Closure for the 3x+1 Collatz Problem | D Bhattacharjee - 2026 - philpapers.org | [link](https://philpapers.org/archive/BHAAFD-2) | sem PDF livre (philpapers.org bloqueou download, 403) |  |  |  |
| 069 | SNSFL-Formally Verified Geometric Axiomatic Module-GAMCollider... [parece não ser sobre Collatz de fato, possível ruído/spam] | R Trent - philpapers.org | [link](https://philpapers.org/archive/TRESVG) | sem PDF livre (philpapers.org bloqueou download, 403) - conteúdo suspeito de não ser paper acadêmico real |  |  |  |
| 070 | The Gate of Collatz: Parity-Gated Expansion, Episodic Reduction, and Recursive Recomposition | MD McPhetridge - philarchive.org | [link](https://philarchive.org/) | sem PDF livre (philarchive.org bloqueia download automatizado) |  |  |  |
| 071 | Parity-Based Level-Set Approach to the Collatz Conjecture | S Koyuncu et al - Mathematics (MDPI), 2026 | [link](https://www.mdpi.com/2227-7390/14/10/1763) | sem PDF livre (mdpi.com bloqueou download automatizado, 403) |  |  |  |
| 072 | Polar recurrence plots on Collatz sequences devoid of exact recurrences | CL Webber Jr - EPJ Special Topics, 2026 - Springer | (sem link PDF detectado pelo Scholar) | sem PDF livre (Springer, pago) |  |  |  |
| 073 | Expansions on Boundary Algebra | A Roif - academia.edu | [link](https://www.academia.edu/) | sem PDF livre (academia.edu bloqueia download automatizado) |  |  |  |
| 074 | Loop Termination and Generalized Collatz Sequences | M Carelli - arXiv:2605.15094, 2026 | BAIXADO | `073_Loop-Termination-Generalized-Collatz.pdf` |  |  |  |
| 075 | (Não relacionado - ruído do Scholar: afogamento na Dinamarca) | N Breindahl et al - Clinical.., 2026 - tandfonline | -- | excluído (não é sobre Collatz, falso positivo do Scholar) |  |  |  |
| 076 | A Structural Proof of the Collatz Conjecture via non-repeating trajectory and Recursive Decay [ALEGAÇÃO DE PROVA] | YH Yun - osf.io | BAIXADO | `075_Structural-Proof-Collatz-nonrepeating.pdf` |  |  |  |
| 077 | Restoring Causal Structure through Natural Mathematics: A Case Study on the Collatz Conjecture | S Hamaji - researchgate.net | [link](https://www.researchgate.net/) | sem PDF livre (ResearchGate bloqueia download automatizado) |  |  |  |
| 078 | Parity vectors and paradoxical sequences in the accelerated Collatz map [RETIRADO PELO AUTOR] | T Niu - arXiv:2605.13886, 2026 | [link](https://arxiv.org/abs/2605.13886) | sem PDF (paper retirado pelo autor no arXiv - só resta o abstract) |  |  |  |
| 079 | (Não relacionado - ruído do Scholar: emergências oftalmológicas na Dinamarca) | N Jensen et al - Scandinavian J, 2026 - Springer | -- | excluído (não é sobre Collatz, falso positivo do Scholar) |  |  |  |
| 080 | Beyond the A Priori Omission: Natural Mathematics and the Collatz Conjecture | S Hamaji - researchgate.net | [link](https://www.researchgate.net/) | sem PDF livre (ResearchGate bloqueia download automatizado) |  |  |  |
| 081 | (Não relacionado - ruído do Scholar: doença de Ménière na Dinamarca) | C Gronlund et al - European Archives, 2026 - Springer | -- | excluído (não é sobre Collatz, falso positivo do Scholar) |  |  |  |
| 082 | On a relation between Collatz-type operators and Euler's pentagonal number generating function | A Mugnai - 2026 - researchgate.net | [link](https://www.researchgate.net/) | sem PDF livre (ResearchGate bloqueia download automatizado) |  |  |  |
| 083 | Wave (Cause)-Particle (Effect) Causality: The Collatz Conjecture as a Case Study | S Hamaji - researchgate.net | [link](https://www.researchgate.net/) | sem PDF livre (ResearchGate bloqueia download automatizado) |  |  |  |
| 084 | MODELLING THE COLLATZ PROBLEM FROM A JACOBSTHAL VIEWPOINT | D Mailland, P Kosobutskyy - 2026 - lpnu.ua | BAIXADO | `084_Modelling-Collatz-Jacobsthal-Viewpoint.pdf` |  |  |  |
| 085 | Deterministic Decay: A Formally Specified Computational Model for Collatz-Guided Operation Minimisation | MSB Masud - researchgate.net | [link](https://www.researchgate.net/) | sem PDF livre (ResearchGate bloqueia download automatizado) |  |  |  |
| 086 | The Axiom of Bijective Causality: Natural Numbers via Wave Processes and the Resolution of the Collatz Conjecture | S Hamaji - researchgate.net | [link](https://www.researchgate.net/) | sem PDF livre (ResearchGate bloqueia download automatizado) |  |  |  |
| 087 | A Common Proof of the Riemann Hypothesis and the Collatz Conjecture [ALEGAÇÃO DE PROVA] | K Tynski - 2026 - academia.edu | [link](https://www.academia.edu/) | sem PDF livre (academia.edu bloqueia download automatizado) |  |  |  |
| 088 | The Prime Lattice Coherence Framework [título sugere possível pseudociência - menciona constante cosmológica, QED e Collatz juntos] | G Gurwell - Spine, 2026 - ctftheory.com | [link](https://ctftheory.com/) | sem PDF livre (não testado - conteúdo suspeito de não ser matemática acadêmica real) |  |  |  |
| 089 | A Fibonacci theorem for Collatz trajectories via modular graph structure [DUPLICADO - já temos, ver item 057] | MA Reyes Jimenez - arXiv e-prints, 2026 - adsabs | [link](https://arxiv.org/abs/2606.02621) | `056_Fibonacci-theorem-Collatz-modular-graph.pdf` (duplicado do item 057) |  |  |  |
| 090 | The Cycle Exclusion Theorem for Generalised Collatz Maps | RA Satnoianu - 2026 - researchgate.net | [link](https://www.researchgate.net/) | sem PDF livre (ResearchGate bloqueia download automatizado) |  |  |  |
| 091 | (Não relacionado - ruído do Scholar: bioinformática, "M Collatz" é sobrenome de coautor) | T Eulenfeld, M Collatz et al - bioRxiv, 2026 | -- | excluído (não é sobre a conjectura, falso positivo do Scholar) |  |  |  |
| 092 | Continued Disproof Sentence towards Collatz Conjecture [ALEGAÇÃO DE REFUTAÇÃO] | M Syzdykov - 2026 - cambridge.org | [link](https://www.researchgate.net/) | sem PDF livre (ResearchGate bloqueia download automatizado) |  |  |  |
| 093 | A Note on a Claimed Disproof of the Collatz Conjecture [RESPOSTA CRÍTICA a outra alegação] | M Lafontaine, G Cheong - researchgate.net | [link](https://www.researchgate.net/) | sem PDF livre (ResearchGate bloqueia download automatizado) |  |  |  |
| 094 | RESOLUTION OF THE COLLATZ CONJECTURE VIA THE AXIOM OF BIJECTIVE CAUSALITY [ALEGAÇÃO DE PROVA] | S Hamaji - researchgate.net | [link](https://www.researchgate.net/) | sem PDF livre (ResearchGate bloqueia download automatizado) |  |  |  |
| 095 | (Não relacionado - ruído do Scholar: hospital domiciliar na Dinamarca) | MB Hagi-Pedersen et al - 2026 - regsj.dk | -- | excluído (não é sobre Collatz, falso positivo do Scholar) |  |  |  |
| 096 | Structural Discoveries in the Collatz Conjecture: Modulo 64 Survivors, Confluence Points, and Energy Deviation | Y Zhang - 2026 - philarchive.org | [link](https://philarchive.org/) | sem PDF livre (philarchive.org bloqueia download automatizado) |  |  |  |
| 097 | The Axiom of Absolute Boundary: Boundaries and Metabolic Failure in Self-Referential Systems [não parece ser sobre Collatz especificamente] | Y Zhang - 2026 - philarchive.org | [link](https://philarchive.org/) | sem PDF livre (philarchive.org bloqueia download automatizado) |  |  |  |
| 098 | Teaching Theory of Computation in STEM K-12 Curricula Through Impossibility and Undecidability Problems (Collatz mencionado como exemplo) | R del Vado Virseda - ACM, 2026 | (sem link PDF detectado pelo Scholar) | sem PDF livre (ACM Digital Library, pago) |  |  |  |
| 099 | Selection Rules and Channel Structure in a Base Octave Model of Collatz Dynamics | K Lodders - arXiv:2604.20181, 2026 | BAIXADO | `098_Selection-Rules-Channel-Structure-Base-Octave.pdf` |  |  |  |
| 100 | A Binary Tree Interpretation of Shared Key Generation Using Modular Ananta-Graph Paths (não parece ser sobre Collatz - criptografia) | HR Vidyashree et al - researchgate.net | [link](https://www.researchgate.net/) | sem PDF livre (ResearchGate bloqueia download automatizado; também parece não ser sobre Collatz) |  |  |  |
