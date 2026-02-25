# Code Review Workflow

## Objective
Execute automated code review pipeline with parallel quality checks and generate comprehensive report.

## Steps

1. **Initialize Review**
   - Read pipeline configuration from `config.json`
   - Identify target (project directory, PR, commit)
   - Determine comparison baseline (branch, commit hash)
   - Initialize review report structure

2. **Execute Stages in Parallel**
   
   All stages execute concurrently for maximum efficiency:

   - **Code Analysis** (software-engineer)
     - Run static analysis tools
     - Calculate code complexity metrics
     - Detect code smells and anti-patterns
     - Identify duplicate code blocks
     - Generate complexity report

   - **Security Scan** (security-engineer)
     - Run SAST tools
     - Scan dependencies for vulnerabilities
     - Detect secrets and sensitive data
     - Check for common security issues
     - Generate security report

   - **Test Suite** (testing-engineer)
     - Run unit tests
     - Run integration tests
     - Measure code coverage
     - Track test execution time
     - Generate test report

   - **TDD Compliance** (software-engineer)
     - Verify test files exist for implementation
     - Check test coverage per module
     - Validate test-first approach
     - Identify untested code paths
     - Generate TDD compliance report

   - **Code Quality** (software-engineer)
     - Run linter
     - Check code formatting
     - Validate style guide compliance
     - Check for best practices violations
     - Generate quality report

   - **Architecture Review** (tech-lead)
     - Verify SOLID principles
     - Validate design patterns
     - Check architecture compliance
     - Analyze dependencies
     - Generate architecture report

   - **Documentation Check** (documentation-specialist)
     - Verify API documentation completeness
     - Check code comments coverage
     - Validate README updates
     - Check changelog entries
     - Generate documentation report

3. **Consolidate Findings**
   - Collect all stage reports
   - Normalize severity levels
   - Deduplicate findings
   - Prioritize by severity and impact
   - Group findings by category

4. **Evaluate Quality Gates**
   - Compare metrics against thresholds
   - Determine pass/fail status
   - Identify critical blockers
   - Flag warnings
   - Generate gate decision

5. **Generate Review Report**
   - Create executive summary
   - Include detailed findings per stage
   - Add severity classifications
   - Provide actionable recommendations
   - Include pass/fail decision

6. **Update State**
   - Update `quality-report.md` with full review report
   - Update `pipeline-status.md` with execution status
   - Record any issues or blockers
   - Document next steps

7. **Commit Changes**
   - Use `/git-manage commit` to commit review artifacts
   - Commit with review summary in message
   - Include report status in commit metadata

## Output

- **Quality Report** (`quality-report.md`)
  - Executive summary
  - Detailed findings by stage
  - Severity levels (critical, high, medium, low)
  - Actionable recommendations
  - Pass/fail decision

- **Pipeline Status** (`pipeline-status.md`)
  - Stage completion status
  - Overall pipeline status
  - Issues and blockers
  - Quality gate results

## Quality Gates

Review passes only if all required quality gates are met:

- Test coverage ≥ 80%
- Zero critical security vulnerabilities
- Code complexity ≤ 10
- TDD compliance ≥ 90%
- Zero test failures

## Example Execution

```bash
# Review entire project
Skill(skill: "team-pipeline-auto-review")

# Review specific directory
Skill(skill: "team-pipeline-auto-review", project_path: "./src")

# Review PR
Skill(skill: "team-pipeline-auto-review", target: "pr/123")

# Strict mode (fail on warnings)
Skill(skill: "team-pipeline-auto-review", strict: true)
```