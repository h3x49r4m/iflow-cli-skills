# Quality Metrics

**Project:** {PROJECT_NAME}  
**Last Updated:** {DATE}  
**Measurement Period:** {START_DATE} - {END_DATE}

---

## Test Coverage

### Overall Coverage

| Metric | Current | Target | Status | Threshold |
|--------|---------|--------|--------|-----------|
| Line Coverage | {PERCENTAGE}% | {PERCENTAGE}% | {PASS/FAIL} | {PERCENTAGE}% |
| Branch Coverage | {PERCENTAGE}% | {PERCENTAGE}% | {PASS/FAIL} | {PERCENTAGE}% |
| Function Coverage | {PERCENTAGE}% | {PERCENTAGE}% | {PASS/FAIL} | {PERCENTAGE}% |
| Statement Coverage | {PERCENTAGE}% | {PERCENTAGE}% | {PASS/FAIL} | {PERCENTAGE}% |

### Coverage by Module

| Module | Lines | Branches | Functions | Statements |
|--------|-------|----------|-----------|------------|
| {MODULE_NAME} | {PERCENTAGE}% | {PERCENTAGE}% | {PERCENTAGE}% | {PERCENTAGE}% |
| {MODULE_NAME} | {PERCENTAGE}% | {PERCENTAGE}% | {PERCENTAGE}% | {PERCENTAGE}% |

### Coverage Trends

| Date | Line Coverage | Branch Coverage | Trend |
|------|---------------|-----------------|-------|
| {DATE} | {PERCENTAGE}% | {PERCENTAGE}% | {↑/↓/→} |
| {DATE} | {PERCENTAGE}% | {PERCENTAGE}% | {↑/↓/→} |

---

## Code Quality

### Complexity Metrics

| Metric | Current | Target | Status | Threshold |
|--------|---------|--------|--------|-----------|
| Avg Cyclomatic Complexity | {VALUE} | {VALUE} | {PASS/FAIL} | {VALUE} |
| Max Cyclomatic Complexity | {VALUE} | {VALUE} | {PASS/FAIL} | {VALUE} |
| Avg Cognitive Complexity | {VALUE} | {VALUE} | {PASS/FAIL} | {VALUE} |
| Max Cognitive Complexity | {VALUE} | {VALUE} | {PASS/FAIL} | {VALUE} |
| Avg Function Length | {LINES} | {LINES} | {PASS/FAIL} | {LINES} |
| Max Function Length | {LINES} | {LINES} | {PASS/FAIL} | {LINES} |

### Code Duplication

| Metric | Current | Target | Status | Threshold |
|--------|---------|--------|--------|-----------|
| Duplicate Lines | {COUNT} | {COUNT} | {PASS/FAIL} | {COUNT} |
| Duplicate Percentage | {PERCENTAGE}% | {PERCENTAGE}% | {PASS/FAIL} | {PERCENTAGE}% |
| Duplicate Blocks | {COUNT} | {COUNT} | {PASS/FAIL} | {COUNT} |

### Linting Violations

| Category | Current | Target | Status |
|----------|---------|--------|--------|
| Errors | {COUNT} | {COUNT} | {PASS/FAIL} |
| Warnings | {COUNT} | {COUNT} | {PASS/FAIL} |
| Notices | {COUNT} | {COUNT} | {PASS/FAIL} |

---

## Security Metrics

### Vulnerability Scan Results

| Severity | Count | Target | Status |
|----------|-------|--------|--------|
| Critical | {COUNT} | {COUNT} | {PASS/FAIL} |
| High | {COUNT} | {COUNT} | {PASS/FAIL} |
| Medium | {COUNT} | {COUNT} | {PASS/FAIL} |
| Low | {COUNT} | {COUNT} | {PASS/FAIL} |
| Info | {COUNT} | {COUNT} | {PASS/FAIL} |

### Security Compliance

| Check | Status | Last Scan |
|-------|--------|-----------|
| Dependency Check | {PASS/FAIL} | {DATE} |
| SAST Check | {PASS/FAIL} | {DATE} |
| Secrets Check | {PASS/FAIL} | {DATE} |
| License Check | {PASS/FAIL} | {DATE} |

---

## Performance Metrics

### Bundle Size

| Bundle | Size (KB) | Gzipped (KB) | Target (KB) | Status |
|--------|-----------|--------------|-------------|--------|
| Main | {SIZE} | {SIZE} | {SIZE} | {PASS/FAIL} |
| Vendor | {SIZE} | {SIZE} | {SIZE} | {PASS/FAIL} |
| CSS | {SIZE} | {SIZE} | {SIZE} | {PASS/FAIL} |

