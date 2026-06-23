# Gen AI Engineer - Take Home Test Assessment Rubric

This interview stage is for assessing a candidate's submission to the Gen AI Take Home Test problem statement (typically a RAG pipeline exercise), and the barrier to entry is based on the question:

**"Is this submission worth a further conversation with the candidate?"**

Given the time-boxed nature of the exercise, it's important to remember that we aren't looking for perfect, production-ready solutions — we are looking for indicators of ability across Gen AI engineering, evaluation, and sound software practices.

The exercise is built on a **provided baseline scaffold** (the Ollama client, Milvus vector store, the `query` method and its base prompt, config, and tooling are all given). Assess only what the candidate added — the chunkers, `add_documents`, evaluation, tests, prompt/parameter changes, and the written answers. See the skill's "The Baseline" section for the exact split.

The result for each category should be one of:
- Pass
- Pass with concern
- Fail

Pass with concern is specifically there to highlight to the following interviewers your areas of concern, remember that the filter level for this interview stage is "is this worth a further conversation".

You may return a maximum of **one** "Pass with Concern" across all three areas, and still move to a Face to Face interview. If you have more than one rating of "Pass with Concern" across all three areas then raise it in the #interviews-dev-global channel before deciding whether or not to fail the candidate.

The submission should be failed if there are any areas that fall outside of the Pass or Pass with concern categories.

In all cases feedback should be recorded.

## 1. Gen AI / RAG Engineering

| *Look for deliberate, justified Gen AI decisions — not defaults left untouched. You are looking for indicators, not production-ready pipelines.* | |
| :---- | :---- |
| Pass | `add_documents` genuinely loads the case studies, chunks, embeds and stores them (the fixed-text stub is gone). `SimpleChunker` handles size and overlap correctly, including edge cases. Chunking is deliberate with a rationale. The pipeline produces the required output. Any changes to provided defaults (prompt, temperature, top_k) are sensible. |
| Pass With Concern | The fixed-text stub left in `add_documents`. Chunking that drops text, produces empty chunks, or mishandles overlap. Unneeded dependencies. GenAI-assisted code is fine as long as the candidate applies their own judgement on top. Unused or commented-out code. Poor error handling in code the candidate added. |

### Nice to see (not required to pass)
- Text preprocessing/cleaning of extracted source data (e.g. from PDFs).
- Re-ranking (cross-encoder), hybrid search, or other retrieval quality improvements.
- Query transformation / rewriting on the original prompt.
- Deliberate temperature / generation parameter tuning with rationale.

## 2. Evaluation & Testing

| *We expect systematic evaluation of a non-deterministic system, not just unit tests. If there is no evaluation of RAG quality at all, that is a fail.* | |
| :---- | :---- |
| Pass | RAG output quality is evaluated systematically with appropriate metrics (e.g. faithfulness, answer relevance, context precision). Results are validated and there is evidence of iteration based on the evaluation. Software tests exist and are independent (can run in isolation). Adequate assertions. The non-deterministic nature of LLM outputs is acknowledged in how things are tested. |
| Pass With Concern | Only generic off-the-shelf metrics with no thought about whether they fit the problem. Evaluation present but no evidence it drove any iteration. Extraneous setup. Poor test naming. Unclear tests. Incomplete assertions. Brittle tests that assert on exact LLM output. Dependency on a "live" endpoint is not in itself a warning. |

### Nice to see (not required to pass)
- Evaluation metrics tailored to the domain rather than only generic ones.
- A held-out / curated evaluation dataset (question–answer or question–context pairs).
- Load testing or robustness testing against the third-party API.

## 3. Design & Engineering Practices

| *The problem covers a small scope; solution complexity should reflect this. Standard EE engineering practices apply.* | |
| :---- | :---- |
| Pass | Minimal viable structure. Clear separation of pipeline stages. Good code organisation and modularity. Sensible configuration management (no hard-coded secrets or magic values scattered through the code). Appropriate dependency management. |
| Pass With Concern | Overly coupled components. Over-engineered for the scope. Large file count for a small problem. Secrets/keys committed. Configuration baked into code. Pipeline stages tangled together so they cannot be evaluated or swapped independently. |

### Not required to pass
- Updating the README with assumptions etc.
