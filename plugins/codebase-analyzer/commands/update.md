# /update

Update existing project skills and CLAUDE.md with the latest codebase information.

## Instructions

### Phase 1: Check Existing Skills

Read the current state:
- Check which skills exist in `.claude/skills/`
- Read `CLAUDE.md` from project root if it exists

### Phase 2: Discovery

Run the **discovery** agent to detect current project aspects:
- api, database, tests, frontend, backend, infrastructure, documentation

Compare with existing skills to identify:
- **Existing** — skills that need updating
- **New** — aspects detected but no skill exists yet
- **Stale** — skills that exist but aspect no longer detected (warn user, don't delete)

### Phase 3: Update Skills

For **existing** skills, run the relevant analyzer and update the skill:
- Preserve any manual sections marked with `<!-- manual -->` comments
- Update auto-generated content with fresh analysis

For **new** aspects, run the analyzer and create the skill.

For **stale** skills, warn the user but don't delete (they may have added them manually).

### Phase 4: Update CLAUDE.md

Update `CLAUDE.md` in the **project root directory**:
- Refresh all sections with latest information
- Add sections for newly detected aspects
- Keep the same structure

### Phase 5: Report

Summarize:
- Skills updated
- New skills created
- Stale skills detected (if any)
- Key changes since last analysis
