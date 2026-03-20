# FluxHub MVP Spec

## Summary

FluxHub is a Windows-native lightweight capture and sticky notes application focused on turning information from across the desktop into quickly retrievable note cards. The first implementation should optimize for fast capture, low interaction cost, and a clean path from captured content to later organization.

This repository still contains collaboration scaffolding only. This spec defines the first application scope but does not authorize packaging, cloud sync, or production deployment work yet.

## Problem

Existing note tools are either too heavy for quick desktop capture or too narrow in how they collect information. The target user wants a tray-resident Windows app that can collect information from multiple system-level entry points and turn that material into lightweight notes without forcing a full document workflow.

## Target user and success criteria

Primary user:

- a Windows desktop user who wants to collect snippets, text, and quick references from across applications

Success for the MVP means:

- capture can be triggered in under a few seconds from the tray or a hotkey
- captured items land reliably in a local inbox/timeline
- users can find stored items again through timeline order, tags, and search
- the first architecture leaves room for later OCR, drag-drop, and sync expansion without rewriting the whole app

## Product principles

- local-first before sync-first
- tray-resident before document-centric
- capture speed before deep formatting
- simple card organization before full notebook hierarchy
- phased integrations instead of trying to support every capture path in v1

## MVP scope

In scope for the first implementation plan:

- Windows-native desktop app using WinUI 3 + Windows App SDK + C#
- tray-resident shell with quick open and quit actions
- global hotkey entry for fast capture
- clipboard text capture into a new note card
- note timeline view sorted by most recent activity
- tag-based organization view
- local full-text or keyword search across stored note content
- local persistence for notes and metadata
- note editing for title, body, and tags
- explicit source metadata fields for captured notes

Allowed but not required in the first implementation plan:

- a lightweight capture panel or quick-add window
- a local attachment path for future screenshots
- storage abstraction that leaves room for sync later

Out of scope for the MVP:

- cloud sync
- account system
- collaborative editing
- browser extension
- deep per-app plugins
- production packaging and installer pipeline
- OCR, drag-drop capture, and Windows share integration as shipping MVP requirements

## Phase strategy

The implementation plan should treat capture capabilities as phases:

Phase 1:

- tray shell
- global hotkey
- quick-add flow
- clipboard capture
- local storage
- timeline, tags, search

Phase 2 candidates after MVP:

- screenshot capture and OCR
- drag-drop capture
- Windows share entry
- richer source previews
- local-to-cloud sync boundary activation

## UX expectations

The app should feel lightweight and immediate:

- launching the quick capture flow should not require opening a heavy main window
- the timeline should behave like an inbox for newly captured material
- tag view should support later organization without blocking initial capture
- editing should stay simple and card-oriented, not document-editor oriented

## Technical defaults

- stack default: WinUI 3 + Windows App SDK + C#
- storage default: local-first with a future sync abstraction
- repository workflow default: spec first, then implementation plan, then application scaffold

## Open constraints for the next plan

The implementation plan still needs to make these concrete:

- exact local storage choice
- hotkey default and conflict handling
- capture panel behavior
- note card data model
- search indexing strategy
- tests for UI-adjacent behavior and storage contracts

## Acceptance criteria for the first implementation plan

The next implementation plan is good enough when it:

- decomposes MVP work into app shell, capture, storage, and views
- keeps OCR, drag-drop, share, and sync outside the first delivery path
- defines validation for storage, search, and core note flows
- does not assume packaging or remote services exist
