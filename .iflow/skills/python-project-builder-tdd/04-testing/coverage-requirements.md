# Coverage Requirements Guide

## Purpose
This guide defines the test coverage requirements for the project and how to measure and maintain them.

## Coverage Metrics

### Types of Coverage

#### 1. Line Coverage
Percentage of code lines that are executed during tests.

**Goal**: 80% minimum, 90% target

```bash
# Check line coverage
uv run pytest --cov=src --cov-report=term-missing
```

#### 2. Branch Coverage
Percentage of conditional branches that are executed.

**Goal**: 75% minimum, 85% target

Branch coverage ensures all `if/else` paths are tested.

#### 3. Function Coverage
Percentage of functions/methods that are called during tests.

**Goal**: 100% minimum

Every function should be tested at least once.

#### 4. Statement Coverage
Similar to line coverage, counts statements executed.

**Goal**: 80% minimum

## Coverage Targets

### Overall Project
| Metric | Minimum | Target |
|--------|---------|--------|
| Line Coverage | 80% | 90% |
| Branch Coverage | 75% | 85% |
| Function Coverage | 100% | 100% |
| Statement Coverage | 80% | 90% |

### Per Module
| Module Type | Line Coverage | Branch Coverage |
|-------------|---------------|-----------------|
| Core Business Logic | 90% | 85% |
| Utilities/Helpers | 80% | 75% |
| Models/Data Classes | 70% | 60% |
| Configuration | 50% | 40% |

### Per Feature
Each feature should have:
- **Unit tests**: 90%+ line coverage
- **Integration tests**: 70%+ line coverage
- **Overall**: 80%+ line coverage

## Measuring Coverage

### Generate Coverage Report
```bash
# Terminal report with missing lines
uv run pytest --cov=src --cov-report=term-missing

# HTML report
uv run pytest --cov=src --cov-report=html
open htmlcov/index.html

# XML report (for CI/CD)
uv run pytest --cov=src --cov-report=xml
```

### Coverage Report Format
```
Name                           Stmts   Miss  Cover   Missing
--------------------------------------------------------------------
src/
├── __init__.py                    2      0   100%
├── main.py                       10      2    80%   8-9
├── tasks/
│   ├── __init__.py                2      0   100%
│   ├── models.py                 15      1    93%   14
│   ├── service.py                40      5    88%   23-24, 45
│   └── repository.py             25      0   100%
└── utils/
    ├── __init__.py                2      0   100%
    └── validators.py             20      3    85%   18-20
--------------------------------------------------------------------
TOTAL                            116     11    91%
```

### Interpreting Coverage

**Missing** column shows which lines are not covered:
- Line 8-9: Not covered (likely error handling)
- Line 14: Not covered (likely edge case)
- Line 23-24, 45: Not covered (specific branches)

## Coverage by Test Type

### Unit Test Coverage
- **Purpose**: Test individual functions in isolation
- **Expected Coverage**: 90%+ line coverage for each module
- **Branch Coverage**: 85%+ for conditional logic
- **Location**: `tests/unit/` (mirrors `src/` directory structure)

```bash
# Run only unit tests
uv run pytest tests/unit/ --cov=src --cov-report=term-missing

# Run with unit marker
uv run pytest -m unit --cov=src --cov-report=term-missing
```

### Integration Test Coverage
- **Purpose**: Test component interactions
- **Expected Coverage**: 70%+ line coverage
- **Focus**: Data flow and integration points
- **Location**: `tests/integration/`

```bash
# Run only integration tests
uv run pytest tests/integration/ --cov=src --cov-report=term-missing

# Run with integration marker
uv run pytest -m integration --cov=src --cov-report=term-missing
```

### E2E Test Coverage
- **Purpose**: Test complete workflows
- **Expected Coverage**: Not measured (focus on scenario coverage)
- **Focus**: Critical user workflows
- **Location**: `tests/e2e/`

```bash
# Run only E2E tests
uv run pytest tests/e2e/ --cov=src --cov-report=term-missing

# Run with e2e marker
uv run pytest -m e2e --cov=src --cov-report=term-missing
```

## Handling Low Coverage

### When Coverage is Below Minimum

1. **Identify Uncovered Code**
```bash
# Show which lines are not covered
uv run pytest --cov=src --cov-report=term-missing
```

2. **Categorize Uncovered Lines**
   - **Error handling**: May be acceptable if hard to test
   - **Edge cases**: Should be tested
   - **Dead code**: Should be removed
   - **Configuration**: May be acceptable

3. **Write Tests or Document Exceptions**
   - **Testable**: Write tests for uncovered lines
   - **Untestable**: Add comment explaining why untested
   - **Dead code**: Remove the code

4. **Re-measure Coverage**
```bash
uv run pytest --cov=src
```

### Acceptable Low Coverage

Some code may have acceptable lower coverage:

#### Configuration Code
```python
# config.py - 50% coverage acceptable
DATABASE_URL = os.getenv("DATABASE_URL")
API_KEY = os.getenv("API_KEY")  # Hard to test in isolation
```

