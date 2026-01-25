# Architecture Analyzer

Analyze project architecture and generate an architecture skill.

## Instructions

Explore the codebase to understand:
- Directory structure and organisation
- Key components/modules and their responsibilities
- Entry points (main files, index files, app entry)
- Data flow between components
- External dependencies and integrations

Look for:
- src/, lib/, app/, packages/ directories
- Configuration files (tsconfig, webpack, vite, etc.)
- Module boundaries and imports
- API routes or endpoints
- Database models or schemas

Generate `.claude/skills/architecture/SKILL.md`:

```markdown
---
name: architecture
description: Explains this project's architecture, components, and data flow
---

# Architecture

## Overview
[What this project does and its main purpose]

## Components
[List key components with their responsibilities]

## Directory Structure
[Important folders and what they contain]

## Data Flow
[How data moves through the system]

## Key Files
[Critical files and their purposes]
```

Return a summary of the architecture findings.
