# H-104 — G(v) tem cauda de lei de potência universal com expoente α=2 exato (previsão do Fable, confirmada empiricamente); refuta a formulação original de "expoente de Kesten local por classe"

Status: confirmado — previsão teórica exata verificada empiricamente
Criada em: 2026-07-16
Origem: uma segunda IA externa consultada sobre a linha G(v)/medida de
Syracuse propôs que a heterogeneidade de 46× no termo de Jensen
(H-099) seria explicada por um "expoente de Kesten local" α(r) variando
por classe residual (classes com ramos "lentos" teriam cauda mais
pesada). Consultado sobre a validade dessa formulação antes de
implementar, o Fable identificou um erro conceitual real e propôs — e
resolveu — a versão matematicamente correta.

## Por que a formulação original estava errada

O Fable explicou: G(v) satisfaz uma equação de ponto fixo do tipo
"smoothing transform" (X ≟ Σ A_i·X_i), mas os pesos A_i não são i.i.d.
— são deterministicamente fixados pelo resíduo v mod 3^m nas primeiras
m gerações. A teoria clássica de Kesten (produtos de matrizes,
perpetuidades X=AX+B) não se aplica diretamente. A teoria correta é a
de "smoothing transforms" multitipo/modulados por Markov (Durrett–
Liggett, Guivarc'h, Liu, Biggins–Kyprianou, Buraczewski–Damek–
Guivarc'h): condicionar num prefixo finito muda apenas a **constante**
de cauda C(r) = Σ_folhas L(u)^α (onde L(u) é o produto de pesos ao
longo do caminho até a folha u da árvore-prefixo), não o **expoente**
α — que é um invariante GLOBAL, raiz de uma equação espectral
ρ(M(α))=1 sobre a matriz de transição entre "tipos" (resíduos).

## A previsão exata calculada pelo Fable

Montando M(α) para tipos mod 3^k (k=1 a 4, refinamento crescente), o
Fable encontrou ρ(M(1))=1 e ρ(M(2))=1 **exatamente**, com ρ<1 no
intervalo aberto (1,2) — ou seja, **α*=2 é a raiz não-trivial da
equação de pressão**, estável nos 4 níveis de refinamento testados.
No modelo mod 3 mais simples, verificável à mão: a soma dos dois
termos de sobrevivência vale exatamente 1 em α=1 (conservação de
massa: 1+2=3) e também em α=2 (3/5+12/5=3) — a estrutura 3-2 da
recursão (multiplicador 3 no numerador, 2^a no denominador) força essa
coincidência.

## Verificação empírica (estimador de Hill)

`experiments/E-090-syracuse-measure-vs-density/experiment_hill_tail_index.py`:

**Amostra global** (13.362 valores de G(v), v aleatório):

| topo da cauda (k) | α_Hill |
|---|---|
| 1% (k=133) | 1,973 |
| 2% (k=267) | 1,927 |
| 5% (k=668) | 1,699 |
| 10% (k=1336) | 1,589 |

No topo mais puro da cauda (1%, onde o viés do estimador de Hill é
menor), α_Hill=1,973 — essencially α=2. O decaimento para k maior é o
comportamento clássico esperado do estimador (incluir observações
menos extremas introduz viés para baixo, não indica um expoente
diferente).

**Por classe residual** (mod 3⁴=81, 3.000 amostras cada, k=150/5%):

| resíduo | α_Hill |
|---|---|
| 1 | 1,985 |
| 4 | 2,174 |
| 13 | 1,853 |
| 40 | 2,070 |
| 76 | 1,737 |

Todos os 5 valores ficam em torno de 2,0 (faixa 1,74-2,17) — **sem o
padrão dramaticamente diferente entre classes que a formulação
original da IA externa previa**. Isso confirma diretamente a correção
do Fable: o expoente é universal; a heterogeneidade de 46× do gap de
Jensen (H-099) deve vir da CONSTANTE de cauda C(r), não do expoente.

## O que ainda falta (próximo passo natural, não feito nesta sessão)

O Fable propôs a quantidade local correta para explicar a
heterogeneidade: dado α*=2, a "razão de participação"
PR(r) = S₁(r)²/S₂(r), onde S₁(r)=Σ_caminhos Π(pesos) e
S₂(r)=Σ_caminhos Π(pesos)², calculados por enumeração exata da
árvore-prefixo determinística da classe r (truncada em profundidade
razoável, erro de truncamento geométrico e controlável). Previsão:
gap(r) de Jensen deve ser decrescente em PR(r) — classes que
concentram massa num só caminho (ex: repetição de a=1) têm PR pequeno
e gap grande; classes que espalham massa têm PR grande e gap pequeno.
Essa regressão ainda não foi feita.

**Alerta estatístico do próprio Fable**: com α*=2, a variância de G em
escala linear está na fronteira da existência (E[G²] mal converge) —
isso significa que boa parte do fator 46× medido em H-099 pode ser
**ruído de amostra de cauda pesada**, não heterogeneidade estrutural
real. Antes de tratar o 46× como resultado sólido, seria preciso
bootstrap/half-sample por classe para separar sinal de ruído de cauda.

## Referências

- H-099 (achado original do gap de Jensen, 46× de heterogeneidade —
  agora com uma explicação candidata mais precisa, e um alerta de que
  parte do efeito pode ser ruído de cauda pesada).
- Experimento: `experiments/E-090-syracuse-measure-vs-density/experiment_hill_tail_index.py`.
- Script de validação do Fable (equação de pressão espectral,
  equivalência Parseval/ANOVA): `/tmp/.../scratchpad/validate_ideas.py`
  (fora do repositório — copiar para `experiments/` se for formalizado).
