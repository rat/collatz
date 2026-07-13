# Protocolo — Nova Hipótese

1. Crie um arquivo em `projects/<projeto>/hypotheses/H-XXX-titulo-curto.md` (numeração
   sequencial de 3 dígitos).
2. Use este formato mínimo:

```markdown
# H-XXX — Título

Status: aberta | em revisão | validada | refutada
Criada em: AAAA-MM-DD

## Enunciado

O que está sendo proposto.

## Motivação

Por que isso parece promissor (literatura, padrão observado, intuição).

## Como testar

O que provaria ou refutaria isso.

## Atualizações

- AAAA-MM-DD: ...
```

3. Adicione uma linha em `projects/<projeto>/STATE.md` referenciando a nova hipótese.
4. Nunca apague uma hipótese refutada — mude o status para `refutada` e registre por quê.
   Ideias descartadas também são conhecimento (evita retestar o que já falhou).
