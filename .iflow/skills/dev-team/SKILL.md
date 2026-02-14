---
name: dev-team
description: An autonomous development team that builds complete projects from requirements to deployment
version: 2.0.0
category: development-team
---

# Dev-Team Skill v2.0

An autonomous development team that builds complete projects from requirements to deployment with full automation.

## Overview

This skill recruits and manages a specialized team of AI agents that collaborate to develop software projects following industry best practices. The team self-organizes, makes architectural decisions, and delivers tested, deployable code.

**NEW in v2.0**: Fully automated workflow from requirements to delivery with intelligent task orchestration.

## Team Roles

- **Project Manager**: Orchestrates workflow, manages dependencies, makes go/no-go decisions
- **Tech Lead**: Architectural decisions, technology stack selection, code quality standards
- **Frontend Developer**: UI/UX implementation, component development, styling
- **Backend Developer**: API design, database modeling, server-side logic
- **QA Engineer**: Test strategy, test implementation, bug detection
- **DevOps Engineer**: CI/CD pipelines, deployment configuration, infrastructure

## Usage

### Initialize a New Project (Fully Automated)
```
dev-team build "Build a task management app with drag-and-drop interface"
```

This command will:
1. Extract and validate requirements
2. Create project specification
3. Generate task breakdown
4. Execute development cycle
5. Run quality assurance
6. Deploy and validate
7. Generate delivery report

### Check Team Status
```
dev-team status
```

### Get Progress Report
```
dev-team standup
```

### Scale Team
```
dev-team scale up frontend  # Add more frontend capacity
dev-team scale down backend  # Reduce backend capacity
```

### Save Session State
```
dev-team handoff
```

## Automated Workflow

### Phase 1: Requirements Analysis (Auto-Init)
```
Input: User requirements
↓
Extract: Project type, features, constraints
↓
Validate: Completeness and feasibility
↓
Output: project-spec.md populated
```

### Phase 2: Sprint Planning (Auto-Breakdown)
```
Input: project-spec.md
↓
Parse: Requirements into epics
↓
Break: Epics into stories
↓
Generate: Task list with dependencies
↓
Output: sprint-planner.md + todo list created
```

### Phase 3: Development Cycle (Auto-Execute)
```
For each task in todo list:
  ↓
  Check: Task type and assign to appropriate agent
  ↓
  Enforce: TDD workflow (tdd-enforce skill)
  ↓
  Execute: Implementation
  ↓
  Verify: Tests pass
  ↓
  Commit: git-manage skill with proper format
  ↓
  Update: Progress tracking
```

### Phase 4: Quality Assurance (Auto-Validate)
```
Input: Completed implementation
↓
Run: Full test suite
↓
Check: Coverage thresholds (≥80% lines, ≥70% branches)
↓
Validate: TDD compliance
↓
Execute: QA Engineer validation
↓
Block: If gates fail, return to Phase 3
↓
Pass: If gates succeed, proceed
```

### Phase 5: Deployment (Auto-Deploy)
```
Input: Validated code
↓
Build: Production bundle
↓
Deploy: To staging environment
↓
Validate: Smoke tests
↓
Deploy: To production
↓
Monitor: Health checks
```

### Phase 6: Delivery Report (Auto-Report)
```
Input: Completed project
↓
Generate: quality-metrics.md updated (in PROJECT_ROOT/.state/)
↓
Generate: decisions-log.md populated (in PROJECT_ROOT/.state/)
↓
Generate: handover.md updated (in PROJECT_ROOT/.state/)
↓
Generate: delivery report
↓
Output: Project ready for user
```

## State Management

The skill maintains persistent state in `.state/` directory at the **project root**:

- **project-spec.md**: Requirements, scope, deliverables
- **sprint-planner.md**: Tasks, assignments, progress
- **team-composition.md**: Agent assignments and capacity
- **decisions-log.md**: Architectural and technical decisions
- **quality-metrics.md**: Test coverage, defect density, performance
- **handover.md**: Session continuity information

**Important**: State files are ALWAYS maintained at the project root (`PROJECT_ROOT/.state/`), NOT in the skill directory. The `.iflow/skills/dev-team/.state/` directory serves only as a template.

