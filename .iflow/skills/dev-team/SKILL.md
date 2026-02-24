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
  Execute: RED phase (write failing test)
  - Enforce: Test file exists
  - Enforce: Test fails (red phase confirmed)
  ↓
  Execute: GREEN phase (minimal implementation)
  - Enforce: Minimal code to pass test
  - Enforce: No over-engineering
  - Enforce: Test passes (green phase achieved)
  - Enforce: Simplicity First principle (automatic checks)
    - Function length ≤50 lines
    - File length ≤300 lines
    - Nesting depth ≤4
    - Cyclomatic complexity ≤10
    - No over-engineering
  ↓
  Execute: REFACTOR phase (improve code quality)
  - Enforce: Code is refactored
  - Enforce: Tests still pass
  - Enforce: Complexity decreased or unchanged
  - Enforce: Clean code standards (automatic validation)
    - DRY principle (no duplication)
    - Single responsibility
    - Descriptive naming
    - No magic numbers
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
  Verify: Code complexity and quality gates pass
  - Coverage thresholds (≥80% lines, ≥70% branches)
  - Complexity metrics within limits
  - Code duplication <3%
  - Security vulnerabilities below thresholds
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
2. ✅ Check coverage ≥80% lines, ≥70% branches (configurable)
3. ✅ Validate TDD compliance
4. ✅ Check code complexity (Simplicity First principle)
5. ✅ Verify surgical changes (no unrelated modifications)
6. ✅ Check for hardcoded values (No Hardcoding principle)
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

**Automatic Enforcement (during TDD cycle):**

Complexity checks with configurable thresholds (from `config/quality-gates.json`):
- **Function length**: ≤50 lines (break down larger functions)
- **File length**: ≤300 lines (split into smaller modules)
- **Nesting depth**: ≤4 (flatten with early returns/guard clauses)
- **Cyclomatic complexity**: ≤10 (simplify logic, extract methods)
- **Cognitive complexity**: ≤15 (reduce mental effort to understand)

Clean code validation:
- **DRY principle**: No duplicated code blocks >3 lines
- **Single responsibility**: Functions do one thing only
- **Descriptive naming**: No abbreviations, meaningful names
- **No magic numbers**: Extract to named constants

Over-engineering detection:
- Abstractions for single-use code
- "Flexible" patterns without requirements
- Unnecessary error handling for impossible scenarios
- Configurability that wasn't requested

**Integration with Quality Gates:**
- Code complexity metrics enforced in pre-commit checks
- Clean code validation after REFACTOR phase
- Refactor tasks required if complexity exceeds thresholds
- Block commits if clean code violations detected
- Simplicity criteria evaluated automatically at each phase

**Examples of violations:**
- ❌ Function with 75 lines (max: 50) → Split into 3 smaller functions
- ❌ Nesting depth 6 (max: 4) → Use early returns or extract to helper
- ❌ Cyclomatic complexity 15 (max: 10) → Extract complex logic
- ❌ Same 5-line code block in 3 places → Extract to function
- ❌ Function called `proc` → Rename to `processPayment`
- ❌ Magic number `3000` → `const MAX_RETRY_DELAY_MS = 3000`

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

### No Recursive Algorithms and Infinite Loops

**Problem Addressed**: Stack overflow risks, unpredictable performance, difficult debugging, resource exhaustion

**Enforcement by Tech Lead during Code Review:**

- **Reject all recursive implementations** — Use iterative solutions instead
- **Require explicit loop termination** — All loops must have clear exit conditions
- **Verify bounded iteration** — No infinite loops (while true, for (;;))
- **Check for recursion patterns** — Self-referential function calls are prohibited
- **Validate loop safety** — Ensure loops have maximum iteration limits or timeouts

**Quality Gate Enforcement:**
Before each commit, automatically scan for:
- Recursive function calls (function calling itself directly or indirectly)
- Infinite loop patterns (`while(true)`, `while(1)`, `for(;;)`)
- Unbounded loops without explicit termination conditions
- Mutual recursion between functions
- Tail recursion (still prohibited - use iteration)

**Examples of what NOT to do:**
```typescript
// ❌ Recursive function - stack overflow risk
function factorial(n: number): number {
  if (n <= 1) return 1
  return n * factorial(n - 1)
}

// ❌ Recursive tree traversal
function traverse(node: Node) {
  console.log(node.value)
  if (node.left) traverse(node.left)
  if (node.right) traverse(node.right)
}

// ❌ Infinite loop - never terminates
while (true) {
  processMessages()
}

// ❌ Infinite loop - unbounded
for (;;) {
  waitForEvent()
}

// ❌ Mutual recursion
function isEven(n: number): boolean {
  if (n === 0) return true
  return isOdd(n - 1)
}

function isOdd(n: number): boolean {
  if (n === 0) return false
  return isEven(n - 1)
}

// ❌ Unbounded while loop
while (!isDone()) {
  processItem(items.pop())
}
```

