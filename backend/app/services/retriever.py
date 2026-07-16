from typing import List

from app.db.vector_store import query_documents


def retrieve_context(query: str, top_k: int = 4) -> List[dict]:
    return query_documents(query, n_results=top_k)
