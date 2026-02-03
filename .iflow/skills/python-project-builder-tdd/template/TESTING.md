# Testing Documentation

This document describes the testing strategy and standards for this project.

## Testing Philosophy

This project follows **Test-Driven Development (TDD)** methodology:
1. **Red**: Write a failing test first
2. **Green**: Write minimum code to make the test pass
3. **Refactor**: Improve code while keeping tests passing

## Testing Pyramid

```
        /\
       /  \        E2E Tests (10%)
      /____\       - Complete workflows
     /      \      - Slow, comprehensive
    /________\     
   /          \    Integration Tests (20%)
  /            \   - Component interactions
 /              \  - Medium speed
/________________\
                  Unit Tests (70%)
                  - Individual functions
                  - Fast, isolated
```

## Test Types

### Unit Tests (70%)
- Test individual functions/methods in isolation
- Fast (milliseconds)
- Mock external dependencies
- Located in `tests/unit/`

### Integration Tests (20%)
- Test interactions between components
- Medium speed (seconds)
- Real dependencies or sophisticated mocks
- Located in `tests/integration/`

### End-to-End Tests (10%)
- Test complete workflows
- Slow (minutes)
- Test through external interface (API, CLI)
- Located in `tests/e2e/`

## Coverage Requirements

| Metric | Minimum | Target |
|--------|---------|--------|
| Line Coverage | 80% | 90% |
| Branch Coverage | 75% | 85% |
| Function Coverage | 100% | 100% |

## Running Tests

### All Tests
```bash
uv run pytest
```

### With Coverage
```bash
uv run pytest --cov=src --cov-report=html --cov-report=term-missing
```

### Specific Test Type
```bash
# Unit tests only
uv run pytest tests/unit/ -m unit

# Integration tests only
uv run pytest tests/integration/ -m integration

# E2E tests only
uv run pytest tests/e2e/ -m e2e
```

### Specific Test File
```bash
uv run pytest tests/unit/test_module.py
```

### Specific Test Function
```bash
uv run pytest tests/unit/test_module.py::test_function_name
```

### Verbose Output
```bash
uv run pytest -v
```

### Stop on First Failure
```bash
uv run pytest -x
```

### Run Failed Tests Only
```bash
uv run pytest --lf
```

## Test Organization

### Directory Structure
```
tests/
├── __init__.py
├── conftest.py              # Shared fixtures
├── unit/                    # Unit tests
│   ├── __init__.py
│   ├── test_models.py
│   └── test_service.py
├── integration/             # Integration tests
│   ├── __init__.py
│   └── test_workflows.py
└── e2e/                     # End-to-end tests
    ├── __init__.py
    └── test_api.py
```

### Test Naming

**Files**: `test_<module_name>.py`

**Functions**: `test_<function_name>_<condition>_<expected_result>`

**Classes**: `Test<ClassName>`

### Example Test

```python
def test_create_task_with_valid_title():
    """Should create task with valid title."""
    # Arrange
    service = TaskService()
    title = "Test task"
    
    # Act
    task = service.create_task(title)
    
    # Assert
    assert task.id is not None
    assert task.title == title
    assert task.status == TaskStatus.PENDING
```

## Fixtures

### Using Fixtures
```python
import pytest

@pytest.fixture
def task_service():
    """Provide a task service for testing."""
    return TaskService()

def test_create_task(task_service):
    """Test creating a task."""
    task = task_service.create_task("Test")
    assert task is not None
```

### Parametrized Tests
```python
@pytest.mark.parametrize("title,expected", [
    ("Valid", "created"),
    ("", "error"),
])
def test_create_task_with_various_inputs(title, expected):
    """Test task creation with various inputs."""
    pass
```

## Test Best Practices

1. **Test Behavior, Not Implementation**: Focus on what the code does, not how
2. **Keep Tests Independent**: No shared state between tests
3. **Use Descriptive Names**: Test names should describe what is being tested
4. **Follow AAA Pattern**: Arrange, Act, Assert
5. **Mock External Dependencies**: Mock databases, APIs, etc. for unit tests
6. **Test Edge Cases**: Test boundary values, empty inputs, errors
7. **Keep Tests Fast**: Unit tests should run in < 1 second
8. **Use Fixtures**: Extract common setup into fixtures

## CI/CD Integration

### GitHub Actions
```yaml
- name: Run tests
  run: uv run pytest --cov=src --cov-report=xml

- name: Upload coverage
  uses: codecov/codecov-action@v3
  with:
    file: ./coverage.xml
```

### Pre-commit Hook
```bash
#!/bin/bash
uv run pytest --exitfirst --quiet
```

## Test Quality Checklist

Before marking code as complete:

- [ ] All acceptance criteria have tests
- [ ] All edge cases have tests
- [ ] All tests pass
- [ ] Coverage meets minimum (80%)
- [ ] Tests are independent
- [ ] Tests are fast (< 1 second for unit tests)
- [ ] Tests have descriptive names
- [ ] No test code duplication
- [ ] Fixtures used appropriately

## Troubleshooting

### Tests Fail with Import Errors
```bash
# Reinstall dependencies
uv sync --reinstall

# Check Python path
uv run python -c "import sys; print(sys.path)"
```

### Coverage Shows 0%
```bash
# Check coverage configuration
uv run pytest --cov=src --cov-report=term-missing

# Verify source path
ls src/
```

### Tests Are Slow
```bash
# Run with profiling
uv run pytest --profile

# Identify slow tests
uv run pytest --durations=10
```