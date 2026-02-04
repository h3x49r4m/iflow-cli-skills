"""Pytest configuration and shared fixtures."""

import pytest


def pytest_configure(config):
    """Configure pytest markers."""
    config.addinivalue_line("markers", "unit: Unit tests (fast, isolated)")
    config.addinivalue_line("markers", "integration: Integration tests (medium speed, component interactions)")
    config.addinivalue_line("markers", "e2e: End-to-end tests (slow, complete workflows)")
    config.addinivalue_line("markers", "slow: Slow running tests")


# Fixtures for Unit Tests


@pytest.fixture
def sample_data():
    """Provide sample data for testing."""
    return {
        "id": "123",
        "name": "Test",
        "value": 42,
    }


@pytest.fixture
def mock_config():
    """Provide mock configuration for testing."""
    return {
        "debug": False,
        "log_level": "INFO",
    }


@pytest.fixture
def sample_user():
    """Provide a sample user for testing."""
    return {
        "id": "user-123",
        "name": "Test User",
        "email": "test@example.com",
    }


# Fixtures for Integration Tests


@pytest.fixture
def test_database():
    """Provide an in-memory database for integration testing."""
    # This would typically use sqlite :memory: or a test database
    # Implement based on your database requirements
    yield {}


@pytest.fixture
def test_storage():
    """Provide test storage for integration testing."""
    # This would typically use a mock storage backend
    # Implement based on your storage requirements
    yield {}


# Fixtures for E2E Tests


@pytest.fixture
def api_client():
    """Provide an API client for E2E testing."""
    # This would typically use TestClient from FastAPI or similar
    # Implement based on your API framework
    class TestClient:
        def get(self, path):
            return {"status": "ok", "path": path}
        
        def post(self, path, data):
            return {"status": "created", "path": path, "data": data}
    
    return TestClient()


@pytest.fixture
def test_environment():
    """Provide test environment variables for E2E testing."""
    import os
    
    # Set up test environment
    original_env = os.environ.copy()
    os.environ["TEST_MODE"] = "true"
    os.environ["DATABASE_URL"] = "sqlite:///:memory:"
    
    yield
    
    # Clean up - restore original environment
    os.environ.clear()
    os.environ.update(original_env)


# Autouse Fixtures


@pytest.fixture(autouse=True)
def reset_state():
    """Reset state between tests."""
    # Reset any global state before test
    yield
    # Clean up after test