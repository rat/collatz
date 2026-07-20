# E-109 — H-130: a família de escala por tipo sobrevive à esterilidade extra? (q=7)

## Hipótese relacionada

H-130 pergunta: quando 2 não é raiz primitiva mod q (ex.: q=7,
ord₇(2)=3<φ(7)=6, com resíduos {3,5,6} estéreis além de 0), a
esterilidade extra (i) só reescala a população total por um fator
constante, sem mudar α₋(q) (já confirmado — Teorema 3.3 bate
numericamente para q=7), ou (ii) introduz estrutura mais rica entre os
tipos não-estéreis restantes? A família de escala já confirmada para
q=5 (E-103 Estágio 4, todos os resíduos não-nulos não-estéreis, já
que 2 é raiz primitiva mod 5) prediz $W_i \sim 2^{-a_0(i)\theta}W^*$.
Este experimento testa se essa MESMA relação vale entre os 3 tipos
não-estéreis de q=7 ($\langle2\rangle=\{1,2,4\}$), apesar da
esterilidade extra em outras partes da árvore.

## Por que q=7 e não q=31

q=31 é o caso mais extremo da tabela de H-130 (só 5/30 resíduos
não-nulos não-estéreis), mas $\theta_{31}=\alpha_-(31)\approx0{,}0552$
é pequeno demais para um teste viável: crescimento populacional
$H^{0{,}0552}$ exigiria $H\sim10^{36}$ para dar até 100 amostras na
contagem — impraticável. q=7 ($\theta=0{,}373501$, já usado no resto
do projeto) é o teste viável mais próximo do espírito de H-130.

## Método

$a_0$ para os 3 tipos não-estéreis de q=7: $a_0(1)=3$, $a_0(2)=2$,
$a_0(4)=1$. Amostrei 5000 raízes ímpares por tipo (residuo mod 7 fixo,
excluindo o ciclo trivial $\{1\}$), enumerei a árvore reversa real até
headroom $10^7$ (`tree_lib.count_tree`, cópia isolada e sem efeitos
colaterais de `E-097/empirical_qx1_tree.py`), medi
$W_v=N_v(v\cdot H)/H^\theta$, e comparei razões entre tipos (média,
mediana, e média geométrica) contra a previsão
$W_i/W_j=2^{-(a_0(i)-a_0(j))\theta}$.

## Resultado

Com 5000 raízes por tipo, todas as 3 razões batem com a previsão a
2–4% (médias) — na mesma faixa de precisão do achado original de E-103
Estágio 4 para q=5 ("2–9%"):

```
W_1/W_4: observado=0.5705  previsto=0.5958  razao obs/previsto=0.9574
W_2/W_4: observado=0.7561  previsto=0.7719  razao obs/previsto=0.9796
W_1/W_2: observado=0.7545  previsto=0.7719  razao obs/previsto=0.9774
```

(mediana e média geométrica dão a mesma conclusão, ver saída completa).

**Conclusão para H-130**: a família de escala por tipo sobrevive
intacta entre os tipos não-estéreis, mesmo quando existem tipos
estéreis extras alhures na árvore (q=7). Isso é evidência a favor da
opção (i) de H-130 — a esterilidade extra parece não introduzir
estrutura nova entre os tipos que sobrevivem, apenas remove os que não
sobrevivem, consistente com o Teorema 3.3 já não ser afetado. Não é
uma prova geral (testado só para q=7, um caso), mas é a primeira
evidência direta, não apenas teórica, sobre a pergunta.

## Como reproduzir

```
python3 experiment_type_rescaling_q7.py
```

~11 segundos, sem dependências além da biblioteca padrão. `tree_lib.py`
é uma cópia isolada (sem código de demonstração/efeitos colaterais de
import) de `count_tree`/`CYCLES` de
`E-097-qx1-empirical-gate/empirical_qx1_tree.py`.
