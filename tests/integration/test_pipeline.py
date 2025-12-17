import pytest
from unittest.mock import Mock, patch, MagicMock
from backend.pipeline.pipeline import run_extraction_pipeline, run_complete_pipeline
from backend.models.crawl_session import CrawlSession


class TestPipelineIntegration:
    """Integration tests for the complete pipeline"""

    @patch('backend.pipeline.pipeline.crawl_site')
    def test_run_extraction_pipeline(self, mock_crawl_site):
        """Test the extraction pipeline end-to-end"""
        # Mock the crawl_site function to return a mock CrawlSession
        mock_session = CrawlSession(
            id="test-session",
            created_at=None,
            start_url="https://example.com",
            status="completed",
            pages_processed=5
        )
        mock_crawl_site.return_value = mock_session

        url = "https://example.com"
        result = run_extraction_pipeline(
            url=url,
            max_pages=10,
            chunk_size=512,
            overlap=50
        )

        # Verify that crawl_site was called with the correct parameters
        mock_crawl_site.assert_called_once_with(url, 10)
        assert len(result) == 0  # The current implementation returns an empty list

    @patch('backend.pipeline.pipeline.crawl_site')
    @patch('backend.utils.get_logger')
    def test_run_complete_pipeline(self, mock_get_logger, mock_crawl_site):
        """Test the complete pipeline end-to-end"""
        # Mock the logger
        mock_logger = Mock()
        mock_get_logger.return_value = mock_logger

        # Mock the crawl_site function to return a mock CrawlSession
        mock_session = CrawlSession(
            id="test-session",
            created_at=None,
            start_url="https://example.com",
            status="completed",
            pages_processed=5
        )
        mock_crawl_site.return_value = mock_session

        url = "https://example.com"
        result = run_complete_pipeline(
            url=url,
            collection_name="test-collection",
            chunk_size=512,
            overlap=50,
            max_pages=10
        )

        # Verify that crawl_site was called with the correct parameters
        mock_crawl_site.assert_called_once_with(url, 10)
        # Verify the returned session matches the mocked one
        assert result.id == "test-session"
        assert result.start_url == "https://example.com"
        assert result.status == "completed"
        assert result.pages_processed == 5

        # Verify that logging was called
        mock_logger.info.assert_any_call(f"Starting complete pipeline for URL: {url}")
        mock_logger.info.assert_any_call(f"Complete pipeline finished for URL: {url}")