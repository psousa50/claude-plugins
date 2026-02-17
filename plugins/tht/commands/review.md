---
description: Review a Take Home Test submission against the EE assessment rubric
---

Review a candidate's Take Home Test submission for the Equal Experts Backend Software Engineer role.

## Setup

1. Read the assessment rubric at `${CLAUDE_PLUGIN_ROOT}/references/rubric.md` — this defines the exact pass/fail criteria
2. Read the README.md in the current repo to understand:
   - The problem statement and requirements
   - Any candidate assumptions or notes
   - AI tool usage disclosures

## Codebase Analysis

3. List all files in the repo (excluding .git, build outputs, bin/obj directories)
4. Read all project/build configuration files (e.g. .csproj, package.json, pom.xml, build.gradle, go.mod, Cargo.toml — whatever applies)
5. Read every source code file
6. Read every test file
7. Run `git log --oneline` to understand the development process and commit history

## Evaluation

Assess the submission against each of the three rubric areas. For each area, determine a rating of Pass, Pass with Concern, or Fail.

### Programming Knowledge

Check for:
- Code readability and clarity
- Whether the code produces the required output (verify against the sample in the README)
- Appropriate encapsulation
- Idiomatic use of the chosen language
- Appropriate type choices (e.g. decimal not float for money)

Watch for concern indicators:
- Has the candidate written an app (console, web, CLI)? The brief explicitly prohibits this
- Unneeded dependencies
- Unused or commented-out code
- Poor error handling

### Testing

Check for:
- Reasonable code coverage
- Test independence (tests can run in isolation)
- **HTTP client is tested** — this is a Pass criterion. Tests that only mock the service interface and assert mock return values do NOT count. The actual HTTP integration (request construction, response parsing, error handling) must be tested
- Adequate assertions
- No duplicated tests

Watch for concern indicators:
- Extraneous setup
- Poor test naming
- Incomplete assertions
- Dependency on live endpoints (integration tests against live endpoints are acceptable)

**If there are no tests at all, this is an automatic Fail.**

### Design

Check for:
- Minimal viable structure appropriate to the problem scope
- Clear domain model
- Appropriate dependencies

Watch for concern indicators:
- Overly coupled components
- Over-engineering / unnecessary complexity
- Large file count for a small problem

## Important Rules

- The candidate had ~90 minutes. Look for indicators of ability, not production-ready code.
- Maximum ONE "Pass with Concern" across all three areas to still recommend progressing.
- More than one "Pass with Concern" or any Fail = do not progress.
- The filter question is: **"Is this submission worth a further conversation with the candidate?"**

## Output

Structure your review with these four sections:

### Section 1: Detailed Review

For each rubric area provide:
- **Rating**: Pass / Pass with Concern / Fail
- **Positives**: What the candidate did well, with specific file:line references
- **Concerns**: Issues found, with specific file:line references and explanation of why it matters

Include a summary table:

| Area | Rating |
|---|---|
| Programming Knowledge | ... |
| Testing | ... |
| Design | ... |

State the overall verdict and whether the submission should progress to a face-to-face interview.

### Section 2: Scorecard — Candidate Feedback

Write the text for the "Feedback to share with the candidate" field in the scorecard. This should be:
- Professional and constructive
- Acknowledge what was done well
- Clearly explain the concerns
- Specific enough to be actionable
- 3-5 paragraphs

### Section 3: Scorecard — Key Take-Aways

Write the text for the "Key Take-Aways (conclusions, pros, cons, and things to follow up on)" field. This should be:
- Structured as Pros / Cons / Recommendation
- Concise bullet points for pros and cons
- Clear hire/no-hire recommendation with brief justification
