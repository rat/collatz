# ResearchOS

Laboratório de pesquisa científica assistida por IA. Estrutura mínima, pensada para
crescer por necessidade real em vez de especificação antecipada.

Projeto ativo: [Collatz](projects/collatz/README.md).

## Estrutura

```
ResearchOS/
├── CLAUDE.md                 # instruções para o Claude Code
├── ROADMAP.md                # prioridades gerais do laboratório
├── protocols/                # processos leves (hipótese, experimento, checkpoint)
├── scripts/                  # utilitários (ex: checkpoint.sh)
└── projects/
    └── collatz/               # primeira linha de pesquisa
        ├── STATE.md           # memória: estado atual, hipóteses, próximos passos
        ├── hypotheses/
        ├── experiments/
        ├── literature/
        └── logs/
```

Uma nova linha de pesquisa é adicionada criando `projects/<nome>/` com a mesma
estrutura interna (`STATE.md`, `hypotheses/`, `experiments/`, `literature/`, `logs/`).
Não existe nada além de Collatz até que uma nova linha seja explicitamente iniciada.

## Papéis

- **Diretor científico** (você): define objetivos, prioridades e aprova resultados.
- **Claude Code**: executa — cria/edita arquivos, roda experimentos, mantém o Git.
- **Checkpoints**: toda sessão termina com commit + push (ver `protocols/checkpoint.md`).
