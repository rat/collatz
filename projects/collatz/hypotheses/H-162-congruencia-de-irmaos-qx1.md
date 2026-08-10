# H-162: congruência de irmãos na árvore reversa de qx+1

Status: fechada-confirmada como enunciado estrutural. O papel dela em
explicar a variância reduzida da árvore aritmética fica registrado
abaixo como parcial, medido, e menor do que eu esperava.

Criada: 2026-08-09

Origem: trabalho em O8 (transição do expoente de ramificação na árvore
aritmética genuína, H-113). Ao construir um controle iid casado para
calibrar o estimador de H-113, precisei decidir o que exatamente o
modelo iid deixa de fora da árvore aritmética. A resposta mais simples
é esta congruência. Registrada como hipótese própria por exigência da
Regra 8e.

## Enunciado (provado)

Seja `q >= 3` ímpar, `d = ord_q(2)`, e `u` ímpar com
`2^a u == 1 (mod q)` solúvel (nó fértil). Os filhos de `u` na árvore
reversa acelerada são `w_j = (2^(a_0 + j d) u - 1)/q`, `j >= 0`, onde
`a_0 = A_0(u mod q)` é o único expoente em `{1..d}` admissível. Então

```text
w_{j+1} = 2^d w_j + (2^d - 1)/q          (identidade exata em Z)
w_{j+1} == w_j + c   (mod q),   c := ((2^d - 1)/q) mod q
```

Prova da primeira linha, por substituição direta:
`2^d w_j + (2^d-1)/q = (2^(a_0+(j+1)d) u - 2^d + 2^d - 1)/q = w_{j+1}`.
A segunda sai de `2^d == 1 (mod q)`.

**Quando `c` é invertível mod `q`**, os resíduos de irmãos consecutivos
percorrem um sistema completo de resíduos mod `q`, com período exato
`q`. Logo, entre quaisquer `q` irmãos consecutivos, cada classe mod `q`
aparece exatamente uma vez: `d` deles são férteis e `q - d` são
estéreis, em posições determinadas, não sorteadas.

`c == 0 (mod q)` equivale a `q^2 | 2^d - 1`. Para `q` primo isso é
exatamente a condição de Wieferich na base 2 (`d | q-1`, então
`q^2 | 2^d - 1` implica `q^2 | 2^(q-1) - 1`; a recíproca vale porque a
ordem de 2 mod `q^2` é `d` ou `dq`). Os únicos primos de Wieferich
conhecidos são 1093 e 3511, então `c != 0` para todo `q` de interesse
aqui.

Valores: `q=3`, `d=2`, `c=1`; `q=5`, `d=4`, `c=3`; `q=7`, `d=3`, `c=1`.

Verificação numérica direta (todo `u` ímpar `< 4000`, 6 irmãos cada):
0 violações em `q=3` e `q=5`. Ver
`experiments/E-133-kl-volkov-window-calibration/`.

## Relação com H-018

Para `q=3` isto é exatamente o Teorema 2 de H-018 (periodicidade mod 3
dos galhos de primeiro nível ao longo de uma cadeia de duplicação, com
período 3, lá derivado de `ord_9(4)=3`). H-162 é a generalização para
`qx+1` arbitrário, com a constante `c` identificada e a condição de
Wieferich isolada. Não substitui H-018; estende.

## O que muda em q=7 (nota lateral verificada)

Para `q=7`, `d = ord_7(2) = 3 < q-1 = 6`. Só os resíduos no subgrupo
`<2> = {1,2,4}` são férteis: 4 das 7 classes são estéreis, não 1. Isso
não altera a equação de pressão do paper: para cada expoente `n >= 1`,
o número esperado de filhos de um nó no expoente exatamente `n` é
`1/q`, porque a condição é `2^n r == 1 (mod q)`, ou seja `r == 2^(-n)`,
uma única classe entre `q`. Confirmei numericamente que a forma fechada
recíproca (ver E-133, `annealed_exact.py`) bate com a soma dupla bruta
também em `q=7`.

