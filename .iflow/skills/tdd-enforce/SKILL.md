---
name: tdd-enforce
description: Ensures Test-Driven Development (TDD) workflow is followed throughout the development process
version: 1.0.0
category: development-process
---

# TDD Enforcement Skill

Ensures Test-Driven Development (TDD) workflow is followed throughout the development process.

## Usage

```
/tdd-enforce
```

## What It Does

### 1. Test-First Lock
Prevents implementation without corresponding tests:
- Checks if test file exists before allowing implementation file creation
- Requires test to fail first (red phase)
- Only allows minimal implementation to pass test (green phase)
- Requires refactoring step (refactor phase)

### 2. Test Coverage Gates
Enforces coverage thresholds:
- Component coverage must be ≥ 90% before proceeding
- Integration flow coverage must be 100%
- Safety constraint coverage must be 100%
- Blocks commits if coverage drops below thresholds

### 3. Red-Green-Refactor Cycle Verification
Validates each step of the TDD cycle:
- Detects test creation (no matching implementation)
- Verifies test fails (red state confirmed)
- Detects minimal implementation
- Verifies test passes (green state achieved)
- Detects refactoring changes (without new tests)

### 4. Test Structure Validation
Ensures tests follow TDD best practices:
- Arrange-Act-Assert structure
- Single assertion per test
- Descriptive test names
- Independence between tests
- No test interdependencies

### 5. Implementation Restriction
Enforces test-first workflow:
- Cannot create implementation file without corresponding test file
- Cannot add new function without test
- Cannot modify existing behavior without updating test

### 6. CI Integration
Pipeline checks for automated enforcement:
- All tests pass before merge
- Coverage thresholds met
- TDD cycle steps validated in commit history
- Architecture compliance verified

## Output Format

```
TDD Compliance Report
=====================

Overall Score: 85% (17/20 checks passed)

RED-GREEN-REFACTOR CYCLE
-------------------------
✓ Test Creation Phase (PASS)
✓ Test Failure (Red) (PASS)
✓ Minimal Implementation (Green) (PASS)
✗ Refactoring Phase (FAIL) - No refactoring detected after green

TEST COVERAGE
-------------
Component Coverage: 92% (Required: ≥90%) ✓
Integration Flow Coverage: 100% (Required: 100%) ✓
Safety Constraint Coverage: 95% (Required: 100%) ✗
Overall Coverage: 89% (Required: ≥90%) ✗

TEST STRUCTURE
--------------
✓ Arrange-Act-Assert Pattern (PASS)
✓ Single Assertion Per Test (PASS)
✓ Descriptive Test Names (PASS)
✓ Test Independence (PASS)
✗ No Test Interdependencies (FAIL) - Found 2 dependent tests

IMPLEMENTATION RESTRICTION
---------------------------
✓ All implementations have tests (PASS)
✓ All functions are tested (PASS)
✗ Behavior changes have test updates (FAIL) - Modified goal_engine without test update

VIOLATIONS
----------
1. Refactoring Phase (evo/src/decision_engine.rs)
   No refactoring detected after green phase
   Suggested: Review and refactor for code quality

2. Safety Constraint Coverage (evo/tests/safety_test.rs)
   Coverage: 95% (Required: 100%)
   Missing: storage_limit_enforcement
   Suggested: Add test for storage limit enforcement

3. Test Interdependencies (evo/tests/integration_test.rs)
   Found 2 dependent tests: test_mode_selection, test_handler_routing
   Suggested: Make tests independent with proper setup/teardown

4. Behavior Changes (evo/src/goal_engine.rs)
   Modified goal_engine without test update
   Suggested: Update evo/tests/goal_engine_test.rs to reflect changes

CRITICAL VIOLATIONS: 2 (Build will FAIL)
WARNINGS: 2

TDD CYCLE HISTORY
-----------------
Commit 28d8bfb: Test created → Test failed → Implementation → Test passed ✓
Commit a61cdf0: Test created → Test failed → Implementation → Test passed → Refactored ✓
Commit 4de2892: Test created → Test failed → Implementation → Test passed ✗ (no refactoring)
```

## Enforcement Rules

### File Creation
```
Attempting to create: evo/src/component.rs
VIOLATION: No corresponding test file evo/tests/component_test.rs exists
ACTION: Create test file first, then implement
```

### Function Addition
```
Attempting to add function: new_capability
VIOLATION: No test for new_capability found
ACTION: Add test first, then implement function
```

### Behavior Modification
```
Attempting to modify: goal_engine.evaluate
VIOLATION: Test not updated to reflect new behavior
ACTION: Update test, then modify implementation
```

## Exit Codes

- `0` - All TDD checks passed
- `1` - Critical violations found (build should fail)
- `2` - Warnings only (build can continue)
- `3` - TDD cycle incomplete (missing red/green/refactor steps)

## CI Integration

Add to your CI pipeline:

```yaml
- name: TDD Enforcement
  run: |
    iflow /tdd-enforce
    if [ $? -eq 1 ]; then
      echo "TDD violations detected. Fix before merging."
      exit 1
    fi
```

## Implementation Notes

This skill uses:
- Git history analysis to track TDD cycle progression
- AST parsing for structure validation
- Coverage analysis tools for threshold checking
- Dependency analysis for test independence verification
- File modification tracking for implementation restriction

## Best Practices

1. Always write tests first
2. Ensure tests fail before implementation
3. Write minimal implementation to pass
4. Refactor after green phase
5. Keep tests independent and focused
6. Maintain high coverage (≥90%)
7. Update tests when behavior changes