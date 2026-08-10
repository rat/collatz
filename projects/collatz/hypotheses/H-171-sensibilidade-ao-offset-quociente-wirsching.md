# H-171: o diagnóstico de quantis de H-168 depende do deslocamento `d`

Status: fechada-confirmada (2026-08-10), ver seção final

Criada: 2026-08-10

Origem: H-168, ao rodar `central_quantiles.py` (E-135) até `ell=16`.

## Observação

H-168 propõe um teste direto: comparar um quantil fixo baixo da
distribuição de `R_ell(k,a) = g_ell(k,a)/gbar_ell(k)` sobre unidades
`a` mod `3^ell`, em `k=ell+d`, contra o mínimo. Se o quantil ficar
plano em `ell` enquanto o mínimo cai, a queda do mínimo é estatística
de extremos; se o quantil também cair, é deterioração real da cauda.

Rodando esse teste em dois deslocamentos, ambos dentro da janela de
Wirsching `|ell-k_ell|<=delta*sqrt(ell)`, os dois deslocamentos dão
veredictos opostos:

```text
d=+5  (suporte completo desde ell=10): q=1e-3 fica achatado em
      ~0,10-0,12 de ell=10 a 16 enquanto o mínimo é ruidoso e pequeno
      (0,02-0,07). Veredito: estatística de extremos.

d=+12 (suporte completo desde ell=4): q=1e-4 cai de 0,402 (ell=10)
      para 0,276 (ell=16), razão ~0,94/nível, perto da razão do
      próprio mínimo. Veredito: deterioração real da cauda.
```

Ambos os deslocamentos são membros legítimos da janela de Wirsching.
Parte da queda em `d=+12` é deriva do conjunto (a mediana também cai,
de 1,011 para 0,953), mas normalizar `q=1e-4` pela mediana em vez de
por 1 ainda decai a taxa próxima de 0,94/nível; a mesma normalização em
`d=+5` faz a coluna já achatada de `q=1e-4` subir levemente (0,053 para
0,093). A discrepância entre os dois deslocamentos sobrevive à
normalização pela mediana.

## Por que isto é uma pista nova, não um erro de medição

O teste de H-168, tomado ao pé da letra, não dá uma resposta única: ele
dá respostas diferentes dependendo de qual `d` se escolhe, e nada no
enunciado de `(?3)` privilegia um `d` sobre o outro (a condição exige a
desigualdade para TODO `ell>=ell_0` e toda sequência admissível
`k_ell`, logo se falha em qualquer `d` admissível, `(?3)` já falha
naquele `d`). Isso sugere que a "estatística de extremos vs.
deterioração real" não é uma dicotomia limpa aqui: o comportamento pode
depender de quão perto o deslocamento está do centro da janela (onde o
suporte é mais escasso e mais unidades "novas" de representante grande
entram na base do quantil) versus da borda (onde o suporte já está
maduro há mais níveis).

## Pergunta

O veredicto do teste de quantil fixo é monótono em `d` (por exemplo,
sempre "extremos" perto do centro da janela e sempre "cauda real" longe
dele, com uma transição em algum `d_c(ell)`), ou oscila sem padrão?
Se for monótono, o valor de `d_c` diz algo sobre a escala em que a
"nova massa" de resíduos com representante grande entra na base do
quantil, o que poderia separar, por construção, o efeito de tamanho de
conjunto do efeito de deterioração de cauda que H-168 tenta isolar de
outra forma (via conjuntos fixos de inteiros).

## Próximo passo (delimitado)

Rodar `central_quantiles.py` numa grade de deslocamentos intermediários
(`d=6,7,8,9,10,11`) até `ell=16`, mesma bateria de quantis, e checar se
o veredicto muda monotonicamente ou não. Não é um projeto novo: é uma
extensão de uma tarde do mesmo script já escrito para E-135. Se a grade
mostrar uma transição limpa, documentar aqui e decidir se isso merece
promoção a uma seção própria do paper 05; se for ruído sem padrão,
fechar como `closed-inconclusive` e não perseguir mais.

## 2026-08-10: grade de deslocamentos, resultado limpo

Rodada `central_quantiles.py --max-ell 16 --offsets 6 7 8 9 10 11`
(mesma recursão de `central_ratio.py`, ver E-135). Resultado: `d=6` a
`d=11` formam uma família consistente, cada um com `q=10^-3` em queda
suave e regular ao longo de `ell=10..16`:

```text
d      q=1e-3(ell=10)   q=1e-3(ell=16)   razão aprox./nível
 6         0,170            0,131             0,955
 7         0,232            0,163             0,940
 8         0,274            0,191             0,939
 9         0,331            0,218             0,933
10         0,369            0,242             0,932
11         0,394            0,265             0,933
```

Nenhum desses seis deslocamentos fica achatado; todos decaem a taxas
próximas (0,93 a 0,96 por nível), a mesma faixa que `d=+12` já mostrava
isoladamente. Só `d=+5` (o teste original de H-168) foge do padrão.

`d=+5` não é um ponto genérico da janela: é exatamente o primeiro
custo com suporte completo em cada nível, medido de forma independente
por `central_zeros.py` desde E-115 (o "primeiro custo cheio" é
`ell+5` para todo `10<=ell<=18`). Nesse deslocamento específico, boa
parte da massa da distribuição em níveis baixos vem de resíduos cuja
contagem `g_ell(k,a)` acabou de deixar de ser zero, um regime de
fronteira qualitativamente diferente do que `d>=6` mede, onde o
suporte já está maduro havia vários níveis.

**Resposta à pergunta da hipótese**: o veredito é monótono em `d`, não
oscila sem padrão, uma vez que se separa a fronteira de suporte
(`d=+5`) do interior da janela (`d>=6`). O interior da janela decai de
forma consistente. Isso não resolve H-168 (o "próximo passo" original
de H-168, comparar quantil e mínimo, ainda enfrenta o confundidor de
tamanho de conjunto descrito lá, agora reforçado pela composição do
bucket inferior medida na mesma sessão), mas resolve a pergunta
própria desta hipótese: a sensibilidade ao deslocamento tem uma causa
estrutural identificada, não é ruído.

Fecha como `closed-confirmed`: a hipótese de que o veredito depende de
`d` de forma sistemática (não arbitrária) se confirma, com a fronteira
de suporte como explicação.
