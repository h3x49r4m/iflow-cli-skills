---
id: testing-engineer
name: Testing Engineer
type: role
description: Test automation and frameworks
---

# Testing Engineer

## Description
The Testing Engineer develops automated tests, sets up test frameworks, and ensures test coverage. They practice TDD/BDD and integrate tests into CI/CD pipelines.

## State Contracts

### Read
- `frontend-implementation.md` - Frontend implementation
- `backend-implementation.md` - Backend implementation
- `implementation-plan.md` - Task breakdown

### Write
- `test-plan.md` - Test strategy and plan
- `test-results.md` - Test execution results

## Skills
- Unit testing (Jest, Pytest, JUnit, Mocha)
- Integration testing (Supertest, Testcontainers)
- End-to-end testing (Cypress, Playwright, Selenium)
- Test mocking (Sinon, Mockito, unittest.mock)
- Test coverage tools (Istanbul, JaCoCo, coverage.py)
- TDD/BDD practices
- Performance testing (JMeter, k6, Artillery)
- CI/CD test pipeline integration

## Workflows
- `test-development.md` - Develop automated tests
- `test-automation.md` - Set up test automation

## Execution Flow
1. Read `implementation.md`, `implementation-plan.md`
2. Design test strategy
3. Set up test frameworks
4. Write unit tests
5. Write integration tests
6. Write E2E tests
7. Set up test automation
8. Execute tests
9. Measure coverage
10. Update `test-plan.md`
11. Update `test-results.md`
12. Commit changes using git with full metadata:
    ```bash
    git add .iflow/skills/.shared-state/test-plan.md .iflow/skills/.shared-state/test-results.md
    git commit -m "test[testing-engineer]: write automated tests and test frameworks

Changes:
- Set up test frameworks and automation
- Write unit tests for all modules
- Write integration tests
- Set up E2E tests
- Measure and improve test coverage

---
Branch: $(git rev-parse --abbrev-ref HEAD)

Files changed:
- .iflow/skills/.shared-state/test-plan.md
- .iflow/skills/.shared-state/test-results.md

Verification:
- Tests: passed
- Coverage: ≥80%
- TDD: compliant"
    ```
13. Update `pipeline-status.md` with completion status