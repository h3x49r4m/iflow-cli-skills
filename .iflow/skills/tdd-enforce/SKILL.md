---
name: tdd-enforce
description: Comprehensive enforcement of TDD workflow, project conventions, code conciseness, and code quality
version: 2.0.0
category: development-process
---

# TDD Enforcement Skill

Comprehensive enforcement system that ensures Test-Driven Development (TDD) workflow, project convention compliance, code conciseness, and code quality standards are maintained throughout the development process.

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
Enforces coverage thresholds (configurable in `config.json`):
```json
{
  "tddEnforce": {
    "coverageThresholds": {
      "lines": 90,
      "branches": 80,
      "functions": 90,
      "statements": 90
    },
    "criticalCoverage": {
      "integrationFlow": 100,
      "safetyConstraints": 100
    }
  }
}
```

Default thresholds:
- Component coverage: ≥90% lines, ≥80% branches
- Integration flow coverage: 100%
- Safety constraint coverage: 100%
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

RECURSION AND INFINITE LOOPS
-----------------------------
✗ Recursive function detected (FAIL) - Function calls itself
✓ All loops have explicit termination (PASS)
✓ Loop bounds defined with constants (PASS)
✗ Infinite loop pattern detected (FAIL) - while(true) found

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

5. Recursive Function (evo/src/tree_utils.rs)
   Function traverseTree calls itself recursively
   Suggested: Convert to iterative solution using stack or queue

6. Infinite Loop (evo/src/event_loop.rs)
   Pattern while(true) detected at line 42
   Suggested: Add explicit condition and timeout limit
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

### Recursion Detection

**AST Analysis:**
- Detect direct recursion: function calling itself
- Detect indirect recursion: mutual recursion between functions
- Detect tail recursion: still prohibited, use iteration

**Pattern Matching:**
```typescript
// Direct recursion detected
function factorial(n) {
  return n * factorial(n - 1)
}

// Indirect recursion detected
function isEven(n) { return isOdd(n - 1) }
function isOdd(n) { return isEven(n - 1) }
```

**Enforcement:**
```
Attempting to commit: src/utils/tree.ts
VIOLATION: Recursive function detected
  Function: traverse(node)
  Line: 12
  Calls: traverse(node.left), traverse(node.right)
ACTION: Convert to iterative solution using stack/queue
```

### Infinite Loop Detection

**Pattern Matching:**
- `while(true)` - Always infinite
- `while(1)` - Always infinite
- `for(;;)` - Always infinite
- Unbounded loops without termination conditions

**Enforcement:**
```
Attempting to commit: src/core/event_loop.ts
VIOLATION: Infinite loop detected
  Pattern: while(true)
  Line: 42
ACTION: Add explicit condition and maximum iteration limit
```

### Loop Bounding Requirements

**Required for all loops:**
1. Explicit termination condition
2. Maximum iteration limit or timeout
3. Early exit on error/timeout

**Examples:**
```typescript
// ✅ Bounded loop
const MAX_ITERATIONS = 1000
const TIMEOUT_MS = 5000
const startTime = Date.now()

while (!isDone() && iterations < MAX_ITERATIONS && (Date.now() - startTime) < TIMEOUT_MS) {
  processItem()
  iterations++
}
```

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

## IDE Integration

### VS Code
Create `.vscode/settings.json`:
```json
{
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.fixAll": true
  },
  "files.associations": {
    "*.test.ts": "typescript"
  }
}
```

### Vim/Neovim
Add to `.vimrc`:
```vim
autocmd BufWritePost *.test.ts :!tdd-enforce check %
```

### Real-Time Feedback

The skill provides real-time feedback during development:

**Red Phase Detection:**
- Monitors test file creation
- Validates test fails before implementation
- Alert: "Test must fail before implementation (TDD red phase)"

**Green Phase Detection:**
- Monitors implementation file creation
- Validates minimal implementation only
- Alert: "Implementation exceeds minimal required code"

**Refactor Phase Detection:**
- Monitors code changes after green phase
- Validates refactoring improves code quality
- Alert: "Refactoring step required (TDD refactor phase)"

**Integration with Watch Mode:**
```bash
# Run TDD enforcement in watch mode
/tdd-enforce watch
```

This monitors file changes and provides instant feedback on TDD compliance.

## Implementation Notes

