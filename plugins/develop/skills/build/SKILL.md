---
name: build
description: Write tests and implementation together for a user story
---

# Build Story

Write tests and implementation together for a user story. Tests and code evolve in tandem — define the behaviour, implement it, iterate until all tests pass.

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

Before writing anything, understand the project's conventions:

- Look for existing test files using Glob to understand the testing framework, directory structure, naming conventions, and mocking patterns
- Read 2-3 existing test files to learn the exact style and patterns used
- Look for existing source files similar to what you need to create — understand the architecture, naming, and dependency patterns
- Discover the available commands for testing, linting, and formatting by exploring project configuration files
- Identify test utilities, fixtures, factories, or helpers already in the codebase

### 3. Write Tests

For each acceptance criterion, write test cases following the project's established conventions:

- Same testing framework, file naming pattern, and test structure
- Same mocking approach, utilities, and assertion style
- Tests may reference classes, functions, and modules that do not exist yet — that is expected

### 4. Implement

Follow the project's established architecture. Implement in dependency order — create things that other things depend on first.

Write the minimum code to satisfy the tests. No gold-plating, no extra methods, no speculative features.

### 5. Run Tests

Run the project's test command. All tests must pass — both the new ones and existing ones.

If tests fail, read the error output and decide: fix the implementation, or fix the test if it is genuinely wrong. Iterate until all tests pass.

### 6. Run Linters

Run the project's lint and type-check commands. Fix any violations.

### 7. Write Summary

Derive `story-slug` from the story filename. Create the directory `docs/reviews/{story-slug}/` if it does not exist.

Write to `docs/reviews/{story-slug}/01-build.md`:

```markdown
# Phase 1: Build

**Story:** {story file path}
**Date:** {ISO date}

## Test Files

- `path/to/test_file` — {what it tests}

## Implementation Files

- `path/to/file` — {purpose}

## Files Modified

- `path/to/file` — {what changed}

## Acceptance Criteria Coverage

| Criterion        | Test(s)          |
| ---------------- | ---------------- |
| {criterion text} | {test reference} |

## Test Corrections

{Only include this section if test files were modified after the initial write. For each change, explain what was wrong and why it was corrected. Omit this section entirely if no corrections were made.}

## Test Results

{Paste the final test output showing all tests passing}

## Lint/Type Check Results

{Paste lint output}
```

## Rules

- Prefer testing behaviour over testing implementation details.
- You MAY modify test files during iteration to correct genuine errors (wrong import path, incorrect assertion, broken setup). Do NOT modify tests to paper over a weak implementation.
- Document every test correction in the "Test Corrections" section with a clear reason.
- Do NOT add features beyond what the acceptance criteria require.
- Do NOT stop until all tests pass and linters are clean.
