# H-072 — Revisão: De Mol, "Tag systems and Collatz-like functions" (2008)

Status: revisão externa concluída (correto, sem erros encontrados; não tenta resolver a conjectura)
Criada em: 2026-07-15
Origem: item 102 da coleção de literatura (`literature/papers/INDEX.md`),
arquivado via busca EBSCO/ScienceDirect em 2026-07-15.

## O paper

Liesbeth De Mol (Ghent University, Centre for Logic and Philosophy of
Science). *Theoretical Computer Science* 390, 92-101 (2008), Elsevier —
periódico revisado por pares estabelecido em ciência da computação
teórica. **Não é sobre resolver a Conjectura de Collatz** — usa o
"problema 3n+1" como ferramenta para um resultado de teoria da
computabilidade sobre **sistemas de tag** (produzidos por Post,
recursivamente indecidíveis em geral por Minsky).

## O que o paper prova

**Teorema 2.1** (resultado principal): a função acelerada de Collatz
C'(2m)=m, C'(2m+1)=3m+2 é redutível a um sistema de tag T_C com μ=3
símbolos {α,c,y} e shift v=2, regras α→cy, c→α, y→ααα. Cada iteração de
C'(n) corresponde à produção de uma string α^(C'(n)) a partir de α^n.

**Teorema 2.2/2.3**: generaliza a construção para qualquer "função tipo
Collatz" G(n) com módulo d arbitrário (não só o caso d=2 do 3n+1
clássico), dando uma redução explícita a um sistema de tag T_G.

**Conclusão central**: como funções tipo-Collatz são recursivamente
indecidíveis em geral (Conway, 1972), isso dá uma prova alternativa de
que sistemas de tag da classe TS(3,2) são indecidíveis — situando a
"linha 3n+1" próxima da "linha de universalidade" conhecida para
sistemas de tag, um resultado sobre a estrutura de sistemas de tag, não
sobre a Conjectura de Collatz em si.

## Verificação computacional

`experiments/E-072-de-mol-tag-systems-review/experiment.py`:

1. **Teorema 2.1**: implementamos o sistema de tag bruto T_C literal
   (não a taquigrafia "↦" do paper) e confirmamos que, partindo de α^n,
   o próximo estado puramente-α tem comprimento exatamente C'(n), para
   n=1 a 200. **200 casos, 0 falhas** (excluído n=1, caso degenerado
   explícito do próprio formalismo: α^1 tem comprimento 1<v=2, então o
   sistema para imediatamente sem produzir nada — não é uma falha do
   teorema, é a condição de parada definida na Seção 1.1 do paper).
2. **Composição sob iteração repetida**: encadeamos o sistema de tag
   (saída de uma rodada vira entrada da próxima) para 4 sementes (7, 27,
   97, 871), confirmando que a trajetória bate exatamente com a
   trajetória de C'(n) calculada diretamente, até convergir a {1,2,4}.
   **0 falhas** (871 precisou de 111 iterações e ~64.000 passos brutos
   na iteração mais longa — só convergiu após corrigirmos um limite de
   passos insuficiente na nossa própria implementação, não um problema
   do sistema de tag em si).
3. **Exemplo introdutório do próprio paper** (v=3, sistema diferente de
   T_C, usado só para ilustrar o conceito de sistema de tag): reproduz
   exatamente o período de 6 passos afirmado no texto (A₀ é reproduzido
   após 6 iterações).

Nenhum erro encontrado. Construção matematicamente correta e verificada
em múltiplas frentes independentes.

## Nota de metodologia própria (auto-correção durante a implementação)

Minha primeira implementação usava concatenação de string Python
(`s[v:] + producao`) para cada passo bruto, O(n) por passo — para n
grandes (871 exigiu ~64.000 passos brutos numa única iteração de C'),
isso deu O(n²) total e estourou o timeout de 2 minutos. Reimplementado
com `collections.deque` (O(1) por passo), resolvendo o problema de
performance sem mudar a lógica — confirmado que os resultados batem
antes e depois da otimização (mesmos valores nos casos pequenos já
testados).

## Avaliação geral

Paper tecnicamente sólido, sem nenhuma alegação sobre a Conjectura de
Collatz em si (nunca afirma provar ou refutar nada sobre convergência a
1) — usa Collatz como um "problema difícil conhecido" para estabelecer
um resultado sobre a estrutura de sistemas de tag. Categoricamente
diferente da maioria dos papers desta coleção: não é sobre a conjectura,
é sobre teoria da computabilidade usando a conjectura como caso de
estudo. Nenhuma conexão nova com as linhas de pesquisa deste projeto
identificada (não usa árvore reversa, densidade, nem resíduos 3-ádicos
— o ângulo é puramente de simulação por autômatos).

## Atualizações

- 2026-07-15: revisão externa concluída. PDF lido por completo (10
  páginas). Teorema 2.1 confirmado sem exceção em 200 casos diretos e 4
  trajetórias iteradas completas; exemplo introdutório do paper também
  reproduzido exatamente. Nenhum erro encontrado.
