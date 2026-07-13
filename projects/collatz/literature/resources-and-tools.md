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

## Ferramentas práticas de busca de "delay records" (checagem de novidade de H-028)

- [`rogerdahl/cuda-collatz`](https://github.com/rogerdahl/cuda-collatz) — calculadora
  de "Delay Records" via GPU. README documenta explicitamente as otimizações usadas:
  pular N par (trivial), pular N≡2 mod3 (= nosso H-007, já conhecido), e **pular
  N≡5 mod8 exceto o próprio 5** (= nosso H-014, quase palavra por palavra, incluindo
  a mesma exceção). Usa também uma técnica geral de "sieve" (checar se dois caminhos
  se juntam) que exclui ~80% dos N restantes — mais do que nossos 62,5% (H-028),
  mas de forma computacional/empírica, não como fórmulas fechadas.
- [`AlexMorson/Collatz-Delay-Records`](https://github.com/AlexMorson/Collatz-Delay-Records)
  — outro buscador de delay records. Não menciona mod8/mod9 explicitamente, só uma
  técnica de "skip" via potências de 2 e 3.
- Nenhuma das duas fontes menciona uma exclusão mod9 (nosso H-022) — não temos
  confirmação de que seja novo, só ausência de evidência do contrário.

## Winkler (2026) — "Deterministic Structures in the Stopping Time Dynamics of the 3x+1 Problem"

[arXiv:1709.03385](https://arxiv.org/abs/1709.03385) — lido por completo (PDF salvo
localmente durante a sessão de 2026-07-13). **Tópico diferente do nosso**: estuda o
*coefficient stopping time* de Terras (σ*, uma variante algébrica do stopping time
clássico, conjecturalmente igual a ele) e constrói uma árvore recursiva de classes de
congruência mod 2^σₙ que caracteriza TODOS os inteiros com um dado valor de σ*— não
trata de recordistas (delay records) nem de exclusões mod3/mod8/mod9. Reformula a
conjectura como um "problema de cobertura Diofantina" (união das classes cobre todos
os inteiros?). Não resolve nem contradiz nada do nosso H-007/H-014/H-022/H-028;
não usado para a checagem de novidade, mas relevante para catalogar caso a via de
"árvore de classes de congruência" seja retomada no futuro (conecta com nosso H-013/
H-018 em espírito, embora com maquinário diferente).
