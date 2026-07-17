# H-110 — Barreira teórica honesta para a exatidão de G~μ: modelo "toy" com liberdade de gauge (existe), mecanismo 2-ádico específico (refutado), e o problema real identificado como endogenia/decorrelação entre folhas

Status: confirmado (lema verificado numericamente) — a peça teórica
mais importante desta linha inteira, resultado de uma terceira
correção do Fable à mesma IA externa
Criada em: 2026-07-17
Origem: uma IA externa, avaliando se a investigação G(v)/μ está madura
para uma nota técnica, recomendou fechar a questão da existência do
limite de escala com uma "barreira teórica" articulada em vez de
deixá-la vaga, sugerindo especificamente: um modelo "toy" onde
"flutuações 2-ádicas maliciosamente construídas" impedem a variância
residual de colapsar a zero. Consultado com pedido explícito de
ceticismo (o Fable já havia corrigido essa mesma IA duas vezes antes,
sobre "expoente de Kesten local" e sobre Furstenberg/Fronteira de
Martin).

## Resposta 1 — o "toy" existe, mas por um mecanismo diferente do proposto

A recursão limite G(v) = Σ_a 3·2^{-a}·G(w_a) é **linear** em G, o que
lhe dá "liberdade de gauge": se W é a solução "endógena" (mensurável
nos dígitos 3-ádicos — a que nossos dados descrevem) e Y é qualquer
função positiva limitada satisfazendo uma condição de harmonicidade
(em particular, qualquer Y invariante ao longo da árvore), então
X = W·Y é **outra solução exata da mesma recursão**.

**Construção explícita**: um espaço-produto ℤ₃*×𝒴 onde a dinâmica age
nos dígitos 3-ádicos exatamente como na árvore de Collatz, mas passa
uma coordenada auxiliar y **inalterada** a todos os filhos.
X(r,y)=W(r)·Y(y), com Y limitada e não-constante, satisfaz:
- **Mesma equação de pressão exatamente** (mesmos pesos, mesma matriz
  M(α), mesmas raízes α=1 e α*=2 — H-104/H-109).
- **Mesma cauda** (índice 2 — Hill e EVT dariam os mesmos números de
  H-104/H-108).
- **Mesma regressão contra μ** (slope b≈1, com dispersão extra fixa).
- **Mas**: Var[log X | m dígitos 3-ádicos] → Var[log Y] > 0 para
  **todo** m, inclusive m=∞. A variância residual nunca colapsa.

**Consequência importante**: nenhuma estatística medida nesta linha
inteira (pressão, α*=2, Hill, EVT, gap de Jensen, slope b) distingue
W de W·Y. O resíduo de ~0,12 dex em M=14 (H-091 Parte 2) é exatamente
a assinatura que um fator de gauge com σ_Y≤0,12 dex deixaria. Os
experimentos de pares casados (H-101) e ANOVA (H-107) são,
retrospectivamente, **cotas superiores decrescentes sobre σ_Y** — e
nenhuma teoria baseada só na recursão pode empurrar essa cota até
zero. O nome técnico é **endogenia** (Aldous–Bandyopadhyay 2005): o
colapso da variância condicional é equivalente a X ser mensurável na
σ-álgebra dos dígitos ("endógena"); o toy é uma solução não-endógena.
Literatura estabelecida, não invenção do Fable.

**Ressalva honesta necessária**: o toy prova "a recursão sozinha não
implica exatidão" — mas não prova que um Y não-trivial plausível
exista de fato para Collatz (no toy, Y é injetado à mão como fator de
produto; para Collatz teria que ser fabricado a partir do próprio
inteiro v). As duas afirmações devem ficar sempre separadas.

## Resposta 2 — o mecanismo específico proposto ("conspiração 2-ádica") está refutado

