from pathlib import Path
from typing import List, Optional

import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions

from app.services.embeddings import embed_texts

DB_DIR = Path(__file__).resolve().parent.parent.parent / "data" / "chroma_db"
DB_DIR.mkdir(parents=True, exist_ok=True)

client = chromadb.Client(Settings(chromadb_db_impl="duckdb+parquet", persist_directory=str(DB_DIR)))
collection = client.get_or_create_collection(
    name="campus_documents",
    metadata={"description": "Ingested PDF chunks for Campus Copilot"},
    embedding_function=embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2"),
)


def add_documents(texts: List[str], metadatas: List[dict], ids: List[str]):
    return collection.add(documents=texts, metadatas=metadatas, ids=ids)


def query_documents(query: str, n_results: int = 4) -> List[dict]:
    query_embedding = embed_texts([query])[0]
    results = collection.query(query_embeddings=[query_embedding], n_results=n_results)
    docs = []
    if results and results["documents"]:
        for text, meta in zip(results["documents"][0], results["metadatas"][0]):
            docs.append({"text": text, "metadata": meta})
    return docs


def persist():
    client.persist()
