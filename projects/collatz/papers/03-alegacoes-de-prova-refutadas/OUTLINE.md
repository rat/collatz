# OUTLINE — Alegações de prova (ou refutação) completa da Conjectura de Collatz: catálogo e taxonomia dos erros

Status: rascunho de estrutura, ainda não escrito. Aberto por pedido explícito
do diretor científico em 2026-07-20 ("vamos iniciar o paper sobre erros dos
papers ao tentar provar a conjectura?"), com escopo confirmado via pergunta
direta no mesmo dia (ver decisão abaixo).

## Escopo (decisão 2026-07-20)

Este paper cobre **apenas** casos que alegam ter uma prova (ou refutação)
*completa* da Conjectura de Collatz — não qualquer paper da coleção do
Google Scholar que apenas toque no tema (esses ficam para o
`02-critica-cumulativa-literatura/`, item 8 do `BACKLOG.md`, que continua
`PENDENTE` e não deve ser iniciado sem novo pedido explícito).

Diferença estrutural chave em relação ao item 8: este catálogo é **fechável**.
O universo de "alegações de prova completa já encontradas e revisadas a
fundo" é finito e conhecido hoje — 12 casos, todos já com revisão
independente completa (leitura integral + verificação computacional quando
aplicável + consulta a Opus/Fable nos casos de julgamento matemático mais
sutil). Novos casos que aparecerem no futuro podem ser adicionados como uma
revisão do paper, mas ele tem um estado "completo" genuíno hoje — ao
contrário do item 8, que por design não tem ponto de fechamento.

O item 5 do BACKLOG (Santos 2018) está **absorvido** neste escopo — é um dos
12 casos abaixo, não precisa de um paper separado. O item 7 (Pratiher 2026,
erro de rotulagem de um coeficiente conjectural num resultado estatístico
parcial) **fica de fora**: não é uma alegação de prova completa da
conjectura, é uma categoria de erro diferente (rótulo incorreto num
resultado honestamente parcial, não um "buraco lógico" numa prova alegada
completa). Mantém-se como item isolado do BACKLOG, a escrever separadamente
se/quando pedido.

## Por que este catálogo é interessante (tese central)

Nenhum dos 12 casos é uma prova válida — mas eles **não falham da mesma
forma**, e as poucas formas em que falham se repetem com uma regularidade
que é, em si, o achado central do paper: quase todo erro localizado aponta,
por um caminho ou outro, para o mesmo "obstáculo estrutural" que nenhuma
tentativa de prova conhecida resolve (ver
`literature/overview-and-known-results.md`) — a impossibilidade de excluir
sequências adversárias arbitrariamente longas de passos crescentes sem, em
algum ponto, assumir exatamente o que se quer provar. A contribuição do
paper não é "aqui estão 12 papers errados" (pouco interessante por si só),
mas sim a **taxonomia recorrente** desses erros e o que ela revela sobre por
que a conjectura resiste.

## Estrutura proposta

1. **Introdução**
   - O fenômeno: Collatz atrai um volume incomum de "provas" em veículos de
     baixo rigor de revisão por pares (preprints, revistas genéricas,
     academia.edu/researchgate/rxiverse/engrxiv/osf.io). Regra de ceticismo
     já estabelecida em `literature/unverified-proof-claims.md`.
   - Metodologia de revisão usada em todos os 12 casos: leitura integral,
     reconstrução formal do argumento central, verificação computacional
     independente sempre que a alegação admite teste numérico, consulta a
     julgamento matemático externo (Opus/Fable) nos pontos mais sutis.
   - O que o paper NÃO é: não é uma crítica ad hominem aos autores nem uma
     alegação de má-fé — vários casos mostram honestidade epistêmica correta
     em outras partes do mesmo texto (rótulos corretos como "conjectura",
     admissão de limitações). O foco é estritamente o erro logico/matemático
     localizado.

2. **Taxonomia dos erros** (contribuição estrutural central, não apenas
   lista de casos). **Revisada em 2026-07-20 após ler os 12 H-arquivos
   na íntegra** — a primeira versão desta taxonomia (7 categorias) foi
   montada só a partir de título + uma linha de status por caso, e não
   sobreviveu à leitura completa (Boyle não se encaixava em nenhuma das
   7; a leitura revelou que ele e mais 4 casos são, na verdade, a MESMA
   falácia). A revisão apertou 7 categorias para 5, e uma delas — (C) —
   passou a concentrar 5 dos 12 casos, o que se tornou a tese central do
   paper, não um acidente de categorização.
   - **(A) Petição de princípio / circularidade** (3 casos): a "prova" de
     terminação usa, sem perceber, uma definição ou premissa logicamente
     equivalente à própria conjectura. Getachew/H-079 (relação "pai" =
     mapa de Collatz direto), Spencer 2025/H-081 ("ocupação de resíduo"
     ⇏ "valor exato atingido"), Yun/H-068 (três circularidades
     independentes: função de posto `r(x)` indefinida se a órbita não
     atinge 1, Teorema 6.1 assume "único ponto fixo conhecido" como se
     excluísse outros, falácia de cardinalidade infinita na Seção 5).
   - **(B) Generalização ilegítima de um caso específico para o caso
     geral** (2 casos): mostra algebricamente que uma sequência
     *particular* de passos converge/diverge e estende a conclusão para
     todas as sequências, sem limitar sequências adversárias. Santos
     2018 (Seção 2.6, K>30 hipotético com sequência fixa à mão), Halemane
     CTUHSK/H-043 (predecessor de ciclo hipotético assumido com expoente
     v=1 especificamente, quando v≥3 também é solução válida).
   - **(C) Propriedade agregada/média/assintótica confundida com garantia
     determinística/pontual sobre uma trajetória individual** (5 casos —
     categoria dominante, achado central do paper): a mesma falácia
     reaparece disfarçada por aparatos formais completamente diferentes.
     Mohammed/H-045 (Teorema de Baker aplicado a M≈2P, expectativa
     ERGÓDICA, no lugar da restrição de autoconsistência real de um
     ciclo M/P→log₂3); Boyle/H-065 (frequência de paridade e=2/3, válida
     só como média de ensemble sobre n aleatório, imposta como
     propriedade necessária de UMA trajetória hipotética fixa); Tynski/
     H-093 (axioma W6: limite de Lyapunov determinístico "forçado" por
     um argumento circular, sustentado só por verificação numérica em
     faixa estreita, refutado computacionalmente logo além dela);
     cluster Syzdykov/H-098+H-094 (com a crítica correta de Lafontaine &
     Cheong, H-095: compara uma CLASSE de funções O(f(n)) a um inteiro
     via ≤, erro categorial que — mesmo relaxado informalmente — só
     garantiria cota assintótica, nunca valor pontual); Barghout/H-116
     (densidade 2-ádica ESTÁTICA sobre o conjunto de inteiros pares,
     reimportada sem justificativa como estatística de VISITAS de uma
     órbita dinâmica específica). Confirmado nos próprios H-arquivos:
     H-093, H-095 e H-116 já se citam mutuamente e a H-045/H-065 como "a
     mesma falácia recorrente" — a categoria não é uma imposição externa,
     é um padrão que o próprio material já apontava.
   - **(D) Erro elementar isolado, contraexemplo trivial refuta um lema
     central** (1 caso): Roif/H-096 — confunde "densidade assintótica
     zero" com "conjunto vazio" (refutado por quadrados perfeitos,
     potências de 2), disfarçado por um espaço topológico de 3 pontos
     que nunca estabelece a identificação necessária. Único caso do
     catálogo sem relação com o obstáculo estrutural central — é um erro
     de teoria dos números elementar, não uma tentativa (mesmo que
     falha) de atacar o problema real.
   - **(E) Lacuna de rigor identificada, sem contraexemplo computacional
     encontrado** (1 caso, tratamento diferenciado): Spencer 2026/H-085 —
     mesmo autor do caso B em (A) (Spencer 2025), mas com anatomia de
     erro distinta: Teorema 14.1 prova ocupação de *classes* residuais,
     Teorema 14.2 conclui ocupação de *elementos individuais* sem
     justificar a passagem — mas a investigação computacional (cobertura
     testada até 10.000) não encontrou o gap se manifestar como falha
     real, ao contrário do caso irmão (Spencer 2025). Importante para o
     paper mostrar que nem todo "furo" é igualmente fatal nem do mesmo
     tipo.

