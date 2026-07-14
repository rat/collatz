# E-044 — Verificação do paper #018/019 (Fu, Liu & Wang — Gamma/Poisson)

## Objetivo

Verificar de forma independente o paper "Emergence of Gamma-Type
Upward-Phase Statistics in the Collatz Map: An Effective Poisson
Process Mechanism" (Fu, Liu & Wang, arXiv:2606.26811) — item 019 do
`INDEX.md` (arquivo local numerado `018_...pdf`, um dos 15 baixados).
Diferente do CTUHSK (H-043), **este paper não alega provar a
conjectura** — propõe um mecanismo heurístico (processo de Poisson +
valuação 2-ádica geométrica) para explicar por que N↑ (número de passos
de Syracuse até atingir 1) segue aproximadamente uma distribuição
Gamma.

## O que fizemos

1. Confirmamos E[h]=2, Var(h)=2 para a valuação 2-ádica (já estabelecido
   em H-001/H-011 — ponto de calibração).
2. Testamos a Eq.6 do paper (fórmula fechada aproximada ligando N↓ a
   X0 e N↑, herdada da ref.[19] do mesmo grupo) contra o N↓ exato
   simulado, para todo X0 ímpar de 3 a 200.001 — incluindo a órbita
   classicamente longa de X0=27 (41 passos acelerados).
3. Reproduzimos (em escala bem menor que o paper: L=10⁴ e 10⁵ vs
   10⁵–10¹⁵ deles) a verificação central — média e variância empíricas
   de N↑ comparadas às previsões teóricas θ_T=2/(2−log₂3)² e
   K_T=(2−log₂3)/2·(1+log₂L).
4. Conferimos manualmente, termo a termo, a álgebra da condição de
   fechamento de ciclos (Eqs.30-34).

## Resultado

- **Eq.6 bate exatamente em 99999/99999 (100%) dos casos testados**,
  inclusive X0=27 — nossa hipótese inicial de que a aproximação
  quebraria em órbitas longas estava errada; a fórmula é mais robusta
  do que esperávamos.
- **Média de N↑** bate com a previsão corrigida (Eq.37) a ~2% em
  L=10⁴ e 10⁵ — mesma ordem de precisão relatada pelo próprio paper.
- **θ empírico (~10.6) fica ~8,5% abaixo de θ_T=11,61** nessas escalas.
  Isso **não é um erro do paper** — o próprio paper mostra que θ só se
  aproxima do valor teórico lentamente conforme L cresce, e mesmo em
  L=10¹⁵ o valor ajustado (11,245) ainda fica ~3% abaixo do teórico.
  Como não temos orçamento computacional para replicar L=10¹⁵, um gap
  maior nas nossas escalas menores é o esperado, na direção correta —
  confirmação com escopo honestamente limitado, não uma discrepância.
- **Álgebra da condição de fechamento de ciclos (Eqs.30-34) está
  correta** — verificamos cada passo da derivação manualmente.
  Diferente do CTUHSK (H-043), este paper é **explícito e correto** ao
  afirmar que essa obstrução assintótica NÃO prova a inexistência de
  ciclos não-triviais — reconhece textualmente que a correção finita
  1/Xn não pode ser descartada rigorosamente.

**Nenhum erro encontrado.** Ver
`hypotheses/H-044-fu-liu-wang-gamma-poisson-review.md`.

## Como rodar

```
/home/rat/.venv/bin/python3 experiment.py
```

Sem dependências externas (apenas `math` e `collections` da biblioteca
padrão — não usamos scipy, que não está instalado no venv do projeto;
o ajuste de Gamma foi feito por método dos momentos, suficiente para
comparar com as previsões teóricas do próprio paper).
