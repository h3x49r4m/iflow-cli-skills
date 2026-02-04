# Edge Cases Guide

## Purpose
This guide explains how to identify and test edge cases to ensure robust code.

## What Are Edge Cases?

Edge cases are situations that occur at the extreme ends of operating ranges, boundary conditions, or unusual inputs that may not be immediately obvious but can cause bugs.

## Categories of Edge Cases

### 1. Boundary Values
Values at the minimum or maximum limits of valid ranges.

#### Examples
- **String Length**: Empty string, maximum length string
- **Numeric Values**: Zero, negative, maximum, minimum
- **Array/List**: Empty, single element, maximum size
- **Date/Time**: Minimum date, maximum date, leap year, timezone boundaries

#### Testing Boundary Values
```python
def test_task_title_boundary_values():
    """Test task creation with boundary title lengths."""
    service = TaskService()
    
    # Minimum valid length (1 character)
    task_min = service.create_task("A")
    assert task_min.title == "A"
    
    # Maximum valid length (200 characters)
    max_title = "x" * 200
    task_max = service.create_task(max_title)
    assert task_max.title == max_title
    
    # Just over maximum (201 characters)
    too_long = "x" * 201
    with pytest.raises(ValidationError):
        service.create_task(too_long)
```

### 2. Empty and Null Values
Inputs that are empty, None, or contain no meaningful data.

#### Examples
- **Empty String**: `""`
- **None**: `None`
- **Empty List**: `[]`
- **Empty Dict**: `{}`
- **Whitespace Only**: `"   "`

#### Testing Empty Values
```python
def test_create_task_with_empty_values():
    """Test task creation with empty values."""
    service = TaskService()
    
    # Empty string
    with pytest.raises(ValidationError):
        service.create_task("")
    
    # None
    with pytest.raises(ValidationError):
        service.create_task(None)
    
    # Whitespace only
    with pytest.raises(ValidationError):
        service.create_task("   ")
    
    # Empty description (should be OK if optional)
    task = service.create_task("Valid title", description="")
    assert task.description == ""
```

### 3. Type Mismatches
Inputs of incorrect data types.

#### Examples
- **String instead of Number**: `"123"` instead of `123`
- **Number instead of String**: `123` instead of `"123"`
- **List instead of String**: `["item"]` instead of `"item"`
- **Dict instead of Object**: `{"key": "value"}` instead of object

#### Testing Type Mismatches
```python
def test_create_task_with_type_mismatches():
    """Test task creation with incorrect types."""
    service = TaskService()
    
    # Number instead of string
    with pytest.raises(TypeError):
        service.create_task(123)
    
    # List instead of string
    with pytest.raises(TypeError):
        service.create_task(["title"])
    
    # Dict instead of string
    with pytest.raises(TypeError):
        service.create_task({"title": "value"})
```

### 4. Special Characters
Inputs containing special or unusual characters.

#### Examples
- **Unicode Characters**: 中文, 🎉, é, ñ
- **HTML/Script Tags**: `<script>alert('xss')</script>`
- **SQL Injection**: `' OR '1'='1`
- **Control Characters**: `\n`, `\t`, `\r`
- **Path Traversal**: `../../../etc/passwd`

#### Testing Special Characters
```python
def test_create_task_with_special_characters():
    """Test task creation with special characters."""
    service = TaskService()
    
    # Unicode characters
    task_unicode = service.create_task("中文标题 🎉")
    assert task_unicode.title == "中文标题 🎉"
    
    # Special symbols
    task_symbols = service.create_task("Task with <special> & characters!")
    assert task_symbols.title == "Task with <special> & characters!"
    
    # Newlines and tabs
    task_whitespace = service.create_task("Line1\nLine2\tTab")
    assert "Line1" in task_whitespace.title
    
    # Verify no XSS (sanitized)
    task_xss = service.create_task("<script>alert('xss')</script>")
    assert "<script>" not in task_xss.title  # Should be sanitized
```

### 5. Large Values
Inputs that are unusually large or long.

#### Examples
- **Large Numbers**: Very large integers, floating point overflow
- **Large Strings**: Very long strings, memory issues
- **Large Lists**: Very large lists, performance issues
- **Large Files**: Very large file uploads

#### Testing Large Values
```python
def test_create_task_with_large_values():
    """Test task creation with large values."""
    service = TaskService()
    
    # Large description (should be allowed up to limit)
    large_description = "x" * 1000
    task = service.create_task("Title", description=large_description)
    assert len(task.description) == 1000
    
    # Very large description (should fail if exceeds limit)
    too_large = "x" * 10001
    with pytest.raises(ValidationError):
        service.create_task("Title", description=too_large)
```

### 6. Concurrent Access
Multiple operations happening simultaneously.

