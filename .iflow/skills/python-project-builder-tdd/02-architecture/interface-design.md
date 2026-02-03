# Interface Design Guide

## Purpose
This guide explains how to design clean, well-defined interfaces for modules, features, and external APIs.

## Interface Design Principles

### 1. Clear Contracts
Interfaces should define clear contracts:
- What inputs are accepted
- What outputs are returned
- What errors can be raised
- What side effects occur

### 2. Minimal and Focused
Interfaces should be:
- Minimal: Only expose what's needed
- Focused: Each interface has one purpose
- Coherent: Related functions grouped together

### 3. Type Safety
Use type hints for all interfaces:
- Parameter types
- Return types
- Custom types for domain concepts

### 4. Error Handling
Define clear error handling:
- What exceptions can be raised
- When each exception is raised
- What information exceptions contain

## Interface Types

### 1. Function Interfaces
Simple function signatures with clear contracts:

```python
from typing import List, Optional
from .models import Task, TaskFilter

def get_tasks(filter: Optional[TaskFilter] = None) -> List[Task]:
    """
    Retrieve tasks based on optional filter criteria.
    
    Args:
        filter: Optional filter criteria for tasks
        
    Returns:
        List of tasks matching the filter, or all tasks if no filter
        
    Raises:
        DatabaseError: If database query fails
    """
    pass
```

### 2. Class Interfaces
Classes with well-defined methods:

```python
from abc import ABC, abstractmethod

class TaskRepository(ABC):
    """Abstract interface for task storage operations."""
    
    @abstractmethod
    def save(self, task: Task) -> Task:
        """Save a task and return the saved task."""
        pass
    
    @abstractmethod
    def find_by_id(self, task_id: str) -> Optional[Task]:
        """Find a task by ID, or None if not found."""
        pass
    
    @abstractmethod
    def find_all(self) -> List[Task]:
        """Find all tasks."""
        pass
    
    @abstractmethod
    def delete(self, task_id: str) -> bool:
        """Delete a task by ID, return True if deleted."""
        pass
```

### 3. Data Transfer Objects (DTOs)
Structured data for passing between layers:

```python
from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class CreateTaskRequest:
    """Request to create a new task."""
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None

@dataclass
class TaskResponse:
    """Response with task data."""
    id: str
    title: str
    description: Optional[str]
    status: str
    created_at: datetime
    due_date: Optional[datetime]
```

### 4. API Endpoints (if REST API)
RESTful API interface definitions:

```python
from fastapi import APIRouter, HTTPException
from typing import List

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("/", response_model=TaskResponse, status_code=201)
async def create_task(request: CreateTaskRequest) -> TaskResponse:
    """
    Create a new task.
    
    Returns:
        TaskResponse: The created task
        
    Raises:
        HTTPException(400): If validation fails
    """
    pass

@router.get("/", response_model=List[TaskResponse])
async def list_tasks(status: Optional[str] = None) -> List[TaskResponse]:
    """
    List all tasks, optionally filtered by status.
    
    Args:
        status: Optional status filter (pending, in_progress, completed)
        
    Returns:
        List of tasks
    """
    pass
```

## Interface Documentation Template

```python
def function_name(
    param1: Type1,
    param2: Type2,
    optional_param: Optional[Type3] = None
) -> ReturnType:
    """
    Brief description of what the function does.
    
    More detailed description if needed.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        optional_param: Description of optional_param, defaults to None
        
    Returns:
        Description of return value
        
    Raises:
        ExceptionType: Description of when this exception is raised
        AnotherException: Description of when this exception is raised
        
    Examples:
        >>> result = function_name("value1", "value2")
        >>> print(result)
        expected output
    """
    pass
```

## Interface Design Process

### Step 1: Identify Interfaces
For each feature/module, identify:
- What operations are needed?
- What data is exchanged?
- What errors can occur?

### Step 2: Define Signatures
Create function/method signatures with:
- Descriptive names
- Type hints
- Parameter descriptions

### Step 3: Define Data Structures
Create DTOs/models for:
- Input data
- Output data
- Internal data

### Step 4: Define Errors
Create exception types for:
- Validation errors
- Not found errors
- Permission errors
- System errors

### Step 5: Document Contracts
Write clear documentation for:
- Preconditions (what must be true before calling)
- Postconditions (what is true after calling)
- Invariants (what remains true)

### Step 6: Validate Design
Check that interfaces are:
- Clear and understandable
- Complete (cover all use cases)
- Minimal (no unnecessary parameters)
- Consistent with other interfaces

## Interface Evolution Guidelines

### Versioning
When changing interfaces:
- Add new functions/methods (don't remove)
- Deprecate old interfaces gracefully
- Use semantic versioning

### Backward Compatibility
Maintain compatibility when possible:
- Use optional parameters for additions
- Use default values for new fields
- Provide migration guides

## Best Practices

1. **Use Type Hints**: All parameters and returns
2. **Write Docstrings**: Clear, complete documentation
3. **Validate Inputs**: Validate at interface boundaries
4. **Handle Errors Gracefully**: meaningful error messages
5. **Keep Interfaces Stable**: Don't change frequently
6. **Provide Examples**: Show how to use the interface
7. **Test Interfaces**: Unit tests for each interface

## Example: Task Service Interface

```python
from typing import List, Optional
from src.tasks.models import Task, TaskStatus
from src.tasks.exceptions import TaskNotFound, InvalidTaskStatus

class TaskService:
    """Service interface for task operations."""
    
    def create_task(
        self,
        title: str,
        description: Optional[str] = None,
        due_date: Optional[datetime] = None
    ) -> Task:
        """
        Create a new task.
        
        Args:
            title: Task title (required, max 200 chars)
            description: Optional task description
            due_date: Optional due date
            
        Returns:
            The created task with generated ID
            
        Raises:
            ValueError: If title is empty or too long
        """
        pass
    
    def get_task(self, task_id: str) -> Task:
        """
        Retrieve a task by ID.
        
        Args:
            task_id: The task ID to retrieve
            
        Returns:
            The task
            
        Raises:
            TaskNotFound: If task with ID doesn't exist
        """
        pass
    
    def list_tasks(
        self,
        status: Optional[TaskStatus] = None,
        limit: int = 100
    ) -> List[Task]:
        """
        List tasks, optionally filtered by status.
        
        Args:
            status: Optional status filter
            limit: Maximum number of tasks to return (default 100, max 1000)
            
        Returns:
            List of tasks matching criteria
        """
        pass
    
    def update_task_status(
        self,
        task_id: str,
        new_status: TaskStatus
    ) -> Task:
        """
        Update a task's status.
        
        Args:
            task_id: The task ID to update
            new_status: The new status
            
        Returns:
            The updated task
            
        Raises:
            TaskNotFound: If task doesn't exist
            InvalidTaskStatus: If status transition is invalid
        """
        pass
    
    def delete_task(self, task_id: str) -> bool:
        """
        Delete a task.
        
        Args:
            task_id: The task ID to delete
            
        Returns:
            True if task was deleted, False if not found
        """
        pass
```