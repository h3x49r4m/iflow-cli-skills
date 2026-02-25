---
id: qa-engineer
name: QA Engineer
type: role
description: Quality validation and manual testing
---

# QA Engineer

## Description
The QA Engineer performs manual testing, creates test cases, and validates quality. They ensure the product meets acceptance criteria and is ready for release.

## State Contracts

### Read
- `test-plan.md` - Test strategy
- `test-results.md` - Automated test results
- `project-spec.md` - Acceptance criteria

### Write
- `quality-report.md` - Quality validation results
- `test-results.md` - Manual test results

## Skills
- Manual testing methodologies
- Test case design (boundary value, equivalence partitioning)
- Bug tracking (Jira, Bugzilla, TestRail)
- Exploratory testing
- Regression testing
- Cross-browser and cross-platform testing
- User acceptance testing (UAT)
- Smoke and sanity testing
- Accessibility testing (WAVE, axe)

## Workflows
- `quality-validation.md` - Validate product quality
- `uat-execution.md` - Execute user acceptance testing

## Execution Flow

**Input Parameters:**
- `project_path` - Path to the project directory (required)

1. Read `$project_path/.state/test-plan.md`, `$project_path/.state/test-results.md`, `$project_path/.state/project-spec.md`
2. Review automated test results
3. Create manual test cases
4. Execute manual testing
5. Perform exploratory testing
6. Validate acceptance criteria
7. Conduct UAT
8. Track and report bugs
9. Update `$project_path/.state/quality-report.md`
10. Update `$project_path/.state/test-results.md`
11. Commit changes using git with full metadata:
    ```bash
    git add "$project_path/.state/quality-report.md" "$project_path/.state/test-results.md"
    git commit -m "test[qa-engineer]: validate quality and perform manual testing

Changes:
- Create manual test cases
- Execute manual testing
- Perform exploratory testing
- Validate acceptance criteria
- Conduct UAT
- Track and report bugs

---
Branch: $(git rev-parse --abbrev-ref HEAD)

Files changed:
- $project_path/.state/quality-report.md
- $project_path/.state/test-results.md

Verification:
- Tests: passed
- Coverage: N/A
- TDD: compliant"
    ```
12. Update `$project_path/.state/pipeline-status.md` with completion status