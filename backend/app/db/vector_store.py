from typing import List

import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions

from app.services.embeddings import embed_texts

# Use an ephemeral in-memory Chroma client for Render deployments.
# This avoids relying on a local persistent disk path that is not guaranteed
# on Render's free web service filesystem.
client = chromadb.Client(
    Settings(chroma_db_impl="duckdb+parquet", is_persistent=False)
)
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
    # No-op for in-memory mode; persistence is intentionally disabled on Render.
    return None
