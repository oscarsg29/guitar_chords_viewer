---
name: markdown-doc-dedup
description: Check Markdown documentation changes for duplicated or conflicting information, especially after creating or updating .md files.
metadata:
  short-description: Check Markdown docs for duplication
---

# Markdown Doc Dedup

Use this skill when creating or updating Markdown documentation. The goal is to keep each document focused, avoid repeated source-of-truth content, and prevent conflicting instructions across docs.

## Workflow

After Markdown files are added or edited:

1. List the repository Markdown files with `rg --files -g '*.md' -g '*.MD'`.
2. Identify each file's intended responsibility before editing further. Prefer an existing `AGENTS.md`, `PROJECT_STRUCTURE.md`, README, or equivalent documentation map when present.
3. Search for repeated headings, repeated command blocks, repeated architecture descriptions, repeated setup steps, and repeated file-responsibility lists.
4. Decide which file should be the source of truth for each topic. Keep detailed information there. In other files, replace repeated detail with a short summary and a pointer to the source file.
5. Check for conflicts after deduplication, especially launch commands, paths, dependency instructions, package names, and verification commands.
6. Report what duplication was removed, what source-of-truth file was chosen, and any intentional overlap left in place.

## Source-Of-Truth Guidance

Prefer this ownership model when the repository has these files:

- `README.md`: short project introduction and first run command only.
- `PROJECT_STRUCTURE.md`: folder layout and file responsibility details.
- `SETUP_CHECKLIST.md`: setup, verification, and run commands.
- `SCRIPT_FEATURES.md`: user-visible features and high-level implementation summary.
- `DESIGN_PRINCIPLES.md`: principles and architecture rules.
- `DESIGN_PRINCIPLES_CHECKLIST.md`: current compliance scores and maintenance checklist.
- `AGENTS.md`: the intention of documentation files, not duplicated content from those files.

## What Counts As Duplication

Treat these as duplication that should usually be reduced:

- The same folder tree copied into multiple docs.
- The same long verification command repeated in several docs when one checklist can own it.
- Full file-responsibility descriptions repeated outside the project-structure doc.
- Setup instructions repeated outside setup docs.
- Design rules repeated in feature or structure docs.

Intentional short overlap is acceptable when it improves navigation, such as a one-line run command in `README.md` or a one-line pointer to another doc.

## Completion Check

Before finishing, make sure:

- Every major topic has one clear source-of-truth document.
- Other documents link or point to that source instead of copying it.
- No Markdown file now contains stale commands, stale paths, or conflicting architecture descriptions.
- Any documentation map, such as `AGENTS.md`, includes newly created Markdown files.
