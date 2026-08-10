# H-175: coeficientes de Mellin/caracteres de V (a rota de Weyl que sobra)

Status: backlog

Criada: 2026-08-10

Origem: pista aberta na "Terceira rodada" de H-161 (2026-08-09,
programa de somas de Weyl), nunca antes registrada como hipótese
própria. Número escolhido para não colidir com outros agentes rodando
em paralelo nesta sessão (estado do repositório nesta rodada ia até
H-174); renumerar na integração se necessário.

## O que já se sabe

O programa de somas de Weyl de H-161 (terceira rodada) provou que
NENHUMA cota que dependa só de `|S|`, `|S'|` (tamanhos dos conjuntos de
nível `{V<=x}`) e dados espectrais do mapa afim `sigma` (que relaciona
pares consecutivos na órbita de `A`) pode ser não trivial, a rota por
norma de operador devolve exatamente a cota trivial de Cauchy-Schwarz,
porque a composição com `sigma` é unitária em `L²(G)`. O diagnóstico
final de H-161: falta controle HARMÔNICO do próprio conjunto de nível
`{V<=x}` (a estrutura autossimilar/recursiva de `V=W_ell` em si), não
equidistribuição de `sigma`.

A identidade exata já provada `What(m) = Nhat(m)/(1-(1/4)e(-m/3^n))`
(a recursão de `W` diagonaliza exatamente na base de caracteres de `G`)
diz que `W` e `N` têm coeficientes de Fourier/Mellin comparáveis ,
então estimar os coeficientes de UM dos dois já informa o outro.

## Pergunta

Os próprios coeficientes de caractere/Mellin de `V` (ou de `N`, mesma
coisa via a identidade acima) têm alguma estrutura fechada ou
recursiva que se preste a uma estimativa direta (não via `sigma`, não
via cotas de tamanho de conjunto)? Isto não foi tentado, o programa de
Weyl inteiro de H-161 atacou o problema pelo lado do MAPA (`sigma`),
nunca pelo lado do PRÓPRIO OBJETO (`V`/`N`/`W`).

## Por que vale investigar

