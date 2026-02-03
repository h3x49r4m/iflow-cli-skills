# Performance Check Guide

## Purpose
This guide explains how to validate that the feature meets performance requirements and identify any performance bottlenecks.

## Performance Metrics

### Key Metrics to Measure

| Metric | Description | Target |
|--------|-------------|--------|
| Response Time | Time to complete a request | < 100ms (API), < 1s (CLI) |
| Throughput | Requests per second | > 100 req/s |
| Memory Usage | Memory consumed | < 100MB (typical) |
| CPU Usage | CPU time consumed | < 50% (idle) |
| Database Queries | Number of queries per request | < 5 (typical) |
| Cache Hit Rate | Percentage of cache hits | > 80% |

## Performance Check Process

### Step 1: Define Performance Requirements
- Identify acceptable response times
- Define throughput requirements
- Set memory and CPU limits
- Document database query limits

### Step 2: Measure Baseline Performance
- Measure performance with typical load
- Record baseline metrics
- Identify current bottlenecks
- Document findings

### Step 3: Load Testing
- Test with expected load
- Test with peak load
- Test with stress load
- Identify breaking points

### Step 4: Analyze Results
- Compare against requirements
- Identify bottlenecks
- Find optimization opportunities
- Document recommendations

### Step 5: Optimize (if needed)
- Implement optimizations
- Re-measure performance
- Verify improvements
- Document changes

## Performance Testing Tools

### Built-in Python Tools
```bash
# cProfile for profiling
uv run python -m cProfile -o profile.stats src/main.py

# pstats for analyzing profile
uv run python -m pstats profile.stats
```

### Third-party Tools
```bash
# Add performance testing tools
uv add --dev pytest-benchmark locust py-spy

# pytest-benchmark for microbenchmarks
uv run pytest --benchmark-only

# locust for load testing
uv run locust -f locustfile.py

# py-spy for profiling running processes
py-spy record -o profile.svg --pid <pid>
```

## Performance Testing Examples

### 1. Response Time Testing
```python
import time
import pytest

def test_create_task_response_time():
    """Verify task creation completes within acceptable time."""
    service = TaskService()
    
    start_time = time.perf_counter()
    service.create_task("Performance test task")
    elapsed_time = time.perf_counter() - start_time
    
    # Should complete in less than 100ms
    assert elapsed_time < 0.1, f"Response time {elapsed_time}s exceeds 100ms"
```

### 2. Throughput Testing
```python
def test_task_creation_throughput():
    """Verify can handle high throughput of task creation."""
    service = TaskService()
    num_tasks = 100
    
    start_time = time.perf_counter()
    for i in range(num_tasks):
        service.create_task(f"Task {i}")
    elapsed_time = time.perf_counter() - start_time
    
    throughput = num_tasks / elapsed_time
    # Should handle at least 100 tasks per second
    assert throughput >= 100, f"Throughput {throughput} tasks/s below 100 tasks/s"
```

### 3. Memory Usage Testing
```python
import tracemalloc

def test_task_creation_memory_usage():
    """Verify task creation doesn't leak memory."""
    tracemalloc.start()
    
    service = TaskService()
    
    # Create many tasks
    for i in range(1000):
        service.create_task(f"Task {i}")
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    # Memory usage should be reasonable (< 50MB for 1000 tasks)
    assert peak < 50 * 1024 * 1024, f"Peak memory {peak} bytes exceeds 50MB"
```

### 4. Database Query Testing
```python
def test_task_creation_database_queries():
    """Verify task creation doesn't make excessive database queries."""
    from unittest.mock import Mock
    
    mock_repo = Mock()
    mock_repo.save.return_value = Task(id="1", title="Test", status=TaskStatus.PENDING)
    
    service = TaskService(mock_repo)
    service.create_task("Test task")
    
    # Should only make 1 database query
    assert mock_repo.save.call_count == 1, "Too many database queries"
```

