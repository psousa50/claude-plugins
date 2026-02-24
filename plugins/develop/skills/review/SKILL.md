---
name: review
description: Review implementation code for issues and produce a written report
---

# Review Code

Review all code changes for a user story and produce an actionable report. Be thorough but pragmatic — only flag genuine issues, not style preferences already within the project's conventions.

## Input

`$ARGUMENTS` is the path to a story file.

## Steps

### 1. Read the Story

Read the file at `$ARGUMENTS`. Understand the acceptance criteria — the review must verify the implementation satisfies them.

### 2. Learn the Project

Before reviewing, understand what "correct" looks like:

- Look at a few existing source files similar to the changed ones to calibrate your expectations

### 3. Identify Changed Files

Run `git diff --name-only HEAD` and `git status --short` to find all changed, staged, and untracked files. Include everything — implementation files, test files, schema changes, configuration.

### 4. Read Every Changed File

Use the Read tool on each file. Read the full file, not just the diff — context matters for architectural correctness.

### 5. Review Against Checklist

Evaluate the code against each of these categories:

**Correctness**

- Does the implementation match every acceptance criterion?
- Are edge cases handled?

**Security**

- No injection vulnerabilities
- Authentication and authorisation enforced on all endpoints
- No data leakage across users or tenants
- Sensitive data not exposed in responses

**Architecture**

- Proper layer separation maintained
- Dependencies flow in the correct direction
- No business logic in the wrong layer

**Test Quality**

- Tests actually test behaviour, not just call code
- Edge cases covered
- Mocking follows project conventions
- Each acceptance criterion has at least one test

**Code Style**

- Follows the project's established conventions (learned from existing code)
- Consistent with patterns in similar existing files

**Naming**

- Follows the project's naming conventions exactly

**Performance**

- No obvious performance issues (N+1 queries, unbounded fetches, missing pagination)

**Consistency**

- New code follows patterns established in similar existing files
- Uses existing utilities and helpers rather than reinventing

### 6. Write Report

Derive `story-slug` from the story filename. Write to `docs/reviews/{story-slug}/02-review.md`:

```markdown
# Code Review

**Story:** {story file path}
**Date:** {ISO date}
**Status:** {PASS | ISSUES_FOUND}

## Summary

{One paragraph overall assessment}

## Critical

{Must fix. Each finding with file path and description.}

- `path/to/file:line` — {description of issue and what to fix}

## Warnings

{Should fix. Lower severity but still worth addressing.}

- `path/to/file:line` — {description}

## Suggestions

{Optional improvements. Not blocking.}

- {suggestion}

## Acceptance Criteria Check

| Criterion   | Status    | Evidence                 |
| ----------- | --------- | ------------------------ |
| {criterion} | PASS/FAIL | {test or code reference} |

## Files Reviewed

- `path/to/file` — {brief description}
```

If there are no Critical or Warning findings, set Status to `PASS`. Otherwise `ISSUES_FOUND`.

### 7. Output Summary

After writing the report, output a brief summary: total findings by severity and the report file path.

## Rules

- Every finding MUST reference a specific file and ideally a line number.
- Every finding MUST describe what to fix, not just what's wrong.
- Do NOT flag style choices that are consistent with the project's existing patterns.
- Be pragmatic — minor issues that don't affect correctness or security are Suggestions, not Warnings.
