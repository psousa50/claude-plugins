---
name: genai-review
description: Review an Equal Experts Gen AI Engineer take-home test submission (typically a RAG pipeline exercise) against the EE assessment rubric. Use when reviewing a candidate's Gen AI / LLM / RAG take-home test, assessing a retrieval-augmented-generation or prompt-engineering exercise, or scoring a THT for a Gen AI Engineer role.
---

Review a candidate's Take Home Test submission for the Equal Experts Gen AI Engineer role. The exercise is a RAG pipeline over Equal Experts case studies (chunking → embedding → vector search → LLM answering), built on top of a **provided baseline scaffold**. Our company only hires senior engineers — calibrate expectations accordingly.

## The Baseline

This exercise ships a working scaffold; the candidate fills in specific gaps. **Credit and criticise only what the candidate added — never the scaffold.** Before reviewing, run `git log --oneline`, identify the baseline commit(s) (the provided template, authored before the candidate started — typically messages like "Add python exercise template" / "Initialising readme"), and review the candidate's work as the **diff on top of that baseline**.

### Provided by the scaffold — do NOT credit or penalise the candidate for these
- `src/llm/ollama.py` — the Ollama HTTP client (`generate`, `get_embeddings`, `close`), fully implemented
- `src/vectorstore/milvus_store.py` — the Milvus vector store (`create_collection`, `insert_embeddings`, `retrieve`), fully implemented
- `src/rag/pipeline.py::query` — retrieval + prompt + generation, **including a base prompt that already instructs the model to refuse when context is insufficient**, and `top_k` / `temperature` wiring
- `BaseChunker` / `BaseLLM` abstractions; `config.py` defaults (chunk size 500, overlap 50, top_k 3, temperature 0.7); `main.py` driver; `case_studies.json` data
- Tooling already configured: mypy (strict), ruff, black, isort, pytest
- Stub tests — `tests/test_chunking_strategies.py::test_simple_chunker` is an empty `pass`; `test_pipeline_query` is a provided mock-only test

### The candidate is expected to implement
1. `SimpleChunker.chunk_text` — size + overlap chunking
2. `RAGPipeline.add_documents` — load `case_studies.json`, chunk → embed → store, **replacing the fixed-text / fixed-embedding stub** (a submission that still returns the hardcoded `fixed_texts` has not done the core task)
3. **Evaluation metrics** to measure pipeline performance (external tools allowed) — this is an explicit, required step, not a nice-to-have
4. `AdvancedChunker` + its `chunk_text` — the stated end goal: a more sophisticated strategy than fixed-size
5. Re-evaluation after the advanced chunker, plus any prompt improvements
6. Unit tests for their own code (the chunkers, `add_documents`)
7. Written answers to the three README questions: how to improve the pipeline, chunking-strategy trade-offs, and what it takes to go to production

Completion calibration: `SimpleChunker` + real `add_documents` + some evaluation is the baseline expectation. Reaching `AdvancedChunker` with a before/after evaluation comparison is a strong signal. Not finishing the advanced chunker is not an automatic fail — but a thoughtful, evaluated comparison is what separates a strong submission from a passable one.

## Setup

1. Read the assessment rubric at `references/rubric.md` in this skill's directory — this defines the exact pass/fail criteria
2. Read the README.md in the current repo to understand:
   - The problem statement and requirements (what corpus, what questions, what output)
   - Any candidate assumptions or notes
   - AI tool usage disclosures
   - How to run the pipeline and the evaluation

## Codebase Analysis

3. Run `git log --oneline` and identify the baseline commit(s). Run `git diff <baseline>..HEAD --stat` (and the full diff on the source files) so you review the candidate's additions, not the scaffold. If the history has been squashed or the baseline is unclear, fall back to the "Provided by the scaffold" list above to separate scaffold from candidate work
4. List all files in the repo (excluding .git, virtualenvs, caches, `milvus.db` and other vector-store dumps, large data/model files)
5. Read the dependency/config files (`pyproject.toml`, `poetry.lock`) and note any dependencies the candidate added beyond the baseline (e.g. an evaluation framework like ragas/deepeval)
6. Focus your reading on the candidate-implemented surfaces: `SimpleChunker.chunk_text`, `AdvancedChunker`, `RAGPipeline.add_documents`, any prompt changes in `query`, plus any new modules they introduced (evaluation, preprocessing, scripts)
7. Read the evaluation code, notebooks, and any evaluation datasets or result outputs
8. Read every test file, distinguishing candidate-written tests from the provided stubs
9. Check the README / notes for the candidate's written answers to the three questions and any assumptions or AI-usage disclosures

