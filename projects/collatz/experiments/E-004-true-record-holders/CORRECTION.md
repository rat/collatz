# Correção — erro de transcrição na análise mod-3 original

## O que aconteceu

Ao caracterizar o achado de H-004 (distribuição mod-3/mod-9 dos recordistas
reais), o script auxiliar usado para gerar o `Counter` continha uma lista de
57 números **digitada de memória**, não copiada da saída real do experimento.
Essa lista tinha 4 valores incorretos (1327403, 1493987, 1657647, 1901451 —
números que NÃO são recordistas reais; seus stopping times reais são 261, 62,
114 e 189 respectivamente, muito abaixo do recorde vigente na época, 524).

Isso é exatamente o tipo de erro que `literature/resources-and-tools.md` (lição
do paper de colaboração humano-LLM) alertava para evitar: "confiar sem
verificar". A lista foi reconstruída por aproximação em vez de vir da fonte.

## Verificação de que o código está correto

Antes de corrigir os dados, verificamos se havia um bug real em
`total_steps_only` ou na lógica de busca de recordistas (o que seria mais
grave, afetando outros experimentos). Reexecutamos o scan original até 4M e
comparamos termo a termo com a sequência oficial OEIS A006877 (fonte: dados de
Roosendaal, `http://www.ericr.nl/wondrous/delrecs.html`) — **bateu exatamente**.
O código está correto; o erro foi só na lista digitada manualmente depois.

## Correção aplicada

Baixamos a sequência completa e oficial (`oeis_A006877_record_holders.txt`,
148 termos, de 1 até ~1.47×10^19, fonte Roosendaal via OEIS) e refizemos a
análise mod-3/mod-9/mod-27 do zero com esses dados corretos e uma amostra
muito maior (148 em vez de 57). Ver resultados atualizados em `README.md`.

## Lição para o protocolo

Nunca reconstruir dados de memória para análise — sempre usar a saída real do
script (re-executar se necessário) ou uma fonte de dados salva no repositório.
Adicionado a `protocols/new-experiment.md`.