### 5. Cache Performance Testing
```python
def test_task_retrieval_cache_performance():
    """Verify cache improves performance."""
    repository = CachedTaskRepository(
        base_repository=DatabaseTaskRepository(),
        cache=InMemoryCache()
    )
    service = TaskService(repository)
    
    # First call - no cache
    start_time = time.perf_counter()
    service.get_task("123")
    no_cache_time = time.perf_counter() - start_time
    
    # Second call - with cache
    start_time = time.perf_counter()
    service.get_task("123")
    cache_time = time.perf_counter() - start_time
    
    # Cached call should be at least 2x faster
    assert cache_time < no_cache_time / 2, "Cache not providing performance benefit"
```

### 6. Using pytest-benchmark
```python
import pytest

def test_task_creation_benchmark(benchmark):
    """Benchmark task creation performance."""
    service = TaskService()
    
    def create_task():
        return service.create_task("Benchmark task")
    
    result = benchmark(create_task)
    
    # Benchmark will provide statistics
    assert result is not None
```

## Load Testing with Locust

### locustfile.py Example
```python
from locust import HttpUser, task, between

class TaskUser(HttpUser):
    wait_time = between(1, 3)
    
    def on_start(self):
        """Login on start."""
        response = self.client.post("/auth/login", json={
            "email": "test@example.com",
            "password": "password"
        })
        self.token = response.json()["token"]
    
    @task
    def create_task(self):
        """Create a task."""
        self.client.post(
            "/tasks",
            json={"title": "Load test task"},
            headers={"Authorization": f"Bearer {self.token}"}
        )
    
    @task(3)
    def list_tasks(self):
        """List tasks (3x more frequent)."""
        self.client.get(
            "/tasks",
            headers={"Authorization": f"Bearer {self.token}"}
        )
```

### Running Locust
```bash
# Run Locust
uv run locust -f locustfile.py

# Run in headless mode
uv run locust -f locustfile.py --headless --users 100 --spawn-rate 10 --run-time 60s
```

## Performance Checklist

Use this checklist to verify feature performance.

---

## Performance Check: [Feature Name]

### Performance Requirements

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Response Time | < 100ms | __ms | ✅/❌ |
| Throughput | > 100 req/s | __ req/s | ✅/❌ |
| Memory Usage | < 100MB | __MB | ✅/❌ |
| CPU Usage | < 50% | __% | ✅/❌ |
| Database Queries | < 5 per request | __ | ✅/❌ |
| Cache Hit Rate | > 80% | __% | ✅/❌ |

**All performance requirements met?** ✅/❌

---

### Response Time Tests

| Operation | Target | Actual | Status |
|-----------|--------|--------|--------|
| Create | < 100ms | __ms | ✅/❌ |
| Read | < 50ms | __ms | ✅/❌ |
| Update | < 100ms | __ms | ✅/❌ |
| Delete | < 100ms | __ms | ✅/❌ |
| List | < 200ms | __ms | ✅/❌ |

**Response time acceptable?** ✅/❌

---

### Throughput Tests

| Operation | Target | Actual | Status |
|-----------|--------|--------|--------|
| Create | > 100 req/s | __ req/s | ✅/❌ |
| Read | > 500 req/s | __ req/s | ✅/❌ |
| Update | > 100 req/s | __ req/s | ✅/❌ |
| Delete | > 100 req/s | __ req/s | ✅/❌ |

**Throughput acceptable?** ✅/❌

---

### Resource Usage Tests

| Resource | Target | Actual | Status |
|----------|--------|--------|--------|
| Memory (idle) | < 50MB | __MB | ✅/❌ |
| Memory (peak) | < 200MB | __MB | ✅/❌ |
| CPU (idle) | < 10% | __% | ✅/❌ |
| CPU (peak) | < 80% | __% | ✅/❌ |

**Resource usage acceptable?** ✅/❌

---

### Database Performance Tests

