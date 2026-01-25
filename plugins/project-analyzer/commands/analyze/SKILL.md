---
name: analyze
description: Analyze a project's codebase and generate CLAUDE.md and skills with project knowledge
---

# Analyze Project

Analyze the current project and generate CLAUDE.md and relevant skills.

## Instructions

### Phase 1: Discovery

Run the **discovery** agent to detect what aspects exist in this project:
- api
- database
- tests
- frontend
- backend
- infrastructure
- documentation

### Phase 2: Analysis

Based on discovery results, run only the relevant analyzers in parallel:

| Detected | Agent |
|----------|-------|
| api | api-analyzer |
| database | database-analyzer |
| tests | tests-analyzer |
| frontend | frontend-analyzer |
| backend | architecture-analyzer |
| infrastructure | infrastructure-analyzer |

Always run:
- **architecture-analyzer** — overall structure
- **patterns-analyzer** — code patterns
- **build-analyzer** — build/dev workflow

### Phase 3: Generate CLAUDE.md

Create `CLAUDE.md` in the **project root directory** (not in .claude/) combining findings:

```markdown
# Project: [name]

## Overview
[1-2 sentences describing what this project does]

## Tech Stack
[Key technologies and frameworks]

## Architecture
[From architecture-analyzer]

## Directory Structure
[Key folders and their purposes]

## Development
[From build-analyzer - install, run, test, build commands]

## Key Patterns
[From patterns-analyzer - important conventions to follow]

## Key Files
[Critical files for understanding the project]
```

### Phase 4: Report

Summarize:
- What aspects were detected
- What skills were generated in `.claude/skills/`
- Any notable findings or recommendations
