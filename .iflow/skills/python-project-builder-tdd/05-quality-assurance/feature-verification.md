# Feature Verification Guide

## Purpose
This guide explains how to verify that each feature is complete, correct, and ready for deployment.

## Verification Process

### Step 1: Review Feature Specification
- Read the original feature specification
- Verify all acceptance criteria are met
- Check that requirements are fully implemented

### Step 2: Review Test Coverage
- Check test coverage meets minimum requirements (80%)
- Verify all acceptance criteria have tests
- Ensure edge cases are tested
- Review test quality (clear, independent, fast)

### Step 3: Manual Testing
- Test the feature manually (if applicable)
- Verify user experience meets expectations
- Check error messages are clear
- Validate UI/UX (if applicable)

### Step 4: Code Review
- Review code for quality and standards
- Check for code duplication
- Verify type hints and docstrings
- Ensure error handling is appropriate

### Step 5: Integration Testing
- Test feature with other features
- Verify data flow works correctly
- Check for side effects
- Validate state management

### Step 6: Documentation
- Update feature documentation
- Add usage examples
- Document API changes
- Update README if needed

## Feature Verification Checklist

Use this checklist before marking a feature as complete.

---

## Feature: [Feature Name]

### Acceptance Criteria Verification
For each acceptance criterion from the feature specification:

| Criterion | Test | Pass/Fail | Notes |
|-----------|------|-----------|-------|
| Criterion 1 | test_... | ✅/❌ | |
| Criterion 2 | test_... | ✅/❌ | |
| Criterion 3 | test_... | ✅/❌ | |

**All acceptance criteria met?** ✅/❌

---

### Test Coverage Verification

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Line Coverage | 80% | __% | ✅/❌ |
| Branch Coverage | 75% | __% | ✅/❌ |
| Function Coverage | 100% | __% | ✅/❌ |

**Coverage meets minimum?** ✅/❌

---

### Code Quality Verification

#### Code Standards
- [ ] Follows PEP 8
- [ ] Type hints present for all functions
- [ ] Docstrings for all public functions/classes
- [ ] No hardcoded secrets
- [ ] No code duplication

#### Error Handling
- [ ] Input validation present
- [ ] Appropriate error types raised
- [ ] Clear error messages
- [ ] Errors handled gracefully

#### Code Organization
- [ ] Follows project structure
- [ ] Proper module organization
- [ ] Clear separation of concerns
- [ ] Dependencies are minimal

**Code quality acceptable?** ✅/❌

---

### Test Quality Verification

#### Test Coverage
- [ ] All acceptance criteria tested
- [ ] Edge cases tested
- [ ] Error conditions tested
- [ ] Integration tests present (if needed)

#### Test Quality
- [ ] Tests are independent
- [ ] Tests are fast (< 1 second for unit tests)
- [ ] Tests have descriptive names
- [ ] Tests use fixtures appropriately

#### Test Execution
- [ ] All tests pass
- [ ] No flaky tests
- [ ] Tests run in any order
- [ ] No shared state between tests

**Test quality acceptable?** ✅/❌

---

### Integration Verification

#### Component Integration
- [ ] Works with other features
- [ ] No breaking changes to existing code
- [ ] Data flow works correctly
- [ ] State management works correctly

#### API Integration (if applicable)
- [ ] API endpoints work correctly
- [ ] Request/response formats match spec
- [ ] Error responses are correct
- [ ] Authentication/authorization works

#### Database Integration (if applicable)
- [ ] Database operations work correctly
- [ ] Transactions are proper
- [ ] Constraints are enforced
- [ ] Data integrity maintained

**Integration working?** ✅/❌

---

### Performance Verification

#### Response Time
- [ ] Meets performance requirements
- [ ] No memory leaks
- [ ] Efficient algorithms used
- [ ] No unnecessary database queries

#### Scalability (if applicable)
- [ ] Handles expected load
- [ ] Resource usage is reasonable
- [ ] No bottlenecks identified
- [ ] Caching used appropriately

**Performance acceptable?** ✅/❌

---

### Security Verification

#### Input Validation
- [ ] All inputs are validated
- [ ] SQL injection prevented
- [ ] XSS attacks prevented
- [ ] Path traversal prevented

#### Authentication/Authorization (if applicable)
- [ ] Authentication works correctly
- [ ] Authorization enforced properly
- [ ] Sensitive data protected
- [ ] Sessions managed correctly

**Security acceptable?** ✅/❌

---

### Documentation Verification

#### Code Documentation
- [ ] Docstrings present and complete
- [ ] Type hints present
- [ ] Complex code has comments
- [ ] Examples in docstrings

#### User Documentation
- [ ] Feature documented in README
- [ ] Usage examples provided
- [ ] API documentation updated
- [ ] Migration guide (if breaking change)

