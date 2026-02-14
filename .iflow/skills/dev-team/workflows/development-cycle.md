# Development Cycle Workflow

The iterative workflow for developing features during sprints.

## Overview

This workflow describes the day-to-day development process, from picking up tasks to delivering completed features. It emphasizes continuous integration, testing, and quality assurance.

## Participants

- **All Developers**: Implement features
- **Tech Lead**: Code reviews and guidance
- **QA Engineer**: Testing and validation
- **Project Manager**: Coordination and tracking

## Workflow Steps

### Step 1: Task Pickup
**Owner**: Developer

**Actions**:
1. Select task from sprint backlog
2. Review task requirements and acceptance criteria
3. Identify dependencies and blockers
4. Create feature branch from main
5. Update task status to "In Progress"

**Deliverables**:
- Feature branch created
- Task assigned to developer

---

### Step 2: Implementation (TDD)
**Owner**: Developer

**Actions**:
1. Write failing tests for the feature
2. Implement minimal code to pass tests
3. Refactor for code quality
4. Add documentation as needed
5. Run tests locally
6. Commit changes with descriptive messages

**Deliverables**:
- Working code with tests
- Documentation updates
- Commits to feature branch

**TDD Cycle**:
```
Red → Write failing test
Green → Write minimal code to pass
Refactor → Improve code quality
Repeat → Until feature complete
```

---

### Step 3: Self-Review
**Owner**: Developer

**Actions**:
1. Review own code changes
2. Ensure code follows project conventions
3. Verify all tests pass
4. Check for security issues
5. Validate performance impact
6. Update documentation

**Checklist**:
- [ ] Code follows style guide
- [ ] Tests added and passing
- [ ] No console errors or warnings
- [ ] Documentation updated
- [ ] No hardcoded values
- [ ] Error handling implemented

---

### Step 4: Pull Request
**Owner**: Developer

**Actions**:
1. Create pull request with clear description
2. Link to relevant task/issue
3. Add screenshots for UI changes
4. Request review from Tech Lead and peer
5. Ensure CI checks run

**PR Template**:
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Unit tests added
- [ ] Integration tests added
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guide
- [ ] Tests passing
- [ ] Documentation updated
- [ ] No merge conflicts
```

---

### Step 5: Code Review
**Owner**: Tech Lead + Peer Developer

**Actions**:
1. Review code for correctness and quality
2. Check for security vulnerabilities
3. Verify test coverage
4. Suggest improvements
5. Approve or request changes
6. Ensure CI checks pass

**Review Criteria**:
- Code correctness and logic
- Adherence to coding standards
- Test coverage and quality
- Documentation completeness
- Performance implications
- Security considerations
- Maintainability and readability

**Approval Rules**:
- At least 2 approvals required
- Tech Lead approval mandatory
- All CI checks must pass
- No unresolved review comments

---

### Step 6: Testing
**Owner**: QA Engineer

**Actions**:
1. Verify acceptance criteria met
2. Perform manual testing
3. Run automated test suite
4. Test edge cases
5. Validate integration points
6. Report any bugs found

**Testing Checklist**:
- [ ] Acceptance criteria validated
- [ ] Happy path tested
- [ ] Error scenarios tested
- [ ] Edge cases covered
- [ ] Integration points verified
- [ ] Performance acceptable
- [ ] Accessibility checked (if UI)

---

### Step 7: Integration
**Owner**: Developer + QA Engineer

**Actions**:
1. Merge PR to main branch
2. Verify deployment to staging
3. Run smoke tests on staging
4. Monitor for errors
5. Validate feature end-to-end
6. Update task status

**Merge Requirements**:
- All reviews approved
- All tests passing
- No merge conflicts
- Documentation updated

---

### Step 8: Deployment Preparation
**Owner**: DevOps Engineer

**Actions**:
1. Build production artifacts
2. Run security scans
3. Create deployment plan
4. Prepare rollback plan
5. Schedule deployment window
6. Notify stakeholders

**Pre-Deployment Checklist**:
- [ ] All tests passing
- [ ] Security scan clean
- [ ] Performance benchmarks met
- [ ] Documentation complete
- [ ] Rollback plan ready
- [ ] Stakeholders notified

---

## Daily Routine

### Standup (Daily)
**Time**: 15 minutes
**Participants**: All team members

**Format**:
1. What I completed yesterday
2. What I'm working on today
3. Any blockers or dependencies

**Output**:
- Progress update
- Blocker identification
- Task adjustment if needed

### Continuous Integration
**Triggers**:
- Every commit to feature branch
- Every pull request
- Merge to main branch

**CI Checks**:
- Install dependencies
- Run linter
- Run unit tests
- Run integration tests
- Generate coverage report
- Security scan
- Build artifacts

### Code Review Turnaround
**Target**: <4 hours
**Process**:
- Automated review (CI)
- Peer review (first reviewer)
- Tech Lead review (final approval)

## Quality Gates

### Gate 1: Code Complete
- [ ] All acceptance criteria met
- [ ] Tests written and passing
- [ ] Code follows conventions
- [ ] Documentation updated
- [ ] No known issues

### Gate 2: Review Approved
- [ ] Code reviewed by peers
- [ ] Tech Lead approval obtained
- [ ] All review comments addressed
- [ ] CI checks passing

### Gate 3: Testing Complete
- [ ] Manual testing done
- [ ] Automated tests passing
- [ ] No critical bugs found
- [ ] Performance acceptable

### Gate 4: Ready for Merge
- [ ] All approvals received
- [ ] No merge conflicts
- [ ] Documentation complete
- [ ] Deployment plan ready

## Metrics Tracking

### Development Metrics
- **Cycle Time**: Time from task start to merge
- **Lead Time**: Time from task creation to deployment
- **Velocity**: Story points completed per sprint
- **Throughput**: Number of tasks completed per sprint

### Quality Metrics
- **Test Coverage**: Percentage of code covered
- **Bug Escape Rate**: Bugs found in production
- **Review Time**: Average time for code review
- **Rework Rate**: Percentage of tasks requiring rework

### Process Metrics
- **PR Merge Time**: Time from PR creation to merge
- **Build Success Rate**: Percentage of successful builds
- **Test Failure Rate**: Percentage of test failures
- **Deployment Frequency**: Number of deployments per week

## Blocker Handling

### Common Blockers
- Waiting for code review
- Dependency on another task
- Unclear requirements
- Technical challenges
- Environment issues

### Resolution Process
1. Identify blocker early (standup)
2. Document in blocker tracker
3. Escalate to Project Manager
4. Coordinate with team for resolution
5. Update task status when resolved

## Best Practices

### For Developers
- Follow TDD methodology
- Write small, focused commits
- Keep PRs small and focused
- Review your own code before submitting
- Respond to review comments promptly
- Document complex logic

### For Reviewers
- Provide constructive feedback
- Be specific and actionable
- Respond within SLA
- Explain the "why" behind suggestions
- Approve promptly when satisfied

### For QA
- Test early and often
- Report bugs with clear steps
- Verify fixes thoroughly
- Communicate blockers promptly
- Maintain test documentation

## Exit Criteria

A task is complete when:
1. All acceptance criteria met
2. Code reviewed and approved
3. All tests passing
4. QA validation complete
5. Merged to main branch
6. Deployed to staging successfully
7. Task status updated to "Done"

## Next Steps

After development cycle completion:
1. Update sprint progress
2. Monitor production deployment
3. Gather user feedback
4. Plan next iteration
5. Update quality metrics
6. Document lessons learned