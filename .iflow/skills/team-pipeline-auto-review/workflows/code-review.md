# Automated Code Review Workflow

## Objective
Perform comprehensive automated code review for pull requests and commits.

## Overview
This workflow orchestrates automated code review processes including linting, static analysis, security scanning, and quality validation. It ensures code quality and security before merging.

## Execution Flow

**Input Parameters:**
- `project_path` - Path to the project directory (required)
- `pr_number` - Pull request number (optional, for PR-specific review)
- `branch` - Branch to review (optional, defaults to current branch)
- `commit_hash` - Specific commit to review (optional)

## Review Stages

### Stage 1: Linting
1. Run project-specific linters (ESLint, Pylint, Rubocop, etc.)
2. Check code style and formatting
3. Identify potential code smells
4. Generate lint report

**Tools:** ESLint, Pylint, Rubocop, Flake8, ShellCheck
**Output:** Lint report with issues and severity

### Stage 2: Static Analysis
1. Run static analysis tools (SonarQube, CodeQL, DeepScan)
2. Analyze code complexity and maintainability
3. Identify potential bugs and vulnerabilities
4. Check code duplication
5. Generate analysis report

**Tools:** SonarQube, CodeQL, DeepScan, Semgrep
**Output:** Static analysis report with quality metrics

### Stage 3: Security Scanning
1. Scan for hardcoded secrets and credentials
2. Run dependency vulnerability scanners
3. Check for common security issues (OWASP Top 10)
4. Validate security best practices
5. Generate security report

**Tools:** Snyk, Dependabot, GitGuardian, OWASP Dependency-Check
**Output:** Security scan report with vulnerabilities

### Stage 4: Test Validation
1. Run all automated tests
2. Verify test coverage meets thresholds
3. Check test results and failures
4. Identify flaky tests
5. Generate test report

**Tools:** Jest, Pytest, JUnit, Coverage tools
**Output:** Test results with coverage metrics

### Stage 5: Code Quality Metrics
1. Calculate code quality scores
2. Measure technical debt
3. Track code complexity trends
4. Generate quality dashboard
5. Provide improvement recommendations

**Tools:** SonarQube, CodeClimate, Codacy
**Output:** Quality metrics and recommendations

## Review Gates

### Must Pass
- All linting errors must be resolved (warnings may be allowed based on config)
- No critical security vulnerabilities
- All tests must pass
- Code coverage must meet minimum threshold (default: 80%)

### Should Pass
- Static analysis score above threshold
- No high-severity issues
- Technical debt within acceptable limits

### May Pass with Approval
- Medium-severity issues with documented justification
- Coverage slightly below threshold with approval

## Configuration

### Review Configuration File
Create `.iflow/review-config.json`:

```json
{
  "linting": {
    "enabled": true,
    "tools": ["eslint", "pylint"],
    "failOnError": true,
    "allowWarnings": false
  },
  "staticAnalysis": {
    "enabled": true,
    "tools": ["sonarqube"],
    "qualityGate": "B",
    "failOnError": false
  },
  "security": {
    "enabled": true,
    "tools": ["snyk", "gitguardian"],
    "failOnCritical": true,
    "failOnHigh": false
  },
  "testing": {
    "enabled": true,
    "coverageThreshold": {
      "lines": 80,
      "branches": 75,
      "functions": 80,
      "statements": 80
    },
    "failOnTestFailure": true
  }
}
```

## Usage

### Review Current Branch
```bash
Skill(skill: "team-pipeline-auto-review", project_path: "./myapp")
```

### Review Pull Request
```bash
Skill(skill: "team-pipeline-auto-review", project_path: "./myapp", pr_number: 123)
```

### Review Specific Commit
```bash
Skill(skill: "team-pipeline-auto-review", project_path: "./myapp", commit_hash: "abc123")
```

## Output

### Review Report
- Overall review status (PASS/FAIL/WARNING)
- Linting results with issues
- Static analysis results with metrics
- Security scan results with vulnerabilities
- Test results with coverage
- Code quality metrics
- Recommendations for improvement

### Commit Comment
Automatic comment on commit/PR with review summary:
```
## Automated Code Review Results

**Status:** ✅ PASS

### Linting
- 0 errors, 2 warnings

### Security
- 0 vulnerabilities found

### Testing
- All tests passed
- Coverage: 85% (target: 80%)

### Quality Metrics
- Code Quality: A
- Technical Debt: 30min
- Complexity: Low

### Recommendations
- Consider reducing cyclomatic complexity in auth.py:45
```

## Error Handling

### Linting Failures
- Block commit if failOnError is true
- Allow commit with warnings if allowWarnings is true
- Provide fix suggestions where possible

### Security Failures
- Block commit on critical vulnerabilities
- Warn on high-severity vulnerabilities
- Document all vulnerabilities with remediation steps

### Test Failures
- Block commit if any test fails
- Show failing tests with error messages
- Suggest running tests locally before committing

### Coverage Failures
- Block commit if coverage below threshold
- Show coverage breakdown by file
- Suggest tests for uncovered code

## Integration

### With git-flow
- Runs automatically on `/git-flow commit`
- Results attached to commit message
- Blocks merge if review fails

### With CI/CD
- Integrates with GitHub Actions, GitLab CI, Jenkins
- Results posted as PR comments
- Status checks on commits

## Exit Codes

- `0` - Review passed
- `1` - Review failed (blocking issues)
- `2` - Review warning (non-blocking issues)
- `3` - Configuration error
- `4` - Tool execution error