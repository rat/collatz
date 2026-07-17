# H-121 — Aliyev, "The 3x+1 Problem For Rational Numbers" (2020): sem erros, verificação numérica 100% consistente

Status: sem erros
Criada em: 2026-07-17
Origem: item 125 do INDEX.md (IEEE AICT 2020). Precursor do item 121/H-120
(mesmo autor), especializado para p=3,q=2 mas com 4 operações
(T=x/2, S=(3x+1)/2, V=(3x+2)/2, W=3x/2 — a operação extra W é
necessária para permitir órbitas racionais fechadas fora do mapa
Collatz padrão de inteiros).

## Enunciado

Prova 4 teoremas (variantes ±, com papéis de i,j trocados) sobre a
mesma família de invariantes 3^k·U_i vista em H-120, para a família de
4 operações T,S,V,W. Reconhece explicitamente em aberto se o número de
casos onde x0 é inteiro é finito ou não.

## Avaliação

Mesma natureza do item 121/H-120: estrutural/algébrico sobre ciclos
racionais, não sobre a conjectura clássica em inteiros — reconhecido
honestamente pelo próprio paper.

**Reprodução computacional**: composição P=TTSWVW (k=0 para W, k=1
para S, k=2 para V) — x_i calculados batem exatamente com o paper
(x0=-44/17, x1=-88/17, x2=-176/17, x3=-123/17, x4=-82/17, x5=-66/17);
U_i=-2^i/17 confirmado; as 4 verificações numéricas dos Teoremas 1-4
(-1782, -198, -123, -1892) todas batem exatamente com o reproduzido
independentemente.

## Relevância para a investigação atual

Baixa — mesma avaliação de H-120 (estrutura algébrica de ciclos
racionais sob composições afins arbitrárias, não estatística de
trajetórias inteiras).

## Veredito

Nenhum erro encontrado — o mais limpo dos 3 papers algorítmicos
revisados nesta rodada (119/121/125), com verificação numérica 100%
consistente.
