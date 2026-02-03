# Feature Test Checklist

## Purpose
This checklist ensures each feature is thoroughly tested before being marked as complete.

## Checklist Template

Use this checklist for each feature to ensure comprehensive test coverage.

---

## Feature: [Feature Name]

### Unit Tests

#### Core Functionality
- [ ] **Happy Path**: Primary use case works correctly
- [ ] **Valid Inputs**: All valid input variations work
- [ ] **Output Format**: Returns data in correct format
- [ ] **Return Values**: Returns expected values

#### Input Validation
- [ ] **Required Fields**: Validates required fields are present
- [ ] **Empty Values**: Handles empty strings, None, empty lists
- [ ] **Type Validation**: Validates correct data types
- [ ] **Length Validation**: Validates min/max lengths
- [ ] **Format Validation**: Validates formats (email, URL, etc.)
- [ ] **Range Validation**: Validates numeric ranges

#### Edge Cases
- [ ] **Boundary Values**: Tests at min/max boundaries
- [ ] **Zero Values**: Handles zero, empty, None correctly
- [ ] **Negative Values**: Handles negative numbers correctly
- [ ] **Unicode Characters**: Handles unicode and special characters
- [ ] **Whitespace**: Handles leading/trailing/multiple whitespace
- [ ] **Duplicate Values**: Handles duplicate inputs

#### Error Handling
- [ ] **Invalid Inputs**: Raises appropriate errors for invalid inputs
- [ ] **Error Messages**: Provides clear error messages
- [ ] **Error Types**: Raises correct exception types
- [ ] **Graceful Failure**: Fails gracefully, doesn't crash

#### Dependencies
- [ ] **Mock External Services**: External services are mocked
- [ ] **Mock Database**: Database operations are mocked (for unit tests)
- [ ] **Mock APIs**: API calls are mocked
- [ ] **Mock File System**: File operations are mocked

#### Performance
- [ ] **Fast Execution**: Test runs in < 1 second
- [ ] **No Sleep Statements**: No arbitrary delays
- [ ] **Efficient Setup**: Test setup is minimal

---

### Integration Tests

#### Component Interactions
- [ ] **Service + Repository**: Service correctly uses repository
- [ ] **Service + Validation**: Service correctly validates
- [ ] **Service + External API**: Service correctly calls external APIs
- [ ] **Multiple Services**: Multiple services work together

#### Data Flow
- [ ] **Input → Processing → Output**: Complete data flow works
- [ ] **Data Transformation**: Data transforms correctly
- [ ] **Data Persistence**: Data saves correctly to storage
- [ ] **Data Retrieval**: Data retrieves correctly from storage

#### Error Propagation
- [ ] **Errors Propagate Correctly**: Errors bubble up correctly
- [ ] **Error Handling**: Integration layer handles errors
- [ ] **Rollback**: Failed operations roll back correctly

#### State Management
- [ ] **State Changes**: State changes persist correctly
- [ ] **Concurrent Access**: Handles concurrent access (if applicable)
- [ ] **Transaction Boundaries**: Transactions work correctly

---

### End-to-End Tests

#### User Workflows
- [ ] **Complete Workflow**: End-to-end workflow works
- [ ] **API Endpoint**: API endpoint works correctly
- [ ] **CLI Command**: CLI command works correctly (if applicable)
- [ ] **Web Interface**: Web interface works correctly (if applicable)

#### Authentication/Authorization
- [ ] **Unauthenticated Access**: Rejects unauthenticated requests
- [ ] **Authenticated Access**: Allows authenticated requests
- [ ] **Unauthorized Access**: Rejects unauthorized access
- [ ] **Permission Checks**: Enforces permissions correctly

#### Data Integrity
- [ ] **Data Consistency**: Data remains consistent across operations
- [ ] **Referential Integrity**: References are maintained
- [ ] **Data Validation**: Data validates at all layers

#### Error Scenarios
- [ ] **Network Errors**: Handles network failures
- [ ] **Service Unavailable**: Handles service unavailable
- [ ] **Timeout**: Handles timeouts correctly
- [ ] **Rate Limiting**: Handles rate limiting (if applicable)

---

### Property-Based Tests

#### Random Inputs
- [ ] **Random Valid Inputs**: Works with random valid inputs
- [ ] **Random Invalid Inputs**: Handles random invalid inputs
- [ ] **Large Inputs**: Handles large inputs
- [ ] **Special Characters**: Handles special characters

#### Invariants
- [ ] **Idempotency**: Repeated operations produce same result
- [ ] **Commutativity**: Order doesn't matter (if applicable)
- [ ] **Associativity**: Grouping doesn't matter (if applicable)