É a única rota harmônica que a exclusão de H-161 deixa explicitamente
de pé ("isso exclui especificamente o programa 'estimar T, inserir,
limitar o erro por Cauchy-Schwarz/norma de operador', não exclui
necessariamente todo método harmônico"). Se os coeficientes de `V`
tiverem decaimento direto conhecido (por exemplo, via a mesma
identidade de auto-similaridade recursiva que já produziu a
monotonicidade de `min R`, H-166), isso poderia alimentar de volta a
desigualdade de par (Q2 de H-161) sem precisar do mapa `sigma` de
jeito nenhum.

## Primeiro passo barato

Calcular numericamente `What(m)` (ou `Nhat(m)`) para `ell` pequeno a
moderado e ver se a magnitude por condutor segue algum padrão limpo
(decaimento de potência, platô, etc.), E-137 já fez uma medição
adjacente (espectro primitivo de `mu_ell`, não de `N_ell`/`W_ell`
especificamente); conferir se é a mesma quantidade ou uma diferente
antes de recomputar do zero.

## Passo barato executado (2026-08-10): tentativa 1, invalidada por crítica independente

A primeira versão desta seção afirmava `Nhat_ell(m) = 3^ell *
muhat_ell(m)` e concluía, sem mais cálculo, que a transformada que
H-161 chama de "Mellin/Weyl" (caracteres do grupo cíclico `G = {z ≡ 1
mod 3}`, indexados por TEMPO DE ÓRBITA sob `A` = multiplicação por 4)
já tinha sido medida por E-137. Um crítico independente (Regra 8/15)
mostrou que isso está errado: E-137 mede a transformada ADITIVA comum
sobre `Z/3^ell` (caracteres `e(xi*u/3^ell)`, indexados pelo próprio
resíduo `u`); a transformada de H-161 é indexada pela posição na
órbita de `A`, uma reordenação NÃO-LINEAR de `u`. As duas só coincidem
se a órbita de `A` fosse ela mesma linear em `u`, o que não é (`A` é
afim em `k`, e `k` não é uma função linear de `u`). Rule 8c aplicada
à correção também: reproduzi o cálculo do zero, computei as duas
transformadas de verdade e confirmei que diferem estruturalmente, não
por um fator de escala único.

## Passo barato, tentativa 2 (2026-08-10, cálculo real, tabela corrigida numa terceira rodada de crítica)

Construí a sequência `N_ell(y(k_t))` ordenada por TEMPO DE ÓRBITA `t`
(`k_0=0`, `k_{t+1}=A(k_t)=4k_t+1 mod 3^{ell-1}`, representante `y` via
o ramo `t0=1`, mesma construção já verificada em H-176), tomei a DFT
dessa sequência (o objeto que a seção de Weyl de H-161 de fato usa), e
comparei com a DFT aditiva usual de `N_ell` sobre `Z/3^ell` completo
(zeros nos não-unidades). Verificação de autoconsistência antes de
aceitar qualquer número (identidade de Plancherel, `sum|hat(m)|^2 =
(tamanho) * sum(valor^2)`): bate a `2e-16` em todo nível testado.

**Correção (terceira rodada de crítica, 2026-08-10)**: a primeira
versão desta tabela comparava a transformada ADITIVA restrita a
frequências PRIMITIVAS (convenção de E-137/`primitive_energy_fft`,
`3∤xi`) contra a transformada de Mellin sobre TODAS as frequências
não-nulas, uma comparação de maçãs com laranjas, não "uma convenção de
normalização diferente" como um diagnóstico anterior (errado, Regra 8c)
alegou. Tabela refeita com as duas transformadas sobre o MESMO conjunto
(todas as frequências/índices não-nulos):

```text
ell   DC_aditivo   sup_aditivo   rms_aditivo   DC_Mellin   sup_Mellin   rms_Mellin   sup_aditivo/sup_Mellin   rms_aditivo/rms_Mellin
 6      729,00       420,89         46,80        486,00      183,69       36,97              2,2913                   1,2660
 7    2187,00      1262,67         87,08       1458,00      551,07       70,03              2,2913                   1,2435
 8    6561,00      3788,00        160,62       4374,00     1653,22      130,94              2,2913                   1,2267
 9   19683,00     11363,99        294,24      13122,00     4959,65      242,43              2,2913                   1,2137
```

A EVIDÊNCIA real está em `sup`/`rms`: a razão `sup_aditivo/sup_Mellin`
fica PRESA em `2,2913` (constante exata em todo nível testado), mas
`rms_aditivo/rms_Mellin` DERIVA de `1,266` para `1,214` (não constante).
Se as duas transformadas fossem a mesma coisa reescalada por um único
fator, as duas razões teriam que ser iguais e constantes; não são. Isso
é o que estabelece que `Nhat` (Mellin) e `muhat` (aditivo) são
transformadas genuinamente diferentes, não uma reescala uma da outra.

**Nota de contabilidade, rebaixada a checagem de sanidade (não é mais a
evidência principal, Regra 8c)**: a razão `DC_aditivo/DC_Mellin` é
EXATAMENTE `3/2` em todo nível, mas isso é FORÇADO pela construção, não
evidência de nada. `DC_aditivo = sum` sobre TODAS as unidades (as duas
fases `t0=1` e `t0=2`); `DC_Mellin`, como construído aqui, soma só o
ramo `t0=1` (SEMPRE o filho MAIOR de cada `k`, por F1: os dois filhos
valem `(3/2)W(k)` e `(3/4)W(k)`), que carrega exatamente `2/3` da massa
total por construção, um número forçado (`3^ell / ((2/3)*3^ell) =
3/2`), não uma descoberta.

Os achados de E-137 (RMS na escala raiz-quadrada, máximo concentrado na
órbita de duplicação) descrevem a transformada ADITIVA, não a Mellin
que o programa de Weyl de H-161 de fato usa, e não podem ser importados
diretamente para o argumento sobre `V`/`N`/`W` que esta hipótese
pergunta. A alegação original da tentativa 1 ("já é a mesma quantidade,
não recomputar") estava errada; isso ficou confirmado de forma
independente duas vezes (por mim e por um crítico independente,
convergindo no mesmo padrão qualitativo mesmo com conjuntos de
frequência de referência diferentes na primeira rodada).

**Avaliação honesta**: passo barato refeito corretamente. Não decide a
questão original desta hipótese (se os coeficientes de Mellin de `V`
têm alguma estrutura útil para Q2); ao contrário da tentativa 1, agora
está estabelecido que a resposta não pode vir de reciclar os achados de
E-137, precisa de uma medição nova e própria da transformada de Mellin.
Isso é, honestamente, menos progresso do que a tentativa 1 alegava, mas
é o estado real. Mantido em `backlog`: o próximo passo real é medir a
estrutura da transformada de Mellin diretamente (o `sup`/`rms` acima já
são um primeiro esboço dela, até `ell=9`; estender e procurar um padrão
de decaimento por "condutor de órbita" análogo ao que E-137 fez para a
transformada aditiva, mas sobre o objeto certo desta vez).