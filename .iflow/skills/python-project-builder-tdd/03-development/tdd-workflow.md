# TDD Workflow Guide

## Purpose
This guide explains the Test-Driven Development (TDD) workflow and how to apply it when developing Python features.

## TDD Cycle: Red-Green-Refactor

### 1. Red: Write a Failing Test
- Write a test that defines the desired behavior
- Run the test - it should fail (test doesn't exist or code doesn't implement it)
- This ensures the test is valid and will catch issues

### 2. Green: Make the Test Pass
- Write the minimum code to make the test pass
- Don't worry about perfect code yet - just make it work
- Run the test - it should now pass

### 3. Refactor: Improve the Code
- Improve the code quality while keeping tests passing
- Remove duplication, improve naming, optimize
- Run tests after each refactoring to ensure nothing breaks

### 4. Repeat
- Continue for each feature/behavior
- Build up tests and code incrementally

## TDD Workflow Steps

### Step 1: Understand the Requirement
- Read the feature specification
- Identify the acceptance criteria
- Understand the inputs and expected outputs

### Step 2: Write the First Test
- Choose a simple, testable behavior
- Write a test that describes this behavior
- Use descriptive test names

```python
# test_task_service.py
def test_create_task_with_valid_input():
    """Should create a task with valid input."""
    service = TaskService()
    task = service.create_task("Test task")
    
    assert task.id is not None
    assert task.title == "Test task"
    assert task.status == TaskStatus.PENDING
```

### Step 3: Run the Test (It Should Fail)
```bash
uv run pytest tests/test_task_service.py::test_create_task_with_valid_input
```

Expected result: Test fails (TaskService or create_task doesn't exist)

### Step 4: Implement Minimum Code
- Create the minimum code to make the test pass
- Don't over-engineer

```python
# task_service.py
from src.tasks.models import Task, TaskStatus

class TaskService:
    def create_task(self, title: str) -> Task:
        """Create a new task."""
        return Task(
            id="123",
            title=title,
            status=TaskStatus.PENDING
        )
```

### Step 5: Run the Test (It Should Pass)
```bash
uv run pytest tests/test_task_service.py::test_create_task_with_valid_input
```

Expected result: Test passes

### Step 6: Add More Tests (Edge Cases)
```python
def test_create_task_with_empty_title_should_raise_error():
    """Should raise ValueError when title is empty."""
    service = TaskService()
    
    with pytest.raises(ValueError):
        service.create_task("")

def test_create_task_with_long_title_should_raise_error():
    """Should raise ValueError when title exceeds 200 chars."""
    service = TaskService()
    long_title = "x" * 201
    
    with pytest.raises(ValueError):
        service.create_task(long_title)
```

### Step 7: Implement to Pass All Tests
```python
class TaskService:
    def create_task(self, title: str) -> Task:
        """Create a new task."""
        if not title:
            raise ValueError("Title cannot be empty")
        if len(title) > 200:
            raise ValueError("Title cannot exceed 200 characters")
        
        return Task(
            id=str(uuid.uuid4()),
            title=title,
            status=TaskStatus.PENDING
        )
```

### Step 8: Refactor (If Needed)
- After tests pass, look for improvements
- Keep tests passing while refactoring

```python
class TaskService:
    def __init__(self):
        self._max_title_length = 200
    
    def create_task(self, title: str) -> Task:
        """Create a new task."""
        self._validate_title(title)
        
        return Task(
            id=str(uuid.uuid4()),
            title=title,
            status=TaskStatus.PENDING
        )
    
    def _validate_title(self, title: str) -> None:
        """Validate task title."""
        if not title:
            raise ValueError("Title cannot be empty")
        if len(title) > self._max_title_length:
            raise ValueError(f"Title cannot exceed {self._max_title_length} characters")
```

### Step 9: Repeat for Each Feature
- Continue the cycle for each behavior
- Build comprehensive test coverage

## Test Organization

### Unit Tests
- Test individual functions/methods in isolation
- Mock external dependencies
- Fast execution

```python
def test_task_status_transition_from_pending_to_in_progress():
    """Should allow transition from pending to in_progress."""
    task = Task(id="1", title="Test", status=TaskStatus.PENDING)
    task.transition_to(TaskStatus.IN_PROGRESS)
    
    assert task.status == TaskStatus.IN_PROGRESS
```

### Integration Tests
- Test interactions between components
- Use real dependencies where appropriate
- Slower than unit tests

```python
def test_create_and_retrieve_task():
    """Should create a task and then retrieve it."""
    service = TaskService(repository=InMemoryTaskRepository())
    
    created = service.create_task("Test task")
    retrieved = service.get_task(created.id)
    
    assert retrieved.id == created.id
    assert retrieved.title == "Test task"
```

### End-to-End Tests
- Test complete workflows
- Test through API or CLI
- Slowest but most comprehensive

```python
def test_create_task_via_api():
    """Should create a task through the API."""
    response = client.post("/tasks", json={"title": "Test task"})
    
    assert response.status_code == 201
    assert response.json()["title"] == "Test task"
```

## Running Tests

### Run All Tests
```bash
uv run pytest
```

### Run Specific Test File
```bash
uv run pytest tests/test_task_service.py
```

### Run Specific Test
```bash
uv run pytest tests/test_task_service.py::test_create_task_with_valid_input
```

### Run with Coverage
```bash
uv run pytest --cov=src --cov-report=html
```

### Run with Verbose Output
```bash
uv run pytest -v
```

## Test Naming Conventions

Use descriptive names that explain what is being tested:

```python
# Good
def test_create_task_with_valid_input():
    pass

def test_create_task_with_empty_title_should_raise_error():
    pass

def test_delete_task_that_does_not_exist_should_return_false():
    pass

# Avoid
def test_create_task():
    pass  # What's being tested?

def test_task_creation():
    pass  # Vague
```

## When to Write Tests

### Always Write Tests First (TDD)
- Before writing any implementation code
- For all new features
- For bug fixes (write test that reproduces bug first)

### When Tests Aren't Necessary
- Simple data classes (use type checking instead)
- Configuration constants
- Trivial getters/setters

## Common TDD Mistakes

### 1. Writing Too Much Code Before Testing
- Only write enough code to make the current test pass
- Don't implement multiple features at once

### 2. Skipping the Red Step
- Always run the test before writing implementation
- Ensures the test is valid

### 3. Skipping Refactoring
- Refactor after tests pass
- Don't let technical debt accumulate

### 4. Writing Untestable Code
- Design for testability from the start
- Use dependency injection
- Keep functions small and focused

### 5. Testing Implementation Details
- Test behavior, not implementation
- Focus on inputs and outputs

## TDD Checklist

Before marking a feature as complete:

- [ ] All acceptance criteria have tests
- [ ] All edge cases have tests
- [ ] All tests pass
- [ ] Code has been refactored
- [ ] Coverage is at least 80%
- [ ] No test code is duplicated
- [ ] Tests are fast (unit tests < 1 second)

## Commands Reference

```bash
# Initialize project with pytest
uv add pytest pytest-cov

# Run tests
uv run pytest

# Run with coverage
uv run pytest --cov=src --cov-report=term-missing

# Run specific test
uv run pytest tests/test_module.py::test_function

# Run tests matching pattern
uv run pytest -k "test_create"

# Stop on first failure
uv run pytest -x

# Show print statements
uv run pytest -s
```