---

### Coverage

#### Code Coverage
- [ ] **Lines Covered**: All lines covered (aim for 100% for critical paths)
- [ ] **Branches Covered**: All branches covered (aim for 100%)
- [ ] **Functions Covered**: All functions covered
- [ ] **Overall Coverage**: At least 80% overall coverage

#### Scenario Coverage
- [ ] **Happy Path**: Covered
- [ ] **All Error Paths**: All error paths covered
- [ ] **All Edge Cases**: All identified edge cases covered
- [ ] **All Acceptance Criteria**: All acceptance criteria covered

---

### Test Quality

#### Test Independence
- [ ] **No Shared State**: Tests don't share state
- [ ] **Run in Any Order**: Tests can run in any order
- [ ] **Isolated**: Each test is isolated

#### Test Clarity
- [ ] **Descriptive Names**: Test names describe what is tested
- [ ] **Clear Assertions**: Assertions are clear and specific
- [ ] **Good Documentation**: Tests are documented if complex

#### Test Maintainability
- [ ] **DRY**: No test code duplication
- [ ] **Fixtures Used**: Common setup uses fixtures
- [ ] **Easy to Update**: Tests are easy to update when code changes

---

## Example Checklist: Create Task Feature

### Unit Tests

#### Core Functionality
- [x] **Happy Path**: Can create a task with valid title
- [x] **Valid Inputs**: Creates task with various valid titles
- [x] **Output Format**: Returns Task object with all fields
- [x] **Return Values**: Returns task with generated ID and PENDING status

#### Input Validation
- [x] **Required Fields**: Raises error when title is missing
- [x] **Empty Values**: Raises error when title is empty string
- [x] **Length Validation**: Raises error when title > 200 chars
- [x] **Whitespace**: Trims whitespace from title

#### Edge Cases
- [x] **Boundary Values**: Accepts exactly 200 character title
- [x] **Unicode Characters**: Handles unicode in title
- [x] **Special Characters**: Handles special characters in title

#### Error Handling
- [x] **Invalid Inputs**: Raises ValidationError for invalid titles
- [x] **Error Messages**: Provides clear error messages
- [x] **Error Types**: Raises correct exception types

#### Dependencies
- [x] **Mock External Services**: Repository is mocked
- [x] **Mock Database**: Database operations are mocked

#### Performance
- [x] **Fast Execution**: Test runs in < 1 second

---

### Integration Tests

#### Component Interactions
- [x] **Service + Repository**: Service correctly saves to repository
- [x] **Service + Validation**: Service validates before saving

#### Data Flow
- [x] **Input → Processing → Output**: Complete flow works
- [x] **Data Persistence**: Task persists in repository
- [x] **Data Retrieval**: Task can be retrieved after creation

#### Error Propagation
- [x] **Errors Propagate Correctly**: Repository errors propagate to service

---

### End-to-End Tests

#### User Workflows
- [x] **Complete Workflow**: Can create task through API
- [x] **API Endpoint**: POST /tasks endpoint works
- [x] **Response Format**: Returns 201 with task data

#### Data Integrity
- [x] **Data Consistency**: Task data is consistent
- [x] **Id Generation**: Unique ID is generated

---

### Coverage

#### Code Coverage
- [x] **Lines Covered**: 95% coverage
- [x] **Branches Covered**: 100% branch coverage
- [x] **Functions Covered**: All functions covered
- [x] **Overall Coverage**: 95% overall coverage

#### Scenario Coverage
- [x] **Happy Path**: Covered
- [x] **All Error Paths**: All error paths covered
- [x] **All Edge Cases**: All edge cases covered
- [x] **All Acceptance Criteria**: All 3 acceptance criteria covered

---

### Test Quality

#### Test Independence
- [x] **No Shared State**: Tests don't share state
- [x] **Run in Any Order**: Tests can run in any order
- [x] **Isolated**: Each test is isolated

#### Test Clarity
- [x] **Descriptive Names**: All tests have descriptive names
- [x] **Clear Assertions**: Assertions are clear
- [x] **Good Documentation**: Complex tests documented

#### Test Maintainability
- [x] **DRY**: No duplication, fixtures used
- [x] **Fixtures Used**: Common setup uses fixtures
- [x] **Easy to Update**: Tests are maintainable

---

## Using This Checklist

1. **Copy the template** for each feature
2. **Check off items** as you write tests
3. **Aim for 100%** on critical items (happy path, error handling)
4. **Review checklist** before marking feature as complete
5. **Track coverage** in `test-coverage-tracker.md`