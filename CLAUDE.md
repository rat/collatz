# ResearchOS — instruções para o Claude Code

Este repositório é um laboratório de pesquisa assistida por IA. O primeiro projeto
ativo é `projects/collatz`. A estrutura foi desenhada para crescer (novas linhas de
pesquisa em `projects/<nome>/`), mas hoje só existe Collatz — não crie estrutura para
projetos que ainda não existem.

## Início de sessão

1. Leia `projects/collatz/STATE.md` (estado atual: hipóteses abertas, últimas
   descobertas, ideias descartadas, próximos passos).
2. Leia `ROADMAP.md` para prioridades gerais.
3. Continue de onde parou. Não recomece a exploração do zero.

## Durante a sessão

- Nova hipótese → siga `protocols/new-hypothesis.md`.
- Novo experimento (script, cálculo, teste numérico) → siga `protocols/new-experiment.md`.
- Busca literária dirigida (ingrediente técnico específico, não a coleção ampla do
  Google Scholar) → siga `protocols/literature-search.md`.
- Paper próprio (resultado final, distinto de notas sobre papers de terceiros) →
  vive em `projects/collatz/papers/<NN-titulo>/`, com um `OUTLINE.md` mínimo. Ver
  `projects/collatz/papers/README.md`.
- Registre decisões e descobertas relevantes em `STATE.md` conforme forem acontecendo,
  não só no final.
- Não crie agentes, personas ou protocolos novos "por precaução". Só formalize algo
  quando a necessidade aparecer de verdade (ex: se retrabalho ou perda de contexto virar
  um problema recorrente).

## Consultando o Fable (IA externa consultora de matemática)

Quando surgir dúvida de matemática/prova que exija julgamento externo, consulte o
Fable via `Agent` com `subagent_type: "general-purpose"` e `model: "fable"`
(NÃO `subagent_type: "fable"` — isso não existe e erra). Dê contexto completo e
autocontido no prompt (o Fable não vê o histórico da sessão). Reserve o Fable para
julgamento matemático de verdade; busca/leitura de papers é mais barata feita
diretamente (WebSearch/WebFetch).

## Fim de sessão — checkpoint

Sempre feche a sessão com um checkpoint (`protocols/checkpoint.md`):

1. Atualize `projects/collatz/STATE.md`.
2. `git add -A`
3. `git commit` com mensagem descritiva do que avançou.
4. `git push`.

Nunca deixe trabalho sem commit ao final da sessão — este repo é a memória persistente
do projeto entre sessões.