## Run It — Mandatory Smoke Test (before rating Gen AI / RAG)

A static code review of a RAG submission is **not sufficient** and has repeatedly produced wrong verdicts: a polished pipeline can return zero correct answers, and the candidate's own reported results can be wrong. **You must run the pipeline against the brief's canonical questions and read the retrieved context before rating Gen AI / RAG.** Polish is not function.

Procedure:
1. Ensure Ollama is running with the required models pulled — `nomic-embed-text` plus the model in `config.py` (often `llama3.2`, sometimes `qwen2.5:7b`). If the candidate switched the core pipeline to a paid API (e.g. OpenAI in `config.py`), either supply a key or temporarily point `LLM_MODEL` / `EMBEDDING_MODEL` back to the Ollama defaults to exercise retrieval — and note the deviation.
2. **Delete any stale vector store first** (`rm -rf milvus.db`) — some submissions reuse a persisted collection across runs and contaminate results.
3. Run the driver on the brief's example questions — e.g. `poetry run python -m src.main`. The **scaffold ships exactly two canonical questions: "What work did Equal Experts do for IG Group?" and "What was demonstrated in the Forrester study?"** (read them from the README / baseline `main.py` — do not assume; a candidate may have added or changed them). Count how many are answered vs return "I cannot answer". Then also test any questions the candidate added, plus at least one **named-entity stress question whose case study is in the corpus** (e.g. "How did Equal Experts help HMRC?") — proper-noun retrieval is the failure mode worth stressing.
4. **Inspect retrieval, not just the answers.** Use `references/retrieval_probe.py` (copy into the repo root, run with `PYTHONPATH=. poetry run python retrieval_probe.py`) to print the top-k retrieved chunks per question. Confirm the *relevant* case-study content is actually present — not headings, "Full case study" boilerplate, or related-links navigation.

Interpret what you see:
- **Answers most questions, relevant chunks retrieved** → retrieval works; rate on sophistication.
- **Refuses, and retrieval returned irrelevant / boilerplate chunks** → genuine retrieval failure (a floor miss), no matter how clean the code looks.
- **Refuses, but the right chunk *was* retrieved** → a prompt/generation issue, milder than a retrieval failure. Only chunk-level inspection separates these — a refusal alone does not.

### The retrieval anti-pattern that hides behind a clean pipeline
The most common silent failure is **`metric_type="IP"` (inner product) over un-normalised embeddings**. `nomic-embed-text` returns vectors with norm ~18, not 1, so inner product ranks by *magnitude*, not meaning — the same high-magnitude chunk (often boilerplate) wins for every query. Check `milvus_store.py` for the metric, and check whether the candidate normalises embeddings or switched to `COSINE`. If it is `IP` + un-normalised, retrieval is almost certainly broken even though every line looks reasonable. The fix is one line (cosine, or L2-normalise the vectors); not making it — and not *noticing* — is the failure.

Named anti-patterns to grep/check for:
- `metric_type="IP"` + un-normalised embeddings → magnitude-dominated retrieval (silent failure).
- `create_collection` that reuses or appends to an existing collection across runs → contaminated before/after comparison and accumulating duplicates.
- Named-entity questions (HMRC, "IG Group") failing while topical ones (Forrester) succeed → dense-only retrieval can't match proper nouns; the fix is hybrid / keyword (BM25) search. This is a ceiling technique, not required to pass, but name the gap.
- LLM-as-judge that returns a default score (e.g. `0.0`) on a parse failure or in an `except` → silent zeros make a low score uninterpretable.
- Boilerplate/heading chunks ("Full case study", `####` headings, related-links nav) surviving into retrieved context → weak or absent data cleaning, even if a "boilerplate filter" is claimed.

## Evaluation

Assess the submission against each of the three rubric areas. For each area, determine a rating of Pass, Pass with Concern, or Fail.

### Gen AI / RAG Engineering

Check the candidate's additions for:
- **`add_documents`** — does it actually load `case_studies.json`, chunk, embed via the provided client, and store? A submission still returning the hardcoded `fixed_texts`/`fixed_embeddings` stub has not completed the core task
- **`SimpleChunker.chunk_text`** — correct size + overlap handling, and sensible behaviour on edge cases (text shorter than chunk size, final chunk, overlap larger than chunk)
- **`AdvancedChunker`** — did they reach the end goal, and is the strategy genuinely more sophisticated (e.g. sentence/paragraph/semantic boundaries) with a stated rationale, rather than a cosmetic variation of fixed-size?
- **Deliberate changes to provided defaults** — changing temperature, top_k, or improving the base prompt are positive signals of going beyond the scaffold (the README explicitly invites prompt improvements)
- Reasonable handling of the case-study data (any cleaning/preprocessing before chunking)

