# E-065 — Verificação do paper #049 (Boyle, "The Collatz Conjecture is True") — ALEGAÇÃO DE PROVA

Hipótese relacionada: [`H-065-boyle-collatz-proof-review.md`](../../hypotheses/H-065-boyle-collatz-proof-review.md)

## Paper

Boyle, D.G. (2026). *The Collatz Conjecture is True*. rxiverse.org
(não peer-reviewed). PDF local:
`literature/papers/049_The-Collatz-Conjecture-is-True.pdf`.

## Veredito

**NÃO é uma prova válida.** Gap fatal localizado no Lemma 4.2: o paper
deriva `e=2/3, o=1/3` (frações assintóticas de passos pares/ímpares)
sob a hipótese de "n aleatório" (Teorema 3.2 — um argumento de
densidade/ensemble), depois substitui esses valores diretamente numa
alegação sobre UMA trajetória hipotética específica e fixa (a gerada
por `n+1`, suposta divergente). É a clássica falácia do "argumento do
passeio aleatório" — heurística útil para intuição, não uma prova.

## O que foi testado

1. Aritmética das exclusões de ciclo de 2, 3, 4 termos — correta.
2. Busca exaustiva da equação diofantina `2^(n+1)-3^m=1` (incluindo o
   caso `n+1` ímpar que o paper não trata) — conclusão numérica do
   paper sobrevive, mas a demonstração como escrita tem uma lacuna.
3. Aritmética da série geométrica (limite = 2/3) — correta.
4. **Demonstração quantitativa**: fração de passos pares realizada por
   3.000 trajetórias individuais completas — desvio-padrão 0,031,
   10,2% desviam de 2/3 por mais de 0,05, mostrando que "2/3" é uma
   média de ensemble, não uma restrição por trajetória.

## Como reproduzir

```
python3 experiment.py
```

Sem dependências além da stdlib. Roda em alguns segundos.
