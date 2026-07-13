# Revisão crítica de três listas de ideias externas (outras IAs)

Data: 2026-07-13. O diretor científico trouxe três listas de sugestões
geradas por outros modelos de IA, pedindo avaliação crítica: o que já
fizemos (descartar), o que é vago demais, e o que vale seguir.

## Critério de avaliação

Para cada item: existe uma ponte concreta e verificável entre a máquina
matemática proposta e a estrutura combinatória real do Collatz (paridade,
valuação 2-ádica, árvore reversa, resíduos mod 3^k)? Ou é só vestir o
problema com formalismo de outra área sem mecanismo demonstrado? Esse
segundo padrão é exatamente o erro que já identificamos e catalogamos no PDF
de Santos (`unverified-proof-claims.md`) — formalismo elaborado sem
substância verificável.

## Lista 1 (10 ideias + 1 sobre embeddings/autoencoders)

Já fazemos (com outro nome ou parcialmente):
- Física estatística / grandes desvios → H-001, H-010, H-011, H-017.
- Expoente de Lyapunov → parcialmente, via θ*=1 de H-017.
- "Linguagem própria" para descrever o sistema → nossa notação de
  valuações a(n) já cumpre esse papel.
- Formalização em Lean/SageMath → já no roadmap de longo prazo, fora de
  escopo imediato.
- Meta-pesquisa (registrar o que já foi tentado) → é a função do
  `STATE.md`/`BACKLOG.md`.

Descartados por vagueza ou dependência de ferramentas não instaladas
(numpy/scipy/PyTorch) sem justificativa clara de que resolveriam algo que
as ferramentas atuais não resolvem: descoberta automática de conjecturas
via busca de padrões (item de "brute-force pattern mining"), embeddings /
autoencoders (item 11) — não há evidência de que uma representação latente
aprendida revelaria estrutura que a valuação 2-ádica explícita já não
mostra, e treinar uma rede não é falsificável do mesmo jeito que uma prova
ou um contra-exemplo.

## Lista 2 ("outras dimensões")

- Espaço de estados / espaço simbólico → já fazemos, nossa notação de
  sequência de paridades é exatamente isso, comprimida.
- 2-ádico → coberto extensivamente (H-005, H-007, H-014, H-015, H-022,
  `literature/approaches-2adic-ergodic.md`).
- **Tensor / Koopman operator ("Project PHI")** → o item mais concreto e
  acionável das três listas inteiras. Insight chave: **H-017 já é**, sem
  usarmos o nome, um cálculo de autovalor de Koopman para um observável
  escalar (E[3/2^a]=1 é exatamente a equação de autovalor 1 do operador de
  Koopman aplicado ao observável log n). Isso sugere uma extensão natural e
  ainda não tentada: um vetor pequeno de observáveis simultâneos (n^θ,
  resíduos mod 2^k, mod 3^k, valuação corrente) e uma aproximação DMD
  (Dynamic Mode Decomposition) da dinâmica linearizada nesse espaço. Ver
  proposta de H-025 no BACKLOG.

## Lista 3 (15 ideias especulativas de matemática avançada)

Esta lista é qualitativamente diferente das outras duas: teoria de Galois,
esquemas/fibrados, functores/categorias, operadores quânticos
(Hamiltoniano, gap espectral, Lieb-Robinson), espaço de Teichmüller,
números transcendentes, teoria de campos conforme/OPE, teoria da homotopia/
cobordismo, mecânica estatística de spins, teoria de modelos, álgebras de
von Neumann, grupos quânticos, formas modulares, subshifts de tipo finito,
análise não-padrão.

**Avaliação**: descartada a maioria por falta de qualquer ponte
demonstrada — nenhum desses formalismos tem, na literatura ou na nossa
própria análise, um mecanismo concreto ligado à estrutura real do problema
(3n+1, paridade, árvore reversa). O risco de investir tempo aqui é gerar
"matemática de aparência" — exatamente o padrão que criticamos no PDF do
Santos.

Exceções tratadas com mais cuidado:
- **Subshifts de tipo finito**: já corresponde, na prática, à nossa notação
  de sequências de paridade/valuação — não é uma ideia nova, é uma
  formalização de algo que já fazemos.
- **Operadores de transferência quânticos (Hamiltoniano, gap espectral)**:
  em vez de descartar por especulação, testei computacionalmente antes de
  julgar (H-024/E-024). Resultado: a densidade do subárvore reverso D(v)
  exige precisão 3-ádica ilimitada (variação >300× entre números com
  mesmo resíduo mod 3^6). Isso mostra que a obstrução real é sobre a
  PRECISÃO NECESSÁRIA para descrever o sistema, não sobre o tipo de
  operador usado — um operador de transferência quântico de dimensão
  finita sofreria exatamente a mesma obstrução que um operador clássico de
  dimensão finita. Testado e descartado com evidência direta, não por
  intuição.

## Conclusão e próximo passo proposto

Das três listas, a única direção nova, concreta e ainda não testada é a
extensão de H-017 para uma análise Koopman/DMD vetorial (Lista 2). Proposta
registrada no BACKLOG como candidata a H-025 — pendente de confirmação do
diretor científico, já que representa mudança de metodologia (álgebra
linear/autovalores aplicada a observáveis, em vez de teoria de números
pura).
