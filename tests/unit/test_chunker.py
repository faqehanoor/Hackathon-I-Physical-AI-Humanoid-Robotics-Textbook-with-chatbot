import pytest
from unittest.mock import Mock, patch, MagicMock
from backend.pipeline.chunker import chunk_text, chunk_document_chunks
from backend.models.document_chunk import DocumentChunk


class TestChunker:
    """Unit tests for chunker module"""

    def test_chunk_text_empty_content(self):
        """Test chunking empty content"""
        result = chunk_text("")
        assert result == []

    def test_chunk_text_shorter_than_chunk_size(self):
        """Test chunking content shorter than chunk size"""
        content = "Short content"
        result = chunk_text(content, chunk_size=50, overlap=10)
        assert result == [content]

    def test_chunk_text_exact_chunk_size(self):
        """Test chunking content exactly the chunk size"""
        content = "A" * 100  # 100 characters
        result = chunk_text(content, chunk_size=100, overlap=10)
        assert result == [content]

    def test_chunk_text_with_no_overlap(self):
        """Test chunking with no overlap"""
        content = "A" * 200  # 200 characters
        result = chunk_text(content, chunk_size=100, overlap=0)
        expected = ["A" * 100, "A" * 100]
        assert result == expected

    def test_chunk_text_with_overlap(self):
        """Test chunking with overlap"""
        content = "0123456789" * 10  # 100 characters
        result = chunk_text(content, chunk_size=30, overlap=5)
        # First chunk: "012345678901234567890123456789"
        # Second chunk should start at position 30-5=25: "...5678901234567890123456789"
        expected_first = "0123456789" * 3  # 30 chars
        expected_second = "567890123456789012345678901234"  # chars 25-54
        assert result[0] == expected_first
        assert result[1] == expected_second

    def test_chunk_document_chunks(self):
        """Test chunking a list of document chunks"""
        doc_chunk = DocumentChunk(
            content="A" * 200,  # 200 characters
            source_url="https://example.com",
            title="Test Title"
        )
        
        result = chunk_document_chunks([doc_chunk], chunk_size=100, overlap=0)
        
        assert len(result) == 2
        assert result[0].content == "A" * 100
        assert result[1].content == "A" * 100
        assert result[0].source_url == "https://example.com"
        assert result[1].source_url == "https://example.com"
        assert result[0].title == "Test Title - Part 1"
        assert result[1].title == "Test Title - Part 2"

    def test_chunk_document_chunks_with_metadata(self):
        """Test that metadata is preserved and extended when chunking document chunks"""
        original_metadata = {"original_key": "original_value"}
        doc_chunk = DocumentChunk(
            content="A" * 200,  # 200 characters
            source_url="https://example.com",
            title="Test Title",
            metadata=original_metadata
        )
        
        result = chunk_document_chunks([doc_chunk], chunk_size=100, overlap=0)
        
        # Check that original metadata is preserved and new metadata is added
        assert result[0].metadata["original_key"] == "original_value"
        assert result[0].metadata["original_chunk_id"] == doc_chunk.id
        assert result[0].metadata["chunk_index"] == 0
        assert result[0].metadata["total_chunks"] == 2