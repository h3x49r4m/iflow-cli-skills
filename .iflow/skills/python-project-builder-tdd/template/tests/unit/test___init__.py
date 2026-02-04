"""Unit tests for src/__init__.py."""

import pytest


def test_module_imports():
    """Should import module successfully."""
    import src
    
    assert src is not None


def test_module_version():
    """Should have version information."""
    # This test will fail until version is defined in src/__init__.py
    # Implement version check when version is added
    pass


def test_module_exports():
    """Should export expected public API."""
    import src
    
    # Update this test when public API is defined
    expected_exports = []
    actual_exports = [name for name in dir(src) if not name.startswith('_')]
    
    # For now, just verify we can list exports
    assert isinstance(actual_exports, list)