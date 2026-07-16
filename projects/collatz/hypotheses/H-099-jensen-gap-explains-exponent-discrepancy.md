# H-099 — O termo de Jensen explica exatamente (por identidade) a diferença entre b agregado e b por-v; mas revela um novo enigma: a forma da distribuição de G varia ~46× entre classes

Status: confirmado (identidade algébrica verificada) — mas revela um
novo achado empírico não explicado (variação extrema da dispersão
intra-classe)
Criada em: 2026-07-16
Origem: sugestão #1 de uma IA externa consultada com prompt de
contexto completo sobre a linha H-024→H-091 (ver
`density-3adic-obstruction-synthesis.md` e H-091). A IA propôs que a
discrepância entre o expoente b~1,00 (teste agregado por classe,
H-091 Parte 1) e b~0,96-0,98 (teste por-v individual, H-091 Parte 2)
seria efeito da desigualdade de Jensen.

## O teste

`experiments/E-090-syracuse-measure-vs-density/experiment_jensen.py`:
M=8 (mod 3⁸=6561), headroom=2000, 500 classes residuais amostradas,
150 v's por classe. Para cada classe r, calculado:
- log(E[G|r]) — log da média aritmética (estatística do teste agregado)
- E[log G|r] — média do log (estatística latente do teste por-v)
- gap(r) = log(E[G|r]) − E[log G|r] (termo de Jensen, sempre ≥0 pela
  desigualdade de Jensen para função côncava log)

## Resultado

| estatística | valor |
|---|---|
| b (log da média agregada vs log μ) | 0,9968 (corr 0,9964) |
| b (média do log vs log μ, "por-v latente") | 0,9735 (corr 0,9984) |
| diferença dos b's | 0,0233 |
| inclinação de gap(r) vs log(μ_r) | 0,0232 |
| corr(gap, log μ) | 0,2995 |
| gap(r): média / desvio / min / max | 0,1176 / 0,0835 / 0,0266 / 1,2195 |

**A diferença entre os dois expoentes é EXATAMENTE (não aproximadamente)
a inclinação do termo de Jensen contra log(μ)** — isso é uma identidade
algébrica forçada pela definição de gap(r), não uma coincidência
empírica: como log(E[G|r]) = E[log G|r] + gap(r), regredir cada lado
contra log(μ_r) força slope_agregado = slope_por-v + slope(gap). A
sugestão da IA está formalmente correta, mas é quase tautológica — não
resolve o mistério, só o reformula.

## O achado novo e genuíno

**gap(r) varia por um fator de ~46× entre classes** (0,027 a 1,22 dex).
Isso significa que a FORMA da distribuição condicional de G(v) dado o
resíduo — não só sua média — muda drasticamente de uma classe para
outra: algumas classes têm G(v) concentrado (gap pequeno, distribuição
quase degenerada/log-normal de baixa variância), outras têm cauda
pesada o suficiente para que a média aritmética fique até ~16× acima
do valor típico (gap=1,22 dex ⟹ razão e^{1,22·ln10}≈16,6×). Isso é
exatamente o tipo de heterogeneidade que sustentaria a hipótese mais
ampla da IA (estrutura multifractal real na árvore), mas **ainda não
identificamos o que determina, para uma classe r específica, se ela
terá gap pequeno ou grande** — a correlação com log(μ_r) é real mas
modesta (0,30), longe de explicar toda a variação do gap.

## O que ainda não foi feito

- Calcular o espectro multifractal completo (função de partição
  Z(q)=Σ G(v)^q por classe, ver se τ(q) é côncavo) — sugestão original
  da IA, ainda não implementada.
- Identificar covariáveis que expliquem POR QUE gap(r) varia tanto
  entre classes (candidatos das outras sugestões da IA: resíduo
  cruzado mod 2^K, distância até a primeira ramificação na árvore).

## Referências

- H-091 (Parte 1 e 2) — os dois testes cuja discrepância motivou esta
  hipótese.
- Experimento: `experiments/E-090-syracuse-measure-vs-density/experiment_jensen.py`.
