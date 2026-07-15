# H-039 — Revisão crítica do paper #001 ("Geometría Residual de Ruiz Castillo") + cálculo explícito que o paper nunca faz

Status: revisão externa concluída (correções documentadas e depois
confirmadas/refinadas contra o PDF completo, não só a leitura via
navegador); extensão computacional própria confirmada e verificada
Criada em: 2026-07-14
Origem: primeiro paper da coleção `literature/papers/INDEX.md`
(item 001), pedido explícito do diretor científico: "vamos ler e
corrigir o primeiro e procurar novas hipóteses nele".

## O paper

"Geometría Residual de Ruiz Castillo para la dinámica acelerada de la
Conjetura de Collatz" — Juan Carlos Ruiz Castillo (ScD., Universidad de
San Carlos de Guatemala), 2026, DOI 10.5281/zenodo.21271452, 39
páginas. Lido originalmente inteiramente via navegador (ResearchGate
bloqueava download automatizado); PDF baixado manualmente pelo diretor
científico em 2026-07-15 e arquivado em
`literature/papers/001_Geometria-Residual-Ruiz-Castillo.pdf`. É a
"segunda etapa" de uma
série de ~20 papers do mesmo autor (todos catalogados na coleção),
propondo construir uma "geometria" (métrica, curvatura, comprimento)
sobre o formalismo termodinâmico residual das etapas anteriores.

## Avaliação matemática geral

A maquinaria usada é **teoria de formalismo termodinâmico clássica e
correta** (Ruelle/Bowen/Ellis): pressão como sup de entropia menos um
funcional linear sobre medidas invariantes, métrica de Fisher como
segunda derivada da pressão, relação metric=variância assintótica de
somas de Birkhoff. Nada disso está matematicamente errado — é
maquinaria padrão de teoria ergódica/grandes desvios, aplicada
(honestamente, sem alegar provar Collatz) ao observável de dissipação
2-ádica do Collatz. O autor inclusive identifica corretamente, por
conta própria, que o espaço de parâmetros é 1-dimensional e que a
curvatura riemanniana clássica seria trivial ali — e define
explicitamente uma noção alternativa de "curvatura" para contornar
isso, com a ressalva clara de que não é a curvatura riemanniana
padrão. Isso é bom rigor.

## Correções e problemas encontrados

