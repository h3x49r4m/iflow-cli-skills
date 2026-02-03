# Integration Check Guide

## Purpose
This guide explains how to verify that features work together correctly and that integration points are functioning as expected.

## Integration Check Process

### Step 1: Identify Integration Points
- List all features that interact with the new feature
- Identify data flow between features
- Identify shared resources (database, cache, etc.)
- Identify API endpoints affected

### Step 2: Test Feature Interactions
- Test each interaction between features
- Verify data flows correctly
- Check for side effects
- Validate state management

### Step 3: Test End-to-End Workflows
- Test complete user workflows
- Verify multi-feature scenarios
- Check error propagation
- Validate rollback scenarios

### Step 4: Test Shared Resources
- Test database operations
- Test cache interactions
- Test file system operations
- Test external API calls

### Step 5: Performance Testing
- Test with realistic data volumes
- Check for performance bottlenecks
- Verify resource usage
- Test concurrent operations

## Integration Check Types

### 1. Feature-to-Feature Integration
Test how features interact with each other.

#### Example: User + Tasks Integration
```python
def test_user_can_create_and_manage_their_tasks():
    """Verify users can create and manage their own tasks."""
    # Create user
    user_service = UserService()
    user = user_service.create_user("test@example.com", "password")
    
    # Create tasks for user
    task_service = TaskService()
    task1 = task_service.create_task("Task 1", user_id=user.id)
    task2 = task_service.create_task("Task 2", user_id=user.id)
    
    # Retrieve user's tasks
    user_tasks = task_service.get_user_tasks(user.id)
    
    assert len(user_tasks) == 2
    assert task1.id in [t.id for t in user_tasks]
    assert task2.id in [t.id for t in user_tasks]
```

### 2. Database Integration
Test database operations and transactions.

#### Example: Transaction Rollback
```python
def test_task_creation_rolls_back_on_error():
    """Verify task creation rolls back on error."""
    repository = DatabaseTaskRepository()
    
    # Mock a database error
    with patch.object(repository, 'save') as mock_save:
        mock_save.side_effect = DatabaseError("Connection lost")
        
        service = TaskService(repository)
        
        with pytest.raises(TaskError):
            service.create_task("Test task")
        
        # Verify no partial data was saved
        tasks = repository.find_all()
        assert len(tasks) == 0
```

### 3. API Integration
Test API endpoints and request/response handling.

#### Example: API Workflow
```python
def test_create_task_via_api_workflow():
    """Test complete API workflow for task creation."""
    client = TestClient(app)
    
    # Login
    login_response = client.post("/auth/login", json={
        "email": "test@example.com",
        "password": "password"
    })
    token = login_response.json()["token"]
    
    # Create task
    create_response = client.post(
        "/tasks",
        json={"title": "Test task"},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert create_response.status_code == 201
    task_id = create_response.json()["id"]
    
    # Get task
    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 200
    assert get_response.json()["title"] == "Test task"
    
    # Update task
    update_response = client.put(
        f"/tasks/{task_id}",
        json={"title": "Updated task"},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert update_response.status_code == 200
    
    # Delete task
    delete_response = client.delete(
        f"/tasks/{task_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert delete_response.status_code == 204
```

### 4. External Service Integration
Test interactions with external APIs and services.

#### Example: External API Integration
```python
def test_task_notification_sent_to_external_service():
    """Verify task creation sends notification to external service."""
    with patch('src.tasks.service.notification_service') as mock_notify:
        mock_notify.send.return_value = True
        
        service = TaskService()
        task = service.create_task("Test task")
        
        # Verify notification was sent
        mock_notify.send.assert_called_once_with(
            event="task.created",
            data={"task_id": task.id, "title": task.title}
        )
```

### 5. Cache Integration
Test cache operations and invalidation.

#### Example: Cache Integration
```python
def test_task_caching_and_invalidation():
    """Verify task caching and cache invalidation."""
    cache = InMemoryCache()
    repository = CachedTaskRepository(
        base_repository=DatabaseTaskRepository(),
        cache=cache
    )
    
    service = TaskService(repository)
    
    # First call - should fetch from database
    task1 = service.get_task("123")
    assert cache.get("task:123") is not None
    
    # Second call - should fetch from cache
    task2 = service.get_task("123")
    assert task1 == task2
    
    # Update task - should invalidate cache
    service.update_task("123", "Updated title")
    assert cache.get("task:123") is None
    
    # Third call - should fetch from database again
    task3 = service.get_task("123")
    assert task3.title == "Updated title"
```

## Integration Check Checklist

Use this checklist when checking feature integration.

---

## Integration Check: [Feature Name]

### Integration Points Identified
List all features and systems that integrate with this feature:

| Integration Point | Type | Status |
|-------------------|------|--------|
| Feature A | Feature-to-Feature | ✅/❌ |
| Feature B | Feature-to-Feature | ✅/❌ |
| Database | Data Layer | ✅/❌ |
| Cache | Caching Layer | ✅/❌ |
| External API | External Service | ✅/❌ |

---

### Feature-to-Feature Integration Tests

| Test | Status | Notes |
|------|--------|-------|
| Interaction with Feature A | ✅/❌ | |
| Interaction with Feature B | ✅/❌ | |
| Workflow A → B → C | ✅/❌ | |
| Error propagation | ✅/❌ | |

**All feature interactions working?** ✅/❌

---

### Database Integration Tests

