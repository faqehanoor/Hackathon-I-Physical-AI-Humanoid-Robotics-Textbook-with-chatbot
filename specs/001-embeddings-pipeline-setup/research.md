# Research: Embeddings Pipeline Setup

## Overview

This research document covers the key technologies and implementation approaches for the embeddings pipeline that extracts text from Docusaurus URLs, generates embeddings using Cohere, and stores them in Qdrant for RAG-based retrieval.

## Technology Research

### 1. Cohere API for Embeddings

**Decision**: Use Cohere's embedding API
**Rationale**: Cohere provides high-quality embeddings with good semantic understanding, has a Python SDK, and is well-documented
**Alternatives considered**:
- OpenAI embeddings: More expensive, limited control over model
- Hugging Face transformers: Self-hosted, more complex setup but free
- Sentence Transformers: Open source, self-hosted option

### 2. Qdrant Vector Database

**Decision**: Use Qdrant for vector storage and retrieval
**Rationale**: Qdrant is designed specifically for vector search, has good Python client, supports metadata, and is efficient for similarity searches
**Alternatives considered**:
- Pinecone: Managed service, but more expensive
- Weaviate: Alternative vector database with GraphQL interface
- FAISS: Facebook's library, but requires more manual management

### 3. Web Scraping and Text Extraction

**Decision**: Use Beautiful Soup 4 with requests
**Rationale**: BeautifulSoup is the standard for HTML parsing in Python, reliable and well-documented
**Alternatives considered**:
- Selenium: More powerful but slower and resource-intensive
- Scrapy: Good for large-scale crawling but overkill for this use case
- Playwright: Modern alternative but more complex setup

### 4. URL Crawling Strategy

**Decision**: Implement breadth-first search with proper handling of Docusaurus sites
**Rationale**: Will ensure proper discovery of all pages while respecting robots.txt and avoiding infinite loops
**Alternatives considered**:
- scrapy-spiders: More sophisticated but complex setup
- Custom recursive approach: Simpler but risk of getting stuck

## Implementation Details

### 1. Docusaurus Site Handling

- Docusaurus sites typically have sitemaps at `/sitemap.xml`
- Need to identify and extract content from `<main>` or `.markdown` containers
- Navigation and header content should be excluded
- Handle relative links within the site

### 2. Text Chunking Strategy

**Decision**: Use recursive character splitting with overlap
**Rationale**: Simple but effective for preserving context while fitting model limits
**Chunk size**: 512-1024 tokens (approximately 400-800 words)
**Overlap**: 10-20% to maintain context across chunks

### 3. Embedding Dimensions

**Decision**: Use Cohere's default embedding model (typically 1024 dimensions)
**Rationale**: Good balance between accuracy and storage efficiency
**Model**: Cohere's embed-english-v3.0 or latest recommended model

### 4. Qdrant Collection Structure

**Decision**: Create collection with metadata storage
- Points: Each chunk as a vector with metadata (URL, content, etc.)
- Payload: Store source URL, chunk content, timestamp, and any relevant metadata
- Vector size: Match Cohere embedding dimensions (typically 1024)

## Security Considerations

- API keys for Cohere and Qdrant should be stored as environment variables
- Rate limiting for API calls to avoid exceeding quotas
- Proper error handling for failed API requests
- Validation of URLs to prevent access to unauthorized resources

## Dependencies

- `cohere`: For embedding generation
- `qdrant-client`: For vector database interaction
- `requests`: For HTTP requests
- `beautifulsoup4`: For HTML parsing
- `urllib3`: For URL handling and validation

## Error Handling Strategy

- Graceful degradation when pages can't be crawled
- Retry mechanisms for API calls
- Logging of failed documents for later review
- Handling of malformed HTML content

## Performance Optimizations

- Batch processing for embedding generation to reduce API calls
- Parallel crawling of multiple URLs within the same domain
- Caching of already processed URLs
- Monitoring of rate limits and quota consumption