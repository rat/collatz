# E-109 — H-130: a família de escala por tipo sobrevive à esterilidade extra? (q=7, q=15)

## Hipótese relacionada

H-130 pergunta: quando 2 não é raiz primitiva mod q (ex.: q=7,
ord₇(2)=3<φ(7)=6, com resíduos {3,5,6} estéreis além de 0), a
esterilidade extra (i) só reescala a população total por um fator
constante, sem mudar α₋(q) (já confirmado — Teorema 3.3 bate
numericamente para q=7), ou (ii) introduz estrutura mais rica entre os
tipos não-estéreis restantes? A família de escala já confirmada para
q=5 (E-103 Estágio 4, todos os resíduos não-nulos não-estéreis, já
que 2 é raiz primitiva mod 5) prediz $W_i \sim 2^{-a_0(i)\theta}W^*$.
Este experimento testa se essa MESMA relação vale entre os tipos
não-estéreis, apesar da esterilidade extra em outras partes da árvore,
para **dois** casos com estruturas diferentes: q=7 (primo, 3 de 6
resíduos não-nulos não-estéreis) e q=15 (composto, 4 de 8 resíduos
coprimos não-estéreis — testa robustez a q não-primo).

## Por que q=7/q=15 e não q=31

q=31 é o caso mais extremo da tabela de H-130 (só 5/30 resíduos
não-nulos não-estéreis), mas $\theta_{31}=\alpha_-(31)\approx0{,}0552$
é pequeno demais para um teste viável: crescimento populacional
$H^{0{,}0552}$ exigiria $H\sim10^{36}$ para dar até 100 amostras na
contagem — impraticável. q=7 ($\theta=0{,}373501$) e q=15
($\theta=0{,}131006$, ainda tratável com $H=10^8$) são os testes
viáveis mais próximos do espírito de H-130.

## Método

$a_0$ para os tipos não-estéreis: q=7, $\langle2\rangle=\{1,2,4\}$,
$a_0$: 3,2,1. q=15, $\langle2\rangle=\{1,2,4,8\}$, $a_0$: 4,3,2,1.
Amostrei raízes ímpares coprimas a $q$ por tipo (5000 para q=7, 3000
para q=15, residuo mod $q$ fixo, excluindo ciclos triviais), enumerei
a árvore reversa real até headroom $H$ ($10^7$ para q=7, $10^8$ para
q=15) via `tree_lib.count_tree` (cópia isolada e sem efeitos
colaterais de `E-097/empirical_qx1_tree.py`), medi
$W_v=N_v(v\cdot H)/H^\theta$, e comparei razões entre tipos (mediana e
média geométrica) contra a previsão
$W_i/W_j=2^{-(a_0(i)-a_0(j))\theta}$.

## Resultado

**q=7** (5000 raízes/tipo), todas as 3 razões batem com a previsão a
2–4% (mesma faixa do achado original de E-103 Estágio 4 para q=5,
"2–9%"):

```
W_1/W_2: observado=0.7430  previsto=0.7719  razao obs/previsto=0.9626
W_1/W_4: observado=0.5807  previsto=0.5958  razao obs/previsto=0.9747
W_2/W_4: observado=0.7816  previsto=0.7719  razao obs/previsto=1.0126
```

**q=15** (3000 raízes/tipo, q **composto**), todas as 6 razões batem a
1–4%:

```
W_1/W_2: observado=0.9117  previsto=0.9132  razao obs/previsto=0.9983
W_1/W_4: observado=0.7986  previsto=0.8339  razao obs/previsto=0.9576
W_1/W_8: observado=0.7337  previsto=0.7615  razao obs/previsto=0.9634
W_2/W_4: observado=0.8760  previsto=0.9132  razao obs/previsto=0.9592
W_2/W_8: observado=0.8048  previsto=0.8339  razao obs/previsto=0.9650
W_4/W_8: observado=0.9187  previsto=0.9132  razao obs/previsto=1.0061
```

**Conclusão para H-130**: a família de escala por tipo sobrevive
intacta entre os tipos não-estéreis, em dois casos estruturalmente
diferentes (q=7 primo, 3/6 tipos; q=15 composto, 4/8 tipos coprimos).
Isso é evidência forte a favor da opção (i) de H-130 — a esterilidade
extra parece não introduzir estrutura nova entre os tipos que
sobrevivem, apenas remove os que não sobrevivem, consistente com o
Teorema 3.3 já não ser afetado. Combinado com o argumento analítico de
auto-similaridade (ver atualização em H-130: o primeiro passo da raiz
contribui o fator $2^{-a_0(i)\theta}$, e tudo depois é estatisticamente
idêntico entre tipos não-estéreis, incluindo a mistura com classes
estéreis encontradas mais fundo — que afeta $W^*$ igualmente para todo
tipo de origem, não a razão entre tipos), isso é razoavelmente
conclusivo para a opção (i), sem ser uma prova formal completa.

## Como reproduzir

```
python3 experiment_type_rescaling_q7.py
```

~11 segundos (ambos os q juntos), sem dependências além da biblioteca
padrão. `tree_lib.py` é uma cópia isolada (sem código de demonstração/
efeitos colaterais de import) de `count_tree`/`CYCLES` de
`E-097-qx1-empirical-gate/empirical_qx1_tree.py`.
