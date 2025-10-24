"""
Reranker scaffold:
- For small demo, we provide a lexical-scoring fallback and a place to plug a transformer cross-encoder.
- If you have a cross-encoder model, replace lexical_score with cross_encoder.predict([ (query, doc) ])
"""
from typing import List, Dict
from math import log
from logger_config import get_logger
from sentence_transformers import CrossEncoder
cross_encoder = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")


logger = get_logger()

def lexical_score(query: str, doc: str) -> float:
    # simple BM25-like heuristics using term frequency
    q_terms = [t.lower() for t in query.split()]
    d_terms = [t.lower() for t in doc.split()]
    score = 0.0
    for qt in q_terms:
        cnt = d_terms.count(qt)
        if cnt:
            score += log(1 + cnt)
    # length penalty
    score = score / (1 + len(d_terms)/200)
    return score

def rerank(query: str, candidates: list, cross_encoder_model=None, use_lexical=True, alpha=0.4, beta=0.6) -> list:
    """
    Rerank candidates combining:
      - weighted embedding score (from retrieval)
      - optional lexical score
      - optional cross-encoder score

    Parameters:
    - alpha: weight for embedding + lexical
    - beta: weight for cross-encoder
    """
    # Step 1: compute lexical scores if enabled
    if use_lexical:
        for c in candidates:
            c["lexical_score"] = lexical_score(query, c["text"])
    else:
        for c in candidates:
            c["lexical_score"] = 0.0

    # Step 2: compute cross-encoder scores if provided
    if cross_encoder_model:
        pairs = [(query, c["text"]) for c in candidates]
        scores = cross_encoder_model.predict(pairs)
        for c, s in zip(candidates, scores):
            c["cross_score"] = float(s)
    else:
        for c in candidates:
            c["cross_score"] = 0.0

    # Step 3: combine scores
    for c in candidates:
        # formula: final_score = alpha*(weighted_score + lexical) + beta*(cross)
        final = alpha * (c.get("weighted_score", 0.0) + c.get("lexical_score",0.0)) \
                + beta * c.get("cross_score", 0.0)
        c["final_score"] = final

    return sorted(candidates, key=lambda x: x["final_score"], reverse=True)

