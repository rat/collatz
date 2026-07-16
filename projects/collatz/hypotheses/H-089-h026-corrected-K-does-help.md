# H-089 — H-026 corrigida: K maior REDUZ a incerteza sobre G(v), contrariando a conclusão original

Status: confirmada (H-026 revertida — conclusão original estava errada por testar a variável errada)
Criada em: 2026-07-16
Origem: consulta ao Fable pedindo revisão da metodologia de H-026. Ele
confirmou (por aritmética direta, sem rodar nada) que os valores
relatados em H-026 batem quase exatamente com o termo trivial de
magnitude −ln(v/v₀) identificado em H-086 — ou seja, H-026 mediu D(v)
bruto, dominado pelo mesmo efeito de magnitude que H-024 tinha, em vez
do resíduo G(v)=D(v)·v que H-087 já mostrou ter continuidade 3-ádica
real. Ele propôs um desenho de teste corrigido, implementado aqui.

## A pergunta original de H-026 (não resolvida corretamente antes)

Fixando um resíduo mod 3^K, a "previsão" de memória-K para D(v) diverge
do valor real conforme v cresce (mantendo o resíduo fixo). H-026
perguntava: **K maior atrasa essa divergência** (funciona por mais
tempo antes de errar)? A resposta original foi "não, a divergência
depende só da magnitude, K não ajuda" — mas essa conclusão comparava
D(v) bruto numa única medição por célula, sem separar o efeito trivial
de magnitude do efeito de resíduo.

## Por que a resposta original estava matematicamente pré-determinada a dar "não"

Como o Fable mostrou por aritmética direta: se D(v)≈C/v (H-086), então
log(D(v)/D(v₀)) = −log(v/v₀) + log(G(v)/G(v₀)). O primeiro termo é
determinístico e, nas magnitudes testadas por H-026 (log₂v de 13 a 21),
vale de −4,9 a −9,8 — enquanto o efeito real de K (que vive inteiro no
segundo termo) é de apenas ~0,1-0,4 dex. H-026 estava comparando três
cópias quase idênticas de um número dominado por um termo que nada tem
a ver com K — a conclusão "K não ajuda" era numericamente garantida
pelo desenho, não uma descoberta.

## O teste corrigido

`experiments/E-089-h026-corrected/experiment.py`: mede a dispersão
(desvio-padrão) de log₁₀(G(v)) — não uma única medição, mas a variação
de G dentro de uma **janela de magnitude fixa e controlada**, com o
resíduo mod 3^K fixo (cadeias nested, cada K refinando a anterior).
Repetido com 5 cadeias de resíduo independentes e 3 janelas de
magnitude distintas (log₁₀v em [6,6.6), [7,7.6), [8,8.6)), para K∈
{2,4,6,8}.

**Bug encontrado e corrigido no caminho**: uma primeira tentativa usou
janelas de magnitude estreitas demais para K grande — o espaçamento
entre valores do mesmo resíduo mod 3^K pode exceder a largura da
janela, fazendo a amostragem repetir o mesmo v (variância artificial
igual a zero). Corrigido verificando explicitamente que a janela
contém valores distintos suficientes antes de amostrar, e usando
janelas mais largas (magnitude ~10⁶ a 10⁸·⁶, garantindo centenas de
valores distintos possíveis mesmo para K=8).

## Resultado

| K | dispersão média de log₁₀(G) (3 janelas × 5 cadeias) |
|---|---|
| 2 | 0,2352 |
| 4 | 0,1748 |
| 6 | 0,1444 |
| 8 | 0,0936 |

**A dispersão cai monotonicamente e de forma consistente em todas as
3 janelas de magnitude testadas** — redução de ~2,5× entre K=2 e K=8.
Isso confirma decisivamente: **K maior reduz a incerteza sobre G(v)**,
mesmo controlando rigorosamente a magnitude — o oposto exato da
conclusão original de H-026 ("não há evidência de que K=8 aguenta mais
que K=4").

## Conclusão

**H-026 estava errada, não só "fraca"**: não foi uma medição ruidosa
que por acaso não achou o efeito — foi uma medição da variável errada
(D bruto em vez de G=D·v), que garantia matematicamente a conclusão
"K não importa" independente da verdade sobre G. Testando a variável
certa, com controle rigoroso de magnitude e replicação entre cadeias
independentes, o resultado inverte: **K maior sim ajuda**, consistente
com H-087 (continuidade 3-ádica de G) e com o argumento geral de
H-024/H-086 (D(v) fatora aproximadamente como C(v)·G(v mod 3^k), e é
G, não D, que carrega qualquer estrutura de resíduo tratável).

## Atualizações

- 2026-07-16: consulta ao Fable identificou o erro de variável em
  H-026. Testado com desenho corrigido (dispersão de G em janelas de
  magnitude controladas, múltiplas cadeias de resíduo). Resultado
  inverte a conclusão original: K maior reduz a dispersão de forma
  clara e consistente (0,2352→0,0936, K=2 a K=8). H-026 deve ser
  considerada revertida/superada por esta hipótese.
