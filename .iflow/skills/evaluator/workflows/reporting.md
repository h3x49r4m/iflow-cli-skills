# Report Generation Workflow

## Overview

The reporting phase generates a comprehensive evaluation report that summarizes test results, discovered issues, quality metrics, and provides prioritized recommendations for improvements.

## Process

### 1. Compile Test Results

**Data Sources:**

| Source | Data | Location |
|--------|------|----------|
| Feature Checklist | Feature statuses, results | `.state/evaluation.md` |
| Issues List | Issue descriptions, severity, locations | `.state/evaluation.md` |
| Progress Stats | Tested, passed, failed, partial, skipped counts | `.state/evaluation.md` |
| Project Metadata | Project type, stack, root path | `.state/evaluation.md` |

**Compilation Steps:**

1. Read state file: `.state/evaluation.md`
2. Parse feature checklist
3. Extract issues list
4. Calculate progress statistics
5. Generate quality metrics

### 2. Calculate Quality Metrics

**Metric Formulas:**

```
Feature Completeness = (Total Features Tested / Total Features Found) × 100

Test Coverage = (Features with Existing Tests / Total Features) × 100

Reliability = (Fully Passing Features / Tested Features) × 100

UX Assessment = (Subjective score based on partial/fail results)
  - Deduct points for usability issues
  - Deduct points for mobile responsiveness issues
  - Deduct points for poor error messages
  - Base score: 100%
```

**Quality Score Calculation:**

```
Overall Quality Score = (
  (Feature Completeness × 0.3) +
  (Reliability × 0.4) +
  (UX Assessment × 0.2) +
  (Test Coverage × 0.1)
)

Interpretation:
  90-100%: Excellent
  80-89%: Good
  70-79%: Needs Improvement
  60-69%: Fair
  <60%: Poor
```

### 3. Determine Overall Status

**Status Determination:**

| Conditions | Status | Emoji |
|------------|--------|-------|
| No critical issues AND reliability ≥ 80% | Excellent | ✅ |
| Critical issues = 0 AND reliability ≥ 70% | Good | ✅ |
| Critical issues = 0 AND reliability ≥ 60% | Needs Improvement | ⚠️ |
| Critical issues > 0 OR reliability < 60% | Poor | ❌ |

**Status Examples:**

```
Critical: 0, High: 0, Reliability: 85% → ✅ Excellent
Critical: 0, High: 2, Reliability: 75% → ⚠️ Needs Improvement
Critical: 1, High: 0, Reliability: 90% → ❌ Poor (due to critical issue)
Critical: 0, High: 0, Reliability: 55% → ❌ Poor (due to low reliability)
```

### 4. Organize Feature Results

**Group by Status:**

```markdown
FEATURE TEST RESULTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ PASSED (<count>/<total>)
  • Feature 1: <name>
  • Feature 2: <name>
  • Feature 3: <name>
  ...

❌ FAILED (<count>/<total>)
  • Feature X: <name> - <reason>
  • Feature Y: <name> - <reason>
  ...

⚠️ PARTIAL (<count>/<total>)
  • Feature A: <name> - <reason>
  • Feature B: <name> - <reason>
  ...

⬜ SKIPPED (<count>/<total>)
  • Feature M: <name> - <reason>
  • Feature N: <name> - <reason>
  ...
```

### 5. Categorize Issues by Severity

**Severity Groups:**

```markdown
ISSUES DISCOVERED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔴 CRITICAL (<count>)
  1. <Issue description> - <location>
  2. <Issue description> - <location>
  ...

🟠 HIGH PRIORITY (<count>)
  1. <Issue description> - <location>
  2. <Issue description> - <location>
  ...

🟡 MEDIUM PRIORITY (<count>)
  1. <Issue description> - <location>
  2. <Issue description> - <location>
  ...

🟢 LOW PRIORITY (<count>)
  1. <Issue description> - <location>
  2. <Issue description> - <location>
  ...
```

### 6. Generate Recommendations

**Recommendation Prioritization:**

