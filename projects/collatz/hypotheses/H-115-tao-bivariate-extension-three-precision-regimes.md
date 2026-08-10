# H-115 — Por que a extensão bivariada de Tao não cruza a barreira: três regimes de precisão, e onde cada um vive

Status: fechada — obstrução identificada com precisão matemática; os
dois lemas de próximo passo (regime 2, redução Z-number) foram
executados (ver H-126/H-127) e convergem, por vias independentes, no
mesmo ingrediente faltante do regime 3 — problema aberto reconhecido
da área, não mais perseguido
Criada em: 2026-07-17
Origem: depois de fechar o pacote de publicação (H-109 a H-113) e
esgotar 7 rodadas de tentativas de "importar maquinaria de outra área"
(Kesten, Furstenberg, Martin, conspiração 2-ádica, Bourgain-Garaev-
Konyagin, Breiman sem independência, Bilu/Chambert-Loir, Bourgain-
Gamburd — todas refutadas), o diretor científico pediu uma tentativa
séria (não mais uma rodada de consulta) de avaliar a extensão bivariada
de Tao (2022) — a única rota que sobreviveu a todas as rodadas
anteriores como "genuinamente viva". Isso exigiu ler a Seção 7 inteira
da prova de Tao (o mecanismo real, não só o enunciado da Proposição
1.17) e formular uma pergunta precisa ao Fable a partir dessa leitura.

## O que a leitura da Seção 7 revelou

O mecanismo de Tao (caracteres χ_ξ, pares de valuações b_j~Pascal
i.i.d., fase θ(j,l) evoluindo multiplicativamente por log9/log2,
"conjunto preto" = união de triângulos bem separados, processo de
renovação bidimensional com holding time, indução decrescente com
monotonicidade) opera INTEIRAMENTE sobre Syrac(ℤ/3ⁿℤ), definida como
i.i.d. Geom(2)ⁿ **por construção** (equação 1.22 do paper) — não uma
aproximação. A ligação com inteiros reais é feita em outro lugar do
paper (Prop. 1.9: aproximação em variação total, erro exponencial,
válida só para profundidade n≲log(N); Remark 1.10: identidade exata no
limite de Haar 2-ádico).

## A percepção central (formulada nesta sessão, confirmada e aprofundada pelo Fable)

Para o NOSSO problema (árvore reversa, um único v fixo, duas folhas
irmãs w_1(v), w_2(v)), as "duas folhas" NÃO são duas amostras i.i.d. de
um processo — são duas FUNÇÕES DETERMINÍSTICAS DIFERENTES da MESMA
variável v. Isso é qualitativamente diferente do objeto de Tao.