3. **Estudos de caso** (um por paper — resumo da alegação, reconstrução do
   argumento central, erro localizado, veredito, status de verificação)
   1. Getachew (2025) — H-079
   2. Spencer, "Finite Block Exhaustion" (2025) — H-081
   3. Spencer, "Rooted Surjectivity" (2026) — H-085
   4. Santos (2018) — `literature/unverified-proof-claims.md` (sem H-number
      dedicado; análise vive diretamente no catálogo)
   5. Halemane, CTUHSK (2025) — H-043
   6. Mohammed, "Density Sieve" — H-045
   7. Boyle, "The Collatz Conjecture is True" — H-065
   8. Roif, "On the Convergence of the Collatz Function" (2026) — H-096
   9. Yun, "A Structural Proof..." — H-068
   10. Tynski, "A Common Proof of RH and Collatz" (2026) — H-093
   11. Disputa Syzdykov (2025-2026): "Disproof... O-notation" (H-098,
       original) × Lafontaine & Cheong, nota crítica (H-095, item 093) ×
       "Continued Disproof Sentence" (H-094, réplica não substantiva)
   12. Barghout, "On the Probabilistic Proof..." (2019) — H-116

4. **Discussão**
   - Achado central: 10 dos 12 casos (categorias A, B, C) falham, por
     rotas superficialmente muito diferentes (circularidade,
     generalização ilegítima, proxy agregado/assintótico), no mesmo
     ponto — nenhum estabelece um limite real sobre sequências
     adversárias de passos crescentes, o obstáculo estrutural que
     nenhuma tentativa conhecida resolve. A categoria (C), sozinha,
     concentra 5 casos e atravessa vocabulários completamente diferentes
     (teoria de números elementar, Baker, Lyapunov/2-ádico, Big-O,
     densidade estática) — o mesmo erro conceitual sobrevive a qualquer
     disfarce formal.
   - Os dois casos que não seguem o padrão: Roif (D, erro elementar
     isolado, sem relação com o obstáculo estrutural — mostra que nem
     todo erro em prova de Collatz é "do tipo interessante") e Spencer
     2026 (E, único caso onde a lacuna de rigor identificada não gerou
     contraexemplo computacional — mostra que nem todo furo é igualmente
     fatal, mesmo dentro do mesmo autor/família de argumento que no caso
     irmão, Spencer 2025, falhou de verdade).
   - Nota sobre honestidade epistêmica variável: contraste com o padrão
     observado no material do item 8 do BACKLOG (não citado como fonte
     primária aqui, apenas mencionado como contexto de que existem também
     muitos papers Collatz-adjacentes que rotulam corretamente resultados
     parciais como conjecturais — esses ficam fora do escopo deste paper).

