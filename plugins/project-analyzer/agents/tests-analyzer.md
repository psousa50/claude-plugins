# Tests Analyzer

Analyze testing structure and generate a tests skill.

## Instructions

Explore the codebase to understand:
- Testing framework(s) used
- Test organization (unit, integration, e2e)
- Test file naming conventions
- Mocking patterns
- Test utilities and helpers
- Coverage configuration
- CI test setup

Look for:
- Test files and directories
- Test configuration files
- Mock/fixture files
- Test utilities
- Coverage reports/config

Create the folder `.claude/skills/tests/` and generate `SKILL.md` inside it:

```markdown
---
name: tests
description: Explains this project's testing patterns, structure, and how to write tests
---

# Testing Guide

## Framework
[Testing framework and tools used]

## Structure
[How tests are organized]

## Running Tests
[Commands to run tests]

## Writing Tests
[Patterns and conventions for writing tests]

## Mocking
[How to mock dependencies]

## Test Utilities
[Available test helpers and utilities]
```

Return a summary of the testing findings.