**Lema (verificado nesta sessão, numericamente, para a=1 a 10, 500+
valores de v cada)**: 3·w_a = 2^a·v − 1 ⟹ 3·w_a ≡ −1 (mod 2^a) ⟹
**w_a ≡ −3⁻¹ (mod 2^a), independente de v**. Os bits baixos do filho
são constantes universais do ramo, não dependem da raiz. Por indução,
um descendente ao fim de um caminho com soma de expoentes A tem seus
A bits mais baixos determinados **só pelo caminho**, com zero
informação sobre a raiz — **a árvore reversa destrói informação
2-ádica sobre a raiz a cada geração**. Não existe coordenada 2-ádica
persistente para "conspirar" com o resíduo 3-ádico, como a IA externa
propôs. Verificação numérica confirmou exatamente a constante prevista
em todos os casos testados (ex: a=5 → w_a≡21 mod32 sempre; a=10 →
w_a≡341 mod1024 sempre).

As coordenadas de gauge que **sobrevivem** de fato são outras: (i) a
fase arquimediana (log v mod 1, transladada por a·log2−log3 a cada
passo) e (ii) correlações entre subárvores (todas as folhas são
funções determinísticas do mesmo v).

## Resposta 3 — a formulação precisa da barreira real

- **Recursão sozinha**: não força colapso (toy acima).
- **Recursão + independência entre subárvores + média finita**:
  força colapso, por dois mecanismos estabelecidos: (a) classificação
  de pontos fixos de smoothing transforms (Durrett–Liggett 1983;
  Alsmeyer–Biggins–Meiners 2012) — soluções não-endógenas de
  distribuição têm cauda de índice 1 e média infinita, **já excluídas
  pelos nossos próprios dados** (α*=2 medido por três vias
  independentes); (b) para a fase arquimediana, teoremas tipo
  Choquet–Deny (funções harmônicas limitadas de passeios aleatórios em
  grupos abelianos são constantes) eliminam qualquer gauge
  arquimediano **no modelo probabilístico completo**.

**Conclusão refinada**: no mundo probabilístico idealizado, a
exatidão É forçada — não há barreira estrutural adicional ali. O que
não segue é que o objeto **aritmético** real (onde as folhas da
árvore-prefixo são todas funções determinísticas de um único inteiro
v) satisfaça a hipótese de independência do modelo — "os dígitos
3-ádicos frescos das folhas se comportam como independentes entre
subárvores" é uma afirmação aritmética **não provada**, não uma
propriedade automática.

## Enunciado da barreira (para uso honesto em qualquer texto futuro)

> Qualquer argumento que use apenas (i) a recursão exata de pesos da
> árvore reversa e (ii) estatísticas dos dígitos 3-ádicos fatora
> através do modelo de smoothing transform — que admite soluções
> não-endógenas (fatores de gauge harmônicos) com variância residual
> condicional positiva em toda resolução, indistinguíveis da solução
> endógena por pressão, cauda, ou qualquer marginal testada. O
> ingrediente que fecha o gap no modelo — e que resta transferir para
> a aritmética — é a quase-independência, entre subárvores, dos
> dígitos 3-ádicos frescos dos inteiros-folha, junto com
> equidistribuição da fase arquimediana ao longo dos caminhos. O
> análogo rigoroso conhecido, na direção forward, é o decaimento de
> Fourier das variáveis de Syracuse de Tao (2022); a versão
> árvore-reversa/densidade permanece aberta e não é implicada por ele.

