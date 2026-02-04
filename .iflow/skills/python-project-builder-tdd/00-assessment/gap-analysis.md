# Gap Analysis Guide

## Purpose
This guide explains how to document gaps between a project's current state and the TDD skill standards, and how to prioritize them for alignment.

## Gap Analysis Process

### Step 1: Identify Gaps

Use the compliance checklist to identify areas where the project deviates from standards.

**Gap Categories:**
1. **Structural Gaps** - Directory structure, file organization
2. **Tooling Gaps** - Missing or misconfigured tools
3. **Process Gaps** - TDD workflow, testing practices
4. **Quality Gaps** - Code standards, coverage, documentation
5. **Workflow Gaps** - State management, tracking

### Step 2: Assess Impact

For each gap, assess:
- **Severity**: How much does this gap affect development?
- **Frequency**: How often does this gap cause issues?
- **Dependencies**: What other gaps depend on this one?

**Impact Matrix:**

| Severity | Description | Example |
|----------|-------------|---------|
| **Critical** | Blocks development, causes failures | No test framework, broken build |
| **High** | Significantly slows development | Low coverage, no linting |
| **Medium** | Causes occasional issues | Inconsistent style, missing docs |
| **Low** | Nice to have improvements | Missing changelog, minor style issues |

### Step 3: Estimate Effort

For each gap, estimate the effort to fix:
- **Time**: Hours or days required
- **Risk**: Likelihood of introducing bugs
- **Disruption**: Impact on ongoing development

**Effort Levels:**

| Effort | Time | Risk | Disruption |
|--------|------|------|------------|
| **Trivial** | < 1 hour | Low | None |
| **Low** | 1-4 hours | Low | Minimal |
| **Medium** | 1-2 days | Medium | Moderate |
| **High** | 3-5 days | High | Significant |
| **Very High** | 1+ weeks | Very High | Major disruption |

### Step 4: Determine Priority

Use the **Impact/Effort Matrix** to prioritize gaps:

```
           High Impact
                |
      Critical  |  High
    (Do First)  |  (Do Soon)
----------------+----------------
 Medium         |  Low
 (Schedule)     |  (Do Last)
                |
           Low Impact
                Low Effort    High Effort
```

**Priority Levels:**
- **P0 - Critical**: Do immediately (high impact, low/medium effort)
- **P1 - High**: Do soon (high impact, any effort)
- **P2 - Medium**: Schedule appropriately (medium impact, low/medium effort)
- **P3 - Low**: Do when convenient (low impact, any effort)

### Step 5: Create Migration Plan

Organize gaps into logical migration phases based on dependencies and priorities.

## Gap Analysis Template

