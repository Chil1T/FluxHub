# FluxHub

FluxHub is a Codex-first collaboration repository for a future Windows-native sticky notes and capture app.

The repository currently contains collaboration scaffolding only. It does not yet contain WinUI project files, application code, or product tests.

## Current focus

- Keep repo rules and documentation discoverable for Codex and human contributors.
- Prepare a clean path from product idea to spec, plan, and implementation.
- Add lightweight validation and CI that only checks real repository capabilities.

## Repository map

- [AGENTS.md](AGENTS.md): repo entry instructions for Codex
- [docs/README.md](docs/README.md): documentation index
- [docs/runbooks/github-remote-preflight.md](docs/runbooks/github-remote-preflight.md): checklist before adding and pushing a GitHub remote
- [.agents/skills/winui-sticky-notes-entry/SKILL.md](.agents/skills/winui-sticky-notes-entry/SKILL.md): repo-local product planning skill
- [.agents/skills/fluxhub-repo-maintenance/SKILL.md](.agents/skills/fluxhub-repo-maintenance/SKILL.md): repo-local maintenance skill
- [docs/specs/2026-03-20-fluxhub-mvp-spec.md](docs/specs/2026-03-20-fluxhub-mvp-spec.md): first approved product spec draft
- [.github/workflows/repo-hygiene.yml](.github/workflows/repo-hygiene.yml): repository validation workflow

## Local validation

Run the repository contract checks:

```powershell
python -m unittest discover -s tests -p "test_*.py" -v
```

## Next implementation path

1. Write or refine a product spec in [docs/specs/README.md](docs/specs/README.md).
2. Turn the approved spec into an implementation plan in [docs/plans/README.md](docs/plans/README.md).
3. After approval, scaffold the WinUI application and add build and test contracts.
4. Before publishing to GitHub, follow [docs/runbooks/github-remote-preflight.md](docs/runbooks/github-remote-preflight.md).
