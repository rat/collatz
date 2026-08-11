# Our own papers (final result)

Unlike `../literature/` (notes on THIRD-PARTY papers we read and
evaluate), this folder holds the papers that ResearchOS ITSELF
produces — the final result to be written/published from the
accumulated hypotheses and experiments.

Each paper has its own `NN-short-title/` subfolder, containing at
least an `OUTLINE.md` (scope, structure, source hypotheses, status)
and, as writing progresses, the draft files themselves.

## Active/planned papers

- **`01-syracuse-qx1-endogenia/`** — this line's main paper, being split
  (started 2026-08-10) into a leaner umbrella plus three companion
  papers below, each self-contained and independently citable (Rule 10:
  not to inflate citation count, but because 04/05/06 target different
  literatures than 01's own). 01 keeps the endogeny-barrier framing, the
  triangulation of β=1/WCC/Wirsching Conjecture 3 (§9.1), H-166's new
  unconditional bound, the two failed-lemma attempts (§10), and the
  8 tracked open directions (O1-O8); §3, §6, and §9.2-9.3 move out.
  Scope: H-109 through H-169 (companion papers keep their own scope
  listed below). Repo: `collatz-endogeny` (existing, unchanged).
- **`04-kontorovich-lagarias-volkov/`** — self-contained empirical
  paper: exact enumeration of the $5x+1$ reverse tree, a calibrated
  comparison (matched synthetic controls, not a raw estimator reading)
  separating the Kontorovich-Lagarias exponent from Volkov's competing
  prediction. Scope: H-113, H-169, E-097, E-139. Repo:
  `collatz-kl-volkov`. Split off 01 on 2026-08-10.
- **`05-wirsching-2003-conjecturas/`** — proof of Wirsching's (2003)
  Conjecture 1, a corrected reading of Conjecture 2 against the primary
  source, and a certified numerical test of Conjecture 3. Scope: H-125,
  H-133, H-134, H-142 through H-147, H-153, H-160, H-167, H-168, H-171,
  E-135. Repo: `collatz-wirsching-2003`. Split off 01 on 2026-08-10.
  Backlog exhausted 2026-08-10: H-168 and H-171 both closed, no open
  items remain in scope.
- **`06-pressao-qx1-ramificacao/`** — closed-form pressure identity,
  q-adic density martingale, and $L^p$ collision criterion for the
  accelerated $qx+1$ branching process; general branching-random-walk
  theory, reusable outside the endogeny-barrier narrative. Scope:
  H-109, H-132, H-138, H-139, H-141, H-129 (attribution resolved
  2026-08-10; formalized as `conj:real-tree-tail`, distinct from
  `conj:tail-index`).
  Repo: `collatz-qx1-pressure`. Split off 01
  on 2026-08-10.
## Paused papers

Not active. Left exactly as they are; no further work without a new
explicit request from the scientific director.

- **`02-critica-cumulativa-literatura/`** — cumulative,
  running/incomplete survey of the Collatz-adjacent literature that
  does NOT claim a complete proof (16 items consolidated as of
  2026-07-20, out of a much larger surveyed collection). Draft complete
  (`main.tex`/`main-pt-br.tex`, both compiled) but never reviewed by
  the scientific director. See `BACKLOG.md` item 8 and `OUTLINE.md`.
  **Paused indefinitely 2026-08-10** at the scientific director's
  explicit request.
- **`03-alegacoes-de-prova-refutadas/`** — narrower, closable sibling of
  02: catalogs *only* claims of a complete proof (or disproof) of the
  Collatz conjecture (12 cases as of 2026-07-20, all already reviewed
  in depth, none valid), with a taxonomy of the recurring error
  patterns. Draft complete (`main.tex`/`main-pt-br.tex`, both compiled)
  but never reviewed by the scientific director. See `OUTLINE.md`.
  **Paused indefinitely 2026-08-10** at the scientific director's
  explicit request.

## Convention

A paper only gets a folder here once the hypotheses supporting it have
converged enough to be worth sketching a structure (it shouldn't be
born alongside a line's first hypothesis). Do not create a folder for
hypothetical/future papers without a real investigation line behind them.
