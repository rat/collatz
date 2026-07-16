# H-097 — Revisão: del Vado Vírseda (2026), "Teaching Theory of Computation in the STEM K-12 Curricula Through Impossibility and Undecidability Problems" — sem alegação matemática própria sobre Collatz

Status: revisado — paper de educação/pedagogia, Collatz aparece como
exemplo didático; a única afirmação factual sobre Collatz é correta e
já bem estabelecida na literatura
Criada em: 2026-07-16
Origem: item 098 do catálogo, baixado manualmente pelo diretor
científico. Proceedings of the 31st ACM Conference on Innovation and
Technology in Computer Science Education (ITiCSE 2026), Madrid, 7
páginas, peer-reviewed (conferência ACM formal).

## O que o paper faz

Estudo de pedagogia/educação em ciência da computação: propõe e avalia
estatisticamente (teste t de Welch, grupos controle/experimental, n=40
cada) três atividades didáticas em Python para ensinar conceitos de
Teoria da Computação (computabilidade, indecidibilidade) a estudantes
do ensino médio dentro do currículo STEM: (i) o circuito infinito de
Feynman (números computáveis), (ii) a Conjectura de Collatz
("sequências de granizo", indecidibilidade/imprevisibilidade), e (iii)
o problema de ladrilhamento de poliominós inspirado na cosmologia de
Penrose (indecidibilidade geométrica).

Não é um paper de matemática sobre Collatz — não alega provar, refutar
ou avançar a conjectura em si. Collatz entra só como estudo de caso
motivacional/pedagógico.

## A única afirmação factual sobre Collatz (verificação de contexto, não computacional)

O paper cita (Seção 4.2, referências [29,36]) que "Conway demonstrou,
em 1972, que uma versão generalizada do processo de Collatz... é
algoritmicamente indecidível" — referenciando Kurtz & Simon (2007),
"The Undecidability of the Generalized Collatz Problem". Essa é uma
afirmação **correta e bem estabelecida** na literatura: o resultado de
indecidibilidade se aplica a generalizações do tipo f(n)=a_i·n+b_i
(mod m) com múltiplos ramos livres (formalismo tipo funções de Collatz
generalizadas / FRACTRAN de Conway), **não** à conjectura clássica 3n+1
em si, que continua em aberto. O paper não confunde as duas coisas —
distingue claramente "a conjectura clássica permanece não resolvida"
(citando Tao 2022 corretamente) de "a versão generalizada é
indecidível" (Conway/Kurtz-Simon). Mesma distinção correta já
encontrada em outras revisões desta coleção (ex. H-067/Carelli).

## Avaliação

Sem erros matemáticos sobre Collatz para verificar computacionalmente
— não há alegação numérica ou algébrica própria sobre a conjectura
neste paper, só um fato citado corretamente da literatura estabelecida
de teoria da computação. A parte estatística (testes t, p-valores para
avaliar eficácia pedagógica) está fora do escopo de verificação deste
projeto (não é uma alegação sobre a Conjectura de Collatz). Marcado
como "N/A" nas colunas Corrigido/Implementado, mesmo padrão usado para
outros itens desta coleção onde Collatz aparece só tangencialmente
(itens 023, 024, 102, 103).

## Referências

- Paper: `literature/papers/098_Teaching-Theory-of-Computation-STEM-K12.pdf`.
- Kurtz & Simon (2007), "The Undecidability of the Generalized Collatz
  Problem" — citado corretamente pelo paper, não catalogado
  separadamente neste projeto (fora do escopo: trata de uma
  generalização, não da conjectura clássica).
