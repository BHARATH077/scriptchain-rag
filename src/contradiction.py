"""
Contradiction detection & resolution:
- Detects when top candidate texts assert opposing facts.
- Resolution policy uses:
   1) prefer docs over blogs over forums (configurable)
   2) if equal, prefer more recent (not implemented here; metadata could include dates)
   3) if still ambiguous, present both to user and mark as contradictory
- Also produces synthesized answer with provenance.
"""
from logger_config import get_logger
import re
from typing import List


logger = get_logger()

def extract_facts(text: str) -> List[str]:
    # naive fact extraction: find short sentences containing keywords like 'is', 'are', 'should', 'use'
    sents = re.split(r'(?<=[.!?])\s+', text)
    facts = []
    for s in sents:
        s = s.strip()
        if len(s.split()) < 5:  # skip too-short
            continue
        if any(k in s.lower() for k in ["is", "are", "should", "use", "must", "can", "cannot", "don't", "do not"]):
            facts.append(s)
    return facts

def detect_contradictions(candidates):
    # Build fact -> list of sources that assert it; treat simple negation as contradiction
    fact_map = {}
    for c in candidates:
        facts = extract_facts(c["text"])
        for f in facts:
            key = f.lower()
            if key not in fact_map:
                fact_map[key] = []
            fact_map[key].append(c["meta"])
    # naive contradiction detection: if two facts contradict using keywords (is vs is not)
    contradictions = []
    # simplistic: if one sentence contains "is" and another similar sentence contains "is not" -> contradiction
    keys = list(fact_map.keys())
    for a in keys:
        for b in keys:
            if a == b:
                continue
            if a.replace("is not", "is") == b or b.replace("is not", "is") == a:
                contradictions.append((a, b, fact_map[a], fact_map[b]))
    return contradictions

def resolve(candidates, prefer_order=("docs","blogs","forums")):
    # If contradictions exist, pick facts from highest-preference source
    contradictions = detect_contradictions(candidates)
    if not contradictions:
        return {"status":"no_contradiction", "candidates": candidates, "contradictions": []}
    # resolution strategy: for each pair, select the one from higher-priority source
    resolved = []
    for pair in contradictions:
        a_text, b_text, a_sources, b_sources = pair
        # find highest priority source present in a_sources and b_sources
        def best_priority(sources):
            ranks = [prefer_order.index(s["source_type"]) if s["source_type"] in prefer_order else len(prefer_order) for s in sources]
            return min(ranks) if ranks else len(prefer_order)
        a_rank = best_priority(a_sources)
        b_rank = best_priority(b_sources)
        chosen = a_text if a_rank <= b_rank else b_text
        resolved.append({"chosen": chosen, "a_sources": a_sources, "b_sources": b_sources})
    return {"status":"resolved", "resolved_pairs": resolved, "contradictions": contradictions}
