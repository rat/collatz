# H-125 — Wirsching (2003): densidade invariante φ = análogo base-3 da função de Fabius, terceira perna de triangulação com teste computacional certificável

Status: concluída — experimento EXECUTADO até ℓ=500 (E-099, 2026-07-17): Conjectura 3 SUPORTADA numericamente com c≈0,54 (intervalo honesto 0,53–0,55); L_ℓ→2/3 com déficit 0,580/ℓ previsto pela própria φ₀ (ver seção "Resultado do experimento" abaixo). Integrada ao paper (Proposição~\ref{prop:fabius}, Teorema~\ref{thm:conjecture3}, main.tex/main-pt-br.tex, 2026-07-18 confirmado). Único item restante é opcional (escada ℓ∈{1000,2000,5000} para apertar a constante c) e explicitamente não recomendado sem necessidade específica.
Criada em: 2026-07-17
Origem: busca literária dirigida pedida explicitamente pelo diretor
científico ("achar coisas que ajudem a ter algo digno de citações").
Encontrado e baixado (com permissão explícita) Wirsching (2003), "On
positive predecessor density in 3n+1 dynamics", Discrete and
Continuous Dynamical Systems 9(3), 771-787 — item 132 do INDEX.md,
versão preliminar em `132_Wirsching-2003-Positive-Predecessor-
Density.pdf`. Rota DIFERENTE e mais refinada que a Weak Covering
Conjecture do livro de 1998 (H-112/H-114), para o mesmo objetivo
(densidade positiva de predecessores 3n+1).

## O objeto central

O paper define funções "Elka" e_ℓ(k,a):=|E_{ℓ,k}(a)|, contando
caminhos no grafo de Collatz de comprimento k+ℓ (k passos T₀, ℓ passos
T₁) terminando em a — o mesmo objeto combinatório de contagem que
sustenta toda a nossa linha G(v)/Syracuse. O espaço de estados natural
é 𝕏=𝕀₃×ℤ₃ˣ: o fator ℤ₃ˣ carrega a variável 3-ádica a (habitat da
nossa medida de Syracuse μ); o fator 𝕀₃≅{0,1,2}^ℕ carrega k/3^ℓ (a
contagem normalizada de passos T₀). **As duas marginais da mesma
contagem**: marginal 3-ádica = análogo backward da medida de Syracuse
de Tao; marginal arquimediana = converge para uma densidade φ.

