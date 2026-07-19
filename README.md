# ResearchOS

AI-assisted scientific research lab. Minimal structure, designed to grow by
real need rather than upfront specification.

Active project: [Collatz](projects/collatz/README.md).

## Structure

```
ResearchOS/
├── CLAUDE.md                 # instructions for Claude Code
├── ROADMAP.md                # lab-wide priorities
├── protocols/                # lightweight processes (hypothesis, experiment, literature search, checkpoint)
├── scripts/                  # utilities (e.g. checkpoint.sh)
└── projects/
    └── collatz/               # first research line
        ├── STATE.md           # memory: current state, hypotheses, next steps
        ├── hypotheses/
        ├── experiments/
        ├── literature/        # notes on THIRD-PARTY papers
        ├── papers/            # OUR OWN papers (final result to write/publish)
        └── logs/
```

A new research line is added by creating `projects/<name>/` with the same
internal structure (`STATE.md`, `hypotheses/`, `experiments/`, `literature/`, `logs/`).
Nothing exists beyond Collatz until a new line is explicitly started.

## Roles

- **Scientific director** (you): sets goals, priorities, and approves results.
- **Claude Code**: executes — creates/edits files, runs experiments, maintains Git.
- **Checkpoints**: every session ends with a commit + push (see `protocols/checkpoint.md`).