```markdown
# Gap Analysis Report

**Project Name**: _____________
**Analysis Date**: YYYY-MM-DD
**Compliance Score**: __/100

## Identified Gaps

### Category: Structure

| Gap ID | Description | Current State | Target State | Impact | Effort | Priority | Dependencies |
|--------|-------------|---------------|--------------|--------|--------|----------|--------------|
| S001 | No src/ directory | Flat layout | src/ layout | Critical | Medium | P0 | None |
| S002 | Tests not organized | Flat tests/ | unit/integration/e2e | High | Medium | P1 | S001 |
| S003 | Missing documentation files | No FEATURES.md | Full docs | Medium | Low | P2 | None |

**Total Structural Gaps**: __

---

### Category: Tooling

| Gap ID | Description | Current State | Target State | Impact | Effort | Priority | Dependencies |
|--------|-------------|---------------|--------------|--------|--------|----------|--------------|
| T001 | No pytest configured | unittest | pytest | Critical | Low | P0 | None |
| T002 | No ruff configured | None | ruff | High | Low | P1 | None |
| T003 | No mypy configured | None | mypy | Medium | Medium | P2 | T001 |
| T004 | No pre-commit hooks | None | pre-commit | Low | Low | P3 | T002, T003 |

**Total Tooling Gaps**: __

---

### Category: Process

| Gap ID | Description | Current State | Target State | Impact | Effort | Priority | Dependencies |
|--------|-------------|---------------|--------------|--------|--------|----------|--------------|
| P001 | No TDD workflow | Code-first | Test-first | High | High | P1 | T001 |
| P002 | No state management | No tracking | .state/ tracking | Medium | Medium | P2 | None |
| P003 | No change management | Ad-hoc changes | Structured workflow | Medium | High | P2 | P002 |

**Total Process Gaps**: __

---

### Category: Quality

| Gap ID | Description | Current State | Target State | Impact | Effort | Priority | Dependencies |
|--------|-------------|---------------|--------------|--------|--------|----------|--------------|
| Q001 | Low test coverage (40%) | 40% | 80% | High | High | P1 | T001, S002 |
| Q002 | No type hints | Missing | Full type hints | High | High | P1 | None |
| Q003 | No docstrings | Missing | Full docstrings | Medium | Medium | P2 | None |
| Q004 | Inconsistent naming | Mixed | snake_case | Low | Medium | P3 | T002 |

**Total Quality Gaps**: __

---

## Summary Statistics

### Gaps by Priority

| Priority | Count | Total Effort |
|----------|-------|--------------|
| P0 - Critical | __ | __ hours/days |
| P1 - High | __ | __ hours/days |
| P2 - Medium | __ | __ hours/days |
| P3 - Low | __ | __ hours/days |

### Gaps by Category

| Category | Count | Critical | High | Medium | Low |
|----------|-------|----------|------|--------|-----|
| Structure | __ | __ | __ | __ | __ |
| Tooling | __ | __ | __ | __ | __ |
| Process | __ | __ | __ | __ | __ |
| Quality | __ | __ | __ | __ | __ |

### Total Effort Estimate

- **Critical Gaps**: __ hours/days
- **High Gaps**: __ hours/days
- **Medium Gaps**: __ hours/days
- **Low Gaps**: __ hours/days
- **Total**: __ hours/days

## Migration Phases

### Phase 1: Critical Foundation (Week 1)
**Goal**: Establish basic development infrastructure

| Gap ID | Description | Effort | Owner | Status |
|--------|-------------|--------|-------|--------|
| S001 | Create src/ directory | 2 hours | - | [ ] |
| T001 | Configure pytest | 1 hour | - | [ ] |
| T002 | Configure ruff | 1 hour | - | [ ] |

**Total Effort**: 4 hours

---

### Phase 2: High Priority Alignment (Week 2)
**Goal**: Align critical development practices

| Gap ID | Description | Effort | Owner | Status |
|--------|-------------|--------|-------|--------|
| S002 | Reorganize tests | 4 hours | - | [ ] |
| Q001 | Improve coverage to 80% | 2 days | - | [ ] |
| Q002 | Add type hints | 2 days | - | [ ] |

**Total Effort**: 4.5 days

---

### Phase 3: Medium Priority (Week 3-4)
**Goal**: Complete standard alignment

| Gap ID | Description | Effort | Owner | Status |
|--------|-------------|--------|-------|--------|
| P001 | Adopt TDD workflow | 2 days | - | [ ] |
| P002 | Set up state management | 4 hours | - | [ ] |
| Q003 | Add docstrings | 1 day | - | [ ] |

**Total Effort**: 3.5 days

---

### Phase 4: Low Priority (Ongoing)
**Goal**: Nice-to-have improvements

| Gap ID | Description | Effort | Owner | Status |
|--------|-------------|--------|-------|--------|
| P003 | Set up change management | 1 day | - | [ ] |
| T004 | Configure pre-commit hooks | 2 hours | - | [ ] |
| Q004 | Standardize naming | 4 hours | - | [ ] |

**Total Effort**: 1.5 days

---

## Dependencies Graph

```
Critical Path:
S001 (Create src/) → S002 (Reorganize tests) → Q001 (Improve coverage)

Parallel Paths:
T001 (pytest) → T003 (mypy) → T004 (pre-commit)
T002 (ruff) → Q004 (naming)
P002 (state management) → P003 (change management)