#### Simple Data Classes
```python
# models.py - 70% coverage acceptable
@dataclass
class Task:
    id: str
    title: str
    # Getters/setters auto-generated, hard to test
```

#### Platform-Specific Code
```python
# platform.py - Lower coverage acceptable
def get_platform():
    if sys.platform == "darwin":  # Hard to test on all platforms
        return "macos"
    # ...
```

## Excluding Code from Coverage

### Mark Code to Exclude
```python
# pragma: no cover - Exclude specific line
if DEBUG:  # pragma: no cover
    log.debug("Debug info")

# pragma: no cover - Exclude entire block
def internal_debug_function():  # pragma: no cover
    """Internal debug function, not tested."""
    pass

# pragma: no cover - Exclude function
@dataclass
class DebugInfo:  # pragma: no cover
    timestamp: datetime
```

### Configure Coverage Exclusions

```ini
# .coveragerc
[run]
omit =
    */tests/*
    */__init__.py
    */config.py
    */migrations/*
    setup.py

[report]
exclude_lines =
    pragma: no cover
    def __repr__
    raise AssertionError
    raise NotImplementedError
    if __name__ == .__main__.:
    if TYPE_CHECKING:
    @abstractmethod
```

## Coverage in CI/CD

### GitHub Actions Example
```yaml
# .github/workflows/coverage.yml
name: Coverage

on: [push, pull_request]

jobs:
  coverage:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - run: pip install uv
      
      - run: uv sync
      
      - run: |
          uv run pytest --cov=src --cov-report=xml --cov-report=term-missing
      
      - name: Check coverage threshold
        run: |
          coverage=$(uv run pytest --cov=src --cov-report=json | jq '.totals.percent_covered')
          if (( $(echo "$coverage < 80" | bc -l) )); then
            echo "Coverage $coverage% is below 80% threshold"
            exit 1
          fi
      
      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v3
        with:
          file: ./coverage.xml
          fail_ci_if_error: true
          token: ${{ secrets.CODECOV_TOKEN }}
```

### Pre-commit Hook
```bash
#!/bin/bash
# .git/hooks/pre-commit

# Run coverage check
COVERAGE=$(uv run pytest --cov=src --cov-report=json --quiet | jq '.totals.percent_covered')

echo "Current coverage: ${COVERAGE}%"

if (( $(echo "$COVERAGE < 80" | bc -l) )); then
    echo "❌ Coverage is below 80% threshold"
    echo "Please add tests to improve coverage"
    exit 1
fi

echo "✅ Coverage meets 80% threshold"
```

## Coverage Best Practices

### 1. Focus on Meaningful Coverage
- Test critical paths thoroughly
- Test error conditions
- Test edge cases
- Don't just aim for high numbers

### 2. Quality Over Quantity
```python
# Good - meaningful test
def test_create_task_with_invalid_title_raises_error():
    with pytest.raises(ValidationError):
        service.create_task("")

# Avoid - meaningless test for coverage
def test_task_exists():
    task = Task(id="1", title="Test")  # Just for coverage
    assert task is not None
```

### 3. Use Coverage as a Guide
- Coverage shows what's NOT tested
- High coverage doesn't mean good tests
- Use coverage to find gaps, not as the only metric

### 4. Monitor Coverage Trends
```bash
# Generate coverage badge
uv run pytest --cov=src --cov-report=badge
```

Track coverage over time:
- Set baseline coverage
- Monitor for drops
- Investigate significant changes

### 5. Set Module-Specific Targets
- Core logic: 90%+
- Utilities: 80%+
- Configuration: 50%+

## Coverage Tracking Template

Use this template to track coverage per feature:

```markdown
## Feature: [Feature Name]

| Module | Lines | Target | Actual | Status |
|--------|-------|--------|--------|--------|
| service.py | 40 | 90% | 92% | ✅ |
| repository.py | 25 | 85% | 90% | ✅ |
| models.py | 15 | 70% | 75% | ✅ |
| **Total** | **80** | **85%** | **89%** | ✅ |

### Uncovered Lines
- service.py:23-24 (error handling, documented)
- models.py:14 (optional field, tested in integration)

### Notes
- All acceptance criteria covered
- Edge cases tested
- Error handling documented
```

## Coverage Commands Reference

```bash
# Generate coverage report
uv run pytest --cov=src

# Detailed report with missing lines
uv run pytest --cov=src --cov-report=term-missing

# HTML report
uv run pytest --cov=src --cov-report=html

# JSON report (for CI/CD)
uv run pytest --cov=src --cov-report=json

# Generate coverage badge
uv run pytest --cov=src --cov-report=badge

# Filter by module
uv run pytest --cov=src.tasks --cov-report=term-missing

# Combine coverage from multiple runs
uv run pytest --cov=src --cov-append
uv run pytest --cov=src --cov-append

# Show coverage summary only
uv run pytest --cov=src --cov-report=summary

# Generate coverage with branch coverage
uv run pytest --cov=src --cov-branch
```