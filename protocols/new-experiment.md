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
