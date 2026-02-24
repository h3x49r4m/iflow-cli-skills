---
name: dev-enforce
description: Unified development enforcement combining TDD workflow and project convention compliance
version: 1.0.0
category: development-process
---

# Dev-Enforce Skill

Unified development enforcement that combines Test-Driven Development (TDD) workflow with project convention compliance. Provides a single command interface for the entire development cycle from feature analysis to compliant code generation.

## Usage

```
/dev-enforce <request>
```

Where `<request>` is a natural language description of:
- A new feature to implement
- A bug to fix
- Code to refactor
- Any development task

## What It Does

### Integrated Development Workflow

When you invoke `/dev-enforce "add user authentication"`, the skill:

1. **Understand Request**
   - Parses natural language request
   - Identifies task type (feature, bug fix, refactor)
   - Extracts key requirements and constraints

2. **Analyze Codebase**
   - Searches for similar existing implementations
   - Identifies related files and modules
   - Discovers existing utilities and helpers
   - Learns project conventions and patterns

3. **Create Development Plan**
   - Determines files to create/modify
   - Selects appropriate patterns to follow
   - Identifies tests to write
   - Finds utilities to reuse

4. **Execute TDD Cycle**
   - **Red Phase**: Write test following project conventions
   - **Green Phase**: Write minimal implementation matching patterns
   - **Refactor Phase**: Improve code while maintaining consistency

5. **Validate Compliance**
   - TDD cycle completeness
   - Convention adherence
   - Code quality metrics
   - Duplicate code detection

6. **Generate Report**
   - What was done and why
   - Files changed
   - Tests added
   - Patterns used
   - Validation results

## Output Format

```
/dev-enforce "add user authentication with JWT tokens"

==================================================
DEV-ENFORCE: Development Compliance Report
==================================================

Request: add user authentication with JWT tokens
Type: New Feature
Status: ✓ Complete

--------------------------------------------------
ANALYSIS
--------------------------------------------------

Similar Patterns Found:
  - auth/token_manager.py (JWT token handling)
  - auth/password_hasher.py (password utilities)
  - tests/test_auth.py (auth test patterns)

Project Conventions:
  - Use bcrypt for password hashing
  - JWT tokens for session management
  - Async/await for all auth operations
  - Pydantic models for request/response validation

Existing Utilities:
  - token_utils.py (generate_token, validate_token)
  - password_hasher.py (hash_password, verify_password)
  - auth_middleware.py (authentication middleware)

--------------------------------------------------
DEVELOPMENT PLAN
--------------------------------------------------

Files to Create:
  - tests/test_user_auth.py (test patterns from test_auth.py)
  - auth/user_auth.py (auth patterns from token_manager.py)

Files to Modify:
  - auth/__init__.py (add exports)

Patterns to Follow:
  - Test structure: Arrange-Act-Assert
  - Error handling: CustomAuthException
  - Logging: auth_logger with DEBUG/INFO/ERROR levels
  - API response: standardized JSON format

--------------------------------------------------
TDD CYCLE EXECUTION
--------------------------------------------------

Phase 1: RED (Write Test)
  ✓ Test file created: tests/test_user_auth.py
  ✓ Test structure follows project conventions
  ✓ Test fails as expected (red state confirmed)

Phase 2: GREEN (Minimal Implementation)
  ✓ Implementation file created: auth/user_auth.py
  ✓ Minimal code to pass test
  ✓ Test passes (green state achieved)

Phase 3: REFACTOR (Improve Code)
  ✓ Code improved for readability
  ✓ Patterns maintained with existing code
  ✓ No behavior changes
  ✓ Tests still pass

--------------------------------------------------
VALIDATION RESULTS
--------------------------------------------------

TDD Compliance:
  ✓ Test-first workflow followed
  ✓ Minimal implementation
  ✓ Refactoring completed
  ✓ All tests passing

Convention Compliance:
  ✓ Naming conventions matched
  ✓ API patterns consistent
  ✓ Error handling aligned
  ✓ Logging format correct
  ✓ Type hints included
  ✓ Docstrings follow project style

Code Conciseness:
  ✓ Uses list comprehensions over loops
  ✓ Leverages built-in functions
  ✓ No redundant code
  ✓ Minimal intermediate variables
  ✓ Simple, readable solutions
  ✓ Avoids over-engineering

Code Quality:
  ✓ No duplicate code detected
  ✓ No magic literals
  ✓ Functions within size limits
  ✓ Complexity acceptable
  ✓ All imports used
  ✓ No dead code

Overall Score: 98% (59/60 checks passed)

--------------------------------------------------
FILES CHANGED
--------------------------------------------------

Created:
  - tests/test_user_auth.py (145 lines)
    * TestUserAuth class
    * test_login_success
    * test_login_invalid_credentials
    * test_token_validation
    * test_password_hashing

  - auth/user_auth.py (89 lines)
    * UserAuth class
    * login() method
    * validate_token() method
    * hash_password() method

Modified:
  - auth/__init__.py (+2 lines)
    * Added UserAuth export
    * Added user_auth import

--------------------------------------------------
PATTERNS USED
--------------------------------------------------

Import Organization:
  from fastapi import HTTPException
  from pydantic import BaseModel
  from auth.token_utils import generate_token, validate_token
  from auth.password_hasher import hash_password, verify_password

Error Handling:
  raise HTTPException(
      status_code=401,
      detail="Invalid credentials",
      headers={"WWW-Authenticate": "Bearer"}
  )

Logging Pattern:
  auth_logger.info(f"User login attempt: {username}")
  auth_logger.error(f"Login failed: {username}")

API Response:
  return {
      "access_token": token,
      "token_type": "bearer",
      "user_id": user.id
  }

--------------------------------------------------
NEXT STEPS
--------------------------------------------------

1. Review the generated code
2. Run tests: uv run pytest tests/test_user_auth.py -v
3. Commit changes: /git-manage commit feat: add user authentication

==================================================
READY TO COMMIT
==================================================
```

