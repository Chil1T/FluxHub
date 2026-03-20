---
name: fluxhub-repo-maintenance
description: Use when changing repository rules, docs, repo-local skills, CI, or validation scaffolding in FluxHub.
---

# FluxHub Repo Maintenance

Use this skill for repository maintenance work that is specific to this repo.

## Workflow

1. Read [README.md](../../../README.md), [AGENTS.md](../../../AGENTS.md), and [docs/README.md](../../../docs/README.md).
2. Keep the root AGENTS file short. Put details in docs unless a deeper directory needs its own override.
3. When repo structure, docs, skills, or CI change, update [tests/test_repo_contract.py](../../../tests/test_repo_contract.py) if the repository contract changed.
4. Keep CI honest: validate only what the repository really contains.
5. Sync documentation index links after adding or renaming any durable doc or skill.

## Boundaries

- Do not add product code from this skill.
- Do not create repo-local skills that duplicate global skills unless the behavior is repo-specific.
- Do not add build jobs for a WinUI app before the app scaffold exists.

## Validation

- Run `python -m unittest discover -s tests -p "test_*.py" -v`.
- Review workflow changes together with the repository contract tests.
