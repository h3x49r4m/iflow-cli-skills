"""Pytest configuration and shared fixtures."""

import pytest


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