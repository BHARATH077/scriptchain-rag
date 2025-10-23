"""
Glue everything together:
- Prepare data
- Build index
- Run queries and show:
  - retrieval results with source metadata
  - reranked top results
  - contradiction detection/resolution
  - logging of sources used
"""
import argparse
from pathlib import Path
from data_prep import write_example_files
from chunker import chunk_file
from embedder_retriever import Retriever
from reranker import rerank
from contradiction import resolve
from logger_config import get_logger
import glob
import json

logger = get_logger()

def build_index(data_dir: str, index_dir: str):
    write_example_files(base_dir=data_dir)
    chunks = []
    for src_type in ["docs", "forums", "blogs"]:
        for p in Path(data_dir, src_type).glob("*"):
            ch = chunk_file(p, src_type)
            chunks.extend(ch)
    retriever = Retriever()
    retriever.build(chunks)
    Path(index_dir).mkdir(parents=True, exist_ok=True)
    retriever.save(Path(index_dir))
    logger.info("Build complete.")
    return retriever

def load_index(index_dir: str):
    r = Retriever()
    r.load(Path(index_dir))
    return r

def interactive_query(retriever):
    print("Enter query (or 'exit'):")
    while True:
        q = input(">> ").strip()
        if q in ("exit","quit"):
            break
        # Retrieve
        candidates = retriever.retrieve(q, top_k=10)
        logger.info("Top retrievals (weighted):")
        for c in candidates[:5]:
            logger.info(f"{c['meta']['source_type']} | {c['meta']['source_id']} | score {c['weighted_score']:.4f}")
        # Rerank
        reranked = rerank(q, candidates)
        logger.info("Top reranked:")
        for c in reranked[:5]:
            print(f"[{c['meta']['source_type']}] ({c['meta']['source_id']}) final_score={c['final_score']:.4f}")
            print(c['text'])
            print("-"*40)
        # contradiction
        res = resolve(reranked[:6])
        print("Contradiction check:", res["status"])
        if res["status"] != "no_contradiction":
            print("Resolved pairs:")
            for rp in res.get("resolved_pairs", []):
                print("Chosen:", rp["chosen"])
        # Logging: write usage record
        usage = {
            "query": q,
            "top_sources": [c['meta'] for c in reranked[:5]]
        }
        Path("logs").mkdir(exist_ok=True)
        with open("logs/usage_log.jsonl", "a") as f:
            f.write(json.dumps(usage) + "\n")
        print("Logged query. Next.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dir", default="../data")
    parser.add_argument("--index_dir", default="../index")
    parser.add_argument("--build", action="store_true")
    parser.add_argument("--interactive", action="store_true")
    args = parser.parse_args()
    if args.build:
        retriever = build_index(args.data_dir, args.index_dir)
    else:
        retriever = load_index(args.index_dir)
    if args.interactive:
        interactive_query(retriever)