| Test | Target | Actual | Status |
|------|--------|--------|--------|
| Queries per request | < 5 | __ | ✅/❌ |
| Query time (avg) | < 10ms | __ms | ✅/❌ |
| Query time (max) | < 100ms | __ms | ✅/❌ |
| Index usage | > 90% | __% | ✅/❌ |

**Database performance acceptable?** ✅/❌

---

### Cache Performance Tests

| Test | Target | Actual | Status |
|------|--------|--------|--------|
| Cache hit rate | > 80% | __% | ✅/❌ |
| Cache miss rate | < 20% | __% | ✅/❌ |
| Cache latency | < 1ms | __ms | ✅/❌ |
| Invalidations | Correct | ✅/❌ | |

**Cache performance acceptable?** ✅/❌

---

### Load Testing Results

| Load Level | Response Time | Error Rate | Status |
|------------|---------------|------------|--------|
| Normal (10 users) | __ms | __% | ✅/❌ |
| High (100 users) | __ms | __% | ✅/❌ |
| Peak (1000 users) | __ms | __% | ✅/❌ |

**Load testing acceptable?** ✅/❌

---

### Scalability Tests

| Test | Result | Status |
|------|--------|--------|
| Linear scaling (10x load) | __x response time | ✅/❌ |
| Memory growth (1000 items) | __MB | ✅/❌ |
| Connection pooling | Working | ✅/❌ |

**Scalability acceptable?** ✅/❌

---

## Bottleneck Analysis

### Identified Bottlenecks
List any performance bottlenecks identified:

| Bottleneck | Impact | Severity | Recommendation |
|------------|--------|----------|----------------|
| Database query | High | Critical | Add index |
| N+1 query problem | Medium | High | Use eager loading |
| Memory leak | High | Critical | Fix reference |
| Inefficient algorithm | Low | Medium | Optimize |

**Bottlenecks addressed?** ✅/❌

---

## Optimization Recommendations

### Implemented Optimizations
List optimizations implemented:

| Optimization | Impact | Status |
|--------------|--------|--------|
| Added database index | 50% faster | ✅ |
| Implemented caching | 80% faster | ✅ |
| Optimized algorithm | 30% faster | ✅ |

### Future Optimizations
List potential future optimizations:

| Optimization | Expected Impact | Priority |
|--------------|-----------------|----------|
| Redis caching | 90% faster | High |
| Query optimization | 40% faster | Medium |
| Code refactoring | 20% faster | Low |

---

## Final Performance Check

### Summary
- **Total checks**: __/__
- **Passed**: __
- **Failed**: __

### Performance Score
- **Overall Score**: __/100
- **Response Time**: __/20
- **Throughput**: __/20
- **Resource Usage**: __/20
- **Database**: __/20
- **Scalability**: __/20

### Decision
- [ ] **PASSED**: Performance meets all requirements
- [ ] **CONDITIONAL**: Minor performance issues, can proceed
- [ ] **FAILED**: Critical performance issues, optimization required

### Approver
- Name: _____________
- Date: _____________

---

## Performance Testing Commands

```bash
# Run performance tests
uv run pytest tests/performance/

# Run with benchmarking
uv run pytest --benchmark-only

# Profile with cProfile
uv run python -m cProfile -o profile.stats src/main.py

# Analyze profile
uv run python -m pstats profile.stats

# Run load tests
uv run locust -f locustfile.py

# Profile running process
py-spy record -o profile.svg --pid <pid>

# Memory profiling
uv run pytest --memprof

# Check database query count
uv run pytest --db-query-log
```

## Performance Best Practices

1. **Measure First**: Always measure before optimizing
2. **Focus on Hotspots**: Optimize the slowest parts first
3. **Use Caching**: Cache expensive operations
4. **Optimize Queries**: Use indexes and avoid N+1 queries
5. **Use Connection Pooling**: Reuse database connections
6. **Limit Data**: Only fetch needed data
7. **Use Asynchronous Operations**: For I/O bound tasks
8. **Monitor Continuously**: Track performance in production
9. **Set Alerts**: Alert on performance degradation
10. **Document**: Document performance characteristics