Independent:
Q002 (type hints) - Can be done anytime
Q003 (docstrings) - Can be done anytime
```

## Risk Assessment

### High Risk Items

| Gap | Risk | Mitigation |
|-----|------|------------|
| S001 | Breaking imports | Use relative imports, update all references |
| S002 | Breaking test imports | Update imports, verify all tests pass |
| Q001 | Regression bugs | Run full test suite after changes |

### Medium Risk Items

| Gap | Risk | Mitigation |
|-----|------|------------|
| Q002 | Type errors | Run mypy incrementally, fix errors as found |
| P001 | Slower development | Start with new features only |

---

## Success Criteria

Alignment is successful when:

- [ ] All P0 gaps are resolved
- [ ] All P1 gaps are resolved
- [ ] Compliance score ≥ 80%
- [ ] Test coverage ≥ 80%
- [ ] All quality tools pass
- [ ] TDD workflow is followed for new features

---

## Notes

* Add any additional context, constraints, or considerations
* Note any blockers or external dependencies
* Document any trade-offs or decisions made
```

## Common Gap Patterns

### Pattern 1: Flat Layout

**Gaps:**
- No src/ directory
- Tests at root level
- Mixed source and test files

**Alignment Strategy:**
1. Create src/ directory
2. Move source code to src/
3. Update all imports
4. Reorganize tests
5. Update configuration

**Effort**: 1-2 days

---

### Pattern 2: No Testing

**Gaps:**
- No test framework
- No test files
- No coverage measurement

**Alignment Strategy:**
1. Add pytest to dependencies
2. Create tests/ directory structure
3. Write tests for critical paths
4. Configure coverage
5. Achieve 80% coverage

**Effort**: 3-5 days

---

### Pattern 3: Legacy Tools

**Gaps:**
- Using pip instead of uv
- Using unittest instead of pytest
- Using flake8 instead of ruff

**Alignment Strategy:**
1. Migrate to uv (create pyproject.toml)
2. Migrate tests to pytest
3. Replace flake8 with ruff
4. Update CI/CD if applicable

**Effort**: 2-3 days

---

### Pattern 4: No Type Hints

**Gaps:**
- No type hints in code
- No mypy configuration
- Type errors not caught

**Alignment Strategy:**
1. Configure mypy
2. Add type hints to public API
3. Add type hints to internal code
4. Fix type errors
5. Run mypy in CI

**Effort**: 2-3 days

---

## Gap Prioritization Examples

### Example 1: Critical Infrastructure

**Gaps:**
- No test framework (Critical, Low effort) → P0
- No src/ directory (Critical, Medium effort) → P0
- Low coverage (High, High effort) → P1

**Order:**
1. Configure pytest (P0, 1 hour)
2. Create src/ directory (P0, 2 hours)
3. Improve coverage (P1, 2 days)

---

### Example 2: Quality Improvements

**Gaps:**
- No type hints (High, High effort) → P1
- No docstrings (Medium, Medium effort) → P2
- Inconsistent naming (Low, Medium effort) → P3

**Order:**
1. Add type hints (P1, 2 days)
2. Add docstrings (P2, 1 day)
3. Standardize naming (P3, 4 hours)

---

## Migration Best Practices

### 1. Incremental Changes
- Make small, verifiable changes
- Run tests after each change
- Commit frequently

### 2. Maintain Functionality
- Never break existing functionality
- Use feature flags if needed
- Keep backwards compatibility when possible

### 3. Parallel Development
- Work on independent gaps in parallel
- Use feature branches
- Merge frequently

### 4. Communication
- Inform team of changes
- Document breaking changes
- Provide migration guides

### 5. Testing
- Add tests before refactoring
- Run full test suite
- Verify coverage doesn't drop

## Tracking Gap Resolution

Use the alignment-tracker.md to monitor progress:

```markdown
# Alignment Tracker

## Phase 1: Critical Foundation

| Gap ID | Description | Status | Completed Date | Notes |
|--------|-------------|--------|----------------|-------|
| S001 | Create src/ directory | [in_progress/done] | YYYY-MM-DD | __ |
| T001 | Configure pytest | [pending/in_progress/done] | YYYY-MM-DD | __ |

**Progress**: 1/2 (50%)
```