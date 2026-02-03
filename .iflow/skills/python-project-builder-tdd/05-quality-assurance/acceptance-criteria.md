# Acceptance Criteria Guide

## Purpose
This guide explains how to define and verify acceptance criteria for features to ensure they meet business requirements.

## What Are Acceptance Criteria?

Acceptance criteria are conditions that a feature must satisfy to be accepted by the product owner, user, or other stakeholder. They define the scope of a feature and provide clear testable conditions.

## Acceptance Criteria Format

### Given-When-Then Format (Gherkin)

```
Given [precondition]
When [action]
Then [expected outcome]
```

### Example
```
Given a user is logged in
When the user creates a task with a valid title
Then the task is created with a unique ID and PENDING status
```

## Writing Acceptance Criteria

### 1. Make Them Testable
Each criterion must be verifiable through testing.

**Good**:
- [ ] User can create a task with a title between 1 and 200 characters
- [ ] System returns a 201 status code when task is created successfully

**Bad**:
- [ ] System should be user-friendly (not testable)
- [ ] System should perform well (too vague)

### 2. Make Them Specific
Each criterion should describe a specific behavior.

**Good**:
- [ ] Task title cannot be empty
- [ ] Task title cannot exceed 200 characters

**Bad**:
- [ ] Task title should be validated (too vague)

### 3. Make Them Measurable
Each criterion should have a clear pass/fail condition.

**Good**:
- [ ] Response time for task creation is less than 100ms
- [ ] System can handle 100 concurrent task creation requests

**Bad**:
- [ ] System should be fast (not measurable)

### 4. Cover All Scenarios
Include happy path, error paths, and edge cases.

**Scenarios to Cover**:
- Happy path: Everything works as expected
- Error path: Invalid inputs, errors occur
- Edge cases: Boundary values, unusual inputs
- Security: Authentication, authorization
- Performance: Response times, throughput

## Acceptance Criteria Template

Use this template for each feature.

---

## Feature: [Feature Name]

### Description
[Brief description of the feature]

### User Story
As a [type of user]
I want [to perform an action]
So that [I can achieve a goal]

### Acceptance Criteria

#### AC1: [Criterion Title]
**Given**: [Precondition]
**When**: [Action]
**Then**: [Expected outcome]

**Test**: [Test name that verifies this criterion]
**Status**: ✅/❌

---

#### AC2: [Criterion Title]
**Given**: [Precondition]
**When**: [Action]
**Then**: [Expected outcome]

**Test**: [Test name that verifies this criterion]
**Status**: ✅/❌

---

### Verification Summary
- **Total Criteria**: __
- **Passed**: __
- **Failed**: __
- **Overall Status**: ✅/❌

---

## Example: Create Task Feature

## Feature: Create Task

### Description
Allow users to create new tasks with a title and optional description.

### User Story
As a user
I want to create tasks
So that I can track my work

### Acceptance Criteria

#### AC1: Create Task with Valid Title
**Given**: A user is authenticated
**When**: The user creates a task with a title between 1 and 200 characters
**Then**: The task is created with a unique ID, the provided title, PENDING status, and current timestamp

**Test**: `test_create_task_with_valid_title`
**Status**: ✅

---

#### AC2: Reject Empty Title
**Given**: A user is authenticated
**When**: The user attempts to create a task with an empty title
**Then**: The system returns a 400 error with message "Title cannot be empty"

**Test**: `test_create_task_with_empty_title_raises_error`
**Status**: ✅

---

#### AC3: Reject Title Exceeding 200 Characters
**Given**: A user is authenticated
**When**: The user attempts to create a task with a title exceeding 200 characters
**Then**: The system returns a 400 error with message "Title cannot exceed 200 characters"

**Test**: `test_create_task_with_long_title_raises_error`
**Status**: ✅

---

#### AC4: Accept Optional Description
**Given**: A user is authenticated
**When**: The user creates a task with a title and description
**Then**: The task is created with both title and description saved

**Test**: `test_create_task_with_description`
**Status**: ✅

---

#### AC5: Handle Whitespace in Title
**Given**: A user is authenticated
**When**: The user creates a task with a title containing leading/trailing whitespace
**Then**: The whitespace is trimmed before saving

**Test**: `test_create_task_trims_whitespace`
**Status**: ✅

---

#### AC6: Response Time Requirement
**Given**: A user is authenticated
**When**: The user creates a task
**Then**: The system responds within 100ms

**Test**: `test_create_task_response_time`
**Status**: ✅

---

### Verification Summary
- **Total Criteria**: 6
- **Passed**: 6
- **Failed**: 0
- **Overall Status**: ✅

---

## Mapping Tests to Acceptance Criteria

For each acceptance criterion, ensure there's a corresponding test.

