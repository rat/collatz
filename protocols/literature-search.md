# Protocolo — Busca Literária Dirigida

Diferente da "coleção de papers" (busca ampla no Google Scholar, ver
`projects/collatz/BACKLOG.md` item 0 — leitura item a item, só quando
pedido), este protocolo é para buscas DIRIGIDAS: quando uma hipótese
já identificou um ingrediente faltante específico e queremos saber se
alguém já resolveu (ou quase resolveu) esse ingrediente exato.

1. Busque pela MAQUINARIA TÉCNICA específica, não pelo tema geral.
   "Fourier decay self-similar measures without separation condition"
   encontra coisa útil; "Collatz Fourier" não encontra (satura de
   resultados de baixa qualidade sobre o tema geral).
2. Para cada candidato promissor, busque o abstract/introdução real
   (WebFetch na página do arXiv ou HTML, não confiar só no resumo do
   buscador) antes de avaliar aplicabilidade — teoremas têm hipóteses
   precisas que resumos automáticos comem.
3. Se a pergunta de aplicabilidade exigir julgamento matemático não
   trivial ("essa técnica X se aplica ao nosso objeto Y?"), não
   adivinhe — consulte o advisor/Fable com o enunciado exato extraído
   do passo 2. Ver seção "Consultando o Fable" em `CLAUDE.md`.
4. Registre o resultado na hipótese relacionada mesmo quando for
   negativo ("não se aplica, pelo motivo X") — evita repetir a mesma
   busca/consulta numa sessão futura. Ver exemplos reais em
   `projects/collatz/hypotheses/H-127*.md` (addendum) e
   `H-110-endogeny-barrier-toy-model-2adic-lemma.md` (addendum).

## Armadilha conhecida — candidatos diferentes, mesma parede

Em `H-128-busca-literaria-dirigida-pos-h127.md`, três candidatos
tecnicamente distintos (Baker-Banaji, Li-Sahlsten, Kolesko-Mentemeier)
foram avaliados um a um pelo Fable e **todos falharam pela mesma razão
estrutural** (rigidez de Z_3^× — todo ramo da nossa recursão tem a
mesma razão de contração 3-ádica, então qualquer técnica que dependa
de múltiplas razões distintas ou de sintonia fina de um parâmetro
contínuo degenera). Antes de gastar uma consulta inteira em cada novo
candidato "parecido", vale checar rapidamente se ele depende do mesmo
tipo de estrutura que já se sabe ausente no nosso objeto — mas ainda
assim documente a checagem específica (o mecanismo de falha às vezes
difere mesmo quando a conclusão não difere, e isso importa para a
seção de trabalhos relacionados do paper).

## Armadilha conhecida — quando parar

Depois de 2-3 rodadas de busca convergindo no mesmo veredito ("não se
aplica, mesma parede"), isso é sinal de retorno decrescente, não
motivo para desistir da pesquisa em si — a convergência de múltiplas
vias independentes no mesmo obstáculo é evidência citável de que a
barreira é real (ver `STATE.md`, seção sobre H-126/H-127/H-128). Continuar
buscando no mesmo estilo tende a só reconfirmar o mesmo ponto; se o
diretor científico quiser continuar, mude de ângulo de busca em vez de
repetir o padrão (ex: trocar "decaimento de Fourier" por "endogenia em
árvores aritméticas" gerou o achado de Chang em H-128, um ângulo
genuinamente novo).
