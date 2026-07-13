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

## Reyes Jiménez (2026) — "A Fibonacci theorem for Collatz trajectories via modular graph structure"

[arXiv:2606.02621](https://arxiv.org/abs/2606.02621) — lido por completo.
Prova que exatamente F(m+1) inteiros ímpares em {1,...,2^m} têm órbita que
*evita* visitar o resíduo 4 (mod 6) nos passos 2..m (contagem via análise
espectral do grafo de transição mod6, gap espectral φ vs 2). **Conexão
real e verificada com H-027**: o grafo de transição deles (resíduo 4 → {2,5})
é exatamente o mecanismo algébrico da nossa prova (N≡4mod6 par, N/2 cai
em {2,5} mod6, a classe excluída por H-007) — anotado em H-027.md como
coincidência estrutural interessante, não uma nova prova.

## Carelli (2026) — "Loop Termination and Generalized Collatz Sequences"

[arXiv:2605.15094](https://arxiv.org/pdf/2605.15094) — conecta a
decidibilidade de terminação de loops de uma variável com restrições
lineares à conjectura de Collatz generalizada (mapas lineares por classe
residual). Resultado: terminação é decidível em tempo polinomial *se* uma
conjectura de longa data sobre sequências de Collatz generalizadas for
verdadeira (e vice-versa). Tópico de ciência da computação teórica
(decidibilidade), não se conecta às nossas questões residuais/de
recordistas. Catalogado como contexto — não perseguido further.

## Yolcu, Aaronson & Heule (2021-2022) — "An Automated Approach to the Collatz Conjecture"

[arXiv:2105.14697](https://arxiv.org/abs/2105.14697) — paper respeitado
(Scott Aaronson é autor bem conhecido; publicado em CADE-28 e Journal of
Automated Reasoning). Constrói um sistema de reescrita de strings
(representação binária-ternária mista) cuja terminação é EQUIVALENTE à
conjectura de Collatz, e usa provadores automáticos de terminação
(interpretações de matriz/árticas). Não prova a conjectura, mas mostra que
abordagens ingênuas de reescrita unária não admitem prova de terminação
por esse método. Área especializada (SAT/prova automatizada de teoremas)
distante do nosso toolkit atual — catalogado como referência séria, não
perseguido nesta sessão.

## Outras duas leituras rápidas (2026-07-13) — sem conexão nova encontrada

- **Angermund (2025)**, ["A Two-Operator Calculus for Arithmetic-Progression
  Paths in the Collatz Graph"](https://arxiv.org/pdf/2506.19115) — reformulação
  elementar via dois operadores (T₁,T₂) em progressões aritméticas S(a,b).
  Contribuição real: prova simples (invariante afim b=a−1) de que nenhuma
  órbita pode consistir de infinitos passos ímpares consecutivos — um fato já
  conhecido, mas com um argumento mais curto que o clássico (comparação de
  taxas 3/2 vs 1/2). Não discute recordistas, exclusões residuais, nem bit-4.
  Sem conexão com nossas questões abertas.
- **Bouhamidi (2026)**, ["An Extension of the Collatz Conjecture modulo
  2^p+2^q"](https://arxiv.org/pdf/2601.06208) — generaliza para uma família de
  mapas "tipo-Collatz" (parâmetros d,α,β) e estuda quais membros da família
  têm dinâmica bem-comportada (ciclos finitos, sem divergência). Tópico
  genuinamente diferente (família de mapas generalizados, não o 3n+1
  clássico) — confirmado que não discute recordistas/stopping-time records.
  Sem conexão com nossas questões abertas.

## Chang (2026) — "A Structural Reduction of the Collatz Conjecture to One-Bit Orbit Mixing"

[arXiv:2603.25753](https://arxiv.org/abs/2603.25753) — lido por completo e
**verificado independentemente** (ver `hypotheses/H-030-chang-onebit-mixing-verification.md`).
Reduz a conjectura, no mapa de Syracuse comprimido, a uma pergunta muito
específica: o bit 4 do valor de fim-de-burst determina o comprimento do
próximo gap (para a classe dominante n≡1 mod8); a conjectura equivale a
mostrar equilíbrio dessa subsequência esparsa entre as classes 9 e 25
(mod 32). **Conexão real com H-024**: a "Rota A" do paper (contração via
sistema de transferência 5×5) trava na mesma obstrução que encontramos —
resolução mais fina não fecha uniformemente. Verificamos os três lemas
centrais (0 falhas) e tentamos uma extensão com nossos 148 recordistas
reais — resultado consistente com o que o próprio paper já documenta
(desvio de órbita individual, não achado novo), com cuidado explícito para
não cair em pseudo-replicação (órbitas de recordistas colidem entre si).

## Pratiher (2026) — "Recurrence Structures, Finite State Decomposition, and Statistical Bias in Collatz Path Sequences"

[arXiv:1608.03600](https://arxiv.org/pdf/1608.03600) — lido por completo.
**Nota de integridade**: um resumo inicial via WebFetch alegou que este
paper discutia "delay records" e exclusões de classe residual para
recordistas — ao ler o PDF diretamente, isso é **falso** (alucinação do
resumo automático); o paper não menciona recordistas em nenhum lugar. É
sobre um tópico diferente: redução da conjectura à classe n≡3 mod4,
seis "formas recorrentes" mod9 que classificam para qual potência de 2
cada inteiro converge, e viés estatístico na frequência de terminação
(forma 'a' domina ~97,6%). Catalogado como lembrete de sempre verificar
a fonte primária antes de confiar em resumos de ferramenta.

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
