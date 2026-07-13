# Protocolo — Novo Experimento

Um "experimento" aqui é qualquer verificação computacional, cálculo numérico ou teste
que gere evidência a favor ou contra uma hipótese.

1. Crie uma pasta em `projects/<projeto>/experiments/E-XXX-titulo-curto/` contendo:
   - o script/código usado;
   - um `README.md` curto com: hipótese relacionada, o que foi testado, resultado,
     como reproduzir.
2. Resultado precisa ser reprodutível: outra pessoa (ou outra sessão) deve conseguir
   rodar o mesmo script e obter o mesmo resultado.
3. Atualize a hipótese relacionada em `hypotheses/` com o resultado (suporta, refuta,
   inconclusivo).
4. Referencie o experimento em `STATE.md` se o resultado mudar o rumo da pesquisa.

## Armadilha conhecida — colisão de órbitas (pseudo-replicação)

Órbitas de Collatz colidem: uma vez que duas trajetórias diferentes atingem o
mesmo valor intermediário, toda a cauda seguinte é idêntica entre elas. Qualquer
experimento que agregue estatísticas ao longo de **múltiplas posições de
múltiplas órbitas** (em vez de uma observação por trajetória) corre o risco de
contar o mesmo trecho de caminho várias vezes, inflando artificialmente a
significância estatística (ver `experiments/E-001-parity-independence/README.md`
para um caso real onde isso produziu um "sinal" espúrio). Ao desenhar um
experimento estatístico sobre órbitas, prefira amostrar números iniciais
distintos e espalhados (idealmente grandes o suficiente para tornar colisão
improvável no trecho analisado) e verifique explicitamente a ausência de
colisões, em vez de agregar posições de dentro da mesma árvore de trajetórias.

## Armadilha conhecida — funções "aceleradas" que assumem paridade da entrada

Funções que implementam o passo acelerado de Collatz (`m=3n+1` seguido de
dividir todos os fatores de 2) só fazem sentido se `n` for ímpar — se chamadas
com `n` par, aplicam "3n+1" indevidamente e retornam um resultado errado **sem
lançar erro** (ver `experiments/E-007-why-record-holders-avoid-2-mod-3/README.md`
para um caso real: `total_steps_only(2)` retornou 17 em vez do correto 1).
Isso nunca afetou os scans principais (que sempre iteram só sobre ímpares),
mas pegou uma verificação ad-hoc de desprevenida. Ao escrever uma função nova
que assume paridade da entrada, deixe isso explícito (nome, docstring, ou um
`assert n % 2 == 1`) — ou, melhor, use sempre uma versão genérica (mapa padrão,
sem assumir paridade) ao testar algo com números arbitrários.

## Armadilha conhecida — nunca reconstruir dados de memória

Ao caracterizar o resultado de um experimento (ex: contar resíduos de uma lista
de números especiais), **nunca digite a lista de memória ou por aproximação**.
Use sempre a saída real do script (re-execute se necessário) ou um arquivo de
dados salvo no repositório. Um caso real: em `experiments/E-004-true-record-holders/CORRECTION.md`,
uma lista de recordistas foi reconstruída de memória para uma análise
posterior, e continha 4 valores incorretos que distorceram a conclusão inicial
— o código estava certo, só a transcrição manual estava errada. Sempre que
possível, prefira usar uma fonte de dados externa verificável (ex: OEIS) e
salvá-la no repositório, em vez de confiar em regenerar valores de memória.
