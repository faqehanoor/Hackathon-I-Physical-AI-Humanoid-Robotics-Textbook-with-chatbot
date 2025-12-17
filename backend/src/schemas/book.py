from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime
from uuid import UUID


class BookBase(BaseModel):
    title: str
    author: str
    content: Optional[str] = None
    summary: Optional[str] = None
    metadata_json: Optional[str] = None


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    content: Optional[str] = None
    summary: Optional[str] = None
    metadata_json: Optional[str] = None


class BookResponse(BookBase):
    id: UUID
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class AISummarizeRequest(BaseModel):
    text: str
    model: Optional[str] = "summarize-xlarge"
    length: Optional[str] = "medium"
    format: Optional[str] = "paragraph"
    extractiveness: Optional[str] = "medium"
    temperature: Optional[float] = 0.3


class AISummarizeResponse(BaseModel):
    summary: str


class AIEmbeddingRequest(BaseModel):
    texts: List[str]
    model: Optional[str] = "embed-english-v3.0"
    input_type: Optional[str] = "search_document"


class AIEmbeddingResponse(BaseModel):
    embeddings: List[List[float]]