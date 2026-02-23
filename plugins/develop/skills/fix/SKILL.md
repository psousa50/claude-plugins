---
name: fix
description: Read a review report and apply fixes to the codebase
---

# Fix Review Issues

Read a code review report and apply all necessary fixes. Critical findings are mandatory. Warnings are applied unless disproportionate. Suggestions are skipped.

## Input

`$ARGUMENTS` is the path to a story file.

## Steps

### 1. Find the Review Report

Derive `story-slug` from the story filename. Read `docs/reviews/{story-slug}/03-review.md`.

If the report status is `PASS`, there is nothing to fix. Write a brief summary to `docs/reviews/{story-slug}/04-fix.md` noting no fixes were needed, and stop.

### 2. Learn the Project

Discover the project's test and lint commands by exploring project configuration files. Look at existing source files to understand the code style.

### 3. Parse Findings

Categorise the findings:

- **Critical** — must fix, no exceptions
- **Warnings** — fix unless doing so requires a disproportionate refactor or conflicts with a Critical fix
- **Suggestions** — skip (these are for humans to consider later)

### 4. Apply Fixes

For each Critical finding, then each Warning:

1. Read the referenced file
2. Understand the issue described
3. Apply the fix
4. Move to the next finding

Do not introduce new features or refactor beyond what the findings require.

### 5. Run Tests

Run the project's test command. All tests must still pass after fixes.

If a fix breaks a test, the fix is wrong — revert it and try a different approach. Tests are the source of truth.

### 6. Run Linters

Run the project's lint and type-check commands. Fix any issues introduced by the fixes.

### 7. Write Summary

Write to `docs/reviews/{story-slug}/04-fix.md`:

```markdown
# Phase 4: Fixes Applied

**Story:** {story file path}
**Date:** {ISO date}

## Critical Fixes

- `path/to/file:line` — {what was fixed}

## Warning Fixes

- `path/to/file:line` — {what was fixed}

## Skipped

- {finding reference} — {reason for skipping}

## Test Results

{Final test output confirming all pass}
```

## Rules

- Do NOT modify test files unless a review finding specifically says to.
- Do NOT add features or refactor beyond what findings require.
- Do NOT apply Suggestions — they are informational only.
- If a fix breaks tests, revert and find an alternative approach.
