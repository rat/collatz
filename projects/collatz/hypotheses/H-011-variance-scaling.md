# H-011 — A variância residual de H-010 é ruído previsto, não estrutura escondida

Status: confirmada (coeficiente empírico 181.53 vs teórico 186.93, diferença 2.9%)
Criada em: 2026-07-13

## Contexto

H-010 confirmou que total_stopping_time(n) ≈ K·log₂(n) com K≈7.23 (dentro de
0.62% dos dados), mas achou R²=0.03 — log₂(n) sozinho explica pouquíssimo da
variância individual. Isso ficou registrado como pergunta em aberto: essa
variância vem de estrutura fina ainda não encontrada, ou é só o ruído
esperado do próprio processo estocástico?

## Enunciado

Propomos que a variância é majoritariamente ruído previsto pela própria
heurística de passeio aleatório — não evidência de estrutura escondida. Se a
heurística estiver certa, Var(total_stopping_time(n)) deveria crescer
linearmente em log₂(n) (não em log₂(n)², que seria o caso se o "erro relativo"
fosse constante) — e com um coeficiente específico derivável.

## Derivação

Cada passo acelerado contribui X_i = log₂3 − a_i para a mudança em log₂(n)
(deriva μ = E[X] = log₂3−2 ≈ −0.41504, variância σ² = Var(a) = 2, pois a_i
segue Geométrica(p=1/2)). O número de passos acelerados T até cruzar a
barreira −log₂(n) é um tempo de primeira passagem de um passeio aleatório com
deriva — pela aproximação de difusão (distribuição Gaussiana Inversa):

Var(T) ≈ σ²·log₂(n) / |μ|³ ≈ 27.97 · log₂(n)

Como cada passo acelerado consome Y_i = 1+a_i = c−X_i passos padrão (com
c=1+log₂3), e essa relação é exatamente linear em X_i, temos
total_stopping_time(n) ≈ c·T + log₂(n), logo:

Var(total_stopping_time(n)) ≈ c²·Var(T) ≈ **186.93 · log₂(n)**

Ou seja: desvio padrão ≈ 13.67·√(log₂n) — cresce como raiz quadrada de
log₂(n), bem mais devagar que a própria média (que cresce linear em log₂n).
Isso já prevê R² baixo mesmo sem nenhuma estrutura escondida: a razão
sinal-ruído (desvio padrão / média) cai como 1/√(log₂n), mas para os n
testados (log₂n ~ 20), ainda é grande o suficiente (~40% da média) para
produzir R² pequeno.

## Como testar

Calcular total_stopping_time(n) para uma amostra grande, dividir em faixas de
log₂(n), calcular a variância empírica dentro de cada faixa, e comparar o
coeficiente angular (variância vs. log₂n) com o valor teórico 186.93.

## Atualizações

- 2026-07-13: hipótese aberta, derivação teórica registrada.
- 2026-07-13: testada em `experiments/E-011-variance-scaling/` — amostras em
  8 níveis de magnitude (log₂n de 10.5 a 45.5, usando inteiros grandes
  nativos). Coeficiente empírico da regressão Var~coef·log₂n = 181.53 vs.
  teórico 186.93 (diferença 2.9%). Confirma que a variância residual de
  H-010 é ruído previsto pela heurística de passeio aleatório, não estrutura
  escondida — resolve a pergunta em aberto que H-010 tinha deixado.
