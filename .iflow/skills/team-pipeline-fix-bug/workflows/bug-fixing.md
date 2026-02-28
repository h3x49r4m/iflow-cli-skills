# Bug Fixing Workflow

## Objective
Rapidly identify, reproduce, fix, and validate bugs in production or development environments.

## Overview
This workflow provides a streamlined process for bug fixing, from initial bug report through validation and deployment. It prioritizes speed while maintaining quality standards.

## Execution Flow

**Input Parameters:**
- `project_path` - Path to the project directory (required)
- `bug_id` - Bug identifier from issue tracker (required)
- `severity` - Bug severity (critical, high, medium, low) (optional)
- `environment` - Target environment (production, staging, development) (required)
- `quick_fix` - Enable quick fix mode for critical bugs (optional, default: false)

## Bug Fixing Stages

### Stage 1: Bug Triage
1. **Receive Bug Report**
   - Read bug details from issue tracker
   - Understand bug description and impact
   - Review reproduction steps
   - Check severity and priority

2. **Initial Assessment**
   - Verify bug exists
   - Assess impact and scope
   - Estimate fix complexity
   - Assign to appropriate team member

3. **Set Priority**
   - Critical: Production down, data loss, security breach
   - High: Major feature broken, significant impact
   - Medium: Minor feature broken, limited impact
   - Low: Cosmetic issue, edge case

### Stage 2: Bug Reproduction
1. **Create Reproduction Environment**
   - Set up environment matching bug report
   - Configure test data and state
   - Ensure proper tools and dependencies

2. **Reproduce Bug**
   - Follow reproduction steps
   - Verify bug behavior
   - Capture logs and error messages
   - Document reproduction conditions

3. **Isolate Root Cause**
   - Debug application
   - Analyze logs and stack traces
   - Identify affected components
   - Determine root cause

### Stage 3: Bug Analysis
1. **Root Cause Analysis**
   - Identify why bug occurred
   - Analyze code path and logic
   - Review recent changes
   - Check for similar issues

2. **Impact Assessment**
   - Identify affected features
   - Check for related bugs
   - Assess data impact
   - Determine user impact

3. **Fix Strategy**
   - Design minimal fix
   - Consider side effects
   - Plan regression testing
   - Document fix approach

### Stage 4: Bug Fixing
1. **Implement Fix**
   - Write minimal code change
   - Follow coding standards
   - Add comments explaining fix
   - Ensure no breaking changes

2. **Write Tests**
   - Add regression test for bug
   - Test edge cases
   - Ensure test passes with fix
   - Update existing tests if needed

3. **Local Validation**
   - Run tests locally
   - Verify fix resolves bug
   - Check for regressions
   - Test related functionality

### Stage 5: Code Review
1. **Self-Review**
   - Review code changes
   - Check for quality issues
   - Verify test coverage
   - Ensure documentation updated

2. **Peer Review**
   - Submit for review
   - Get feedback
   - Address review comments
   - Update fix as needed

### Stage 6: Regression Testing
1. **Test Suite**
   - Run full test suite
   - Verify all tests pass
   - Check coverage maintained
   - Identify any failures

2. **Manual Testing**
   - Test fixed functionality
   - Test related features
   - Perform smoke tests
   - Verify no regressions

3. **Integration Testing**
   - Test in staging environment
   - Test with real data
   - Test with other systems
   - Verify deployment process

### Stage 7: Deployment
1. **Prepare Deployment**
   - Create release notes
   - Update changelog
   - Plan deployment strategy
   - Prepare rollback plan

2. **Deploy Fix**
   - Deploy to staging
   - Verify staging deployment
   - Deploy to production (if approved)
   - Monitor deployment

3. **Monitor Post-Deployment**
   - Monitor application health
   - Check error rates
   - Review user feedback
   - Verify bug resolved

### Stage 8: Validation & Closure
1. **Validate Fix**
   - Confirm bug is resolved
   - Get stakeholder sign-off
   - Document resolution
   - Update issue tracker