## O que foi testado sobre o papel explicativo (parcial)

Hipótese de trabalho: essa congruência é redução de variância que o
modelo iid não tem (no iid cada irmão é estéril por moeda independente,
mesma média, variância maior), e por isso a árvore aritmética
convergiria mais rápido do que o modelo no mesmo estimador.

Medido em E-133, `q=5`, mesmas 300 raízes, mesma janela `1e5..1e8`,
mesmos buffers, estimador de H-113 idêntico nos três casos:

| modo | descrição | estimador | sd de log10 N(1e8) |
|------|-----------|-----------|--------------------|
| iid | classe de ramo sorteada em cada nó | 0.6119 | 0.8014 |
| cyc | primeira classe sorteada, irmãos avançam `+c` | 0.6283 | 0.6657 |
| arith | árvore aritmética verdadeira | 0.6364 | 0.5942 |

(valor anelado exato do modelo: `alpha_-(5) = 0.650919`.)

A congruência de irmãos cobre cerca de metade do caminho de `iid` até
`arith` no estimador. Na dispersão ela cobre tudo, ver a seção
seguinte, que corrige a leitura ingênua desta coluna.

Antes desta tabela eu produzi uma versão errada dela, com o iid em
0.484, por um artefato de amostragem: as raízes aritméticas são
sorteadas com `u mod q != 0`, logo sempre férteis, enquanto o controle
sorteava o resíduo da raiz em `{0..q-1}` e matava 1 raiz em 5 na hora.
Corrigido (o controle passa a sortear a raiz entre os resíduos
férteis). Registro o erro porque a conclusão errada, "o modelo iid é
absurdamente mais lento", teria sido muito conveniente.

## Separação entre-raízes versus dentro-de-raiz (feita, e corrige a leitura acima)

A tabela acima compara coisas diferentes: em `arith` cada raiz dá UMA
árvore determinística, enquanto em `cyc` e `iid` cada raiz dá UM sorteio
de um ensemble. O controle carrega ruído de realização que a árvore
aritmética não tem, então sd menor em `arith` não prova nada sozinho.

Medido em `within_root_spread.py` (10 raízes fixas, 3000 realizações
cada, buffer `1e11` nos três casos, para comparar no mesmo truncamento):

| quantidade | valor |
|------------|-------|
| `arith`, sd de log10 N(1e8) entre as 300 raízes determinísticas | 0.5869 |
| `cyc`, sd de log10 N(1e8) DENTRO de uma raiz (média sobre 10 raízes) | 0.5824 |
| `iid`, idem | 0.7419 |

Ou seja: a congruência de irmãos derruba a flutuação do modelo de 0.742
para 0.582, que é exatamente o nível da dispersão total da árvore
aritmética. **Essa é a leitura defensável**: a congruência dá conta da
redução de flutuação; não sobra efeito residual detectável com este
desenho. Uma decomposição mais fina (tirar dos 0.5869 a parte que vem
só do deslocamento de janela `log10(x/u)`, comum aos três modos)
sugeriria um resíduo pequeno a favor de `arith`, mas ela depende de
supor independência entre deslocamento e idiossincrasia, e não vou
apoiar conclusão nenhuma nisso.

O mesmo script mede em que percentil a árvore aritmética cai dentro do
ensemble casado da própria raiz: mediana 23.6% (cyc) e 34.7% (iid) no
slope. Isso **não** é evidência de que a árvore aritmética seja uma
realização atípica: as 10 raízes usadas têm slope aritmético médio
0.58915 contra 0.63121 nas 300, isto é, são uma amostra baixa a 2.3
erros-padrão. O percentil está medindo a amostra de raízes, não a
árvore. Registro como inconclusivo.

## Referências

- H-018 (Teorema 2, caso `q=3`).
- H-113 e `experiments/E-097-qx1-empirical-gate/` (o estimador
  calibrado aqui).
- `experiments/E-133-kl-volkov-window-calibration/`.
