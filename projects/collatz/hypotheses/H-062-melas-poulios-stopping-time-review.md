# H-062 — Revisão do paper #031 (Melas & Poulios, "Predicting Extreme Stopping Time Behavior") — paper estatístico peer-reviewed, base empírica confirmada exatamente

Status: revisão externa concluída — identidade fundamental e as 6
estimativas de densidade citadas confirmadas exatamente; modelos
preditivos (logit/árvore) não reproduzidos byte-a-byte (dependem de
amostragem aleatória sem gerador/semente totalmente especificado)
Criada em: 2026-07-15
Origem: item 031 da coleção (`literature/papers/INDEX.md`), já baixado
(`031_Predicting-Extreme-Stopping-Time.pdf`).

## O paper

Melas, E. & Poulios, N.C. (2026), *Predicting Extreme Stopping Time
Behavior in the Collatz System: A Probabilistic and Statistical
Approach*, Journal of Dynamics and Games (AIMS), **peer-reviewed**
(recebido, revisado, publicado com DOI). Departamento de Economia,
Universidade Nacional e Kapodistríaca de Atenas.

Paper **estatístico/preditivo**, não alega provar Collatz — explícito
na conclusão: *"These results do not solve the Collatz conjecture and
do not establish a new density theorem."* Constrói dois modelos logit
e uma árvore de decisão (CART) para **prever** (não provar) se um
inteiro `n` tem tempo de parada normalizado extremo (`Rs(n)=s(n)/log₂n
≥ 7`), usando variáveis substitutas: o tempo de parada de um "sistema
Collatz modificado" `Col_mod` (convergência mais regular, sem o outlier
n=27) e defasagens locais `Rs(n-1), Rs(n-2), Rs(n-3)`.

## Definição exata usada pelo paper (importante, difere de outras revisões desta coleção)

`Col(n) = n/2` (par), `(3n+1)/2` (ímpar) — **um mapa diferente** do
mapa acelerado `T(n)` usado em outras revisões desta coleção: aqui só
**uma** divisão por 2 é embutida no passo ímpar, não todas as
divisões até voltar a ímpar. Isso muda a contagem de `s(n)` — foi
necessário implementar `Col` exatamente como definido, não reciclar o
`T(n)` de experimentos anteriores.

## O que foi verificado

`experiments/E-062-melas-poulios-stopping-time-check/experiment.py`,
quatro partes:

1. **Identidade logarítmica exata** (Eq. 3: `Log₂(n) = s(n) −
   Log₂(3)d(n) − Σ Log₂(1+1/(3o_i))`) — verificada via `Fraction`
   (sem ponto flutuante) para 300 valores aleatórios de `n`. 0 falhas.
2. **Exemplo numérico específico** (`n=10`: `s(10)=5, d(10)=1`, Eq. 4
   com o valor explícito `Log₂(5·32/16)=Log₂(10)`) — reproduzido
   exatamente.
3. **Sanidade do mapa Collatz modificado** `Col_mod` (Seção 3) — bem
   definido (produz inteiro para todo `n`) e preserva `{1,2}` como
   único ciclo, testado para `n=2..200.000`. 0 exceções.
4. **Reprodução EXATA e determinística das 6 janelas de densidade**
   citadas nas Figuras 7 e 8 — **censo completo** (não amostra) de
   10.000 inteiros consecutivos a partir de cada âncora, sem nenhuma
   semente aleatória envolvida:
   - Potências de 10: `[10⁶,+10⁴]`→1059, `[10⁸,+10⁴]`→937,
     `[10¹⁵,+10⁴]`→51.
   - Potências de 3: `[3¹³,+10⁴]`→1692, `[3¹⁸,+10⁴]`→531,
     `[3³⁰,+10⁴]`→1145.
   - **Todas as 6 contagens batem exatamente** com os valores citados
     no paper, incluindo a janela em `10¹⁵` (requer computar `s(n)`
     para 10.000 inteiros de 16 dígitos — tratável, cada órbita
     converge em algumas centenas de passos).

## Resultado

**Base empírica e identidades fundamentais confirmadas sem exceção.**
A reprodução exata das 6 contagens de densidade (Parte 4) é
particularmente forte: são censos completos e determinísticos (sem
depender de nenhuma amostragem aleatória), e todas batem precisamente
— incluindo a janela mais extrema (`10¹⁵`), que exige computar tempos
de parada para inteiros de 16 dígitos.

## Escopo não coberto (não é uma falha do paper, é uma limitação de reprodutibilidade)

Os coeficientes específicos dos dois modelos logit (Tabelas 1 e 6) e
da árvore de decisão (Tabela 13) dependem de amostragem aleatória
balanceada. A árvore de decisão dá uma semente explícita (`20250414`),
mas não especifica linguagem/biblioteca de geração de números
aleatórios — a mesma semente numa implementação diferente (Python
`random` vs. NumPy vs. R, por exemplo) produziria uma amostra
diferente. Os Modelos 1 e 2 (Seções 5-6) não mencionam nenhuma
semente. **Não é possível reproduzir os coeficientes exatos sem o
código/dados originais** (disponíveis mediante solicitação ao autor,
per prática declarada no paper). A metodologia estatística em si
(logit balanceado, validação multi-escala, CART com Gini) é sólida e
padrão — nenhum problema aparente nela, só não é byte-a-byte
reproduzível aqui.

## Por que isso é uma revisão positiva, não uma crítica

Diferente da maioria dos papers "amadores" desta coleção, este é
peer-reviewed, metodologicamente cuidadoso, com todas as alegações
verificáveis (identidade matemática, exemplo numérico, e — o mais
importante — as contagens de densidade empíricas específicas)
batendo exatamente. A limitação de reprodutibilidade dos modelos
estatísticos é uma questão de prática de publicação (semente/código
não totalmente especificados), comum na literatura, não um erro.

## Novas hipóteses?

Nenhuma concreta. Nota de interesse: o achado de forte **clustering**
não-uniforme de inteiros com `Rs(n)>7` (coeficiente de variação >1,37
entre 200 janelas Monte Carlo, variando de 0% a 36% em janelas de
10.000 inteiros) é consistente com o padrão geral já observado neste
projeto de que propriedades "raras" do Collatz tendem a se agrupar
localmente (via estrutura da árvore reversa) em vez de se distribuir
uniformemente — relevante para a síntese final se universos de
"raridade correlacionada" forem discutidos.

## Atualizações

- 2026-07-15: paper lido por completo (29 páginas), 4 partes
  verificadas computacionalmente, incluindo reprodução exata das 6
  contagens de densidade específicas do paper. `INDEX.md` atualizado
  (item 031: Lido=Sim, Corrigido=Sim [nada a corrigir], Implementado=Sim).