2. **Post-Mortem (for critical bugs)**
   - Conduct post-mortem meeting
   - Document lessons learned
   - Update processes
   - Prevent recurrence

## Quick Fix Mode

For critical bugs requiring immediate attention:

1. **Skip non-essential steps**
   - Minimal testing (smoke tests only)
   - Fast-tracked review
   - Deploy to production directly

2. **Follow-up actions**
   - Complete full testing later
   - Add comprehensive tests
   - Conduct post-mortem
   - Document improvements

## Configuration

### Bug Fixing Configuration File
Create `.iflow/bug-fix-config.json`:

```json
{
  "quickFixMode": {
    "enabled": true,
    "criticalBugsOnly": true,
    "skipFullTesting": true,
    "skipDetailedReview": true,
    "requireFollowUp": true
  },
  "testing": {
    "minTestsRequired": 1,
    "coverageCheck": true,
    "runFullSuite": true,
    "runRegressionTests": true
  },
  "review": {
    "required": true,
    "autoApproveTrivial": false,
    "minReviewers": 1
  },
  "deployment": {
    "requireStaging": true,
    "allowProductionDirect": false,
    "requireApproval": true,
    "autoRollback": true
  },
  "notification": {
    "slackChannel": "#bugs",
    "notifyOnStart": true,
    "notifyOnComplete": true,
    "notifyOnFailure": true
  }
}
```

## Usage

### Fix Bug with Default Settings
```bash
Skill(skill: "team-pipeline-fix-bug", project_path: "./myapp", bug_id: "BUG-123", severity: "high", environment: "production")
```

### Quick Fix for Critical Bug
```bash
Skill(skill: "team-pipeline-fix-bug", project_path: "./myapp", bug_id: "BUG-456", severity: "critical", environment: "production", quick_fix: true)
```

## Output

### Bug Fix Report
- Bug ID and description
- Root cause analysis
- Fix implementation details
- Test results
- Deployment status
- Validation results
- Lessons learned (if post-mortem)

### Git Commit
Follows conventional commit format:
```
fix[bug-BUG-123]: resolve authentication timeout

Fix authentication timeout issue in production.

Root Cause: Database connection pool exhaustion.
Solution: Increase pool size and add connection retry logic.

Tests: Added regression test for timeout scenario.
Coverage: Maintained at 85%.

---
Branch: fix/BUG-123-auth-timeout

Files changed:
- src/auth/session.py
- tests/test_auth.py

Verification:
- Tests: passed
- Coverage: 85%
- TDD: compliant
```

## Error Handling

### Bug Cannot Be Reproduced
- Document inability to reproduce
- Request more information
- Mark as need-more-info
- Reassign if needed

### Fix Introduces Regression
- Roll back fix
- Update fix to address regression
- Re-run testing
- Re-deploy after validation

### Deployment Fails
- Roll back to previous version
- Investigate deployment issue
- Fix deployment problem
- Retry deployment

## Integration

### With git-flow
- Creates feature branch: `fix/BUG-{id}-{description}`
- Follows git-flow commit process
- Integrates with review gates
- Supports unapproval if fix has issues

### With Issue Trackers
- Updates bug status automatically
- Posts progress comments
- Links commits to bug
- Closes bug on successful validation

### With Monitoring
- Alerts on critical bugs
- Provides bug context
- Monitors fix effectiveness
- Tracks bug recurrence

## Exit Codes

- `0` - Bug fixed and validated
- `1` - Bug cannot be reproduced
- `2` - Fix failed testing
- `3` - Deployment failed
- `4` - Validation failed
- `5` - Configuration error

## Best Practices

1. **Prioritize Quality**
   - Never skip regression testing
   - Always add tests for bugs
   - Document the fix thoroughly

2. **Communicate Effectively**
   - Keep stakeholders informed
   - Provide regular updates
   - Document decisions clearly

3. **Learn and Improve**
   - Conduct post-mortems for critical bugs
   - Update processes based on learnings
   - Share lessons with team

4. **Prevent Recurrence**
   - Add automated tests
   - Update documentation
   - Improve code reviews
   - Enhance monitoring