**Identidade de φ (derivada pelo Fable)**: φ é a densidade da variável
aleatória real X=Σ_{j≥1} 2U_j·3^{-j} (U_j uniformes iid em [0,1]) — o
análogo BASE-3 da **função de Fabius** (que satisfaz f'(x)=2f(2x); a
nossa satisfaz φ'(x)=(9/2)φ(3x) em [0,2/3]) — da família das "atomic
functions" de Rvachev. Prova (Corolário 7 do paper): φ é o único ponto
fixo em L¹([0,1]) do operador de médias W₃f(x):=(3/2)∫_{3x-2}^{3x}f(t)dt,
C^∞, polinomial em cada intervalo fora do conjunto de Cantor clássico,
com convergência geométrica certificada (∥f_n−φ∥₁≤2^{-n+1}∥f₁-f₀∥₁).

**Não é a mesma medida que nossa μ de Syracuse** — é o objeto DUAL/
complementar da mesma contagem, vivendo no lugar arquimediano em vez
do 3-ádico. Não há transformada direta entre os dois; a conexão
genuína é serem as duas marginais do mesmo objeto combinatório.

## As 3 conjecturas (cadeia lógica reduzindo densidade positiva)

**Teorema 1** (provado): condição (⋆₁) sobre razão limitada de Elka
functions ⟹ densidade positiva uniforme de predecessores.
**Conjectura 1**: (⋆₂) sobre generators g_ℓ(k,a) ⟹ (⋆₁).
**Conjectura 2**: (⋆₄) sobre razão de iteradas de W₃ aplicadas a
indicadores ⟹ condição intermediária do Teorema 2.
**Conjectura 3** (a mais concreta, implicação (⋆₅)⟹(⋆₄) PROVADA no
paper): existe φ₀ (função de comparação explícita, assintótica
log-normal) tal que liminf φ(z_ℓ)/φ₀(z_ℓ)=c>0 uniformemente em
sequências na classe A_δ (janela CLT |ℓ−k_ℓ|≤δ√ℓ — o mesmo regime
crítico que aparece como β=1 em H-124 e regime 3 em H-115). O paper
cita evidência de suporte já na literatura: Berg & Krüppel (1998,
seção 9) sugerem que a Conjectura 3 é verdadeira.

## Por que isso é uma terceira perna de triangulação (não um atalho)

A janela A_δ é a mesma "janela CLT em torno da diagonal k≈ℓ" que
aparece em β=1 (H-124) e no regime 3 (H-115) — mesmo regime crítico de
contração marginal, roupagem analítica diferente (equação funcional
real em vez de contagem inteira ou caracteres de Tao). A dificuldade
não muda de natureza; muda de forma. Isso é exatamente o que dá valor
de triangulação: WCC inteira (H-114) / β=1 de Tao (H-124) / equação
funcional real (aqui) sobre a MESMA barreira, três roupagens
independentes.

**Ressalva honesta necessária**: verificar a Conjectura 3 numericamente
NÃO fecha a cadeia — as Conjecturas 1 e 2 permanecem abertas acima
dela, e são trocas de limite-com-uniformidade do mesmo tipo duro.
Evidência numérica da Conjectura 3 é evidência na ponta mais concreta
de uma cadeia com dois elos conjecturais não testados.

## Experimento desenhado (não implementado ainda)

**O teste ingênuo falha**: sequências (x_ℓ)∈A_δ têm x_ℓ~ℓ·3^{-ℓ}
(cauda esquerda extrema de φ), onde φ(x)~exp(-c·ℓ²) — super-
exponencialmente pequeno. A garantia L¹ do Corolário 8 não controla
erro pontual nessa escala; já em ℓ=20 o valor está abaixo de qualquer
precisão prática.

**Redução rigorosa que funciona** (derivada pelo Fable): definindo
primitivas iteradas F_j de φ, obtém-se por indução, para z≤2/3 e
qualquer m com 3^m·x≤2/3:

φ(x) = (3/2)·2^{-m}·3^{-m(m-1)/2}·F_{m+1}(3^{m+1}x)

com F_{m+1}(y)=∫₀^{min(y,1)} ((y-t)^m/m!)·φ(t)dt. Escolhendo m≈ℓ tal
que y=3^{m+1}x∈(2/3,2], toda a dificuldade da cauda vira uma integral
suave de φ na escala macro — perfeitamente condicionada. φ na escala
macro é obtida iterando W₃ (aritmética racional exata: W₃ⁿχ_{[0,1]} é
polinomial por partes de grau n com nós triádicos), com erro
certificável em F_{m+1}(y) (≤(y^m/m!)·2^{-n+1}·C, não heurística).
Alcança ℓ na casa das centenas — ordens de magnitude além de H-114.

A razão-alvo real (⋆₅) reduz-se, via a fórmula acima, a
φ(3x)/φ(x)=2·3^{m-1}·F_m(y)/F_{m+1}(y) com o MESMO y — razão de dois
momentos consecutivos de φ num ponto O(1).

## Bloqueio atual: precisa de 2 papers antes de implementar

φ₀ (a função de comparação da Conjectura 3) só é dada no paper em
formato assintótico geral, sem as constantes explícitas — necessárias
para implementar o teste, não apenas desejáveis. Papers identificados
(não baixados ainda):

1. **Berg, L. & Krüppel, M. (1998)**, "On the Solution of an
   Integral-Functional Equation with a Parameter", Zeitschrift für
   Analysis und ihre Anwendungen (ZAA) 17(1), 159-181 — contém a Seção
   9 citada como evidência de suporte à Conjectura 3. Provavelmente
   acessível via EMS Press (https://ems.press/journals/zaa/issues/724).
2. **Berg, L. & Krüppel, M.**, "Series Expansions for the Solution of
   an Integral-Functional Equation with a Parameter", Results in
   Mathematics (Springer, DOI 10.1007/BF03322765,
   https://link.springer.com/article/10.1007/BF03322765) — expansões
   em série da mesma solução, potencialmente mais direto para
   implementação que o paper de 1998.

## Ponte fechada e algoritmo final (2026-07-17, papers 133/134 em mãos)

**Ponte de notação (verificada lendo Wirsching 2003 seção 7 + BK 1998
pp. 159-160, 178-180)**:

1. O φ₀ da Conjectura 3 é DEFINIDO pelo Wirsching em (7.11) como o lado
   direito da assintótica (9.6) do BK — a fórmula fechada em si
   ("g₀(t) ~ φ₀(t) := ..."), não g₀ (nada de Bromwich), não a solução
   completa com fator Q. Constantes: α=1/2−ln2/ln3, β=1/(2ln3),
   δ=1/2+α−2β·ln(2β), γ=−2β−δ−1/2, ε=1/2+α−β·ln(2β). Valores:
   α≈−0,1309297536, β≈0,4551196133, δ≈0,4546762683, γ≈−1,8649154949,
   ε≈0,4118732574. USAR EXPRESSÕES SIMBÓLICAS (erro 10⁻⁵ em β gera
   erro O(1) no log para ℓ~300, pois β multiplica ln²t~ℓ²ln²3).
2. O φ do BK (eq. (1), a=3, b=3/2: φ(t)=(3/2)∫_{3t−2}^{3t}φ) É
   IDENTICAMENTE o φ do Wirsching (mesma equação W₃φ=φ, mesma
   normalização ∫₀¹φ=1, supp⊂[0,1]; BK citam Wirsching [8]
   explicitamente para a=3, p. 160). λ=1/b=2/3 é o "special case" da
   Prop. 9.3 do BK. Nenhum ajuste de constantes; qualquer constante
   multiplicativa seria absorvida em c de qualquer forma.
3. **Ressalva importante (BK p. 180, último parágrafo)**: a expectativa
   de BK é φ ~ g₀ "up to a factor which is both bounded and bounded
   away from zero" — por causa do fator Q ESPECÍFICO e não trivial da
   Prop. 9.3 (Φ(p)~G₀(p)Q(ln p/ln a)). A Conjectura 3 do Wirsching
   (lim = c constante) é mais forte que isso. O experimento deve
   detectar os dois cenários: razão convergente vs. modulação
   log-periódica em log₃(1/x). Observação-chave: a razão que entra de
   fato em (⋆₄) é r(3x)/r(x), que é IMUNE a modulação log₃-periódica —
   então mesmo o cenário fraco de BK pode bastar para (7.5).

**Upgrade do algoritmo — W₃ eliminado**: os momentos M_i=E[X^i] de φ
são racionais EXATOS pela autossimilaridade X =_d (2U+X)/3:
M_i = [Σ_{k=1}^i C(i,k)·(2^k/(k+1))·M_{i−k}]/(3^i−1). Com y=3^{m+1}x
∈[1,2] (caso A), F_{m+1}(y)=(1/m!)·E[(y−X)^m] é soma binomial exata
de momentos — erro zero, sem iterar W₃. Caso B (y∈(2/3,1)): simetria
φ(t)=φ(1−t) (BK Prop. 4.1) dá F_j(y)=(1/(j−1)!)E[(y−X)^{j−1}]
+(−1)^j·F_j(1−y), e F_j(w)=(3/2)·3^{−j}·F_{j+1}(3w) re-escala o
argumento pequeno; recursão com truncamento certificado via
0≤F_j(w)≤w^{j−1}/(j−1)!.

**Validação executada** (script em scratchpad da sessão): M₁=1/2,
M₂=7/24, momentos centrais ímpares ≡0 exatos; φ(1/2)=3/2; redução
(casos A e B) confere com ponto fixo em grade independente em ~6
dígitos (limite da grade); φ₀ satisfaz (7.12) numericamente
(λφ₀'/aφ₀(3t)→1 até ℓ=200; usar derivada logarítmica ANALÍTICA, diff
numérico explode a precisão para ℓ grande).

**Teste decisivo**: L_ℓ := 3^{1−ℓ}·φ(3x⁺_ℓ)/φ(x⁺_ℓ)
= 2·3^{m−ℓ}·F_m(y)/F_{m+1}(y) (mesmo y). Predição via φ₀ (7.13):
L_ℓ → 2/3. (⋆₄) precisa de limsup < 1. Segunda saída: ln r_ℓ =
ln φ(z_ℓ) − ln φ₀(z_ℓ) — convergência vs. oscilação log-periódica.
Trabalhar SEMPRE em logs (φ ~ 3^{−ℓ²/2}); mp.dps~60 basta (nunca
exponenciar valores minúsculos).

## Resultado do experimento (E-099, 2026-07-17, ℓ=250–500, 6+ decimais)

**Dados (u=0)**: ln r = ln φ(z_ℓ) − ln φ₀(z_ℓ) = −0,66894826 (ℓ=250),
−0,66457839 (300), −0,66117415 (350), −0,65843318 (400), −0,65616994
(450), −0,65426365 (500). Crescente, côncavo, uniforme em u∈[−2,2]
(dispersão <8×10⁻⁵, encolhendo com ℓ). Sem sinal de modulação
log-periódica (cenário do fator Q de BK) — monotonia limpa.

**Ajuste de cauda (critério de estabilidade de C por incrementos
consecutivos, 8 formas testadas)**:
- **C/√ℓ confirmada como melhor forma**: C=0,79 estável (spread 0,87%,
  drift NÃO-monótono), L_i = −0,6187…−0,6190; razões de incremento
  observadas (0,7790/0,8052/0,8257/0,8423) batem com a predição de
  ℓ^{−1/2} (0,7772/0,8061/0,8283/0,8460) em ≤0,4%. Ajuste global com
  expoente livre dá p=0,51; dois termos L−C/√ℓ−D/ℓ dá L=−0,6191.
- **C·ln²ℓ/ℓ REBAIXADA** pela extensão: C agora exibe drift monótono
  (+3,3%), L_i deriva (−0,6295→−0,6284). Era co-líder com 4 pontos;
  não é mais.
- **Degenerescência residual**: C/ln²ℓ é igualmente estável (spread
  0,84%, não-monótono) e dá L=−0,599. Indistinguível de C/√ℓ nesta
  faixa (fator 2 em ℓ); é a fonte dominante da incerteza sistemática.
- **C/lnℓ desfavorecida**: drift monótono forte de C (−9,9%), L_i sem
  estabilizar, e razões de incremento previstas ~+0,02 acima das
  observadas. C/ℓ e C·lnℓ/ℓ excluídas (drift 14–24%).
- **Nota estrutural**: ln r crescente ⟹ liminf φ/φ₀ ≥ e^{−0,669} > 0
  ao longo de toda a janela testada, INDEPENDENTE da forma da cauda —
  o cenário c=0 exigiria ln r decrescente, que não é o observado.

**Estimativa final**: L = −0,619 ± 0,001 (estatística, dentro da
família de potência) com sistemática de forma funcional [−0,63; −0,60]
⟹ **c = e^L ≈ 0,538, intervalo honesto 0,53–0,55** (a incerteza é
sistemática de forma, não estatística — os dados têm erro certificado
~10⁻⁸).

**Razão decisiva**: L_ℓ → 2/3 com aproximação 1/ℓ limpíssima:
ℓ·(2/3−L_ℓ) = 0,58020/0,58012/0,58006/0,58001 (ℓ=350…500). Check de
consistência forte: a PRÓPRIA φ₀ prediz esse coeficiente
(ℓ·déficit^{φ₀} → 0,579…0,58 em ℓ=10⁴–10⁵) — o subleading de L_ℓ
bate com Berg-Krüppel, não só o limite 2/3. limsup L_ℓ < 1 com folga
enorme ⟹ (⋆₅) suportada.

**Frase-resumo citável**: "Teste numérico com erro certificado
(aritmética racional exata via momentos da autossimilaridade; erro
≤10⁻⁸) da Conjectura 3 de Wirsching (2003) até profundidade ℓ=500 na
janela CLT (k=ℓ+u√ℓ, u∈[−2,2]): a razão decisiva
L_ℓ=3^{1−ℓ}φ(3x_ℓ)/φ(x_ℓ) converge ao valor previsto 2/3 com déficit
(0,580±0,001)/ℓ — coeficiente reproduzido pela própria assintótica φ₀
de Berg–Krüppel — mantendo limsup L_ℓ<1 com folga, como exige (⋆₅);
ln(φ/φ₀) é crescente, côncavo e uniforme em u (dispersão <10⁻⁴),
consistente com limite finito L=−0,619±0,001(estat)±0,015(forma), i.e.
c=e^L≈0,54 (intervalo honesto 0,53–0,55), com cauda melhor descrita
por 0,79/√ℓ; nenhum sinal de modulação log-periódica (cenário do fator
Q de BK). Isto suporta a ponta mais concreta da cadeia; as Conjecturas
1–2 permanecem abertas acima dela."

**Para apertar c (opcional)**: os 3 candidatos sobreviventes preveem
ln r em ℓ=2000: −0,63664 (C/√ℓ), −0,63808 (ln²ℓ/ℓ), −0,63610 (1/ln²ℓ)
— separação 5×10⁻⁴–1,4×10⁻³ contra incerteza de extrapolação ~4×10⁻⁴
por forma. Uma escada geométrica ℓ∈{1000, 2000} (idealmente 5000, onde
a separação √ vs 1/ln² sobe a 1,5×10⁻³) discriminaria; ℓ=1000 sozinho
é marginal. Custo cresce ~ℓ² (momentos racionais até N~2000).

## Valor para o pacote de publicação (independente do teste ser feito)

1. Identificação de φ como análogo base-3 da função de Fabius/atomic
   function de Rvachev — conecta nosso trabalho a uma literatura
   analítica madura (Berg, Krüppel, Rvachev) raramente citada pela
   comunidade Collatz. Citável por si só como contribuição de
   enquadramento.
2. Confirmação (via Fable) de que Krasikov-Lagarias (γ=0,84) continua
   sendo o melhor resultado incondicional conhecido — a rota do
   Wirsching 2003 não foi superada, nem por Tao (que resolve um
   problema diferente, densidade LOGARÍTMICA de órbitas limitadas, não
   densidade natural de predecessores).
3. ~~Nota de rigor bibliográfico: o PDF baixado é marcado "(preliminary
   version)" — a versão de journal é DCDS 9(3), 771-787 (2003);
   conferir números de equação contra a versão final antes de citar
   no pacote.~~ **CONFIRMADO (2026-07-18) pelo diretor científico: as
   equações são as mesmas entre a versão preliminar em mãos e a versão
   final publicada.** Citações de (7.5), (7.11), (7.12), (7.13) etc.
   no paper e nesta hipótese podem ser usadas sem ressalva.

## Próximos passos

1. ~~Diretor científico baixar os 2 papers de Berg-Krüppel~~ — FEITO
   (itens 133/134 do INDEX.md).
2. ~~Implementar o experimento de antiderivadas iteradas~~ — FEITO
   (E-099, `experiment_conjecture3.py`), executado até ℓ=500 com erro
   certificado ≤10⁻⁸.
3. Documentado como quarta linha de evidência (junto com H-111 ρ_eff,
   H-114 WCC, H-124 β=1) — ver frase-resumo citável acima. Pronto para
   entrar no pacote de publicação.
4. Opcional, não pré-requisito: escada ℓ∈{1000,2000,5000} para apertar
   o valor de c (discriminar entre C/√ℓ, ln²ℓ/ℓ, 1/ln²ℓ) — custo cresce
   ~ℓ², não perseguir sem necessidade específica do texto final.

## Referências

- H-110/H-111/H-112/H-114/H-124 — a barreira de endogenia e as outras
  duas pernas de triangulação (WCC, β=1 de Tao).
- Wirsching (2003), item 132 do INDEX.md.
- Krasikov & Lagarias (2003) — melhor bound incondicional conhecido,
  já citado em H-091.
