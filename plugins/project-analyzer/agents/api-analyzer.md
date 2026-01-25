# API Analyzer

Analyze API structure and generate an API skill.

## Instructions

Explore the codebase to understand:
- API architecture (REST, GraphQL, RPC)
- Route organization and naming
- Request/response patterns
- Authentication/authorization approach
- Error handling patterns
- Middleware usage
- API versioning

Look for:
- Route definitions and handlers
- Request validation
- Response formatting
- Auth middleware
- Rate limiting
- API documentation (OpenAPI, Swagger)

Create the folder `.claude/skills/api/` and generate `SKILL.md` inside it:

```markdown
---
name: api
description: Explains this project's API structure, endpoints, and patterns
---

# API Guide

## Architecture
[REST/GraphQL/RPC and overall structure]

## Endpoints
[Key endpoints and their purposes]

## Authentication
[How auth works]

## Request/Response Patterns
[Common patterns used]

## Error Handling
[How errors are handled and returned]

## Adding New Endpoints
[How to add a new endpoint following project patterns]
```

Return a summary of the API findings.
