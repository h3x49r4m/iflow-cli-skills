# Feature Implementation Guide

## Purpose
This guide explains how to implement features following TDD principles and the project architecture.

## Feature Implementation Process

### Step 1: Review Feature Specification
- Read the feature spec from `01-planning/`
- Understand acceptance criteria
- Review dependencies and interfaces

### Step 2: Review Architecture Design
- Check module design from `02-architecture/`
- Review interface definitions
- Understand data flow

### Step 3: Create Test File
Create a test file for the feature:

```python
# tests/test_[feature_name].py
import pytest
from src.[module].[module] import [Class/Function]

def test_[specific_behavior]():
    """[Description of what is being tested]."""
    # Arrange
    # Set up test data
    
    # Act
    # Call the function/method
    
    # Assert
    # Verify expected behavior
```

### Step 4: Write Tests for Acceptance Criteria
For each acceptance criterion, write a test:

```python
# Example: Feature - Create Task
# Acceptance Criteria:
# 1. User can create a task with valid title
# 2. Empty title should raise error
# 3. Title exceeding 200 chars should raise error

def test_create_task_with_valid_title():
    """Should create a task when title is valid."""
    service = TaskService()
    task = service.create_task("Valid title")
    
    assert task.id is not None
    assert task.title == "Valid title"
    assert task.status == TaskStatus.PENDING

def test_create_task_with_empty_title_should_raise_error():
    """Should raise ValueError when title is empty."""
    service = TaskService()
    
    with pytest.raises(ValueError, match="Title cannot be empty"):
        service.create_task("")

def test_create_task_with_long_title_should_raise_error():
    """Should raise ValueError when title exceeds 200 chars."""
    service = TaskService()
    long_title = "x" * 201
    
    with pytest.raises(ValueError, match="Title cannot exceed 200 characters"):
        service.create_task(long_title)
```

### Step 5: Write Edge Case Tests
Identify and test edge cases:

```python
def test_create_task_with_unicode_title():
    """Should handle unicode characters in title."""
    service = TaskService()
    task = service.create_task("中文标题 🎉")
    
    assert task.title == "中文标题 🎉"

def test_create_task_with_special_characters():
    """Should handle special characters in title."""
    service = TaskService()
    task = service.create_task("Task with <special> & characters!")
    
    assert task.title == "Task with <special> & characters!"

def test_create_task_with_whitespace_only():
    """Should raise error when title is only whitespace."""
    service = TaskService()
    
    with pytest.raises(ValueError):
        service.create_task("   ")
```

### Step 6: Implement the Feature
Write minimum code to pass tests:

```python
# src/tasks/service.py
import uuid
from src.tasks.models import Task, TaskStatus
from src.tasks.exceptions import ValidationError

class TaskService:
    MAX_TITLE_LENGTH = 200
    
    def create_task(self, title: str) -> Task:
        """Create a new task."""
        self._validate_title(title)
        
        return Task(
            id=str(uuid.uuid4()),
            title=title.strip(),
            status=TaskStatus.PENDING
        )
    
    def _validate_title(self, title: str) -> None:
        """Validate task title."""
        if not title or not title.strip():
            raise ValidationError("Title cannot be empty")
        if len(title) > self.MAX_TITLE_LENGTH:
            raise ValidationError(f"Title cannot exceed {self.MAX_TITLE_LENGTH} characters")
```

### Step 7: Run Tests
```bash
uv run pytest tests/test_[feature_name].py -v
```

### Step 8: Refactor Code
Improve code quality while keeping tests passing:

```python
# Refactored version
class TaskService:
    MAX_TITLE_LENGTH = 200
    
    def __init__(self, repository: TaskRepository):
        self._repository = repository
    
    def create_task(self, title: str, description: str = None) -> Task:
        """Create a new task."""
        validated_title = self._validate_and_sanitize_title(title)
        
        task = Task(
            id=str(uuid.uuid4()),
            title=validated_title,
            description=description,
            status=TaskStatus.PENDING
        )
        
        return self._repository.save(task)
    
    def _validate_and_sanitize_title(self, title: str) -> str:
        """Validate and sanitize task title."""
        if not title:
            raise ValidationError("Title cannot be empty")
        
        sanitized = title.strip()
        
        if not sanitized:
            raise ValidationError("Title cannot be empty")
        
        if len(title) > self.MAX_TITLE_LENGTH:
            raise ValidationError(f"Title cannot exceed {self.MAX_TITLE_LENGTH} characters")
        
        return sanitized
```

### Step 9: Add Integration Tests
Test interactions with other components:

