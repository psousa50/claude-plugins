# Build Analyzer

Analyze build process and generate a build skill.

## Instructions

Explore the codebase to understand:
- How to install dependencies
- How to run the project locally
- How to run tests
- How to build for production
- Environment setup requirements
- CI/CD configuration

Look for:
- package.json scripts
- Makefile, Taskfile, or similar
- pyproject.toml, Cargo.toml, go.mod
- Dockerfile, docker-compose.yml
- .env.example or environment documentation
- CI config (.github/workflows, .gitlab-ci.yml, etc.)
- README setup instructions

Generate `.claude/skills/build/SKILL.md`:

```markdown
---
name: build
description: Explains how to build, test, and develop this project
---

# Build & Development

## Prerequisites
[Required tools and versions]

## Installation
[How to install dependencies]

## Running Locally
[How to start the development server]

## Testing
[How to run tests]

## Building
[How to build for production]

## Environment Variables
[Required env vars and their purpose]

## Common Tasks
[Frequently used commands]
```

Return a summary of the build process.
