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
   lista de casos)
   - **(A) Petição de princípio / circularidade**: a "prova" de terminação
     usa, sem perceber, uma definição logicamente equivalente à própria
     conjectura. Casos: Getachew/H-079, Spencer 2025/H-081, Yun/H-068.
   - **(B) Generalização ilegítima de um caso específico para o caso geral**:
     mostra algebricamente que uma sequência *particular* de passos
     converge/diverge e estende a conclusão para todas as sequências, sem
     limitar sequências adversárias. Casos: Santos 2018, Halemane
     (CTUHSK)/H-043.
   - **(C) Substituição da restrição real por um proxy estatístico/médio
     mais fraco**: usa uma ferramenta forte (Teorema de Baker, argumento
     ergódico) mas troca a condição de auto-consistência real de um ciclo
     ou órbita por uma expectativa média/estática, produzindo uma checagem
     vazia. Casos: Mohammed/H-045, Barghout/H-116.
   - **(D) Contraexemplo elementar refuta um lema central**: erro não é
     sutil, é uma afirmação matemática simplesmente falsa, com
     contraexemplo direto. Caso: Roif/H-096.
   - **(E) Verificação numérica limitada apresentada como geral**: alegação
     "forçada"/estabelecida mas só checada numericamente até um limite
     pequeno, refutável além dele. Caso: Tynski/H-093.
   - **(F) Disputa de refutação sem engajamento substantivo**: réplica a uma
     crítica reafirma o erro original sem rebatê-la. Cluster
     Syzdykov/H-094+H-098 (com a nota crítica de Lafontaine & Cheong,
     item 093, como terceira peça do mesmo debate).
   - **(G) Lacuna de rigor identificada mas sem contraexemplo computacional
     encontrado** — caso diferenciado, importante para mostrar que nem todo
     "furo" é do mesmo tipo nem igualmente fatal: Spencer 2026/H-085 (mesmo
     autor do caso B em (A), mas com anatomia de erro distinta e sem
     refutação computacional).

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
       original) × Lafontaine & Cheong, nota crítica (item 093) ×
       "Continued Disproof Sentence" (H-094, réplica não substantiva)
   12. Barghout, "On the Probabilistic Proof..." (2019) — H-116

4. **Discussão**
   - Convergência de quase todos os erros para o mesmo obstáculo estrutural
     (sequências adversárias de passos crescentes não limitadas) — por
     rotas superficialmente muito diferentes (petição de princípio,
     generalização ilegítima, proxy estatístico fraco).
   - O que distingue os dois casos que NÃO seguem esse padrão: Roif (D,
     erro trivial sem relação com o obstáculo estrutural) e a disputa
     Syzdykov (F, sobre uma alegação de *refutação*, não prova — erro
     categorial diferente, sobre o que O-notation pode/não pode mostrar
     sobre convergência pontual).
   - Nota sobre honestidade epistêmica variável: contraste com o padrão
     observado no material do item 8 do BACKLOG (não citado como fonte
     primária aqui, apenas mencionado como contexto de que existem também
     muitos papers Collatz-adjacentes que rotulam corretamente resultados
     parciais como conjecturais — esses ficam fora do escopo deste paper).

5. **Conclusão**
   - Síntese: 12/12 alegações revisadas a fundo, 0 provas válidas, mas o
     valor do catálogo está na taxonomia recorrente, não na contagem.

## Decisões em aberto (para o diretor científico)

- **Idioma**: paper 01 tem versão EN (`main.tex`, submissão) e PT-BR
  (`main-pt-br.tex`, revisão do diretor). Este paper é mais uma nota
  crítica/catálogo do que um paper de resultado original — vale o mesmo
  padrão dual, ou basta uma versão (e nesse caso, qual)?
- **Nível de formalidade**: nota curta tipo "comentário crítico" (como
  originalmente pedido para o item 5/Santos sozinho) ou paper completo com
  aparato formal por caso (reconstrução de lema, contraexemplo explícito)?
  Dado que agora são 12 casos e uma taxonomia, o formato "paper completo"
  parece mais adequado que "nota curta", mas cada estudo de caso pode ainda
  ser enxuto (a análise detalhada já existe nos H-arquivos; a seção 3 deste
  paper resume, não reproduz).

## Fontes a consolidar (não recatalogar do zero)

- `literature/unverified-proof-claims.md` — catálogo cético já existente,
  cobre os casos 1-6 (Getachew, Spencer×2, Santos, Halemane, Mohammed).
- `literature/papers/INDEX.md` — linhas dos itens 049, 050, 076(075), 087,
  092, 093, 115, 123 têm os vereditos resumidos dos casos 7-12.
- Hipóteses individuais listadas na seção 3 acima — fonte primária de cada
  reconstrução formal e verificação computacional.
- `BACKLOG.md` itens 4 (processo geral de verificação) e 5 (pedido original
  do Santos, agora absorvido aqui).