This skill uses:
- Git history analysis to track TDD cycle progression
- AST parsing for structure validation
- Coverage analysis tools for threshold checking
- Dependency analysis for test independence verification
- File modification tracking for implementation restriction

## Convention Enforcement

### Naming Conventions

**Enforced Rules:**
- Functions: snake_case (calculate_total_price)
- Classes: PascalCase (UserAuthentication)
- Constants: UPPER_SNAKE_CASE (MAX_LOGIN_ATTEMPTS)
- Private methods: _leading_underscore
- Minimum 3 characters for names
- Forbidden names: temp, data, info, obj, var, item

**Configuration:**
```json
{
  "conventions": {
    "naming": {
      "enforceSnakeCase": true,
      "enforcePascalCase": true,
      "enforceUpperSnakeCase": true,
      "minNameLength": 3,
      "forbiddenNames": ["temp", "data", "info", "obj", "var", "item"]
    }
  }
}
```

### Code Structure

**Enforced Rules:**
- Maximum 50 lines per function
- Maximum 10 cyclomatic complexity
- Maximum 5 parameters per function
- Maximum 4 levels of nesting
- Single responsibility per function
- Pure functions preferred (no side effects)

**Configuration:**
```json
{
  "conventions": {
    "structure": {
      "maxFunctionLines": 50,
      "maxComplexity": 10,
      "maxParameters": 5,
      "maxNestingDepth": 4
    }
  }
}
```

### Import Organization

**Enforced Rules:**
1. Standard library imports
2. Third-party imports
3. Local project imports
- Alphabetically sorted within each group
- No unused imports
- No duplicate imports

**Configuration:**
```json
{
  "conventions": {
    "imports": {
      "enforceOrganization": true,
      "checkUnused": true,
      "checkDuplicates": true,
      "groupOrder": ["stdlib", "third_party", "local"]
    }
  }
}
```

### Type Hints

**Enforced Rules:**
- All functions must have type hints
- Use project's type conventions
- Proper typing for complex types
- Type checking enabled

**Configuration:**
```json
{
  "conventions": {
    "typeHints": {
      "required": true,
      "strictMode": true
    }
  }
}
```

### Docstrings

**Enforced Rules:**
- Google-style or NumPy-style (based on project)
- All public functions documented
- Parameters and returns documented
- Raises documented
- Examples included where appropriate

**Configuration:**
```json
{
  "conventions": {
    "docstrings": {
      "style": "google",
      "requiredForPublic": true
    }
  }
}
```

## Code Conciseness Enforcement

### Clean Code Principles

