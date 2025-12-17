import pytest
from datetime import datetime
from backend.models.document_chunk import DocumentChunk
from backend.models.crawl_session import CrawlSession
from backend.models.embedding import Embedding
from backend.models.vector_index import VectorIndex


class TestDocumentChunk:
    """Unit tests for DocumentChunk model"""

    def test_create_document_chunk(self):
        """Test creating a basic DocumentChunk"""
        chunk = DocumentChunk(
            content="Test content",
            source_url="https://example.com",
            title="Test Title"
        )
        
        assert chunk.content == "Test content"
        assert chunk.source_url == "https://example.com"
        assert chunk.title == "Test Title"
        assert chunk.id is not None  # Auto-generated
        assert chunk.created_at is not None  # Auto-generated
        assert chunk.metadata == {}  # Default empty dict

    def test_document_chunk_with_metadata(self):
        """Test creating a DocumentChunk with metadata"""
        metadata = {"section": "introduction", "level": 1}
        chunk = DocumentChunk(
            content="Test content",
            source_url="https://example.com",
            title="Test Title",
            metadata=metadata
        )
        
        assert chunk.metadata == metadata

    def test_document_chunk_default_values(self):
        """Test that DocumentChunk has proper default values"""
        chunk = DocumentChunk(
            content="Test content",
            source_url="https://example.com"
        )
        
        assert chunk.title == ""
        assert chunk.metadata == {}


class TestCrawlSession:
    """Unit tests for CrawlSession model"""

    def test_create_crawl_session(self):
        """Test creating a basic CrawlSession"""
        session = CrawlSession(
            start_url="https://example.com",
            status="initialized"
        )
        
        assert session.start_url == "https://example.com"
        assert session.status == "initialized"
        assert session.id is not None  # Auto-generated
        assert session.created_at is not None  # Auto-generated
        assert session.pages_processed == 0
        assert session.errors_count == 0
        assert session.processed_urls == []
        assert session.error_details == []

    def test_crawl_session_with_optional_params(self):
        """Test creating a CrawlSession with optional parameters"""
        session = CrawlSession(
            start_url="https://example.com",
            status="completed",
            pages_processed=10,
            errors_count=1,
            processed_urls=["https://example.com/page1"],
            error_details=[{"url": "https://example.com/bad", "error": "404"}],
            completed_at=datetime.now()
        )
        
        assert session.start_url == "https://example.com"
        assert session.status == "completed"
        assert session.pages_processed == 10
        assert session.errors_count == 1
        assert len(session.processed_urls) == 1
        assert len(session.error_details) == 1


class TestEmbedding:
    """Unit tests for Embedding model"""

    def test_create_embedding(self):
        """Test creating a basic Embedding"""
        vector = [0.1, 0.2, 0.3]
        embedding = Embedding(
            vector=vector,
            model="test-model",
            chunk_id="chunk-123"
        )
        
        assert embedding.vector == vector
        assert embedding.model == "test-model"
        assert embedding.chunk_id == "chunk-123"
        assert embedding.id is not None  # Auto-generated
        assert embedding.created_at is not None  # Auto-generated
        assert embedding.metadata == {}  # Default empty dict

    def test_embedding_with_metadata(self):
        """Test creating an Embedding with metadata"""
        vector = [0.1, 0.2, 0.3]
        metadata = {"source_url": "https://example.com", "chunk_title": "Test"}
        embedding = Embedding(
            vector=vector,
            model="test-model",
            chunk_id="chunk-123",
            metadata=metadata
        )
        
        assert embedding.metadata == metadata


class TestVectorIndex:
    """Unit tests for VectorIndex model"""

    def test_create_vector_index(self):
        """Test creating a basic VectorIndex"""
        index = VectorIndex(
            name="test-index"
        )
        
        assert index.name == "test-index"
        assert index.id is not None  # Auto-generated
        assert index.created_at is not None  # Auto-generated
        assert index.size == 0
        assert index.vector_dimension == 0
        assert index.updated_at is not None  # Auto-generated
        assert index.metadata_schema == {}  # Default empty dict

    def test_vector_index_with_params(self):
        """Test creating a VectorIndex with parameters"""
        index = VectorIndex(
            name="test-index",
            size=100,
            vector_dimension=1024
        )
        
        assert index.name == "test-index"
        assert index.size == 100
        assert index.vector_dimension == 1024