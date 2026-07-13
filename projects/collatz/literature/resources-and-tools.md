# Recursos e ferramentas

## Bibliografias de referência (Lagarias)

Jeffrey Lagarias mantém as bibliografias anotadas mais completas do problema:

- [The 3x+1 Problem: An Annotated Bibliography (1963–1999)](https://arxiv.org/abs/math/0309224)
- [The 3x+1 Problem: An Annotated Bibliography II (2000–2009)](https://arxiv.org/abs/math/0608208)
- "The 3x+1 Problem: An Overview" — survey introdutório de Lagarias.

Ponto de partida obrigatório antes de "reinventar" qualquer abordagem — alta
probabilidade de já ter sido tentada e catalogada aqui.

## Projeto de formalização em andamento — ccchallenge.org

Projeto comunitário ativo com objetivo de **formalizar sistematicamente a
literatura de Collatz** (363+ artigos catalogados, status: identificado → em
formalização → pronto para auditoria → formalizado). Usa fórum GitHub e Discord.
Relevante como (a) fonte de triagem do que já foi tentado, e (b) possível
inspiração de processo para nosso próprio `protocols/`.
https://ccchallenge.org/

## Paper metodológico — colaboração humano-LLM em Collatz

["Exploring Collatz Dynamics with Human-LLM Collaboration"](https://arxiv.org/pdf/2603.11066)
— diretamente relevante à forma como este laboratório opera. PDF salvo em
`/home/rat/.claude/projects/-home-rat-Google-Projetos-Claude-ResearchOS/25582fe4-e7a2-4675-aadb-21cdcad240de/tool-results/webfetch-1783944652055-osbeny.pdf`
(cache local da sessão — se for referenciar de novo no futuro, baixar o PDF para
dentro deste repositório, essa cache não é persistente).

Lições reportadas:

- **O que funcionou**: validação humana rigorosa filtrando sugestões implausíveis da
  IA; exploração sistemática de variações matemáticas; iteração rápida entre
  proposição e verificação.
- **O que não funcionou**: confiar em propostas de LLM sem verificação; perguntas de
  pesquisa formuladas de forma vaga; falta de estrutura matemática clara antes de
  pedir à IA para explorar.
- **Recomendação central dos autores**: LLMs funcionam bem como assistentes
  colaborativos sob supervisão rigorosa, não como substitutos de julgamento
  matemático experiente.

Isso reforça o desenho do `protocols/new-hypothesis.md` e `new-experiment.md` —
toda hipótese gerada precisa de um caminho claro de verificação, e resultados de
experimento precisam ser reprodutíveis, não apenas "a IA disse que funciona".
