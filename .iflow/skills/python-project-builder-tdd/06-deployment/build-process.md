# Build Process Guide

## Purpose
This guide explains how to build a Python project using uv and prepare it for deployment.

## Build Process Overview

### Build Steps
1. **Prepare Environment**: Set up build environment
2. **Install Dependencies**: Install production dependencies
3. **Run Tests**: Verify all tests pass
4. **Type Check**: Run type checker
5. **Lint**: Run linter and formatter
6. **Build Package**: Create distributable package
7. **Verify Build**: Verify build output
8. **Generate Artifacts**: Generate deployment artifacts

## Using uv for Building

### uv Build Commands

```bash
# Build the project
uv build

# Build in release mode (optimized)
uv build --release

# Build with specific Python version
uv build --python 3.11

# Build with verbose output
uv build -v
```

### Build Output

When you run `uv build`, it creates:
- `dist/` directory containing:
  - `<project-name>-<version>.tar.gz` (source distribution)
  - `<project_name>-<version>-py3-none-any.whl` (wheel)

## pyproject.toml Configuration

### Minimum Configuration

```toml
[project]
name = "my-project"
version = "0.1.0"
description = "My project description"
readme = "README.md"
requires-python = ">=3.11"
authors = [
    {name = "Author Name", email = "author@example.com"}
]
dependencies = [
    "fastapi>=0.104.0",
    "uvicorn>=0.24.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",
    "ruff>=0.1.0",
    "mypy>=1.7.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

### Complete Configuration

```toml
[project]
name = "my-project"
version = "0.1.0"
description = "My project description"
readme = "README.md"
requires-python = ">=3.11"
license = {text = "MIT"}
authors = [
    {name = "Author Name", email = "author@example.com"}
]
maintainers = [
    {name = "Maintainer Name", email = "maintainer@example.com"}
]
keywords = ["task", "management", "todo"]
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
]
dependencies = [
    "fastapi>=0.104.0",
    "uvicorn>=0.24.0",
    "pydantic>=2.5.0",
    "sqlalchemy>=2.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",
    "pytest-asyncio>=0.21.0",
    "ruff>=0.1.0",
    "mypy>=1.7.0",
]
test = [
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",
]
docs = [
    "mkdocs>=1.5.0",
    "mkdocs-material>=9.4.0",
]

[project.scripts]
my-project = "my_project.cli:main"

[project.urls]
Homepage = "https://github.com/username/my-project"
Documentation = "https://my-project.readthedocs.io"
Repository = "https://github.com/username/my-project"
"Bug Tracker" = "https://github.com/username/my-project/issues"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/my_project"]

[tool.hatch.build.targets.sdist]
include = [
    "/src",
    "/tests",
    "/README.md",
    "/LICENSE",
]

[tool.ruff]
line-length = 79
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "I", "N", "W"]
ignore = ["E501"]

[tool.mypy]
python_version = "3.11"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = "test_*.py"
python_classes = "Test*"
python_functions = "test_*"
addopts = "-v --cov=src --cov-report=term-missing"

[tool.coverage.run]
source = ["src"]
omit = ["*/tests/*", "*/__init__.py"]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "raise AssertionError",
    "raise NotImplementedError",
    "if __name__ == .__main__.:",
    "if TYPE_CHECKING:",
    "@abstractmethod",
]
```

## Build Script

Create a build script for reproducible builds:

```bash
#!/bin/bash
# build.sh

set -e  # Exit on error

echo "🔨 Starting build process..."

# Clean previous builds
echo "🧹 Cleaning previous builds..."
rm -rf dist/ build/

# Install dependencies
echo "📦 Installing dependencies..."
uv sync --dev

# Run tests
echo "🧪 Running tests..."
uv run pytest --cov=src --cov-report=term-missing

# Type check
echo "🔍 Running type checker..."
uv run mypy src

# Lint
echo "✨ Running linter..."
uv run ruff check src tests

# Format check
echo "📐 Checking formatting..."
uv run ruff format --check src tests

# Build
echo "🏗️  Building package..."
uv build

# Verify build
echo "✅ Verifying build..."
if [ -d "dist" ] && [ "$(ls -A dist)" ]; then
    echo "✅ Build successful!"
    echo "📦 Build artifacts:"
    ls -lh dist/