**Achado do Fable, mais forte que a percepção original**: para um PAR
FIXO de caminhos-irmãos (profundidade D), a congruência de existência
(bridge exato de H-111) pina v numa única classe mod 3^D — escrevendo
v=v₀+3^D·t, as duas folhas viram FUNÇÕES AFINS da MESMA variável livre
t, com multiplicadores unitários: w_i = w_i(v₀) + 2^{A_i}·t. Consequência:
o par (w_1,w_2) mod 3^ℓ vive numa RETA de tamanho 3^ℓ dentro de
(ℤ/3^ℓ)² — dependência determinística PERFEITA em TODA precisão ℓ≥1,
com uma reta inteira de frequências ressonantes onde a correlação tem
módulo exatamente 1. **"Aplicar Prop. 1.17 duas vezes + independência
condicional dado o ancestral" não é só circular — é FALSO como
enunciado, em qualquer precisão.** Nenhuma rodada anterior (incluindo a
validação do Fable na rodada 5, que chamou isso de "a melhor ideia da
linha") tinha articulado isso com essa precisão.

## Mas existe uma reformulação correta, não-circular — só que com alcance limitado

A quantidade que realmente importa (decorrelação de AGREGADOS de
subárvore entre irmãs, não folha-a-folha) é um enunciado de SEGUNDO
MOMENTO, que se expande em soma sobre PARES DE CAMINHOS:

> E_v[Z₁·Z₂] ∝ #{(a,a′) : a₁∈B₁, a′₁∈B₂, Syrac(a)≡Syrac(a′) mod 3^D}

e por Fourier, Cov ∝ Σ_{ξ≠0} S₁(ξ)·S₂(ξ)*, com S_i somas de caracteres
tipo-Syracuse condicionadas no primeiro passo. Aqui NÃO há
circularidade — os dois índices de caminho são independentes por
tautologia da expansão do quadrado, não por hipótese aritmética.

## Três regimes de precisão (o resultado central desta hipótese)

1. **ℓ arbitrário, par FIXO de caminhos**: dependência perfeita, sem
   decaimento possível. Decorrelação só pode vir de média sobre
   caminhos, nunca folha-a-folha.
2. **ℓ = O(log D)**: PROVÁVEL, com a maquinaria da Seção 7 quase
   inalterada (orçamento: |ρ(ξ)|≤C_A·D^{-A} controla a soma sobre
   3^ℓ-1 frequências só se 3^ℓ≪D^{2A}, i.e. módulos polinomiais em D).
   Um lema honesto e alcançável, ainda não escrito.
3. **ℓ≍c·D** (onde vivem a barreira de endogenia, os dígitos frescos e
   a Weak Covering Conjecture de Wirsching, H-112/H-114): exigiria
   decaimento de Fourier EXPONENCIAL (power-saving) uniforme em ξ — a
   Prop. 1.17 dá só super-polinomial, e o método da Seção 7
   estruturalmente não dá mais (as perdas dos triângulos pretos estão
   amarradas às propriedades diofantinas de log3/log2 via a inclinação
   log9/log2). **Este regime é equivalente a um problema aberto
   reconhecido da área**: os análogos estruturais honestos identificados
   pelo Fable são (i) correlações de funções digitais (Mauduit-Rivat/
   Fouvry-Mauduit/Spiegelhofer), (ii) rigidez efetiva ×2×3 de
   Furstenberg (o par (w₁,w₂) é v observado por dois elementos do
   semigrupo afim gerado por x↦(2^a·x−1)/3) — aberto na generalidade
   necessária, e (iii) decaimento de Fourier de medidas auto-similares
   (Syrac é uma medida auto-similar 3-ádica; o decaimento exponencial
   pedido é o análogo 3-ádico de resultados tipo Breuillard-Varjú,
   conhecidos só em casos algébricos especiais). Correlações de funções
   multiplicativas (Elliott/MRT) NÃO são o lar certo (nossos funcionais
   são dirigidos por dígitos/valuações, não multiplicativos).

## Veredito final

A validação anterior do Fable ("extensão bivariada = melhor ideia da
linha", rodada 5) permanece correta EM RELAÇÃO às alternativas
(Kesten, Furstenberg-ingênuo, etc.), mas estava mal escopada: era uma
boa ideia para um lema em precisão logarítmica (regime 2), não uma
rota através da barreira (regime 3). A percepção desta sessão é a
correção que faltava articular.

**Recomendação disciplinada (Fable + concordância)**:
1. **Não perseguir mais o regime 3 por analogia** — a resposta já é
   conhecida (território ×2×3-efetivo/Breuillard-Varjú, ferramenta que
   não existe hoje). Sete rodadas + esta análise convergem nisso.
2. **Trabalho empírico continua valendo** (extensão de H-114 a ℓ≥18-20)
   — dado primário sobre o objeto em precisão plena, exatamente o
   regime que a teoria disponível não alcança.
3. **Opcional, com prazo limitado**: escrever o lema do regime 2
   (decorrelação de agregados irmãos em módulos 3^{O(log D)}) — seria
   o primeiro enunciado teórico POSITIVO e não-refutado desta linha
   inteira, risco baixo, valor modesto mas real, companheiro rigoroso
   do ρ_eff≲0,06 empírico (H-111).

## Pacote final desta linha de pesquisa (estado da arte alcançável)

ρ_eff≲0,06 empírico (H-111) + quadro teórico de três regimes de
precisão, com a obstrução do regime 3 identificada com precisão em vez
de deixada vaga (esta hipótese) + dados diretos sobre a WCC de
Wirsching até ℓ=17, regime assintótico indeterminado (H-114) — coerente,
honesto, e defensável como o limite do que esta investigação alcança
sem resolver um problema aberto reconhecido da área.

## Adendo (2026-07-17, ver H-124): forma mínima nomeada do regime 3

Busca literária dirigida encontrou que o próprio Tao (post de blog,
janeiro 2020, "Equidistribution of Syracuse random variables and
density of Collatz preimages") propôs uma conjectura — **β=1**
(c_n:=inf_b P(Syrac(ℤ/3ⁿℤ)=b) = 3^{-n+o(n)}) — que é, após
verificação estrutural, o MESMO objeto algébrico da Weak Covering
Conjecture de Wirsching (H-112/H-114), numa forma um degrau mais fraca
(WCC ⟹ β=1 essencialmente; β=1 sozinho só dá uma WCC enfraquecida).
β=1 é uma barra mais baixa que o power-saving exigido pelo regime 3
aqui descrito, e MESMO ASSIM está aberta há 6 anos, nunca virou paper.
Isso dá ao regime 3 sua testemunha mais limpa possível: em vez de só
"equivalente por analogia a território ×2×3/Breuillard-Varjú", agora
também "sua forma mínima útil é uma conjectura nomeada do próprio Tao,
não provada". Três articulações quase-equivalentes do mesmo
ingrediente faltante: endogenia (H-110), WCC (H-112), β=1 (H-124) —
nenhuma provada. Ver H-124 para a análise completa.

## Próximos passos declarados (2026-07-17) — antes de escrever o paper

Dois lemas concretos, de baixo risco/custo, identificados ao longo
desta hipótese mas ainda não escritos. Marcados como próxima ação
(não mais rodada exploratória — são fechamentos de pontas já
mapeadas):

1. **Lema do regime 2**: decorrelação de agregados de subárvore (não
   folha-a-folha) em módulos grosseiros 3^{O(log D)}, via contagem de
   pares de caminhos + Prop. 1.14 de Tao (condicionada no primeiro
   passo, uniforme em ξ) — maquinaria da Seção 7 quase inalterada.
   Seria o primeiro enunciado teórico POSITIVO e demonstrado (não só
   medido) desta linha inteira.
2. **Lema de redução Z-number** (da análise de Littlewood-Offord de
   Tao 2011, ver adendo acima): formalizar "falha da WCC em escala ℓ
   com j acima do limiar ⟹ concentração de Bohr dos geradores de
   potências de 2 ⟹ configuração tipo Z-number para ×2 mod 3^s" —
   upgrade de "analogia com problema aberto" para "redução explícita
   a problema aberto nomeado".

Ambos "dias, não semanas" segundo o Fable. Fazer os dois antes de
começar a redação do paper — depois disso, parar de investigar.

## Execução dos dois próximos passos (2026-07-17) — ambos concluídos, ambos com resultado diferente do esperado

**Lema do regime 2 → H-126.** Refutado como esboçado: o orçamento
"|ρ(ξ)|≤C_A·D^{-A} uniforme em ξ" contradiz uma identidade EXATA de
Tao (eq. 1.23, auto-similaridade — não uma estimativa perdida). O que
sobrevive é um teorema de estrutura POSITIVO (a componente grosseira
da covariância de irmãs é exata, não-nula, independente de D — Prop.
2 de H-126, endogenia convertida em fórmula fechada) mais um lema
condicional cuja hipótese (K_∞<∞, medida de Syracuse em L²(Z_3)) foi
testada e **refutada computacionalmente** em E-100 (K_ℓ diverge
linearmente até ℓ=17, incrementos convergindo a ≈0,47 sem sinal de
saturação). Regime 2 não é um degrau mais fácil que o regime 3 — é
irmão dele, com o mesmo ingrediente faltante, agora com refutação
direta em vez de "em aberto".

**Lema de redução Z-number → H-127.** Não é a equivalência limpa
esperada — é uma dicotomia condicional (Lema B): falha da WCC +
concentração espectral ⟹ configuração de Bohr pós-wrap (parente de
Erdős-Lagarias-Furstenberg, não do problema clássico de Mahler); o
ramo espectralmente difuso é inacessível a métodos ℓ¹ tipo
Littlewood-Offord, por uma parede de constantes EXATA (Proposição C,
identidade de Jensen Λ=log γ_c≈0,58 contra o necessário log3≈1,10,
folga de fator 1,88, confirmada por Monte Carlo em E-101). O ramo
difuso inacessível é "exatamente o núcleo de β=1" — mesma parede do
regime 3 e da condição L² de H-126, vista por uma quarta via
independente.

**Consequência para o pacote final**: em vez de dois lemas positivos
fechando pontas, o resultado é uma quinta e sexta articulação
independente do MESMO ingrediente faltante (endogenia H-110, WCC
H-112/H-114, β=1 H-124, condição L² H-126, dicotomia espectral H-127)
— nenhuma provada, todas convergindo. Isso é, honestamente, um
resultado mais forte para o paper do que dois lemas soltos teriam
sido: a convergência de cinco/seis formulações independentes no mesmo
ponto é evidência estrutural de que o ingrediente é real e único, não
um artefato de uma abordagem específica. Ver H-126/H-127 para os
teoremas de estrutura positivos que sobrevivem em cada caso (Prop. 2
de H-126; Prop. C de H-127) — ambos citáveis por si mesmos.

**Próximo passo agora**: nenhum lema pendente. Parar de investigar e
começar a escrever o paper (escopo H-109 a H-127, conforme já
decidido).

## Adendo (2026-07-20): checagem da direção reversa da redução do regime 3

Terceira auditoria do paper apontou que "equivalente em dificuldade"
(thm:regime3) não é uma relação matemática definida, e o paper foi
corrigido para uma redução unidirecional precisa ("Regime 3 é ao menos
tão difícil quanto [Spiegelhofer / rigidez de Furstenberg /
Breuillard–Varjú]"). Isso deixou em aberto, explicitamente, se a
implicação reversa vale (o que fecharia uma equivalência de verdade).
Busca literária dirigida (WebSearch) não achou nenhuma redução
conhecida na direção reversa — nem um resultado que derive decaimento
de Fourier exponencial 3-ádico a partir de correlações de dígitos
base 2/3 tipo Spiegelhofer, nem o inverso. Isso é consistente com o
veredito já registrado nesta hipótese há 7 rodadas: "não perseguir
mais o regime 3 por analogia — a resposta já é conhecida (território
sem ferramenta hoje)". A direção reversa permanece genuinamente aberta
— não é uma lacuna de busca bibliográfica, seria trabalho matemático
novo (uma prova de redução de verdade), fora do escopo de uma
auditoria de correção de texto. A reformulação unidirecional do paper
("ao menos tão difícil quanto") é, portanto, a mais forte alegação
defensável no estado atual do conhecimento — não uma perda de rigor,
mas o reflexo exato do que é conhecido.

## Passe dirigido a O4 (2026-08-09): a ponte com O7, e o diagnóstico do obstáculo

Rodada pedida com um objetivo estreito: procurar um ângulo ainda não
tentado para o regime 3 (estrutura de bloco não linear, outra escala de
frequência, ou redução a outra direção em aberto), ou, na falta dele,
escrever o obstáculo com precisão. Não apareceu ângulo novo. Apareceu
uma redução que não estava registrada, e uma medida que explica por que
a hierarquia de escalas da §8 não compra nada.

### Correção de enquadramento sobre H-153 (Regra 8c)

O pedido desta rodada supunha que H-153 já mostrava que "a separação de
blocos falha até em escala linear", e portanto que o obstáculo aparece
antes de `ell≍D`. Isso não é o que H-153 prova. O
`thm:linear-block-nonequivalence` prova não equivalência dos VETORES DE
CUSTO LATENTES em escala linear, e tanto o arquivo da hipótese quanto o
manuscrito (linhas 2078 a 2081 de `main.tex`) dizem explicitamente que
isso NÃO transfere para os resíduos módulo `3^r`: a projeção é
muitos-para-um e pode apagar a estatística suficiente `S_(ell,r)`. H-153
é um resultado de afiação para `thm:sublinear-precision-ensemble`, não
um obstáculo a O4. A razão real pela qual a maquinaria sublinear não
alcança O4 é outra, e é a de (2) abaixo.

### (1) O alvo uniforme de O4 implica a condição L² de O7

Pela identidade de Parseval multiescala de H-155,
`E_r = K_r - K_(r-1)` é a energia primitiva na escala `r`, e há
`2*3^(r-1)` frequências primitivas nessa escala. Suponha o alvo uniforme
que a rota de segundo momento pede, na sua forma pontual:

```text
sup_{3 nao divide xi} |muhat_r(xi)| <= C * 3^(-r(1/2+eps)),  eps>0.
```

Então `E_r <= 2*3^(r-1) * C^2 * 3^(-r(1+2eps)) = (2C^2/3) * 3^(-2eps r)`,
que é somável, logo `K_infinity = 1 + sum_r E_r < infinity`. Isto é a
condição L² de O7 (H-126, H-155, E-100).

Ou seja: O4, na forma pontual uniforme, é ao menos tão forte quanto o
ramo L² de O7. A dependência registrada até aqui era a oposta, em H-126
(um lema de regime 2 que PRECISAVA de `K_infinity<infinity` como
hipótese). A implicação nesta direção não estava escrita. Ela é a mesma
ponte que H-155 usa entre O5 e O7, aplicada a um terceiro item, e
responde à pergunta desta rodada: O4 se conecta a O7, não a O2.

**Escopo: o alvo tem de ser posto por classe de primeiro passo.** O
enunciado acima é sobre `muhat_r`, e o alvo de O4 no paper é sobre as
somas condicionadas `S_i`. A ponte entre os dois é a decomposição de Tao
(eq. 1.22), `mu_r = sum_j 2^(-j) mu_r^(j)`, com pesos positivos somando
1. Se a cota uniforme valer para CADA classe de primeiro passo `j`, a
desigualdade triangular a transporta para qualquer combinação convexa
normalizada dessas classes, o que inclui tanto `S_1` e `S_2` quanto o
próprio `muhat_r`, e a implicação acima vale sem mudança.

Se, em vez disso, o alvo for posto apenas para as duas somas agregadas
`S_1` e `S_2`, a implicação NÃO fica disponível: `B_1` e `B_2` não
esgotam necessariamente os primeiros passos, e cancelamento entre
classes fora de `B_1 uniao B_2` não está excluído. A forma por classe é
a que a rota de segundo momento de fato precisa, já que a expansão do
quadrado percorre pares de índices de caminho e a cota tem de ser
uniforme sobre o condicionamento; mas o ganho registrado aqui é o da
forma por classe, e é nessa forma que ele deve ser citado.

Não é uma equivalência, e o arquivo não deve deixar isso escorregar
(H-135 existe por causa de uma alegação de equivalência anterior).
A recíproca falha: o que a rota de Cauchy-Schwarz de fato consome é
`T_ell(r_ell) = K_ell - K_(r_ell) -> 0` ao longo de sequências
sublineares `r_ell -> infinity`, e essa condição de tipo Cauchy é
estritamente mais fraca que `K_infinity<infinity` (basta tomar
`K_ell = log log ell`, divergente, com `K_ell - K_(sqrt ell) -> 0`).

### (2) Por que "separar os modos de condutor sublinear" não ajuda

O enunciado de O4 no paper embute um passo preparatório: separar os
modos de condutor sublinear, tratados por
`thm:sublinear-precision-ensemble`. Sob a identidade de H-155 esse passo
é mensurável: a parcela da massa l² primitiva que ele remove é
`(K_(r_ell) - 1)/(K_ell - 1)`.

Medido em E-133 (níveis exatos até `ell=15`), com `E_r` perto de 0,47 em
toda a faixa, essa fração vale 0,408 em `(ell,r)=(8,3)`, 0,330 em
`(10,3)`, 0,276 em `(12,3)` e 0,238 em `(14,3)`. Ao longo de qualquer
`r_ell = o(ell)` ela tende a `r_ell/ell -> 0`. O passo preparatório
remove uma fração assintoticamente nula do problema, e o resíduo
`K_ell - K_(r_ell)` cresce linearmente em `ell`.

A dicotomia, que não exige tomar partido sobre a questão em aberto:
se `K_infinity < infinity`, a separação sublinear captura
assintoticamente TODA a massa e a rota de Cauchy-Schwarz fecha sozinha;
se `K_ell ~ c*ell`, a cauda restante diverge linearmente e nenhum
rearranjo de escalas a torna pequena. As duas direções em aberto são a
mesma direção em aberto.

### (3) A medida do espectro primitivo, e o que ela alcança

Também em E-133, e rotulado como medição de nível finito (Regra 10b;
H-140 continua valendo, `K_ell` é não decrescente e nenhuma faixa finita
decide o assintótico):

- O coeficiente primitivo em RMS fica entre `0,832` e `0,845` vezes
  `3^(-ell/2)` de `ell=2` a `ell=15`, sem tendência que o tire dali.
  Exatamente a escala de raiz quadrada.
- O máximo é muito maior: `sup * 3^(ell/2)` vai de 1,13 em `ell=2` a
  61,69 em `ell=15`, com `sup/rms` subindo de 1,3 para 73. A razão por
  nível `sup_ell/sup_(ell-1)` sobe de 0,6546 para 0,8513, com recuos em
  `ell=9` e `ell=12`, contra o `3^(-1/2)=0,5774` que uma cota uniforme de
  raiz quadrada exigiria.
- O maximizador fica na órbita de `1` sob duplicação em quase todo
  nível, o que é onde o suporte de `mu_ell` vive. O espectro primitivo é
  concentrado, não plano.

O que isso alcança: evidência forte, em nível finito, contra a forma
pontual uniforme do alvo de O4. O que isso NÃO alcança: a rota de
segundo momento não precisa de cota pontual, precisa que o pareamento
bilinear `sum_xi S_1(xi) S_2(xi)^*` seja pequeno. Descartar uma condição
suficiente não descarta o alvo. A medida restringe métodos de tipo l² e
função quadrática, e nada além disso.

Transferência para as somas condicionadas `S_i` de O4: pela recursão de
Tao (eq. 1.22), `mu_ell = sum_j 2^(-j) mu_ell^(j)`, decomposição pelo
primeiro passo. Jensen dá `E_ell <= sum_j 2^(-j) E_ell^(j)`, logo
condicionar no primeiro passo não pode reduzir a energia primitiva MÉDIA
e o obstáculo transfere na direção certa. Isso é uma cota inferior sobre
a média das energias condicionadas, não um enunciado sobre qualquer
`S_i(xi)` individual; a distância entre "o perfil de energia de `mu_ell`"
e "os `S_i` do alvo de O4" continua sendo real e não foi fechada aqui.

### (4) O4 não se reduz a O2

Procurei a ponte e ela não existe, por uma razão que dá para escrever.
O2 é uma cota INFERIOR sobre massa de cobertura e multiplicidade; O4 é
uma cota SUPERIOR sobre oscilação. Nenhuma das duas direções fecha:

- De O4 para O2: mesmo com `sup |muhat_r| <= 3^(-r(1/2+eps))`, inverter
  Fourier custa a norma l¹ sobre `3^r` frequências. Por Cauchy-Schwarz,
  `sum_{xi!=0} |muhat_r(xi)| <= 3^(r/2) * sqrt(K_r - 1)`, logo
  `|mu_r(b) - 3^(-r)| <= 3^(-r/2) * sqrt(K_r - 1)`. O fator
  `sqrt(K_r - 1)` NÃO é O(1) aqui: sob o platô medido em E-133 vale
  `K_r - 1 ~ 0,47 r`, logo o erro é da ordem de `0,68 * sqrt(r) *
  3^(-r/2)`, maior que `3^(-r)` por um fator `3^(r/2)` a menos de
  `sqrt(r)`. A escala pontual de que O2 e beta=1 tratam fica inteiramente
  abaixo do erro. Nem uma cota de Fourier com power-saving entrega uma
  cota inferior de cobertura. (Escrever `C*3^(-r/2)` aqui seria importar
  `K_infinity<infinity` sem dizer, que é exatamente o que H-140 existe
  para pegar.)
- De O2 para O4: uma cota inferior de multiplicidade não produz nenhuma
  cota superior de coeficiente de Fourier. H-149 já mostra o lado
  vizinho disso, que buraco de suporte sozinho não força espectro
  primitivo.

Não redução documentada, com o motivo explícito, em vez de "incompatível
por tipo".

### O que sobra

A única rota que esta análise deixa de pé é genuinamente bilinear:
cancelamento no pareamento `sum_xi S_1(xi) S_2(xi)^*` sem qualquer
decaimento pontual nem l², explorando a fase relativa entre as duas
irmãs. Todo método de função quadrática está barrado pelo item (2), e a
forma pontual uniforme está barrada, em nível finito, pelo item (3).
Registrada como H-162, em backlog, com a origem marcada.

Veredito desta rodada, sem forçar tentativa artificial: nenhum ângulo
novo viável para o regime 3. O ganho é a redução do item (1), que amarra
O4 ao mesmo ingrediente faltante de O7 pela ponte de H-155, e a
quantificação do item (2), que explica por que a hierarquia de três
escalas da §8 não é um caminho e sim uma descrição.

## Referências

- H-110/H-111 — a barreira de endogenia e sua calibração empírica.
- H-112 — checagem de novidade, conexão com a Weak Covering Conjecture.
- H-114 — teste computacional direto da WCC.
- Tao (2022), Seção 7 (item 106 do INDEX) — mecanismo completo lido
  integralmente nesta sessão.
- Análogos estruturais citados pelo Fable (não lidos nesta sessão,
  candidatos a checagem futura se o regime 2 for perseguido):
  Mauduit-Rivat, Fouvry-Mauduit, Spiegelhofer (correlações de funções
  digitais); Bourgain-Lindenstrauss-Michel-Venkatesh e sucessores
  (rigidez efetiva ×2×3); Breuillard-Varjú (decaimento de Fourier de
  medidas auto-similares).
