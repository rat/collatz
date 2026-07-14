# H-048 — Revisão do paper #006 (Anthony, "A Two-Field Propagation Model for the Collatz Map") — sem erros encontrados

Status: revisão externa concluída — paper elaborado e honesto, todas as
reivindicações testáveis confirmadas corretas
Criada em: 2026-07-14
Origem: paper baixado manualmente pelo diretor científico (item 006 da
coleção, `literature/papers/006_Two-Field-Propagation-Model.pdf`,
Michael Mark Anthony, Enertron Inc., 17 páginas).

## O paper

"A Two-Field Propagation Model for the Collatz Map: A Möbius
Reformulation, Monodromy Structure, and a 2-adic Non-Expansion
Theorem" — Michael Mark Anthony. Paper longo e denso, empilhando bastante
aparato matemático sofisticado: equação P de Riemann (Fuchsiana,
monodromia), grupo PGL(2,C), função digamma, séries hipergeométricas,
24 soluções de Kummer. Propõe um modelo de dois campos vetoriais
contínuos (camada ímpar expansiva, camada par colapsante) cujos "tempos
de voo" específicos recuperam exatamente os passos do Collatz, depois
reformula tudo via a coordenada Φ(n)=1/(n+1) como duas transformações
de Möbius, e traça uma analogia estrutural (não literal) com a
monodromia da equação P de Riemann.

## O que foi verificado (todos confirmados)

- **Reformulação Möbius Φ(n)=1/(n+1)** (Proposição 5.1, Eqs.18-21):
  confirmada em 4999 casos
  (`experiments/E-048-anthony-two-field-propagation-check/`) — as duas
  transformações M_E(φ)=2φ/(1+φ) e M_O(φ)=φ/(3-φ) reproduzem exatamente
  Φ(T(n)) para n par/ímpar respectivamente. Verificado também
  algebricamente à mão (pontos fixos {0,1} e {0,2}, autovalores/
  multiplicadores 2 e 3 das matrizes correspondentes).
- **Teorema 8.1** (regime m=v₂(3n+1)=1 não pode persistir
  indefinidamente): confirmado — maior corrida encontrada até
  n=200.000 foi de 16 passos; a construção explícita do próprio teorema
  (n₀=2^(t+1)-1 sustenta exatamente t passos) confirmada exatamente
  para t=1..10. Prova por indução 2-ádica correta.
- **Exemplo trabalhado da Seção 9** (n=7): trajetória
  7→22→11→...→1 confirmada exatamente.
- **Teoremas 10.3/10.4** (identidade harmônica exata H_q=ψ(q+1)+γ,
  limite de Euler-Mascheroni): confirmados via `mpmath` a 50 dígitos de
  precisão — são fatos padrão e bem conhecidos da função digamma
  (nada específico do Collatz), mas corretamente aplicados aqui.
- **Identidade hipergeométrica da Eq.28**
  (ψ(z)=(z-1)·₃F₂(1,1,2-z;2,2;1)-γ): confirmada numericamente para
  vários valores de z.

**Nenhum erro encontrado** em nenhuma reivindicação testável.

## Por que este paper se destaca (honestidade epistêmica excepcional)

Ao longo de TODO o texto, o paper distingue com extremo cuidado quatro
categorias diferentes de afirmação:

1. **Teorema provado sobre a reformulação** (Teorema 8.1, prova por
   indução 2-ádica; Teoremas 10.3/10.4, fatos padrão da digamma
   corretamente derivados).
2. **Analogia estrutural, não identificação literal** (Proposição 6.1 /
   Remark 6.1: "this is an analogy of form, not of kind" — os
   geradores de Möbius do Collatz são hiperbólicos com multiplicadores
   2 e 3, enquanto a monodromia de uma equação P com expoentes reais é
   elíptica, logo **não podem** ser literalmente a mesma coisa; o
   próprio paper explica exatamente por quê).
3. **Heurístico/condicional, rotulado como tal apesar do nome
   "Teorema"**: o "Collapse Theorem" (14.1) tem Remark 14.1 explicando
   com precisão cirúrgica: "Theorem 14.1 proves convergence of the
   ABSTRACT contraction system... It does NOT prove the Collatz
   conjecture because the connection between the abstract contraction
   factors and the actual Collatz steps requires establishing that
   every orbit stays [bounded]... Theorem 14.1 should be understood
   as: if the orbit stays bounded, then it converges to n=1, which is
   conditional...consistent with, but not a proof of, the conjecture."
   Mesma estrutura lógica ("se limitado, então converge") que
   aparece em várias tentativas de prova malsucedidas na nossa coleção
   — mas aqui, ao contrário delas, o autor identifica corretamente que
   essa condicional NÃO fecha o argumento.
4. **Onde não há extensão de resultados conhecidos**: Seção 12 sobre o
   resultado de Tao (2019/2022): "No claim is made to have proved that
   the exceptional set has Hausdorff dimension zero or that the
   density extends to full Lebesgue measure; these remain open."

Além disso, o próprio autor **identifica e corrige, dentro do texto**,
uma reivindicação anterior equivocada: a Seção 10 abre com "A caution
on an earlier formulation" reconhecendo que uma alegação δ_m=1/m não
se sustenta sob nenhuma definição consistente de densidade, e
substituindo-a pelas versões corretas (Teoremas 10.2-10.4). Isso é
autocorreção genuína, não um erro que tivemos que caçar — sinal forte
de prática de pesquisa cuidadosa.

## Ressalva sobre o aparato decorativo

Boa parte da maquinaria mais vistosa (equação P de Riemann, monodromia,
PGL(2,C), 24 soluções de Kummer) funciona mais como **contexto/analogia
decorativa** do que como conteúdo matemático com peso real sobre a
conjectura — o próprio paper concorda com essa leitura na Seção 16
("Relation to prior work"): "these are structural observations that
complement, rather than compete with, the density-theoretic results
above" e "the contributions of this paper... are structural rather
than density-improving."

## Novas hipóteses?

Nenhuma diretamente aplicável à nossa linha principal. O Teorema 8.1
(nenhuma expansão infinita no regime m=1) é um resultado elementar já
implícito na distribuição geométrica de v₂ (H-001/H-011), apenas
apresentado com uma prova por indução 2-ádica explícita e correta.

## Atualizações

- 2026-07-14: paper lido por completo (17 páginas), reivindicações
  centrais verificadas computacionalmente
  (`experiments/E-048-anthony-two-field-propagation-check/`), nenhum
  erro encontrado. Flags atualizadas em `literature/papers/INDEX.md`
  (item 006: Lido=Sim, Corrigido=Sim [nada a corrigir], Implementado=Sim).
