# H-015 — Busca sistemática de coalescências (generalização de H-014)

Status: confirmada como técnica geral (2374 classes novas excluídas, 69.3% de mod 2^16); não resolve H-008 por construção
Criada em: 2026-07-13
Origem: ideia mais ambiciosa do brainstorm do modelo Fable ("H-C"), com
escopo reduzido para ser tratável nesta sessão.

## Enunciado

H-007 e H-014 são os dois casos mais simples de uma família maior: pares de
progressões aritméticas cujas órbitas colidem ("coalescem") em poucos passos,
excluindo uma classe residual inteira do conjunto de possíveis recordistas.
Propomos uma busca sistemática (não a busca completa de profundidade
8-10 sugerida pelo Fable, que exigiria tratar módulos 2 e 3 conjuntamente —
escopo maior que o tratável agora) restrita a: **classes residuais mod 2^d,
comparando N com N−k para k pequeno**, generalizando exatamente a técnica de
H-014 (que é o caso d=3, k=1).

## Método simbólico

Para N ≡ r (mod 2^d), representamos N = 2^d·K + r (K livre). Simulamos a
órbita simbolicamente: enquanto o "coeficiente" de K permanecer par, o
próximo passo (par ou ímpar) é determinado só pela parte conhecida (r), sem
depender de K. Isso continua até termos consumido as d divisões conhecidas,
quando o coeficiente de K vira ímpar (uma potência de 3) e a órbita deixa de
ser previsível sem mais bits.

Para dois candidatos N=2^d·K+r₁ e M=N−k=2^d·K+r₂ (mesmo K, r₂=r₁−k, k
pequeno), simulamos ambos até esse ponto. Se os pontos finais (coeficiente,
constante) baterem exatamente, as órbitas colidem — e se M levou menos ou
igual passos que N para chegar lá, total_stopping_time(M) ≥
total_stopping_time(N) **para todo K**, excluindo N como recordista (M<N
sempre, por construção).

## Como testar

Para d de 2 a 12, r₁ de 0 a 2^d−1, k de 1 a 30 (com r₁≥k): simular
simbolicamente as duas trajetórias; registrar toda coalescência encontrada
com steps(M) ≥ steps(N); verificar contra os 148 recordistas oficiais quais
classes novas (além de mod3=2 e mod8=5, já explicadas) ficam confirmadas
como vazias.

## Atualizações

- 2026-07-13: hipótese aberta.
- 2026-07-13: testada em `experiments/E-015-systematic-coalescence-search/`.
  Busca d=2..16, k=1..40 encontrou 2374 classes residuais genuinamente novas
  (além de H-014), excluindo cumulativamente 69.3% dos resíduos mod 2^16.
  Verificação contra órbitas reais revelou efeito de borda para K pequeno
  (resolvido testando K≥10, onde bate exatamente). 6 dos 148 recordistas
  oficiais "violam" alguma exclusão, mas todos são números muito pequenos
  (3,6,7,9,18,25) — exceções esperadas, análogas ao N=2 de H-007. **Não
  resolve H-008** (classe 4 mod 9) por limitação estrutural: mod 2^d e mod 9
  são coprimos, então esta técnica nunca poderia dizer nada sobre mod 9.
  Confirmada como técnica geral válida, mas não fecha a questão em aberto.
