# Gen AI Engineer — Interview Question Crib Sheet

Interviewer-facing question set for each phase, with what a strong (senior-level) candidate should give you. Walkthrough questions are grounded in the take-home exercise (Ollama/Milvus baseline, `SimpleChunker`/`AdvancedChunker`, `add_documents`, evaluation).

---

## Phase 1 — Exercise Walkthrough (25 min)

Open-ended start: *"Walk me through your solution as if I'm another Gen AI engineer — focus on the decisions you made and why."* Then probe.

### Chunking
- **"Why that chunk size and overlap? How did you arrive at them?"**
  Expect: a reason tied to the case-study text length and retrieval quality — not "the default looked fine". Should know overlap preserves context across boundaries.
- **"What does your `AdvancedChunker` do differently, and why is it better here?"**
  Expect: a genuine strategy (sentence/paragraph/semantic boundaries, structure-aware) with a rationale — and ideally evidence it beat `SimpleChunker` in their evaluation. If they didn't reach it: *"How would you have approached it?"*
- **"What are the trade-offs between the two strategies?"** (a README question)
  Expect: fixed-size is simple/fast but cuts mid-sentence; semantic gives better context but is more complex/slower. A senior names the cost, not just the benefit.

### Retrieval & generation
- **"How did you choose top-k? Did you change it?"**
  Expect: awareness that too low misses context, too high dilutes the prompt / adds noise.
- **"Did you touch the prompt or temperature? Why / why not?"**
  Expect: recognition that the base prompt already constrains to context; a strong candidate improved it or lowered temperature for factual Q&A and can justify it. "Didn't touch it" is acceptable *if* reasoned.
- **"Any cleaning or preprocessing of the case-study data before chunking?"** (Bonus — not mandatory.)

### Evaluation (the differentiator)
- **"How did you evaluate the pipeline? Which metrics and tool?"**
  Expect: a real harness (ragas/deepeval or hand-rolled) with faithfulness / answer-relevance / context-precision — and ideally something less generic, tailored to factual recall over case studies.
- **"How did you validate the results, and did the evaluation change anything you did?"**
  Expect: a before/after comparison of Simple vs Advanced chunker that actually drove a decision. An evaluation that was built but never informed a change is weak.
- **"What's your testing approach, and what's covered?"**
  Expect: their own tests for the chunkers and `add_documents`; awareness that the provided mock-only pipeline test doesn't prove their code works. Should mention how they test a non-deterministic system.

### Forward-looking (the four scaling questions — where senior shows)
- **"How would you evaluate RAG quality systematically, at scale?"**
  Expect: golden datasets, LLM-as-judge with caveats, offline + online eval, regression suites, human-in-the-loop sampling.
- **"What changes to handle 10M+ documents with real-time updates?"**
  Expect: a production vector DB (not local Milvus file), batched/streaming ingestion, incremental indexing, ANN trade-offs, metadata filtering, sharding, embedding cost/latency. Watch they move off the toy setup.
- **"How would you prevent hallucination and ensure factual accuracy?"**
  Expect: grounding/citation enforcement, "I don't know" behaviour, retrieval-quality focus (most hallucination is bad retrieval), faithfulness checks, reranking, guardrails.
- **"What monitoring would you put in production?"**
  Expect: latency/cost/token tracking, retrieval hit quality, answer-quality drift, feedback capture, tracing (LangSmith/Langfuse/OTel), alerting.

---

## Phase 2 — Experience Deep Dive (20 min)

*"Walk me through a Gen AI project you're proud of or found challenging."* Then explore four angles:

- **Problem definition** — *"Why was Gen AI the right tool versus a simpler/cheaper alternative?"*
  Expect: pragmatism. Red flag: AI-for-AI's-sake, couldn't articulate the genuine need.
- **Technical depth** — *"Model selection and hosting? RAG vs fine-tuning vs both — why? Where did the model fail and how did you handle it?"* Touch on **agentic architectures, observability, cost tracking.**
  Expect: opinionated, experience-backed reasoning; honest about failure modes, not just the happy path.
- **Stakeholder management** — *"How did you set realistic expectations about what AI could do? How did you handle a request for something it couldn't reliably deliver?"*
  Expect: concrete examples of managing hype and saying no with alternatives.
- **Trade-offs & outcomes** — *"How did you measure success? What would you do differently?"*
  Expect: a metric and genuine reflection — not "it went great".

---

## Phase 3 — Getting to Know Us (5–10 min)

Their questions about EE. Strong candidates ask about delivery model, client engagement, and how EE approaches Gen AI pragmatically.

---

## Cross-cutting signals

**Green flags:** justifies decisions with trade-offs not preferences; evaluation drove iteration; moves off the toy setup when asked about scale; honest about what they didn't finish; treats hallucination as a retrieval problem.

**Red flags:** accepted all defaults with no rationale; "the evaluation was just to show I can"; can't explain a chunk-size choice; over-engineered against the "keep it simple" brief; production answers stay at the demo level; AI-for-AI's-sake in their experience.
