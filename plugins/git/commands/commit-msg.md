# /commit-msg

Generate a single-line commit message based on the conversation context, using the git diff to confirm scope.

## Instructions

### Phase 1: Gather Context

Run in parallel:

- Review the full conversation history — this is the primary source of intent
- `git diff --staged` — to confirm what's actually staged

If nothing is staged, inform the user and stop.

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

### Phase 4: Output

Display only the commit message, nothing else. No explanation, no alternatives.
Do not commit or push code, only generate the message.