**Examples of what TO do:**
```typescript
// ✅ Iterative factorial
function factorial(n: number): number {
  let result = 1
  for (let i = 2; i <= n; i++) {
    result *= i
  }
  return result
}

// ✅ Iterative tree traversal
function traverse(root: Node) {
  const stack: Node[] = [root]
  while (stack.length > 0) {
    const node = stack.pop()
    console.log(node.value)
    if (node.right) stack.push(node.right)
    if (node.left) stack.push(node.left)
  }
}

// ✅ Bounded loop with timeout
const MAX_ITERATIONS = 1000
const startTime = Date.now()
const TIMEOUT_MS = 5000

while (!isDone() && iterationCount < MAX_ITERATIONS && (Date.now() - startTime) < TIMEOUT_MS) {
  processItem(items.pop())
  iterationCount++
}

// ✅ Explicit condition
while (hasMoreMessages()) {
  const message = getNextMessage()
  if (!message) break
  processMessage(message)
}

// ✅ Iterative solution for mutual recursion
function isEven(n: number): boolean {
  return n % 2 === 0
}

function isOdd(n: number): boolean {
  return n % 2 !== 0
}

// ✅ Queue-based processing
function processQueue(queue: QueueItem[]) {
  for (const item of queue) {
    if (item.shouldProcess) {
      processItem(item)
    }
  }
}
```

**Integration with Code Review:**
- AST analysis to detect recursive function calls
- Pattern matching for infinite loop constructs
- Control flow analysis to verify loop termination
- Block commits containing recursive implementations
- Flag infinite loops as critical violations

**Integration with Quality Gates:**
- Pre-commit validation scans for recursion patterns
- Block commits with unbounded loops
- Require maximum iteration limits for all loops
- Validate all while/for loops have explicit conditions

### No Hardcoding

**Problem Addressed**: Magic numbers, embedded configuration values, hardcoded thresholds that make code difficult to maintain and adapt

**Enforcement by All Agents during Implementation and Code Review:**

- **Externalize all configuration** — No magic numbers, thresholds, or constant values in implementation code
- **Use configuration files** — All project settings, limits, and constants must be in config files (e.g., `config/*.json`, `.env`, `constants.ts`)
- **Read from environment** — Use environment variables for deployment-specific values
- **Define constants explicitly** — If a value must be in code, it must be a named constant at the top of the file with clear documentation
- **Dynamic over static** — Prefer data-driven approaches (read from files/databases) over hardcoded logic

**Quality Gate Enforcement:**
Before each commit, automatically scan for:
- Numeric literals that aren't defined constants
- String literals used as configuration values
- Threshold values embedded in conditionals
- URLs, API endpoints, or service addresses
- File paths outside the project directory
- Magic numbers without context (comments not sufficient)

**Examples of what NOT to do:**
```typescript
// ❌ Hardcoded threshold
if (coverage.lines < 80) throw new Error('Coverage too low')

// ❌ Magic number
const timeout = 30000 // 30 seconds - what does this mean?

// ❌ Hardcoded tech stack
const techStack = { framework: 'React', language: 'TypeScript' }

// ❌ Hardcoded API endpoint
const API_URL = 'https://api.example.com/v1'

// ❌ Hardcoded file path
const logFile = '/var/log/app.log'

// ❌ Magic number in loop
for (let i = 0; i < 100; i++) { /* what is 100? */ }
```

**Examples of what TO do:**
```typescript
// ✅ Read from config
const config = loadConfig('quality-gates.json')
if (coverage.lines < config.coverage.lines) throw new Error(config.errors.coverageTooLow)

// ✅ Named constant with documentation
const API_TIMEOUT_MS = 30000 // 30 seconds: maximum wait time for external API responses

// ✅ Data-driven
const techStack = recommendTechStack(projectType, features, constraints)

// ✅ Environment variable
const API_URL = process.env.API_URL || 'https://api.example.com/v1'

// ✅ Project-relative path
const logFile = path.join(process.cwd(), 'logs', 'app.log')

// ✅ Named constant
const MAX_RETRY_ATTEMPTS = 100
for (let i = 0; i < MAX_RETRY_ATTEMPTS; i++) { /* ... */ }
```

