# H-065 — Revisão do paper #049 (Boyle, "The Collatz Conjecture is True") — ALEGAÇÃO DE PROVA, gap fatal localizado no Lemma 4.2

Status: revisão externa concluída — gap lógico fatal localizado e
explicado; NÃO é uma prova válida
Criada em: 2026-07-15
Origem: item 049 da coleção (`literature/papers/INDEX.md`), já baixado
(`049_The-Collatz-Conjecture-is-True.pdf`). **Alegação de prova
completa** — requer maior rigor de escrutínio (não peer-reviewed,
rxiverse.org).

## O paper

Boyle, D.G. (2026), *The Collatz Conjecture is True*, rxiverse.org,
30 páginas. Estrutura em 3 blocos: (1) argumento de "não-divergência"
via análise probabilística de paridade (Seção 3); (2) exclusão de
ciclos não-triviais via árvore algébrica simbólica + equação
diofantina (Seção 4, Lemas 4.3); (3) prova por indução combinando
(1)+(2) (Teorema 4.1, Lemas 4.2/4.4, Teorema 4.5).

## Veredito: NÃO é uma prova válida

## O gap fatal — Lemma 4.2 ("a sequência gerada por n+1 não diverge")

A cadeia lógica do paper:

```
Lema 3.1: "se n∈2N é escolhido aleatoriamente, P{n/2 par} = 1/2"
   (afirmação de DENSIDADE sobre o CONJUNTO de todos os pares —
   correta, mas trivial: metade de {1,2,3,...} é par)
        ↓
Teorema 3.2: assume "n∈N escolhido aleatoriamente" E "gera uma
   sequência que diverge", trata a paridade de C^k(n) como um
   processo de MOEDA (P=1/2 a cada passo, via recursão Eq 3.2),
   deriva lim P{C^k(n) par} = 2/3 (soma de série geométrica)
        ↓
Lema 4.2: substitui e=2/3, o=1/3 diretamente na Equação 4.4, que é
   sobre UMA trajetória hipotética ESPECÍFICA e FIXA (a gerada por
   n+1, suposta divergente) — deriva um "limite superior que tende a
   0", contradição, conclui que a sequência de n+1 não diverge
```

**O problema**: o Lema 3.1 é uma afirmação sobre a *densidade* do
conjunto de todos os números pares — não diz nada sobre a órbita
determinística de um `n` específico. O Teorema 3.2 já comete o salto
ao tratar a paridade de `C^k(n)` como uma variável aleatória
independente a cada passo — mas para um `n` **fixo**, a sequência
`C(n), C²(n), C³(n), ...` é inteiramente determinística; não há
"probabilidade" alguma de que um termo específico seja par ou ímpar,
isso já está determinado por `n` e `k`. O salto fatal ocorre quando o
**Lema 4.2** pega os valores `e=2/3, o=1/3` — válidos, na melhor das
hipóteses, como uma **média de ensemble** sobre muitos `n` aleatórios
diferentes (a "heurística do passeio aleatório", bem conhecida na
literatura desde Crandall/Lagarias como fonte de *intuição*, não de
prova) — e os substitui como se fossem uma propriedade **necessária e
determinística** de UMA trajetória hipotética específica e fixa (a
gerada por `n+1`). Nada na dinâmica determinística do mapa de Collatz
obriga essa órbita específica a ter frequência assintótica de paridade
igual à média heurística do ensemble. A "contradição" derivada
(Equação 4.4, limite superior → 0) depende inteiramente dessa
substituição ilegítima — portanto não é uma contradição válida, e o
Lema 4.2 não está provado.

Como o Teorema 4.1 (indução) e o Lema 4.4 ("alcança 1") dependem
*ambos* de que o Lema 4.2 valha **incondicionalmente** para todo `n`,
o colapso deste único passo invalida toda a cadeia até o Teorema 4.5.

Notavelmente, a própria referência `[6]` que o paper cita como fonte
da técnica probabilística é um post do StackExchange (Rocherz, 2023)
sobre um argumento heurístico — não uma prova publicada.

## Demonstração quantitativa (Parte 3b de `experiment.py`)

