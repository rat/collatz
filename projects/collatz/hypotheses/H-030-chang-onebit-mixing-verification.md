# H-030 — Verificação independente do paper de Chang (2026) sobre "one-bit orbit mixing"

Status: confirmada (verificação bem-sucedida) + extensão honesta sem
achado surpreendente
Criada em: 2026-07-13
Origem: leitura de literatura recente ainda não revisada, motivada pela
instrução do diretor científico de continuar buscando ângulos genuinamente
novos, mesmo sem garantia de achar algo.

## O paper

[Edward Y. Chang (Stanford), "A Structural Reduction of the Collatz
Conjecture to One-Bit Orbit Mixing"](https://arxiv.org/abs/2603.25753)
(2026). Reduz a conjectura, dentro de um framework de "burst/gap" no mapa
de Syracuse comprimido, a uma pergunta muito específica: **o bit 4 do
valor de fim-de-burst determina o comprimento do próximo gap** (para a
classe dominante n≡1 mod8); a conjectura equivale a mostrar que essa
subsequência esparsa visita as classes 9 e 25 (mod 32) com equilíbrio
suficiente.

**Conexão notável com nosso próprio trabalho**: a "Rota A" do paper
(contração via sistema de transferência 5×5) trava exatamente no mesmo
tipo de obstrução que encontramos em H-024 — "at finer resolution (mod 16
and beyond), sub-fiber matrices do not all contract uniformly." Isso é
evidência independente (de outra fonte, outro método) de que esse tipo de
obstrução — aproximações de dimensão finita que não fecham por exigirem
resolução cada vez mais profunda — é um fenômeno recorrente e genuíno
nessa área, não uma peculiaridade da nossa derivação específica.

## O que foi testado

1. **Verificação independente** (nunca aceitar afirmação de paper externo
   sem checar) de três resultados centrais do paper:
   - Lema 4.1 (mecanismo mod-8 do comprimento de gap).
   - Teorema 4.2, "Map Balance Theorem" (|C₃(K)−C₇(K)|=1 para K≥5).
   - Mecanismo do "bit 4" (Seção 5.1), restrito corretamente aos valores
     de fim-de-burst (n≡1 mod8 com k=(n−1)/8 ímpar, i.e. n≡9 mod16).
2. **Extensão 1**: equilíbrio bit-4 em órbitas com n₀ maior que o testado
   no paper (que foi até 10⁹).
3. **Extensão 2**: equilíbrio bit-4 usando nossos próprios 148 recordistas
   reais de stopping time (órbitas excepcionalmente longas por
   construção) — um conjunto de teste que o paper não usou.

## Erros próprios encontrados e corrigidos no caminho

Dois bugs na PRÓPRIA verificação (não no paper), pegos por assert/teste
antes de reportar qualquer coisa:
1. Testei o mecanismo do bit-4 em todo n≡1 mod8, sem restringir a k=(n−1)/8
   ímpar (a condição que o paper de fato usa) — gerava "falhas" espúrias.
2. Ao calcular o comprimento do gap G, apliquei o teste mod-8 do Lema 4.1
   ao valor errado (n em vez de m=T(n), o valor que efetivamente inicia o
   gap) — dava G=2 sempre, mascarando os casos G=1.
Corrigidos antes de reportar; versão final: **zero falhas** nos três
testes, milhares de casos.

## Resultado

- Lema 4.1: confirmado, 0 falhas em 50.000 casos.
- Map Balance Theorem: confirmado exatamente para K=5..15.
- Mecanismo bit-4: confirmado, 0 falhas em 12.500 casos (restrito
  corretamente).
- Extensão 1 (órbitas aleatórias maiores, 10¹⁰–7×10¹²): amostras pequenas
  (poucas dezenas de burst-endings por órbita, já que órbitas típicas
  terminam rápido) — sem conclusão forte possível.
- Extensão 2 (148 recordistas reais): fração agregada de 0,6129 (9064
  observações) e média por órbita de 0,6196 (142 órbitas) — desvio de
  ~11-12 pontos percentuais de 0,5.

## Honestidade sobre a Extensão 2 (armadilha de pseudo-replicação evitada)

Um desvio de 0,61 com 9064 observações pareceria, ingenuamente, ~21 desvios-padrão
de significância sob a hipótese nula de 0,5 — um "achado" aparentemente
enorme. **Não caí nessa armadilha**: as 9064 observações vêm de só 142
órbitas de recordistas, e órbitas de recordistas **colidem** entre si —
isso é literalmente o que H-007/H-014/H-022 provam (a órbita de um número
menor passa pelo número maior). Confirmei diretamente: dos 45 pares entre
os 10 maiores recordistas testados, 8 pares (18%) compartilham pelo menos
um valor na cauda em uma janela de 500 passos — confirmando sobreposição
real, não hipotética. Isso invalida o cálculo ingênuo de significância
(a mesma lição de pseudo-replicação documentada desde H-001).

Mais importante: o desvio de ~11-12 pontos percentuais **não é surpreendente
nem novo** — o próprio paper já demonstra exatamente esse fenômeno na sua
Tabela 2 (órbitas genéricas grandes desviam ±10-25% de 0,5 no nível de
órbita individual, com a média teórica de 0,5 valendo só no agregado sobre
MUITAS órbitas independentes — ver Remark 6.3 do paper). Recordistas, por
serem órbitas selecionadas justamente por serem excepcionalmente longas
(H-021 já mostrou que têm runs de subida mais longos que o típico), são
exatamente o tipo de órbita não-genérica onde esse desvio de órbita-a-órbita
seria esperado ser grande — não é evidência contra a conjectura de
equilíbrio do paper, é uma reconfirmação (com ressalva de pseudo-replicação)
de um padrão que eles já documentaram e já esperavam.

## Fechamento definitivo (não é só pseudo-replicação — é tautológico com H-021)

Além da pseudo-replicação, há uma explicação mais direta e definitiva para
o desvio de 0,61: no framework de Chang, um "gap" (mod8=7, bit4=0, 9mod32)
é exatamente um passo de CRESCIMENTO (×1.5, sem a contração extra de um
burst) — gaps mais longos (G≥2) correspondem a runs de subida mais longos.
**H-021 já mediu isso diretamente**: recordistas têm runs de subida médios
de 2,512 passos vs. 2,035 típico (consequência de serem selecionados por
altura excepcional). Logo, recordistas mostrarem viés em direção a
9mod32 (G≥2, gaps mais longos) não é uma medição nova — é **H-021
reformulado na linguagem do paper de Chang**. Isso fecha o assunto com uma
explicação específica, não apenas uma ressalva metodológica genérica.

## Conclusão

Contribuição modesta e honesta: (1) verificamos independentemente que os
resultados centrais do paper de Chang (2026) estão corretos, pelo menos
nas partes finitas/computáveis que checamos; (2) identificamos uma conexão
real com nossa própria obstrução de H-024 (evidência cruzada de que esse
tipo de obstrução de "precisão infinita necessária" é recorrente na área);
(3) tentamos uma extensão com dados nossos (recordistas reais) e, em vez
de superclaimar um desvio aparentemente grande, aplicamos a mesma
disciplina de pseudo-replicação já estabelecida no projeto, concluindo
corretamente que o resultado não contradiz nem estende o problema aberto
do paper — apenas o reconfirma com uma amostra diferente.

## Atualizações

- 2026-07-13: paper lido, verificado independentemente (3 lemas centrais,
  0 falhas), extensão tentada com honestidade sobre suas limitações
  (pseudo-replicação identificada e corretamente neutralizada antes de
  reportar).