**Immediate (This Sprint):**
- All critical issues
- High-priority issues blocking users
- Security vulnerabilities

**Short-Term (Next Sprint):**
- High-priority usability issues
- Medium-priority issues affecting core features
- Performance improvements

**Long-Term (Future):**
- Medium-priority enhancements
- Low-priority cosmetic issues
- Documentation improvements
- Test coverage improvements

**Recommendation Format:**

```markdown
RECOMMENDATIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 IMMEDIATE (This Sprint)
  1. <Priority issue> - <severity>
  2. <Priority issue> - <severity>

📅 SHORT-TERM (Next Sprint)
  1. <Issue> - <severity>
  2. <Issue> - <severity>

🔮 LONG-TERM (Future)
  1. <Improvement>
  2. <Improvement>
```

### 7. Generate Full Report

**Complete Report Structure:**

```markdown
📊 PROJECT EVALUATION REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Project: <project-name>
Evaluated: <date>
Features Tested: <X>/<N> (<Y>%)

EXECUTIVE SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Overall Status: <emoji> <STATUS>
Critical Issues: <N>
High Priority Issues: <N>
Medium Priority Issues: <N>
Low Priority Issues: <N>

Quality Score: <score>%
Feature Completeness: <X>%
Reliability: <Y>%
UX Assessment: <Z>%
Test Coverage: <W>%

KEY FINDINGS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• <Finding 1>
• <Finding 2>
• <Finding 3>

PROJECT DETAILS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Type: <project-type>
Stack: <technologies>
Root: <project-root-path>

FEATURE TEST RESULTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ PASSED (<count>/<total>)
  • Feature 1: <name>
  • Feature 2: <name>
  ...

❌ FAILED (<count>/<total>)
  • Feature X: <name> - <reason>
  • Feature Y: <name> - <reason>
  ...

⚠️ PARTIAL (<count>/<total>)
  • Feature A: <name> - <reason>
  • Feature B: <name> - <reason>
  ...

⬜ SKIPPED (<count>/<total>)
  • Feature M: <name> - <reason>
  • Feature N: <name> - <reason>
  ...

ISSUES DISCOVERED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔴 CRITICAL (<count>)
  1. <Issue description> - <location>
  2. <Issue description> - <location>
  ...

🟠 HIGH PRIORITY (<count>)
  1. <Issue description> - <location>
  2. <Issue description> - <location>
  ...

🟡 MEDIUM PRIORITY (<count>)
  1. <Issue description> - <location>
  2. <Issue description> - <location>
  ...

🟢 LOW PRIORITY (<count>)
  1. <Issue description> - <location>
  2. <Issue description> - <location>
  ...

QUALITY METRICS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Feature Completeness: <X>% (<tested>/<total> features tested)
Test Coverage: <Y>% (existing tests cover <n>/<total> features)
Reliability: <Z>% (<passed>/<tested> features fully working)
UX Assessment: <W>% (based on partial/fail results)

Overall Quality Score: <score>%
Interpretation: <Excellent|Good|Needs Improvement|Fair|Poor>

TESTING STATISTICS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total Features: <N>
Tested: <X> (<Y>%)
Passed: <A> (<P>% of tested)
Failed: <B> (<Q>% of tested)
Partial: <C> (<R>% of tested)
Skipped: <D> (<S>% of total)

Issues Found: <total>
  Critical: <count>
  High Priority: <count>
  Medium Priority: <count>
  Low Priority: <count>

RECOMMENDATIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎯 IMMEDIATE (This Sprint)
  1. <Priority issue> - <severity>
  2. <Priority issue> - <severity>

📅 SHORT-TERM (Next Sprint)
  1. <Issue> - <severity>
  2. <Issue> - <severity>

🔮 LONG-TERM (Future)
  1. <Improvement>
  2. <Improvement>

NEXT STEPS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Address critical issues immediately
2. Fix high-priority issues in next sprint
3. Improve test coverage for failed features
4. Consider using dev-team skill to fix issues
5. Re-run evaluation after fixes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Report Generated: <timestamp>
Evaluator Skill v1.0.0
```

### 8. Save Report File

