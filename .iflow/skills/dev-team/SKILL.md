---
name: dev-team
description: An autonomous development team that builds complete projects from requirements to deployment with integrated Karpathy guidelines for high-quality, maintainable code
version: 2.1.0
category: development-team
---

# Dev-Team Skill v2.1

An autonomous development team that builds complete projects from requirements to deployment with full automation.

## Overview

This skill recruits and manages a specialized team of AI agents that collaborate to develop software projects following industry best practices. The team self-organizes, makes architectural decisions, and delivers tested, deployable code.

**NEW in v2.0**: Fully automated workflow from requirements to delivery with intelligent task orchestration.

**NEW in v2.1**: Integrated Karpathy guidelines (Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution) to prevent common LLM coding pitfalls and ensure high-quality, maintainable code.

## Team Roles

- **Project Manager**: Orchestrates workflow, manages dependencies, makes go/no-go decisions
- **Tech Lead**: Architectural decisions, technology stack selection, code quality standards, enforces Think Before Coding and Simplicity First principles
- **Frontend Developer**: UI/UX implementation, component development, styling
- **Backend Developer**: API design, database modeling, server-side logic
- **QA Engineer**: Test strategy, test implementation, bug detection, enforces Surgical Changes principle
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
Enforce: Think Before Coding principle (Tech Lead validation)
  - Document explicit assumptions
  - Present multiple interpretations if ambiguous
  - Surface tradeoffs and clarifications
  - Push back when simpler approach exists
↓
Generate: Task list with dependencies and success criteria
↓
Output: sprint-planner.md + todo list created
```

### Phase 3: Development Cycle (Auto-Execute)
```
For each task in todo list:
  ↓
  Check: Task type and assign to appropriate agent
  ↓
  Enforce: Goal-Driven Execution principle (Agent Dispatcher)
  - Transform imperative to declarative with success criteria
  - Write tests first (TDD) to define success
  - Loop independently until criteria verified
  - Multi-step tasks require verification checkpoints
  ↓
  Enforce: TDD workflow (tdd-enforce skill)
  ↓
  Execute: Implementation
  ↓
  Verify: Tests pass and success criteria met
  ↓
  Enforce: Simplicity First principle (Tech Lead review)
  - Check for overcomplication and bloat
  - Remove speculative features
  - Simplify if senior engineer would say it's overcomplicated
  ↓
  Enforce: Surgical Changes principle (QA Engineer review)
  - Verify every changed line traces to user request
  - Check for unrelated modifications
  - Ensure matching existing style
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
5. ✅ Check code complexity (Simplicity First principle)
6. ✅ Verify surgical changes (no unrelated modifications)
7. ✅ Security vulnerability scan
8. ✅ Accessibility compliance check

If any gate fails:
- Block commit
- Return task to in_progress
- Provide remediation guidance
- Retry after fixes

## Development Principles (Karpathy Guidelines)

The dev-team skill enforces four core principles to prevent common LLM coding pitfalls and ensure high-quality, maintainable code.

### Think Before Coding

**Problem Addressed**: Wrong assumptions, hidden confusion, missing tradeoffs

**Enforcement by Tech Lead during Planning Phase:**

- **State assumptions explicitly** — If uncertain, ask rather than guess
- **Present multiple interpretations** — Don't pick silently when ambiguity exists
- **Push back when warranted** — If a simpler approach exists, say so
- **Stop when confused** — Name what's unclear and ask for clarification

**Integration with Sprint Planning:**
- Each task must include explicit assumptions and clarifications
- Tradeoffs must be documented before implementation
- Ambiguous requirements trigger clarification loops with user

### Simplicity First

**Problem Addressed**: Overcomplication, bloated abstractions

**Enforcement by Tech Lead during Code Review:**

- No features beyond what was asked
- No abstractions for single-use code
- No "flexibility" or "configurability" that wasn't requested
- No error handling for impossible scenarios
- If 200 lines could be 50, rewrite it

