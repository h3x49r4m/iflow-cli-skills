# Test Strategy Guide

## Purpose
This guide defines the testing strategy for Python projects, including test types, organization, and best practices.

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

### 1. Unit Tests
Test individual functions/methods in isolation.

**Purpose**: Verify each piece of code works correctly.

**Characteristics**:
- Fast (milliseconds)
- No external dependencies
- Mock external services
- Test one thing at a time

**Example**:
```python
def test_create_task_with_valid_input():
    """Should create task with valid input."""
    service = TaskService()
    task = service.create_task("Test task")
    
    assert task.id is not None
    assert task.title == "Test task"
    assert task.status == TaskStatus.PENDING
```

### 2. Integration Tests
Test interactions between components.

**Purpose**: Verify components work together correctly.

**Characteristics**:
- Medium speed (seconds)
- Real dependencies or sophisticated mocks
- Test workflows across components

**Example**:
```python
def test_create_and_retrieve_task():
    """Should create task and retrieve it."""
    repository = InMemoryTaskRepository()
    service = TaskService(repository)
    
    created = service.create_task("Test task")
    retrieved = service.get_task(created.id)
    
    assert retrieved.id == created.id
    assert retrieved.title == "Test task"
```

### 3. End-to-End (E2E) Tests
Test complete workflows from start to finish.

**Purpose**: Verify the system works as expected for users.

**Characteristics**:
- Slow (minutes)
- Test through external interface (API, CLI)
- Most comprehensive

**Example**:
```python
def test_create_task_via_api():
    """Should create task through API."""
    response = client.post("/tasks", json={"title": "Test task"})
    
    assert response.status_code == 201
    assert response.json()["title"] == "Test task"
    
    # Verify task exists
    get_response = client.get(f"/tasks/{response.json()['id']}")
    assert get_response.status_code == 200
```

### 4. Property-Based Tests
Test with random inputs to find edge cases.

**Purpose**: Find bugs through systematic testing of many inputs.

**Characteristics**:
- Uses hypothesis library
- Generates random inputs
- Finds unexpected edge cases

**Example**:
```python
from hypothesis import given, strategies as st

@given(st.text(min_size=1, max_size=200))
def test_create_task_with_various_titles(title):
    """Should create task with various valid titles."""
    service = TaskService()
    task = service.create_task(title)
    
    assert task.title == title
    assert task.id is not None
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
│   ├── test_service.py
│   └── test_validators.py
├── integration/             # Integration tests
│   ├── __init__.py
│   ├── test_task_workflow.py
│   └── test_user_workflow.py
├── e2e/                     # End-to-end tests
│   ├── __init__.py
│   └── test_api.py
└── fixtures/                # Test data fixtures
    ├── __init__.py
    └── task_fixtures.py
```

### Test File Naming
- Use `test_` prefix
- Match module being tested
- `test_task_service.py` tests `task_service.py`

### Test Naming
- Use descriptive names
- Format: `test_[function_name]_[condition]_[expected_result]`
- Examples:
  - `test_create_task_with_valid_title`
  - `test_delete_task_with_invalid_id_should_raise_error`
  - `test_update_task_status_from_pending_to_in_progress`

## Fixtures

### Using pytest Fixtures
```python
# conftest.py - Shared fixtures
import pytest
from src.tasks.service import TaskService
from src.tasks.repository import InMemoryTaskRepository

@pytest.fixture
def task_repository():
    """Provide a test repository."""
    return InMemoryTaskRepository()

@pytest.fixture
def task_service(task_repository):
    """Provide a task service with test repository."""
    return TaskService(task_repository)

@pytest.fixture
def sample_task():
    """Provide a sample task."""
    return Task(
        id="123",
        title="Sample task",
        status=TaskStatus.PENDING
    )

# Use fixtures in tests
def test_create_task(task_service):
    """Test creating a task."""
    task = task_service.create_task("Test")
    assert task is not None
```

### Parametrized Tests
```python
@pytest.mark.parametrize("title,expected_status", [
    ("Valid task", "created"),
    ("", "error"),
    ("x" * 201, "error"),
])
def test_create_task_with_various_inputs(title, expected_status):
    """Test task creation with various inputs."""
    service = TaskService()
    
    if expected_status == "error":
        with pytest.raises(ValidationError):
            service.create_task(title)
    else:
        task = service.create_task(title)
        assert task.title == title
```

## Mocking

### Mock External Dependencies
```python
from unittest.mock import Mock, patch

def test_create_task_with_external_api():
    """Test task creation that calls external API."""
    # Mock the external API call
    with patch('src.tasks.service.external_api') as mock_api:
        mock_api.send_notification.return_value = True
        
        service = TaskService()
        task = service.create_task("Test task")
        
        # Verify API was called
        mock_api.send_notification.assert_called_once()
```

### Mock Database
```python
def test_task_service_with_mocked_repository():
    """Test task service with mocked repository."""
    mock_repo = Mock()
    mock_repo.save.return_value = Task(id="123", title="Test", status=TaskStatus.PENDING)
    
    service = TaskService(mock_repo)
    task = service.create_task("Test task")
    
    # Verify repository was called
    mock_repo.save.assert_called_once()
    assert task.id == "123"
```

## Test Coverage

