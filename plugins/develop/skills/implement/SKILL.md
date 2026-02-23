---
name: implement
description: Write minimal implementation to make tests pass (tests-first green phase)
---

# Implement Story

Write the minimum implementation code to make all tests pass for a user story. Tests must already exist (written by the `/story-tests` phase or manually).

## Input

`$ARGUMENTS` is the path to a story file.

## Steps

### 1. Read the Story

Read the file at `$ARGUMENTS`. Understand the requirements, acceptance criteria, and technical notes.

### 2. Learn the Project

Before writing any code, understand the project's conventions:

- Discover the available commands for testing, linting, and formatting by exploring project configuration files
- Look for existing source files similar to what you need to create — understand the architecture, naming, and dependency patterns
- Identify dependency injection, configuration, or registration patterns that new code must follow

### 3. Find the Tests

Derive `story-slug` from the story filename. Read `docs/reviews/{story-slug}/01-tests.md` to find which test files were created.

Read every test file listed. Understand:

- What classes, functions, and modules the tests import
- What behaviour each test expects
- What interfaces, services, or components need to exist

### 4. Implement

Follow the project's established architecture and layer ordering. Implement in dependency order — create things that other things depend on first.

Write the minimum code to satisfy the tests. No gold-plating, no extra methods, no speculative features.

### 5. Run Tests

Run the project's test command. All tests must pass — both the new ones and existing ones.

If tests fail, read the error output, fix the implementation, and run again. Iterate until all tests pass.

### 6. Run Linters

Run the project's lint and type-check commands. Fix any violations.

### 7. Write Summary

Write to `docs/reviews/{story-slug}/02-implement.md`:

```markdown
# Phase 2: Implementation

**Story:** {story file path}
**Date:** {ISO date}

## Files Created

- `path/to/file` — {purpose}

## Files Modified

- `path/to/file` — {what changed}

## Test Results

{Paste the final test output showing all tests passing}

## Lint/Type Check Results

{Paste lint output}
```

## Rules

- Do NOT modify test files. If a test seems wrong, note it in the summary but implement to satisfy it.
- Do NOT add features beyond what tests require.
- Do NOT stop until all tests pass and linters are clean.
