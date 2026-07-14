# H-038 — Busca de estrutura não-linear (mutual information) além de H-025: real, mas genérica de aritmética de carry, não específica do Collatz

Status: refutada como estrutura nova (resultado negativo, com mecanismo
identificado e confirmado por experimento de controle)
Criada em: 2026-07-13
Origem: resposta de uma IA externa propondo "Project PHI" (embedding rico
de n + busca de estrutura) e um "campo vetorial" Δ(n)=Φ(T(n))-Φ(n). Já
identificado que a versão linear dessa ideia (Koopman/DMD) é redundante
com H-025 (`BACKLOG.md`: "DESCARTADO"). Este teste ataca a generalização
honesta: existe dependência NÃO-linear (não capturada por correlação
tipo Pearson) que H-025 poderia ter deixado passar?

## Diferença em relação a H-025

H-025 testou correlação linear bit-a-bit (`bit_i(n)` vs `bit_j(m)`).
Este teste usa **informação mútua** (captura qualquer dependência
estatística, linear ou não) entre um conjunto mais rico de features:
peso de Hamming, resíduos mod 5/7/9/11, janela de bits distante do
carry de baixa ordem (bits 10-13), byte alto (bits 17-24), e a
**segunda valuação a2** (v₂ do passo seguinte) — nenhuma dessas
combinações foi testada em H-025.

## Método

`experiments/E-038-nonlinear-embedding-clustering/experiment.py`:
400.000 n ímpares aleatórios em [2²⁴,2²⁵) (bit-length fixo, evita
confundir com efeito de magnitude). Para cada par de features
(uma de n, uma de m), calcula MI empírica condicionada em cada valor
fixo de a (1 a 6) e compara contra um null de embaralhamento (15
repetições) — só conta como sinal real se MI observada exceder muito o
que embaralhar produziria (z-score).

## Resultado bruto

**Há, sim, dependência real e estatisticamente muito robusta além do
que H-025 testou.** Dois grupos:

1. **Controle positivo esperado** (`mod_k(n)` vs `mod_k(n)` mesmo k):
   MI ≈ log2(k) ou log2(3) exatamente, z-score >10.000 em vários casos.
   Isso é **identidade algébrica trivial** — m=(3n+1)/2^a mod k é uma
   função afim exata de n mod k (bijetiva se mdc(3,k)=1; 3-para-1 se
   k=9, já que mdc(3,9)=3). Confirma que o método de MI funciona
   corretamente; não é achado novo, é o mecanismo já usado em
   H-007/H-008/H-022.

2. **Achado que precisava de explicação**: `hamming(n)` vs `hamming(m)`
   (peso de Hamming), e janelas de bits (`mid4_10_13`, `topbyte`) vs
   `hamming(m)` e vs `a2` — MI real muito acima do null (z até ~2448),
   com efeito de tamanho não-trivial (até 0,45 bits em alguns casos).

## Verificação do mecanismo (decisiva)

Confirmado computacionalmente, **exato, 0 exceções em 200.000 casos**:
`popcount(m) == popcount(3n+1)` sempre — dividir por 2^a só remove bits
zero à direita, não muda o peso de Hamming. Logo a dependência
observada é inteiramente sobre como `popcount(3n+1)` se relaciona com
`popcount(n)` — uma pergunta de **combinatória de carry em aritmética
binária**, não de dinâmica de Collatz especificamente.

**Experimento de controle (decisivo)**: substituí "3n+1" por
transformações sintéticas do mesmo tipo geral (multiplicador ímpar
qualquer + constante, condicionando na mesma valuação a=1):

| Transformação | MI(popcount(n); popcount(saída)) |
|---|---|
| 3n+1 (Collatz real) | 0,1332 |
| 5n+1 (controle) | 0,0350 |
| 7n+3 (controle) | 0,0385 |
| 9n+5 (controle) | 0,0262 |

**Todas as transformações de controle (que nada têm a ver com
Collatz) mostram o mesmo tipo de dependência não-nula.** Isso descarta
"é uma propriedade especial do 3n+1" como explicação — é uma
propriedade genérica de "multiplicar por ímpar, somar constante,
remover zeros à direita", que qualquer transformação desse tipo exibe
em algum grau, por causa de propagação de carry na adição binária.

Teste adicional: variando o multiplicador como 2^k+1 (k=1 é
exatamente o caso do Collatz, 3=2¹+1), a MI não decresce
monotonicamente com k (0,133 em k=1, cai para ~0,036 em k=2-3, sobe de
novo para 0,077 em k=6) — mostra que k=1 (nosso caso real) está dentro
de uma família mais ampla de comportamentos, não é um ponto
singularmente "mágico" do Collatz.

## Conclusão

**Não há invariante novo específico do Collatz.** A dependência
não-linear encontrada é real (H-025 não a capturaria, já que é
agregada/de peso de Hamming, não bit-a-bit) mas **generaliza para
qualquer transformação afim ímpar semelhante** — é a mesma classe de
fenômeno que H-025 já identificou como "propagação clássica de carry
em adição binária", só visível por um ângulo diferente (estatística
agregada em vez de pares de bits individuais). Isso **estende e reforça
H-025** por um método genuinamente diferente (MI não-linear + conjunto
de features mais rico), em vez de contradizê-lo.

**Sobre "Project PHI"/o "campo vetorial" Δ(n) da IA externa**: mesmo
generalizando para não-linearidade (o que a formulação original não
especificava), a ideia continua sem produzir estrutura nova — o
"campo" de deslocamento em qualquer embedding razoável (bits, pesos,
resíduos) está inteiramente explicado por mecanismos aritméticos já
catalogados, não por uma geometria escondida do Collatz.

**Contribuição metodológica reaproveitável**: o experimento de
controle (comparar a transformação real contra transformações
sintéticas do mesmo tipo geral, com outros multiplicadores ímpares) é
uma forma limpa e barata de testar "isso é específico do Collatz ou
genérico de aritmética binária?" — vale reusar em hipóteses futuras
antes de reportar qualquer "estrutura" encontrada em features de n vs
m.

## Atualizações

- 2026-07-13: testado, achado real confirmado, mecanismo identificado
  e validado por experimento de controle com transformações sintéticas.
