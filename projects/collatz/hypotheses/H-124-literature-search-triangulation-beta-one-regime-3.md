# H-124 — Busca literária dirigida: três literaturas independentes confirmam a obstrução do regime 3, e uma forma mínima nomeada (β=1 de Tao) equivalente à WCC de Wirsching

Status: concluída — não reabre o regime 3, mas fornece triangulação e um enquadramento mais forte para o pacote de publicação
Criada em: 2026-07-17
Origem: pedido do diretor científico de buscar literatura especificamente
sobre a linha G(v)/qx+1/endogenia que pudesse melhorar o material para
uma publicação de respeito. Busca dirigida (WebSearch/WebFetch) por 5
frentes específicas motivadas pelo framework de três regimes de H-115.

## Os 5 achados

1. **Tao (2011), post de blog "The Collatz conjecture, Littlewood-Offord
   theory, and powers of 2 and 3"**: prova Proposições 6/7 (separação
   polinomial/exponencial de 2^a−3^k), mas CONDICIONAIS à conjectura
   fraca de Collatz já ser verdadeira — e o próprio post reconhece que
   o teorema de Baker/transcendência já dá incondicionalmente uma
   separação mais forte, tornando as proposições um exercício
   metodológico sem valor de ferramenta. A técnica (Littlewood-Offord +
   produtos de Riesz + Bohr sets) transfere estruturalmente de
   "evitação" (o problema de ciclos) para "cobertura" (nossa WCC), mas
   a segunda metade do argumento (refutar concentração de Bohr dos
   geradores 2^{α_i}·3^i mod 3^ℓ) reduz-se a não-concentração de
   órbitas de ×2 mod 3^s — território Erdős/Mahler/Z-numbers,
   reconhecidamente aberto. **Sem ferramenta nova**, mas dá um lema de
   redução condicional honesto (upgrade de "analogia" para "redução
   explícita a problema nomeado").

2. **Varjú & Yu (2022), "Fourier decay of self-similar measures..."**:
   dá decaimento quantitativo assumindo razão de contração não-Pisot/
   não-Salem. Nossa medida (razões racionais 3/2^a) satisfaz
   nominalmente a condição, MAS: (i) a conclusão de VY é apenas
   polilogarítmica, exponencialmente aquém do power-saving necessário;
   (ii) nas frequências ressonantes, o teto colapsa exatamente no
   problema de (3/2)^n mod 1 (Mahler, Flatto-Lagarias-Pollington) — já
   conectado a Collatz por Lagarias, e igualmente aberto. **Não é
   porta — é a nomeação mais precisa da parede que temos.**

3. **Badea & Grivaux (2023)**: mostra que medidas T_p-invariantes
   GENÉRICAS (sentido de Baire) não convergem para Lebesgue sob
   T_{q^n}. Irrelevante como obstáculo real: nossa medida de Syracuse
   não é genérica nesse espaço (é estruturada, autosimilar, exata) e
   nem é literalmente T_p-invariante no sentido do resultado — a
   conexão com H-115 é via analogia de rigidez efetiva, não invariância
   literal. Calibra (nenhum argumento "soft"/genérico basta — precisa
   de estrutura aritmética específica), não bloqueia.

4. **Tao (2020), post de blog "Equidistribution of Syracuse random
   variables and density of Collatz preimages"** — o achado mais
   importante. Define c_n:=inf_{b∈ℤ/3ⁿℤ,3∤b} P(Syrac(ℤ/3ⁿℤ)=b) e
   propõe a conjectura **β=1** (c_n=3^{-n+o(n)}, "nenhuma classe de
   resíduo tem probabilidade muito menor que a média"). Prova
   condicionalmente: β=1 ⟹ densidade de Collatz ≫x^{1-o(1)} (quase
   total). Cita o melhor resultado incondicional conhecido,
   Krasikov-Lagarias (2003), γ=0,84.

   **Verificação estrutural feita pelo Fable**: a variável de Syracuse
   de Tao e os conjuntos R_{j,k} de Wirsching são, após um twist de
   unidade, o MESMO objeto algébrico (somas de potências de 2 e 3 com
   expoentes estritamente decrescentes). WCC (3.9, sub-exponencial)
   ⟹ β=1 essencialmente (conta de entropia exata: j=log₄3·ℓ+o(ℓ) dá
   c_ℓ≳3^{-ℓ(1+o(1))}); β=1 sozinho só dá uma WCC enfraquecida (K
   exponencial). São formulações irmãs na mesma escala de entropia
   exata (o limiar log₄3≈0,7925 de H-114 é a mesma identidade
   4^j vs. 3^ℓ nos dois lados — não coincidência).

   **Consequência direta e valiosa para H-114**: o excesso
   e(ℓ)=j*(ℓ)−log₄3·ℓ medido em H-114 é literalmente o o(n) do
   expoente de β=1 (c_ℓ≳3^{-ℓ}·4^{-e(ℓ)}) — e(ℓ) sub-linear ⟺ K
   sub-exponencial ⟺ compatível com β=1. **Nossa leitura qualitativa
   de H-114 (crescimento lento favorecido sobre estabilização, mas
   sub-linear em ambos os casos) é evidência computacional DIRETA a
   favor de β=1** — não só da WCC. H-114 pode ser reenquadrado como
   primeiro teste computacional do esqueleto de cobertura de AMBAS as
   conjecturas.

   **Insight estrutural adicional**: a rota de Tao mostra que a
   decomposição endogenia/decorrelação bivariada de H-110 É EVITÁVEL —
   ele substitui "quase-independência entre subárvores" por "separação
   determinística de pré-imagens (fácil, Prop. 4 do post) + controle
   L^∞ marginal (β=1, onde mora toda a dificuldade)". Isso responde a
   pergunta implícita de H-110 ("existe rota que dispense a
   decorrelação?") — sim, existe, é a de Tao, e ela bate na MESMA
   parede em forma marginal. Temos agora **três articulações
   quase-equivalentes do mesmo ingrediente faltante**: endogenia
   (H-110), Weak Covering Conjecture (H-112/H-114), β=1 (este achado) —
   nenhuma provada. Triangulação máxima entre três abordagens
   independentes (nossa, Wirsching 1998, Tao 2020).

5. **Spiegelhofer (2021/2023), "Collisions of digit sums in bases 2 and
   3"**: prova infinitas colisões s_2(n)=s_3(n), taxa
   N^{log₄3-δ} — mesmo limiar log₄3 por ser a mesma contabilidade de
   entropia 4^j vs. 3^ℓ (estrutural, não coincidência). Mas é resultado
   de contagem/existência ABAIXO do limiar (média sobre n, não
   worst-case sobre resíduos) — exatamente onde a técnica satura, sem
   cruzar. Classificado por H-115 como análogo (i) da obstrução do
   regime 3; este paper confirma a classificação. **Fila condicional**:
   só ler a fundo se o lema opcional do regime 2 de H-115 for escrito
   (as estimativas de somas exponenciais podem servir a módulos
   polinomiais, onde power-saving não é necessário).

## Item de bibliografia verificado

Krasikov-Lagarias (2003), γ=0,84 (melhor incondicional conhecido) — já
citado corretamente em H-091 (linhas 76-77, 161-167), com a hierarquia
honesta em torno dele. Sem lacuna — só conferir formatação completa da
referência (Acta Arithmetica 109, 237-258) no pacote de publicação.

## Veredito final

**Não reabre o regime 3** — nenhuma ferramenta nova foi encontrada, e
dois dos achados (1 e 2) na verdade REFORÇAM o diagnóstico de H-115 por
vias independentes (triangulação entre combinatória aditiva/Littlewood-
Offord, decaimento de Fourier auto-similar, e agora a própria conjectura
de Tao). Mas o achado 4 é genuinamente valioso para o ENQUADRAMENTO do
pacote de publicação: (a) H-115 ganha a forma mínima nomeada da
barreira (β=1, mais fraca que power-saving, proposta pelo próprio Tao,
aberta há 6 anos, nunca virou paper); (b) H-114 vira teste computacional
do esqueleto de cobertura de β=1 além da WCC, com e(ℓ) sub-linear como
evidência a favor — alegação de publicação mais forte e mais precisa;
(c) H-110 ganha a confirmação de que a rota "sem decorrelação" existe
(a de Tao) mas concentra toda a dificuldade no marginal, e H-112 ganha
a terceira articulação equivalente do ingrediente faltante.

## Ações de arquivo recomendadas

1. Adicionar o post de Tao (jan/2020) ao índice de literatura — como
   SEQUÊNCIA (não precursor) do paper de 2022 (arXiv de set/2019); o
   post explora a direção de pré-imagens que ficou fora do paper
   publicado e nunca virou artigo próprio.
2. H-115 e H-114 devem cruzar-referenciar β=1 (feito nesta hipótese;
   considerar nota direta nos arquivos originais se o pacote for
   escrito).
3. Próxima passada de literatura (se houver): checar rapidamente se
   há progresso pós-2020 em β=1 — não encontrado nenhum até o momento
   desta busca (2026-07-17).

## Referências

- H-110 (barreira de endogenia), H-112 (Weak Covering Conjecture,
  novidade), H-114 (teste computacional da WCC), H-115 (três regimes
  de precisão da extensão de Tao) — todas recalibradas por este achado.
- Tao (2011), "The Collatz conjecture, Littlewood-Offord theory, and
  powers of 2 and 3", https://terrytao.wordpress.com/2011/08/25/
- Tao (2020), "Equidistribution of Syracuse random variables and
  density of Collatz preimages", https://terrytao.wordpress.com/2020/01/25/
- Varjú & Yu (2022), "Fourier decay of self-similar measures and
  self-similar sets of uniqueness", Analysis & PDE 15(3), 843-858
  (arXiv:2004.09358).
- Badea & Grivaux (2023), "Around Furstenberg's times p, times q
  conjecture: times p-invariant measures with some large Fourier
  coefficients", Discrete Analysis (arXiv:2303.01089).
- Spiegelhofer (2021/2023), "Collisions of digit sums in bases 2 and
  3", Israel J. Math. 258, 475-502 (arXiv:2105.11173).
- Krasikov & Lagarias (2003), "Bounds for the 3x+1 Problem using
  Difference Inequalities", Acta Arithmetica 109, 237-258 (já citado
  em H-091).
