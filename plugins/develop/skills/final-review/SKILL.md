---
name: final-review
description: Final quality review producing a human-readable report
---

# Final Review

Produce a final human-readable review report after all fixes have been applied. This report is for a human reviewer — concise, clear, and focused on whether the story is ready for merge.

## Input

`$ARGUMENTS` is the path to a story file.

## Steps

### 1. Read Context

Derive `story-slug` from the story filename. Read:

- The story file at `$ARGUMENTS` — for acceptance criteria
- `docs/reviews/{story-slug}/03-review.md` — previous review findings
- `docs/reviews/{story-slug}/04-fix.md` — what was fixed (if it exists)

### 2. Learn the Project

Discover the project's test commands by exploring project configuration files. Look at existing source files to understand the code style and conventions.

### 3. Verify Previous Findings Resolved

For each Critical and Warning finding from the previous review, check the specific file and line referenced. Confirm the fix was applied correctly.

### 4. Fresh Review

Run `git diff --name-only HEAD` and `git status --short` to find all changed files. Read every changed file.

Do a holistic review focused on:

- Do all the pieces fit together cohesively?
- Were any new issues introduced by the fixes?
- Is every acceptance criterion covered by a passing test?
- Would a human reviewer find anything surprising or concerning?

### 5. Run Tests

Run the project's test command. Confirm all tests pass.

### 6. Write Final Report

Write to `docs/reviews/{story-slug}/05-final-review.md`:

```markdown
# Final Review

**Story:** {story file path}
**Date:** {ISO date}
**Verdict:** {READY FOR MERGE | NEEDS ATTENTION}

## What Was Built

{2-3 sentence summary suitable for a PR description}

## Acceptance Criteria

| Criterion        | Status    | Test             |
| ---------------- | --------- | ---------------- |
| {criterion text} | PASS/FAIL | {test reference} |

## Previous Review

- **Critical findings:** {N} found, {N} resolved
- **Warnings:** {N} found, {N} resolved

## Remaining Concerns

{List any issues that still need attention, or "None"}

## Files Changed

- `path/to/file` — {one-line description}

## Test Results

{Summary: N tests passed, 0 failed}
```

### 7. Output Verdict

After writing the report, output:

- The verdict (READY FOR MERGE or NEEDS ATTENTION)
- The report file path
- A one-line summary

## Rules

- The report is for humans — be concise, not exhaustive.
- If any acceptance criterion lacks a test, mark it FAIL.
- If any Critical finding from the previous review was not resolved, verdict is NEEDS ATTENTION.
- Be honest about the verdict — READY FOR MERGE means you'd be comfortable merging this.
