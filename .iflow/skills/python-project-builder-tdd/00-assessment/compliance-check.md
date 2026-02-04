# Compliance Checklist

## Purpose
This checklist verifies whether a Python project complies with the TDD skill standards.

## Compliance Areas

### 1. Directory Structure

**Standard Requirements:**
- [ ] Project uses `src/` directory for source code
- [ ] Tests are in `tests/` directory
- [ ] Tests are organized as `tests/unit/`, `tests/integration/`, `tests/e2e/`
- [ ] Configuration files at root level (`pyproject.toml`, `pytest.ini`)
- [ ] Documentation at root level (`README.md`, `FEATURES.md`, `TESTING.md`)

**Check Commands:**
```bash
# Check for src directory
test -d src && echo "✓ src/ exists" || echo "✗ src/ missing"

# Check for tests directory
test -d tests && echo "✓ tests/ exists" || echo "✗ tests/ missing"

# Check test organization
test -d tests/unit && echo "✓ tests/unit/ exists" || echo "✗ tests/unit/ missing"
test -d tests/integration && echo "✓ tests/integration/ exists" || echo "✗ tests/integration/ missing"
test -d tests/e2e && echo "✓ tests/e2e/ exists" || echo "✗ tests/e2e/ missing"

# Check for required docs
test -f README.md && echo "✓ README.md exists" || echo "✗ README.md missing"
test -f FEATURES.md && echo "✓ FEATURES.md exists" || echo "✗ FEATURES.md missing"
test -f TESTING.md && echo "✓ TESTING.md exists" || echo "✗ TESTING.md missing"
```

**Scoring:**
- 0-2 compliant: **Critical** - Must fix
- 3-4 compliant: **Important** - Should fix
- 5-6 compliant: **Good** - Minor improvements possible
- All compliant: **Excellent**

---

### 2. Package Management

**Standard Requirements:**
- [ ] Uses `uv` as package manager
- [ ] Has `pyproject.toml` configuration file
- [ ] Has `uv.lock` lock file
- [ ] Dependencies are properly declared in `[project.dependencies]`
- [ ] Dev dependencies in `[project.optional-dependencies.dev]`
- [ ] Build system configured with `hatchling`

**Check Commands:**
```bash
# Check for pyproject.toml
test -f pyproject.toml && echo "✓ pyproject.toml exists" || echo "✗ pyproject.toml missing"

# Check for uv.lock
test -f uv.lock && echo "✓ uv.lock exists" || echo "✗ uv.lock missing"

# Check pyproject.toml structure
grep -q "\[project\]" pyproject.toml && echo "✓ [project] section exists" || echo "✗ [project] section missing"
grep -q "uv" pyproject.toml && echo "✓ uv configured" || echo "✗ uv not configured"
grep -q "hatchling" pyproject.toml && echo "✓ hatchling configured" || echo "✗ hatchling not configured"

# Verify uv is installed
command -v uv >/dev/null && echo "✓ uv installed" || echo "✗ uv not installed"
```

**Scoring:**
- 0-2 compliant: **Critical** - Must migrate to uv
- 3-4 compliant: **Important** - Should complete setup
- 5-6 compliant: **Good** - Minor adjustments needed
- All compliant: **Excellent**

---

### 3. Testing Framework

**Standard Requirements:**
- [ ] Uses `pytest` as test framework
- [ ] Has pytest configuration (in `pyproject.toml` or `pytest.ini`)
- [ ] Test markers defined (unit, integration, e2e)
- [ ] Coverage measurement enabled with `pytest-cov`
- [ ] Test discovery configured correctly
- [ ] Tests follow naming convention (`test_*.py`)

**Check Commands:**
```bash
# Check for pytest in dependencies
grep -q "pytest" pyproject.toml && echo "✓ pytest in dependencies" || echo "✗ pytest not in dependencies"

# Check for pytest-cov
grep -q "pytest-cov" pyproject.toml && echo "✓ pytest-cov in dependencies" || echo "✗ pytest-cov not in dependencies"

# Check pytest configuration
grep -q "\[tool.pytest.ini_options\]" pyproject.toml && echo "✓ pytest configured in pyproject.toml" || \
test -f pytest.ini && echo "✓ pytest.ini exists" || echo "✗ pytest configuration missing"

# Check for markers
grep -q "markers" pyproject.toml && echo "✓ markers defined" || grep -q "markers" pytest.ini 2>/dev/null && echo "✓ markers defined" || echo "✗ markers not defined"

# Check test files
find tests -name "test_*.py" | wc -l | grep -q "[1-9]" && echo "✓ test files found" || echo "✗ no test files"

# Verify pytest can run
uv run pytest --collect-only >/dev/null 2>&1 && echo "✓ pytest can collect tests" || echo "✗ pytest cannot collect tests"
```

