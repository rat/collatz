# H-159: transferência da cauda iid para a árvore aritmética

Status: aberta

Criada: 2026-08-08

## Alvo

Transferir o teorema de cauda de H-132 para o funcional enraizado na
árvore reversa aritmética. É necessário controlar a dependência entre
dígitos novos de subárvores irmãs depois da média sobre os índices de
caminho e da remoção dos modos afins grosseiros identificados em H-150.

## Critério de fechamento

Uma prova deve fornecer uma aproximação quantitativa suficiente para
aplicar renovação implícita ou construir diretamente a cauda regular
com índice `alpha_plus(q)/alpha_minus(q)`. Um contraexemplo estrutural
que impeça qualquer transferência desse tipo também fecha a hipótese,
como refutada.

## Relações

Esta é a dívida aritmética compartilhada por O1 e O7. Independência
par a par de caminhos fixos já foi refutada por H-150; o alvo correto é
cancelamento após agregação.

## Atualização E-129 (2026-08-08)

Testada a rota ingênua mais óbvia para a agregação: promediar a lei
conjunta dos dígitos frescos (E-120) sobre a medida de ramificação
natural do gap `Delta` entre irmãos (peso `P(Delta=2k)=3*4^-k`, de
E-108), e medir a distância TV e a informação mútua da lei conjunta
agregada contra o produto de suas próprias marginais.

Resultado: a agregação sobre `Delta` **não** aproxima a lei do produto.
Em `fresh=6`, TV de um par com `delta` fixo é `0.998628`; agregada sobre
`Delta` (com `k_max=16`, cobrindo essencialmente toda a massa da série
geométrica) ainda é `0.992193`. A informação mútua se comporta do mesmo
jeito. Verificado antes de aceitar o número: a lei conjunta de um único
`delta` não depende de qual resíduo unitário `x0 mod 3^coarse` é usado
como referência (checado para vários `coarse` e `delta`), então a
agregação usada é a lei condicional correta, não artefato de uma
escolha arbitrária.

**Isso não fecha H-159 nem a move para refutada.** TV e informação
mútua são as métricas erradas para refutar a transferência: elas ficam
dominadas pela estrutura de suporte determinística (para `delta` fixo,
o bloco de `y` é função determinística do bloco de `x`), então TV
próxima de 1 é esperada independente de qualquer cancelamento no
funcional que a renovação implícita realmente precisa (um momento ou
coeficiente de Fourier/Mellin específico, não a distância em variação
total). O experimento também fixa só um par de irmãos de um mesmo pai;
a árvore real agrega muitos mais pares simultaneamente.

**O que o resultado realmente descarta**: a rota ingênua "promediar
sobre o gap `Delta` isoladamente e invocar renovação implícita direto
sobre a lei quase-produto resultante" não funciona, porque a lei
agregada não fica perto de um produto em nenhuma das duas métricas
testadas. O alvo permanece em aberto, mas mais restrito: precisa ser
cancelamento num funcional específico (momento/Fourier), não
aproximação distribucional, e provavelmente precisa agregar sobre mais
do que um único par de irmãos.

Ver `projects/collatz/experiments/E-129-fresh-digit-aggregate-cancellation/`.

## Nota E-138 (2026-08-09): o lado O7 encontrou o mesmo objeto de O1

Atacando o sub-alvo de O7 (a margem de sinal uniforme de `q=3` em
H-157), o funcional que sobra é uma colisão deslocada afim,
`T_ell(4,1) = 3^ell P[F' = 4F+1 mod 3^ell]`, que é a correlação de
vizinhos `(1/M) sum_j N_j N_(j+1)` ao longo da órbita do mapa afim
`A(k)=4k+1`. É a mesma órbita e o mesmo mapa de H-161, e são os mesmos
pares consecutivos que E-132 mede.

As duas perguntas não são a mesma. E-132 mede a cauda inferior conjunta
(com que frequência os dois membros de um par consecutivo são pequenos
ao mesmo tempo) e acha antiaglomeração; O7 precisa de cota inferior
para a esperança do produto do par. Antiaglomeração empurra na direção
certa para essa cota, mas não a dá.

Isso confirma o diagnóstico de "dívida aritmética compartilhada" desta
hipótese em forma concreta: os dois lados chegam a um funcional de
momento sobre pares na mesma órbita afim, por rotas independentes. Ver
a seção datada de 2026-08-09 em H-157 e
`projects/collatz/experiments/E-138-diagonal-shifted-collision/`.
