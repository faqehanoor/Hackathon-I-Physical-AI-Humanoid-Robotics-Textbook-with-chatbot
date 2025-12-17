# Data Model: Embeddings Pipeline

## Overview

This document describes the data structures and entities used in the embeddings pipeline system that extracts text from Docusaurus URLs, generates embeddings using Cohere, and stores them in Qdrant for RAG-based retrieval.

## Entities

### 1. Document Chunk

Represents a segment of text extracted from a Docusaurus page, including content, source URL, and metadata

```python
class DocumentChunk:
    id: str                    # Unique identifier for the chunk
    content: str              # Text content of the chunk
    source_url: str           # Original URL from which text was extracted
    title: str                # Title of the page (if available)
    created_at: datetime      # Timestamp when chunk was created
    metadata: Dict[str, Any]  # Additional metadata (section, hierarchy, etc.)
```

**Validation rules**:
- content must be non-empty
- source_url must be a valid URL
- id must be unique within the system

**Relationships**:
- Belongs to one source page
- Associated with one embedding vector

### 2. Embedding

High-dimensional vector representation of text content, associated with its source document chunk

```python
class Embedding:
    id: str                  # Same as the document chunk id
    vector: List[float]      # The actual embedding vector (typically 1024 floats)
    model: str              # Model used to generate the embedding
    created_at: datetime    # Timestamp when embedding was generated
    chunk_id: str           # Reference to the source document chunk
```

**Validation rules**:
- vector must match expected dimensions (e.g., 1024 for Cohere models)
- chunk_id must reference an existing document chunk
- model must be a valid Cohere model identifier

**Relationships**:
- Associated with one document chunk
- Stored in Qdrant collection

### 3. Crawl Session

Record of a website crawling operation, tracking which pages were processed and any errors encountered

```python
class CrawlSession:
    id: str                    # Unique identifier for the crawl session
    start_url: str            # Initial URL that started the crawl
    status: str               # Status (e.g., "in_progress", "completed", "failed")
    started_at: datetime      # When crawling started
    completed_at: datetime    # When crawling completed (if finished)
    pages_processed: int      # Number of pages successfully processed
    errors_count: int         # Number of errors encountered
    processed_urls: List[str] # List of URLs that were successfully processed
    error_details: List[Dict[str, Any]]  # Details about any errors
```

**Validation rules**:
- start_url must be a valid URL
- status must be one of the allowed values
- completed_at must be after started_at when set

**Relationships**:
- Contains multiple document chunks
- Generates multiple embeddings

### 4. Vector Index

Organized structure in Qdrant that enables fast similarity search of stored embeddings

```python
class VectorIndex:
    name: str                    # Name of the Qdrant collection (e.g., "chatbot-embeddings")
    size: int                   # Number of vectors in the collection
    vector_dimension: int       # Dimension of vectors in the collection
    created_at: datetime        # When the collection was created
    updated_at: datetime        # When the collection was last updated
    metadata_schema: Dict[str, Any]  # Schema for metadata fields
```

**Validation rules**:
- name must follow Qdrant naming conventions
- vector_dimension must match the embedding model used
- size must be non-negative

**Relationships**:
- Contains multiple embeddings

## State Transitions

### Document Chunk States
- `created`: Chunk extracted from source document
- `embedding`: Currently being processed for embedding
- `embedded`: Successfully embedded and ready for storage
- `stored`: Saved in vector database
- `failed`: Could not be processed after retries

### Crawl Session States
- `initialized`: Crawl session created, ready to start
- `in_progress`: Crawling is currently happening
- `completed`: All pages processed successfully
- `failed`: Crawl terminated due to errors
- `interrupted`: Crawl stopped before completion

## Relationships Summary

```
CrawlSession (1) -> DocumentChunk (Many)
DocumentChunk (1) -> Embedding (1)
Embedding (Many) -> VectorIndex (1)
```

## Data Flow

1. CrawlSession initiates the crawling process
2. Multiple DocumentChunks are created from the crawled pages
3. Each DocumentChunk gets converted to an Embedding
4. Embeddings are stored in a VectorIndex for retrieval