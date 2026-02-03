# Test Coverage Tracker

This document tracks test coverage for each feature and module to ensure quality standards are met.

## Coverage Targets

| Metric | Minimum | Target | Current |
|--------|---------|--------|---------|
| Line Coverage | 80% | 90% | __% |
| Branch Coverage | 75% | 85% | __% |
| Function Coverage | 100% | 100% | __% |

## Feature Coverage

### Feature 1 (F001)

**Module**: `src/module1/`

| File | Lines | Covered | Missing | Coverage | Status |
|------|-------|---------|---------|----------|--------|
| `models.py` | __ | __ | __ | __% | ✅/❌ |
| `service.py` | __ | __ | __ | __% | ✅/❌ |
| `repository.py` | __ | __ | __ | __% | ✅/❌ |
| `exceptions.py` | __ | __ | __ | __% | ✅/❌ |
| **Total** | __ | __ | __ | __% | ✅/❌ |

**Test Files**:
- `tests/unit/test_models.py` - __ tests
- `tests/unit/test_service.py` - __ tests
- `tests/integration/test_module1.py` - __ tests

**Notes**:
- Missing lines: __
- Edge cases not covered: __
- Improvements needed: __

---

### Feature 2 (F002)

**Module**: `src/module2/`

| File | Lines | Covered | Missing | Coverage | Status |
|------|-------|---------|---------|----------|--------|
| `models.py` | __ | __ | __ | __% | ✅/❌ |
| `service.py` | __ | __ | __ | __% | ✅/❌ |
| `utils.py` | __ | __ | __ | __% | ✅/❌ |
| **Total** | __ | __ | __ | __% | ✅/❌ |

**Test Files**:
- `tests/unit/test_models.py` - __ tests
- `tests/unit/test_service.py` - __ tests
- `tests/integration/test_module2.py` - __ tests

**Notes**:
- Missing lines: __
- Edge cases not covered: __
- Improvements needed: __

---

### Feature 3 (F003)

**Module**: `src/module3/`

| File | Lines | Covered | Missing | Coverage | Status |
|------|-------|---------|---------|----------|--------|
| `service.py` | __ | __ | __ | __% | ✅/❌ |
| `api.py` | __ | __ | __ | __% | ✅/❌ |
| **Total** | __ | __ | __ | __% | ✅/❌ |

**Test Files**:
- `tests/unit/test_service.py` - __ tests
- `tests/integration/test_module3.py` - __ tests
- `tests/e2e/test_api.py` - __ tests

**Notes**:
- Missing lines: __
- Edge cases not covered: __
- Improvements needed: __

---

## Module Coverage

### Core Modules

| Module | Lines | Covered | Coverage | Target | Status |
|--------|-------|---------|----------|--------|--------|
| `src/models/` | __ | __ | __% | 70% | ✅/❌ |
| `src/services/` | __ | __ | __% | 90% | ✅/❌ |
| `src/repositories/` | __ | __ | __% | 85% | ✅/❌ |
| `src/api/` | __ | __ | __% | 85% | ✅/❌ |
| `src/utils/` | __ | __ | __% | 80% | ✅/❌ |

### Overall Coverage

| Type | Lines | Covered | Coverage | Target | Status |
|------|-------|---------|----------|--------|--------|
| **Line** | __ | __ | __% | 80% | ✅/❌ |
| **Branch** | __ | __ | __% | 75% | ✅/❌ |
| **Function** | __ | __ | __% | 100% | ✅/❌ |

## Coverage by Test Type

| Test Type | Coverage | Notes |
|-----------|----------|-------|
| Unit Tests | __% | Tests individual functions |
| Integration Tests | __% | Tests component interactions |
| E2E Tests | __% | Tests complete workflows |
| **Overall** | __% | |

## Coverage Trend

| Date | Line Coverage | Branch Coverage | Function Coverage |
|------|---------------|-----------------|-------------------|
| YYYY-MM-DD | __% | __% | __% |
| YYYY-MM-DD | __% | __% | __% |
| YYYY-MM-DD | __% | __% | __% |

## Low Coverage Areas

### Files Below Minimum Coverage

| File | Coverage | Target | Gap | Priority |
|------|----------|--------|-----|----------|
| `src/module/file.py` | __% | __% | __% | High/Medium/Low |
| `src/module/file2.py` | __% | __% | __% | High/Medium/Low |

### Action Items

1. **File**: `src/module/file.py`
   - **Gap**: __%
   - **Action**: Write tests for missing lines
   - **Due**: YYYY-MM-DD
   - **Assignee**: _____

2. **File**: `src/module/file2.py`
   - **Gap**: __%
   - **Action**: Add edge case tests
   - **Due**: YYYY-MM-DD
   - **Assignee**: _____

## Coverage Reports

### Generate Coverage Report

```bash
# Terminal report
uv run pytest --cov=src --cov-report=term-missing

# HTML report
uv run pytest --cov=src --cov-report=html
open htmlcov/index.html

# XML report (for CI/CD)
uv run pytest --cov=src --cov-report=xml
```

### Coverage Report Interpretation

```
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/
├── __init__.py              2      0   100%
├── models.py               15      1    93%   14
├── service.py              40      5    88%   23-24, 45
└── utils.py                20      3    85%   18-20
-------------------------------------------------------
TOTAL                       77      9    88%
```

- **Stmts**: Total statements in file
- **Miss**: Statements not covered by tests
- **Cover**: Percentage of statements covered
- **Missing**: Line numbers not covered

## Coverage Best Practices

### Improving Coverage

1. **Add Unit Tests**: Test individual functions
2. **Test Edge Cases**: Boundary values, empty inputs
3. **Test Error Paths**: Test exception handling
4. **Test All Branches**: Ensure all if/else paths tested
5. **Mock External Dependencies**: Test code in isolation

### Maintaining Coverage

1. **Write Tests First**: Follow TDD methodology
2. **Check Coverage Regularly**: Run coverage on each commit
3. **Review Missing Lines**: Address uncovered code
4. **Document Uncovered Code**: Explain why code can't be tested
5. **Use Coverage Gates**: Fail PRs below threshold

## Using This Tracker

1. **Update Regularly**: After each feature or major change
2. **Check Targets**: Ensure coverage meets minimum requirements
3. **Track Trends**: Monitor coverage over time
4. **Identify Gaps**: Find areas needing more tests
5. **Prioritize Improvements**: Focus on high-priority modules
6. **Document Reasons**: Explain why some code can't be tested

## Notes

- Coverage is a quality indicator, not the only metric
- Focus on meaningful tests, not just high numbers
- Test behavior, not implementation
- Review missing lines to understand what's not tested
- Use coverage to find gaps, not as a goal in itself