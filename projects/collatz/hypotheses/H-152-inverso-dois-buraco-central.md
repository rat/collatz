# H-152: o inverso de dois seria um buraco central persistente

Status: fechada-refutada

Criada e encerrada: 2026-08-07

## Hipótese

Os dados de E-115 sugeriam que

```text
g_ell(ell, 2^(-1) mod 3^ell) = 0
```

para todo `ell`. Isso refutaria imediatamente a condição `(?3)` de
Wirsching, pois `k=ell` pertence a qualquer janela central não trivial.

## Teste exato

E-121 implementa diretamente a recursão booleana

```text
hit(ell,k,a) = OR_j hit(
    ell-1,
    k-j,
    (2^(j+1)*a-1)/3 mod 3^(ell-1)
).
```

Somente incrementos para os quais o numerador é divisível por três são
admitidos. A recursão é exatamente a equação (2.1), sem amostragem.

O resíduo proposto tem custo mínimo `ell+1` entre os níveis 2 e 21.
No nível 22 seu custo mínimo cai para 22. Ele permanece alcançável no
custo central em todos os níveis testados até 60.

## Auditoria da implementação

O predicado direcionado foi comparado com todas as entradas da tabela
booleana independente de E-115, para todos os resíduos unitários, todos
os custos `0<=k<=12` e todos os níveis `1<=ell<=8`. Não houve nenhuma
divergência. A divisão modular por três também é exata: trocar um
representante do produto por um múltiplo de `3^ell` altera o quociente
apenas por um múltiplo de `3^(ell-1)`.

## Conclusão

A hipótese é falsa. Os buracos observados na tabela completa até o nível
16 não podem ser extrapolados por essa família 3-ádica. Nenhum enunciado
foi acrescentado ao paper. O resultado metodológico é que qualquer
tentativa de refutar `(?3)` por um resíduo de forma fechada deve ser
testada além da transição tardia do nível 22.
