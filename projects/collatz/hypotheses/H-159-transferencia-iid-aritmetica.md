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
