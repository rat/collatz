# Protocolo — Checkpoint de fim de sessão

Objetivo: garantir que nada se perde entre sessões. Este repositório é a memória do
laboratório — se não está commitado, não aconteceu.

1. Atualize `projects/<projeto>/STATE.md`:
   - o que mudou nesta sessão;
   - hipóteses novas/atualizadas;
   - próximos passos concretos para a próxima sessão.
2. Rode `scripts/checkpoint.sh "mensagem descritiva"` — isso faz `git add -A`,
   `git commit` e `git push`.
3. Se algo ficou pela metade, registre isso explicitamente em `STATE.md` em vez de
   deixar implícito no código.
