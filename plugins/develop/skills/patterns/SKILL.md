---
name: patterns
description: Shared code and test patterns for the story pipeline skills
---

# Story Pipeline Patterns

These patterns apply to all code written or modified by the story pipeline skills.

## Code Patterns

- Do NOT add comments, docstrings, or type annotations to code you didn't write. Only add comments where the logic isn't self-evident.
- Do NOT add features, refactor code, or make improvements beyond what was asked.
- Do NOT add error handling, fallbacks, or validation for scenarios that can't happen.
- Do NOT create helpers, utilities, or abstractions for one-time operations.
- Follow the project's existing code style strictly — learn it from existing files, not assumptions.
- Prefer simple, direct code over clever abstractions. Three similar lines is better than a premature abstraction.

## Test Patterns

- Never use `patch`, `mock.patch`, `vi.mock`, `jest.mock`, or any module-level mocking. Use dependency injection and constructor-level mocks instead.
- Only mock dependencies that are explicitly injected — never mock a module or file import directly.
