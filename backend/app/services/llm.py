import os
from anthropic import Anthropic, HUMAN_PROMPT


from typing import Optional

import os
from anthropic import Anthropic, HUMAN_PROMPT


def build_prompt(query: str, context_docs: list[dict], department: Optional[str] = None, subgroup: Optional[str] = None) -> str:
    instructions = (
        "You are a helpful assistant for a Campus Copilot app. Answer only using the provided context. "
        "If the answer cannot be found in the context, say 'I don't know.' "
        "Cite sources using the source filename and chunk index from the context. "
        "Do not invent new facts."
    )

    if department or subgroup:
        instructions += " Use the selected department and subgroup to frame your answer when appropriate. "

    context_text = []
    for index, doc in enumerate(context_docs, start=1):
        source = doc["metadata"].get("source", "unknown")
        chunk_index = doc["metadata"].get("chunk_index", "?")
        snippet = doc["text"].strip().replace("\n", " ")
        context_text.append(
            f"[{index}] {source} (chunk {chunk_index}): {snippet}"
        )

    combined_context = "\n\n".join(context_text) if context_text else "No relevant context was found."

    department_note = f"Department: {department}\n" if department else ""
    subgroup_note = f"Subgroup: {subgroup}\n" if subgroup else ""

    return (
        f"{HUMAN_PROMPT}\n{instructions}\n\n"
        f"{department_note}{subgroup_note}"
        f"Context:\n{combined_context}\n\n"
        f"Question: {query}\n\nAnswer:"
    )


def query_llm(query: str, context_docs: list[dict], department: Optional[str] = None, subgroup: Optional[str] = None) -> str:
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("Missing ANTHROPIC_API_KEY")

    client = Anthropic(api_key=api_key)
    prompt = build_prompt(query, context_docs, department=department, subgroup=subgroup)
    response = client.completions.create(
        model="claude-sonnet-4-6",
        prompt=prompt,
        max_tokens_to_sample=700,
        temperature=0.0,
    )
    return response.completion.strip()