**Enforced Principles:**
- **DRY** (Don't Repeat Yourself): No duplicate code
- **KISS** (Keep It Simple, Stupid): Prefer simple solutions
- **YAGNI** (You Aren't Gonna Need It): Avoid over-engineering
- **Single Responsibility**: One function = one purpose
- **Early Returns**: Reduce nesting depth with guard clauses
- **Expressive Code**: Code should be self-documenting

### Conciseness Rules

**Enforced Rules:**
- Prefer list comprehensions over for loops when appropriate
- Use built-in functions (map, filter, reduce, any, all) instead of manual implementations
- Avoid redundant code and unnecessary intermediate variables
- Prefer one-liners for simple operations without sacrificing readability
- Use ternary operators for simple conditional assignments
- Leverage language idioms and patterns

**Configuration:**
```json
{
  "conciseness": {
    "enabled": true,
    "preferComprehensions": true,
    "preferBuiltins": true,
    "maxIntermediateVariables": 3,
    "suggestOneLiners": true,
    "avoidOverEngineering": true,
    "enforceEarlyReturns": true,
    "preferTernaryOperators": true,
    "detectVerbosePatterns": true
  }
}
```

### Enforcement Examples

```
❌ Verbose - Can be simplified
result = []
for item in items:
    if item > 0:
        result.append(item)

✓ Concise - List comprehension
result = [item for item in items if item > 0]
```

```
❌ Verbose - Unnecessary intermediate variable
total = 0
for number in numbers:
    total = total + number
return total

✓ Concise - Built-in function
return sum(numbers)
```

```
❌ Verbose - Nested conditions
if x > 0:
    if y > 0:
        return True
    else:
        return False
else:
    return False

✓ Concise - Single expression
return x > 0 and y > 0
```

### Anti-Patterns Detection

**Detected Anti-Patterns:**
- Excessive intermediate variables (>3 per function)
- Verbose loops that could use comprehensions
- Manual implementations of built-in functionality
- Over-engineered solutions for simple problems
- Redundant conditional checks
- Unnecessary function wrapping

## Code Quality Enforcement

### Duplicate Code Detection

**Detection Rules:**
- Identical code blocks (100% match)
- Similar code blocks (≥80% similarity)
- Minimum 5 lines for duplicate consideration
- Suggests extraction to shared functions

**Configuration:**
```json
{
  "quality": {
    "duplicateCode": {
      "enabled": true,
      "minSimilarityScore": 0.8,
      "minLinesForDuplicate": 5,
      "ignoreTestFiles": true,
      "ignoreComments": true,
      "ignoreWhitespace": true
    }
  }
}
```

### Magic Literals

**Detection Rules:**
- Hardcoded numbers (excluding 0, 1, -1)
- Hardcoded strings (excluding empty string)
- Repeated literals (2+ occurrences)
- Requires extraction to named constants

**Configuration:**
```json
{
  "quality": {
    "magicLiterals": {
      "enabled": true,
      "minOccurrences": 2,
      "ignoreValues": [0, 1, -1, "", "null", "false", "true"],
      "extractNumbers": true,
      "extractStrings": true,
      "extractBooleans": false
    }
  }
}
```

### Dead Code Elimination

**Detection Rules:**
- Unused imports
- Unused variables
- Unused functions
- Unreachable code blocks

**Configuration:**
```json
{
  "quality": {
    "deadCode": {
      "enabled": true,
      "checkUnusedImports": true,
      "checkUnusedVariables": true,
      "checkUnusedFunctions": true,
      "checkUnusedClasses": true,
      "ignoreUnderscored": true
    }
  }
}
```

### Code Smells

**Detection Rules:**
- God functions (>200 lines, >15 complexity)
- Feature envy (using other object's data)
- Data clumps (variables appearing together)
- Primitive obsession (use domain objects)

**Configuration:**
```json
{
  "quality": {
    "codeSmells": {
      "enabled": true,
      "detectGodFunctions": true,
      "detectFeatureEnvy": true,
      "detectDataClumps": true,
      "detectPrimitiveObsession": true,
      "godFunctionThreshold": {
        "maxLines": 200,
        "maxComplexity": 15
      }
    }
  }
}
```

### Complex Conditionals

**Detection Rules:**
- Nested if/else (>3 levels)
- Complex boolean expressions (>3 conditions)
- Suggests guard clauses or early returns

**Configuration:**
```json
{
  "quality": {
    "complexConditionals": {
      "enabled": true,
      "maxNestingDepth": 3,
      "maxBooleanConditions": 3
    }
  }
}
```

## Enhanced Output Format

```
TDD Compliance Report
=====================

Overall Score: 87% (52/60 checks passed)

TDD CYCLE
---------
✓ Test Creation Phase (PASS)
✓ Test Failure (Red) (PASS)
✓ Minimal Implementation (Green) (PASS)
✗ Refactoring Phase (FAIL) - No refactoring detected after green

TEST COVERAGE
-------------
Component Coverage: 92% (Required: ≥90%) ✓
Integration Flow Coverage: 100% (Required: 100%) ✓
Safety Constraint Coverage: 95% (Required: 100%) ✗

CONVENTION COMPLIANCE
----------------------
Naming Conventions: 95% ✓
  ✓ Functions use snake_case
  ✓ Classes use PascalCase
  ✓ Constants use UPPER_SNAKE_CASE
  ✗ Found forbidden name 'temp' in utils.py:42

Code Structure: 88% ✓
  ✓ Functions within size limits
  ✓ Complexity acceptable
  ✗ Function process_data has 6 parameters (max: 5)
  ✗ Function validate_input has nesting depth 5 (max: 4)

Import Organization: 100% ✓
  ✓ Imports properly organized
  ✓ No unused imports
  ✓ No duplicate imports

Type Hints: 100% ✓
  ✓ All functions have type hints

Docstrings: 90% ✓
  ✓ Most public functions documented
  ✗ Missing docstring for helper_function

CODE CONCISENESS
----------------
Overall Score: 92% ✓
  ✓ Uses comprehensions appropriately
  ✓ Leverages built-in functions
  ✓ Minimal intermediate variables
  ✗ Verbose loop detected in data_processor.py:67
    Suggestion: Replace with list comprehension

CODE QUALITY
------------
Duplicate Code: 100% ✓
  ✓ No duplicate code detected

Magic Literals: 95% ✓
  ✓ Most constants extracted
  ✗ Magic number '3600' found in timer.py:23
    Suggestion: Extract to TIMEOUT_SECONDS constant

Dead Code: 100% ✓
  ✓ No unused imports
  ✓ No unused variables
  ✓ No unused functions

Code Smells: 98% ✓
  ✓ No god functions
  ✓ No feature envy
  ✓ No data clumps
  ✗ Primitive obsession detected in user.py
    Suggestion: Create User domain object

Complex Conditionals: 90% ✓
  ✓ Nesting depth acceptable
  ✗ Complex boolean expression found in validator.py:45
    Suggestion: Extract to named variable

RECURSION AND INFINITE LOOPS
-----------------------------
✗ Recursive function detected (FAIL) - Function calls itself
✓ All loops have explicit termination (PASS)
✓ Loop bounds defined with constants (PASS)
✗ Infinite loop pattern detected (FAIL) - while(true) found

VIOLATIONS
----------
1. Refactoring Phase (evo/src/decision_engine.rs)
   No refactoring detected after green phase
   Suggested: Review and refactor for code quality

2. Safety Constraint Coverage (evo/tests/safety_test.rs)
   Coverage: 95% (Required: 100%)
   Missing: storage_limit_enforcement
   Suggested: Add test for storage limit enforcement

3. Naming Convention (utils.py:42)
   Forbidden name 'temp' detected
   Suggested: Rename to descriptive name like 'buffer'

4. Code Structure (process_data)
   Too many parameters: 6 (max: 5)
   Suggested: Create parameter object or data class

5. Code Structure (validate_input)
   Excessive nesting: 5 levels (max: 4)
   Suggested: Use guard clauses to flatten

6. Docstrings (helper_function)
   Missing docstring for public function
   Suggested: Add Google-style docstring

7. Code Conciseness (data_processor.py:67)
   Verbose loop detected
   Suggested: Replace with list comprehension

8. Magic Literal (timer.py:23)
   Magic number '3600' found
   Suggested: Extract to TIMEOUT_SECONDS constant

9. Code Smell (user.py)
   Primitive obsession detected
   Suggested: Create User domain object

10. Complex Conditional (validator.py:45)
    Complex boolean expression
    Suggested: Extract to named variable

CRITICAL VIOLATIONS: 2 (Build will FAIL)
WARNINGS: 8
```

## Configuration

### Full Configuration Example

```json
{
  "tdd": {
    "enforceTestFirst": true,
    "requireTestFailure": true,
    "requireMinimalImplementation": true,
    "requireRefactoring": true,
    "testStructure": {
      "enforceArrangeActAssert": true,
      "maxAssertionsPerTest": 1,
      "minTestNameLength": 10
    },
    "coverageThresholds": {
      "lines": 90,
      "branches": 80,
      "functions": 90,
      "statements": 90
    },
    "criticalCoverage": {
      "integrationFlow": 100,
      "safetyConstraints": 100
    },
    "propertyBasedTesting": {
      "enabled": true,
      "frameworks": ["hypothesis", "fast-check", "jsverify"]
    }
  },
  "recursionDetection": {
    "enabled": true,
    "detectDirectRecursion": true,
    "detectIndirectRecursion": true,
    "detectTailRecursion": true,
    "blockRecursiveFunctions": true
  },
  "loopBounding": {
    "enabled": true,
    "requireExplicitTermination": true,
    "requireMaxIterationLimit": true,
    "requireTimeoutLimit": true,
    "defaultMaxIterations": 1000,
    "defaultTimeoutMs": 5000
  },
  "conventions": {
    "naming": {
      "enforceSnakeCase": true,
      "enforcePascalCase": true,
      "enforceUpperSnakeCase": true,
      "minNameLength": 3,
      "forbiddenNames": ["temp", "data", "info", "obj", "var", "item"]
    },
    "structure": {
      "maxFunctionLines": 50,
      "maxComplexity": 10,
      "maxParameters": 5,
      "maxNestingDepth": 4
    },
    "imports": {
      "enforceOrganization": true,
      "checkUnused": true,
      "checkDuplicates": true,
      "groupOrder": ["stdlib", "third_party", "local"]
    },
    "typeHints": {
      "required": true,
      "strictMode": true
    },
    "docstrings": {
      "style": "google",
      "requiredForPublic": true
    }
  },
  "conciseness": {
    "enabled": true,
    "preferComprehensions": true,
    "preferBuiltins": true,
    "maxIntermediateVariables": 3,
    "suggestOneLiners": true,
    "avoidOverEngineering": true,
    "enforceEarlyReturns": true,
    "preferTernaryOperators": true,
    "detectVerbosePatterns": true
  },
  "quality": {
    "duplicateCode": {
      "enabled": true,
      "minSimilarityScore": 0.8,
      "minLinesForDuplicate": 5,
      "ignoreTestFiles": true,
      "ignoreComments": true,
      "ignoreWhitespace": true
    },
    "magicLiterals": {
      "enabled": true,
      "minOccurrences": 2,
      "ignoreValues": [0, 1, -1, "", "null", "false", "true"],
      "extractNumbers": true,
      "extractStrings": true,
      "extractBooleans": false
    },
    "deadCode": {
      "enabled": true,
      "checkUnusedImports": true,
      "checkUnusedVariables": true,
      "checkUnusedFunctions": true,
      "checkUnusedClasses": true,
      "ignoreUnderscored": true
    },
    "codeSmells": {
      "enabled": true,
      "detectGodFunctions": true,
      "detectFeatureEnvy": true,
      "detectDataClumps": true,
      "detectPrimitiveObsession": true,
      "godFunctionThreshold": {
        "maxLines": 200,
        "maxComplexity": 15
      }
    },
    "complexConditionals": {
      "enabled": true,
      "maxNestingDepth": 3,
      "maxBooleanConditions": 3
    }
  },
  "reporting": {
    "includeAllCategories": true,
    "showViolationsByCategory": true,
    "provideFixSuggestions": true,
    "generateScore": true
  }
}
```

## Best Practices

1. Always write tests first
2. Ensure tests fail before implementation
3. Write minimal implementation to pass
4. Refactor after green phase
5. Keep tests independent and focused
6. Maintain high coverage (≥90% by default, configurable)
7. Update tests when behavior changes
8. Never use recursive algorithms - use iterative solutions
9. Always bound loops with explicit conditions and limits
10. Avoid while(true), for(;;), and infinite loops

## Iterative Over Recursive

**Why Iteration:**
- Predictable memory usage (no stack growth)
- No stack overflow risk
- Better performance (no function call overhead)
- Easier to debug and test
- More resource-efficient

**Common Patterns:**

**Factorial:**
```typescript
// ❌ Recursive
function factorial(n) { return n <= 1 ? 1 : n * factorial(n-1) }

// ✅ Iterative
function factorial(n) {
  let result = 1
  for (let i = 2; i <= n; i++) result *= i
  return result
}
```

**Tree Traversal:**
```typescript
// ❌ Recursive
function traverse(node) {
  if (!node) return
  console.log(node.value)
  traverse(node.left)
  traverse(node.right)
}

// ✅ Iterative (stack-based)
function traverse(root) {
  const stack = [root]
  while (stack.length > 0) {
    const node = stack.pop()
    console.log(node.value)
    if (node.right) stack.push(node.right)
    if (node.left) stack.push(node.left)
  }
}
```

**DFS/BFS:**
```typescript
// ❌ Recursive DFS
function dfs(node, target) {
  if (!node) return false
  if (node.value === target) return true
  return dfs(node.left, target) || dfs(node.right, target)
}

// ✅ Iterative DFS
function dfs(root, target) {
  const stack = [root]
  while (stack.length > 0) {
    const node = stack.pop()
    if (node.value === target) return true
    if (node.right) stack.push(node.right)
    if (node.left) stack.push(node.left)
  }
  return false
}
```

## Property-Based Testing

The skill supports property-based testing for edge case coverage:

```json
{
  "tddEnforce": {
    "enablePropertyBasedTesting": true,
    "propertyTestFrameworks": ["hypothesis", "fast-check", "jsverify"]
  }
}
```

**Property Test Validation:**
- Ensures property tests exist for critical functions
- Validates property test coverage (≥80% of critical paths)
- Checks for invariant preservation
- Validates edge case generation

**Example Property Test Requirements:**
```python
# Required property tests for critical functions
@pytest.mark.parametrize("input, expected", property_test_cases)
def test_property_preserves_invariant(input, expected):
    result = function_under_test(input)
    assert invariant_holds(result)
```