# H-034 — Vídeo "Messing Around with Math": redescoberta da equação de ciclo, e extensão de H-009

Status: confirmada (achado do vídeo refutado tecnicamente; H-009
estendido de forma honesta até um limite combinatório bem quantificado)
Criada em: 2026-07-13
Origem: diretor científico compartilhou transcrição de um vídeo
("Messing Around with Math") onde o autor, de forma informal e não
rigorosa ("só brincando por algumas horas"), redescobre a técnica
clássica de equação de ciclo (usada por Steiner 1977, Simons 2005, Simons
& de Weger 2005 — já catalogada em `literature/nontrivial-cycles.md`).

## O que o vídeo faz (avaliação técnica)

O autor busca ciclos não-triviais fixando um número de passos de
multiplicação (×3+1) e divisão (÷2), montando a equação algébrica que
`n₀` precisa satisfazer para fechar um ciclo com essa contagem de passos,
e testando se a solução é um inteiro. Isso é **exatamente** a técnica
profissional padrão (a mesma que já implementamos em H-009/E-009). O
autor também nota corretamente, por conta própria, que passos de
multiplicação não podem ser consecutivos (trivial: ×3+1 sempre produz um
número par) e que, numa sequência cíclica, o primeiro e o último passo
não podem ambos ser multiplicação (senão a paridade de entrada do
primeiro passo contradiz a paridade de saída do último) — uma restrição
correta, que já está automaticamente embutida em qualquer formulação
rigorosa (inclusive a nossa), não uma descoberta nova, mas um raciocínio
sólido para quem chegou lá sozinho.

## O achado específico do vídeo (n=13 para 3 mult + 5 div) — REFUTADO

O vídeo alega ter encontrado n=13 como solução candidata para um ciclo
com 3 multiplicações e 5 divisões (S=5), que "quase" fecha mas falha no
último passo. **Testei com a fórmula correta e verificada** (a mesma de
H-009): para a=3, S=5, **nenhuma das 6 ordens possíveis de divisão produz
um candidato inteiro positivo**. A alegação do vídeo não se sustenta sob
derivação rigorosa — mais provavelmente um erro na álgebra informal feita
de cabeça/à mão durante a gravação (consistente com o próprio autor
admitir que o vídeo "não é sério").

## Extensão de H-009 além de a=14

Tentei estender nossa própria busca exaustiva (H-009 foi até a=14, janela
S∈[S_min, S_min+20]) para além disso, usando o mesmo método (equação +
verificação de autoconsistência via simulação real).

**Parede combinatória quantificada precisamente**: o número de composições
a testar cresce como C(S−1, a−1), que explode rapidamente:
- a=14: ~497 mil composições no S mínimo.
- a=18: ~21 milhões no S mínimo.
- a=20: ~141 milhões no S mínimo.
- a=22: ~928 milhões no S mínimo.
- a=25: ~25 **bilhões** no S mínimo.

Com janela reduzida a **apenas S=S_min** (o caso mais "apertado" e mais
provável a priori), consegui uma verificação **completa e limpa** (sem
nenhum par pulado) até **a=16** — nenhum ciclo novo encontrado, só o
trivial (n₀=1) repetido. Além de a=16 (mesmo só no S mínimo), a
combinatória já supera o que é razoável rodar sem otimização adicional.

## Por que isso confirma (não desafia) o método dos profissionais

Isto explica **com números concretos** por que Simons & de Weger (2005)
precisaram de algo mais esperto que força bruta para chegar a a=68: não é
uma questão de "mais poder computacional" — o crescimento combinatório é
tão rápido que nem datacenters resolveriam isso por enumeração pura muito
além de a≈20-25. A técnica real deles usa frações contínuas de log₂(3)
(a mesma conexão que testamos e descartamos para H-013 em H-032, mas que
aqui *é* genuinamente a ferramenta certa) para restringir quais valores
de S sequer precisam ser considerados para cada a, e provavelmente
argumentos adicionais (tipo redução de reticulado ou cotas de Baker) para
evitar enumerar composições completamente. Reproduzir isso exigiria
implementar essa maquinária mais sofisticada — um projeto separado, não
uma tarde de continuação.

## Conclusão

Contribuição honesta e completa: (1) tecnicamente refutamos o achado
específico do vídeo (n=13 não é solução sob a fórmula correta); (2)
estendemos nossa própria verificação de H-009 até a=16 (de a=14) de forma
limpa numa janela mais estreita; (3) quantificamos precisamente onde e
por que a força bruta pura deixa de ser viável, conectando isso
diretamente à razão pela qual a literatura profissional precisa de
métodos mais sofisticados — não é falta de tentativa, é uma barreira
combinatória real e agora bem entendida por nós.

## Atualizações

- 2026-07-13: vídeo avaliado tecnicamente, achado específico refutado,
  H-009 estendido com honestidade sobre os limites exatos alcançados.
