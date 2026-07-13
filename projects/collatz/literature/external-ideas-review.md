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
  acionável das três primeiras listas. Correção registrada após revisão
  (o enquadramento inicial era solto demais): E[3/2^a]=1 é uma afirmação
  de martingale/drift sobre o **modelo estocástico**, não literalmente uma
  equação de autofunção de Koopman para o mapa determinístico — a conexão
  com Koopman/Perron-Frobenius é uma **analogia a testar**, não uma
  identidade já estabelecida. Mantido como candidato de extensão (vetor de
  observáveis + DMD), mas **retido** até formular, antes de implementar, a
  afirmação falsificável específica que o resultado do DMD confirmaria ou
  refutaria — do contrário corre-se o mesmo risco de "matemática de
  aparência" já identificado na Lista 3.

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

## Lista 4 (15 ideias "corrigidas" após crítica à Lista 3)

Reação da mesma fonte externa à nossa crítica da Lista 3, com o objetivo
declarado de garantir pontes concretas com v₂, a árvore reversa, o drift
log(3/2) e o martingale. Avaliação item a item:

**Já feito / sobreposição forte com trabalho existente:**
- #4 (branching process com ramificação dependente do tipo de v₂) →
  essencialmente H-018 (árvore de Galton-Watson já construída e analisada).
- #10 (passeio aleatório com correlações de longo alcance / grandes
  desvios explícitos) → coberto por H-011/H-017 (Cramér, θ*=1).
- #2 (transfer operator em partições (v₂, mod 3^k)) → sobrepõe H-024:
  já demonstramos que a densidade não é função de resíduo 3-ádico
  limitado, então qualquer truncamento finito desse operador não pode ser
  exato.

**Testado nesta sessão:**
- **#9 (busca de invariantes lineares sobre GF(2)/Z)** → escolhido como
  abertura por ser barato, rápido e ter resultado interpretável em
  qualquer desfecho. Testado e **refutado com mecanismo identificado** —
  ver `hypotheses/H-025-linear-bit-correlations.md`. Toda correlação
  bit-a-bit encontrada se reduz ao valor exato de a (já conhecido) e ao
  bias clássico e de curto alcance de carry em adição binária — nenhuma
  informação nova sobre a estrutura do Collatz.

**Vago ou de alto risco de "matemática de aparência", não priorizado:**
#11 (cobordismo combinatório — não é mais que indução renomeada, sem
técnica nova), #12 (persistent homology — sem mecanismo demonstrado
ligando topologia da nuvem de pontos a teoria de números, exigiria
bibliotecas novas), #3, #6, #7, #13 (vagos: pedem "construa", "derive",
"mostre decréscimo" sem especificar o passo concreto que fecharia o
argumento).

**Candidatos remanescentes de interesse real, não implementados ainda:**
- #15 (operador de transferência com memória 3-ádica finita crescente,
  medindo a *taxa* na qual a aproximação diverge conforme a magnitude
  cresce) — diferente de #2: H-024 refutou a existência de uma
  aproximação *exata* de dimensão finita, mas não caracterizou a taxa de
  divergência da aproximação em função da profundidade de memória K. É
  uma extensão legítima e ainda em aberto de H-024.
- #14 (programação dinâmica / estratégia adversarial de máxima subida) —
  conecta com a literatura já catalogada de limites inferiores em ciclos
  (Simons & de Weger, Eliahou), potencial ângulo novo para H-008/H-009.
- #1 (Koopman/DMD vetorial) — mantido em espera até que a afirmação
  falsificável específica seja formulada antes da implementação (ver
  nota acima).

## Conclusão e próximo passo proposto

A extensão fechada e mais promissora agora é **#15**, por continuar
diretamente H-024 com uma pergunta nova e bem definida (taxa de
divergência, não apenas existência). #14 é a segunda candidata mais
concreta. Koopman/DMD (#1) fica reservado até ter uma afirmação
falsificável explícita — não descartado, apenas não priorizado sem essa
condição.