5. **Conclusão**
   - Síntese: 12/12 alegações revisadas a fundo, 0 provas válidas, mas o
     valor do catálogo está na taxonomia recorrente, não na contagem.

## Decisões confirmadas (2026-07-20)

- **Idioma**: dual EN/PT-BR, mesmo padrão do paper 01 — `main.tex`
  (inglês, eventual submissão/publicação) e `main-pt-br.tex` (português,
  revisão do diretor científico), mantidos em sincronia.
- **Nível de formalidade**: paper completo, com o aparato formal
  concentrado na seção de taxonomia (contribuição central). Cada um dos
  12 estudos de caso fica enxuto — alegação + erro + veredito, ~1
  parágrafo cada — remetendo ao H-arquivo correspondente para a
  reconstrução formal e verificação computacional completas, sem
  reproduzi-las no corpo do paper.

## Fontes a consolidar (não recatalogar do zero)

- `literature/unverified-proof-claims.md` — catálogo cético já existente,
  cobre os casos 1-6 (Getachew, Spencer×2, Santos, Halemane, Mohammed).
- `literature/papers/INDEX.md` — linhas dos itens 049, 050, 076(075), 087,
  092, 093, 115, 123 têm os vereditos resumidos dos casos 7-12.
- Hipóteses individuais listadas na seção 3 acima — fonte primária de cada
  reconstrução formal e verificação computacional.
- `BACKLOG.md` itens 4 (processo geral de verificação) e 5 (pedido original
  do Santos, agora absorvido aqui).
