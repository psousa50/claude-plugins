---
name: tests
description: Write tests from a user story's acceptance criteria (tests-first, before implementation)
---

# Write Tests from Story

Write test files for a user story BEFORE any implementation exists. The goal is to produce tests that act as a specification — they define what the implementation must satisfy and ensure the code is testable by design.

## Input

`$ARGUMENTS` is the path to a story file.

## Steps

### 1. Read the Story

Read the file at `$ARGUMENTS`. Extract:

- Acceptance criteria (checkboxes, numbered lists, or prose)
- Technical notes and implementation guidance
- API contracts (request/response examples)
- User flows

### 2. Learn the Project

Before writing any tests, understand the project's conventions:

- Look for existing test files using Glob to understand the testing framework, directory structure, naming conventions, and mocking patterns
- Read 2-3 existing test files to learn the exact style and patterns used
- Identify test utilities, fixtures, factories, or helpers already in the codebase

### 3. Determine Scope

From the acceptance criteria, identify which layers and components need tests. Use the project's existing test directory structure as your guide — place new tests alongside similar existing tests.

### 4. Write Tests

For each acceptance criterion, write one or more test cases following the project's established conventions exactly:

- Same testing framework
- Same file naming pattern
- Same test structure (class-based, function-based, describe blocks — match what exists)
- Same mocking approach and utilities
- Same assertion style

Tests WILL reference classes, functions, and modules that do not exist yet. This is expected and correct — the implementation comes later.

### 5. Write Summary

Create the directory `docs/reviews/{story-slug}/` if it does not exist (derive `story-slug` from the story filename).

Write a summary to `docs/reviews/{story-slug}/01-tests.md`:

```markdown
# Phase 1: Tests Written

**Story:** {story file path}
**Date:** {ISO date}

## Test Files Created

- `path/to/test_file` — {what it tests}

## Acceptance Criteria Coverage

| Criterion        | Test(s)          |
| ---------------- | ---------------- |
| {criterion text} | {test reference} |

## Notes

{Any decisions made, assumptions, or gaps}
```

## Rules

- Do NOT write any implementation code. Only test files.
- Do NOT run the tests — they cannot pass without implementation.
- Each acceptance criterion must map to at least one test.
- Prefer testing behaviour over testing implementation details.
