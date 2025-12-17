from fastapi import APIRouter
from typing import Dict, Any
import cohere
from qdrant_client import QdrantClient
import os
from dotenv import load_dotenv
from src.schemas.ai import AISummarizeRequest, AISummarizeResponse, AIEmbeddingRequest, AIEmbeddingResponse
from src.utils.exceptions import InvalidInputException

# Load environment variables
load_dotenv()

router = APIRouter()

# Initialize Cohere client
cohere_api_key = os.getenv("COHERE_API_KEY")
if cohere_api_key:
    cohere_client = cohere.Client(cohere_api_key)
else:
    cohere_client = None
    print("Warning: COHERE_API_KEY not set. AI features will be limited.")

# Initialize Qdrant client
qdrant_url = os.getenv("QDRANT_URL", "https://066dbcf1-8341-4072-b4ae-c664e0daaa89.europe-west3-0.gcp.cloud.qdrant.io")
qdrant_client = QdrantClient(url=qdrant_url)


@router.post("/summarize", response_model=AISummarizeResponse)
async def ai_summarize(request: AISummarizeRequest):
    """Generate AI-powered summary of content"""
    if not cohere_client:
        raise InvalidInputException("Cohere client not initialized. Check API key.")

    # Validate input
    if not request.text or len(request.text.strip()) == 0:
        raise InvalidInputException("Text to summarize cannot be empty")

    if len(request.text) > 100000:  # Limit to 100k characters
        raise InvalidInputException("Text too long for summarization. Maximum 100,000 characters allowed.")

    try:
        response = cohere_client.summarize(
            text=request.text,
            model=request.model if request.model else "summarize-xlarge",
            length=request.length if request.length else "medium",
            format=request.format if request.format else "paragraph",
            extractiveness=request.extractiveness if request.extractiveness else "medium",
            temperature=request.temperature if request.temperature else 0.3,
        )

        return AISummarizeResponse(summary=response.summary)
    except Exception as e:
        raise InvalidInputException(f"Error generating summary: {str(e)}")


@router.post("/embeddings", response_model=AIEmbeddingResponse)
async def get_embeddings(request: AIEmbeddingRequest):
    """Generate embeddings for text using Cohere"""
    if not cohere_client:
        raise InvalidInputException("Cohere client not initialized. Check API key.")

    # Validate input
    if not request.texts or len(request.texts) == 0:
        raise InvalidInputException("At least one text is required for embedding")

    if len(request.texts) > 96:  # Cohere's batch limit
        raise InvalidInputException("Too many texts provided. Maximum 96 texts allowed per request.")

    for i, text in enumerate(request.texts):
        if len(text) > 4096:  # Character limit per text
            raise InvalidInputException(f"Text at index {i} is too long. Maximum 4096 characters allowed per text.")

    try:
        response = cohere_client.embed(
            texts=request.texts,
            model=request.model if request.model else "embed-english-v3.0",
            input_type=request.input_type if request.input_type else "search_document"
        )

        return AIEmbeddingResponse(embeddings=response.embeddings)
    except Exception as e:
        raise InvalidInputException(f"Error generating embeddings: {str(e)}")


@router.post("/generate")
async def ai_generate(request: Dict[str, Any]):
    """General AI text generation"""
    if not cohere_client:
        raise InvalidInputException("Cohere client not initialized. Check API key.")

    # Validate input
    prompt = request.get("prompt", "")
    if not prompt or len(prompt.strip()) == 0:
        raise InvalidInputException("Prompt cannot be empty")

    max_tokens = request.get("max_tokens", 100)
    if max_tokens <= 0 or max_tokens > 4000:
        raise InvalidInputException("Max tokens must be between 1 and 4000")

    temperature = request.get("temperature", 0.7)
    if temperature < 0.0 or temperature > 5.0:
        raise InvalidInputException("Temperature must be between 0.0 and 5.0")

    try:
        # Extract parameters from the request
        model = request.get("model", "command-r-plus")

        response = cohere_client.generate(
            model=model,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature
        )

        return {"generated_text": response.generations[0].text}
    except Exception as e:
        raise InvalidInputException(f"Error generating text: {str(e)}")