**Integration with Project Initialization:**
- Auto-generate configuration files during project setup
- Document all configuration options and their purposes
- Provide validation schemas for configuration files
- Create `.env.example` template for environment variables

**Integration with Code Review:**
- Scan for magic numbers and hardcoded values
- Verify all thresholds come from configuration
- Check for embedded constants that should be externalized
- Validate file paths are project-relative
- Block commits with hardcoded values detected

**Principle Enforcement Summary:**

| Principle | Enforced By | When |
|---|---|---|
| Think Before Coding | Tech Lead | Planning Phase |
| Simplicity First | Tech Lead | Code Review |
| Surgical Changes | QA Engineer | Code Review |
| Goal-Driven Execution | Agent Dispatcher | Task Assignment |
| No Hardcoding | All Agents | Implementation + Code Review |
| No Recursive Algorithms | Tech Lead + Quality Gates | Code Review + Pre-commit |

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
- User configuration directories outside project

**Enforcement by All Agents:**

Before any `write_file` or `replace` operation, every agent MUST:

1. **Validate the file path**:
   ```python
   # Pseudo-code for path validation
   import os
   project_root = os.getcwd()
   abs_path = os.path.abspath(file_path)

   if not abs_path.startswith(project_root):
       raise PermissionError(
           f"File operations restricted to project directory. "
           f"Attempted: {abs_path}, Project root: {project_root}"
       )
   ```

2. **Check for forbidden patterns**:
   - Reject any path starting with `/tmp/`
   - Reject any path starting with `/var/`
   - Reject any path starting with `/home/` (unless within project)
   - Reject any path starting with `/Users/` (unless within project)
   - Reject any absolute path outside project root

3. **Block and report violations**:
   - Stop the operation immediately
   - Report the violation with clear error message
   - Suggest using project directory instead
   - Log the attempted operation for audit

4. **Quality Gate Validation**:
   - Pre-commit validation ensures no files outside project directory were modified
   - Block commits if forbidden paths are detected in changes
   - Scan git diff for absolute paths outside project root

**Examples:**

✅ **Allowed:**
- `./src/components/Button.tsx`
- `tests/integration/test_api.py`
- `/Users/inu/project/src/app.tsx` (within project root)
- `/path/to/project/config/settings.json` (within project root)

❌ **Forbidden:**
- `/tmp/test_file.txt`
- `/var/log/app.log`
- `/home/user/somefile.txt` (outside project)
- `/Users/inu/somefile.txt` (outside project)
- `~/.bashrc` (user config)
- `/etc/hosts` (system config)

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

## Current Limitations

**IMPORTANT**: The dev-team skill is currently in a documentation-only state. While the SKILL.md and workflows provide comprehensive specifications for an autonomous development team, the actual implementation does not yet exist.

### What's Missing

1. **No Agent Implementation** - The skill has agent definitions (Project Manager, Tech Lead, Frontend Developer, Backend Developer, QA Engineer, DevOps Engineer) in markdown files, but there's no actual code to execute these agents or orchestrate their work.

2. **No Task Execution Engine** - The workflows are documented but there's no mechanism to actually run them, track progress, or hand off between agents.

3. **No State Management System** - While it mentions persistent state tracking at project root, there's no actual implementation for storing/retrieving state between sessions.

4. **No Integration with Build Tools** - The skill mentions "quality gates" and "CI/CD pipeline" but doesn't actually integrate with build systems, test runners, or deployment tools.

5. **Manual Workflow** - The current implementation relies on the user to invoke different agents manually rather than having an autonomous orchestration system.

## Roadmap to Full Autonomy

To transform dev-team from documentation to a fully autonomous development pipeline, the following components need to be implemented:

### 1. Agent Orchestration Engine

A central dispatcher that can:
- Analyze requirements and break them into tasks
- Assign tasks to appropriate specialized agents
- Track task completion and dependencies
- Handle failures and retries
- Coordinate handoffs between agents

**Implementation Approach**:
- Create a Python-based orchestration engine
- Use task queue system (Celery, RQ, or custom)
- Implement dependency graph for task scheduling
- Add retry mechanism with exponential backoff
- Support parallel execution of independent tasks

### 2. State Persistence Layer

A robust state management system that:
- Stores project context, decisions, and progress
- Enables session continuity
- Tracks handoffs between agents
- Maintains project specification and sprint plans

**Implementation Approach**:
- Use SQLite or JSON-based storage at project root
- Implement versioning for state files
- Add automatic state snapshots
- Support state recovery from interruptions
- Provide query interface for state inspection

