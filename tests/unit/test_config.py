import pytest
import os
from backend.config import Config


class TestConfig:
    """Unit tests for Config class"""

    def test_validate_with_cohere_api_key(self, monkeypatch):
        """Test validation passes when COHERE_API_KEY is set"""
        monkeypatch.setenv("COHERE_API_KEY", "test-key")
        
        # Reload the Config class after changing the environment
        import importlib
        import backend.config
        importlib.reload(backend.config)
        from backend.config import Config
        
        # Check that the validation passes
        assert Config.validate() is True

    def test_validate_without_cohere_api_key(self, monkeypatch):
        """Test validation fails when COHERE_API_KEY is not set"""
        monkeypatch.delenv("COHERE_API_KEY", raising=False)
        
        # Reload the Config class after changing the environment
        import importlib
        import backend.config
        importlib.reload(backend.config)
        from backend.config import Config
        
        # Check that the validation fails
        assert Config.validate() is False

    def test_default_values(self, monkeypatch):
        """Test that default configuration values are set correctly"""
        # Remove any environment variables that might be set
        monkeypatch.delenv("DEFAULT_CHUNK_SIZE", raising=False)
        monkeypatch.delenv("DEFAULT_OVERLAP", raising=False)
        monkeypatch.delenv("DEFAULT_COLLECTION_NAME", raising=False)
        monkeypatch.delenv("MAX_PAGES_TO_CRAWL", raising=False)
        monkeypatch.delenv("QDRANT_URL", raising=False)
        
        # Reload the Config class after changing the environment
        import importlib
        import backend.config
        importlib.reload(backend.config)
        from backend.config import Config
        
        # Check default values
        assert Config.DEFAULT_CHUNK_SIZE == 512
        assert Config.DEFAULT_OVERLAP == 50
        assert Config.DEFAULT_COLLECTION_NAME == "chatbot-embeddings"
        assert Config.MAX_PAGES_TO_CRAWL is None
        assert Config.QDRANT_URL == "http://localhost:6333"

    def test_custom_values(self, monkeypatch):
        """Test that custom configuration values are set correctly from environment"""
        monkeypatch.setenv("DEFAULT_CHUNK_SIZE", "1024")
        monkeypatch.setenv("DEFAULT_OVERLAP", "100")
        monkeypatch.setenv("DEFAULT_COLLECTION_NAME", "custom-embeddings")
        monkeypatch.setenv("MAX_PAGES_TO_CRAWL", "50")
        monkeypatch.setenv("QDRANT_URL", "https://custom-qdrant.example.com")
        
        # Reload the Config class after changing the environment
        import importlib
        import backend.config
        importlib.reload(backend.config)
        from backend.config import Config
        
        # Check custom values
        assert Config.DEFAULT_CHUNK_SIZE == 1024
        assert Config.DEFAULT_OVERLAP == 100
        assert Config.DEFAULT_COLLECTION_NAME == "custom-embeddings"
        assert Config.MAX_PAGES_TO_CRAWL == 50
        assert Config.QDRANT_URL == "https://custom-qdrant.example.com"