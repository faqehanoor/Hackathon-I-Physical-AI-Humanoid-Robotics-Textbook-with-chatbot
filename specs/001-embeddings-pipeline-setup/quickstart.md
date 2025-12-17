# Quickstart Guide: Embeddings Pipeline

## Overview
This guide will help you set up and run the embeddings pipeline that extracts text from Docusaurus URLs, generates embeddings using Cohere, and stores them in Qdrant for RAG-based retrieval.

## Prerequisites

- Python 3.11 or higher
- pip package manager
- Cohere API key
- Qdrant instance (local or cloud)

## Setup

### 1. Install Dependencies

```bash
pip install requests beautifulsoup4 cohere qdrant-client python-dotenv
```

### 2. Environment Configuration

Create a `.env` file in your project directory with the following content:

```env
COHERE_API_KEY=your_cohere_api_key_here
QDRANT_URL=your_qdrant_url_here
QDRANT_API_KEY=your_qdrant_api_key_here  # if using cloud instance
```

### 3. Create Backend Directory

```bash
mkdir backend
cd backend
```

## Usage

### 1. Run the Pipeline

Execute the main pipeline script:

```bash
python main.py --url "https://hackathon-i-physical-ai-humanoid-ro-cyan.vercel.app/" --collection-name "chatbot-embeddings"
```

### 2. Command Line Options

- `--url`: URL of the Docusaurus site to process (required)
- `--collection-name`: Name of the Qdrant collection to store embeddings (default: "chatbot-embeddings")
- `--chunk-size`: Size of text chunks in tokens (default: 512)
- `--overlap`: Overlap between chunks in tokens (default: 50)
- `--limit`: Maximum number of pages to crawl (default: None, unlimited)

## Pipeline Overview

The pipeline performs the following steps:

1. **URL Crawling**: Discovers all pages from the provided Docusaurus site
2. **Text Extraction**: Extracts clean text content from each page
3. **Text Chunking**: Splits text into appropriate-sized chunks
4. **Embedding Generation**: Creates vector embeddings for each chunk using Cohere
5. **Vector Storage**: Stores embeddings in Qdrant with metadata

## Example Usage

```python
# In main.py

# 1. Get all URLs from the Docusaurus site
urls = get_all_urls("https://hackathon-i-physical-ai-humanoid-ro-cyan.vercel.app/")

# 2. Extract and clean text from each URL
for url in urls:
    text = extract_text_from_url(url)
    chunks = chunk_text(text, chunk_size=512, overlap=50)

# 3. Generate embeddings for each chunk
embeddings = embed(chunks)

# 4. Store in Qdrant collection
save_chunk_to_qdrant(embeddings, collection_name="chatbot-embeddings")
```

## Verification

After running the pipeline:
1. Check your Qdrant instance for the new collection
2. Verify the count of stored vectors matches expectations
3. Perform a test search to confirm retrieval works

## Troubleshooting

- **Rate Limit Errors**: Add delays between API calls or reduce concurrent requests
- **Memory Issues**: Process documents in smaller batches
- **Connection Errors**: Verify your Cohere and Qdrant API keys are correct