```python
def test_create_task_with_repository_integration():
    """Should create and save task through repository."""
    repository = InMemoryTaskRepository()
    service = TaskService(repository)
    
    task = service.create_task("Test task")
    
    retrieved = repository.find_by_id(task.id)
    assert retrieved is not None
    assert retrieved.title == "Test task"
```

### Step 10: Update Documentation
Update relevant documentation:
- Add examples to docstrings
- Update feature tracker
- Document any API changes

## Implementation Checklist

Before marking a feature as implemented:

- [ ] All acceptance criteria have tests
- [ ] All edge cases have tests
- [ ] All tests pass
- [ ] Code follows project conventions
- [ ] Type hints are present
- [ ] Docstrings are complete
- [ ] Code has been refactored
- [ ] No code duplication
- [ ] Integration tests written (if applicable)
- [ ] Documentation updated

## Code Structure Guidelines

### File Organization
```
src/
├── [module_name]/
│   ├── __init__.py          # Public API exports
│   ├── models.py            # Data models
│   ├── service.py           # Business logic
│   ├── repository.py        # Data access (if needed)
│   └── exceptions.py        # Module exceptions
```

### Class Structure
```python
class ClassName:
    """Brief description of the class.
    
    Longer description if needed.
    """
    
    # Class constants
    CONSTANT_NAME = value
    
    def __init__(self, param1: Type1, param2: Type2):
        """Initialize the class.
        
        Args:
            param1: Description
            param2: Description
        """
        self._param1 = param1
        self._param2 = param2
    
    def public_method(self, param: Type) -> ReturnType:
        """Public method description.
        
        Args:
            param: Description
            
        Returns:
            Description
            
        Raises:
            ExceptionType: Description
        """
        pass
    
    def _private_method(self, param: Type) -> ReturnType:
        """Private method description."""
        pass
```

### Function Structure
```python
def function_name(param1: Type1, param2: Type2) -> ReturnType:
    """Brief description.
    
    Args:
        param1: Description
        param2: Description
        
    Returns:
        Description
        
    Raises:
        ExceptionType: Description
        
    Example:
        >>> result = function_name("value1", "value2")
        >>> print(result)
        expected output
    """
    pass
```

## Common Patterns

### Dependency Injection
```python
class Service:
    def __init__(self, dependency: DependencyInterface):
        self._dependency = dependency
```

### Factory Pattern
```python
def create_task_service(config: Config) -> TaskService:
    """Factory function to create TaskService."""
    repository = TaskRepository(config.db_url)
    return TaskService(repository)
```

### Strategy Pattern
```python
class Validator(ABC):
    @abstractmethod
    def validate(self, data: Any) -> None:
        pass

class EmailValidator(Validator):
    def validate(self, data: str) -> None:
        # Email validation logic
        pass
```

## Handling Dependencies

### External Libraries
```python
# Add to pyproject.toml
# uv add library_name

# Import in code
import library_name
```

### Internal Modules
```python
# Import from module's public API
from src.tasks.models import Task
from src.tasks.service import TaskService
```

### Testing Dependencies
```python
# Use pytest fixtures for setup
@pytest.fixture
def task_service():
    """Fixture providing TaskService instance."""
    repository = InMemoryTaskRepository()
    return TaskService(repository)

# Use fixture in tests
def test_create_task(task_service):
    task = task_service.create_task("Test")
    assert task is not None
```

## Debugging Failed Tests

### Run Test with Output
```bash
uv run pytest tests/test_feature.py::test_function -v -s
```

### Run with Debugger
```bash
uv run pytest --pdb tests/test_feature.py::test_function
```

### Print Test Coverage
```bash
uv run pytest --cov=src --cov-report=term-missing
```

## Best Practices

1. **Write Tests First**: Always follow TDD
2. **Keep Functions Small**: Single responsibility
3. **Use Type Hints**: All parameters and returns
4. **Write Docstrings**: Clear documentation
5. **Handle Errors Gracefully**: Meaningful error messages
6. **Avoid Code Duplication**: Extract common logic
7. **Follow Naming Conventions**: PEP 8
8. **Keep Tests Independent**: No shared state between tests
9. **Make Tests Fast**: Unit tests should be fast
10. **Refactor Continuously**: Improve code quality

## Commands Reference

```bash
# Add dependency
uv add package-name

# Add dev dependency
uv add --dev package-name

# Run tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=src --cov-report=html

# Run linter
uv run ruff check .

# Run formatter
uv run ruff format .

# Run type checker
uv run mypy src
```