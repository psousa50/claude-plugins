---
description: Review a Take Home Test submission against the EE assessment rubric
---

Review a candidate's Take Home Test submission for the Equal Experts Backend Software Engineer role. Our company only hires senior engineers — calibrate expectations accordingly.

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

## Review Mindset

Before writing up your assessment, go back to the brief's requirements and verify point by point that the candidate's public API actually satisfies them. Don't assume — check method signatures against the stated interface.

For each class, ask: "Does this have a single clear responsibility?" If a class is doing multiple jobs, trace the consequences — does it make the tests harder to write? Does it force complex mocking? Design problems in production code often surface as pain in the tests.

For each method, ask: "Does this method do what its name says and nothing more?" Look for hidden side effects, especially in methods whose names suggest they are queries.

For each piece of stored state, ask: "Is this the source of truth, or could it be derived from other data that already exists?" Redundant state is a bug waiting to happen.

For each file, ask: "Is this file what it claims to be? Is it in the right place?" Don't take file names or candidate descriptions at face value.

## Important Rules

- The candidate had ~90 minutes. Look for indicators of ability, not production-ready code. However, "indicators of ability" must be calibrated to senior level — time pressure does not excuse issues a senior engineer would instinctively avoid (e.g. committing IDE files, leaving dead code, ignoring the brief's constraints, copy-pasting test setup). When in doubt, ask: "Would I expect a senior engineer to know better here, even under time pressure?" If yes, it is a genuine concern, not a minor nit.
- Do NOT default to leniency. A borderline rating should land on the stricter side. It is better to flag a concern that turns out to be minor in a follow-up interview than to let a weak submission through unchallenged.
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
- **Short: 2-3 short paragraphs maximum.** Aim for under ~150 words total. Density over length.
- Do not reference the rubric, or use terms like "fail" or "pass with concern" — frame everything in natural language

Avoid the following — they pad the feedback without adding signal:
- Closing or forward-looking paragraphs ("we look forward to…", "in the next round we will…", "thank you for your time"). End on the last substantive point.
- Meta-commentary about AI tool usage. Do not praise candour, honesty, or self-awareness about AI. If AI authorship is relevant, it belongs in the Key Take-Aways follow-up list, not in candidate-facing feedback.
- Restating the rubric, the brief, or what the task was.
- Hedging filler ("overall", "broadly speaking", "generally").
- Listing every positive — pick the two or three that most signal ability and move on.

Save this section as plain text to `candidate-feedback.txt` in the repo root.

### Section 3: Reviewer Notes (private, not for the scorecard)

Write a longer Pros / Cons / Things to follow up on list, **for the reviewer's own use** — to brief themselves before the next interview round and to keep the depth that gets stripped out of the scorecard summary. This is the working scaffold, not a candidate-facing artefact.

- Structured as **Pros / Cons / Things to follow up on / Recommendation**
- One sentence per bullet, with enough context (file:line where useful, why the issue matters) to brief a stage-2 interviewer cold
- Do not reference the rubric, or use terms like "fail" or "pass with concern" — frame everything in natural language

Bucket guidance:
- **Cons** are flaws in the submission itself (wrong type choice, missing test boundary, coupled design, etc.). **Order them by importance, most material first.** Concrete bugs (something that produces wrong behaviour or a crash on a plausible input) come before defects that require a future drift to bite, which come before mitigated trade-offs and stylistic concerns. Same logic applies to Pros — lead with the most signal-bearing strengths.
- **Things to follow up on** are open questions the next interviewer might want to explore — including any AI tool usage disclosure. AI authorship percentage is NOT a con; it is a thing to probe at stage 2. Disclosed AI usage is the behaviour we want, not a strike against the candidate.

Tone for the Recommendation and follow-ups:
- **Suggest, do not mandate.** The next interviewer decides their own approach. Use phrasing like "could be useful to explore", "may be worth checking", "worth discussing if time allows". Avoid "must verify", "should probe", "use stage 2 to…", or any imperative that tells the next interviewer what to do.
- Keep the Recommendation to **2-3 sentences**. State the verdict, name the gap area in a phrase, optionally surface angles for the next round. No calibration jargon ("senior", "indicators of ability"), no restating the rubric.
- **Relative-quality calibration is welcome when it is genuinely true.** A line like "one of the strongest submissions seen recently" or "weakest submission this quarter" is high-signal for downstream interviewers and changes how they prepare. Only include it when it actually applies — it has to mean something. If the submission is solidly average, say nothing on this dimension.

Save this section as plain text to `reviewer-notes.txt` in the repo root.

### Section 4: Scorecard — Key Take-Aways

Write the text for the "Key Take-Aways (conclusions, pros, cons, and things to follow up on)" field. **This is the short, scorecard-bound version of the reviewer notes** — same structure, ruthlessly trimmed.

- Same four headings: **Pros / Cons / Things to follow up on / Recommendation**
- Aim for **3-5 bullets per section, max one short sentence per bullet.** Whole document under ~150 words.
- Drop file:line references and explanatory clauses — they belong in the reviewer notes, not the scorecard
- Recommendation is one sentence (e.g. "Progress." / "Do not progress.")
- Do not reference the rubric, or use terms like "fail" or "pass with concern" — frame everything in natural language

Save this section as plain text to `key-take-aways.txt` in the repo root.