**Auto-Update Behavior**: The dev-team skill automatically updates all state files in `.state/` at the project root during:
- Requirements analysis phase → Updates `project-spec.md`
- Sprint planning phase → Updates `sprint-planner.md`
- Development cycle → Updates `team-composition.md` and `decisions-log.md`
- Quality assurance → Updates `quality-metrics.md`
- Completion/handoff → Updates `handover.md`

**State Location**: Always `PROJECT_ROOT/.state/` (e.g., `/Users/inu/_dev/github/navier_stokes/.state/`)

## Agent Dispatcher

The skill includes an intelligent agent dispatcher that:

1. **Task Type Detection**:
   - Frontend tasks → Frontend Developer agent
   - Backend tasks → Backend Developer agent
   - Test tasks → QA Engineer agent
   - Architecture decisions → Tech Lead agent
   - Infrastructure tasks → DevOps Engineer agent
   - Progress tracking → Project Manager agent

2. **Automatic Skill Integration**:
   - Development tasks → Auto-enforce TDD workflow
   - All commits → Auto-use git-manage format
   - Quality gates → Auto-run QA validation
   - Coverage checks → Auto-enforce thresholds

3. **Dependency Management**:
   - Parse task dependencies
   - Execute tasks in correct order
   - Parallelize independent tasks
   - Handle blockers automatically

## Quality Gates (Auto-Enforced)

Before each commit, automatically:

1. ✅ Run test suite
2. ✅ Check coverage ≥80% lines, ≥70% branches
3. ✅ Validate TDD compliance
4. ✅ Run architecture checks
5. ✅ Security vulnerability scan
6. ✅ Accessibility compliance check

If any gate fails:
- Block commit
- Return task to in_progress
- Provide remediation guidance
- Retry after fixes

## Progress Tracking

The skill automatically updates:

- **Real-time progress**: Task completion status
- **Quality metrics**: Coverage, test results, defect count
- **Velocity tracking**: Tasks completed per sprint
- **Blocker management**: Automatic escalation of blockers

## Integration with Other Skills

- **tdd-enforce**: Automatically enforced for all development
- **git-manage**: Automatically used for all commits
- **frontend-tester**: Automatically invoked after frontend changes
- **python-project-builder-tdd**: Template factory for new projects

## Completion Detection

Project is considered complete when:

1. ✅ All todos marked "completed"
2. ✅ All quality gates passed
3. ✅ Final QA validation successful
4. ✅ Build successful
5. ✅ Deployment successful
6. ✅ Smoke tests passing

Then automatically:
- Generate delivery report
- Update quality-metrics.md
- Create handoff documentation
- Notify user project is ready

## Example Usage

```
User: dev-team build "Create a weather dashboard with 7-day forecast, location search, and dark mode"

Dev-Team:
  [INIT] Extracting requirements...
  [PLAN] Creating task breakdown (18 tasks identified)
  [EXEC] Starting development cycle...
    [TDD] Task 1/18: Setup Next.js project
    [TDD] Task 2/18: Create weather API integration
    [TDD] Task 3/18: Build location search component
    [TDD] Task 4/18: Implement 7-day forecast display
    [TDD] Task 5/18: Add dark mode toggle
    [QA] Running test suite... 45 tests passing
    [QA] Coverage: 82% lines, 75% branches ✓
    [COMMIT] feat: setup Next.js project
    [COMMIT] feat: integrate weather API
    [COMMIT] feat: build location search
    [COMMIT] feat: implement forecast display
    [COMMIT] feat: add dark mode
  [VALIDATE] All quality gates passed ✓
  [DEPLOY] Building production bundle...
  [DEPLOY] Deploying to staging...
  [DEPLOY] Smoke tests passed ✓
  [DEPLOY] Deploying to production...
  [REPORT] Project delivered successfully!
  
  📊 Final Stats:
  - Tasks: 18/18 completed
  - Tests: 45 passing
  - Coverage: 82% lines, 75% branches
  - Build time: 47s
  - Total duration: 23 minutes
```

## Exit Codes

- `0` - Project completed successfully
- `1` - Quality gates failed
- `2` - Build failed
- `3` - Deployment failed
- `4` - Requirements invalid
- `5` - Timeout exceeded