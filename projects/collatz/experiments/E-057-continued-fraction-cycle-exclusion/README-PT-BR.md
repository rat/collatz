# E-057 — Frações contínuas de log₂(3) e exclusão de ciclos

Hipótese relacionada: [`H-057-continued-fraction-cycle-exclusion.md`](../../hypotheses/H-057-continued-fraction-cycle-exclusion.md)

## Origem

Candidato #1 da lista "candidatos ainda não implementados" do
`BACKLOG.md` (seção 6): conectar a técnica clássica de exclusão de
ciclos (Steiner/Simons/de Weger/Hercher, via frações contínuas de
log₂(3)) com nosso próprio muro combinatório (H-009/H-034).

## O que foi testado

1. **Fração contínua de log₂(3)** (45 termos) + convergentes plenos +
   **semiconvergentes** (necessários porque este é um problema de
   aproximação unilateral — precisamos `S > a·log₂(3)` estritamente,
   não só `|S/a − log₂(3)|` pequeno; convergentes plenos sozinhos dão
   uma lista esparsa demais, com saltos enormes entre `a=1,5,41,306,...`).
2. **Checagem real de autoconsistência** (reaproveitando `compositions`/
   `candidate_n0`/`check_self_consistency` de E-034, sem reimplementar)
   nos candidatos `(a,S)` dentro do nosso alcance computacional
   (`a=3,5,17`), no `S` exato do convergente/semiconvergente.
3. **`n0_min` em forma fechada**: `(3^a−2^a)/(2^S−3^a)`, para a
   composição `(1,1,...,1,S-a+1)` — confirmada por enumeração exaustiva
   (a=3,5,17) como a que minimiza `n₀` entre todas as composições de
   `S` em `a` partes.
4. **Custo combinatório** `C(S-1,a-1)` para os candidatos além do nosso
   alcance, até e além do bound atual da literatura (`a=91`, Hercher
   2023, arXiv:2201.00406 — atualização de "a≤68" que estava desatualizado
   em nossas notas, verificada via WebSearch/WebFetch antes de escrever
   o código).

## Resultado

Nenhum ciclo novo. Para `a=3,5,17`: mais forte que "nenhum
autoconsistente" — **nenhuma composição produz sequer um `n₀` inteiro
positivo** (falha na própria condição de divisibilidade, para as 6 / 35
/ 5.311.735 composições testadas). Subconjunto do que H-034 já cobria
(mesmo `S`, dentro da janela `S_min..S_min+20`), não uma checagem
adicional.

Para `a=29,41`: fora do nosso alcance (`C(S-1,a-1)` ~10¹²/~10¹⁷), mas já
excluídos por Simons & de Weger (2005, `a≤68`). Para `a=94` em diante:
território aberto (além de Hercher 2023, `a≤91`) — não resolvido nem por
nós nem, até onde verificamos, pela literatura.

## Correção de interpretação (via `advisor()`, antes de finalizar)

A primeira versão deste experimento afirmava que **menor excesso
`L(a,S)=S−a·log₂(3)` implica menor `n₀` possível**, e por isso rotulava
`a=29,41` como os candidatos mais "perigosos". **Invertido**: para a
composição minimizadora, `n0_min ≈ 1/(L·ln2)` — menor excesso implica
`n0_min` **maior**. Verificado numericamente (Parte 2b do script):
`n0_min` cresce de 3,8 (`a=3`) a ~1069 (`a=1636`) conforme `L` encolhe.
Mas isso é só o mínimo sobre composições — o `n₀` de uma composição
"ruim" (valuações grandes no início) para o mesmo par `(a=306,S=485)`
chega a ~4,5×10²⁵, contra `n0_min≈978`. `L(a,S)` pequeno mede
dificuldade **analítica** de exclusão (cotas de Baker), não o tamanho de
um eventual ciclo. Ver `H-057` para a análise completa desta correção.

## Como reproduzir

```
python3 experiment.py
```

Sem dependências além de `mpmath`. Roda em bem menos de um minuto
(maior custo: checagem exaustiva de `a=17`, ~13s para 5.311.735
composições).
