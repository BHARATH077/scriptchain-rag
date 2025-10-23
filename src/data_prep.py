"""
Generate or load three different data sources:
- product documentation (docs/)
- customer forums (forums/)
- technical blog posts (blogs/)

This file creates small example documents so the pipeline is runnable.
"""
import os
from pathlib import Path
from typing import List
logger = None

def write_example_files(base_dir: str = "../data"):
    global logger
    from logger_config import get_logger
    logger = get_logger()
    base = Path(base_dir)
    docs = base / "docs"
    forums = base / "forums"
    blogs = base / "blogs"
    for d in [docs, forums, blogs]:
        d.mkdir(parents=True, exist_ok=True)

    # Product docs (structured, precise)
    docs_texts = {
        "getting_started.md": """# ScriptChain App - Getting Started
ScriptChain is a fictional product for securely connecting scripts to healthcare workflows.
Installation: pip install scriptchain
Auth: API key in header X-API-Key
Endpoints:
- /v1/run : runs a script
- /v1/status : job status (id)
Retries: exponential backoff, status 429 means rate-limited
""",
        "features.md": """# Features
- Secure sandboxing
- Versioned deployments
- Webhooks for events
- Role-based access control
""",
    }

    for fn, text in docs_texts.items():
        (docs / fn).write_text(text)
        logger.info(f"Wrote doc {fn}")

    # Forums (conversational; might have opinions / contradictions)
    forums_texts = {
        "thread_001.txt": """UserA: I tried scriptchain with API key but got 401. How do I fix?
UserB: Make sure the header is X-API-Key, and that your key has 'run' permission.
UserC: I think the header should be Authorization: Bearer <token>.
""",
        "thread_002.txt": """UserD: How to handle rate limits? I'm getting 429 frequently.
UserE: The docs say exponential backoff; I used 1s, 2s, 4s and it works.
UserF: Alternatively, you can set parallelism to 1 to avoid bursts.
""",
    }
    for fn, text in forums_texts.items():
        (forums / fn).write_text(text)
        logger.info(f"Wrote forum {fn}")

    # Blogs (narrative, may contain deeper tips)
    blogs_texts = {
        "deploying_at_scale.md": """# Deploying ScriptChain at Scale
When deploying in production, pin the runtime and use background workers to run long jobs.
Tip: use exponential backoff plus jitter to reduce synchronization.
""",
        "security_considerations.md": """# Security
Store API keys in environment variables; rotate them every 90 days.
For audit logging, enable request tracing.
""",
    }
    for fn, text in blogs_texts.items():
        (blogs / fn).write_text(text)
        logger.info(f"Wrote blog {fn}")

if __name__ == "__main__":
    write_example_files()
