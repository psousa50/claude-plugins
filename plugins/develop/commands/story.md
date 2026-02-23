---
description: Run the full story implementation workflow (tests, implement, review, fix, final review)
---

Run the complete implementation workflow for a user story. This is a fire-and-forget orchestrator — it chains five phases sequentially using sub-agents for context isolation. Each phase writes artefacts to `docs/reviews/{story-slug}/` so you can review what happened after completion.

## Input

`$ARGUMENTS` is the path to a story file.

## Workflow

Derive `story-slug` from the story filename (strip the directory path and file extension). Create the directory `docs/reviews/{story-slug}/` if it does not exist.

Run each phase in sequence using the Task tool to launch sub-agents. Each sub-agent gets an isolated context window. Wait for each phase to complete before starting the next.

### Phase 1: Write Tests

Launch a sub-agent with subagent_type `general-purpose`:

```
Invoke the develop:tests skill with arguments: {$ARGUMENTS}

The story slug is: {story-slug}
```

When the sub-agent returns, confirm it reports tests were written and a summary exists at `docs/reviews/{story-slug}/01-tests.md`.

### Phase 2: Write Implementation

Launch a sub-agent with subagent_type `general-purpose`:

```
Invoke the develop:implement skill with arguments: {$ARGUMENTS}

The story slug is: {story-slug}
```

When the sub-agent returns, check its result. If it reports tests are NOT passing, STOP the workflow. Output an error message with the sub-agent's report and the path to any artefacts written so far.

### Phase 3: Code Review

Launch a sub-agent with subagent_type `general-purpose`:

```
Invoke the develop:review skill with arguments: {$ARGUMENTS}

The story slug is: {story-slug}
```

When the sub-agent returns, read `docs/reviews/{story-slug}/03-review.md` to check the review status.

### Phase 4: Fix Review Issues

Only run this phase if the review report status is `ISSUES_FOUND`.

If the review status is `PASS`, skip to Phase 5.

Launch a sub-agent with subagent_type `general-purpose`:

```
Invoke the develop:fix skill with arguments: {$ARGUMENTS}

The story slug is: {story-slug}
```

### Phase 5: Final Review

Launch a sub-agent with subagent_type `general-purpose`:

```
Invoke the develop:final-review skill with arguments: {$ARGUMENTS}

The story slug is: {story-slug}
```

## Completion

After all phases complete, read `docs/reviews/{story-slug}/05-final-review.md` and output:

1. **Verdict** — READY FOR MERGE or NEEDS ATTENTION
2. **Summary** — what was built (from the final review report)
3. **Artefacts** — list all files in `docs/reviews/{story-slug}/`
4. **Phase recap:**
   - Phase 1: {N} test files written
   - Phase 2: all tests passing / failed (if workflow stopped)
   - Phase 3: {N} critical, {N} warnings, {N} suggestions
   - Phase 4: {N} fixes applied / skipped (if review was clean)
   - Phase 5: verdict

## Error Handling

- If Phase 2 fails (tests not passing), stop immediately. Output what happened and the artefacts path.
- If any sub-agent fails unexpectedly, stop and report the phase that failed with whatever information is available.
- Do NOT continue to later phases if an earlier phase failed — there is no point reviewing broken code.
