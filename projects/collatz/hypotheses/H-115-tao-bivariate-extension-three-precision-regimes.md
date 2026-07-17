# H-115 — Por que a extensão bivariada de Tao não cruza a barreira: três regimes de precisão, e onde cada um vive

Status: fechada — obstrução identificada com precisão matemática; um
lema tratável (regime 2) identificado como próximo passo opcional de
baixo risco; a barreira em si (regime 3) é equivalente a um problema
aberto reconhecido da área
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