Para tornar a distinção ensemble-vs-trajetória-individual concreta,
computei a fração de passos pares **realizada por cada trajetória
individual completa** (não a média sobre muitas trajetórias, mas o
valor de UMA órbita específica até alcançar 1), para 3.000 valores de
`n` amostrados em `[3,10⁶]`:

```
média = 0,6767 (perto de 2/3 = 0,6667 — é isso que o paper mostra em Fig 3/5)
desvio-padrão = 0,0309, mínimo = 0,6314, máximo = 0,8667
10,2% das trajetórias desviam de 2/3 por mais de 0,05
```

Ou seja: mesmo entre trajetórias **conhecidas e convergentes**, a
fração de passos pares realizada por cada órbita individual varia
substancialmente ao redor de 2/3 — longe de ser uma constante fixa por
trajetória. Isso ilustra concretamente por que não há base para forçar
essa razão sobre uma trajetória hipotética específica (divergente) no
Lema 4.2: a variabilidade real, mesmo em casos convergentes, mostra que
"2/3" é uma propriedade estatística agregada, não uma restrição rígida
sobre cada órbita individual.

## Gap secundário — Lemma 4.3, Equação 4.28 (caso n+1 ímpar não tratado)

Ao resolver a equação diofantina `2^(n+1) - 3^m = 1` (Equação 4.26), o
paper fatora `2^(n+1) - 1` como diferença de quadrados
`(2^((n+1)/2)-1)(2^((n+1)/2)+1)` — o que só faz sentido se `n+1` for
**par** (para que `(n+1)/2` seja um expoente inteiro). O caso `n+1`
**ímpar** nunca é tratado separadamente no texto.

Busca exaustiva computacional (Parte 2 de `experiment.py`, testando
`n+1=1..2000`, ambas as paridades): as únicas soluções são
`(n+1,m)=(1,0)` [ímpar, degenerado — `m=0` não corresponde a um ciclo
genuíno, já que um ciclo exige ao menos um passo ímpar] e `(n+1,m)=(2,1)`
[par — a solução que o paper encontra, correspondendo ao ciclo trivial].
**A conclusão numérica do paper sobrevive** mesmo incluindo o caso
ímpar — mas a demonstração, como escrita, tem essa lacuna não
endereçada (o argumento de que `d=gcd(2^(n+1)-3^m, b)=1` é "a única
solução" também é justificado de forma pouco rigorosa no texto,
descartando outros primos com uma frase solta sobre paridade em vez de
uma eliminação caso-a-caso completa).

## O que está correto no paper

- **Parte 1** (exclusão de ciclos de 2, 3 e 4 termos, Equações
  4.6-4.16): aritmética simples e correta — nenhum erro de cálculo.
- **Parte 3a** (aritmética da série geométrica, Equações 3.3-3.5): a
  soma da série geométrica `a=1, r=-1/2` de fato converge para `2/3` —
  o problema não é um erro de cálculo aqui, é a validade conceitual de
  aplicar esse modelo probabilístico a uma trajetória determinística
  específica (ver acima).
- O código Pari/GP e JavaScript (Apêndices A, B) parece corretamente
  implementado para o que se propõe a calcular.

## Por que isso não é incomum

Esta é exatamente a falácia do "argumento do passeio aleatório"
("random walk heuristic"), um dos padrões mais recorrentes em
tentativas amadoras de provar Collatz: a heurística estatística que
torna a conjectura *plausível* (citada por praticamente todo survey
sério, incluindo Lagarias — referência `[1]` do próprio paper) é
tratada como se fosse uma prova, quando a própria literatura é
explícita que ela não basta, precisamente porque a paridade de uma
órbita determinística específica não é uma variável aleatória.

## Novas hipóteses?

Nenhuma. Item descartado como alegação de prova inválida, com o gap
localizado e documentado para referência futura (caso outra versão ou
paper similar apareça na coleção).

## Atualizações

- 2026-07-15: paper lido por completo (30 páginas), gap fatal
  localizado (Lemma 4.2, substituição ensemble→trajetória específica),
  gap secundário identificado (Lemma 4.3, caso n+1 ímpar), demonstração
  quantitativa da variância entre trajetórias individuais. `INDEX.md`
  atualizado (item 049: Lido=Sim, Corrigido=Não [alegação de prova
  refutada — gap fatal no Lemma 4.2], Implementado=Sim [partes
  verificáveis testadas]).
