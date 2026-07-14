# H-053 — Revisão do paper #013 (Ruiz Castillo, "Operador de Transferencia Residual") — Proposición 5.3 é falsa, contradita pela própria demonstração

Status: revisão externa concluída — **primeiro erro real** encontrado
nos quatro papers Ruiz Castillo revisados até agora; inconsistência
enunciado-vs-demonstração contida na Seção 5, sem impacto no restante
do paper
Criada em: 2026-07-14
Origem: paper baixado manualmente pelo diretor científico (item 013 da
coleção, `literature/papers/013_Operador-Transferencia-Ruiz-Castillo.pdf`,
Juan Carlos Ruiz Castillo, 47 páginas).

## O paper

"Operador de Transferencia Residual de Ruiz Castillo y teoría
espectral para la dinámica acelerada de la Conjetura de Collatz" —
quarto paper deste autor revisado na coleção (após item 001/H-039,
item 008/H-050, item 010/H-052). Introduz um operador de transferência
formal L_t sobre o espaço simbólico completo (sem restrições
aritméticas de Collatz), com potencial φ(m,a₀,a₁,...) = m − log₂(3).
A partir daí, motiva conjecturalmente uma versão restrita L_{RC,t}
sobre o espaço realizável Σ_C, usando teoria espectral clássica
(fórmula de Gelfand, Perron-Frobenius, brecha espectral) para formular
três conjecturas explícitas: Conjetura 6.6 (Princípio Variacional
Espectral), Conjetura 7.1 (Perron-Frobenius Residual), Conjetura 8.4
(Brecha Espectral Residual). Não alega provar Collatz — conclusão
explícita: "los resultados obtenidos no constituyen una demostración
de la Conjetura de Collatz."

## Achado central: Proposición 5.3 é falsa conforme impressa

**Proposición 5.3 afirma**: lim_{t→∞} L_t(1) = 0.

**A própria "Demostración"** parte da fórmula fechada de Proposición
5.1, L_t(1) = e^{t·log₂3}·e^{-t}/(1−e^{-t}), reescreve como
e^{-t(1−log₂3)}/(1−e^{-t}) = e^{(log₂3−1)t}/(1−e^{-t}), e observa
CORRETAMENTE: "Como log₂(3)≈1,58496, resulta 1−log₂(3)<0... la
cantidad anterior crece exponencialmente cuando t→∞. Por ello, la
normalización mediante la presión residual será indispensable para
compensar este crecimiento." O símbolo de fim de demonstração (□)
aparece imediatamente depois — sem que o enunciado "= 0" seja
corrigido ou retirado.

Verificamos numericamente (`experiments/E-053-ruiz-castillo-transfer-operator-check/`):
L_t(1) cresce de 2,84 (t=1) a 6,4×10⁵⁰ (t=200), estritamente crescente
em toda a faixa testada — o oposto exato de "→0".

## Caracterização exata do erro (via `advisor()`)

Consultamos `advisor()` antes de finalizar este achado, dado que é o
primeiro erro real nesta série de papers (diferente do padrão
"elementar mas correto" de H-039/H-050/H-052). Avaliação confirmada:

- O cálculo está correto e a Proposición 5.3, como impressa, é
  de fato falsa (log₂3−1>0 garante divergência para t>0; t=0⁺ também
  diverge pelo denominador →0⁺; t<0 está fora do domínio de
  convergência exigido pela Proposición 4.2).
- **A demonstração do próprio paper deriva o comportamento assintótico
  correto** (crescimento exponencial) e o autor claramente entendeu
  isso — usa a observação para justificar a necessidade de
  normalização futura via "presión residual" (Seção 6 em diante).
- O defeito é que o **enunciado formal em caixa nunca foi atualizado**
  para refletir a própria demonstração — uma inconsistência
  enunciado-vs-demonstração, **não** um erro de cálculo do autor.
- Mesma categoria do erro de rotulagem já encontrado em Pratiher
  (H-037: números corretos, forma/rótulo errado) — por isso **não**
  vai para `literature/unverified-proof-claims.md` (nenhum dos dois
  papers alega provar Collatz; ambos são erros de rotulagem/enunciado,
  não tentativas de prova completa falhas como Halemane/H-043 ou
  Mohammed/H-045).

## Contenção do erro

Confirmado que a Proposición 5.3 pertence à Seção 5, um cálculo
preliminar/pedagógico sobre o espaço simbólico **irrestrito**. Nenhum
resultado posterior (Seções 6-8, sobre o operador **restrito**
L_{RC,t} em Σ_C, todas explicitamente conjecturais) cita ou depende do
valor numérico de L_t(1). O erro não compromete o restante da
arquitetura teórica do paper.

## O que mais foi verificado (confirmado correto)

- **Proposición 4.1** (forma explícita do operador via preimagens do
  shift): reescrita direta da definição, correta.
- **Proposición 4.2** (convergência absoluta da série para t>0,
  |f|≤M): comparação padrão com série geométrica, correta; confirmada
  numericamente (diferença entre somas truncadas em 1000/2000 termos
  ≈0).
- **Proposición 5.1** (fórmula fechada de L_t(1)): confirmada — soma
  direta da série bate com a fórmula fechada.
- **Proposición 5.2** (positividade L_t(1)>0 para t>0): confirmada.
- **Fórmula de Gelfand, positividade/equivalência logarítmica do raio
  espectral** (Proposições 6.2, 6.4, 6.5): análise funcional padrão,
  corretamente aplicada (lema de Fekete, subaditividade) — não é
  Collatz-específico, não exige verificação numérica própria.
- **Conjeturas 6.6, 7.1, 8.4**: honestamente rotuladas como
  conjecturas (não teoremas), consistente com o padrão de honestidade
  parcial já visto em H-039/H-050/H-052.

## Caráter do paper — quebra o padrão "elementar mas correto" dos 3 anteriores

Este é o **primeiro erro real** encontrado nos quatro papers Ruiz
Castillo revisados até agora. Os três anteriores (H-039, H-050,
H-052) eram todos matematicamente corretos em tudo verificado, apesar
de elementares e sem verificação numérica própria. Este paper mantém o
padrão de honestidade quanto ao alcance geral (conjecturas rotuladas
como tal, conclusão explícita de não-prova), mas contém um enunciado
formal genuinamente falso — o que sugere que a produção rápida desta
série de ~19 papers (todos autocitados) não inclui uma revisão
cuidadosa de coerência interna entre enunciados e demonstrações.

## Novas hipóteses?

Nenhuma. O erro encontrado é de rotulagem/consistência textual, não
abre uma nova linha de investigação matemática sobre Collatz.

## Atualizações

- 2026-07-14: paper lido por completo (47 páginas), proposições
  centrais verificadas computacionalmente
  (`experiments/E-053-ruiz-castillo-transfer-operator-check/`).
  Encontrada Proposición 5.3 falsa conforme impressa (contradita pela
  própria demonstração) — `advisor()` consultado antes de finalizar,
  confirmando a caracterização exata (inconsistência
  enunciado-vs-demonstração, não erro de cálculo; contido, sem impacto
  em resultados posteriores). Flags atualizadas em
  `literature/papers/INDEX.md` (item 013: Lido=Sim, Corrigido=Sim
  [erro documentado, não há como "corrigir" o paper original],
  Implementado=Sim).
