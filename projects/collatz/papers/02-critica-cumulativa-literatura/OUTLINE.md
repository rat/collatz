# OUTLINE — Crítica cumulativa da coleção de literatura Collatz (v1)

Status: **v1 completa e compilada** (`main.tex`/`main.pdf`, inglês, 7
páginas; `main-pt-br.tex`/`main-pt-br.pdf`, português, 7 páginas; ambos
limpos, sem undefined refs, bibliografia auditada contra INDEX.md/
H-arquivos — nenhum ano impresso sem fonte, mesmo padrão do paper 03).
Ainda não revisada pelo diretor científico.
Iniciado por pedido explícito do diretor científico em 2026-07-20
("pode iniciar"), depois de fechar o paper 03 (alegações de prova
completa). Este paper é, por natureza, **incremental e sem ponto de
fechamento** (ver `README.md` desta pasta e item 8 do `BACKLOG.md`) —
esta v1 cobre os itens já escritos com detalhe no `BACKLOG.md`, não a
coleção inteira.

## Escopo desta versão

A coleção completa (`literature/papers/INDEX.md`) tem 97 itens
catalogados, 81 já lidos (`Lido=Sim`). Deste universo:
- **13 itens** são alegações de prova/refutação completa → já viraram o
  **paper 03** (`03-alegacoes-de-prova-refutadas/`), excluídos daqui:
  itens 011, 016, 022, 037, 049, 050, 076, 087, 092, 093, 109, 115, 123.
- **16 itens** têm revisão completa já escrita em detalhe no `BACKLOG.md`
  e nos H-arquivos individuais, lidos integralmente para esta v1: itens
  001, 002, 003, 004, 005, 006, 007, 008, 009, 010, 013, 014, 017, 019,
  020, 026.
- **~21 itens** foram lidos (`Lido=Sim` no INDEX) mas ainda **não têm**
  resumo crítico escrito em lugar nenhum acessível para consolidar sem
  reabrir o PDF: 015, 021, 023, 024, 025, 028, 029, 030, 031, 032, 035,
  036, 038, 055, 057, 071, 074, 084, 089, 098, 099. Ficam para uma
  próxima versão — **não fabricados aqui**.
- O restante (~16 itens do range 001-100 ainda não lidos, mais itens
  101+ que são majoritariamente papers de referência para a linha de
  pesquisa qx+1 — Tao, Kontorovich-Lagarias, Applegate-Lagarias,
  Berg-Küppel, Mahler, etc. — e não alvos de crítica) fica
  explicitamente fora do escopo, sempre.

Esta v1 cobre portanto **16 itens revisados em profundidade até agora**
— não "16 de 97", já que os 97 incluem papers de referência (Tao,
Kontorovich-Lagarias etc.) que nunca serão alvo de crítica; uma fração
sobre 97 sugeriria uma cobertura-alvo que não existe. O paper deixa a
cobertura parcial explícita no texto e é estruturado para crescer por
revisões futuras.

## Tese central (não é só um catálogo)

**Revisada após `advisor()` apontar uma contradição interna**: a
primeira versão desta tese afirmava, para a coleção inteira, que "os
erros reais encontrados são sempre contidos, nunca invalidam o
argumento central do paper" — mas o item 004 (Seymour, Steiner
Sentence) contradiz isso diretamente: o erro ali é no **Teorema 5.1**,
o resultado titular do paper, não um detalhe periférico. A generalização
não se sustentava e um contraexemplo dela já estava neste próprio
documento, sob outro tópico.

O eixo de contraste correto com o paper 03 não é "os erros são
contidos" (falso, e além disso trivial — nenhum destes 16 papers
decide a conjectura, então "o erro nunca está no ponto que decidiria
a conjectura" não diz nada). É a **honestidade quanto ao escopo**:
nenhum dos 16 papers desta coleção veste uma conjectura de roupa de
teorema provado da Conjectura de Collatz — mesmo quando erram (Seymour
004), mesmo quando são extremamente repetitivos e autocitados (toda a
série Ruiz Castillo), a distinção teorema-vs-conjectura é mantida com
rigor quase universal. Isso contrasta com os 13 casos do paper 03, onde
o overclaim sistemático (alegar prova completa) é exatamente o que
falha. Esse é o contraste que atravessa a coleção inteira, sem exceção
conhecida nesta v1.

A **contenção de erro** (não afetar o restante do argumento) é uma
observação verdadeira, mas só sobre o **programa Ruiz Castillo
especificamente**, não uma generalização da coleção: 7 papers do mesmo
autor (Juan Carlos Ruiz Castillo, ScD., Universidad de San Carlos de
Guatemala), cada um aplicando um conceito clássico de teoria
ergódica/grandes desvios (pressão, geometria residual, cotas
dissipativas, TCL, operador de transferência, medidas de Gibbs,
princípio variacional, grandes desvios) à MESMA quantidade elementar (o
"drift residual" L_k(n)=k·log₂3−A_k(n), a mesma equação de ciclo já
conhecida deste projeto). Apresentação fortemente repetitiva/decorativa
(quadros coloridos, autocitação de 75-100%, revelando ~19-20 papers
quase idênticos na lista de referências), mas com um padrão de rigor
formal notavelmente estável: 5 dos 7 sem nenhum erro real, os 2 erros
reais encontrados (itens 013 e 026) são ambos do mesmo tipo —
inconsistência enunciado-vs-demonstração/resultado-já-provado, não erro
de cálculo — e ambos **genuinamente contidos** (Seção 5 e Seção 7
respectivamente, sem afetar conclusões posteriores do próprio paper).