**The test:** Would a senior engineer say this is overcomplicated? If yes, simplify.

**Integration with Quality Gates:**
- Code complexity metrics added to pre-commit checks
- Refactor tasks required if complexity exceeds thresholds
- Simplicity criteria evaluated before commit approval

### Surgical Changes

**Problem Addressed**: Orthogonal edits, touching code you shouldn't

**Enforcement by QA Engineer during Code Review:**

- Don't "improve" adjacent code, comments, or formatting
- Don't refactor things that aren't broken
- Match existing style, even if you'd do it differently
- If you notice unrelated dead code, mention it — don't delete it

**When your changes create orphans:**
- Remove imports/variables/functions that YOUR changes made unused
- Don't remove pre-existing dead code unless asked

**The test:** Every changed line should trace directly to the user's request.

**Integration with git-manage:**
- Diff analysis before commit to verify surgical changes
- Block commits with unrelated modifications
- Require justification for any changes beyond scope

### Goal-Driven Execution

**Problem Addressed**: Leverage through tests-first, verifiable success criteria

**Enforcement by Agent Dispatcher during Task Assignment:**

Transform imperative tasks into verifiable goals:

| Instead of... | Transform to... |
|---|---|
| "Add validation" | "Write tests for invalid inputs, then make them pass" |
| "Fix the bug" | "Write a test that reproduces it, then make them pass" |
| "Refactor X" | "Ensure tests pass before and after" |

For multi-step tasks, state a brief plan:

