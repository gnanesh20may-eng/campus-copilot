from typing import List, Optional

from pydantic import BaseModel


class UploadResponse(BaseModel):
    filename: str
    chunks_added: int


class ChatRequest(BaseModel):
    query: str
    department: Optional[str] = None
    subgroup: Optional[str] = None


class ChatResponse(BaseModel):
    answer: str
    sources: List[str]