### Core Web Vitals

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| LCP | {MS}ms | {MS}ms | {PASS/FAIL} |
| FID | {MS}ms | {MS}ms | {PASS/FAIL} |
| CLS | {VALUE} | {VALUE} | {PASS/FAIL} |
| FCP | {MS}ms | {MS}ms | {PASS/FAIL} |
| TTI | {MS}ms | {MS}ms | {PASS/FAIL} |

### Lighthouse Scores

| Category | Score | Target | Status |
|----------|-------|--------|--------|
| Performance | {SCORE}/100 | {SCORE}/100 | {PASS/FAIL} |
| Accessibility | {SCORE}/100 | {SCORE}/100 | {PASS/FAIL} |
| Best Practices | {SCORE}/100 | {SCORE}/100 | {PASS/FAIL} |
| SEO | {SCORE}/100 | {SCORE}/100 | {PASS/FAIL} |

---

## Accessibility Metrics

### WCAG Compliance

| Level | Issues | Status |
|-------|--------|--------|
| A | {COUNT} | {PASS/FAIL} |
| AA | {COUNT} | {PASS/FAIL} |
| AAA | {COUNT} | {PASS/FAIL} |

### Accessibility Issues

| Severity | Count | Status |
|----------|-------|--------|
| Critical | {COUNT} | {PASS/FAIL} |
| Serious | {COUNT} | {PASS/FAIL} |
| Moderate | {COUNT} | {PASS/FAIL} |
| Minor | {COUNT} | {PASS/FAIL} |

---

## Defect Metrics

### Defect Density

| Period | Defects Found | Defects Fixed | Defects Open | Defect Density |
|--------|---------------|---------------|-------------|----------------|
| {PERIOD} | {COUNT} | {COUNT} | {COUNT} | {VALUE} |
| {PERIOD} | {COUNT} | {COUNT} | {COUNT} | {VALUE} |

### Defect Distribution by Severity

| Severity | Open | In Progress | Resolved | Total |
|----------|------|-------------|----------|-------|
| Critical | {COUNT} | {COUNT} | {COUNT} | {COUNT} |
| High | {COUNT} | {COUNT} | {COUNT} | {COUNT} |
| Medium | {COUNT} | {COUNT} | {COUNT} | {COUNT} |
| Low | {COUNT} | {COUNT} | {COUNT} | {COUNT} |

### Defect Distribution by Type

| Type | Count | Percentage |
|------|-------|------------|
| Functional | {COUNT} | {PERCENTAGE}% |
| UI/UX | {COUNT} | {PERCENTAGE}% |
| Performance | {COUNT} | {PERCENTAGE}% |
| Security | {COUNT} | {PERCENTAGE}% |
| Other | {COUNT} | {PERCENTAGE}% |

---

## Quality Gate Status

### Current Gate Status

| Gate | Status | Last Check | Notes |
|------|--------|------------|-------|
| Test Coverage | {PASS/FAIL} | {DATE} | {NOTES} |
| Code Complexity | {PASS/FAIL} | {DATE} | {NOTES} |
| Security Scan | {PASS/FAIL} | {DATE} | {NOTES} |
| Linting | {PASS/FAIL} | {DATE} | {NOTES} |
| Performance | {PASS/FAIL} | {DATE} | {NOTES} |
| Accessibility | {PASS/FAIL} | {DATE} | {NOTES} |

### Gate History

| Date | Test Coverage | Code Complexity | Security | Linting | Performance | Accessibility |
|------|---------------|-----------------|----------|---------|-------------|----------------|
| {DATE} | {PASS/FAIL} | {PASS/FAIL} | {PASS/FAIL} | {PASS/FAIL} | {PASS/FAIL} | {PASS/FAIL} |
| {DATE} | {PASS/FAIL} | {PASS/FAIL} | {PASS/FAIL} | {PASS/FAIL} | {PASS/FAIL} | {PASS/FAIL} |

---

## Trend Analysis

### Quality Trend Summary

| Metric | Trend | Notes |
|--------|-------|-------|
| Coverage | {↑/↓/→} | {NOTES} |
| Complexity | {↑/↓/→} | {NOTES} |
| Security | {↑/↓/→} | {NOTES} |
| Performance | {↑/↓/→} | {NOTES} |
| Defects | {↑/↓/→} | {NOTES} |

---

## Changelog

| Date | Changes | Author |
|------|---------|--------|
| {DATE} | Initial quality metrics | {AUTHOR} |
| {DATE} | Updated coverage metrics | {AUTHOR} |