**Report File Location:**
```
PROJECT_ROOT/.state/evaluation-report.md
```

**Save Operation:**
- Use write_file tool (only allowed in .state/ directory)
- Include timestamp in report
- Overwrite existing report if present

### 9. Update State File

Update `.state/evaluation.md` with report generation timestamp:

```markdown
# Evaluation State

Project: <project-name>
Started: <timestamp>
Last Updated: <timestamp>
Report Generated: <timestamp>

## Metadata
Type: <project-type>
Stack: <technologies>

## Feature Checklist
[... existing checklist ...]

## Issues
[... existing issues ...]

## Progress
Total Features: <N>
Tested: <X> (<Y>%)
Passed: <A>
Failed: <B>
Partial: <C>
Skipped: <D>

## Report
Last Generated: <timestamp>
File: .state/evaluation-report.md
```

### 10. Display Report Summary

**Summary Display:**

```
📊 EVALUATION REPORT GENERATED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Overall Status: <STATUS>
📈 Quality Score: <score>%

📋 Test Results:
  • Passed: <count> (<percentage>%)
  • Failed: <count> (<percentage>%)
  • Partial: <count> (<percentage>%)
  • Skipped: <count> (<percentage>%)

🐛 Issues Found:
  • Critical: <count>
  • High Priority: <count>
  • Medium Priority: <count>
  • Low Priority: <count>

📁 Full Report: .state/evaluation-report.md
📁 State File: .state/evaluation.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 Tip: Say "evaluator list issues" to see all issues
💡 Tip: Say "evaluator show checklist" to view full status
💡 Tip: Consider using dev-team skill to fix discovered issues
```

## Report Customization

### Minimal Report

For quick summary:

```markdown
📊 QUICK SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Status: <STATUS>
Passed: <count>/<total>
Issues: <count> critical, <count> high
```

### Detailed Report

For comprehensive analysis (default format shown above).

### Export Formats

**Markdown (Default):**
- Human-readable
- Git-friendly
- Easy to edit

**JSON (Future Enhancement):**
```json
{
  "project": "<name>",
  "date": "<timestamp>",
  "status": "<STATUS>",
  "features": {
    "total": <N>,
    "tested": <X>,
    "passed": <A>,
    "failed": <B>,
    "partial": <C>,
    "skipped": <D>
  },
  "issues": {
    "critical": <count>,
    "high": <count>,
    "medium": <count>,
    "low": <count>
  },
  "metrics": {
    "completeness": <X>,
    "reliability": <Y>,
    "ux_assessment": <Z>,
    "test_coverage": <W>,
    "overall_score": <score>
  },
  "recommendations": [...]
}
```

## Integration with Other Skills

### dev-team

After evaluation, use dev-team to fix issues:

```
User: dev-team build "Fix critical and high-priority issues from evaluation report"

Dev-Team will:
1. Read evaluation report
2. Prioritize critical issues
3. Create tasks for each issue
4. Implement fixes following TDD
5. Verify fixes with tests
```

### git-manage

Commit evaluation report:

```
User: /git-manage commit docs: add evaluation report

This commits the evaluation report to git for tracking
```

### tdd-enforce

Check if failed features have corresponding tests:

```
User: /tdd-enforce

This verifies TDD compliance and identifies missing tests
```

## Exit Conditions

**Success:**
- Report generated
- Report file saved
- State file updated
- Summary displayed

**Warning:**
- Low test coverage (< 50%)
- Many features skipped (> 30%)
- High issue count

**Failure:**
- State file not found
- Report file save failed
- Data parsing errors

## Best Practices

1. **Generate reports regularly**: Don't wait until all features tested
2. **Track trends**: Compare reports over time
3. **Share with team**: Include in standup/sprint review
4. **Prioritize fixes**: Focus on critical and high-priority issues
5. **Re-evaluate**: After fixes, run evaluation again

## Next Steps

After report generation:

1. Review recommendations
2. Prioritize issues
3. Use dev-team skill to fix issues
4. Re-run evaluation after fixes
5. Track improvement trends