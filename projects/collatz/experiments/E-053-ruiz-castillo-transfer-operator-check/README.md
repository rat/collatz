# E-053 — Verificação do paper #013 (Ruiz Castillo, "Operador de Transferencia Residual")

## Objetivo

Verificar "Operador de Transferencia Residual de Ruiz Castillo y
teoría espectral para la dinámica acelerada de la Conjetura de
Collatz" (Juan Carlos Ruiz Castillo, 47 páginas). Quarto paper deste
autor revisado na coleção (após item 001/H-039, item 008/H-050, item
010/H-052). Introduz um operador de transferência formal L_t sobre o
espaço simbólico completo, depois motiva conjecturalmente uma versão
restrita L_{RC,t} sobre o espaço realizável Σ_C, usando teoria
espectral clássica (fórmula de Gelfand, Perron-Frobenius, brecha
espectral) para formular três conjecturas explícitas (Conjetura 6.6,
7.1, 8.4).

## Achado central — primeiro erro real nesta série de 4 papers

**Proposición 5.3 afirma `lim_{t→∞} L_t(1) = 0`**, mas sua própria
"Demostración" deriva a fórmula fechada de Proposición 5.1,
`L_t(1) = e^{(log₂3−1)t}/(1−e^{-t})`, e como log₂3−1 ≈ 0,585 > 0, essa
expressão **diverge exponencialmente** quando t→∞ — o oposto exato do
que a proposição afirma. O próprio texto reconhece isso na frase
seguinte ("crece exponencialmente cuando t → ∞"), mas o símbolo de fim
de demonstração (□) aparece logo depois, sem que o enunciado "= 0"
seja corrigido ou retirado.

Consultamos `advisor()` antes de finalizar este achado. Avaliação: o
cálculo está correto e a Proposición 5.3, como impressa, é de fato
falsa — mas a demonstração do próprio paper **deriva corretamente** o
comportamento assintótico (crescimento exponencial) e até usa essa
observação para justificar a necessidade de normalização futura via
"presión residual". O autor entendeu a assintótica; o defeito é que o
enunciado formal em caixa nunca foi atualizado para refletir a própria
demonstração. Isto é uma **inconsistência enunciado-vs-demonstração**
— mesma categoria do erro de rotulagem já encontrado em Pratiher
(H-037), **não** um erro de cálculo do autor. Por isso não vai para
`literature/unverified-proof-claims.md` (o paper não alega provar
Collatz).

## O que fizemos

1. **Proposición 5.1** (fórmula fechada de L_t(1)): confirmada —
   soma direta da série (5000 termos) bate com a fórmula fechada para
   t ∈ {0,1; 0,5; 1; 2; 5; 10}.
2. **Proposición 5.2** (positividade, L_t(1)>0 para t>0): confirmada.
3. **Proposición 4.2** (convergência absoluta): confirmada — diferença
   entre somas truncadas em 1000 e 2000 termos é ~0 para todo t testado.
4. **Proposición 5.3** (comportamento assintótico): **FALSA conforme
   impressa** — calculamos L_t(1) para t=1 até t=200: a sequência é
   estritamente **crescente** (2,84 → 6,4×10⁵⁰), não decrescente para 0.

## Contenção do erro

Confirmamos que a Proposición 5.3 é um cálculo preliminar da Seção 5,
sobre o espaço simbólico **irrestrito** (sem restrições aritméticas de
Collatz). Nenhum resultado posterior do paper (Seções 6-8, sobre o
operador **restrito** L_{RC,t} em Σ_C, todas explicitamente
conjecturais) cita ou depende do valor numérico de L_t(1). O erro não
compromete o restante do paper, que permanece honesto quanto ao seu
alcance: "los resultados obtenidos no constituyen una demostración de
la Conjetura de Collatz."

## Resultado

Primeiro erro real encontrado nos quatro papers Ruiz Castillo
revisados até agora (H-039, H-050, H-052 eram todos "elementares mas
corretos"). O restante do aparato (fórmula de Gelfand, positividade do
raio espectral, equivalência logarítmica) é matemática funcional
padrão, corretamente aplicada; as três conjecturas centrais (Conjetura
6.6, 7.1, 8.4) são honestamente rotuladas como conjecturas, não
teoremas.

Ver `hypotheses/H-053-ruiz-castillo-transfer-operator-review.md`.

## Como rodar

```
/home/rat/.venv/bin/python3 experiment.py
```
