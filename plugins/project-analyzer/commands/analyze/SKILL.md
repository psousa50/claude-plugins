---
name: analyze
description: Analyze a project's codebase and generate CLAUDE.md and skills with project knowledge
---

# Analyze Project

Analyze the current project and generate CLAUDE.md and skills with project knowledge.

## Instructions

Run the following agents in parallel to analyze different aspects of the codebase:

1. **architecture-analyzer** — Analyze project structure, components, and data flow
2. **patterns-analyzer** — Analyze coding patterns, conventions, and idioms
3. **build-analyzer** — Analyze build process, scripts, and development workflow

After all agents complete, create `CLAUDE.md` combining their findings:

```markdown
# Project: [name from package.json or directory]

## Overview
[1-2 sentences from architecture analysis]

## Architecture
[From architecture-analyzer]

## Directory Structure
[From architecture-analyzer]

## Patterns & Conventions
[From patterns-analyzer]

## Development
[From build-analyzer]

## Key Files
[Combined from all analyzers]
```

Each agent also generates a skill in `.claude/skills/` for ongoing reference.

Report what was created when done.
