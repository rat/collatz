# E-004 — Recordistas reais de stopping time

Hipótese relacionada: [`H-004-true-record-holders.md`](../../hypotheses/H-004-true-record-holders.md)

> **⚠️ Correção (2026-07-13)**: a versão original deste experimento usou uma
> lista de recordistas parcialmente incorreta (digitada de memória em vez de
> vinda da saída real do script — ver [`CORRECTION.md`](CORRECTION.md)). O
> código de busca de recordistas (`experiment.py`) estava correto; o erro foi
> só na lista usada na caracterização mod-3/mod-9 depois. A análise abaixo usa
> a sequência oficial e completa (OEIS A006877, 148 termos, fonte Roosendaal) e
> **substitui** a conclusão anterior — o achado ficou mais forte, não mais
> fraco, com dados corretos.

## O que foi testado

Recordistas reais (n tal que total_stopping_time(n) supera todo m < n) e sua
estrutura residual mod 3 / mod 9 / mod 27, usando a sequência oficial e
completa de Roosendaal/OEIS A006877 (148 termos, de n=1 até
~1.47×10^19 — muito além do que dá para escanear em Python puro neste
ambiente). Arquivo de dados: `oeis_A006877_record_holders.txt`. Reproduzir:
`python3 experiment_v2_oeis_verified.py`.

Também testamos, separadamente, (b) autocorrelação lag-1 interna da órbita de
cada recordista (ver seção própria abaixo) — essa parte não foi afetada pelo
erro de transcrição, pois usava o scan real (até 20-50M) diretamente.

## Resultado (a) — resíduo, com dados corretos e completos

| módulo | classes com 0 ocorrências | chi2 | dof | p |
|---|---|---|---|---|
| 3  | nenhuma | 76.39  | 2  | 5.2×10⁻¹⁴ |
| 9  | {4, 5, 8} | 118.11 | 8  | 3.2×10⁻¹⁹ |
| 27 | {4,5,8,11,13,14,17,20,22,23,26} | 174.54 | 26 | 1.8×10⁻²² |

Distribuição mod 3: **85 recordistas ≡0, 62 ≡1, apenas 1 ≡2** (esperado
uniforme: ~49.3 cada). O único caso ≡2 mod 3 é **n=2** — um recordista trivial
(órbita de 1 passo). **Excluindo esse caso de borda, 0 dos 147 recordistas
restantes são ≡2 mod 3.**

Em mod 9, as classes 4, 5 e 8 (todas ≡2 mod 3) nunca ocorrem — consistente com
o achado mod-3. Em mod 27, 11 das 27 classes nunca ocorrem.

### Por que isso não é tautológico

Como discutido em H-005 (`experiments/E-005-mod3-valuation-parity/`), existe um
lema provado que liga resíduo mod 3 de **termos subsequentes** de uma órbita à
paridade da valuação daquele passo — mas esse lema não se aplica ao número
**inicial** de uma órbita (não há "passo anterior" para ele). O viés
encontrado aqui é sobre o número inicial (o próprio recordista), então H-005
não o explica automaticamente. Continua sendo um padrão empírico genuíno e
muito bem verificado, mas sem explicação mecanicista completa ainda.

### O que descartamos ao longo do caminho (importante para não repetir)

Tentamos replicar esse achado usando "top-K por valor bruto de stopping time"
em vez de recordistas estritos (`experiments/E-006-topk-stopping-time-mod3/`)
e não vimos o mesmo viés. Investigando por quê, descobrimos que essas são
**populações diferentes**: muitos números do "top-K bruto" nunca bateram
recorde algum (só têm valor coincidentemente alto). Isso não refuta o achado —
só mostra que "recordista estrito" é uma noção mais restritiva e especial do
que "está entre os valores mais altos", e o viés mod-3 parece ser específico
de recordistas estritos.

## Resultado (b) — autocorrelação interna, com controle de confounder

(Esta parte não foi afetada pelo erro de transcrição.)

Primeira rodada (sem controle): recordistas com autocorrelação lag-1 média
0.076-0.106, típico 0.038-0.046, diferença "significativa" (p ~0.001-0.0001).

Identificamos um confounder: recordistas têm órbitas sistematicamente mais
longas (média 149 passos vs 73 do grupo típico filtrado), e a estimativa de
autocorrelação amostral tem viés conhecido dependente do comprimento da série
(~-1/(L-1) para séries i.i.d. curtas). Controlando via regressão ajustada no
grupo típico, o resíduo médio dos recordistas caiu para 0.023 (p=0.053) — **não
significativo** no corte de 0.01 usado no projeto. A diferença "ingênua" era
majoritariamente explicada pelo viés de comprimento de amostra curta.

## Status de H-004

- Autocorrelação interna: **não suportada** (não sobrevive ao controle de
  confounder).
- **Estrutura residual mod-3/9/27 dos recordistas: achado forte e robusto**,
  agora verificado com dados oficiais completos (n=148, p < 10⁻¹³ em todos os
  módulos testados). Sem explicação mecanicista completa ainda — candidato
  genuíno para investigação teórica futura.
