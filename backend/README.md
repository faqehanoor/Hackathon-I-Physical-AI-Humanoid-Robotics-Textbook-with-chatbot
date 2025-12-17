# AI-Native Book Backend

This is the backend for an AI-powered book processing and management application. It provides APIs for managing books and integrating AI capabilities for content analysis, summarization, and embeddings.

## Features

- RESTful API for managing books
- AI-powered text summarization using Cohere
- Embedding generation for semantic search using Cohere and Qdrant
- Content analysis and processing
- SQLite database (with PostgreSQL support)

## Prerequisites

- Python 3.11+
- pip
- venv (recommended)

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd ai-native-book/backend
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install uv
uv sync
```

4. Create a `.env` file in the root directory with the following:
```env
COHERE_API_KEY=your_cohere_api_key_here
QDRANT_URL=http://localhost:6333  # Or your Qdrant instance URL
DATABASE_URL=sqlite:///./books.db  # Or your database URL
```

5. Run the application:
```bash
python main.py
```

Or use the development server directly:
```bash
uv run dev
```

## API Endpoints

### Books API (`/api/v1/books`)
- `GET /` - Get all books
- `GET /{book_id}` - Get a specific book
- `POST /` - Create a new book
- `PUT /{book_id}` - Update a specific book
- `DELETE /{book_id}` - Delete a specific book

### AI API (`/api/v1/ai`)
- `POST /summarize` - Summarize text content
- `POST /embeddings` - Generate embeddings for texts
- `POST /generate` - Generate text using AI

## Environment Variables

- `COHERE_API_KEY` - Your Cohere API key (get it from https://dashboard.cohere.com/api-keys)
- `QDRANT_URL` - URL for your Qdrant instance (default: http://localhost:6333)
- `DATABASE_URL` - Database connection string (default: sqlite:///./books.db)

## Running with uv

This project uses `uv` for dependency management. To run commands:

- `uv run dev` - Start the development server with hot reload
- `uv run start` - Start the production server
- `uv run python src/utils/db_init.py` - Initialize the database

## Project Structure

```
backend/
├── main.py                 # Entry point
├── pyproject.toml          # Project dependencies and metadata
├── src/
│   ├── main.py             # FastAPI app definition
│   ├── api/                # API route definitions
│   │   ├── books.py        # Book-related endpoints
│   │   └── ai.py           # AI-related endpoints
│   ├── models/             # Database models
│   │   └── book.py         # Book model
│   ├── schemas/            # Pydantic schemas
│   │   └── book.py         # Request/response schemas
│   ├── database/           # Database utilities
│   │   └── session.py      # Database session management
│   └── utils/              # Utility functions
│       └── db_init.py      # Database initialization
└── README.md               # This file
```

## Development

For development, use the `dev` command which starts the server with hot reload:

```bash
uv run dev
```

The API documentation will be available at `http://127.0.0.1:8000/docs` when the server is running.