### 3. Automated Quality Gates

Actual integration with:
- Test runners (pytest, jest, vitest, etc.)
- Linters and formatters (ESLint, Prettier, Black, etc.)
- Static analysis tools (SonarQube, ESLint, Ruff)
- Coverage reporters (Coverage.py, Istanbul)
- TDD enforcement (tdd-enforce skill integration)
- Complexity analysis (maintainability index, cyclomatic complexity)

**Implementation Approach**:
- Create adapter layer for different tools
- Implement configurable quality thresholds
- Add blocking/non-blocking checks
- Generate quality reports
- Integrate with git-manage pre-commit hooks

### 4. CI/CD Integration

Connect to actual CI/CD platforms:
- GitHub Actions, GitLab CI, CircleCI, Jenkins
- Automated deployment to staging/production
- Rollback mechanisms
- Environment configuration management
- Infrastructure as Code (Terraform, AWS CDK)

**Implementation Approach**:
- Support multiple CI/CD platforms via adapters
- Auto-generate CI/CD configuration files
- Implement deployment pipeline templates
- Add rollback capabilities
- Support multi-environment deployments

### 5. Project Template System

Create scaffolding for:
- Different project types (web, CLI, library, mobile)
- Pre-configured build systems (Vite, Webpack, Rollup, Cargo)
- Standardized testing setup
- Documentation templates
- Configuration management

**Implementation Approach**:
- Create template registry with metadata
- Implement template selection based on requirements
- Add template customization capabilities
- Support project initialization from templates
- Maintain template versioning

### 6. Autonomous Decision Making

Implement:
- Architecture decision logging (ADR format)
- Technology selection heuristics
- Conflict resolution between agents
- Automatic refactoring suggestions
- Tradeoff analysis and documentation

**Implementation Approach**:
- Create decision framework with criteria
- Implement scoring system for alternatives
- Add decision logging with rationale
- Support manual override of decisions
- Provide decision audit trail

### 7. Communication Protocol

Define:
- Standard message format between agents
- Task completion confirmation
- Error handling and escalation
- Progress reporting
- Agent handoff protocol

**Implementation Approach**:
- Design JSON-based message schema
- Implement message bus/event system
- Add message validation and type checking
- Support async communication
- Provide logging and debugging tools

### 8. Monitoring and Observability

Add:
- Real-time progress tracking dashboard
- Agent health monitoring
- Performance metrics (execution time, success rate)
- Debugging tools and logs
- Alert system for failures

**Implementation Approach**:
- Create web-based dashboard (Streamlit, Gradio)
- Implement metrics collection and aggregation
- Add log aggregation and search
- Support real-time progress updates
- Provide alerting via multiple channels

## Implementation Phases

### Phase 1: Core Infrastructure (Foundation)
- Implement Agent Orchestration Engine
- Create State Persistence Layer
- Define Communication Protocol
- Add basic monitoring

### Phase 2: Quality Integration
- Implement Automated Quality Gates
- Integrate with build tools
- Add test runner adapters
- Implement coverage reporting

### Phase 3: Agent Development
- Implement Project Manager agent
- Implement Tech Lead agent
- Implement Frontend Developer agent
- Implement Backend Developer agent
- Implement QA Engineer agent
- Implement DevOps Engineer agent

### Phase 4: CI/CD and Deployment
- Add CI/CD platform integration
- Implement deployment pipelines
- Add rollback mechanisms
- Support multi-environment deployments

### Phase 5: Project Templates
- Create project template system
- Build template registry
- Add template customization
- Support project initialization

### Phase 6: Advanced Features
- Implement autonomous decision making
- Add refactoring automation
- Integrate with refactor skill
- Add performance optimization

### Phase 7: User Experience
- Create monitoring dashboard
- Add progress visualization
- Implement interactive debugging
- Support manual intervention

## Next Steps

To begin implementing the autonomous dev-team skill:

1. **Phase 1 Start**: Implement the Agent Orchestration Engine as a Python module
2. **Define Protocol**: Create the Communication Protocol specification
3. **State Management**: Implement the State Persistence Layer
4. **Agent Skeletons**: Create basic agent implementations with placeholders
5. **Integration**: Connect with existing skills (tdd-enforce, git-manage, refactor)
6. **Testing**: Create comprehensive test suite for all components
7. **Documentation**: Update SKILL.md as implementations are completed

The roadmap is designed to build incrementally, with each phase building on the previous one, allowing for iterative development and testing.