1. **Repetição excessiva do mesmo fato trivial como resultado maior**
   (confirmado e ampliado após leitura direta do PDF completo, que
   permitiu contagem exata): "convexa ⟹ segunda derivada ≥ 0" (fato de
   cálculo de primeiro semestre) é apresentado formalmente **pelo menos
   cinco vezes** como resultado nomeado independente: Proposição 1.3
   ("Não negatividade formal da métrica residual", p.4), Corolário 2.6
   ("Não negatividade da segunda derivada", p.10 — decorre trivialmente
   da Proposição 2.5 já provada duas páginas antes), Teorema 3.2
   ("Positividade da métrica residual", p.14, que apenas acrescenta a
   cláusula de estrita positividade), e a Seção 4.4 ("Consequência
   imediata", p.19, que re-deriva `g_RC≥0` — já estabelecido *sem*
   condições pelo Teorema 3.2 — de forma *condicional* à Conjetura 4.1,
   tornando essa derivação estritamente redundante). Cada instância tem
   uma "demonstração" que é, literalmente, a definição de convexidade
   reescrita. Além disso, o paper contém **dez quadros coloridos**
   ("Idea central del artículo" p.5, "Idea fundamental" p.8, "Conclusión
   estructural" p.11, "Interpretación geométrica" pp.16,25,34, "Lectura
   probabilística" p.20, "Lectura dinámica" p.29, "Aporte central del
   trabajo" p.37, entre outros) que redesenham repetidamente a mesma
   cadeia conceitual (Presión→Métrica→Curvatura→...→Rigidez), cada um
   acrescentando apenas um elo à cadeia do quadro anterior — um padrão
   de apresentação fortemente repetitivo/padded ao longo de 39 páginas.

2. **Tensão de tom retórico entre o texto formal e os quadros
   ilustrativos** (ponto corrigido/refinado após leitura direta — a
   caracterização original, feita via navegador, estava imprecisa
   quanto à localização exata do problema): a identidade central
   `g_RC(t) = σ²_RC(t)` **é**, na verdade, rotulada corretamente como
   `Conjetura 4.1` já na sua primeira introdução formal (Seção 4.3,
   p.19, com quatro hipóteses explícitas listadas) — não apenas
   admitida tardiamente na Conclusão, como uma leitura anterior menos
   cuidadosa sugeriu. O padrão real é mais sutil: toda vez que a
   identidade aparece dentro de um **quadro colorido** de "leitura"/
   "interpretação" (ex: p.19-20 "Lectura probabilística", que afirma
   secamente "Por ello, métrica residual = varianza residual =
   intensidad de las fluctuaciones", sem qualificação), o tom é mais
   assertivo e categórico do que nos enunciados formais correspondentes
   (`Conjetura`, `Si además se verifica...`), que são consistentemente
   bem qualificados. Ou seja: o aparato formal (Definição/Conjetura/
   Proposição) é epistemicamente honesto do início ao fim; é a prosa
   decorativa ao redor dele que soa mais categórica do que o formalismo
   que resume — uma inconsistência estilística menor, não uma alegação
   de prova disfarçada.

3. **Nenhum conteúdo numérico ou empírico**: as duas únicas figuras do
   paper (Figura 1, Seção 7, p.30; Figura 2, Seção 8, p.31) são
   explicitamente rotuladas pelo próprio autor como "**conceptual**"/
   "**Visualización conceptual**" nas legendas — funções ilustrativas
   arbitrárias (confirmado: os eixos dizem "Valor conceptual"), não
   P_RC(t) calculada para o problema real. Em nenhum lugar das 39
   páginas o autor calcula qualquer quantidade numericamente para a
   dinâmica real do Collatz. Tudo fica em nível de "SE P_RC tiver a
   propriedade X, ENTÃO g_RC tem a propriedade Y" — nunca "P_RC(t) É
   [fórmula explícita]".

4. **Referências: 100% autocitação**. As 13 referências são **todas**
   "Ruiz Castillo, J.C." (2025-2026), majoritariamente depósitos Zenodo
   sem peer review (alguns títulos duplicados em espanhol/inglês,
   contados separadamente). **Zero citações** à literatura estabelecida
   do Collatz (Lagarias, Tao, Terras, Wirsching, Kontorovich-Lagarias,
   Barina) e **zero citações** à literatura clássica de formalismo
   termodinâmico/grandes desvios (Ruelle, Bowen, Ellis, Dembo-Zeitouni)
   cuja maquinaria padrão está sendo usada em todo o artigo, apenas
   rebatizada com a marca pessoal "Ruiz Castillo" em cada conceito
   (pressão, métrica, curvatura, entropia, medidas de Gibbs...).

5. **A "conjectura" central não é, em geral, um mistério matemático
   aberto**: no modelo i.i.d. (que é exatamente o modelo padrão que
   ESTE PROJETO já usa — a=v₂(3n+1) ~ Geométrica(1/2) i.i.d., H-001),
   a identidade "métrica = variância assintótica sob a medida
   tilted" é um **fato padrão e demonstrável** da teoria de família
   exponencial/grandes desvios (Ellis 1985; Dembo-Zeitouni, cap. 2),
   não uma conjectura aberta. A parte genuinamente incerta não é a
   identidade abstrata — é se ela se estende à dinâmica real do
   Collatz, que não é exatamente i.i.d. (correlações entre valuações
   sucessivas ao longo de uma órbita real). O paper não faz essa
   distinção, o que torna sua "conjectura" mais forte do que precisa
   ser.

## Extensão computacional própria (o que o paper deveria ter calculado)

Usando o modelo i.i.d. padrão deste projeto (a~Geométrica(1/2), já
usado em H-001/H-011), calculei explicitamente P_RC(t) [≡Λ(t), a
função geradora de cumulantes de φ(a)=a-log₂(3)] via
`experiments/E-039-ruiz-castillo-explicit-pressure/experiment.py`
(sympy, verificado):

```
Λ(t) = t(1-log₂3) - log(2-eᵗ),   domínio t < log(2)
```

**Verificação cruzada** (confirma a fórmula bate com constantes já
estabelecidas neste projeto, sem depender de nada do paper): Λ'(0) =
2-log₂3 ≈ 0,415 (= E[a]-log₂3) e Λ''(0) = 2 (= Var[a], H-001/H-011) —
batem exatamente.

**Resultado novo**: g_RC(t)=Λ''(t)=2eᵗ/(2-eᵗ)² é estritamente positiva
e convexa em todo o domínio natural (confirma, para o modelo i.i.d., a
hipótese que o paper apenas assume formalmente) — **mas diverge
(g_RC(t)→∞) quando t→log(2)⁻**, exatamente no ponto onde a função
geradora de momentos da Geométrica(1/2) deixa de convergir. Isso é uma
singularidade real e quantificável, consequência direta do "2" na
distribuição da valuação 2-ádica — algo que o paper nunca menciona
porque nunca calcula P_RC(t) explicitamente.

Além disso, K_RC(t) = -2·g_RC(t) exatamente neste modelo (relação
fechada específica) — **sempre estritamente negativa**, nunca zero,
divergindo para -∞ no mesmo ponto. Isso contradiz o desenho conceitual
em forma de U do paper (Seção 7) — mas, crucialmente, sem
contradizê-lo de fato, já que o próprio autor rotulou aquele desenho
como ilustrativo/arbitrário, não como o cálculo real.

## Novas hipóteses? Avaliação honesta

O cálculo acima é uma extensão honesta e verificada, mas **não abre
uma nova linha de ataque à conjectura**: é um preenchimento de lacuna
(calcular o que o paper deixou abstrato) usando exatamente o modelo
i.i.d. padrão que já sabemos ser apenas uma heurística (órbitas reais
de Collatz não são i.i.d. — é por isso que a conjectura continua
aberta). A singularidade em t=log(2) é uma curiosidade matemática limpa
e poderia, em princípio, se conectar a estatística de valores extremos
(órbitas com sequências incomumente longas de valuações grandes — o
território de H-004/recordistas), mas isso é especulativo e não foi
aprofundado — não vale reivindicar como hipótese nova sem mais
trabalho.

**Conclusão honesta**: nenhuma hipótese genuinamente nova sobre a
conjectura em si emergiu da leitura. O valor real desta revisão é (1)
documentar com precisão os problemas do paper (correção, conforme
pedido), e (2) demonstrar, com um cálculo limpo e verificado, exatamente
o tipo de conteúdo concreto que falta no paper — que é mais útil como
padrão de comparação para os próximos ~19 papers da mesma série (todos
prováveis de ter a mesma lacuna) do que como fonte de hipótese nova.

## Atualizações

- 2026-07-14: paper lido por completo (39 páginas, via navegador),
  correções documentadas, cálculo explícito feito e verificado.
  Flags atualizadas em `literature/papers/INDEX.md` (item 001: Lido=Sim,
  Corrigido=Sim, Implementado=Parcial — cálculo de apoio feito, mas
  sem hipótese nova sobre a conjectura).
- 2026-07-15: PDF baixado manualmente pelo diretor científico e
  arquivado em `literature/papers/001_Geometria-Residual-Ruiz-Castillo.pdf`.
  `INDEX.md` atualizado (Arquivo local e Link).
- 2026-07-15: revisão finalizada — reli o PDF completo (39 páginas)
  diretamente (em vez da leitura via navegador da sessão anterior) para
  confirmar cada correção contra a fonte primária real. Resultado: dois
  ajustes de precisão, nenhuma mudança de veredito. (1) O item "fato
  trivial repetido" estava subcontado — é pelo menos **cinco** vezes
  (faltava o Corolário 2.6, p.10), não quatro, mais **dez** quadros
  coloridos redesenhando a mesma cadeia conceitual ao longo do texto.
  (2) O item "identidade central apresentada de forma inconsistente"
  estava impreciso — a Conjetura 4.1 já é rotulada corretamente desde a
  primeira introdução (Seção 4.3, p.19), não só na Conclusão; o problema
  real é mais sutil (tom retórico mais assertivo nos quadros
  ilustrativos do que no aparato formal, que é honesto do início ao
  fim) — corrigido no texto acima. Os itens 3 (figuras conceituais — na
  verdade duas, não uma) e 4 (100% autocitação, 13/13 referências)
  foram confirmados exatamente como antes. Nenhuma mudança nas flags de
  `INDEX.md` (Lido/Corrigido/Implementado já corretas).
