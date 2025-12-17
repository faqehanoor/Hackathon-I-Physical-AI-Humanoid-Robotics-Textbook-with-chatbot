from pydantic import BaseModel
from typing import Optional, List
from src.schemas.book import BookBase, BookResponse


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