# Patterns Analyzer

Analyze coding patterns and generate a patterns skill.

## Instructions

Explore the codebase to identify:
- Naming conventions (files, functions, variables, classes)
- Code organisation patterns
- Design patterns used (MVC, repository, factory, singleton, etc.)
- Error handling approach
- State management patterns (if frontend)
- API patterns (if backend)
- Testing patterns

Look at:
- Multiple source files to identify consistent patterns
- How errors are handled and propagated
- How state is managed and shared
- How dependencies are injected or managed
- Code style (functional vs OOP, etc.)

Generate `.claude/skills/patterns/SKILL.md`:

```markdown
---
name: patterns
description: Explains coding patterns and conventions used in this project
---

# Code Patterns

## Naming Conventions
[File naming, function naming, variable naming]

## Design Patterns
[Patterns used and where]

## Error Handling
[How errors are handled]

## State Management
[How state is managed - if applicable]

## Code Style
[Functional vs OOP, formatting conventions]

## Examples
[Brief code examples demonstrating key patterns]
```

Return a summary of the patterns found.
