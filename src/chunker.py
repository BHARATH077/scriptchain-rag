"""
Chunking strategies:
- Documentation: larger, structure-aware chunks (use section headings)
- Forums: smaller chunks per post/comment (preserve speaker lines)
- Blogs: medium chunks per paragraph, keep paragraphs together

Each chunk will have metadata:
- source_type: docs|forums|blogs
- source_id: filename
- position: index in document
"""
import re
from pathlib import Path
from typing import List, Dict

def chunk_document(text: str, max_tokens: int = 250) -> List[str]:
    # naive paragraph split; real implementation could use token counts
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks = []
    for p in paragraphs:
        if len(p) <= max_tokens:
            chunks.append(p)
        else:
            # split long paragraphs by sentences
            sents = re.split(r'(?<=[.!?])\s+', p)
            cur = []
            for s in sents:
                if sum(len(x) for x in cur) + len(s) < max_tokens:
                    cur.append(s)
                else:
                    chunks.append(" ".join(cur))
                    cur = [s]
            if cur:
                chunks.append(" ".join(cur))
    return chunks

def chunk_forum(text: str) -> List[str]:
    # split by speaker lines
    posts = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        posts.append(line)
    return posts

def chunk_blog(text: str, max_chars: int = 500) -> List[str]:
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks = []
    for p in paragraphs:
        if len(p) <= max_chars:
            chunks.append(p)
        else:
            # naive split by sentences
            sents = re.split(r'(?<=[.!?])\s+', p)
            cur = ""
            for s in sents:
                if len(cur) + len(s) < max_chars:
                    cur = (cur + " " + s).strip()
                else:
                    if cur:
                        chunks.append(cur.strip())
                    cur = s
            if cur:
                chunks.append(cur.strip())
    return chunks

def chunk_file(path: Path, source_type: str):
    text = path.read_text()
    if source_type == "docs":
        c = chunk_document(text)
    elif source_type == "forums":
        c = chunk_forum(text)
    elif source_type == "blogs":
        c = chunk_blog(text)
    else:
        raise ValueError(source_type)
    # attach metadata
    chunks = []
    for i, ch in enumerate(c):
        chunks.append({
            "text": ch,
            "source_type": source_type,
            "source_id": path.name,
            "position": i
        })
    return chunks
