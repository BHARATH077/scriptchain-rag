"""
Reranker scaffold:
- For small demo, we provide a lexical-scoring fallback and a place to plug a transformer cross-encoder.
- If you have a cross-encoder model, replace lexical_score with cross_encoder.predict([ (query, doc) ])
"""
from typing import List, Dict
from math import log
from logger_config import get_logger

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

def rerank(query: str, candidates: List[Dict], cross_encoder=None) -> List[Dict]:
    """
    If cross_encoder is provided, it should accept list of (query, doc) pairs and return scores.
    Else use lexical_score as fallback.
    """
    if cross_encoder:
        pairs = [(query, c["text"]) for c in candidates]
        scores = cross_encoder.predict(pairs)  # placeholder API
        for c, s in zip(candidates, scores):
            c["rerank_score"] = float(s)
    else:
        for c in candidates:
            c["rerank_score"] = lexical_score(query, c["text"])
    # combine original weighted_score with rerank score
    for c in candidates:
        c["final_score"] = 0.4 * c.get("weighted_score", 0.0) + 0.6 * c["rerank_score"]
    return sorted(candidates, key=lambda x: x["final_score"], reverse=True)