## Enforcement Rules

### TDD Workflow Enforcement

**Test-First Lock:**
- Implementation files cannot be created without corresponding test files
- Tests must fail before implementation (red phase verification)
- Only minimal implementation allowed to pass test (green phase verification)
- Refactoring required after green phase (refactor phase verification)

**Test Structure Validation:**
- Arrange-Act-Assert pattern required
- Single assertion per test
- Descriptive test names (test_<function>_<scenario>)
- Test independence enforced
- No test interdependencies allowed

### Convention Enforcement

**Naming Conventions:**
- Functions: snake_case (calculate_total_price)
- Classes: PascalCase (UserAuthentication)
- Constants: UPPER_SNAKE_CASE (MAX_LOGIN_ATTEMPTS)
- Private methods: _leading_underscore
- Minimum 3 characters for names
- Forbidden names: temp, data, info, obj, var, item

**Code Structure:**
- Maximum 50 lines per function
- Maximum 10 cyclomatic complexity
- Maximum 5 parameters per function
- Maximum 4 levels of nesting
- Single responsibility per function
- Pure functions preferred (no side effects)

**Import Organization:**
1. Standard library imports
2. Third-party imports
3. Local project imports
- Alphabetically sorted within each group
- No unused imports
- No duplicate imports

**Error Handling:**
- Use project's custom exceptions
- Consistent error response format
- Proper error logging
- Meaningful error messages
- Appropriate HTTP status codes

**Logging:**
- Use project's logger instances
- Consistent log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Structured log messages
- Include context information
- Sensitive data redaction

**Type Hints:**
- All functions must have type hints
- Use project's type conventions
- Proper typing for complex types
- Type checking enabled

**Docstrings:**
- Google-style or NumPy-style (based on project)
- All public functions documented
- Parameters and returns documented
- Raises documented
- Examples included where appropriate

### Code Conciseness Enforcement

