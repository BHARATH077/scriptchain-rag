"""
Embedding + FAISS retrieval with source weighting.
- Uses sentence-transformers for embeddings
- Builds a single FAISS index with metadata stored separately
- Retrieval returns top-k per source then merged using weights
"""
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from typing import List, Dict, Tuple
from pathlib import Path
import pickle
from logger_config import get_logger

logger = get_logger()

class Retriever:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        logger.info("Loading embedder...")
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.id2meta = {}  # mapping from idx -> metadata
        self.embeddings = None

    def build(self, chunks: List[Dict], index_path: Path = None):
        texts = [c["text"] for c in chunks]
        logger.info(f"Embedding {len(texts)} chunks...")
        embs = self.model.encode(texts, convert_to_numpy=True, show_progress_bar=True)
        self.embeddings = embs.astype("float32")
        dim = self.embeddings.shape[1]
        self.index = faiss.IndexFlatIP(dim)  # inner product (after norm)
        faiss.normalize_L2(self.embeddings)
        self.index.add(self.embeddings)
        for i, c in enumerate(chunks):
            self.id2meta[i] = c
        logger.info("Index built.")

    def save(self, path: Path):
        np.save(path / "embeddings.npy", self.embeddings)
        with open(path / "meta.pkl", "wb") as f:
            pickle.dump(self.id2meta, f)
        faiss.write_index(self.index, str(path / "faiss.index"))
        logger.info("Saved index to disk.")

    def load(self, path: Path):
        self.embeddings = np.load(path / "embeddings.npy")
        with open(path / "meta.pkl", "rb") as f:
            self.id2meta = pickle.load(f)
        self.index = faiss.read_index(str(path / "faiss.index"))
        logger.info("Loaded index from disk.")

    def retrieve(self, query: str, top_k:int = 10, source_weights: Dict[str,float]=None) -> List[Dict]:
        """
        Strategy:
        1. Encode and normalize query
        2. Search top_k * N to get diverse candidates
        3. Score candidates and apply source_weights (source-level)
        4. Return merged sorted list
        """
        if source_weights is None:
            source_weights = {"docs": 1.0, "blogs": 0.9, "forums": 0.6}
        q_emb = self.model.encode([query], convert_to_numpy=True)
        q_emb = q_emb.astype("float32")
        faiss.normalize_L2(q_emb)
        # request a larger set to allow reranking/reresolution
        raw_k = min(200, self.index.ntotal) if self.index.ntotal>0 else top_k*5
        D, I = self.index.search(q_emb, raw_k)
        scored = []
        for score, idx in zip(D[0], I[0]):
            if idx < 0:
                continue
            meta = self.id2meta[idx]
            src = meta["source_type"]
            weight = source_weights.get(src, 0.5)
            combined_score = float(score) * weight
            scored.append({
                "idx": int(idx),
                "score": float(score),
                "weighted_score": combined_score,
                "text": meta["text"],
                "meta": meta
            })
        # sort by weighted_score
        scored = sorted(scored, key=lambda x: x["weighted_score"], reverse=True)
        return scored[:top_k]
