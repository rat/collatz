# H-162: cancelamento diagonal pela média sobre índices de caminho, com v fixo

Status: fechada-refutada (2026-08-10). Correção (mesma sessão, depois
de uma crítica independente encontrar um erro em H-163): a frase
"o cancelamento agregado em si é real (ver H-163)" que estava aqui
antes é FALSA. H-163 foi reaberta e retratada: a "confirmação" do
cancelamento agregado era um artefato (controles com dados não
relacionados reproduzem os mesmos números, ver H-163). O veredito desta
hipótese (`fechada-refutada`) sobrevive de forma independente disso, e
está reverificado abaixo, mas a leitura de mecanismo ("cancelamento de
banda larga") foi removida por não ter sustentação. Ver seção
"Fechamento" (reescrita) no fim do arquivo.

Status anterior (histórico): backlog

Criada: 2026-08-09

Origem: surgiu de E-133 (Regra 8e), enquanto se delimitava o alcance do
cancelamento do funcional diagonal registrado na atualização de H-159.

## Enunciado

E-133 mostra que o coeficiente de Fourier diagonal
`D(xi) = E[e_{3^s}(xi(X-Y))]` de um par de folhas irmãs se anula em
toda frequência primitiva acima do condutor `3^(1+v3(k))`, e continua
anulado depois de agregar sobre a medida de ramificação em `Delta`.
Mas a esperança ali é sobre o **parâmetro aritmético livre** `t`, que é
a aleatoriedade postulada por `thm:fresh-digit-coupling`.

O que O1 precisa é outra coisa. Para um inteiro `v` fixo não existe `t`
variando: o produto `S_1(xi) conj(S_2(xi))` de um par de caminhos é uma
única fase de módulo 1, e o cancelamento tem que vir da soma sobre os
dois índices de caminho dentro de cada subárvore, com os pesos reais de
ramo.

A hipótese: para `v` fixo, a soma
`sum_{xi != 0} S_1(xi) conj(S_2(xi))` sobre pares de caminhos exibe o
mesmo tipo de cancelamento, com a ressonância confinada aos modos de
condutor pequeno, depois de removidos os modos afins grosseiros.

## Por que vale investigar

O resultado de E-133 é forte no modelo em que foi provado e diz onde a
ressonância mora (condutor `3^(1+v3(k))`, e o peso de ramificação dos
gaps ressonantes é `4^(1-3^(s-1))`). Se a mesma localização de condutor
valer para a média sobre índices de caminho, e não só sobre o parâmetro
livre, O1 muda de natureza. Se não valer, a diferença entre as duas
médias é ela própria uma descrição limpa da barreira, no mesmo estilo
dos outros resultados do paper.

## Primeiro passo barato

Enumerar, para alguns `v` fixos pequenos e profundidade moderada, as
duas subárvores irmãs completas, formar `S_i(xi)` com os pesos de ramo,
e medir `|sum_{xi primitivo} S_1 conj(S_2)|` contra a linha de base de
fase aleatória, por escala e por condutor. Comparar a localização
observada com a previsão `3^(1+v3(k))` de E-133.

## Relações

Dívida deixada em aberto por H-159 depois de E-133. Toca O1 diretamente
e O7 por meio de H-159. O funcional é o mesmo que
`thm:multiscale-parseval` (H-155) e `prop:primitive-fibre-energy`
(H-154) consomem.

## Nota de numeração

Criada durante trabalho paralelo em worktree isolado. Se outro ramo
tiver usado `H-162` ao mesmo tempo, renumerar na integração.

## Fechamento (2026-08-10): E-141, corrigido depois de uma crítica independente

Executado o "primeiro passo barato" descrito acima, reusando a mesma
construção de `S_i` de E-140/H-163 (enumeração real ponderada, `v`
fixo, subárvore inteira de profundidade `ell-1` abaixo de cada irmão).
Agregado por condutor: para `xi != 0`, condutor `3^r` com
`r = ell - v3(xi)` (graduação de H-154/H-155/E-133). A estatística
exata (Regra 8c: descrita aqui com precisão depois de um crítico
apontar que a primeira versão a descrevia errado) é
`por_condutor[r] = |sum_{xi: cond(xi)=3^r} S_1(xi) S_2(xi)^*|`, a soma
COMPLEXA dentro de cada classe de condutor antes de tomar o módulo
(portanto já inclui qualquer cancelamento interno à classe), normalizada
por `sum_r por_condutor[r]`. Isto não é a mesma coisa que
`sum_{xi: cond=3^r} |S_1(xi)S_2(xi)^*|` (soma de módulos, sem
cancelamento interno), a frase original desta hipótese ("a fração de
`sum_xi |S_1(xi) S_2(xi)^*|` que cai...") descrevia a segunda, o código
mede a primeira. A diferença importa para a magnitude absoluta de cada
classe, não para o veredito abaixo (verificado: refazer a estatística
como soma de módulos por classe dá o mesmo padrão qualitativo, a maior
parte da massa acima do condutor previsto).

Medido em 12 raízes (`1,5,7,11,13,17,19,23,25,29,31,35`) × 3 pares de
posto (`(1,2)`: `k=1` para toda raiz; `(1,3)`: `k=2` ou `k=3` conforme
a raiz; `(2,3)`: `k=1` ou `k=2` conforme a raiz, a frase original
"`(2,3)` dá `k=1` de novo" estava errada, o `k` realizado depende da
raiz) em `ell=8` (36 medições) e 6 raízes × 3 pares de posto em `ell=10`
(18 medições), persistidas em
`experiments/E-141-path-index-diagonal-cancellation/run_ell8.txt` e
`run_ell10.txt` (não existiam no repositório antes desta correção):

```text
ell=8:  fração no condutor previsto: média 0,118 (desvio padrão 0,072)
        fração ACIMA do condutor previsto: média 0,837 (desvio padrão 0,098)
ell=10: mesmo padrão, levemente mais pronunciado
```

Cruzamento de sanidade: para o par de posto `(1,2)`, `|total|` desta
medição bate EXATAMENTE `measured_abs` de E-140 nos mesmos `(v,ell)`,
confirma que as duas implementações constroem o mesmo `S_1`, `S_2`.

**Controle (adicionado depois da crítica a H-163, Regra 8c)**: rodei a
mesma medição de fração-por-condutor substituindo o segundo irmão por
uma dilatação aleatória de sua própria subárvore (mesmo controle que
derrubou H-163), nas mesmas 36 combinações de `ell=8`. Resultado:
fração no condutor previsto, média `0,1235` (desvio padrão `0,0788`);
fração acima, média `0,8235` (desvio padrão `0,1201`), contra
`0,1175`/`0,8367` (desvios `0,0722`/`0,0977`) dos irmãos reais.
Estatisticamente indistinguível. O perfil por condutor, portanto,
TAMBÉM não carrega informação específica de irmandade.

**Veredito, revisado**: o enunciado original desta hipótese ("a mesma
localização de condutor vale para a média sobre índices de caminho")
continua `fechada-refutada`, isso sobrevive à crítica intacto, porque
a refutação não dependia de o cancelamento ser real: mesmo que
`sum_xi S_1(xi)S_2(xi)^*` completo seja um artefato (H-163), o PERFIL
por condutor dessa soma-artefato ainda não se concentra onde E-133
previu, e o controle mostra que essa não-concentração também é
genérica, não uma propriedade fina dos irmãos.

**O que foi removido desta seção (não sustentado, retirado depois da
crítica)**: a alegação de que "o cancelamento existe, mas por um
mecanismo de banda larga" e de que "essa diferença de mecanismo é o
achado". Essas frases pressupunham que H-163 tivesse medido
cancelamento real; não mediu (ver H-163). O achado que sobrevive é mais
modesto: nem a localização por condutor de E-133 nem a ausência dela
aqui distinguem irmãos reais de pares não relacionados, a pergunta de
mecanismo continua genuinamente aberta, não resolvida como "banda
larga".

**Escalonamento (Regra 11b)**: a resposta original ("não foi
necessário") ficou mantida quanto ao veredito de refutação, que
sobrevive; mas o processo deveria ter incluído um controle negativo
antes de interpretar o padrão como um mecanismo, o que só aconteceu
depois da crítica externa encontrar o problema em H-163.

Ver `experiments/E-141-path-index-diagonal-cancellation/` (script,
README atualizado, verificação de corretude, saídas persistidas,
controle).
