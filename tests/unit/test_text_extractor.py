import pytest
from unittest.mock import Mock, patch, MagicMock
from backend.pipeline.text_extractor import (
    clean_text_content, 
    extract_title_from_html, 
    extract_content_by_selectors,
    extract_text_from_html
)
from backend.models.document_chunk import DocumentChunk


class TestTextExtractor:
    """Unit tests for text_extractor module"""

    def test_clean_text_content_empty(self):
        """Test cleaning empty content"""
        result = clean_text_content("")
        assert result == ""

    def test_clean_text_content_whitespace_normalization(self):
        """Test that whitespace is normalized"""
        input_text = "word1    word2\t\tword3\n\n\nword4"
        expected = "word1 word2 word3\nword4"
        result = clean_text_content(input_text)
        assert result == expected

    def test_clean_text_content_copyright_removal(self):
        """Test that copyright notices are removed"""
        input_text = "Some content Copyright 2023 Company Name. More content."
        expected = "Some content  More content."
        result = clean_text_content(input_text)
        assert result == expected

    def test_extract_title_from_html_with_title_tag(self):
        """Test extracting title from title tag"""
        html = '<html><head><title>Test Title</title></head><body>Content</body></html>'
        result = extract_title_from_html(html)
        assert result == "Test Title"

    def test_extract_title_from_html_with_h1_fallback(self):
        """Test extracting title from h1 when no title tag exists"""
        html = '<html><body><h1>Heading Title</h1>Content</body></html>'
        result = extract_title_from_html(html)
        assert result == "Heading Title"

    def test_extract_title_from_html_no_title(self):
        """Test that empty string is returned when no title is found"""
        html = '<html><body>Content</body></html>'
        result = extract_title_from_html(html)
        assert result == ""

    def test_extract_content_by_selectors_success(self):
        """Test extracting content using CSS selectors"""
        html = '''
        <html>
            <body>
                <main>
                    <div class="markdown">Main content here</div>
                </main>
            </body>
        </html>
        '''
        selectors = ['.markdown', 'main']
        result = extract_content_by_selectors(html, selectors)
        assert "Main content here" in result

    def test_extract_content_by_selectors_fallback(self):
        """Test that fallback to all text works when selectors fail"""
        html = '<html><body><p>Fallback content</p></body></html>'
        selectors = ['.nonexistent']
        result = extract_content_by_selectors(html, selectors)
        assert "Fallback content" in result

    def test_extract_text_from_html(self):
        """Test complete HTML to DocumentChunk extraction"""
        html = '''
        <html>
            <head><title>Test Page</title></head>
            <body>
                <main>
                    <div class="markdown">This is the main content of the page.</div>
                </main>
            </body>
        </html>
        '''
        source_url = "https://example.com/test"
        
        result = extract_text_from_html(html, source_url)
        
        assert isinstance(result, DocumentChunk)
        assert result.title == "Test Page"
        assert "main content" in result.content
        assert result.source_url == source_url
        assert result.metadata["extracted_from_html"] is True