# Code Standards Guide

## Purpose
This guide defines the coding standards and conventions to follow when developing Python projects.

## PEP 8 Compliance

Follow PEP 8 (Python Enhancement Proposal 8) for Python code style:

### Indentation
- Use 4 spaces per indentation level
- No tabs

### Line Length
- Maximum 79 characters for code
- Maximum 72 characters for comments/docstrings

### Imports
- Import standard library first
- Import third-party libraries second
- Import local modules third
- Each import on its own line

```python
# Standard library
import os
import sys
from typing import Optional, List

# Third-party
import pytest
from fastapi import FastAPI

# Local
from src.tasks.models import Task
from src.tasks.service import TaskService
```

### Whitespace
- One space around operators
- No spaces inside parentheses/brackets
- Two blank lines before top-level functions
- One blank line before method definitions

### Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| Variables | snake_case | `user_name`, `task_id` |
| Functions | snake_case | `get_user()`, `create_task()` |
| Classes | PascalCase | `UserService`, `TaskManager` |
| Constants | UPPER_SNAKE_CASE | `MAX_RETRIES`, `API_URL` |
| Private | _snake_case | `_internal_method()` |
| Modules | snake_case | `user_service.py`, `task_manager.py` |

```python
# Variables
user_name = "John"
task_list = []

# Functions
def get_user(user_id: str) -> User:
    pass

# Classes
class TaskService:
    def __init__(self):
        self._repository = None

# Constants
MAX_TITLE_LENGTH = 200
DEFAULT_TIMEOUT = 30

# Private methods
def _validate_input(self, data: str) -> bool:
    pass
```

## Type Hints

Use type hints for all function parameters and return values:

```python
from typing import List, Optional, Dict, Any
from dataclasses import dataclass

def get_user(user_id: str) -> Optional[User]:
    """Get user by ID."""
    pass

def create_task(
    title: str,
    description: Optional[str] = None,
    tags: List[str] = []
) -> Task:
    """Create a new task."""
    pass

@dataclass
class Task:
    id: str
    title: str
    description: Optional[str] = None
    tags: List[str] = None
```

## Docstrings

Use Google-style docstrings:

```python
def create_task(title: str, description: Optional[str] = None) -> Task:
    """Create a new task.
    
    Args:
        title: The task title (required).
        description: Optional task description.
        
    Returns:
        The created Task object.
        
    Raises:
        ValidationError: If title is invalid.
        
    Example:
        >>> task = create_task("My task", "Do something")
        >>> print(task.title)
        My task
    """
    pass

class TaskService:
    """Service for managing tasks.
    
    This service provides methods for creating, updating, and deleting tasks.
    """
    
    def __init__(self, repository: TaskRepository):
        """Initialize the TaskService.
        
        Args:
            repository: The task repository instance.
        """
        self._repository = repository
```

## Error Handling

### Define Custom Exceptions
```python
class TaskError(Exception):
    """Base exception for task-related errors."""
    pass

class ValidationError(TaskError):
    """Raised when validation fails."""
    pass

class NotFoundError(TaskError):
    """Raised when a resource is not found."""
    pass
```

### Use Specific Exceptions
```python
# Good
try:
    task = repository.find_by_id(task_id)
except DatabaseError as e:
    logger.error(f"Database error: {e}")
    raise TaskError("Failed to retrieve task") from e

# Avoid
try:
    task = repository.find_by_id(task_id)
except Exception as e:
    raise  # Too broad
```

### Handle Expected Errors
```python
def get_task(task_id: str) -> Task:
    """Get task by ID."""
    task = repository.find_by_id(task_id)
    
    if task is None:
        raise NotFoundError(f"Task with ID {task_id} not found")
    
    return task
```

## Code Organization

### File Structure
```
src/
├── __init__.py
├── models.py          # Data models
├── service.py         # Business logic
├── repository.py      # Data access
└── exceptions.py      # Custom exceptions
```

### Module Exports
```python
# __init__.py - Export only public API
from .models import Task, TaskStatus
from .service import TaskService, create_task
from .exceptions import TaskError, ValidationError

__all__ = [
    "Task",
    "TaskStatus",
    "TaskService",
    "create_task",
    "TaskError",
    "ValidationError",
]
```

## Best Practices

### 1. Single Responsibility
Each function/class should do one thing well:

```python
# Good
def validate_title(title: str) -> str:
    """Validate and sanitize title."""
    if not title:
        raise ValidationError("Title required")
    return title.strip()

def create_task(title: str) -> Task:
    """Create a task."""
    validated_title = validate_title(title)
    return Task(title=validated_title)

# Avoid
def create_task(title: str) -> Task:
    """Create a task (does too much)."""
    if not title:
        raise ValidationError("Title required")
    sanitized = title.strip()
    # ... more logic mixed in
    return Task(title=sanitized)
```

