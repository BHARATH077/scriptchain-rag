# ScriptChain Health — RAG System Take-Home Assignment

**Author:** Bharath A.  

This repository contains a **Retrieval-Augmented Generation (RAG) system** for answering customer questions about a fictional software product called **ScriptChain**. The system retrieves information from multiple knowledge sources: product documentation, customer forums, and technical blog posts.  

---

## Project Overview

The RAG system consists of:

1. **Data sources**
   - **Docs:** structured product documentation (markdown)
   - **Forums:** customer discussion threads (txt)
   - **Blogs:** narrative technical posts (markdown)

2. **Chunking**
   - Docs: section-aware paragraphs
   - Forums: individual posts/comments
   - Blogs: paragraph-level chunks

3. **Embedding & Retrieval**
   - `sentence-transformers` embeddings (`all-MiniLM-L6-v2`)
   - FAISS vector store
   - Source weighting: docs=1.0, blogs=0.9, forums=0.6

4. **Reranking**
   - Lexical BM25-like reranker by default
   - Supports transformer cross-encoder plug-in

5. **Contradiction Detection & Resolution**
   - Detects conflicting facts across sources
   - Resolves based on source preference: docs > blogs > forums
   - Returns resolved answer with provenance

6. **Logging**
   - Each query logs the top sources used to `logs/usage_log.jsonl`

---

## Setup & Installation

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/scriptchain-rag.git
cd scriptchain-rag.
```

2. Create a virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate      # macOS / Linux
# Windows PowerShell: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Build the Index

```bash
python src/app.py --build --data_dir data --index_dir index
```
- Generates sample documentation, forums, and blogs in 'data/'
- Chunks and embeds each document
- Builds FAISS index in 'index/'

## Run Interactive Queries

```bash
python src/app.py --index_dir index --interactive
```

- Type a query and see:
   - Top retrieved chunks with source metadata
   - Reranked final results
   - Contradiction check & resolution
   - Logging to 'logs/usage_log.jsonl'
- Exit by typing 'exit' or 'quit'.

## Example Queries

1. Query: "How do I authenticate requests to ScriptChain?"
2. Query: "What endpoint runs a script?"
3. Query: "I'm getting 429 errors; how to handle rate limits?"
4. Query: "Should I use Authorization: Bearer or X-API-Key?"
5. Query: "How to deploy ScriptChain at scale?"
6. Query: "How to store API keys securely?"
7. Query: "What endpoints provide job status?"
8. Query: "Is there role-based access control?"
9. Query: "Does ScriptChain support webhooks?"
10. Query: "How frequently should I rotate API keys?"
11. Query: "Are retries automatic or should I implement them?"
12. Query: "Any tips on avoiding 429 bursts for batch jobs?"
Notes: For each query, the system shows:
- Top 3 provenance items (source_type & filename)
- Any contradictions detected and resolved

## Performance Analysis

Metrics you can evaluate:

- **Recall@k** — fraction of queries with correct answer in top-k
- **Mean Reciprocal Rank (MRR)** — average rank of first correct answer
- **NDCG** — normalized discounted cumulative gain for reranking
- **Contradiction detection precision/recall**

**Suggested approach:**

1. Create a small test set of 50–100 Q/A pairs.  
2. Compare retrieved chunks vs ground-truth answers.  
3. Measure Recall@1, Recall@5, Recall@10 and MRR.  
4. Evaluate reranker effectiveness using NDCG@5.  
5. Track contradiction resolution accuracy.  

---

## Future Improvements

- Plug in a **cross-encoder reranker** for higher accuracy  
- Use **NLI models** for robust contradiction detection  
- Add **temporal metadata** to improve source resolution  
- Expand data sources and handle **multilingual content**  

---

## Logs

Queries are logged to `logs/usage_log.jsonl`:

- `query`  
- `top_sources` (source_type, source_id, position)  

Useful for auditing and debugging.

---

## Submission Instructions

1. Push your code to a GitHub repo named `scriptchain-rag`.  
2. Include all files under `src/`, `report/`, `examples/`, `requirements.txt`.  
3. Record a **≤5 minute presentation**:  
   - Show architecture diagram and system flow  
   - Demonstrate 2–3 queries in interactive mode  
   - Highlight contradiction resolution & provenance logging  
4. Provide GitHub link and attach presentation video (or provide shareable link).  

---

## References

- [Sentence-Transformers](https://www.sbert.net/)  
- [FAISS](https://github.com/facebookresearch/faiss)  
- Python libraries: `numpy`, `pandas`, `scikit-learn`, `transformers`, `tqdm`

