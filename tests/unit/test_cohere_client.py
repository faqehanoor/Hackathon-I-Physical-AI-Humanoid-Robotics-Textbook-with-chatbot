import pytest
from unittest.mock import Mock, patch, MagicMock
from backend.services.cohere_client import CohereClient
from backend.config import Config


class TestCohereClient:
    """Unit tests for CohereClient service"""

    @patch('backend.services.cohere_client.cohere')
    def test_init_client_with_api_key(self, mock_cohere):
        """Test initializing CohereClient with API key"""
        # Mock the environment to have an API key
        original_api_key = Config.COHERE_API_KEY
        Config.COHERE_API_KEY = "test-api-key"
        
        mock_client_instance = Mock()
        mock_cohere.Client.return_value = mock_client_instance
        
        client = CohereClient()
        
        # Verify that the client was created with the API key
        mock_cohere.Client.assert_called_once_with("test-api-key")
        assert client.client == mock_client_instance
        assert client.default_model == "embed-english-v3.0"
        
        # Restore original API key
        Config.COHERE_API_KEY = original_api_key

    @patch('backend.services.cohere_client.cohere')
    def test_init_client_without_api_key_raises_error(self, mock_cohere):
        """Test that initializing CohereClient without API key raises error"""
        # Mock the environment to not have an API key
        original_api_key = Config.COHERE_API_KEY
        Config.COHERE_API_KEY = ""
        
        with pytest.raises(ValueError, match="COHERE_API_KEY environment variable is required"):
            CohereClient()
        
        # Restore original API key
        Config.COHERE_API_KEY = original_api_key

    @patch('backend.services.cohere_client.cohere')
    def test_generate_embeddings_success(self, mock_cohere):
        """Test successful embedding generation"""
        original_api_key = Config.COHERE_API_KEY
        Config.COHERE_API_KEY = "test-api-key"
        
        # Set up mock
        mock_client_instance = Mock()
        mock_cohere.Client.return_value = mock_client_instance
        
        mock_response = Mock()
        mock_response.embeddings = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]]
        mock_client_instance.embed.return_value = mock_response
        
        client = CohereClient()
        client.default_model = "test-model"
        
        texts = ["text1", "text2"]
        result = client.generate_embeddings(texts)
        
        # Verify the call to embed
        mock_client_instance.embed.assert_called_once_with(
            texts=texts,
            model="test-model",
            input_type="search_document"
        )
        
        # Verify the result
        assert result == [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]]
        
        # Restore original API key
        Config.COHERE_API_KEY = original_api_key

    @patch('backend.services.cohere_client.cohere')
    def test_embed_single_text(self, mock_cohere):
        """Test embedding a single text"""
        original_api_key = Config.COHERE_API_KEY
        Config.COHERE_API_KEY = "test-api-key"
        
        # Set up mock
        mock_client_instance = Mock()
        mock_cohere.Client.return_value = mock_client_instance
        
        mock_response = Mock()
        mock_response.embeddings = [[0.1, 0.2, 0.3]]
        mock_client_instance.embed.return_value = mock_response
        
        client = CohereClient()
        
        text = "single text"
        result = client.embed_single_text(text)
        
        # Verify the result is the first embedding
        assert result == [0.1, 0.2, 0.3]
        
        # Restore original API key
        Config.COHERE_API_KEY = original_api_key

    @patch('backend.services.cohere_client.cohere')
    def test_generate_embeddings_error_handling(self, mock_cohere):
        """Test error handling in embedding generation"""
        original_api_key = Config.COHERE_API_KEY
        Config.COHERE_API_KEY = "test-api-key"
        
        # Set up mock to raise an exception
        mock_client_instance = Mock()
        mock_cohere.Client.return_value = mock_client_instance
        
        mock_client_instance.embed.side_effect = Exception("API Error")
        
        client = CohereClient()
        
        with pytest.raises(Exception, match="API Error"):
            client.generate_embeddings(["test text"])
        
        # Restore original API key
        Config.COHERE_API_KEY = original_api_key