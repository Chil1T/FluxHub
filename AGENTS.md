# FluxHub

## Purpose
- This file is the repo entry point for Codex in FluxHub.
- Keep it short and stable. Put durable detail in `docs/` and only add nested `AGENTS.md` files when a deeper directory needs different rules.

## Repository direction
- This repository currently contains collaboration scaffolding for a future Windows-native sticky notes and capture app.
- Default future app direction is `WinUI 3 + Windows App SDK + C#`, but no app code exists yet.
- Read `README.md` and `docs/README.md` before making non-trivial changes.

## Working model
- Prefer spec and plan work before implementation when touching product direction, architecture, CI, or workflow rules.
- Keep one thread focused on decisions and final outputs.
- Use subagents for bounded read-heavy work such as exploration, review, and validation summaries.
- Avoid parallel writes to the same file set.

## Repo-local assets
- Repo-local skills live under `.agents/skills/`.
- Keep repo-local skills narrow and specific to FluxHub. Do not duplicate generic system skills.
- Product specs belong in `docs/specs/`. Implementation plans belong in `docs/plans/`.

## Validation
- Run `python -m unittest discover -s tests -p "test_*.py" -v` after changing docs, repo-local skills, tests, or workflows.
- Keep links and required repository files passing the contract tests.
- Do not add build or runtime validation for application code until the application scaffold exists.

## Maintenance
- Update `docs/README.md` when adding a durable document.
- Record initialization defaults and workflow changes in `docs/runbooks/` instead of expanding this file.
