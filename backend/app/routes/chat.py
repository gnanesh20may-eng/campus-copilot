from fastapi import APIRouter, HTTPException

from app.models.schemas import ChatRequest, ChatResponse
from app.services.llm import query_llm
from app.services.retriever import retrieve_context

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest):
    if not request.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty.")

    context_docs = retrieve_context(request.query, top_k=4)
    if not context_docs:
        return {"answer": "I don't know.", "sources": []}

    answer = query_llm(
        request.query,
        context_docs,
        department=request.department,
        subgroup=request.subgroup,
    )
    sources = []
    for doc in context_docs:
        source = doc["metadata"].get("source")
        if source and source not in sources:
            sources.append(source)

    return {"answer": answer, "sources": sources}
