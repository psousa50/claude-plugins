---
name: commit-msg
description: Generate a single-line commit message from conversation context and git diff, then optionally commit
---

# Commit Message

Generate a single-line commit message based on the conversation context, using the git diff to confirm scope.

## Instructions

### Phase 1: Gather Context

1. Review the full conversation history — this is the primary source of intent
2. Run `git diff --staged`
   - **If there is staged output, use it. Do NOT run `git diff` (unstaged). Skip to Phase 2.**
   - If there is no staged output, run `git diff` to check for unstaged changes
   - If neither staged nor unstaged changes exist, inform the user and stop

Only one diff should be in scope — staged takes priority. Ignore any unstaged diff output from earlier in the conversation if staged changes exist.

### Phase 2: Analyse

Priority order:

1. **Conversation intent** — what was the user trying to achieve? What problem were they solving? What did they ask for?
2. **Conversation arc** — did the approach evolve? Was there a key decision or pivot?
3. **Diff confirmation** — use the staged diff to verify scope and catch anything the conversation might not fully reflect

The conversation tells you _why_. The diff tells you _what_. Prefer _why_.

### Phase 3: Generate Message

Create a single-line commit message following these rules:

- Start with verb: add, fix, update, remove, refactor, rename, move
- Lowercase, no period at end
- Max 72 characters
- Focus on _what_ and _why_, not _how_
- Be specific: "fix login redirect loop" not "fix bug"
- Reflect the user's intent from the conversation, not just a mechanical description of changed lines

### Phase 4: Output & Commit

1. Display only the commit message, nothing else. No explanation, no alternatives.
2. Ask the user if they want to commit with this message.
   - If **yes** — run `git commit -m "<message>"` (stage all tracked changes first with `git add -u` if nothing is currently staged)
   - If **no** — stop. Do not commit.
