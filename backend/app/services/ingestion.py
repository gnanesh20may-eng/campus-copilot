import re
from pathlib import Path
from typing import List

from pypdf import PdfReader

from app.db.vector_store import add_documents, persist

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50


def extract_text_from_pdf(file_path: Path) -> str:
    reader = PdfReader(str(file_path))
    pages = []
    for page in reader.pages:
        text = page.extract_text() or ""
        pages.append(text)
    return "\n\n".join(pages).strip()


def chunk_text(text: str, chunk_size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> List[str]:
    cleaned = re.sub(r"\s+", " ", text).strip()
    if not cleaned:
        return []

    words = cleaned.split(" ")
    chunks = []
    start = 0
    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        if end == len(words):
            break
        start += chunk_size - overlap
    return chunks


def ingest_pdf(file_path: Path, filename: str) -> int:
    text = extract_text_from_pdf(file_path)
    if not text:
        return 0
    chunks = chunk_text(text)
    ids = [f"{filename}-{i}" for i in range(len(chunks))]
    metadatas = [
        {"source": filename, "chunk_index": i}
        for i in range(len(chunks))
    ]
    add_documents(chunks, metadatas, ids)
    persist()
    return len(chunks)
