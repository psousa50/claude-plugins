# /commit-msg

Analyse the current git diff and conversation context to generate a single-line commit message.

## Instructions

### Phase 1: Gather Context

Run in parallel:
- `git diff --staged` — staged changes (priority)
- `git diff` — unstaged changes (if nothing staged)
- Review conversation history for context on what was being worked on

### Phase 2: Analyse

Determine:
- What changed (files, functions, features)
- Why it changed (bug fix, feature, refactor, etc.)
- Conversation context (was this fixing a specific issue discussed?)

### Phase 3: Generate Message

Create a single-line commit message following these rules:
- Start with verb: add, fix, update, remove, refactor, rename, move
- Lowercase, no period at end
- Max 72 characters
- Focus on *what* and *why*, not *how*
- Be specific: "fix login redirect loop" not "fix bug"

### Phase 4: Output

Display only the commit message, nothing else. No explanation, no alternatives.
