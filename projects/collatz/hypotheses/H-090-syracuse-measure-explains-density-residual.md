# H-090 — A medida de Syracuse μ em ℤ₃ (Tao 2022, Lemma 1.12) explica G(v)=D(v)·v com correlação forte e crescente

Status: confirmada, resultado fortalecido em H-091 (correlação log-log inicial 0,92–0,98; com o headroom corrigido, converge a proporcionalidade quase exata — ver H-091)
Criada em: 2026-07-16
Origem: implementação da "ideia 2" proposta pelo modelo Fable (medida de
Syracuse μ em ℤ₃) numa consulta anterior desta sessão, depois de H-086/
H-087 mostrarem que G(v)=D(v)·v tem continuidade 3-ádica real. Antes de
implementar, o Fable foi consultado para validar a montagem matemática
exata (ver conversa completa) — ele apontou que minha primeira tentativa
de montagem (transição direta no espaço de resíduos mod 3^K) tinha um
erro estrutural, e forneceu a recursão correta, que é **exatamente a
mesma equação do Lemma 1.12 de Tao (2022)** — já implementada e
verificada neste projeto em H-076/E-076 para a variável aleatória
Syrac(ℤ/3ⁿℤ).

## A conjectura testada

O Fable propôs que G(v) — o resíduo 3-ádico de D(v) depois de remover
o termo trivial de magnitude D(v)≈C/v (H-086) — é bem aproximado pela
densidade local de uma medida μ em ℤ₃, definida pela mesma recursão de
auto-consistência que rege Syrac(ℤ/3ⁿℤ) no framework de Tao:

μ_m(r) = Σ_{a: 2^a·r≡1 mod 3} 2^{-a}·μ_{m-1}((2^a·r-1)/3 mod 3^{m-1}) / normalização

## Implementação

`experiments/E-090-syracuse-measure-vs-density/experiment.py`:
1. Reaproveitada e validada a função `syrac_distribution` já escrita
   em E-076 (verificada contra os valores exatos do Lemma 1.12 de Tao:
   8/63, 16/63, 11/63, 4/63, 2/63, 22/63 para m=2).
2. Escrita uma versão truncada em ponto flutuante
   (`syrac_distribution_float`, a≤64) para escalar a m maior sem o
   custo de `Fraction` exato — validada contra a versão exata: **erro
   0,00 (m=1,2) e ~2,8×10⁻¹⁷ (m=3)**, confirmando que a truncagem não
   introduz erro perceptível.
3. Medido G(v) computacionalmente (via `build_tree_count_dfs`, já
   validado em E-018) para muitos v com resíduo fixo mod 3^m,
   magnitude controlada (log₁₀v ∈ [5,6)), e comparada a média
   geométrica de G(v) por classe residual com 3^m·μ_m(r).

## Resultado

**Correlação log-log entre 3^m·μ_m(r) e a média de G(v) por resíduo**,
crescendo consistentemente com m:

| m | correlação log-log |
|---|---|
| 2 | 0,916 |
| 3 | 0,969 |
| 4 | 0,980 |

**Estabilidade confirmada em 5 sementes aleatórias independentes**
(m=3: 0,947–0,988; m=4: 0,968–0,981) — não é coincidência de uma
amostra específica.

## Interpretação

A conjectura do Fable se confirma com evidência forte: **G(v) é
descrito, com correlação alta e crescente, pela densidade local de uma
medida μ em ℤ₃ construída via a mesma recursão de auto-consistência do
Lemma 1.12 de Tao** — a mesma variável aleatória de Syracuse já
catalogada na literatura mais rigorosa sobre a conjectura, agora
conectada a um objeto novo deste projeto (a densidade da subárvore
reversa de Collatz). Isso dá uma caracterização substancialmente mais
rica que "ruído genérico" para a variância residual de D(v): não é uma
fórmula fechada (μ ainda não tem forma fechada finita, é ela mesma uma
recursão infinita), mas é uma **medida explícita, computável e com
interpretação probabilística clara** (a lei assintótica dos iterados de
Syracuse, sob a heurística padrão de valuações i.i.d. Geométrica(1/2)),
não apenas "sabemos que oscila".

## O que ainda não foi feito

- A correlação, embora alta, não é 1,0 — não testamos se ela continua
  subindo para m>4 (o custo computacional de medir G(v) com baixo
  ruído por classe residual cresce com o número de classes, 3^m).
- Não testamos se a relação é de **proporcionalidade exata** (mesma
  constante multiplicativa para todo v) ou apenas correlação — um
  próximo passo natural seria ajustar essa constante e medir o resíduo
  restante.
- A montagem exata desta recursão foi validada pelo Fable antes de
  implementar (evitando um erro estrutural que eu mesmo tinha proposto
  inicialmente) — mas a interpretação probabilística completa de por
  que essa medida específica deveria descrever a árvore reversa de
  Collatz (não só a órbita direta de Syracuse, que é o que Tao estuda)
  ainda é heurística, não uma prova formal da conexão.

## Atualizações

- 2026-07-16: consulta ao Fable validou a montagem matemática antes de
  implementar (identificou e corrigiu um erro estrutural na minha
  proposta inicial). Implementado, validado contra os valores exatos
  já verificados em E-076, e testado contra G(v) medido
  computacionalmente. Correlação log-log forte e crescente com m
  (0,916→0,980), estável em 5 sementes independentes. Confirma a
  conjectura do Fable com evidência real, não apenas plausibilidade.
- 2026-07-16 (ver H-091): as três perguntas da seção "o que ainda não
  foi feito" acima foram respondidas. A correlação não continuava
  subindo para m>4 com o método original — na verdade DEGRADAVA até
  m=12 (0,998→0,973). Investigação (com crítica dura do Fable)
  encontrou a causa: `measure_G` usava headroom fixo (`n_max=v*20`),
  insuficiente para resolver resíduos finos, mais um viés secundário da
  média geométrica usada. Corrigido (headroom 200-2000, média
  aritmética): a correlação **sobe monotonicamente até m=14** (não
  degrada mais) e o expoente ajustado **converge a ~1,00 exato** — não
  é só correlação forte, é proporcionalidade quase exata. Ver H-091
  para a investigação completa e os números.
