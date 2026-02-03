# Module Design Guide

## Purpose
This guide explains how to design the module structure for a Python project, ensuring clean separation of concerns and maintainability.

## Module Design Principles

### 1. Single Responsibility Principle
Each module should have one clear responsibility.
- Modules should be cohesive (related functionality together)
- Modules should be loosely coupled (minimal dependencies between modules)

### 2. Layered Architecture
Organize modules into logical layers:
```
├── src/
│   ├── __init__.py
│   ├── models/           # Data models and schemas
│   ├── services/         # Business logic
│   ├── repositories/     # Data access (database, file, API)
│   ├── api/              # External interfaces (REST, CLI)
│   └── utils/            # Shared utilities
```

### 3. Feature-Based Organization
For feature-oriented projects, organize by feature:
```
├── src/
│   ├── __init__.py
│   ├── auth/             # Authentication feature
│   ├── users/            # User management feature
│   ├── tasks/            # Task management feature
│   └── common/           # Shared code across features
```

## Module Design Process

### Step 1: Identify Core Domains
Based on features, identify core domains/subsystems:
- What are the main subject areas?
- What are the key entities?
- What are the main operations?

### Step 2: Define Module Boundaries
Group related functionality into modules:
- Functions/classes that work together → same module
- Independent functionality → separate modules
- Shared functionality → common/utilities module

### Step 3: Define Module Interfaces
For each module, define:
- **Public API**: What it exposes to other modules
- **Dependencies**: What it needs from other modules
- **Data Models**: What data structures it uses

### Step 4: Design Internal Structure
For each module, design internal organization:
- Classes and their relationships
- Functions and their responsibilities
- Helper functions vs main API

### Step 5: Validate Design
Check that the design:
- Supports all required features
- Avoids circular dependencies
- Is testable in isolation
- Is maintainable and extensible

## Module Structure Template

```python
# src/<module_name>/
# ├── __init__.py          # Public API exports
# ├── models.py            # Data models
# ├── service.py           # Business logic
# ├── repository.py        # Data access (if needed)
# └── exceptions.py        # Module-specific exceptions
```

### __init__.py
Export only the public API:
```python
"""Module description."""

from .models import ModelA, ModelB
from .service import function_a, ClassB

__all__ = ["ModelA", "ModelB", "function_a", "ClassB"]
```

### models.py
Define data structures:
```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class ModelA:
    """Description of ModelA."""
    field1: str
    field2: int
    field3: Optional[str] = None
```

### service.py
Implement business logic:
```python
from typing import List
from .models import ModelA
from .exceptions import ValidationError

def function_a(input: str) -> ModelA:
    """Process input and return ModelA."""
    # Validation
    if not input:
        raise ValidationError("Input cannot be empty")
    
    # Business logic
    result = process(input)
    
    return result

def process(input: str) -> ModelA:
    """Internal helper function."""
    # Implementation
    pass
```

### exceptions.py
Define module-specific exceptions:
```python
class ModuleError(Exception):
    """Base exception for this module."""
    pass

class ValidationError(ModuleError):
    """Raised when validation fails."""
    pass

class NotFoundError(ModuleError):
    """Raised when resource is not found."""
    pass
```

## Dependency Guidelines

### Internal Dependencies
- Import only what you need from other modules
- Prefer importing the public API from `__init__.py`
- Avoid circular dependencies

### External Dependencies
- Document required packages in `pyproject.toml`
- Use version constraints
- Consider alternatives to minimize dependencies

### Example
```python
# Good: Import from public API
from src.users.models import User
from src.users.service import create_user

# Avoid: Import from internal modules
from src.users.repository import UserRepository  # Not exposed in __init__.py
```

## Module Communication Patterns

### 1. Direct Function Calls
Simple cases where one module calls another:
```python
# In module A
from module_b import process_data

result = process_data(input_data)
```

### 2. Dependency Injection
For testability and loose coupling:
```python
class ServiceA:
    def __init__(self, repository: RepositoryInterface):
        self.repository = repository
    
    def process(self, data):
        return self.repository.save(data)
```

### 3. Event-Based (Optional)
For decoupled modules:
```python
from src.common.events import emit, subscribe

@subscribe("user.created")
def handle_user_created(event):
    # Handle user creation in another module
    pass

# Emit event
emit("user.created", user_data)
```

## Module Documentation

Each module should have:
1. **Module docstring**: What the module does
2. **Function docstrings**: What each function does, parameters, returns
3. **Type hints**: For all function parameters and returns
4. **Examples**: Usage examples in docstrings

## Example: Todo App Module Design

```
src/
├── __init__.py
├── tasks/
│   ├── __init__.py
│   ├── models.py          # Task model
│   ├── service.py         # Task business logic
│   ├── repository.py      # Task storage
│   └── exceptions.py      # Task exceptions
├── users/
│   ├── __init__.py
│   ├── models.py          # User model
│   ├── service.py         # User business logic
│   └── exceptions.py      # User exceptions
└── common/
    ├── __init__.py
    ├── events.py          # Event system
    └── validators.py      # Shared validators
```

## Best Practices

1. **Keep modules small**: 200-500 lines per module
2. **Clear naming**: Module names should be descriptive
3. **Minimize imports**: Import only what you need
4. **Avoid god modules**: Don't put everything in one module
5. **Test independently**: Each module should be testable in isolation
6. **Document boundaries**: Clearly document what's public vs private