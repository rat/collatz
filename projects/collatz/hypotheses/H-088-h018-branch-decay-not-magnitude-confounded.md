# H-088 — A obstrução de H-018 (decaimento entre galhos, 73×–680×) NÃO é o mesmo confound de magnitude de H-024; reforça a conclusão original

Status: confirmada (resultado negativo — a suspeita não se aplica; reforça H-018 em vez de corrigi-lo)
Criada em: 2026-07-16
Origem: consulta ao Fable pedindo revisão metodológica de H-026 (a
mesma variável de confusão de H-024/H-086). Como terceira pergunta,
pedimos que ele apontasse outras hipóteses da linha H-013/H-018/H-024
com suspeita do mesmo padrão. Ele apontou a "taxa de decaimento entre
galhos férteis" de H-018 (documentada como variando de 73× a 680×,
atribuída a "resíduos mod 27, 81... arbitrariamente profundos") como
candidata forte: como os galhos crescem geometricamente (~4× por
posição na cadeia de duplicação), o Fable suspeitou que grande parte
dessa variação fosse o mesmo termo trivial de magnitude já identificado
em H-024→H-086, e que, recomputada sobre G(w)=D(w)·w em vez de D(w)
bruto, a variação de 73×-680× "deveria colapsar substancialmente".

## O teste

`experiments/E-088-h018-magnitude-check/experiment.py`: reaproveitando
os dados de decomposição por galho já extraídos (`experiment_decompose.py`
de E-018) para t=10, 13, 16, 17, calculamos, para todos os 18 pares
disponíveis de galhos "mesma fase, 3 posições de distância" (w_i, w_{i+3}):
a razão bruta D(w_i)/D(w_{i+3}) (proporcional a contrib_i/contrib_{i+3},
já que ambos usam o mesmo n_max), o termo trivial esperado
w_{i+3}/w_i, e o resíduo depois de dividir a razão bruta pelo termo
trivial.

## Resultado

**O termo `w_{i+3}/w_i` é exatamente 64 em todos os 18 pares testados**
(64,000000 a 64,000045 — a variação residual é só arredondamento de
ponto flutuante). Isso é esperado algebricamente: cada galho sucessivo
cresce por um fator ~4 (a cadeia de duplicação 2^g·J_t multiplicada por
4 a cada novo galho), então 3 posições de distância sempre dá
4³=64 exatamente, **sem variar entre pares**.

Consequência estatística direta: dividir 18 valores por uma **constante
fixa idêntica** (64 em todos os casos) desloca a média geométrica, mas
**não muda a dispersão**. Confirmado numericamente: desvio-padrão de
log₁₀ da razão bruta = **0,5674 dex**; desvio-padrão do resíduo depois
de "corrigir" pelo termo trivial = **0,5674 dex** — idêntico até a 4ª
casa decimal.

## Interpretação

A suspeita do Fable, testada diretamente, **não se sustenta neste
caso específico** — e por um motivo estrutural claro: em H-024/H-026,
a magnitude v variava **livremente** por ordens de grandeza diferentes
entre os pontos comparados (v de 85 a 72.985 em H-024, um fator
não-controlado de ~860×), permitindo que ela se disfarçasse de
"estrutura 3-ádica". Aqui, a distância "3 posições na cadeia de
duplicação" já **fixa** o fator de magnitude em exatamente 64 por
construção — não há grau de liberdade para a magnitude variar entre
os pares comparados, logo não há confusão possível para começo de
conversa. A dispersão de 73×–680× documentada em H-018 já era, desde
o início, genuinamente devida à densidade residual G(w), não a um
artefato de magnitude disfarçado.

## Por que isso importa (mais do que um resultado negativo comum)

Isso **reforça a confiabilidade** da conclusão original de H-018 (a
obstrução ali localizada é real, não um erro metodológico à espera de
correção) — o oposto do que aconteceu com H-024→H-086. É um resultado
negativo valioso: testar uma suspeita razoável, bem fundamentada por
precedente direto (o mesmo padrão de erro já confirmado uma vez nesta
sessão), e reportar honestamente que ela não se aplica, em vez de
forçar uma correção que os números não sustentam.

## Nota metodológica geral (para hipóteses futuras nesta linha)

O teste de "há confusão de magnitude escondida?" só é informativo
quando a variável suspeita de confundir (aqui, `w_{i+3}/w_i`) **de
fato varia** entre os casos comparados. Antes de recalcular qualquer
razão "corrigida por magnitude", vale checar primeiro se essa variável
tem variação real na amostra — se for constante (como aqui), a
"correção" é matematicamente incapaz de mudar a dispersão, e não há
necessidade de reprocessar nada.

## Atualizações

- 2026-07-16: testado com os 18 pares de galhos "mesma fase, 3 posições"
  já disponíveis de decomposições anteriores (t=10,13,16,17). Termo
  trivial w_{i+3}/w_i confirmado exatamente 64 em todos os casos —
  dispersão em log10 idêntica antes e depois da "correção" (0,5674 dex
  em ambos). Suspeita do Fable não confirmada para este caso; H-018
  permanece como estava, sem necessidade de revisão.
