# E-079 — Revisão de Getachew, "Unfolding the Collatz Tree: An Indirect Structural Proof" (2025)

Hipótese relacionada: [`H-079-getachew-2025-review.md`](../../hypotheses/H-079-getachew-2025-review.md)

**ALEGAÇÃO DE PROVA COMPLETA — REFUTADA.**

## O que foi feito

O paper (item 109) constrói a árvore reversa de Collatz — a mesma
construção de H-018/E-018 deste projeto — e alega provar a conjectura
mostrando que a árvore (1) cobre todo n∈ℕ, (2) é acíclica exceto pelo
ciclo trivial, e (3) todo caminho de volta à raiz é finito.

## O furo lógico central

A relação "pai" definida no paper (Remark 1) é **idêntica ao mapa de
Collatz direto**: parent(m)=m/2 (par) ou 3m+1 (ímpar). Logo, "caminho de
volta até a raiz" É a órbita direta de Collatz. O Lemma 4.3 (todo
caminho de volta é finito) não decorre de "acíclico + pai único" —
aciclicidade e unicidade de pai garantem que o caminho não repete nem
bifurca, mas **não garantem que seja finito**. O lemma é logicamente
equivalente à própria conjectura, apresentado como se decorresse de
propriedades estruturais mais fracas.

O Teorema 5.1 (cobertura) sofre do mesmo problema por outro caminho: a
fórmula de indexação que ele soma é só a decomposição única
ímpar×potência-de-2 de qualquer inteiro — um fato aritmético universal,
independente de qualquer regra de ramificação de Collatz.

## Verificação computacional

Confirmamos: (1) o Teorema 5.1 está correto mas é tautológico
(independente de g(n)); (2) parent(x)=f(x) exatamente; (3) o número 27
é, em princípio, alcançável a partir da raiz (o caminho reverso de sua
órbita satisfaz a regra de ramificação em todos os 111 passos), mas uma
busca direta a partir da raiz (sem atalho) não o encontra dentro de
milhões de nós processados — evidência concreta de que "cobertura" não
pode ser estabelecida por um argumento combinatório como o do Teorema
5.1, sem verificar Collatz diretamente.

## Resultado

Não é uma prova válida. Ver H-079 para a análise completa da anatomia
do erro (petição de princípio disfarçada por reformulação em linguagem
de teoria dos grafos).

## Reproduzir

```
python3 experiment.py
```