**Scoring:**
- 0-2 compliant: **Critical** - Must set up pytest
- 3-4 compliant: **Important** - Should complete configuration
- 5-6 compliant: **Good** - Minor improvements possible
- All compliant: **Excellent**

---

### 4. Test Organization

**Standard Requirements:**
- [ ] Unit tests in `tests/unit/` directory
- [ ] Integration tests in `tests/integration/` directory
- [ ] E2E tests in `tests/e2e/` directory
- [ ] Test directory mirrors `src/` structure for unit tests
- [ ] `conftest.py` exists with shared fixtures
- [ ] `__init__.py` files exist in test directories

**Check Commands:**
```bash
# Check test directories
test -d tests/unit && echo "✓ tests/unit/ exists" || echo "✗ tests/unit/ missing"
test -d tests/integration && echo "✓ tests/integration/ exists" || echo "✗ tests/integration/ missing"
test -d tests/e2e && echo "✓ tests/e2e/ exists" || echo "✗ tests/e2e/ missing"

# Check for conftest.py
test -f tests/conftest.py && echo "✓ conftest.py exists" || echo "✗ conftest.py missing"

# Check for __init__.py files
test -f tests/__init__.py && echo "✓ tests/__init__.py exists" || echo "✗ tests/__init__.py missing"
test -f tests/unit/__init__.py && echo "✓ tests/unit/__init__.py exists" || echo "✗ tests/unit/__init__.py missing"
test -f tests/integration/__init__.py && echo "✓ tests/integration/__init__.py exists" || echo "✗ tests/integration/__init__.py missing"
test -f tests/e2e/__init__.py && echo "✓ tests/e2e/__init__.py exists" || echo "✗ tests/e2e/__init__.py missing"

# Count tests by type
echo "Unit tests: $(find tests/unit -name 'test_*.py' 2>/dev/null | wc -l)"
echo "Integration tests: $(find tests/integration -name 'test_*.py' 2>/dev/null | wc -l)"
echo "E2E tests: $(find tests/e2e -name 'test_*.py' 2>/dev/null | wc -l)"
```

**Scoring:**
- 0-2 compliant: **Critical** - Must reorganize tests
- 3-4 compliant: **Important** - Should complete organization
- 5-6 compliant: **Good** - Minor adjustments needed
- All compliant: **Excellent**

---

### 5. Test Coverage

**Standard Requirements:**
- [ ] Minimum 80% overall coverage
- [ ] Coverage measured with `pytest-cov`
- [ ] Coverage report configured (term-missing, html)
- [ ] Coverage excludes appropriate files (tests, __init__.py)
- [ ] Coverage tracked over time
- [ ] Critical paths have higher coverage

**Check Commands:**
```bash
# Check for pytest-cov
grep -q "pytest-cov" pyproject.toml && echo "✓ pytest-cov available" || echo "✗ pytest-cov not available"

# Run coverage
uv run pytest --cov=src --cov-report=term-missing --cov-report=html 2>/dev/null | grep -E "TOTAL|coverage" || echo "✗ Cannot run coverage"

# Check coverage configuration
grep -q "\[tool.coverage\]" pyproject.toml && echo "✓ coverage configured" || echo "✗ coverage not configured"

# Check for coverage exclusions
grep -q "omit" pyproject.toml && echo "✓ coverage exclusions defined" || echo "✗ coverage exclusions not defined"
```

**Scoring:**
- Coverage < 50%: **Critical** - Must improve
- Coverage 50-70%: **Important** - Should improve
- Coverage 70-80%: **Good** - Approaching target
- Coverage ≥ 80%: **Excellent** - Meets standard

---

### 6. Code Standards

**Standard Requirements:**
- [ ] PEP 8 compliant (checked with ruff)
- [ ] Type hints present for all functions
- [ ] Docstrings for all public functions/classes
- [ ] Follows naming conventions (snake_case, PascalCase)
- [ ] Imports ordered correctly
- [ ] Line length ≤ 79 characters

**Check Commands:**
```bash
# Check for ruff
grep -q "ruff" pyproject.toml && echo "✓ ruff in dependencies" || echo "✗ ruff not in dependencies"

# Run ruff check
uv run ruff check src 2>/dev/null && echo "✓ ruff check passes" || echo "✗ ruff check fails"

# Check for type hints
grep -r "def " --include="*.py" src/ | grep -v "->" | wc -l | grep -q "^0$" && echo "✓ type hints present" || echo "✗ type hints missing"

# Check for docstrings
find src -name "*.py" -exec grep -l '"""' {} \; | wc -l | grep -q "[1-9]" && echo "✓ docstrings present" || echo "✗ docstrings missing"

# Check line length
uv run ruff check src --select E501 2>/dev/null | grep -q "src/" && echo "✗ line length issues found" || echo "✓ no line length issues"
```

