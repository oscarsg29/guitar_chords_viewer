# Markdown File Intentions

This file explains the intention of each Markdown document in the repository.

## Markdown Maintenance Rule

When adding or updating Markdown files, use the `markdown-doc-dedup` skill to check for duplicated or conflicting documentation before finishing.

The portable repository copy is stored at `skills/markdown-doc-dedup/` for reuse by other agents or machines.

## README.md

Intention: provide the shortest project-level introduction.

Use this file to describe what the repository is, what the main script does at a high level, and where a new reader should start.

## SETUP_CHECKLIST.md

Intention: provide a practical checklist for making the app run locally.

Use this file to track the system requirements, missing dependencies, launch command, and repository setup gaps needed to run `guitarChordsViewer.py`.

## SCRIPT_FEATURES.md

Intention: document what the current Python script contains and what it is trying to accomplish.

Use this file to describe the app's musical purpose, supported chord features, UI controls, implementation structure, and possible future improvements.

## DESIGN_PRINCIPLES.md

Intention: explain practical software design principles and a recommended architecture for future updates.

Use this file when deciding how to organize code changes, where new behavior belongs, and how to keep the app easy to maintain.

## DESIGN_PRINCIPLES_CHECKLIST.md

Intention: rate how closely the app follows the documented design principles.

Use this file before and after refactors to identify what improved, what remains partial, and which verification commands to run.

## PROJECT_STRUCTURE.md

Intention: document the repository layout and the responsibility of each folder and source file.

Use this file when deciding where code should live or when onboarding yourself to the package structure.

## AGENTS.md

Intention: give future coding agents and contributors quick context about the documentation layout.

Use this file as a guide for deciding where new documentation belongs and how each Markdown file should be maintained.
