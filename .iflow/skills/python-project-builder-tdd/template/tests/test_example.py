"""Example test file demonstrating TDD best practices."""

def test_example_with_valid_input():
    """Should process valid input correctly.
    
    This test demonstrates the TDD workflow:
    1. Write this test first (it will fail)
    2. Implement minimum code to make it pass
    3. Refactor to improve code
    """
    # Arrange
    input_data = "valid input"
    
    # Act
    result = process_input(input_data)
    
    # Assert
    assert result is not None
    assert result["status"] == "success"
    assert result["data"] == input_data


def test_example_with_invalid_input_raises_error():
    """Should raise error for invalid input."""
    # Arrange
    input_data = ""
    
    # Act & Assert
    with pytest.raises(ValueError, match="Input cannot be empty"):
        process_input(input_data)


def test_example_with_boundary_values():
    """Should handle boundary values correctly."""
    # Test minimum valid length
    result = process_input("a")
    assert result["status"] == "success"
    
    # Test exactly at boundary
    boundary_input = "x" * 100
    result = process_input(boundary_input)
    assert result["status"] == "success"


# Helper function (would be implemented in src/)
def process_input(input_data: str) -> dict:
    """Process input data and return result.
    
    Args:
        input_data: The input string to process
        
    Returns:
        Dictionary with status and data
        
    Raises:
        ValueError: If input is empty
    """
    if not input_data:
        raise ValueError("Input cannot be empty")
    
    return {
        "status": "success",
        "data": input_data,
    }