O contraponto nítido é exatamente o item 004 (Seymour): o programa mais
prolífico da coleção mantém seus dois erros reais contidos; o resultado
autônomo mais afiado (aparato Lean, testes χ², citação de literatura
real) tem seu resultado central provavelmente errado. Contenção não é
uma propriedade da coleção — é algo que diferencia como Ruiz Castillo
erra de como Seymour erra, e essa diferença é o achado, não "todo mundo
erra pouco".

## Estrutura proposta

1. **Introdução**: contexto (diferença de escopo com o paper 03: aqui
   nenhum item alega provar a conjectura), natureza incremental deste
   documento, declaração explícita de cobertura parcial (16/97).

2. **Metodologia**: mesmo padrão do paper 03 (leitura integral,
   verificação computacional independente, `advisor()` para julgamentos
   sutis) — aqui adaptado, já que a maioria dos papers não faz alegação
   central a "reconstruir": para papers sem alegação de prova, o foco é
   verificar as identidades/teoremas concretos e avaliar a honestidade
   da rotulagem teorema-vs-conjectura.

3. **O programa Ruiz Castillo** (seção central, 7 subseções ou uma
   tabela-resumo + prosa):
   - 001 (Geometria Residual): formalismo correto, mas mesmo fato trivial
     repetido 5x como resultado nomeado, 10 quadros decorativos, zero
     conteúdo numérico, 100% autocitação (13/13); extensão computacional
     própria (Λ(t) explícito, singularidade em t=log2) feita para
     preencher a lacuna que o paper deixou.
   - 008 (Dissipative Bounds): mesmo padrão, 75% autocitação (revela
     ~12 títulos quase idênticos), sem erro.
   - 010 (TCL Residual): resultado central honestamente "Conjetura 4.2"
     apesar do título "Teorema"; testamos a consequência empírica
     (normalidade assintótica) em órbitas reais — plausível.
   - 013 (Operador de Transferência): **primeiro erro real** — Prop 5.3
     afirma limite→0, a própria demonstração deriva crescimento
     exponencial, símbolo ∎ aparece sem correção. Contido à Seção 5.
   - 017 (Medidas de Gibbs): volta ao padrão sem erro.
   - 020 (Princípio Variacional): sem erro, análise convexa abstrata
     corretamente aplicada.
   - 026 (Grandes Desvios): **segundo erro real** — Conjetura 7.3/Figura
     1/Conjetura 7.5 (Seção 7, conjectural) mutuamente consistentes mas
     contradizem a Proposición 3.4 (Seção 3, já provada) — confusão
     entre função de tasa de Cramér bilateral e unilateral. Confirmado
     por 3 métodos independentes. Contido à Seção 7.

4. **Os outros nove papers** (autores independentes, sem alegação de
   prova):
   - 002 (Adnan & Dar): extensão decimal-paridade conceitualmente mal
     definida (regra só existe para decimais finitos, medida zero).
   - 003 (Gilbert): sem erros, alta qualidade, conexão OEIS confirmada.
   - 004 (Seymour, Steiner Sentence): **provável erro real no teorema
     central** (distribuição correta parece ser (1/2)^k, não
     3^(k-1)/4^k alegado), com contraexemplo aritmético exato
     (n=68567) — reportado com a devida cautela epistêmica, já que o
     paper alega verificação formal em Lean não acessível a nós.
   - 005 (Seymour, Regex): majoritariamente correto, um erro pequeno e
     contido (Corolário 2.2), honestamente rotulado "working paper".
   - 006 (Anthony): sem erros, honestidade epistêmica excepcional
     (distingue 4 categorias de afirmação, autocorreção dentro do texto).
   - 007 (Hikawa): sem erros, puramente combinatório, explicitamente
     independente da verdade/falsidade da conjectura.
   - 009 (Olgac): não avaliável como certo/errado (linguagem não
     rigorosa o bastante para testar); conteúdo específico de Collatz é
     tautológico; sinal de alerta pela citação de uma alegação de prova
     de Goldbash do mesmo autor, não catalogada aqui.
   - 014 (Williams): sem erros matemáticos; dois erros pequenos de
     citação OEIS (contidos, não afetam nenhuma prova).
   - 019 (Fu, Liu & Wang): sem erros, contraste didático com o CTUHSK
     (paper 03) sobre honestidade quanto ao alcance do argumento de
     fechamento de ciclo.

5. **Discussão**: contraste com o paper 03 no eixo correto (honestidade
   de escopo — teorema vs. conjectura — não "gravidade do erro"); o
   programa Ruiz Castillo como estudo de caso de produção acadêmica
   rápida/incremental (real, não crank — tese de doutorado real citada)
   cujos erros ficam contidos, contra o contraponto do item 004
   (Seymour) cujo erro é central — contenção como propriedade de COMO
   um autor específico erra, não uma generalização da coleção; nota
   sobre cobertura parcial e como este documento deve crescer.

6. **Conclusão**.

## Fontes usadas nesta v1 (todas lidas na íntegra para esta versão)

H-039, H-040, H-041, H-042, H-044, H-046, H-047, H-048, H-049, H-050,
H-051, H-052, H-053, H-054, H-055, H-056 — não a partir da prosa do
`BACKLOG.md` (que é paráfrase, não fonte primária para alegações
específicas nomeando autores vivos), lição aplicada depois de um
`advisor()` ter pego exatamente esse problema durante a redação do
paper 03.

## Decisões (tomadas por precedente, sem precisar de rodada de pergunta)

- **Idioma**: dual EN/PT-BR, mesmo padrão dos papers 01 e 03.
- **Título**: "Scope Honesty in the Collatz-Adjacent Literature: A
  Running Calibration Against Complete-Proof Claims" — evita "erros"
  no título (a maioria dos 16 não tem erro; o achado é sobre
  honestidade de escopo, não sobre errar), e marca explicitamente que é
  um documento vivo ("Running").
