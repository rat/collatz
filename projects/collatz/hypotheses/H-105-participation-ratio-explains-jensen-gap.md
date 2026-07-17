# H-105 — A razão de participação PR(r) da árvore-prefixo explica parte real (~34% da variância) do gap de Jensen de 46× (H-099)

Status: confirmado — correlação real e mais forte que qualquer preditor
anterior, mas não exaustiva (66% da variância ainda não explicada)
Criada em: 2026-07-16
Origem: quantidade local proposta pelo Fable (ver H-104) após refutar a
formulação original de "expoente de Kesten local por classe" de uma IA
externa. Deriva de: se G|r = Σ_folhas peso_i·G_genérico_i (aproximação
de campo médio, folhas i.i.d.), então Var(G|r) = S2(r)·Var(G_genérico),
onde S2(r) = Σ peso_i² é a soma dos pesos ao quadrado da árvore-prefixo
determinística da classe r. PR(r) := S1(r)²/S2(r) (S1(r)=Σ peso_i, a
mesma quantidade que 3^m·μ_m(r)) mede o "número efetivo de folhas
independentes" contribuindo — árvores mais "espalhadas" (PR alto) têm
distribuição condicional mais concentrada (gap de Jensen pequeno);
árvores que concentram massa num só caminho (PR baixo, ex. repetição
de a=1) têm cauda mais pesada (gap grande).

## Implementação e checagem de sanidade

`experiments/E-090-syracuse-measure-vs-density/experiment_participation_ratio.py`:
calcula S1(r) e S2(r) via recursão vetorizada (numpy) idêntica em
estrutura a `syrac_distribution_np`, mas SEM renormalizar (soma bruta
de pesos, não distribuição de probabilidade) e mantendo em paralelo a
soma dos pesos ao quadrado.

**Checagem de sanidade**: S1(r)/μ_m(r) = 3^m exatamente (testado m=8:
razão = 6561,000000, desvio ~3×10⁻¹², erro de ponto flutuante puro) —
confirma que a implementação bate exatamente com a quantidade já
validada em H-090/H-091 (3^m·μ_m(r)).

## Resultado

Para 300 classes residuais (m=8, mod 3⁸=6561), comparado PR(r) contra
o gap de Jensen medido diretamente (headroom=2000, 150 amostras/classe,
mesma metodologia de H-099):

- **Correlação(gap, log PR) = −0,58** (slope=−0,073) — negativa, como
  previsto pelo Fable.
- PR(r) varia de 3,58 a 48,4 (fator ~13,5×) entre as 300 classes
  testadas; gap(r) varia de 0,026 a 0,62 dex (fator ~24×).

Essa correlação (−0,58, R²≈0,34) é **substancialmente mais forte** que
a correlação fraca encontrada em H-099 entre gap(r) e log(μ_r)
diretamente (0,30, R²≈0,09) — PR(r) explica quase 4× mais da variância
do gap do que a medida μ sozinha explicava.

## Interpretação

A heterogeneidade de 46× no gap de Jensen (H-099) tem, agora, uma
explicação mecanicista parcial e real: parte dela vem da estrutura
combinatória da própria árvore-prefixo (quão "concentrada" ou
"espalhada" é a distribuição de pesos entre os caminhos possíveis a
partir daquele resíduo) — não é um artefato ou puro ruído de
amostragem de cauda pesada (embora o alerta do Fable em H-104
permaneça válido: com α=2 na fronteira da existência da variância,
alguma fração do gap residual não explicado por PR pode ainda ser
ruído). ~66% da variância do gap continua sem explicação por este
mecanismo sozinho — candidato a investigação futura seria combinar
PR(r) com uma correção para ruído de cauda pesada (bootstrap/
half-sample, sugerido pelo Fable) antes de tentar explicar o resíduo
remanescente.

## Referências

- H-104 (previsão do expoente universal α=2, motivação teórica de PR(r)).
- H-099 (achado original do gap de Jensen, 46×).
- Experimento: `experiments/E-090-syracuse-measure-vs-density/experiment_participation_ratio.py`.
