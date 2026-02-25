---
id: team-pipeline-auto-review
name: Team Pipeline - Auto Review
type: pipeline
description: Automated code review pipeline for PRs and commits
---

# Team Pipeline - Auto Review

## Description
Automated code review pipeline that performs comprehensive analysis on projects, PRs, or commits. Runs quality checks, security scans, tests, and generates detailed review reports.

## Configuration
Defined in `config.json`

## Input Parameters

- `project_path` - Path to the project directory (required)
- `project_name` - Name of the project (required)
- `pipeline_type` - Type of pipeline: auto-review (required)
- `branch` - Branch to compare against (default: main)
- `strict` - Enable strict mode (fail on warnings)

## State Contracts

### Read
- `{project_path}/.state/quality-report.md` - Previous quality reports (if exists)
- `{project_path}/.state/test-results.md` - Previous test results (if exists)
- `{project_path}/.state/security-report.md` - Previous security reports (if exists)

### Write
- `{project_path}/.state/pipeline-status.md` - Pipeline execution status
- `{project_path}/.state/quality-report.md` - Consolidated review report

## Execution
Orchestrates review stages in parallel where possible, consolidates findings, and generates comprehensive review report with pass/fail decision based on quality gates.

## Pipeline Stages

1. **Code Analysis** (Software Engineer)
   - Static analysis (complexity, duplication, code smells)
   - Code quality metrics
   - Maintainability index

2. **Security Scan** (Security Engineer)
   - SAST (Static Application Security Testing)
   - Dependency scanning
   - Secrets detection
   - Vulnerability assessment

3. **Test Suite** (Testing Engineer)
   - Run all unit tests
   - Run integration tests
   - Measure code coverage
   - Generate test report

4. **TDD Compliance** (Software Engineer)
   - Verify test-first adherence
   - Check test coverage per module
   - Validate TDD cycle completion

5. **Code Quality** (Software Engineer)
   - Linting checks
   - Code formatting
   - Style guide compliance
   - Best practices validation

6. **Architecture Review** (Tech Lead)
   - SOLID principles check
   - Design pattern validation
   - Architecture compliance
   - Dependency analysis

7. **Documentation Check** (Documentation Specialist)
   - API documentation completeness
   - Code comments coverage
   - README updates
   - Changelog entries

## Parallel Execution

Stages can run in parallel:
- Code Analysis, Security Scan, Test Suite, TDD Compliance, Code Quality, Architecture Review, Documentation Check

## Quality Gates

Configurable thresholds that determine pass/fail:
- Test coverage threshold (default: 80%)
- Security vulnerability threshold (default: 0 critical)
- Code complexity threshold (default: 10)
- Duplicate code threshold (default: 3%)
- TDD compliance threshold (default: 90%)

## Usage

```bash
# Review entire project
Skill(skill: "team-pipeline-auto-review")

# Review specific directory
Skill(skill: "team-pipeline-auto-review", project_path: "./src")

# Review PR/commit
Skill(skill: "team-pipeline-auto-review", target: "pr/123")
```

## Input Parameters

- `project_path` - Path to the project directory (required)
- `project_name` - Name of the project (required)
- `pipeline_type` - Type of pipeline: auto-review (required)
- `target` - Target to review (directory, PR, commit)
- `branch` - Branch to compare against (default: main)
- `strict` - Enable strict mode (fail on warnings)

## Output

- **Review Report** (`{project_path}/.state/quality-report.md`)
  - Executive summary
  - Detailed findings per stage
  - Severity levels (critical, high, medium, low)
  - Actionable recommendations
  - Pass/fail status

- **Pipeline Status** (`{project_path}/.state/pipeline-status.md`)
  - Stage completion status
  - Overall pipeline status
  - Issues and blockers

## Error Handling

- If a stage fails, pipeline continues and marks as failed
- Critical issues block merge
- Non-critical issues generate warnings
- All findings are consolidated in final report

## Integration with Git

Pipeline can be integrated with git hooks:
- Pre-commit: Quick quality checks
- Pre-push: Full review pipeline
- PR creation: Automated review and approval

## Reporting

Reports include:
- Executive summary for stakeholders
- Technical details for developers
- Security findings for security team
- Test results for QA team
- Architecture assessment for tech lead

## Exit Codes

- `0` - All checks passed
- `1` - Critical issues found
- `2` - Quality gate failed
- `3` - Security issues found
- `4` - Test failures
- `5` - TDD compliance failed