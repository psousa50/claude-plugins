# /update-architecture

Update or create ARCHITECTURE.md by exploring the codebase and documenting its structure.

## Instructions

### Phase 1: Read Current State

Run in parallel:

- Read `ARCHITECTURE.md` from the project root (if it exists)
- Scan the project root for config files, entry points, and directory structure

If ARCHITECTURE.md exists, note its current structure — preserve the same sections and ordering unless the codebase has diverged.

### Phase 2: Explore

Run exploration agents in parallel to map the codebase:

- **Server-side**: entry points, modules, classes, key abstractions, database schema
- **Client-side**: framework, routing, components, state management, hooks
- **Configuration**: environment variables, build setup, auth

Focus on structure and relationships, not implementation details. The goal is a map, not a manual.

### Phase 3: Diff Against Current

If ARCHITECTURE.md already exists, identify:

- **New** — files, modules, routes, or patterns not yet documented
- **Changed** — documented items whose role or structure has shifted
- **Removed** — documented items that no longer exist
- **Unchanged** — skip these entirely

If creating from scratch, skip this phase.

### Phase 4: Write ARCHITECTURE.md

Write `ARCHITECTURE.md` at the project root covering:

1. **One-line overview** — what the app is
2. **Tech stack** — key technologies (one line)
3. **Directory structure** — annotated tree, one-liner per file/folder explaining its role
4. **Data flow** — how data moves through the system (pipeline style)
5. **Database schema** — tables and relationships (if applicable)
6. **API surface** — REST routes and real-time events (if applicable)
7. **Configuration** — provider abstractions, env vars, feature toggles
8. **Auth** — authentication approach (if applicable)
9. **Key patterns** — architectural decisions and conventions

Rules:

- No code snippets — describe, don't duplicate
- No implementation details — focus on what each module does, not how
- Keep it under 150 lines
- Use consistent formatting: headers, tables, annotated trees

### Phase 5: Ensure CLAUDE.md References

Read `CLAUDE.md` from the project root. Ensure it contains both of these lines:

```
Read ARCHITECTURE.md before planning features.
Update ARCHITECTURE.md when making changes that affect its content.
```

- If `CLAUDE.md` doesn't exist, create it with those two lines
- If it exists but is missing either line, add the missing line(s) — don't remove or reorder existing content

### Phase 6: Report

Show a brief summary of changes made:

- Sections added or updated
- Notable structural changes detected
- Anything that looked ambiguous and may need manual review
