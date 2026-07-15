# H-056 — Revisão do paper #026 (Ruiz Castillo, "Grandes Desviaciones Residuales") — erro real: Conjetura 7.3/Figura 1/Conjetura 7.5 contradizem a Proposición 3.4 já provada

Status: revisão externa concluída — Seções 1-5 corretas; Seção 7
(conjectural) inconsistente com a Proposición 3.4 (Seção 3, já
demonstrada)
Criada em: 2026-07-14
Origem: Ruiz Castillo, J.C. (2026), *Grandes Desviaciones Residuales de
Ruiz Castillo en la dinámica acelerada de la Conjetura de Collatz*,
Zenodo, DOI [10.5281/zenodo.20767811](https://zenodo.org/records/20767811),
44 páginas. Item 026 da coleção (`literature/papers/INDEX.md`) —
listado lá via ResearchGate (que bloqueia download automatizado);
localizamos o mesmo paper espelhado no Zenodo (acesso aberto) e
salvamos localmente: `literature/papers/026_Grandes-Desviaciones-Residuales-Ruiz-Castillo.pdf`
(md5:f12d30c3d0e052854f6da782f0af7bab, conferido contra o md5 listado
pelo próprio Zenodo).

## O paper

Sétimo paper deste autor revisado na coleção (após item 001/H-039, item
008/H-050, item 010/H-052, item 013/H-053, item 017/H-054, item
020/H-055). Introduz a "teoria de Grandes Desviaciones Residuales de
Ruiz Castillo" para estudar a raridade dos blocos de deuda residual
positiva na dinâmica acelerada U(n)=(3n+1)/2^{v₂(3n+1)}. Define a
palavra de valuações a(n)=(a₀(n),a₁(n),...), a_j(n)=v₂(3·Uʲ(n)+1), a
deuda residual L_k(n)=k·log₂3−A_k(n) (A_k = soma das k primeiras
valuações), o evento residual {L_k/k≥x}, e a função de tasa residual

```
I_RC(x) := −lim_{k→∞} (1/k) log P(L_k/k ≥ x)        (Definición 3.1)
```

Sob o "modelo probabilístico ideal" (a_j iid Geométrica(1/2), mesma
distribuição já estabelecida em H-001/H-011: E[a]=2, Var[a]=2), prova
(Teorema 5.2, pág. 29-31) que existe c>0 com P(L_k≥0)≤e^{-ck} via
Chernoff/Markov padrão. Honesto: repete em duas passagens diferentes
(pág. 41 e 42) que "el marco desarrollado no demuestra la Conjetura de
Collatz" / "no cierra la Conjetura de Collatz".

## O que foi verificado

**Parte 1 (identidades algébricas, Seções 1-2)** — confirmadas sem
exceção contra **órbitas reais** de Collatz (não o modelo i.i.d.
abstrato): Proposición 1.2 (interpretação multiplicativa e critério de
sinal, via aritmética inteira exata `3^k` vs `2^{A_k}`, sem nenhum
log), Proposición 2.3 (equivalência residual-disipativa), Corolario
2.4 (evento crítico x=0), Proposición 2.5 (monotonia de eventos, o
análogo "para k finito, exato" da Proposición 3.4). 2160 casos, 0
falhas.

**Parte 2 (modelo probabilístico ideal)** — Proposición 4.4 (E[a]=2),
Teorema 4.7 (drift residual esperado negativo, log₂3−2<0) e Teorema 5.2
(cota de Chernoff) todos confirmados: o MGF Ψ(t)=e^{t·log₂3}·(e^{-t}/2)/(1−e^{-t}/2)
derivado independentemente bate exatamente com a demonstração do
próprio paper (mesma conta, verificada símbolo a símbolo contra o PDF).
t₀ ótimo ≈0.3036, c=I_RC(0)≈0.05498>0.

## Achado central — inconsistência interna real

A Definición 3.1 define I_RC(x) via o evento de cauda **unilateral**
{L_k/k≥x}. A **Proposición 3.4** (pág. 19, **já provada** no corpo do
texto) mostra corretamente que essa I_RC é monótona não-decrescente:
se x₁≤x₂ (e ambos os limites existem), então I_RC(x₁)≤I_RC(x₂).

A **Figura 1** (pág. 33, Seção 6, explicitamente "conceptual") mostra
I_RC(x) como uma curva em V/U: decresce de ~1.1 (em x=−1) até 0 (no
mínimo, em x*=log₂3−2≈−0.415) e depois cresce de novo — valores
**positivos** também para x<x*. O texto que a acompanha (pág. 32) diz
que a função "debe comportarse como una función convexa... cuyo mínimo
se alcanza en el valor típico del drift residual" e que "las
desviaciones alejadas de x* poseen costo exponencial positivo"
(alejadas = nos dois sentidos). A **Conjetura 7.3** (pág. 36,
propriedade 2) formaliza exatamente essa leitura: "Existe un único
punto x* tal que I_RC(x*)=0" — o que exige I_RC(x)>0 para todo x≠x*,
incluindo x<x*. A **Conjetura 7.5** (pág. 38) fornece a fórmula que
sustentaria essa leitura: I_RC(x)=sup_{t∈ℝ}{tx−Λ(t)}, com Λ(t)=lim(1/k)log E[e^{tL_k}]
— um sup **irrestrito** sobre todo t real, exatamente a transformada de
Legendre-Fenchel clássica e **bilateral**, que para uma Λ estritamente
convexa tem de fato um único zero (no ponto onde Λ'(t)=x, uma bijeção)
— ou seja, Figura 1, Conjetura 7.3 e Conjetura 7.5 são as três
**mutuamente consistentes** entre si: todas descrevem o mesmo objeto
clássico bilateral.

É esse trio, tomado em conjunto, que contradiz a Proposición 3.4: uma
função monótona não-decrescente com I_RC(x*)=0 e I_RC≥0 em toda parte
exige I_RC(x)=0 para **todo** x≤x*, não apenas no ponto x* — o que
contradiz diretamente a "unicidade do zero" da Conjetura 7.3.

**A condição que faz a contradição ser rigorosa, não apenas
sugestiva**: a Proposición 3.4 é condicional — só se aplica em pontos
onde o limite que define I_RC de fato existe. Por isso as partes (2) e
(3) abaixo não são só "confirmação extra": elas estabelecem que o
limite **existe** (e vale 0) para x<x*, o que é exatamente a hipótese
que falta para poder invocar a Proposición 3.4 nesses pontos e fechar
o argumento.

Confirmamos de três formas independentes (`experiments/E-056-ruiz-castillo-large-deviations-check/`):

1. **Analiticamente**: a fórmula PADRÃO da teoria de grandes desvios
   para eventos de cauda unilateral, I_RC(x)=sup_{t≥0}{tx−Λ(t)}
   (Dembo-Zeitouni, cap. 2) — a mesma restrição de sinal usada
   implicitamente (só para o caso x=0) na demonstração, essa sim já
   provada, do Teorema 5.2 (escolha de t>0 via Markov, pág. 29-31) —
   dá I_RC(x)=0 para todo x<x*, coincidindo com a versão irrestrita
   (Conjetura 7.5 como realmente escrita) só para x≥x*.
2. **Monte Carlo**: simulando somas de k valuações Geométrica(1/2) iid,
   para x=−0.6 (<x*), P(L_k/k≥x) **sobe** de 0.667 (k=10) para 0.99996
   (k=1000) conforme k cresce — o evento fica cada vez MENOS raro, não
   mais, e −log(P)/k→0.
3. **Exato para k pequeno**: distribuição Binomial Negativa fechada via
   `Fraction` (sem ponto flutuante perto do limiar irracional
   k·log₂3−x·k — lição já vista e corrigida em H-050/H-052) para a
   soma de k Geométricas(1/2), mesmo padrão crescente (k=5→40:
   0.623→0.804).

O mecanismo do erro: confundir a função de tasa de Cramér **clássica e
bilateral** (sup irrestrito, correta para eventos de desvio genéricos
ou para a cauda oposta) com a função de tasa **real do evento de cauda
unilateral** {L_k/k≥x} que a Definición 3.1 realmente define (e que só
coincide com a bilateral no lado x≥x*). Conferido diretamente contra o
PDF original: o paper contém as duas ocorrências da versão bilateral
(Conjetura 7.3 e Conjetura 7.5) mutuamente consistentes entre si, e
nenhuma versão geral explícita da fórmula unilateral correta — essa só
aparece implícita, restrita ao caso particular x=0, na demonstração já
provada do Teorema 5.2. Tudo sugere que a Seção 7 (inteiramente
conjectural) generalizou a intuição "livro-texto" da forma em V da
função de Cramér para todo x sem preservar a restrição de sinal que
tornava o Teorema 5.2 correto, e sem verificar o resultado contra a
Proposición 3.4 já demonstrada 17 páginas antes.

## Por que isso NÃO é uma alegação de prova, nem um erro de cálculo

- **Não é sobre a Conjectura de Collatz**: o paper nega explicitamente
  provar Collatz, duas vezes (pág. 41, 42).
- **Não é um erro de cálculo isolado**: as Seções 1-5 (identidades
  concretas, Teorema 4.7, Teorema 5.2) são inteiramente corretas e
  verificadas independentemente, símbolo a símbolo.
- **É uma conjectura (Seção 7, nunca rotulada "Teorema"/"Proposición")
  inconsistente com uma proposição já demonstrada no mesmo texto**
  (Proposición 3.4, Seção 3) — mesma categoria geral de erro
  "enunciado-vs-resultado-já-estabelecido" do item 013/H-053, mas aqui
  entre duas partes conjectural/provada do texto, não enunciado vs.
  própria demonstração.
- **Erro contido**: a Seção 8 (Conclusión, pág. 39-42) não depende da
  forma específica de I_RC — só reafirma o programa de pesquisa geral
  e repete o disclaimer de honestidade. Nada posterior à Seção 7 se
  apoia na propriedade "zero único" que está errada.

## Nota de integridade (dupla, pesos diferentes)

1. **Verificado diretamente contra a fonte primária (alta confiança)**:
   um rascunho anterior desta mesma análise, escrito antes desta etapa
   de checagem, caracterizava a Conjetura 7.5 como já contendo a
   restrição de sinal correta (t≥0) — tratando-a, incorretamente, como
   "a correção que o próprio paper oferece" para a Conjetura 7.3.
   Conferimos a pág. 38 diretamente contra o PDF baixado do Zenodo (não
   de memória) e a Conjetura 7.5, como escrita, é **irrestrita**
   (sup_{t∈ℝ}) — portanto parte do mesmo erro, não uma correção dele.
   O achado central (Proposición 3.4 vs. Conjetura 7.3/Figura 1) não
   muda; só a atribuição de qual conjectura tem qual fórmula. Corrigido
   no `experiment.py` (docstrings e texto impresso) antes de finalizar.
   Lição geral: reconferir uma caracterização específica de
   fórmula/página contra a fonte primária antes de fechar a análise,
   mesmo quando já rascunhada com detalhe — o mesmo espírito da
   armadilha "nunca reconstruir dados de memória" documentada em
   `protocols/new-experiment.md`, aqui aplicada à leitura de texto, não
   só a dados numéricos.
2. **Relatado, não re-verificado em detalhe (confiança mais baixa)**:
   também nesta sessão foi relatado — por uma etapa anterior do mesmo
   trabalho, antes de uma interrupção — um bug de inversão na ordem de
   unpacking de tupla no código de verificação (`experiment.py`),
   identificado e corrigido antes de qualquer número ser reportado. O
   arquivo nunca foi commitado (sem histórico de git para conferir), e
   não temos como reconstruir com certeza a forma exata do bug — por
   isso registramos apenas o fato relatado (foi pego e corrigido em
   sessão), sem inventar um diff específico que não observamos
   diretamente.

## Novas hipóteses?

Nenhuma. Segundo erro real encontrado nesta série de 7 papers do autor
(o primeiro foi item 013/H-053) — mesmo padrão geral: aparato
matemático de base (Seções 1-5) correto, honestidade epistêmica mantida
(nada rotulado "Teorema" além do que é realmente provado), mas com um
erro real contido numa parte específica e não detectado pelo próprio
autor.

## Atualizações

- 2026-07-14: paper localizado via Zenodo (ResearchGate bloqueava
  download), lido por completo (44 páginas), identidades algébricas e
  modelo probabilístico ideal confirmados computacionalmente
  (`experiments/E-056-ruiz-castillo-large-deviations-check/`). Achado
  central (Conjetura 7.3/Figura 1/Conjetura 7.5 vs. Proposición 3.4)
  confirmado por três métodos independentes. Flags atualizadas em
  `literature/papers/INDEX.md` (item 026: Lido=Sim, Corrigido=Sim,
  Implementado=Sim).
