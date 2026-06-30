"""Retrieval smoke test for a Gen AI THT submission.

Copy this into the candidate's repo root and run:

    PYTHONPATH=. poetry run python retrieval_probe.py

It ingests the case studies with the candidate's own chunker, embeds with the
provided Ollama client, and ranks chunks for the brief's canonical questions
under BOTH inner-product (IP) and cosine — so you can see, independently of the
generation step, whether retrieval surfaces the relevant content.

What to look at:
- Embedding norm: if it is far from ~1.0, then IP != cosine. A submission that
  searches with metric_type="IP" over these un-normalised vectors is ranking by
  magnitude, not meaning — the classic silent retrieval failure.
- For each question it prints the top chunks under each metric and the rank of
  the first chunk that mentions the target entity. If the relevant content is
  not in the top-k (the candidate's top_k), retrieval has failed regardless of
  how clean the code looks.

Adjust the import or constructor below if the candidate named their chunker
differently. Falls back from AdvancedChunker to SimpleChunker automatically.
"""

import json
import math
from typing import List

from src.llm.ollama import OllamaLLM

try:
    from src.chunking.chunking_strategies import AdvancedChunker as Chunker
except Exception:  # pragma: no cover - submission variance
    from src.chunking.chunking_strategies import SimpleChunker as Chunker

# The scaffold ships exactly two canonical questions (read the README / baseline
# main.py to confirm — a candidate may have changed them). HMRC is NOT a scaffold
# question; it is included as a named-entity stress test because that case study
# is in the corpus and proper-noun retrieval is the common failure mode.
CANONICAL = {
    "IG Group": "What work did Equal Experts do for IG group?",  # scaffold
    "Forrester": "What was demonstrated in the Forrester study?",  # scaffold
    "HMRC": "How did Equal Experts help HMRC?",  # entity stress test (not scaffold)
}
TOP_N_PREVIEW = 5


def _dot(a: List[float], b: List[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def _norm(a: List[float]) -> float:
    return math.sqrt(_dot(a, a)) or 1e-9


def main() -> None:
    docs = [d["content"] for d in json.load(open("case_studies.json"))]
    chunker = Chunker()
    llm = OllamaLLM()

    chunks: List[str] = []
    for doc in docs:
        chunks.extend(chunker.chunk_text(doc))
    print(f"{len(chunks)} chunks from {len(docs)} documents using {type(chunker).__name__}")

    embeddings = [llm.get_embeddings(c) for c in chunks]
    norms = [_norm(e) for e in embeddings]
    print(f"embedding norm sample: {norms[0]:.2f}  (IP == cosine only if ~1.0)\n")

    for entity, question in CANONICAL.items():
        qe = llm.get_embeddings(question)
        qn = _norm(qe)
        ip = [_dot(qe, e) for e in embeddings]
        cos = [_dot(qe, e) / (qn * n) for e, n in zip(embeddings, norms)]
        ip_rank = sorted(range(len(chunks)), key=lambda i: ip[i], reverse=True)
        cos_rank = sorted(range(len(chunks)), key=lambda i: cos[i], reverse=True)

        def first_hit(rank: List[int]) -> object:
            for pos, i in enumerate(rank, 1):
                if entity.lower() in chunks[i].lower():
                    return pos
            return None

        print(f"=== {entity} ===")
        print(f"  first chunk mentioning '{entity}':  IP rank={first_hit(ip_rank)}  COSINE rank={first_hit(cos_rank)}")
        print("  top chunks (IP):")
        for pos, i in enumerate(ip_rank[:TOP_N_PREVIEW], 1):
            print(f"    [{pos}] {' '.join(chunks[i].split())[:110]!r}")
        print()

    llm.close()


if __name__ == "__main__":
    main()
