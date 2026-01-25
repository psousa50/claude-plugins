---
name: analyze
description: Analyze a project's codebase and generate CLAUDE.md and skills with project knowledge. Use when exploring a new codebase or setting up project documentation.
---

# Project Analyzer

Analyze the current project and generate comprehensive documentation.

## Instructions

You are analyzing a codebase to generate project knowledge. Follow these steps:

### Step 1: Explore the Codebase

Use the Explore agent to understand:
- Directory structure and key folders
- Main technologies/frameworks used
- Entry points and core modules
- Test setup and configuration

Look for these files to understand the project:
- package.json, pyproject.toml, Cargo.toml, go.mod (dependencies & scripts)
- tsconfig.json, .eslintrc, .prettierrc (tooling config)
- Dockerfile, docker-compose.yml (deployment)
- README.md (existing documentation)
- src/, lib/, app/ directories (source code)
- test/, tests/, __tests__/ (test structure)

### Step 2: Identify Patterns

Analyze the code for:
- Naming conventions (files, functions, variables)
- Directory organization patterns
- Design patterns used (MVC, repository, factory, etc.)
- Error handling approach
- State management (if frontend)
- API structure (if backend)

### Step 3: Generate CLAUDE.md

Create `.claude/CLAUDE.md` with these sections:

```markdown
# Project: [name]

## Overview
[1-2 sentences describing what this project does]

## Architecture
[Key components and how they interact]

## Directory Structure
[Important folders and what they contain]

## Patterns & Conventions
- Naming: [conventions]
- Code style: [patterns observed]
- Error handling: [approach]

## Development
- Install: [command]
- Run: [command]
- Test: [command]
- Build: [command]

## Key Files
- [file]: [purpose]
```

### Step 4: Generate Skills

Create these skills in `.claude/skills/`:

#### `.claude/skills/architecture/SKILL.md`
```markdown
---
name: architecture
description: Explain this project's architecture
---
[Include specific details about this project's architecture, components, data flow]
```

#### `.claude/skills/patterns/SKILL.md`
```markdown
---
name: patterns
description: Explain the coding patterns and conventions in this project
---
[Include specific patterns, naming conventions, idioms used in this project]
```

#### `.claude/skills/build/SKILL.md`
```markdown
---
name: build
description: Explain how to build, test, and develop this project
---
[Include specific commands, environment setup, common workflows]
```

### Step 5: Report

After generating files, summarize what was created and any notable findings about the project.

## Important

- Be specific to this project, not generic
- Include actual file paths and component names
- Extract real commands from package.json/config files
- Note any unusual patterns or project-specific conventions