| AC | Description | Test | Status |
|----|-------------|------|--------|
| AC1 | Create task with valid title | `test_create_task_with_valid_title` | ✅ |
| AC2 | Reject empty title | `test_create_task_with_empty_title_raises_error` | ✅ |
| AC3 | Reject long title | `test_create_task_with_long_title_raises_error` | ✅ |
| AC4 | Accept optional description | `test_create_task_with_description` | ✅ |
| AC5 | Handle whitespace | `test_create_task_trims_whitespace` | ✅ |
| AC6 | Response time requirement | `test_create_task_response_time` | ✅ |

## Acceptance Criteria Types

### Functional Criteria
Describe what the feature does.

**Examples**:
- User can create a task
- System validates input
- Error messages are clear

### Non-Functional Criteria
Describe how the feature performs.

**Examples**:
- Response time < 100ms
- System handles 100 concurrent users
- Data is encrypted at rest

### Security Criteria
Describe security requirements.

**Examples**:
- User must be authenticated
- SQL injection is prevented
- XSS attacks are prevented

### User Experience Criteria
Describe user experience requirements.

**Examples**:
- Error messages are user-friendly
- Interface is intuitive
- Help text is provided

## Acceptance Criteria Checklist

When writing acceptance criteria, check:

- [ ] **Testable**: Can be verified through testing
- [ ] **Specific**: Describes specific behavior
- [ ] **Measurable**: Has clear pass/fail condition
- [ ] **Complete**: Covers all scenarios
- [ ] **Clear**: Easy to understand
- [ ] **Atomic**: Each criterion is independent
- [ ] **Necessary**: Each criterion is needed

## Verification Process

### Step 1: Review Acceptance Criteria
- Read all acceptance criteria
- Ensure they are clear and complete
- Verify they cover all requirements

### Step 2: Write Tests
- Write a test for each criterion
- Ensure tests are independent
- Verify tests are comprehensive

### Step 3: Run Tests
- Run all tests
- Verify all tests pass
- Check coverage

### Step 4: Manual Verification (if applicable)
- Manually test the feature
- Verify user experience
- Check UI/UX

### Step 5: Document Results
- Document test results
- Note any issues
- Get stakeholder sign-off

## Common Mistakes

### 1. Too Vague
**Bad**: System should be fast
**Good**: Response time should be < 100ms

### 2. Not Testable
**Bad**: System should be user-friendly
**Good**: Error messages should be clear and actionable

### 3. Too Many Criteria in One
**Bad**: User can create, update, and delete tasks
**Good**: 
- User can create a task
- User can update a task
- User can delete a task

### 4. Missing Edge Cases
**Bad**: Only tests happy path
**Good**: Tests happy path, error paths, and edge cases

### 5. Not Specific About Error Handling
**Bad**: System should handle errors
**Good**: System should return 400 error with specific message for invalid input

## Example Test Implementation

```python
# tests/test_task_creation.py

def test_create_task_with_valid_title():
    """AC1: Create task with valid title."""
    service = TaskService()
    task = service.create_task("Valid task title")
    
    assert task.id is not None
    assert task.title == "Valid task title"
    assert task.status == TaskStatus.PENDING
    assert task.created_at is not None

def test_create_task_with_empty_title_raises_error():
    """AC2: Reject empty title."""
    service = TaskService()
    
    with pytest.raises(ValidationError, match="Title cannot be empty"):
        service.create_task("")

def test_create_task_with_long_title_raises_error():
    """AC3: Reject title exceeding 200 characters."""
    service = TaskService()
    long_title = "x" * 201
    
    with pytest.raises(ValidationError, match="Title cannot exceed 200 characters"):
        service.create_task(long_title)

def test_create_task_with_description():
    """AC4: Accept optional description."""
    service = TaskService()
    task = service.create_task("Task title", description="Task description")
    
    assert task.description == "Task description"

def test_create_task_trims_whitespace():
    """AC5: Handle whitespace in title."""
    service = TaskService()
    task = service.create_task("  Task title  ")
    
    assert task.title == "Task title"

def test_create_task_response_time():
    """AC6: Response time requirement."""
    import time
    service = TaskService()
    
    start_time = time.perf_counter()
    service.create_task("Task title")
    elapsed_time = time.perf_counter() - start_time
    
    assert elapsed_time < 0.1, f"Response time {elapsed_time}s exceeds 100ms"
```

## Acceptance Criteria Sign-off

Before marking a feature as complete:

1. **All criteria verified**: ✅/❌
2. **All tests passing**: ✅/❌
3. **Coverage meets requirements**: ✅/❌
4. **Performance meets requirements**: ✅/❌
5. **Security verified**: ✅/❌
6. **Documentation complete**: ✅/❌
7. **Stakeholder approval**: ✅/❌

**Overall Approval**: ✅/❌

---

**Approved by**: _____________
**Date**: _____________
**Signature**: _____________