**Correção ao rótulo da IA externa** ("independência espectral entre
bases 2 e 3"): impreciso em dois pontos — (a) não é sobre dígitos
2-ádicos de v, que dissipam completamente pelo lema acima; (b) a
metade "espectral" já está resolvida (é a equação de pressão em forma
fechada, H-109) — o que falta é decorrelação entre folhas, não
espectro.

## Reabilitação parcial da sugestão anterior de Fronteira de Martin (H-109)

O Fable revisou seu próprio veredito anterior sobre a Fronteira de
Martin (descartada em H-109 como "empréstimo de prestígio"): o espaço
de fatores de gauge É exatamente o espaço de funções harmônicas
limitadas relativo ao fator 3-ádico (a fronteira de Poisson relativa)
— a intuição tinha um núcleo real, ao contrário de Furstenberg/Kesten
(as outras duas correções), onde não havia núcleo salvável. O
descarte como *direção de pesquisa* se mantém (a versão-modelo já está
resolvida por Choquet–Deny; a versão aritmética é só o problema difícil
reenunciado), mas isso é registrado como um caso de autocorreção
honesta do próprio consultor, não uma inconsistência.

## O que pode ser afirmado com rigor de nota técnica (vs. o que fica condicional)

**Afirmável com rigor**: o teorema-toy (prova curta, a linearidade faz
todo o trabalho); o lema 2-ádico (duas linhas, verificado
numericamente nesta sessão); a interpretação dos experimentos H-101/
H-107 como cotas superiores decrescentes sobre σ_Y (o desvio-padrão do
fator de gauge).

**Afirmável só condicionalmente, com flag explícito**: que "recursão +
independência força colapso" via a classificação de smoothing
transforms multitipo/Markov-modulada — o esqueleto é literatura
padrão, mas o Fable não verificou as hipóteses exatas dos teoremas
publicados contra nosso setup específico; deveria ser formulado como
"segue da maquinaria padrão sob [hipóteses], verificação detalhada
pendente", não como teorema próprio sem essa checagem.

**Nunca afirmar**: que σ_Y=0 para Collatz (não sabemos); que a
barreira "explica" por que Collatz é difícil em geral (delimita só
esta linha específica, (S) dado (E), nada mais).

## Avaliação geral

Esta consulta produziu o resultado teórico mais rigoroso e honesto de
toda a investigação: transforma "não sabemos se converge a zero" em
uma barreira matemática articulada e defensável, com um mecanismo
específico proposto pela IA externa corretamente refutado (terceira
vez que isso acontece nesta linha — depois de Kesten e Furstenberg/
Martin), mas com reconhecimento explícito de que, desta vez, havia um
núcleo de intuição real que só precisava de correção, não descarte
total.

## Nota de novidade (2026-07-17, ver H-112)

Checagem de literatura encontrou um precedente direto para o
"ingrediente que falta" (decorrelação/quase-independência aritmética):
Wirsching (1998), Capítulo V, prova densidade positiva uniforme
CONDICIONALMENTE a uma "Weak Covering Conjecture for Mixed Power Sums"
(3.9) — estruturalmente idêntica à nossa barreira (recursão +
equidistribuição/cobertura aritmética não provada ⟹ densidade
positiva), sobre o mesmo tipo de objeto (somas mistas de potências de 2
e 3 mod 3^ℓ). Não há evidência de que essa conjectura tenha sido
resolvida desde 1998. Leitura honesta: o "ingrediente que falta" pode
ser o MESMO problema em aberto há quase 30 anos, articulado de forma
diferente (endogenia/smoothing transforms, mais moderno e conectado a
Tao 2022, vs. combinatória direta de Wirsching) — não uma barreira
nunca vista antes. Ver H-112 para a análise completa.

## Adendo (2026-07-17, ver H-124): a rota de Tao (2020) evita a decorrelação mas bate na mesma parede

Busca literária encontrou que Tao propôs (post de blog, jan/2020) uma
rota condicional para densidade de Collatz que EVITA a decomposição
endogenia/decorrelação bivariada daqui: substitui "quase-independência
entre subárvores" por "separação determinística de pré-imagens (fácil)
+ controle L^∞ marginal (conjectura β=1, onde mora toda a
dificuldade)". Responde a pergunta implícita desta hipótese ("existe
rota que dispense a decorrelação?"): sim, existe, e ela bate na MESMA
parede em forma marginal. Três articulações quase-equivalentes do
mesmo ingrediente faltante: endogenia (aqui), Weak Covering Conjecture
(H-112), β=1 (H-124) — nenhuma provada. Ver H-124 para a análise
completa.

## Referências

- H-091 (Parte 2) — decomposição (E)+(P)+(S), motivação original.
- H-104/H-108/H-109 — α*=2 e sua generalização, usados aqui para
  excluir a classe de soluções não-endógenas de índice 1.
- H-101/H-107 — reinterpretados como cotas superiores sobre σ_Y.
- H-112 — checagem de novidade completa, incluindo a conjectura de
  cobertura de Wirsching (1998) como precedente direto.
- Literatura citada pelo Fable (não lida nesta sessão, candidata a
  checagem futura): Aldous & Bandyopadhyay (2005, endogenia);
  Durrett & Liggett (1983) e Alsmeyer, Biggins & Meiners (2012)
  (classificação de smoothing transforms); teoremas tipo Choquet–Deny.