**Documentation complete?** ✅/❌

---

### Deployment Verification

#### Build Verification
- [ ] Code builds without errors
- [ ] No type checking errors
- [ ] No linting errors
- [ ] All tests pass

#### Deployment Readiness
- [ ] Migration scripts (if needed)
- [ ] Configuration documented
- [ ] Environment variables documented
- [ ] Rollback plan defined

**Ready for deployment?** ✅/❌

---

## Final Verification

### Summary
- **Total checks**: __/__
- **Passed**: __
- **Failed**: __

### Failed Items
List any failed verification items:
1. [ ] Item 1 - Reason
2. [ ] Item 2 - Reason
3. [ ] Item 3 - Reason

### Decision
- [ ] **APPROVED**: Feature is complete and ready for deployment
- [ ] **CONDITIONAL**: Approved with minor fixes required
- [ ] **REJECTED**: Feature needs significant work before approval

### Approver
- Name: _____________
- Date: _____________
- Signature: _____________

---

## Example Verification

## Feature: Create Task

### Acceptance Criteria Verification

| Criterion | Test | Pass/Fail | Notes |
|-----------|------|-----------|-------|
| User can create task with valid title | test_create_task_with_valid_title | ✅ | |
| Empty title should raise error | test_create_task_with_empty_title_raises_error | ✅ | |
| Title exceeding 200 chars should raise error | test_create_task_with_long_title_raises_error | ✅ | |

**All acceptance criteria met?** ✅

---

### Test Coverage Verification

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Line Coverage | 80% | 92% | ✅ |
| Branch Coverage | 75% | 88% | ✅ |
| Function Coverage | 100% | 100% | ✅ |

**Coverage meets minimum?** ✅

---

### Code Quality Verification

#### Code Standards
- [x] Follows PEP 8
- [x] Type hints present for all functions
- [x] Docstrings for all public functions/classes
- [x] No hardcoded secrets
- [x] No code duplication

#### Error Handling
- [x] Input validation present
- [x] Appropriate error types raised
- [x] Clear error messages
- [x] Errors handled gracefully

#### Code Organization
- [x] Follows project structure
- [x] Proper module organization
- [x] Clear separation of concerns
- [x] Dependencies are minimal

**Code quality acceptable?** ✅

---

### Test Quality Verification

#### Test Coverage
- [x] All acceptance criteria tested
- [x] Edge cases tested
- [x] Error conditions tested
- [x] Integration tests present

#### Test Quality
- [x] Tests are independent
- [x] Tests are fast (< 1 second for unit tests)
- [x] Tests have descriptive names
- [x] Tests use fixtures appropriately

#### Test Execution
- [x] All tests pass
- [x] No flaky tests
- [x] Tests run in any order
- [x] No shared state between tests

**Test quality acceptable?** ✅

---

### Integration Verification

#### Component Integration
- [x] Works with other features
- [x] No breaking changes to existing code
- [x] Data flow works correctly
- [x] State management works correctly

#### API Integration
- [x] API endpoints work correctly
- [x] Request/response formats match spec
- [x] Error responses are correct
- [x] Authentication/authorization works

**Integration working?** ✅

---

### Performance Verification

#### Response Time
- [x] Meets performance requirements
- [x] No memory leaks
- [x] Efficient algorithms used
- [x] No unnecessary database queries

**Performance acceptable?** ✅

---

### Security Verification

#### Input Validation
- [x] All inputs are validated
- [x] SQL injection prevented
- [x] XSS attacks prevented
- [x] Path traversal prevented

**Security acceptable?** ✅

---

### Documentation Verification

#### Code Documentation
- [x] Docstrings present and complete
- [x] Type hints present
- [x] Complex code has comments
- [x] Examples in docstrings

#### User Documentation
- [x] Feature documented in README
- [x] Usage examples provided
- [x] API documentation updated

**Documentation complete?** ✅

---

### Deployment Verification

#### Build Verification
- [x] Code builds without errors
- [x] No type checking errors
- [x] No linting errors
- [x] All tests pass

**Ready for deployment?** ✅

---

## Final Verification

### Summary
- **Total checks**: 30/30
- **Passed**: 30
- **Failed**: 0

### Failed Items
None

### Decision
- [x] **APPROVED**: Feature is complete and ready for deployment

### Approver
- Name: Jane Developer
- Date: 2026-02-03
- Signature: JD

---

## Verification Commands

```bash
# Run all tests
uv run pytest

# Check coverage
uv run pytest --cov=src --cov-report=term-missing

# Type checking
uv run mypy src

# Linting
uv run ruff check .

# Formatting check
uv run ruff format --check .

# Build
uv build

# Run integration tests
uv run pytest tests/integration/

# Run E2E tests
uv run pytest tests/e2e/
```