# Product Vision

## Goal

Build a Windows-native lightweight capture and sticky notes app for fast collection of information from across the desktop.

## Default product direction

- Platform: Windows desktop
- Recommended stack for future implementation: WinUI 3 + Windows App SDK + C#
- Interaction model: tray-resident app with fast capture entry points
- Data strategy: local-first with a future sync boundary

## MVP boundary

The future MVP should prioritize:

- global hotkey capture
- clipboard capture
- timeline and tag views
- local storage
- clear path to later OCR, drag-drop, and share integrations

This repository does not implement those features yet. It only prepares the collaboration and planning structure.

## Non-goals for the current repository pass

- no WinUI solution or project files
- no business logic
- no storage schema
- no packaging or release pipeline

## Required next steps

1. Capture product requirements in [../specs/README.md](../specs/README.md).
2. Convert the approved spec into an implementation plan in [../plans/README.md](../plans/README.md).
3. Only then scaffold the application and add build or runtime validation.