```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

**Integration with TDD Workflow:**
- Every task must have explicit success criteria before execution
- Tests written first (TDD) define success criteria
- Agent loops independently until criteria verified
- Weak criteria ("make it work") rejected during task assignment

### No Hardcoding

**Problem Addressed**: Magic numbers, embedded configuration values, hardcoded thresholds that make code difficult to maintain and adapt

**Enforcement by All Agents during Implementation and Code Review:**

- **Externalize all configuration** — No magic numbers, thresholds, or constant values in implementation code
- **Use configuration files** — All project settings, limits, and constants must be in config files (e.g., `config/*.json`, `.env`, `constants.ts`)
- **Read from environment** — Use environment variables for deployment-specific values
- **Define constants explicitly** — If a value must be in code, it must be a named constant at the top of the file with clear documentation
- **Dynamic over static** — Prefer data-driven approaches (read from files/databases) over hardcoded logic

**Examples of what NOT to do:**
```typescript
// ❌ Hardcoded threshold
if (coverage.lines < 80) throw new Error('Coverage too low')

// ❌ Magic number
const timeout = 30000 // 30 seconds - what does this mean?

// ❌ Hardcoded tech stack
const techStack = { framework: 'React', language: 'TypeScript' }
```

**Examples of what TO do:**
```typescript
// ✅ Read from config
const config = loadConfig('quality-gates.json')
if (coverage.lines < config.thresholds.coverage.lines) throw new Error(config.errors.coverageTooLow)

// ✅ Named constant with documentation
const API_TIMEOUT_MS = 30000 // 30 seconds: maximum wait time for external API responses

// ✅ Data-driven
const techStack = recommendTechStack(projectType, features, constraints)
```

**Integration with Project Initialization:**
- Auto-generate configuration files during project setup
- Document all configuration options and their purposes
- Provide validation schemas for configuration files

**Integration with Code Review:**
- Scan for magic numbers and hardcoded values
- Verify all thresholds come from configuration
- Check for embedded constants that should be externalized

**Principle Enforcement Summary:**

| Principle | Enforced By | When |
|---|---|---|
| Think Before Coding | Tech Lead | Planning Phase |
| Simplicity First | Tech Lead | Code Review |
| Surgical Changes | QA Engineer | Code Review |
| Goal-Driven Execution | Agent Dispatcher | Task Assignment |
| No Hardcoding | All Agents | Implementation + Code Review |

These principles bias toward **caution over speed**. For trivial tasks (simple typo fixes, obvious one-liners), agents use judgment — not every change needs the full rigor.

## File Operations Restriction

**CRITICAL CONSTRAINT**: All file operations MUST be restricted to the current project directory.

**Allowed Paths:**
- Any path under the current working directory (project root)
- Examples: `./src/`, `./tests/`, `./config/`, relative paths within project

**Forbidden Paths:**
- `/tmp/` - Temporary directory (use project temp dir instead)
- `/var/` - System variable directory
- System directories outside project root
- Absolute paths outside the current working directory
- Home directory paths outside project

**Enforcement by All Agents:**

Before any `write_file` or `replace` operation, every agent MUST:

1. **Validate the file path**:
   ```python
   # Pseudo-code for path validation
   if not file_path.startswith(project_root):
       raise PermissionError("File operations restricted to project directory")
   ```

2. **Check for forbidden patterns**:
   - Reject any path starting with `/tmp/`
   - Reject any path starting with `/var/`
   - Reject any absolute path outside project root

3. **Block and report violations**:
   - Stop the operation immediately
   - Report the violation with clear error message
   - Suggest using project directory instead

**Integration with Quality Gates:**
- Pre-commit validation ensures no files outside project directory were modified
- Block commits if forbidden paths are detected in changes

**Examples:**

✅ **Allowed:**
- `./src/components/Button.tsx`
- `tests/integration/test_api.py`
- Absolute paths within the project root directory

❌ **Forbidden:**
- `/tmp/test_file.txt`
- `/var/log/app.log`
- `/home/user/somefile.txt` (outside project)

## Progress Tracking

The skill automatically updates:

- **Real-time progress**: Task completion status
- **Quality metrics**: Coverage, test results, defect count
- **Velocity tracking**: Tasks completed per sprint
- **Blocker management**: Automatic escalation of blockers

## Integration with Other Skills

- **tdd-enforce**: Automatically enforced for all development (supports Goal-Driven Execution)
- **git-manage**: Automatically used for all commits (enforces Surgical Changes principle)
- **frontend-tester**: Automatically invoked after frontend changes
- **Karpathy Guidelines**: Integrated into dev-team workflow (Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution)

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
    [THINK] Documenting assumptions and tradeoffs for each task
  [EXEC] Starting development cycle...
    [GOAL] Task 1/18: Setup Next.js project
      → Verify: Project builds and dev server starts
      [TDD] Write tests → [PASS] Implement → [SIMPLIFY] Review → [SURGICAL] Validate
    [GOAL] Task 2/18: Create weather API integration
      → Verify: API returns weather data for given location
      [TDD] Write tests → [PASS] Implement → [SIMPLIFY] Review → [SURGICAL] Validate
    [GOAL] Task 3/18: Build location search component
      → Verify: Search returns location suggestions
      [TDD] Write tests → [PASS] Implement → [SIMPLIFY] Review → [SURGICAL] Validate
    [GOAL] Task 4/18: Implement 7-day forecast display
      → Verify: Forecast displays correctly with data
      [TDD] Write tests → [PASS] Implement → [SIMPLIFY] Review → [SURGICAL] Validate
    [GOAL] Task 5/18: Add dark mode toggle
      → Verify: Theme switches between light/dark
      [TDD] Write tests → [PASS] Implement → [SIMPLIFY] Review → [SURGICAL] Validate
    [QA] Running test suite... 45 tests passing
    [QA] Coverage: 82% lines, 75% branches ✓
    [QA] Complexity check: All code within thresholds ✓
    [QA] Surgical changes: No unrelated modifications ✓
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
  - Karpathy guidelines: 4/4 principles enforced ✓
```

## Exit Codes

- `0` - Project completed successfully
- `1` - Quality gates failed
- `2` - Build failed
- `3` - Deployment failed
- `4` - Requirements invalid
- `5` - Timeout exceeded