Watch for concern indicators:
- `add_documents` left as the fixed-text stub, or only partially wired (chunks but doesn't embed/store correctly)
- Chunking that silently drops text, produces empty chunks, or mishandles overlap
- Unneeded dependencies, unused or commented-out code
- Poor error handling around the data load / model calls in code the candidate added
- GenAI-assisted code is fine — but the candidate must apply their own judgement on top, not paste defaults

Do NOT credit the candidate for the provided client, vector store, base prompt, or abstractions. Do not penalise them for leaving the provided defaults untouched *if* they otherwise show judgement — but examined, justified changes are what a senior is expected to surface.

Nice to see (not required to pass): text preprocessing/cleaning, re-ranking or hybrid search, query transformation, an improved prompt, deliberate parameter tuning with rationale.

### Evaluation & Testing

The README explicitly makes evaluation a required step ("As a next step, you should implement evaluation metrics"), and asks the candidate to evaluate again after the advanced chunker. Treat its absence accordingly.

Check for:
- **Systematic evaluation of RAG output quality** with appropriate metrics (e.g. faithfulness, answer relevance, context precision) — using an external tool (ragas, deepeval, etc.) is explicitly allowed and fine
- **A before/after comparison** of SimpleChunker vs AdvancedChunker, since the README asks for re-evaluation — this is the clearest evidence the evaluation actually drove decisions
- Whether metrics are thought through for the case-study Q&A task, or only generic off-the-shelf defaults
- **Candidate-written tests** for their own code — the `test_simple_chunker` stub filled in, tests for `add_documents` and the advanced chunker
- Acknowledgement of LLM non-determinism in how things are tested (not asserting on exact model output)

Watch for concern indicators:
- The provided `test_pipeline_query` (mock-only) left as the candidate's *only* test — it tests the scaffold, not their work, and does not count toward their testing
- The `test_simple_chunker` stub left as an empty `pass`
- Evaluation present but no evidence it informed the advanced chunker or any iteration
- Only generic metrics with no thought about fit
- Poor test naming, unclear tests, incomplete assertions, brittle tests that assert exact LLM output
- Dependency on a live endpoint (Ollama) is NOT in itself a warning
- **Reported results are claims, not evidence.** Committed `evaluation_results*.json` files, printed scores, and statements in `ANSWERS.md` ("AdvancedChunker wins on every axis") are unverified until you reproduce them. A contradiction between a candidate's stated conclusion and what the live run actually shows is itself a finding — it means the evaluation was not read or not trusted.
- **A narrow, candidate-chosen evaluation set can mask retrieval failure.** Four hand-picked questions that happen to retrieve well will look fine while the brief's own example questions fail. Always test the canonical questions yourself (see "Run It"), not only the candidate's set.

Nice to see (not required to pass): domain-tailored metrics, a curated evaluation set over the case studies, load/robustness testing against the API.

**If there is no evaluation of RAG quality at all, this is an automatic Fail** — it is a required step in the brief, not an optional flourish.

### Design & Engineering Practices

Check for:
- Code that fits cleanly into the existing scaffold conventions rather than fighting them
- New code organised sensibly (e.g. evaluation in its own module, not dumped into `main.py`)
- Magic values placed in `config.py` alongside the existing settings rather than hard-coded
- **Clean types and lint** — the scaffold ships mypy (strict), ruff, black and isort already configured, so a senior is expected to keep `mypy src/` and `ruff check` green. Type errors or lint failures in candidate code are a real concern given the tooling is right there
- Thoughtful written answers to the three README questions (pipeline improvements, chunking trade-offs, productionisation)

Watch for concern indicators:
- Over-engineering for the scope (the README explicitly says "keep the code simple")
- Evaluation or scratch code left tangled into `main.py` or the pipeline
- Secrets or API keys committed (none are needed — Ollama is local)
- Re-committing a large regenerated `milvus.db` or other build artefacts
- The three README questions ignored or answered superficially

## Review Mindset

First separate signal from scaffold: everything in the baseline commit is free. Assess the candidate by their diff. A polished-looking repo is mostly the template — ask "what did *they* actually write, and is it good?"

Before writing up your assessment, go back to the brief and verify point by point that the pipeline actually does what was asked — the right corpus, the right questions, the stated output format. The first thing to confirm: does `add_documents` genuinely chunk/embed/store `case_studies.json`, or is the fixed-text stub still there behind a real-looking pipeline? Don't assume — trace the flow.

For each pipeline stage, ask: "Is this decision justified, or is it a default the candidate never examined?" A senior Gen AI engineer chooses a chunk size for a reason; they don't accept 1000/200 because a tutorial used it.

For the retrieval step, ask: "Has the candidate verified retrieval actually returns relevant context, or only assumed it?" Retrieval quality is the most common silent failure in RAG — look for evidence they measured it, not just the generation. **Do not take this on trust — run the smoke test and read the retrieved chunks yourself (see "Run It").**

For the written answers, ask: "Do they reflect what this candidate's own pipeline actually does?" Comprehensive, polished answers that recommend techniques (hybrid search, re-ranking, metadata filtering) the candidate never measured — on a pipeline that does not retrieve correctly — read as generic/AI-drafted and disconnected from the work. The disconnect is the tell, not the polish. (AI authorship itself is fine and is a stage-2 follow-up, never a candidate-facing point — but do not credit the candidate with understanding a likely-AI-authored document demonstrates.)

For the evaluation, ask: "Does this metric measure something that matters for this problem, and did a result ever change a decision?" An evaluation that never drove iteration is a box-ticking exercise.

For each prompt, ask: "Does this constrain the model to the retrieved context, or does it leave room to hallucinate?" Check how missing/empty context is handled.

For each piece of config, ask: "Is anything secret or environment-specific hard-coded?" Committed keys and baked-in config are senior-level misses, not nits.

For each file, ask: "Is this file what it claims to be? Is it in the right place?" Don't take file names or candidate descriptions at face value.

## Important Rules

- The candidate had limited time. Look for indicators of ability, not production-ready code. However, "indicators of ability" must be calibrated to senior level — time pressure does not excuse issues a senior engineer would instinctively avoid (e.g. leaving the fixed-text stub in place, shipping code that fails the provided mypy/ruff config, leaving an evaluation that drives nothing, dead code). When in doubt, ask: "Would I expect a senior Gen AI engineer to know better here, even under time pressure?" If yes, it is a genuine concern, not a minor nit.
- Judge against what the scaffold asked for, in order: `SimpleChunker` + real `add_documents` **that actually retrieves and answers the brief's questions** (the floor), then evaluation, then `AdvancedChunker` + re-evaluation, hybrid/entity retrieval (the ceiling). Not reaching the ceiling is not a fail; a missing or stubbed floor, **a pipeline that answers none/almost none of the canonical questions when run**, or no evaluation at all, is. A ceiling miss (e.g. no hybrid search, so entity questions fail) is forgivable; a floor miss — especially one the candidate reports as a success — is not.
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
| Gen AI / RAG Engineering | ... |
| Evaluation & Testing | ... |
| Design & Engineering Practices | ... |

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
- **Cons** are flaws in the submission itself (unexamined chunking, retrieval never measured, evaluation that drives nothing, coupled pipeline, committed secrets, etc.). **Order them by importance, most material first.** Concrete defects (wrong output, hallucination-inviting prompt, committed key) come before defects that require a future drift to bite, which come before mitigated trade-offs and stylistic concerns. Same logic applies to Pros — lead with the most signal-bearing strengths.
- **Things to follow up on** are open questions the next interviewer might want to explore — including any AI tool usage disclosure. AI authorship percentage is NOT a con; it is a thing to probe at stage 2. Disclosed AI usage is the behaviour we want, not a strike against the candidate. Good Gen-AI-specific angles: how they would evaluate RAG quality systematically, how they would scale to 10M+ documents with real-time updates, how they would prevent hallucinations, what production monitoring they would add. Keep this section even when the verdict is "do not progress" — the items still serve the calibration discussion (e.g. the #interviews-dev-global check when there is more than one area of concern) and document what a borderline re-review would probe; frame them as what *would* be worth exploring, not as a promise of a next round.

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
- Recommendation is one or two short sentences: the verdict, and when it is "Do not progress" a brief clause naming the decisive reason so the verdict is not bare (e.g. "Do not progress — retrieval was never measured against the real pipeline and is reported as working.")
- Do not reference the rubric, or use terms like "fail" or "pass with concern" — frame everything in natural language

Save this section as plain text to `key-take-aways.txt` in the repo root.