#### Examples
- **Race Conditions**: Two users updating same resource
- **Deadlocks**: Two operations waiting for each other
- **Data Corruption**: Concurrent writes to same data

#### Testing Concurrent Access
```python
import threading

def test_concurrent_task_creation():
    """Test concurrent task creation."""
    service = TaskService()
    results = []
    
    def create_task_task(title):
        try:
            task = service.create_task(title)
            results.append(task.id)
        except Exception as e:
            results.append(str(e))
    
    # Create tasks concurrently
    threads = [
        threading.Thread(target=create_task_task, args=(f"Task{i}",))
        for i in range(10)
    ]
    
    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()
    
    # All tasks should be created successfully
    assert len(results) == 10
    assert all(isinstance(r, str) for r in results)
```

### 7. Network Issues
Problems with network connectivity.

#### Examples
- **Timeouts**: Operations taking too long
- **Connection Errors**: Unable to connect
- **Rate Limiting**: Too many requests
- **Partial Responses**: Incomplete data received

#### Testing Network Issues
```python
from unittest.mock import patch
import requests

def test_task_service_with_network_timeout():
    """Test task service handles network timeout."""
    with patch('src.tasks.repository.requests.get') as mock_get:
        mock_get.side_effect = requests.Timeout("Connection timeout")
        
        service = TaskService()
        
        with pytest.raises(TaskError, match="timeout"):
            service.fetch_external_task("123")

def test_task_service_with_rate_limit():
    """Test task service handles rate limiting."""
    with patch('src.tasks.repository.requests.post') as mock_post:
        mock_post.return_value.status_code = 429
        mock_post.return_value.json.return_value = {"error": "Rate limit exceeded"}
        
        service = TaskService()
        
        with pytest.raises(RateLimitError):
            service.sync_task("123")
```

### 8. Database Issues
Problems with database operations.

#### Examples
- **Connection Lost**: Database connection drops
- **Deadlocks**: Database deadlocks
- **Constraint Violations**: Unique constraint, foreign key violations
- **Transaction Failures**: Rollback on error

#### Testing Database Issues
```python
def test_task_service_with_database_error():
    """Test task service handles database errors."""
    mock_repo = Mock()
    mock_repo.save.side_effect = DatabaseError("Connection lost")
    
    service = TaskService(mock_repo)
    
    with pytest.raises(TaskError, match="database"):
        service.create_task("Test task")

def test_task_service_with_constraint_violation():
    """Test task service handles constraint violations."""
    mock_repo = Mock()
    mock_repo.save.side_effect = IntegrityError("Duplicate key")
    
    service = TaskService(mock_repo)
    
    with pytest.raises(ValidationError, match="already exists"):
        service.create_task("Duplicate task")
```

### 9. Date and Time Edge Cases
Issues with dates, times, and timezones.

#### Examples
- **Leap Years**: February 29th
- **Timezone Changes**: DST transitions
- **Date Boundaries**: Midnight, end of month/year
- **Invalid Dates**: February 30th

#### Testing Date/Time Edge Cases
```python
from datetime import datetime, timezone

def test_task_with_date_boundaries():
    """Test task creation with date boundaries."""
    service = TaskService()
    
    # Midnight
    midnight = datetime(2026, 1, 1, 0, 0, 0)
    task = service.create_task("Test", due_date=midnight)
    assert task.due_date == midnight
    
    # End of year
    end_of_year = datetime(2026, 12, 31, 23, 59, 59)
    task = service.create_task("Test", due_date=end_of_year)
    assert task.due_date == end_of_year
    
    # Leap year
    leap_day = datetime(2024, 2, 29)
    task = service.create_task("Test", due_date=leap_day)
    assert task.due_date == leap_day
    
    # Invalid date (should fail)
    with pytest.raises(ValidationError):
        service.create_task("Test", due_date=datetime(2026, 2, 30))
```

### 10. Invalid States
Objects or data in unexpected states.

#### Examples
- **Already Deleted**: Operating on deleted resource
- **Already Completed**: Operating on completed task
- **Wrong Status**: Transition not allowed
- **Missing Dependencies**: Required data missing

#### Testing Invalid States
```python
def test_task_operations_on_deleted_task():
    """Test operations on deleted task."""
    service = TaskService()
    task = service.create_task("Test")
    
    # Delete the task
    service.delete_task(task.id)
    
    # Try to update deleted task
    with pytest.raises(NotFoundError):
        service.update_task(task.id, "Updated")

def test_invalid_status_transitions():
    """Test invalid status transitions."""
    service = TaskService()
    task = service.create_task("Test")
    
    # Can't go from COMPLETED to PENDING
    task.status = TaskStatus.COMPLETED
    with pytest.raises(ValidationError, match="invalid transition"):
        service.update_task_status(task.id, TaskStatus.PENDING)
```