else
    echo "❌ Build failed - no artifacts found"
    exit 1
fi

echo "🎉 Build complete!"
```

Make it executable:
```bash
chmod +x build.sh
```

## Pre-Build Checklist

Before building, verify:

- [ ] All tests pass
- [ ] Type checking passes
- [ ] Linting passes
- [ ] Formatting is correct
- [ ] Documentation is updated
- [ ] Version number is updated
- [ ] Changelog is updated
- [ ] Dependencies are up to date
- [ ] No hardcoded secrets
- [ ] Configuration is correct

## Build Verification

### Verify Package Contents

```bash
# Inspect wheel file
unzip -l dist/my_project-0.1.0-py3-none-any.whl

# Inspect source distribution
tar -tzf dist/my_project-0.1.0.tar.gz
```

### Test Installed Package

```bash
# Create virtual environment
python -m venv test_env
source test_env/bin/activate

# Install package
pip install dist/my_project-0.1.0-py3-none-any.whl

# Test import
python -c "import my_project; print(my_project.__version__)"

# Test CLI (if applicable)
my-project --version

# Deactivate and cleanup
deactivate
rm -rf test_env/
```

## CI/CD Build Configuration

### GitHub Actions Example

```yaml
# .github/workflows/build.yml
name: Build

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install uv
        run: pip install uv
      
      - name: Install dependencies
        run: uv sync --dev
      
      - name: Run tests
        run: uv run pytest --cov=src --cov-report=xml
      
      - name: Type check
        run: uv run mypy src
      
      - name: Lint
        run: uv run ruff check src tests
      
      - name: Format check
        run: uv run ruff format --check src tests
      
      - name: Build package
        run: uv build
      
      - name: Upload artifacts
        uses: actions/upload-artifact@v3
        with:
          name: dist
          path: dist/
```

### GitLab CI Example

```yaml
# .gitlab-ci.yml
build:
  image: python:3.11
  
  before_script:
    - pip install uv
  
  script:
    - uv sync --dev
    - uv run pytest --cov=src --cov-report=xml
    - uv run mypy src
    - uv run ruff check src tests
    - uv run ruff format --check src tests
    - uv build
  
  artifacts:
    paths:
      - dist/
    expire_in: 1 week
  
  only:
    - main
    - develop
    - merge_requests
```

## Build Optimization

### Reduce Package Size

```toml
[tool.hatch.build.targets.wheel]
packages = ["src/my_project"]

[tool.hatch.build.targets.wheel.shared-data]
"data" = "my_project/data"

[tool.hatch.build.targets.sdist]
include = [
    "/src",
    "/README.md",
    "/LICENSE",
]
exclude = [
    "/tests",
    "/.git",
    "/.github",
    "/docs",
]
```

### Conditional Dependencies

```toml
[project.optional-dependencies]
postgres = ["psycopg2-binary>=2.9.0"]
mysql = ["pymysql>=1.1.0"]
all = [
    "my-project[postgres]",
    "my-project[mysql]",
]
```

## Troubleshooting

### Build Fails

**Problem**: Build fails with import errors

**Solution**:
```bash
# Check dependencies
uv tree

# Reinstall dependencies
uv sync --reinstall

# Check for circular imports
uv run python -c "import my_project"
```

### Package Too Large

**Problem**: Wheel file is too large

**Solution**:
- Exclude unnecessary files
- Use data dependencies instead of bundling
- Use platform-specific wheels

### Version Conflicts

**Problem**: Dependency version conflicts

**Solution**:
```bash
# Check dependency tree
uv tree

# Resolve conflicts
uv lock --upgrade-package <package>

# Use dependency overrides
[tool.uv]
override-dependencies = [
    "package==version",
]
```

## Build Commands Reference

```bash
# Build package
uv build

# Build with specific backend
uv build --backend hatchling

# Build in release mode
uv build --release

# Clean build artifacts
rm -rf dist/ build/

# Install from built package
pip install dist/my_project-0.1.0-py3-none-any.whl

# Publish to PyPI (using twine)
pip install twine
twine upload dist/*

# Check package metadata
pip show my-project

# Verify package integrity
pip install --require-hashes -r requirements.txt
```