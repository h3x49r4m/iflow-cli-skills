# Project Analysis Guide

## Purpose
This guide explains how to analyze an existing Python project to understand its current structure, tools, and practices.

## Analysis Steps

### Step 1: Detect Project Structure

**Check Directory Layout:**
```bash
# List top-level directories
ls -la

# Look for common patterns:
# - Flat layout: mymodule.py, tests.py at root
# - src layout: src/mymodule/ at root
# - Package layout: mypackage/ at root
```

**Structure Patterns:**

| Pattern | Description | Detection |
|---------|-------------|-----------|
| **Flat** | All files at root level | No src/ or package/ directory, .py files at root |
| **src/** | Modern Python layout | src/ directory contains package code |
| **Package** | Traditional layout | Package directory at root (e.g., mypackage/) |
| **Mixed** | Inconsistent structure | Multiple patterns present |

**Analysis Commands:**
```bash
# Find Python files
find . -name "*.py" -type f | head -20

# Check for src directory
test -d src && echo "Uses src layout" || echo "No src directory"

# Check for package directory
find . -maxdepth 2 -name "__init__.py" -type f
```

### Step 2: Identify Package Manager

**Check for Package Files:**
```bash
# Look for package manager files
ls -la | grep -E "(pyproject.toml|setup.py|setup.cfg|requirements.txt|Pipfile|poetry.lock|uv.lock)"
```

**Package Manager Detection:**

| File(s) | Manager | Commands |
|---------|---------|----------|
| `pyproject.toml` + `uv.lock` | uv | `uv add`, `uv run`, `uv sync` |
| `pyproject.toml` + `poetry.lock` | Poetry | `poetry add`, `poetry run`, `poetry install` |
| `pyproject.toml` only | Modern/hatchling | `pip install -e .` |
| `setup.py` or `setup.cfg` | setuptools | `pip install -e .` |
| `requirements.txt` | pip | `pip install -r requirements.txt` |
| `Pipfile` | pipenv | `pipenv install` |

**Verify Dependencies:**
```bash
# For uv
uv pip list

# For poetry
poetry show

# For pip
pip list
```

### Step 3: Find Existing Test Framework

**Check for Test Files:**
```bash
# Find test files
find . -name "test_*.py" -o -name "*_test.py" | head -10

# Check for test directories
find . -type d -name "tests" -o -type d -name "test"
```

**Test Framework Detection:**

| Indicator | Framework | Detection |
|-----------|-----------|-----------|
| `import pytest` | pytest | Look in test files |
| `import unittest` | unittest | Look in test files |
| `import nose` | nose | Look in test files |
| `pytest.ini` or `pyproject.toml` with pytest config | pytest | Check config files |
| `tox.ini` | tox | Check config files |

**Analyze Test Structure:**
```bash
# Count test files
find . -name "test_*.py" -o -name "*_test.py" | wc -l

# Check test organization
tree tests/ 2>/dev/null || find tests/ -type f -name "*.py" | head -20
```

### Step 4: Locate Configuration Files

**Python Configuration:**
```bash
# Check for Python configuration
ls -la | grep -E "(pyproject.toml|setup.py|setup.cfg|tox.ini|.python-version|.flake8|.pylintrc|mypy.ini|.mypy.ini)"
```

**Configuration File Analysis:**

| File | Purpose | Check For |
|------|---------|-----------|
| `pyproject.toml` | Modern Python config | `[tool.*]` sections |
| `setup.py` | Legacy package config | `setup()` function |
| `tox.ini` | Multi-environment testing | `tox` commands |
| `.flake8` | flake8 linting config | flake8 settings |
| `.pylintrc` | pylint linting config | pylint settings |
| `mypy.ini` or `.mypy.ini` | mypy type checking config | mypy settings |
| `pytest.ini` | pytest config | pytest settings |

**Extract Configuration:**
```bash
# Show pyproject.toml (if exists)
cat pyproject.toml | grep -A 20 "\[tool\."

# Show pytest config
cat pytest.ini 2>/dev/null || grep -A 10 "\[tool.pytest\]" pyproject.toml 2>/dev/null

# Show mypy config
cat mypy.ini 2>/dev/null || grep -A 10 "\[tool.mypy\]" pyproject.toml 2>/dev/null
```

### Step 5: Count Test Coverage Baseline

**Check Coverage Tools:**
```bash
# Look for coverage configuration
grep -r "coverage" pyproject.toml setup.cfg tox.ini pytest.ini .coveragerc 2>/dev/null

# Check for coverage reports
find . -name ".coverage" -o -name "htmlcov" -o -name "*.cover"
```

**Run Coverage Check:**
```bash
# If pytest-cov is installed
pytest --cov=src --cov-report=term-missing 2>/dev/null

# If coverage.py is installed
coverage run -m pytest && coverage report 2>/dev/null
```

**Coverage Analysis:**
```
Key Metrics to Capture:
- Overall coverage percentage
- Module-level coverage
- Missing lines count
- Files with zero coverage
```

### Step 6: Analyze Code Quality Tools

**Check for Linting/Formatting:**
```bash
# Check for ruff
ls -la .ruff.toml ruff.toml 2>/dev/null || grep -A 5 "\[tool.ruff\]" pyproject.toml 2>/dev/null

# Check for black
grep -A 5 "\[tool.black\]" pyproject.toml 2>/dev/null

# Check for mypy
grep -A 5 "\[tool.mypy\]" pyproject.toml 2>/dev/null

# Check for pre-commit hooks
ls -la .pre-commit-config.yaml 2>/dev/null
```

**Tool Status:**

| Tool | Installed? | Configured? | Status |
|------|------------|-------------|--------|
| ruff | [ ] | [ ] | - |
| black | [ ] | [ ] | - |
| mypy | [ ] | [ ] | - |
| pylint | [ ] | [ ] | - |
| pre-commit | [ ] | [ ] | - |

### Step 7: Code Standards Assessment

**Check Code Style:**
```bash
# Count Python files
find . -name "*.py" -not -path "./tests/*" -not -path "./.*" | wc -l

# Sample a file to check conventions
head -50 src/__init__.py 2>/dev/null || head -50 *.py 2>/dev/null

# Check for type hints
grep -r "def " --include="*.py" src/ 2>/dev/null | grep -v "->" | wc -l

# Check for docstrings
grep -r '"""' --include="*.py" src/ 2>/dev/null | wc -l
```

**Standards Checklist:**
- [ ] PEP 8 indentation (4 spaces)
- [ ] Type hints present
- [ ] Docstrings for functions
- [ ] Snake_case naming
- [ ] Import ordering

### Step 8: Dependencies Analysis

**List Dependencies:**
```bash
# For uv
uv pip list

# For poetry
poetry show --tree

# For pip
pip list

# Check requirements files
cat requirements*.txt 2>/dev/null
```

**Categorize Dependencies:**
```
Production Dependencies:
- List main packages used

Development Dependencies:
- List testing tools
- List linting tools
- List type checking tools

Outdated Dependencies:
- Note any clearly outdated versions
```

### Step 9: Documentation Assessment

**Check Documentation:**
```bash
# Look for documentation
ls -la | grep -E "(README|CONTRIBUTING|CHANGELOG|docs/|doc/)"

# Check for docstring coverage
find . -name "*.py" -not -path "./tests/*" -exec grep -l '"""' {} \; | wc -l
```

**Documentation Status:**
- [ ] README.md present
- [ ] API documentation
- [ ] Installation instructions
- [ ] Usage examples
- [ ] Contributing guidelines

### Step 10: Git and CI/CD

**Check Git Configuration:**
```bash
# Check if git repo
git status 2>/dev/null && echo "Git repo" || echo "Not a git repo"

# Check for CI/CD
ls -la .github/ .gitlab-ci.yml .travis.yml .circleci/ 2>/dev/null
```

**CI/CD Status:**
- [ ] GitHub Actions
- [ ] GitLab CI
- [ ] Travis CI
- [ ] CircleCI
- [ ] None

## Analysis Report Template

```markdown
# Project Analysis Report

**Project Name**: _____________
**Analysis Date**: YYYY-MM-DD
**Analyzer**: _____________

## Project Structure

| Aspect | Current State |
|--------|---------------|
| Layout Type | [flat/src/package/mixed] |
| Source Location | _____________ |
| Test Location | _____________ |
| Config Files | _____________ |

## Package Management

| Aspect | Current State |
|--------|---------------|
| Manager | [uv/poetry/pip/setuptools] |
| Config File | _____________ |
| Dependencies Count | __ |
| Dev Dependencies Count | __ |

## Testing

| Aspect | Current State |
|--------|---------------|
| Framework | [pytest/unittest/none] |
| Test Files | __ |
| Test Organization | [flat/structured] |
| Coverage | __% |
| Coverage Tool | [pytest-cov/coverage.py/none] |

## Code Quality Tools

| Tool | Installed | Configured | Status |
|------|-----------|------------|--------|
| ruff | [ ]/[x] | [ ]/[x] | - |
| black | [ ]/[x] | [ ]/[x] | - |
| mypy | [ ]/[x] | [ ]/[x] | - |
| pre-commit | [ ]/[x] | [ ]/[x] | - |

## Code Standards

| Standard | Status |
|----------|--------|
| PEP 8 Compliance | [ ]/[x] |
| Type Hints | [ ]/[x] |
| Docstrings | [ ]/[x] |
| Naming Conventions | [ ]/[x] |

## Documentation

| Type | Status |
|------|--------|
| README | [ ]/[x] |
| API Docs | [ ]/[x] |
| Installation Guide | [ ]/[x] |
| Usage Examples | [ ]/[x] |

## CI/CD

| Type | Status |
|------|--------|
| GitHub Actions | [ ]/[x] |
| GitLab CI | [ ]/[x] |
| Other | _____________ |

## Summary

**Overall Compliance**: __% ([none/partial/compliant])

**Key Strengths**:
- _____________
- _____________

**Major Gaps**:
- _____________
- _____________

**Recommendations**:
1. _____________
2. _____________
3. _____________
```

## Analysis Commands Summary

```bash
# Quick analysis script
#!/bin/bash
echo "=== Project Structure ==="
ls -la | grep -E "^d"
echo ""
echo "=== Package Manager ==="
ls -la | grep -E "(pyproject.toml|setup.py|Pipfile|poetry.lock|uv.lock)"
echo ""
echo "=== Test Files ==="
find . -name "test_*.py" -o -name "*_test.py" | head -10
echo ""
echo "=== Config Files ==="
ls -la | grep -E "(pytest.ini|tox.ini|.flake8|mypy.ini|.pre-commit)"
echo ""
echo "=== Python Files Count ==="
find . -name "*.py" | wc -l
```

## Next Steps

After analysis:
1. Review compliance checklist
2. Perform gap analysis
3. Create migration plan
4. Prioritize alignment steps
5. Execute alignment incrementally