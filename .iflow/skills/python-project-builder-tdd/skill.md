---
name: python-project-builder-tdd
description: A comprehensive skill for building Python projects following Test-Driven Development (TDD) methodology. Covers the full project lifecycle from product design to deployment using uv for package management.
license: Apache
---

# Python Project Builder (TDD)

**Name**: python-project-builder-tdd

**Description**: A comprehensive skill for building Python projects following Test-Driven Development (TDD) methodology. Covers the full project lifecycle from product design to deployment using uv for package management.

**Trigger Conditions**:
This skill should be automatically invoked when:
- User requests to develop a Python application, library, or tool
- User asks to create a Python project
- User requests Python development with testing requirements
- User asks to "continue", "resume", or "continue working on" a project
- User requests a change: "change", "modify", "update", "requirement change", "feature change"
- User requests project alignment: "align project", "fix project structure", "improve code quality", "migrate project"
- Keywords: "python", "develop", "create project", "build app", "tdd", "test-driven", "continue", "resume", "change", "modify", "update", "align", "compliance", "standards", "refactor", "migrate"

**Workflow Phases**:
0. **Assessment** (00-assessment/) - Project analysis, compliance check, gap identification
1. **Planning** (01-planning/) - Feature breakdown, dependency mapping, effort estimation
2. **Architecture** (02-architecture/) - Module design, interface design, data flow
3. **Development** (03-development/) - TDD workflow, feature implementation, code standards
4. **Testing** (04-testing/) - Test strategy, coverage requirements, edge cases
5. **Quality Assurance** (05-quality-assurance/) - Feature verification, integration checks, performance validation
6. **Deployment** (06-deployment/) - Build process, deployment strategies

**Project Setup**:
- Use `uv` for package management
- Standard structure: `src/` for source code, `tests/` for tests
- Use `pytest` as the testing framework
- Follow TDD: Write tests first, then implement

**Tracking**:
- Track features in `FEATURES.md`
- Track test coverage in `test-coverage-tracker.md`
- Track bugs/issues in `bug-tracker.md`

**Key Commands**:
- `uv init` - Initialize project
- `uv add pytest` - Add pytest dependency
- `uv run pytest` - Run tests
- `uv run pytest --cov` - Run tests with coverage
- `uv build` - Build project

**Quality Standards**:
- Minimum 80% test coverage per feature
- All features must pass acceptance criteria
- Integration tests required for feature interactions
- Edge cases must be identified and tested

**Instructions**:

### Initial Project Assessment:
When skill is invoked:
1. Check if project exists in current directory
   - If NO → Initialize new project (follow standard workflow from Phase 1)
   - If YES → Check for .state/ directory
     - If .state/ exists → Load and resume existing project
     - If .state/ not exists → Run project assessment:
       1. Analyze project structure and tools (00-assessment/project-analysis.md)
       2. Check compliance with standards (00-assessment/compliance-check.md)
       3. Perform gap analysis (00-assessment/gap-analysis.md)
       4. If compliant (≥80%) → Initialize state and start working
       5. If not compliant (<80%) → Propose migration plan:
          - Show gaps and priorities
          - Ask user to confirm alignment approach
          - Create migration plan in .state/
          - Execute alignment incrementally

### When Starting a New Project:
1. Initialize project state in `.state/` directory
2. Create `project-state.md` with project information
3. Follow each phase sequentially
4. Use checklists to verify completion
5. Update trackers to monitor progress
6. Ensure all quality standards are met before deployment

### When Resuming an Existing Project:
1. **Check for Existing State**: Look for `.state/` directory
2. **Read Project State**: Load `project-state.md` to understand current status
3. **Read Current Feature**: Load `current-feature.md` to see what's being worked on
4. **Read Next Steps**: Load `next-steps.md` to see what to do next
5. **Check Checkpoints**: Review `checkpoints/` for any saved progress
6. **Resume Work**: Continue from the last checkpoint or next step
7. **Update State**: Update state files as progress is made

### When Aligning Existing Projects:
1. **Analyze Project**: Run compliance check to identify gaps
   - Use `00-assessment/project-analysis.md` to understand current state
   - Use `00-assessment/compliance-check.md` to verify compliance
2. **Gap Analysis**: Document deviations and their impact
   - Use `00-assessment/gap-analysis.md` to create gap report
   - Prioritize gaps based on impact and effort
3. **Create Migration Plan**: Prioritize changes based on impact/effort
   - Create alignment phases (P0 critical, P1 high, P2 medium, P3 low)
   - Document dependencies between gaps
   - Estimate effort for each phase
4. **Execute Migration**: Apply changes incrementally
   - Start with P0 critical gaps
   - Make small, verifiable changes
   - Run tests after each change
   - Update alignment-tracker.md
5. **Verify Compliance**: Re-check after each change
   - Run compliance check
   - Update compliance score
   - Verify no regressions
6. **Update State**: Track migration progress in state files
   - Update `alignment-progress.md`
   - Save checkpoints after each phase
   - Document any blockers or issues

### State Persistence:
- **Project State**: `.state/project-state.md` - Overall project status
- **Current Feature**: `.state/current-feature.md` - Feature being worked on
- **Completed Checklist**: `.state/completed-checklist.md` - What's been done
- **Next Steps**: `.state/next-steps.md` - What to do next
- **Checkpoints**: `.state/checkpoints/` - Phase-specific checkpoints
- **Context**: `.state/context/` - Saved context and decisions