## Edge Case Testing Checklist

For each feature, test these edge cases:

### Where to Write Edge Case Tests

- **Unit Tests (`tests/unit/`)**: Write edge case tests for individual functions and methods
  - Test boundary values for function parameters
  - Test type mismatches in function arguments
  - Test empty/null values in function inputs
  - Test special characters in string inputs
  - Test error handling in individual functions

- **Integration Tests (`tests/integration/`)**: Write edge case tests for component interactions
  - Test concurrent access to shared resources
  - Test network issues in component communication
  - Test database issues in data persistence
  - Test invalid state transitions across components

- **E2E Tests (`tests/e2e/`)**: Write edge case tests for complete workflows
  - Test complete workflows with edge case inputs
  - Test authentication/authorization edge cases
  - Test rate limiting and throttling
  - Test timeout scenarios in full workflows

### Edge Case Types to Test

### Input Validation
- [ ] Empty values (None, empty string, empty list)
- [ ] Boundary values (min, max, min-1, max+1)
- [ ] Type mismatches (wrong types)
- [ ] Special characters (unicode, symbols, HTML)
- [ ] Whitespace (leading, trailing, multiple)

### Data Size
- [ ] Very small values (0, 1, empty)
- [ ] Very large values (near limits, over limits)
- [ ] Exactly at limits (boundary values)
- [ ] Just under/over limits

### Data Content
- [ ] Unicode and special characters
- [ ] Malicious input (XSS, SQL injection)
- [ ] Invalid formats (email, URL, date)
- [ ] Duplicate values

### State and Dependencies
- [ ] Operating on non-existent resources
- [ ] Invalid state transitions
- [ ] Missing dependencies
- [ ] Circular dependencies

### Concurrency and Performance
- [ ] Concurrent operations
- [ ] Race conditions
- [ ] Resource exhaustion
- [ ] Timeout scenarios

### External Dependencies
- [ ] Network failures
- [ ] Service unavailable
- [ ] Rate limiting
- [ ] Partial responses

### Database and Storage
- [ ] Connection errors
- [ ] Constraint violations
- [ ] Transaction failures
- [ ] Lock contention

### Time and Dates
- [ ] Leap years
- [ ] Timezone issues
- [ ] DST transitions
- [ ] Date boundaries

## Edge Case Testing Tools

### Property-Based Testing
Use `hypothesis` to find edge cases automatically:

```bash
uv add --dev hypothesis
```

```python
from hypothesis import given, strategies as st

@given(st.text(min_size=1, max_size=200))
def test_task_title_with_random_strings(title):
    """Test task creation with random strings."""
    service = TaskService()
    task = service.create_task(title)
    
    assert task.title == title
    assert len(task.title) <= 200

@given(st.integers(min_value=1, max_value=200))
def test_task_title_with_random_lengths(length):
    """Test task creation with random title lengths."""
    service = TaskService()
    title = "x" * length
    task = service.create_task(title)
    
    assert len(task.title) == length
```

### Fuzz Testing
Use `afl` or similar for fuzz testing:

```bash
uv add --dev fuzz
```

## Best Practices

1. **Identify Early**: Identify edge cases during design
2. **Document**: Document expected edge case behavior
3. **Test Thoroughly**: Write comprehensive edge case tests
4. **Handle Gracefully**: Fail gracefully, don't crash
5. **Provide Feedback**: Give clear error messages
6. **Monitor**: Monitor production for unexpected edge cases
7. **Learn**: Update tests when new edge cases are found

## Example: Complete Edge Case Test Suite

```python
class TestTaskCreationEdgeCases:
    """Edge case tests for task creation."""
    
    # Boundary values
    def test_minimum_length_title(self):
        pass
    
    def test_maximum_length_title(self):
        pass
    
    def test_exceeds_maximum_length(self):
        pass
    
    # Empty/null values
    def test_empty_string_title(self):
        pass
    
    def test_none_title(self):
        pass
    
    def test_whitespace_only_title(self):
        pass
    
    # Special characters
    def test_unicode_title(self):
        pass
    
    def test_html_in_title(self):
        pass
    
    def test_sql_injection_attempt(self):
        pass
    
    # Type mismatches
    def test_numeric_title(self):
        pass
    
    def test_list_as_title(self):
        pass
    
    # Large values
    def test_very_long_description(self):
        pass
    
    def test_exceeds_description_limit(self):
        pass
    
    # Date edge cases
    def test_midnight_due_date(self):
        pass
    
    def test_leap_year_due_date(self):
        pass
    
    def test_invalid_date(self):
        pass
```