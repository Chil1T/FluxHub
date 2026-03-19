# Repo Modernization Baseline

## Purpose

Record the defaults chosen during repository initialization so future threads do not need to rediscover them.

## Approved defaults

- Repository role: Codex-first collaboration scaffold
- Product target: Windows-native sticky notes and capture app
- Recommended future implementation stack: WinUI 3 + Windows App SDK + C#
- Scope of this pass: repo rules, docs, repo-local skills, CI, and validation scaffold only
- CI policy: validate only real repository capabilities
- Skill policy: keep repo-local skills few and narrow

## What this pass intentionally avoids

- application scaffolding
- build jobs for a non-existent app
- fake tests
- speculative architecture that would force future implementation choices too early

## Follow-up trigger

Start the next repo phase when a product spec is ready in [../specs/README.md](../specs/README.md) and an implementation plan is ready in [../plans/README.md](../plans/README.md).