### 2. DRY (Don't Repeat Yourself)
Extract common logic:

```python
# Good
def validate_string(value: str, field_name: str, min_length: int = 1) -> str:
    """Validate a string field."""
    if not value:
        raise ValidationError(f"{field_name} is required")
    if len(value) < min_length:
        raise ValidationError(f"{field_name} must be at least {min_length} characters")
    return value.strip()

# Avoid
def validate_title(title: str) -> str:
    if not title:
        raise ValidationError("Title required")
    return title.strip()

def validate_description(description: str) -> str:
    if not description:
        raise ValidationError("Description required")
    return description.strip()
```

### 3. Early Returns
Return early to reduce nesting:

```python
# Good
def process_task(task: Optional[Task]) -> Result:
    if task is None:
        return Result.error("Task not found")
    
    if not task.is_active:
        return Result.error("Task is inactive")
    
    return Result.success(process(task))

# Avoid
def process_task(task: Optional[Task]) -> Result:
    if task is not None:
        if task.is_active:
            return Result.success(process(task))
        else:
            return Result.error("Task is inactive")
    else:
        return Result.error("Task not found")
```

### 4. Use Context Managers
For resource management:

```python
# Good
with open("file.txt", "r") as f:
    content = f.read()

# For database connections
with db.session() as session:
    session.add(task)
    session.commit()

# Avoid
f = open("file.txt", "r")
content = f.read()
f.close()  # Risk of not closing
```

### 5. Use List Comprehensions
For simple transformations:

```python
# Good
titles = [task.title for task in tasks if task.completed]

# Avoid
titles = []
for task in tasks:
    if task.completed:
        titles.append(task.title)
```

### 6. Use f-strings
For string formatting:

```python
# Good
message = f"User {user.name} has {len(tasks)} tasks"

# Avoid
message = "User {} has {} tasks".format(user.name, len(tasks))
```

### 7. Use Data Classes
For data containers:

```python
# Good
@dataclass
class Task:
    id: str
    title: str
    status: TaskStatus

# Avoid
class Task:
    def __init__(self, id: str, title: str, status: TaskStatus):
        self.id = id
        self.title = title
        self.status = status
```

## Security Best Practices

### 1. Never Hardcode Secrets
```python
# Good
import os
api_key = os.getenv("API_KEY")

# Avoid
api_key = "sk-1234567890abcdef"
```

### 2. Validate Input
```python
def create_user(email: str, password: str) -> User:
    validate_email(email)
    validate_password_strength(password)
    # ...
```

### 3. Use Parameterized Queries
```python
# Good
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))

# Avoid
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")  # SQL injection risk
```

### 4. Sanitize Output
```python
# Good
from html import escape
safe_output = escape(user_input)

# Avoid
output = user_input  # XSS risk
```

## Performance Considerations

### 1. Use Generators for Large Data
```python
# Good
def process_large_file(filename: str):
    with open(filename) as f:
        for line in f:
            yield process_line(line)

# Avoid
def read_large_file(filename: str) -> List[str]:
    with open(filename) as f:
        return f.readlines()  # Loads entire file into memory
```

### 2. Cache Expensive Operations
```python
from functools import lru_cache

@lru_cache(maxsize=128)
def get_user(user_id: str) -> User:
    return repository.find_by_id(user_id)
```

### 3. Use Sets for Lookups
```python
# Good
valid_ids = {task.id for task in tasks}
if task_id in valid_ids:
    # O(1) lookup

# Avoid
task_ids = [task.id for task in tasks]
if task_id in task_ids:
    # O(n) lookup
```

## Tools and Linting

### Required Tools
```bash
# Add to project
uv add --dev ruff black mypy pytest pytest-cov
```

### Ruff (Linter)
```bash
# Check code
uv run ruff check .

# Fix issues automatically
uv run ruff check . --fix
```

### Black (Formatter)
```bash
# Format code
uv run black .

# Check formatting
uv run black --check .
```

### MyPy (Type Checker)
```bash
# Check types
uv run mypy src
```

### Pre-commit Hook
Create `.pre-commit-config.yaml`:
```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.0
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.7.0
    hooks:
      - id: mypy
```

## Review Checklist

Before committing code:

- [ ] Code follows PEP 8
- [ ] Type hints present for all functions
- [ ] Docstrings for all public functions/classes
- [ ] No hardcoded secrets
- [ ] Input validation present
- [ ] Error handling appropriate
- [ ] No code duplication
- [ ] Tests written and passing
- [ ] Coverage at least 80%
- [ ] Linter passes (ruff check)
- [ ] Formatter passes (black)
- [ ] Type checker passes (mypy)