### Session Management:
- **Start Session**: Create session entry in `completed-checklist.md`
- **Save Checkpoint**: Save progress before pausing
- **Update Next Steps**: Update `next-steps.md` before ending
- **Document Context**: Save important context in `context/`
- **Clear Handoff**: Provide clear resume instructions

### Resume Commands:
- "continue working on [project]" - Resume project work
- "resume [feature]" - Resume specific feature
- "what's next?" - Show next steps
- "show progress" - Display project progress
- "pause" - Save current state and pause

### Alignment Commands:
- "analyze project" - Assess current project structure, tools, and compliance
- "show gaps" - Display compliance gaps with priorities and impact
- "check compliance" - Verify current alignment status and show compliance score
- "migration plan" - Show/modify migration plan for alignment
- "migration status" - Show progress of alignment efforts
- "migrate [component]" - Align specific component (structure/tests/standards/tools)
- "align project" - Start or continue project alignment process

### Change Management:
When changes are requested during development:

#### Change Detection
- Check for requirement changes at phase start
- Monitor for feature specification updates
- Detect breaking changes in code
- Identify dependency changes

#### Change Workflow
1. **Document Change**: Record in `.state/context/change-log.md`
2. **Analyze Impact**: Update `.state/context/impact-analysis.md`
3. **Assess State**: Check current progress in state files
4. **Make Decision**: Decide approach (continue/adapt/replan/rollback)
5. **Update State**: Modify all relevant state files
6. **Implement Change**: Execute change following checkpoints
7. **Verify Change**: Re-run tests and QA
8. **Document Rollback**: Update `.state/context/rollback-plan.md`

#### Change Commands:
- "change [feature/requirement]" - Initiate change request
- "impact [change]" - Analyze impact of change
- "approve [change]" - Approve change for implementation
- "reject [change]" - Reject change request
- "rollback [change]" - Rollback implemented change
- "show changes" - Display change history
- "show impact [change]" - Show impact analysis

#### Change Types:
- **Minor Changes**: Small tweaks, continue work with adaptations
- **Moderate Changes**: Feature modifications, adjust plan and implement
- **Major Changes**: New requirements, replan and restructure
- **Breaking Changes**: Architectural changes, may require rollback and restart

#### Alignment Types:
When aligning existing projects, different areas may need attention:

- **Structural Alignment**: Fix directory structure (src/, tests/ organization, config files)
  - Impact: High - affects imports and tooling
  - Effort: Medium - requires moving files and updating imports
  - Priority: P0 (Critical) - Blocks many other improvements

- **Testing Alignment**: Add pytest, reorganize tests, achieve coverage
  - Impact: High - affects code quality and confidence
  - Effort: High - requires writing tests and refactoring
  - Priority: P1 (High) - Essential for TDD workflow

- **Standards Alignment**: Apply PEP 8, type hints, docstrings
  - Impact: Medium - improves code maintainability
  - Effort: High - requires code changes across project
  - Priority: P1 (High) - Important for long-term maintainability

- **Tooling Alignment**: Integrate ruff, black, mypy, pre-commit hooks
  - Impact: Medium - improves development experience
  - Effort: Low - configuration and setup
  - Priority: P1 (High) - Quick wins with high value

- **Process Alignment**: Adopt TDD workflow for new features
  - Impact: High - affects development approach
  - Effort: Medium - requires behavior change
  - Priority: P2 (Medium) - Can be adopted gradually

- **State Management Alignment**: Set up .state/ tracking
  - Impact: Low - improves project tracking
  - Effort: Low - template setup
  - Priority: P2 (Medium) - Nice to have for complex projects

#### Change Integration with Phases:
- **Planning Phase**: Check for requirement changes before planning
- **Architecture Phase**: Assess impact on architecture, update if needed
- **Development Phase**: Adapt implementation to changes, update code and tests
- **Testing Phase**: Update tests for changes, re-run validation
- **QA Phase**: Re-verify changed features, update verification checklist
- **Deployment Phase**: Ensure changes are deployed correctly, update deployment plan

#### State Files for Changes:
- **change-log.md**: Track all changes and their status
- **impact-analysis.md**: Analyze and document impact of each change
- **rollback-plan.md**: Document rollback procedures for each change
- **project-state.md**: Update with change history
- **current-feature.md**: Track change status for current feature
- **next-steps.md**: Reprioritize based on changes

#### State Files for Alignment:
- **compliance-report.md**: Current compliance status and score
- **gap-analysis.md**: Identified gaps with priorities and impact analysis
- **migration-plan.md**: Step-by-step alignment plan with phases
- **migration-progress.md**: Track completed alignment steps and remaining work
- **alignment-checklist.md**: Checklist of alignment tasks and their status

#### Change Checkpoints:
- **change-request-checkpoint.md**: Track change requests and approval
- **change-impact-checkpoint.md**: Track impact analysis progress
- **change-implementation-checkpoint.md**: Track change implementation progress

#### Alignment Checkpoints:
- **assessment-checkpoint.md**: Project analysis complete, compliance score calculated
- **migration-planning-checkpoint.md**: Migration plan created and approved
- **migration-execution-checkpoint.md**: Track progress of alignment phases
- **phase-0-checkpoint.md**: Assessment phase complete
- **phase-1-checkpoint.md**: Critical alignment complete
- **phase-2-checkpoint.md**: High priority alignment complete
- **phase-3-checkpoint.md**: Medium priority alignment complete
- **phase-4-checkpoint.md**: Low priority alignment complete
- **alignment-complete-checkpoint.md**: Project fully compliant