### Coverage Goals
- **Overall**: 80% minimum
- **Unit Tests**: 90% minimum
- **Integration Tests**: 70% minimum
- **E2E Tests**: Cover critical workflows

### Running Coverage
```bash
# Generate coverage report
uv run pytest --cov=src --cov-report=html --cov-report=term-missing

# View HTML report
open htmlcov/index.html
```

### Coverage Report Interpretation
```
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/tasks/models.py          20      2    90%   15-16
src/tasks/service.py         50      5    90%   42-45, 78
src/tasks/repository.py      30      0   100%
-------------------------------------------------------
TOTAL                       100      7    93%
```

## Test Configuration

### pytest.ini
```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = 
    -v
    --strict-markers
    --tb=short
    --cov=src
    --cov-report=term-missing
    --cov-report=html
markers =
    unit: Unit tests
    integration: Integration tests
    e2e: End-to-end tests
    slow: Slow running tests
```

### conftest.py
```python
import pytest

def pytest_configure(config):
    """Configure pytest markers."""
    config.addinivalue_line("markers", "unit: Unit tests")
    config.addinivalue_line("markers", "integration: Integration tests")
    config.addinivalue_line("markers", "e2e: End-to-end tests")
    config.addinivalue_line("markers", "slow: Slow running tests")

@pytest.fixture(autouse=True)
def reset_state():
    """Reset state between tests."""
    # Reset any global state
    yield
    # Cleanup after test
```

## Running Tests

### Run All Tests
```bash
uv run pytest
```

### Run Specific Test Type
```bash
# Only unit tests
uv run pytest -m unit

# Only integration tests
uv run pytest -m integration

# Only E2E tests
uv run pytest -m e2e
```

### Run Specific Test File
```bash
uv run pytest tests/unit/test_task_service.py
```

### Run Specific Test Function
```bash
uv run pytest tests/unit/test_task_service.py::test_create_task
```

### Run Tests Matching Pattern
```bash
uv run pytest -k "create_task"
```

### Run with Verbose Output
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

### Run Tests in Parallel
```bash
uv add --dev pytest-xdist
uv run pytest -n auto
```

## Test Best Practices

### 1. Test Behavior, Not Implementation
```python
# Good - tests behavior
def test_create_task_returns_task_with_id():
    service = TaskService()
    task = service.create_task("Test")
    assert task.id is not None

# Avoid - tests implementation
def test_create_task_calls_repository():
    service = TaskService()
    with patch.object(service._repository, 'save') as mock_save:
        service.create_task("Test")
        mock_save.assert_called_once()  # Too specific
```

### 2. Keep Tests Independent
```python
# Good - each test is independent
def test_create_task():
    service = TaskService()
    task = service.create_task("Test")
    assert task.title == "Test"

def test_update_task():
    service = TaskService()
    task = service.create_task("Original")  # Fresh task
    updated = service.update_task(task.id, "Updated")
    assert updated.title == "Updated"

# Avoid - tests depend on order
task_id = None

def test_create_task():
    global task_id
    task = service.create_task("Test")
    task_id = task.id

def test_update_task():
    # Depends on create_task running first
    updated = service.update_task(task_id, "Updated")
```

### 3. Use Arrange-Act-Assert Pattern
```python
def test_create_task():
    # Arrange
    service = TaskService()
    title = "Test task"
    
    # Act
    task = service.create_task(title)
    
    # Assert
    assert task.title == title
    assert task.status == TaskStatus.PENDING
```

### 4. Use Descriptive Test Names
```python
# Good
def test_create_task_with_empty_title_should_raise_validation_error():
    pass

# Avoid
def test_create_task_error():
    pass
```

### 5. Test Edge Cases
```python
def test_create_task_with_boundary_values():
    service = TaskService()
    
    # Minimum valid length
    task1 = service.create_task("A")
    assert task1.title == "A"
    
    # Maximum valid length
    max_title = "x" * 200
    task2 = service.create_task(max_title)
    assert task2.title == max_title
    
    # Just over maximum
    too_long = "x" * 201
    with pytest.raises(ValidationError):
        service.create_task(too_long)
```

### 6. Use Fixtures for Setup
```python
# Good - uses fixture
def test_create_task(task_service):
    task = task_service.create_task("Test")
    assert task is not None

# Avoid - duplicates setup
def test_create_task():
    repository = InMemoryTaskRepository()
    service = TaskService(repository)
    task = service.create_task("Test")
    assert task is not None
```

## Continuous Testing

### Pre-commit Hook
Run tests before committing:
```bash
# .git/hooks/pre-commit
#!/bin/bash
uv run pytest --exitfirst --quiet
```

### CI/CD Integration
```yaml
# .github/workflows/test.yml
name: Tests
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: pip install uv
      - run: uv sync
      - run: uv run pytest --cov=src --cov-report=xml
      - uses: codecov/codecov-action@v3
```

## Testing Checklist

Before marking a feature as tested:

- [ ] Unit tests written for all functions
- [ ] Integration tests for component interactions
- [ ] E2E tests for critical workflows
- [ ] Edge cases identified and tested
- [ ] Error conditions tested
- [ ] Coverage meets minimum threshold (80%)
- [ ] All tests pass
- [ ] Tests are fast (unit tests < 1 second)
- [ ] Tests are independent
- [ ] Tests have descriptive names
- [ ] Fixtures used appropriately
- [ ] No hardcoded test data (use fixtures)