# Embeddings Pipeline API Contract

This document describes the API endpoints for the embeddings pipeline that extracts text from Docusaurus URLs, generates embeddings using Cohere, and stores them in Qdrant for RAG-based retrieval.

## Endpoints

### 1. Process Docusaurus Site

**POST** `/process-site`

Start the process of extracting text from a Docusaurus site, generating embeddings, and storing in Qdrant.

#### Request

```json
{
  "url": "https://hackathon-i-physical-ai-humanoid-ro-cyan.vercel.app/",
  "collection_name": "chatbot-embeddings",
  "chunk_size": 512,
  "overlap": 50
}
```

#### Response

```json
{
  "session_id": "session-12345",
  "status": "processing",
  "pages_found": 15,
  "estimated_completion": "2025-12-16T10:30:00Z"
}
```

#### Error Response

```json
{
  "error": "invalid_url",
  "message": "The provided URL is not accessible or not a valid Docusaurus site"
}
```

### 2. Check Processing Status

**GET** `/status/{session_id}`

Check the status of a processing session.

#### Response

```json
{
  "session_id": "session-12345",
  "status": "completed",
  "pages_processed": 15,
  "chunks_created": 42,
  "embeddings_generated": 42,
  "start_time": "2025-12-16T10:00:00Z",
  "end_time": "2025-12-16T10:25:00Z",
  "errors": 0
}
```

### 3. Search in Vector Database

**POST** `/search`

Perform a semantic search in the vector database.

#### Request

```json
{
  "query": "How to set up the AI humanoid robot?",
  "collection_name": "chatbot-embeddings",
  "limit": 5
}
```

#### Response

```json
{
  "results": [
    {
      "id": "chunk-abc123",
      "score": 0.87,
      "content": "To set up the AI humanoid robot, first ensure all hardware components are properly connected...",
      "source_url": "https://hackathon-i-physical-ai-humanoid-ro-cyan.vercel.app/setup-guide",
      "title": "Setup Guide"
    }
  ]
}
```

### 4. List Collections

**GET** `/collections`

List all available vector collections in Qdrant.

#### Response

```json
[
  {
    "name": "chatbot-embeddings",
    "vectors_count": 1500,
    "indexed_vectors_count": 1500,
    "vector_dimension": 1024
  }
]
```

### 5. Delete Collection

**DELETE** `/collections/{collection_name}`

Delete a vector collection from Qdrant.

#### Response

```json
{
  "success": true,
  "message": "Collection 'chatbot-embeddings' deleted successfully"
}
```

## Authentication

All endpoints require an API key in the header:

```
Authorization: Bearer {API_KEY}
```

## Error Codes

- `200`: Success
- `400`: Bad request (invalid parameters)
- `401`: Unauthorized (invalid API key)
- `404`: Resource not found
- `500`: Internal server error
- `503`: Service unavailable (external API failure)