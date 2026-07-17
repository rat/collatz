# H-122 — Ito & Nakano, verificação exaustiva por FPGA (2009/2010): engenharia sólida, sem erros

Status: sem erros
Criada em: 2026-07-17
Origem: itens 116 (ISPA 2009) e 120 (IEEE 2010) do INDEX.md, mesmos
autores, 120 é evolução explícita e citada de 116.

## Enunciado

**Item 116**: arquitetura hardware-software para verificação exaustiva
de Collatz em números de 64 bits — tabelas A/B pré-computadas para
blocos de d bits menos significativos colapsam várias iterações numa
única operação n←A[nL]·nH+B[nL], sieving em 24 coprocessadores num
FPGA Virtex II; overflows (>78 bits) escalados para software de
precisão arbitrária no host. 2,89×10⁹ números/s.

**Item 120**: sequência direta (cita 116 como ref. [11]), troca 4
multiplicadores paralelos de 17×17 bits por um bloco DSP48E do
Virtex-5 em pipeline sequencial — clock mais alto (280,6MHz vs
49,5MHz), suporte a números intermediários maiores (112 bits vs 78),
reduzindo drasticamente probabilidade de overflow.

## Avaliação

Ambos são verificação computacional exaustiva de um intervalo finito
(64 bits) — não alegam prova.

**Verificação computacional feita nesta revisão**: as 4 fórmulas de
redução mod-4 (Seção II, ambos papers, texto quase idêntico e
legitimamente reusado) — corretas. Tabela I/II completa (valores A,B
para os 16 padrões de 4 bits, incluindo os 3 padrões "obrigatórios"
S={0111,1011,1111}) — reproduzida via simulação, bate 100% (nota: a
condição "mandatory" é que o valor de `a` nunca caia abaixo de 2^d
DURANTE o processo, não só no final). Tabela III do item 120 (contagem
esperada de operações, base=4 bits → média 6,0 sobre os 16 trajetos) —
confere. Tabela IV (razão de bits obrigatórios, ex. base=4→3/16=0,1875,
base=10→64/1024=0,0625) — confere. Conta final de overflow esperado
(R(112)=1,33×10⁻¹⁵ × 10¹²=1,33×10⁻³, consistente com 0 observados) —
correta.

## Sobreposição

116↔120 é reuso legítimo (evolução incremental citada explicitamente),
não duplicação problemática — padrão normal de "conference paper
incremental" em engenharia.

## Relevância para a investigação atual

Nenhuma — engenharia de hardware pura para acelerar busca exaustiva,
sem tocar medidas de densidade nem generalizações qx+1.

## Veredito

Nenhum erro encontrado em nenhum dos dois papers.
