# H-114 — Primeiro teste computacional direto da Weak Covering Conjecture de Wirsching (1998): j*(ℓ) existe até ℓ=17, regime assintótico indeterminado

Status: fechada por ora — dado primário estabelecido até ℓ=20; regime
assintótico ainda formalmente indeterminado mas com leitura qualitativa
(favorece crescimento lento ilimitado sobre estabilização pura);
extensão adicional (ℓ≥21) descartada por custo explosivo (~3,3×/passo)
sem ganho de poder estatístico — próximo passo real seria reescrever o
algoritmo (bitset comprimido/vetorizado), não rodar mais ℓ em Python puro
Criada em: 2026-07-17
Origem: depois de fechar o pacote de publicação (H-109 a H-113) e esgotar
7 rodadas de tentativas de "importar maquinaria de outra área" para
atacar a barreira de endogenia (todas refutadas — ver H-110/H-111 e o
STATE.md), o diretor científico pediu duas frentes de pesquisa
genuinamente não tentadas: (1) testar computacionalmente a própria
Weak Covering Conjecture de Wirsching (1998) com a definição exata
dele, nunca feito antes até onde sabemos; (2) ler a fundo a Seção 7 da
prova de Tao (2022) para avaliar a extensão bivariada a sério (ver
H-115). Esta hipótese documenta a frente (1).

## Enunciado

Testar diretamente, por força bruta/DP, se a família de conjuntos
R_{j-1,j} (somas mistas de potências de 2 e 3, Corolário II.5.8 do
livro de Wirsching) cobre todos os resíduos invertíveis módulo 3^ℓ, e
medir como o menor j que cobre (j*(ℓ)) escala com ℓ — o objeto exato da
"Weak Covering Conjecture for Mixed Power Sums" (Conjectura 3.9,
Capítulo V), identificada em H-112 como estruturalmente equivalente ao
"ingrediente que falta" da barreira de endogenia de H-110.

## Definições exatas (verificadas contra o PDF, item 131 do INDEX)

- R_{j,k} := {Σ_{i=0}^j 2^{α_i}·3^i : j+k≥α_0>α_1>...>α_j≥0} ⊂ ℤ₃*,
  |R_{j,k}|=C(j+k+1,j+1) (Corolário II.5.8, p.127).
- "A cobre B módulo 3^ℓ" ⟺ π_ℓ(B)⊂π_ℓ(A) (Definição V.1.1, p.124-125).
  Todo elemento de R_{j,k} é automaticamente uma unidade mod 3 (o termo
  de maior expoente não é divisível por 3, todos os outros são) —
  cobrir ℤ₃* mod 3^ℓ = atingir as 2·3^{ℓ-1} classes invertíveis.
- **Conjectura 3.9** (p.139, verbatim): existe K(ℓ)>0 sub-exponencial
  (lim K(ℓ)e^{-γℓ}=0 ∀γ>0) tal que ∀j,ℓ: |R_{j-1,j}|≥K(ℓ)·3^ℓ ⟹
  R_{j-1,j} cobre ℤ₃* mod 3^ℓ. (Leitura correta, confirmada pelo Fable:
  existencial em K, não universal.)
- **Simplificação estrutural** (derivada e verificada pelo Fable): para
  j≥ℓ, todo termo de índice i≥ℓ morre mod 3^ℓ, dando
  R_{j-1,j} mod 3^ℓ = 2^{j-ℓ}·R_{ℓ-1,j} mod 3^ℓ — reduz o custo de
  enumeração de C(2j,j) para C(j+ℓ,ℓ).

## Como testar

DP de bitset com rotação cíclica (especificado pelo Fable,
implementado em `experiment_wcc.py`, E-098): processa expoentes
candidatos em ordem decrescente, mantendo para cada contagem c de
termos já escolhidos o conjunto de somas parciais alcançáveis mod 3^ℓ
como um inteiro Python (bitset); escolher o expoente v na posição c é
uma rotação cíclica por 2^v·3^c mod 3^ℓ. Contagem de bits do bitset
final (`int.bit_count()`) dá o tamanho da imagem diretamente.

**Validação**: bateu exatamente (100%) contra a tabela de referência
do Fable, j*(ℓ) para ℓ=1..7 = 1,4,6,7,9,10,11, e contra uma checagem
pontual (ℓ=2,j=2: imagem={1,2,5,7} mod 9, faltando {4,8}).

## Resultado (ℓ=1 a 20)

