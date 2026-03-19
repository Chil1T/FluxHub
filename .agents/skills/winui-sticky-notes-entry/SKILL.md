---
name: winui-sticky-notes-entry
description: Use when planning or bootstrapping the Windows-native sticky notes and capture app in this repository.
---

# WinUI Sticky Notes Entry

Use this skill when the task is about the future Windows-native app itself.

## Workflow

1. Read [README.md](../../../README.md), [AGENTS.md](../../../AGENTS.md), and [docs/product/vision.md](../../../docs/product/vision.md).
2. Confirm whether the repository still contains collaboration scaffolding only or already includes app code.
3. If app code does not exist yet, stay in spec and plan mode. Write product requirements under [docs/specs/README.md](../../../docs/specs/README.md) and implementation plans under [docs/plans/README.md](../../../docs/plans/README.md) before proposing scaffolding.
4. Default implementation direction is WinUI 3 + Windows App SDK + C# unless the user explicitly changes it.
5. Treat capture capabilities as phased work. Do not assume clipboard, OCR, drag-drop, and share integrations all ship in the first code pass unless an approved plan says so.

## Boundaries

- Do not invent build, packaging, or storage contracts before a product spec exists.
- Do not bypass repo rules or documentation flow because the project is new.
- Prefer global OpenAI/Codex documentation skills for volatile platform guidance.

## Output expectations

- State current repo phase: scaffolding only or app code present.
- Point to the next required document or implementation artifact.
- Keep recommendations aligned with the approved spec and plan chain.
