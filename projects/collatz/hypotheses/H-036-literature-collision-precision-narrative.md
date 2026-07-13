# H-036 — Colisão de literatura: a "obstrução de precisão" que eu ia sintetizar já é o resultado central de um survey de 216 páginas

Status: nota de recalibração (não é uma hipótese testada — é um registro
honesto de um quase-erro de novidade, pego antes de reportar)
Criada em: 2026-07-13

## O que aconteceu

Depois de H-024, H-013/H-018, H-025 (Koopman descartado), H-026 e H-032,
eu ia escrever uma síntese própria: "uma obstrução (precisão 3-ádica
ilimitada), confirmada de forma independente em pelo menos 6 ângulos
diferentes, incluindo a Rota A do paper de Chang (H-030)". Antes de
escrever, segui a mesma disciplina de checagem de novidade usada em
H-028 (e a lição de sempre ler a fonte primária, de Pratiher/H-030) e
pesquisei se esse tipo de "obstrução geral" já era documentado.

Encontrei arXiv:2603.11066 (Chang, 2026, "Exploring Collatz Dynamics
with Human-LLM Collaboration") — um survey de 216 páginas, lido
diretamente em PDF (não via resumo automático, que numa busca inicial
alegou coisas que só a leitura direta pôde confirmar com precisão). É o
survey-pai da companion paper já usada em H-030 (confirmado pela própria
lista de referências dele). Detalhes completos em
`literature/resources-and-tools.md`.

## O resultado da checagem

**A narrativa geral já é o resultado central do survey** (Teorema 13.1
"Paradigm Exhaustion": 29 paradigmas testados, todos com a mesma barreira
distribucional-para-pontual; Teorema 13.2: essa barreira é equivalente à
própria conjectura). Escrever isso como nossa síntese seria repetir o
erro de superclaim de H-028 — só que numa escala muito maior (29
paradigmas documentados a fundo contra nossos ~6 mencionados de
passagem).

## O que sobrevive, com escopo correto

- **H-024 continua válido** como resultado técnico específico: D(v)
  (densidade da subárvore de predecessores de um nó FIXO v) não é
  nenhum dos 29 paradigmas de Chang — todos tratam de convergência de
  órbita para frente, nenhum de densidade de subárvore reversa de um nó
  específico. É uma instância independente e genuína do mesmo fenômeno
  geral, obtida por uma rota diferente da dele — mas é **confirmação,
  não descoberta**, e vale só para o K=6 testado diretamente mais um
  argumento mecanicista (não uma prova formal para todo K).
- **Nenhum resultado nosso foi invalidado.** Só o enquadramento
  ("síntese nova") deixou de fazer sentido.

## Por que isso não é um retrocesso

A disciplina que evitou o erro (checar novidade antes de escrever,
ler a fonte primária em vez de confiar no resumo de busca) é
exatamente a mesma que already tinha nos poupado de superclaims em
H-028, H-030 e H-032. Funcionou de novo, numa escala onde o erro teria
sido bem mais visível se publicado.

## Implicação estratégica (a parte que importa)

As duas linhas mais desenvolvidas deste projeto — exclusão de
recordistas por classe residual (H-007/H-014/H-022/H-027/H-028) e a
obstrução de precisão 3-ádica (H-013/H-018/H-024/H-025/H-026/H-030/H-032)
— **são ambas, agora, sabidamente não-novas no nível geral**: a primeira
é folclore de `cuda-collatz`; a segunda é o resultado central de um
survey de 216 páginas contemporâneo. Continuar gerando H-0XX dentro de
qualquer uma das duas veias tem valor pedagógico/de verificação, mas não
deve ser confundido com progresso em direção a algo publicável. A
próxima iteração precisa de um alvo estruturalmente diferente.

## Direção nova a partir daqui

H-035 (checagem Pratiher) estabeleceu uma distinção categórica que passou
despercebida até agora: D(v) é uma densidade **por-nó** (sofre a
obstrução de H-024); Freq_a(N) de Pratiher é uma **média de conjunto**
sobre {1,...,N} — um tipo de objeto onde ferramentas de equidistribuição/
operador de transferência costumam funcionar bem MESMO QUANDO o objeto
por-nó subjacente é irregular (é exatamente o que o próprio item 1 da
lista de Chang mostra: "operador de transferência — gap uniforme
provado, produz equidistribuição" — funciona quando a pergunta é sobre
médias/frações, falha quando a pergunta é pontual). A obstrução de H-024
não se aplica aqui. Ver H-037 para a tentativa de derivar α≈0,9762 de
Pratiher por essa via.

## Atualizações

- 2026-07-13: nota criada, recalibração feita, direção nova aberta em
  H-037.