**Scoring:**
- 0-2 compliant: **Critical** - Major standards violations
- 3-4 compliant: **Important** - Should improve
- 5-6 compliant: **Good** - Minor violations
- All compliant: **Excellent**

---

### 7. Code Quality Tools

**Standard Requirements:**
- [ ] `ruff` configured for linting
- [ ] `black` configured for formatting
- [ ] `mypy` configured for type checking
- [ ] Pre-commit hooks configured
- [ ] Tools configured in `pyproject.toml`
- [ ] All tools can run successfully

**Check Commands:**
```bash
# Check for tools in dependencies
grep -q "ruff" pyproject.toml && echo "✓ ruff available" || echo "✗ ruff not available"
grep -q "black" pyproject.toml && echo "✓ black available" || echo "✗ black not available"
grep -q "mypy" pyproject.toml && echo "✓ mypy available" || echo "✗ mypy not available"

# Check for tool configuration
grep -q "\[tool.ruff\]" pyproject.toml && echo "✓ ruff configured" || echo "✗ ruff not configured"
grep -q "\[tool.black\]" pyproject.toml && echo "✓ black configured" || echo "✗ black not configured"
grep -q "\[tool.mypy\]" pyproject.toml && echo "✓ mypy configured" || echo "✗ mypy not configured"

# Check for pre-commit
test -f .pre-commit-config.yaml && echo "✓ pre-commit configured" || echo "✗ pre-commit not configured"

# Test tools
uv run ruff check src 2>/dev/null && echo "✓ ruff works" || echo "✗ ruff fails"
uv run black --check src 2>/dev/null && echo "✓ black passes" || echo "✗ black fails"
uv run mypy src 2>/dev/null && echo "✓ mypy passes" || echo "✗ mypy fails"
```

**Scoring:**
- 0-2 compliant: **Critical** - Must set up tools
- 3-4 compliant: **Important** - Should complete setup
- 5-6 compliant: **Good** - Minor adjustments needed
- All compliant: **Excellent**

---

### 8. Documentation

**Standard Requirements:**
- [ ] `README.md` exists with project description
- [ ] `FEATURES.md` documents implemented features
- [ ] `TESTING.md` documents testing approach
- [ ] `QUALITY.md` documents quality standards
- [ ] Installation instructions clear
- [ ] Usage examples provided

**Check Commands:**
```bash
# Check for documentation files
test -f README.md && echo "✓ README.md exists" || echo "✗ README.md missing"
test -f FEATURES.md && echo "✓ FEATURES.md exists" || echo "✗ FEATURES.md missing"
test -f TESTING.md && echo "✓ TESTING.md exists" || echo "✗ TESTING.md missing"
test -f QUALITY.md && echo "✓ QUALITY.md exists" || echo "✗ QUALITY.md missing"

# Check README content
grep -q "# " README.md && echo "✓ README has title" || echo "✗ README missing title"
grep -qi "install" README.md && echo "✓ README has installation info" || echo "✗ README missing installation"
grep -qi "usage" README.md && echo "✓ README has usage info" || echo "✗ README missing usage"
```

**Scoring:**
- 0-2 compliant: **Important** - Should add documentation
- 3-4 compliant: **Good** - Documentation present
- 5-6 compliant: **Excellent** - Complete documentation
- All compliant: **Excellent**

---

### 9. TDD Workflow

**Standard Requirements:**
- [ ] Tests written before implementation (for new code)
- [ ] TDD cycle followed (Red-Green-Refactor)
- [ ] Test-driven development documented in workflow
- [ ] All features have tests
- [ ] Tests drive design
- [ ] Refactoring done with test safety

**Check Commands:**
```bash
# Check test-to-code ratio
echo "Python files: $(find src -name '*.py' | wc -l)"
echo "Test files: $(find tests -name 'test_*.py' | wc -l)"

# Check for TDD documentation
grep -r "TDD\|test-driven" . --include="*.md" | grep -q "." && echo "✓ TDD documented" || echo "✗ TDD not documented"

# Check if tests exist for main modules
for module in $(find src -name "*.py" -not -name "__init__.py"); do
  test_name=$(basename $module | sed 's/\.py$/_test.py/')
  test_name_alt="test_$(basename $module)"
  if find tests -name "$test_name" -o -name "$test_name_alt" | grep -q .; then
    echo "✓ Test found for $module"
  else
    echo "✗ No test for $module"
  fi
done
```

