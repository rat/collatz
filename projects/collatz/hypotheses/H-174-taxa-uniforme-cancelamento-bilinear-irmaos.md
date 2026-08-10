# H-174: taxa e uniformidade do cancelamento bilinear entre irmãos (O4)

Status: fechada-refutada (2026-08-10), por premissa invalidada. Ver
"Fechamento" no fim. A pergunta correta que sobra está reformulada na
última seção, para retomada futura sob um número novo se for
perseguida.

Criada: 2026-08-10

Origem: pista aberta por E-140/H-163 (Regra 8e). Número escolhido para
não colidir com os outros agentes rodando em paralelo nesta sessão
(estado do repositório nesta rodada ia até H-169); renumerar na
integração se necessário. **Atualização (2026-08-10, antes do commit)**:
colisão real detectada com H-170/H-171 já usados na main (pelo agente
do paper 05); esta hipótese e as três seguintes (originalmente
H-170 a H-173) foram renumeradas para H-174 a H-177 antes do commit,
não deixadas para a integração.

## O que já se sabe (na criação; corrigido abaixo)

H-163/E-140 mediram, para pares de irmãos explícitos (enumeração real,
pesos reais de ramo, `v` fixo), que a soma bilinear `sum_xi S_1(xi)
conj(S_2(xi))` cai muito abaixo tanto do orçamento trivial de
Cauchy-Schwarz quanto da estimativa de fase aleatória, monotonicamente
até `ell=14`, em 6 raízes e 3 gaps de irmão (`k=1,2,3`) testados. Isto
é um resultado empírico de nível finito, sem taxa provada.

## Pergunta (como originalmente formulada; ver "Fechamento")

1. A taxa de queda de `ratio_RP` (razão medido/fase-aleatória) segue
   alguma lei limpa em `ell` (exponencial em `ell`? em `sqrt(ell)`?
   outra)? Os dados de E-140 já existem para um ajuste, não foi feito
   aqui (fora do escopo do teste barato original).
2. O cancelamento medido é uniforme sobre TODOS os pares de irmãos
   (todos os `k`, todas as raízes `v`), ou existe alguma família de
   pares (ex.: `v` numa órbita especial, `k` grande) onde ele
   enfraquece ou desaparece? O teste atual amostrou só raízes pequenas
   e `k` até 3.
3. Existe uma prova (não só medição) para a taxa observada, usando a
   estrutura algébrica identificada em H-163 (as duas somas são a
   MESMA função em frequências relacionadas por potências de 2, já que
   condicionar no primeiro passo age por dilatação `xi -> 2^j xi` mais
   fase linear)?

## Por que valia investigar (na criação)

Se a taxa fosse boa o bastante e genuinamente uniforme, isto fecharia
O4 de verdade (não só a checagem qualitativa que H-163 já tinha feito),
o alvo que H-115 registrou como a única rota bilinear ainda de pé
depois de excluir cotas pontuais e L² separadamente.

## Primeiro passo barato (executado, na criação)

Ajustado `log(ratio_RP) ~ a*ell+b` contra `log(ratio_RP) ~
a*sqrt(ell)+b` nos dados de `full_run_ell2_14.txt`, 6 raízes: ajuste
linear em `ell` (fator `~0,73` a `~0,80` por nível) com resíduo igual
ou menor que `sqrt(ell)` em 4 das 6 raízes. Resultado descritivo,
mantido abaixo por completude do registro, mas ver "Fechamento": o que
estava sendo ajustado não é o que se pensava.

```text
v    slope linear (fator/nível)   resíduo linear   slope sqrt(ell)   resíduo sqrt(ell)
1     -0.2305 (0.7941)                  0.223            -1.318            0.255
5     -0.2961 (0.7437)                  0.302            -1.684            0.352
7     -0.2925 (0.7464)                  0.206            -1.679            0.244
11    -0.2206 (0.8020)                  0.222            -1.287            0.207
17    -0.2974 (0.7428)                  1.167            -1.836            1.116
25    -0.3138 (0.7307)                  0.576            -1.858            0.538
```

## Fechamento (2026-08-10): premissa invalidada por crítica independente

Um crítico independente (Regra 8/15) e, depois, verificação minha
própria (Regra 8c, controles refeitos independentemente) encontraram
que a medição base de E-140/H-163 (`sum_xi S_1(xi) conj(S_2(xi))`) não
mede cancelamento de fase: por Parseval, ela é essencialmente
`-m_1*m_2` (produto das massas das duas subárvores) na maior parte dos
casos testados, não porque os suportes sejam esparsos (são PLENOS,
todo resíduo coprimo com 3), mas porque o peso de ramo não
renormalizado concentra a massa numa razão de participação pequena
(dezenas de átomos efetivos, não milhões) dentro desse suporte pleno,
e os átomos pesados dos dois irmãos raramente coincidem. Dois
controles com dados sem relação nenhuma de irmandade (dilatação
aleatória; raiz não relacionada) reproduzem os mesmos números. Ver
H-163 para a análise completa.

Isso significa que o ajuste acima (item "Resultado do primeiro passo")
NÃO é um ajuste da taxa de um cancelamento de fase: é, muito
provavelmente, um ajuste da taxa de encolhimento das massas `m_1`,
`m_2` das subárvores (que decaem porque o peso de ramo não é
renormalizado), disfarçada de "taxa de cancelamento" pela mesma
identidade de Parseval. Um crítico independente ESTIMOU (não uma
verificação ponto a ponto contra os dados reais, ver Regra 11) que o
expoente medido (`~0,28` por nível) é compatível em ordem de grandeza
com aritmética sobre `log(N_1)+log(N_2)` (razões de participação das
duas subárvores) sem nenhum termo de fase: `d(log sqrt(N_1 N_2))/d(ell)
= +0,304` (das razões de participação) menos `log(3)/2 = 0,549` dá
`-0,245`, contra `-0,23` a `-0,31` medido. Consistente, mas uma
estimativa de ordem de grandeza, não uma verificação ponto a ponto. A
pergunta que este ajuste se propunha a responder (existe uma taxa
provável de cancelamento bilinear?) nunca foi de fato testada.

**Decisão**: `fechada-refutada`, no sentido de que a premissa sobre a
qual esta hipótese foi construída (H-163 mediu cancelamento real) está
refutada. Isto não é o mesmo que "a taxa de cancelamento bilinear real
não existe"; é "esta hipótese, como formulada, não tem mais objeto".

## A pergunta que sobra, corretamente colocada (para retomada futura)

Se a linha de O4 for retomada, a pergunta certa não é sobre uma
subárvore real truncada (suporte pleno mas massa concentrada numa
razão de participação pequena, onde Parseval trivializa o resultado),
mas sobre a decomposição IDEALIZADA de Tao,
`mu_ell = sum_j 2^{-j} mu_ell^{(j)}` (medida de suporte pleno em
unidades mod `3^ell`), com os modos afins grosseiros de H-126 Prop. 2
explicitamente removidos ANTES de somar. O protocolo correto, aprendido
nesta sessão, inclui desde o início:

1. Construir `S_i` a partir de `mu_ell^{(j_i)}`, não de uma subárvore
   real truncada.
2. Remover os modos de condutor grosseiro antes de medir.
3. Comparar contra os dois controles (dilatação aleatória; objeto não
   relacionado) como parte do teste, não como reação a uma crítica
   depois do fato.

Nenhuma tentativa nesta direção foi feita (fora do escopo desta sessão
depois da retratação). Se retomada, merece um número de hipótese novo
(não reaproveitar H-174), já que o objeto testado é genuinamente
diferente do que esta hipótese testou.
