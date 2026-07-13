# H-006 — Viés mod 3 em top-K stopping times (mais poder estatístico que H-004)

Status: não suportada como formulada (ver E-006 — diagnóstico útil, populações diferentes)
Criada em: 2026-07-13

## Enunciado

H-004 encontrou, em apenas 57 recordistas reais (n até 20-50M), forte
sub-representação de resíduo 2 mod 3 (2/57, esperado ~19). Amostra pequena
demais para conclusão firme. Propomos testar a mesma pergunta com muito mais
poder estatístico: em vez de exigir "recordista estrito" (bate todo m < n),
pegar os top-K números por stopping time total num intervalo grande (K ~
500-2000) — um grupo bem mais numeroso mas ainda extremo — e ver se o mesmo
viés mod-3 aparece, e com que magnitude.

## Motivação

- Se o viés mod-3 é um fenômeno real ligado a "ter stopping time
  excepcionalmente alto", deveria aparecer também no top-K mais amplo, não só
  nos recordistas estritos.
- Se o viés desaparecer ou diluir no top-K (aproximando de 1:1:1), isso sugere
  que o achado de H-004 pode ter sido uma flutuação de amostra pequena após
  tudo, mesmo tendo sobrevivido a duas seeds.

## Como testar

1. Escanear n ímpar até um limite grande, mantendo os top-K por stopping time
   total (heap, sem guardar todos os valores — H-004 já mostrou que escanear
   ~50M é viável em alguns minutos).
2. Comparar resíduo mod 3 (e mod 9, mod 5/7 como controle) do grupo top-K
   contra uma amostra típica, com o mesmo cuidado de validade estatística
   (checar contagem esperada por célula) usado em E-004.

## Atualizações

- 2026-07-13: hipótese aberta.
- 2026-07-13: testada em `experiments/E-006-topk-stopping-time-mod3/`. Nenhum
  viés mod-3 detectado no top-K bruto (K=200-1000, limite 1M-30M). Diagnóstico:
  top-K bruto e "recordista estrito" são populações diferentes (só 5/50 do
  top-K coincidem com recordistas reais) — isso não refuta H-004, só mostra
  que o viés é específico de recordistas estritos. Esse diagnóstico ajudou a
  identificar um erro de transcrição na análise original de H-004 (ver
  `experiments/E-004-true-record-holders/CORRECTION.md`), que foi corrigido e
  confirmado com dados oficiais (OEIS A006877, n=148).