| Test | Status | Notes |
|------|--------|-------|
| Create operation | ✅/❌ | |
| Read operation | ✅/❌ | |
| Update operation | ✅/❌ | |
| Delete operation | ✅/❌ | |
| Transaction rollback | ✅/❌ | |
| Constraint enforcement | ✅/❌ | |
| Data integrity | ✅/❌ | |

**Database integration working?** ✅/❌

---

### API Integration Tests

| Test | Status | Notes |
|------|--------|-------|
| POST endpoint | ✅/❌ | |
| GET endpoint | ✅/❌ | |
| PUT endpoint | ✅/❌ | |
| DELETE endpoint | ✅/❌ | |
| Error responses | ✅/❌ | |
| Authentication | ✅/❌ | |
| Authorization | ✅/❌ | |

**API integration working?** ✅/❌

---

### External Service Integration Tests

| Test | Status | Notes |
|------|--------|-------|
| Service call success | ✅/❌ | |
| Service call failure | ✅/❌ | |
| Timeout handling | ✅/❌ | |
| Retry logic | ✅/❌ | |
| Error handling | ✅/❌ | |

**External service integration working?** ✅/❌

---

### Cache Integration Tests

| Test | Status | Notes |
|------|--------|-------|
| Cache hit | ✅/❌ | |
| Cache miss | ✅/❌ | |
| Cache invalidation | ✅/❌ | |
| Cache expiration | ✅/❌ | |

**Cache integration working?** ✅/❌

---

### End-to-End Workflow Tests

| Workflow | Status | Notes |
|----------|--------|-------|
| Workflow 1 | ✅/❌ | |
| Workflow 2 | ✅/❌ | |
| Workflow 3 | ✅/❌ | |

**All workflows working?** ✅/❌

---

### Performance Tests

| Test | Target | Actual | Status |
|------|--------|--------|--------|
| Response time | < 100ms | __ms | ✅/❌ |
| Throughput | > 100 req/s | __ req/s | ✅/❌ |
| Memory usage | < 100MB | __MB | ✅/❌ |

**Performance acceptable?** ✅/❌

---

### Concurrency Tests

| Test | Status | Notes |
|------|--------|-------|
| Concurrent reads | ✅/❌ | |
| Concurrent writes | ✅/❌ | |
| Race conditions | ✅/❌ | |
| Deadlocks | ✅/❌ | |

**Concurrency handling working?** ✅/❌

---

### Error Scenario Tests

| Scenario | Status | Notes |
|----------|--------|-------|
| Network failure | ✅/❌ | |
| Database failure | ✅/❌ | |
| External service down | ✅/❌ | |
| Invalid data | ✅/❌ | |
| Resource exhaustion | ✅/❌ | |

**Error handling working?** ✅/❌

---

## Final Integration Check

### Summary
- **Total checks**: __/__
- **Passed**: __
- **Failed**: __

### Failed Items
List any failed integration checks:
1. [ ] Item 1 - Reason
2. [ ] Item 2 - Reason

### Decision
- [ ] **PASSED**: All integrations working correctly
- [ ] **CONDITIONAL**: Minor issues, can proceed with fixes
- [ ] **FAILED**: Critical integration issues, fix required

### Approver
- Name: _____________
- Date: _____________

---

## Integration Test Examples

### Complete User Task Workflow
```python
def test_complete_user_task_workflow():
    """Test complete workflow: register → login → create task → complete task."""
    # Register user
    user_service = UserService()
    user = user_service.register_user("test@example.com", "password123")
    
    # Login
    session = user_service.login("test@example.com", "password123")
    
    # Create task
    task_service = TaskService()
    task = task_service.create_task("Complete this task", user_id=user.id)
    
    # Complete task
    completed_task = task_service.complete_task(task.id, user_id=user.id)
    
    # Verify
    assert completed_task.status == TaskStatus.COMPLETED
    assert completed_task.completed_by == user.id
```

### Multi-Feature Data Flow
```python
def test_data_flow_across_features():
    """Test data flow from task creation to analytics."""
    # Create task
    task_service = TaskService()
    task = task_service.create_task("Analytics test")
    
    # Update task multiple times
    task_service.update_task_status(task.id, TaskStatus.IN_PROGRESS)
    task_service.update_task_status(task.id, TaskStatus.COMPLETED)
    
    # Verify analytics captured
    analytics_service = AnalyticsService()
    stats = analytics_service.get_task_stats(task.id)
    
    assert stats["created_at"] is not None
    assert stats["status_changes"] == 2
    assert stats["completion_time"] > 0
```

### Error Propagation
```python
def test_error_propagation_across_features():
    """Verify errors propagate correctly across features."""
    # Simulate database error
    with patch('src.tasks.repository.db.execute') as mock_db:
        mock_db.side_effect = DatabaseError("Connection lost")
        
        task_service = TaskService()
        
        # Error should propagate
        with pytest.raises(TaskError, match="database"):
            task_service.create_task("Test task")
```

## Integration Test Commands

```bash
# Run integration tests
uv run pytest tests/integration/

# Run specific integration test
uv run pytest tests/integration/test_workflows.py::test_complete_workflow

# Run with coverage
uv run pytest tests/integration/ --cov=src --cov-report=term-missing

# Run with verbose output
uv run pytest tests/integration/ -v

# Run with database
uv run pytest tests/integration/ --db-url=postgresql://localhost/test

# Run with external services
uv run pytest tests/integration/ --mock-external=false
```