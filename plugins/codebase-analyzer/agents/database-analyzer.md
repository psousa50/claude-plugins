# Database Analyzer

Analyze database structure and generate a database skill.

## Instructions

Explore the codebase to understand:
- Database type (SQL, NoSQL, etc.)
- ORM/query builder used
- Schema organization
- Migration patterns
- Relationships between entities
- Query patterns
- Connection management

Look for:
- Schema definitions
- Model files
- Migration files
- Seed files
- Database configuration
- Query helpers/utilities

Create the folder `.claude/skills/database/` and generate `SKILL.md` inside it:

```markdown
---
name: database
description: Explains this project's database schema, models, and data patterns
---

# Database Guide

## Technology
[Database type and ORM/tools used]

## Schema Overview
[Key tables/collections and their purposes]

## Relationships
[How entities relate to each other]

## Migrations
[How migrations work]

## Query Patterns
[Common query patterns used]

## Adding New Models
[How to add a new model/table following project patterns]
```

Return a summary of the database findings.
