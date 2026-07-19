# E-048 — Verificação do paper #006 (Michael Mark Anthony, "A Two-Field Propagation Model for the Collatz Map")

## Objetivo

Verificar "A Two-Field Propagation Model for the Collatz Map" (Michael
Mark Anthony, Enertron Inc., 17 páginas). Paper elaborado, com muito
aparato matemático (equação P de Riemann, monodromia, PGL(2,C), função
digamma, hipergeometria, 24 soluções de Kummer) — mas honesto e
explícito, em várias seções, sobre não estender resultados conhecidos
nem provar a conjectura.

## O que fizemos

Verificamos computacionalmente as reivindicações centrais checáveis:

1. **Reformulação Möbius Φ(n)=1/(n+1)** (Proposição 5.1): confirmada
   em 4999 casos — M_E e M_O reproduzem exatamente Φ(T(n)).
2. **Teorema 8.1** (regime m=1 não persiste indefinidamente): maior
   corrida encontrada até n=200.000 foi de 16 passos; a construção
   explícita n₀=2^(t+1)-1 sustenta exatamente t passos como previsto
   pela prova por indução 2-ádica do próprio teorema.
3. **Exemplo trabalhado da Seção 9** (n=7): trajetória confirmada
   exatamente.
4. **Teoremas 10.3/10.4** (identidade harmônica exata H_q=ψ(q+1)+γ e
   limite de Euler-Mascheroni): confirmados via `mpmath` (50 dígitos
   de precisão) — fatos padrão da função digamma, não específicos do
   Collatz, mas corretamente usados.
5. **Identidade hipergeométrica da Eq.28** (ψ(z)=(z-1)·₃F₂(1,1,2-z;2,2;1)-γ):
   confirmada numericamente para vários z.

## Resultado

**Nenhum erro encontrado** em nenhuma reivindicação testável. O paper é
notavelmente cuidadoso ao longo de TODO o texto (Remarks 5.2, 6.1,
10.1, 11.1, 12.1, 14.1, e a Seção 16 inteira) em distinguir: o que é
teorema provado sobre a reformulação; o que é analogia estrutural, não
identificação literal ("this is an analogy of form, not of kind"); o
que é heurístico/condicional (o "Collapse Theorem" 14.1 é explicitamente
rotulado "conditional...consistent with, but not a proof of, the
conjecture"); e onde não há extensão de resultados conhecidos (Seção
12 sobre o resultado de Tao). O próprio autor identifica e corrige,
dentro do texto, uma reivindicação anterior equivocada (δ_m=1/m, Seção
10) — sinal de prática de pesquisa cuidadosa.

Muito do aparato (equação P, monodromia, PGL(2,C), digamma,
hipergeometria, Kummer) funciona mais como contexto/analogia decorativa
do que como conteúdo matemático com peso real sobre a conjectura — o
próprio paper concorda com essa leitura (Seção 16).

Ver `hypotheses/H-048-anthony-two-field-propagation-review.md`.

## Como rodar

```
/home/rat/.venv/bin/python3 experiment.py
```

Requer `mpmath` (já instalado no venv do projeto).
