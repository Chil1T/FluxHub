# Codex Workflow

## Instruction layers

- Global guidance comes from the user Codex home.
- Repo-specific guidance starts at [../../AGENTS.md](../../AGENTS.md).
- Future module-specific overrides should be added only when a subdirectory needs different rules.

## Documentation flow

- Start at [../README.md](../README.md) for repository documentation.
- Keep the root AGENTS file short and stable.
- Put durable process details, decisions, and product context in `docs/`.

## Repo-local skills

- [../../.agents/skills/winui-sticky-notes-entry/SKILL.md](../../.agents/skills/winui-sticky-notes-entry/SKILL.md)
- [../../.agents/skills/playground-repo-maintenance/SKILL.md](../../.agents/skills/playground-repo-maintenance/SKILL.md)

These skills are intentionally narrow. They should point contributors to the correct repo documents and defaults, not replace global system skills.

## Subagent boundary

- Use subagents for bounded, read-heavy work such as exploration, review, validation summaries, and document checks.
- Avoid parallel writes to the same file set.
- Keep noisy intermediate output out of the main thread whenever parallel analysis is explicitly requested.

## Validation contract

When changing docs, repo-local skills, CI, or repository structure:

1. Run `python -m unittest discover -s tests -p "test_*.py" -v`.
2. Review [../../.github/workflows/repo-hygiene.yml](../../.github/workflows/repo-hygiene.yml) together with the repository contract tests when the workflow changes.
3. Update this document or [../README.md](../README.md) if the contributor workflow changed.
