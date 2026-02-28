# Skill Manager Tests

This directory contains the test suite for the skill manager system.

## Running Tests

### Run All Tests
```bash
python3 tests/run_tests.py
```

### Run Specific Test Class
```bash
python3 -m unittest tests.test_skill_manager.TestSkillVersionManager
```

### Run with Verbose Output
```bash
python3 tests/run_tests.py --verbose
```

### Run with Quiet Output
```bash
python3 tests/run_tests.py --quiet
```

## Test Coverage

The test suite covers:

- **SkillVersionManager**: Version parsing, comparison, compatibility checking
- **SkillRegistry**: Skill loading, capability retrieval, skill discovery
- **SkillDependencyResolver**: Dependency resolution, workflow validation
- **SkillCompatibilityChecker**: Pipeline compatibility, breaking changes detection

## Test Structure

- `test_skill_manager.py` - Main test file with all test cases
- `run_tests.py` - Test runner script with CLI interface

## Adding New Tests

To add new tests:

1. Add test methods to the appropriate test class in `test_skill_manager.py`
2. Follow naming convention: `test_<feature_name>`
3. Use `setUp()` and `tearDown()` for test fixtures
4. Run tests to verify they pass

## CI/CD Integration

These tests can be integrated into CI/CD pipelines:

```yaml
# Example GitHub Actions workflow
- name: Run skill manager tests
  run: |
    cd .iflow/skills
    python3 tests/run_tests.py
```

## Exit Codes

- `0` - All tests passed
- `1` - One or more tests failed