**Clean Code Principles:**
- **DRY** (Don't Repeat Yourself): No duplicate code
- **KISS** (Keep It Simple, Stupid): Prefer simple solutions
- **YAGNI** (You Aren't Gonna Need It): Avoid over-engineering
- **Single Responsibility**: One function = one purpose
- **Early Returns**: Reduce nesting depth with guard clauses
- **Expressive Code**: Code should be self-documenting

**Conciseness Rules:**
- Prefer list comprehensions over for loops when appropriate
- Use built-in functions (map, filter, reduce, any, all) instead of manual implementations
- Avoid redundant code and unnecessary intermediate variables
- Prefer one-liners for simple operations without sacrificing readability
- Use ternary operators for simple conditional assignments
- Leverage Python idioms and patterns

**Enforcement Examples:**

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
❌ Verbose - Manual filtering
filtered = []
for item in items:
    if condition(item):
        filtered.append(item)

✓ Concise - Built-in filter
filtered = list(filter(condition, items))
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

```
❌ Over-engineered - Unnecessary complexity
def calculate_average(numbers):
    if not numbers:
        return None
    else:
        total = sum(numbers)
        count = len(numbers)
        average = total / count
        return average

✓ Clean - Simple and direct
def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else None
```

**Anti-Patterns Detection:**
- Excessive intermediate variables (>3 per function)
- Verbose loops that could use comprehensions
- Manual implementations of built-in functionality
- Over-engineered solutions for simple problems
- Redundant conditional checks
- Unnecessary function wrapping

**Simplification Suggestions:**
- Replace loops with comprehensions where appropriate
- Use built-in functions instead of manual implementations
- Reduce intermediate variables
- Apply guard clauses to reduce nesting
- Choose the most readable concise option

### Code Quality Enforcement

**Duplicate Code Detection:**
- Identical code blocks (100% match)
- Similar code blocks (≥80% similarity)
- Minimum 5 lines for duplicate consideration
- Suggests extraction to shared functions

**Magic Literals:**
- Hardcoded numbers (excluding 0, 1, -1)
- Hardcoded strings (excluding empty string)
- Repeated literals (2+ occurrences)
- Requires extraction to named constants

**Dead Code Elimination:**
- Unused imports
- Unused variables
- Unused functions
- Unreachable code blocks

**Code Smells:**
- God functions (>200 lines, >15 complexity)
- Feature envy (using other object's data)
- Data clumps (variables appearing together)
- Primitive obsession (use domain objects)

**Complex Conditionals:**
- Nested if/else (>3 levels)
- Complex boolean expressions (>3 conditions)
- Suggests guard clauses or early returns

## Configuration

### TDD Configuration

```json
{
  "devEnforce": {
    "tdd": {
      "enforceTestFirst": true,
      "requireTestFailure": true,
      "requireMinimalImplementation": true,
      "requireRefactoring": true,
      "testStructure": {
        "enforceArrangeActAssert": true,
        "maxAssertionsPerTest": 1,
        "minTestNameLength": 10
      }
    }
  }
}
```

### Convention Configuration

```json
{
  "devEnforce": {
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
        "checkDuplicates": true
      },
      "typeHints": {
        "required": true,
        "strictMode": true
      },
      "docstrings": {
        "style": "google",
        "requiredForPublic": true
      }
    }
  }
}
```

### Conciseness Configuration

```json
{
  "devEnforce": {
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
}
```

### Code Quality Configuration

```json
{
  "devEnforce": {
    "quality": {
      "duplicateCode": {
        "enabled": true,
        "minSimilarityScore": 0.8,
        "minLinesForDuplicate": 5
      },
      "magicLiterals": {
        "enabled": true,
        "minOccurrences": 2,
        "ignoreValues": [0, 1, -1, "", "null"]
      },
      "deadCode": {
        "enabled": true,
        "checkUnusedImports": true,
        "checkUnusedVariables": true,
        "checkUnusedFunctions": true
      },
      "codeSmells": {
        "enabled": true,
        "detectGodFunctions": true,
        "detectFeatureEnvy": true,
        "detectDataClumps": true
      },
      "complexConditionals": {
        "enabled": true,
        "maxNestingDepth": 3,
        "maxBooleanConditions": 3
      }
    }
  }
}
```

### Coverage Configuration

```json
{
  "devEnforce": {
    "coverage": {
      "thresholds": {
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
}
```

## Exit Codes

- `0` - All checks passed, code ready to commit
- `1` - Critical violations found (must fix before proceeding)
- `2` - Warnings only (can proceed with caution)
- `3` - TDD cycle incomplete
- `4` - Convention violations detected
- `5` - Code quality issues detected
- `6` - Coverage below threshold
- `7` - Analysis failed (unable to find patterns)

## Integration with Other Skills

### git-manage Integration

The skill integrates seamlessly with git-manage for committing:

```bash
/dev-enforce "add user authentication"
# ... generates code ...
/git-manage commit feat: add user authentication
```

### tdd-enforce Integration

The skill incorporates all TDD enforcement rules from tdd-enforce:

- Test-first workflow
- Red-green-refactor cycle
- Test structure validation
- Coverage thresholds
- Property-based testing

### refactor Integration

The skill uses refactor skill capabilities for:

- Code pattern matching
- Duplicate detection
- Code smell identification
- Refactoring suggestions

## Best Practices

### Before Using dev-enforce

1. **Have a clear request** - Be specific about what you want to implement
2. **Review the plan** - Check the generated development plan before execution
3. **Understand the patterns** - Review the patterns that will be used

### During Development

1. **Review generated code** - Always review the auto-generated code
2. **Run tests** - Execute tests to verify everything works
3. **Check compliance** - Verify all conventions are followed
4. **Iterate if needed** - Request refinements if code doesn't meet expectations

### After Development

1. **Run full test suite** - Ensure no regressions
2. **Check coverage** - Verify coverage meets thresholds
3. **Review changes** - Look at all modified files
4. **Commit with git-manage** - Use conventional commit format

### Writing Short and Clean Code

**Conciseness Principles:**
1. **Prefer comprehensions** - Use list/dict/set comprehensions over loops
2. **Leverage built-ins** - Use sum(), max(), min(), any(), all() instead of manual implementation
3. **Reduce nesting** - Use guard clauses and early returns
4. **Eliminate redundancy** - Remove duplicate code and unnecessary variables
5. **Simplify conditionals** - Use ternary operators for simple cases
6. **Be expressive** - Write self-documenting code that reads like English

**Anti-Patterns to Avoid:**
- Unnecessary intermediate variables (keep ≤3 per function)
- Verbose loops when comprehensions are clearer
- Manual implementations of built-in functions
- Over-engineered solutions for simple problems
- Deep nesting (use early returns to flatten)
- Redundant checks and conditions

**Clean Code Checklist:**
- ✓ Function does one thing well
- ✓ Name describes what it does
- ✓ No more than 50 lines
- ✓ No more than 5 parameters
- ✓ No more than 4 levels of nesting
- ✓ Uses built-in functions when possible
- ✓ Avoids code duplication
- ✓ Reads naturally from top to bottom

## Examples

### Feature Implementation

```bash
/dev-enforce "add user registration with email verification"
```

### Bug Fix

```bash
/dev-enforce "fix memory leak in data processing pipeline"
```

### Refactoring

```bash
/dev-enforce "refactor user service to use repository pattern"
```

### API Endpoint

```bash
/dev-enforce "add REST API endpoint for user profile management"
```

### Database Integration

```bash
/dev-enforce "add database migration for user preferences table"
```

## Implementation Notes

This skill uses:
- **explore-agent** for codebase analysis and pattern discovery
- **search_file_content** and **glob** for finding similar code
- **read_file** for understanding existing implementations
- **write_file** and **replace** for code generation
- **run_shell_command** for test execution and validation
- AST parsing for code structure analysis
- Git history analysis for pattern learning
- Configuration files for customizable rules and thresholds

## Workflow Integration

The skill integrates with the standard development workflow:

```
1. /dev-enforce "implement feature"
   → Analyzes, plans, implements, validates

2. Review generated code
   → Manual review and adjustment if needed

3. Run tests
   → Verify functionality

4. /git-manage commit feat: implement feature
   → Commit with conventional format

5. /git-manage push origin main
   → Push to remote
```

## Advantages

1. **Single Command** - One command handles entire development cycle
2. **Convention Compliance** - Automatically follows project patterns
3. **TDD Enforcement** - Ensures test-driven development
4. **Code Quality** - Validates quality metrics automatically
5. **No Duplicates** - Prevents duplicate code creation
6. **Consistent Style** - Maintains consistent code style
7. **Fast Development** - Accelerates development while maintaining quality
8. **Learning** - Learns project patterns over time