**Scoring:**
- 0-2 compliant: **Critical** - TDD not practiced
- 3-4 compliant: **Important** - Should adopt TDD
- 5-6 compliant: **Good** - TDD partially adopted
- All compliant: **Excellent** - Full TDD adoption

---

### 10. State Management

**Standard Requirements:**
- [ ] `.state/` directory exists
- [ ] `project-state.md` tracks overall status
- [ ] `current-feature.md` tracks active work
- [ ] `next-steps.md` tracks upcoming work
- [ ] `completed-checklist.md` tracks completed items
- [ ] Checkpoints directory exists

**Check Commands:**
```bash
# Check for state directory
test -d .state && echo "✓ .state/ exists" || echo "✗ .state/ missing"

# Check for state files
test -f .state/project-state.md && echo "✓ project-state.md exists" || echo "✗ project-state.md missing"
test -f .state/current-feature.md && echo "✓ current-feature.md exists" || echo "✗ current-feature.md missing"
test -f .state/next-steps.md && echo "✓ next-steps.md exists" || echo "✗ next-steps.md missing"
test -f .state/completed-checklist.md && echo "✓ completed-checklist.md exists" || echo "✗ completed-checklist.md missing"

# Check for checkpoints
test -d .state/checkpoints && echo "✓ checkpoints/ exists" || echo "✗ checkpoints/ missing"

# Check for context directory
test -d .state/context && echo "✓ context/ exists" || echo "✗ context/ missing"
```

**Scoring:**
- 0-2 compliant: **Important** - Should set up state management
- 3-4 compliant: **Good** - State management partially set up
- 5-6 compliant: **Excellent** - Complete state management
- All compliant: **Excellent**

---

## Overall Compliance Score

### Calculation
For each compliance area, assign points:
- **Excellent**: 10 points
- **Good**: 7 points
- **Important**: 4 points
- **Critical**: 0 points

**Total Score = Sum of all area scores / 100**

### Compliance Levels

| Score | Level | Description |
|-------|-------|-------------|
| 90-100 | Fully Compliant | Project meets all standards |
| 70-89 | Mostly Compliant | Minor gaps, can continue development |
| 50-69 | Partially Compliant | Significant gaps, alignment needed |
| 0-49 | Non-Compliant | Major gaps, alignment required before development |

### Quick Compliance Check Script

```bash
#!/bin/bash
score=0

# Directory structure
if [ -d "src" ] && [ -d "tests/unit" ] && [ -d "tests/integration" ] && [ -d "tests/e2e" ]; then
  score=$((score + 10))
  echo "✓ Directory structure: 10/10"
else
  echo "✗ Directory structure: 0/10"
fi

# Package management
if [ -f "pyproject.toml" ] && [ -f "uv.lock" ]; then
  score=$((score + 10))
  echo "✓ Package management: 10/10"
else
  echo "✗ Package management: 0/10"
fi

# Testing framework
if grep -q "pytest" pyproject.toml && grep -q "pytest-cov" pyproject.toml; then
  score=$((score + 10))
  echo "✓ Testing framework: 10/10"
else
  echo "✗ Testing framework: 0/10"
fi

# Code quality tools
if grep -q "ruff" pyproject.toml && grep -q "black" pyproject.toml && grep -q "mypy" pyproject.toml; then
  score=$((score + 10))
  echo "✓ Code quality tools: 10/10"
else
  echo "✗ Code quality tools: 0/10"
fi

echo ""
echo "Total Score: $score/100"

if [ $score -ge 90 ]; then
  echo "Compliance Level: Fully Compliant"
elif [ $score -ge 70 ]; then
  echo "Compliance Level: Mostly Compliant"
elif [ $score -ge 50 ]; then
  echo "Compliance Level: Partially Compliant"
else
  echo "Compliance Level: Non-Compliant"
fi
```

---

## Next Steps After Compliance Check

1. **If Fully Compliant (90-100)**:
   - Continue development following TDD workflow
   - Maintain standards in all new code

2. **If Mostly Compliant (70-89)**:
   - Address minor gaps
   - Plan incremental improvements
   - Can continue development while fixing gaps

3. **If Partially Compliant (50-69)**:
   - Create migration plan
   - Prioritize high-impact improvements
   - Align critical areas first

4. **If Non-Compliant (0-49)**:
   - Perform full gap analysis
   - Create comprehensive migration plan
   - Align project before development