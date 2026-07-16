# E-070 — Verificação do paper #099 (Lodders, "Selection Rules and Channel Structure in a Base-Octave Model of Collatz Dynamics") — ALEGAÇÃO DE PROVA

Hipótese relacionada: [`H-070-lodders-base-octave-review.md`](../../hypotheses/H-070-lodders-base-octave-review.md)

## Paper

Lodders, K. (2026). *Selection Rules and Channel Structure in a
Base–Octave Model of Collatz Dynamics*. arXiv:2604.20181, 60 páginas
(não peer-reviewed). PDF local:
`literature/papers/099_Selection-Rules-Channel-Structure-Base-Octave.pdf`
(nome de arquivo com numeração trocada no download — o conteúdo é do
item 099; item 098 não tem PDF livre, ver `INDEX.md`).

## Veredito

**NÃO é uma prova válida.** O paper reformula Collatz num "modelo
base-octava" (h=B+8(A-1)), deriva 16 regras de transição entre 8 classes
de base (Seção 5) e identifica a classe B=7 (com índice de octava A par)
como o único canal capaz de sustentar crescimento persistente. Até aqui,
correto — verificado. O paper então afirma (Theorem 9.6.8) que toda
trajetória de Collatz está confinada à bacia terminal {1,2} — **alegação
de prova completa** — apoiada no Corollary 9.6.7 (o índice de octava A,
na entrada de episódios sucessivos de persistência base-7, deve
decrescer estritamente), por sua vez apoiado numa enumeração exaustiva
de "22 caminhos de retorno" num sistema de 128 estados (Apêndice A2).

**O Corollary 9.6.7 é falso.** O próprio exemplo citado pelo paper na
Introdução (n=27, "requer substancialmente mais passos que valores
vizinhos") já o viola: seus episódios de persistência base-7 têm
v2(A_entrada) = 2, 1, 3, 1 — o salto de 1 para 3 contradiz diretamente
"deve decrescer estritamente". Em escala (N até 500.000), 56,7% de todos
os pares de episódios sucessivos violam a alegação — não é um caso raro
de borda.

## O que foi testado

1. Codificação base-octava e mapa acelerado, validados contra o exemplo
   próprio do paper (trajetória de h1=7, página 22) e a Tabela 2.
2. As 16 regras de seleção (Seção 5, Casos 1-4) — 31.992 pares (B,A)
   testados, 0 falhas.
3. Proposition 8.4 (comprimento do episódio de persistência ≤
   v2(A_entrada)) — 515.342 episódios testados, 0 falhas.
4. **Corollary 9.6.7** (resultado principal) — falsificado com o próprio
   exemplo do paper (n=27, n=31) e em escala (988.476 pares de episódios
   testados, 560.682 falhas).

## Como reproduzir

```
python3 experiment.py
```

Sem dependências além da stdlib. Roda em menos de 2 minutos.
