# H-136: auditoria de O6 e da proposta módulo 32 de Chang

Status: fechada-confirmada; O6 retirado como problema matemático do paper

Criada: 2026-08-07

## Fontes primárias

- E. Y. Chang, `arXiv:2603.25753v1`, submetido em 24 de março de 2026.
- E. Y. Chang, `arXiv:2603.11066`, versão disponível em 7 de agosto de
  2026.

## Resultado da auditoria

O primeiro preprint propõe controlar, em cada órbita, o desequilíbrio
entre os resíduos `9` e `25 mod 32` nos fins de rajada:

```text
|B9/(B9+B25)-1/2| <= delta < delta_max.
```

O valor de `delta_max` não é dado de forma autocontida. Ele é remetido a
um orçamento block-TV de um paper companheiro. A versão atual do paper
companheiro não contém esse orçamento como uma redução fixa módulo 32.
Ela formula uma conjectura de equidistribuição em módulos crescentes e
usa separadamente uniformidade de caudas para comprimentos de gaps. Seu
próprio resumo classifica o programa como condicional e exploratório.

Portanto a implicação

```text
balanço módulo 32 => Collatz
```

não está estabelecida pelas fontes atuais. O experimento E-102 continua
válido como medição do estatístico módulo 32, mas não testa a hipótese de
módulos crescentes nem o controle de caudas.

## Correção no paper 01

O texto deixou de apresentar essa proposta como quinta formulação ou
como redução. O antigo O6 agora registra a auditoria fechada para manter
a numeração histórica O1-O8, mas não é contado como problema aberto.