```
ell  j*   j*/ell   K_diag       excesso e(ell)=j*-ell*log4(3)
1    1    1.0000   0.6667       0.208
2    4    2.0000   7.7778       2.415
3    6    2.0000   34.2222      3.623
4    7    1.7500   42.3704      3.830
5    9    1.8000   200.0823     5.038
6    10   1.6667   253.4376     5.245
7    11   1.5714   322.5569     5.453
8    12   1.5000   412.1561     5.660
9    13   1.4444   528.4052     5.868
10   15   1.5000   2626.9288    7.075
11   16   1.4545   3393.1164    7.283
12   17   1.4167   4391.0918    7.490
13   18   1.3846   5692.1560    7.698
14   19   1.3571   7389.8166    7.905
15   20   1.3333   9606.7616    8.113
16   20   1.2500   3202.2539    7.320  (platô: j* nao cresceu)
17   21   1.2353   4168.0130    7.528
18   22   1.2222   5431.0472    7.735   (139s)
19   23   1.2105   7083.9746    7.943   (485s)
20   24   1.2000   9248.5224    8.150   (1597s ~ 27min)
```

Custo cresceu ~3,3×/passo nos últimos pontos (ℓ=18→19→20: 139s→485s→
1597s) — extensão a ℓ=21+ custaria ~90min, ℓ=22 ~5h, ℓ=23 ~16h,
inviável em Python puro sem reescrever o algoritmo (bitset
comprimido/vetorizado).

**Leitura honesta final (após extensão a ℓ=20 e reanálise completa —
corrige uma leitura intermediária)**: com os 17 primeiros pontos, a
inclinação local de j* parecia desacelerar monotonicamente até ≈0,77
(perto do limiar log₄3≈0,7925), sugerindo possível convergência. Os 3
pontos novos (ℓ=18,19,20, incrementos todos exatamente +1, sem novos
platôs) mostram que essa "desaceleração monotônica" era **artefato do
platô isolado em ℓ=16** atravessando a janela deslizante — sem ele, a
inclinação local oscila em 0,74–0,86, **cavalgando o limiar log₄3 dos
dois lados**, não convergindo de forma limpa. e(20)=8,150 é um novo
máximo da série (supera e(15)=8,113).

Ajustes formais (const/linear/log/sqrt em e(ℓ), AIC/BIC) na cauda
ℓ=10-20: a **estabilização pura passou de "empatada" para
desfavorecida** (ΔAIC≈5 contra o modelo constante) — consistente com o
déficit de platôs (1 platô observado em 19 incrementos vs. ~3,9
esperados sob estabilização na taxa log₄3; teste binomial p≈0,072,
marginal mas na mesma direção). Crescimento lento ilimitado (log ℓ, √ℓ,
ou linear muito lento a 0,07/passo) continua indistinguível entre si
(ΔAIC<0,5, correlação de regressores ≥0,995 — limite matemático de
identificabilidade, não falha de método). Os quatro modelos só
divergiriam por ≥1 unidade de j* perto de ℓ≈40 — inalcançável por este
caminho algorítmico.

**Estatística discriminante identificada** (frequência de platôs
Δj*(ℓ)=0): permanece a métrica correta para trabalho futuro, mas com
apenas 1 platô em 19 incrementos o teste ainda não tem poder decisivo
(p≈0,072, não cruza 0,05).

## Veredito

Este é (até onde sabemos) o primeiro teste computacional direto do
objeto exato da Weak Covering Conjecture de Wirsching, estendido até
ℓ=20. O dado primário — j*(ℓ) existe e é finito em toda a faixa
testada, com DP validada exatamente contra referência independente —
é uma contribuição honesta por si só. A leitura qualitativa (não
formalmente decisiva, mas consistente em duas estatísticas
independentes — ΔAIC e frequência de platôs) **favorece crescimento
lento ilimitado de e(ℓ) sobre estabilização pura** — compatível com a
conjectura fraca 3.9 (K(ℓ) sub-exponencial), desfavorecendo a versão
forte 3.8 (K constante). A discriminação fina entre as formas de
crescimento lento (log ℓ vs. √ℓ vs. linear muito lento) permanece
matematicamente inacessível nesta faixa.

## Próximos passos (descartados por ora, custo/benefício desfavorável)

Estender além de ℓ=20 em Python puro tem custo explosivo (~3,3×/passo)
sem ganho de poder estatístico proporcional (a estatística de platôs
precisaria de ~10+ novos incrementos para mover o teste binomial de
forma decisiva). Se a linha for retomada no futuro, o passo certo é
reescrever o DP (bitset comprimido/vetorizado em C ou numpy) para
alcançar ℓ~30+ de uma vez, não estender incrementalmente em Python.

## Referências

- H-110/H-111/H-112 — a barreira de endogenia e sua conexão com a WCC.
- Wirsching (1998), Capítulo V (item 131 do INDEX), Corolário II.5.8,
  Definição V.1.1, Conjectura 3.9 (e a versão forte 3.8, p.138).
- `experiments/E-098-wirsching-weak-covering-test/experiment_wcc.py`.
