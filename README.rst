iFlow CLI Skills
================

A comprehensive skill set for iFlow CLI that extend its capabilities for specialized development workflows.

About
-----

This repository contains reusable, modular skills that can be loaded into iFlow CLI to assist with various development tasks. Each skill provides domain-specific functionality following best practices and standardized workflows.

Skills are organized in the ``.iflow/skills/`` directory and are automatically loaded based on their trigger conditions.

**Inspired by OpenClaw**: This project draws inspiration from OpenClaw's skill system architecture, implementing AgentSkills-compatible skill folders with YAML frontmatter, skill gating, environment injection, and a sophisticated loading system with precedence rules.

Available Skills
----------------

dev-team
~~~~~~~~
An autonomous development team that builds complete projects from requirements to deployment with integrated Karpathy guidelines for high-quality, maintainable code.

**Version:** 2.1.0

**Status:** Documentation Only (See Current Limitations section)

**Purpose:**

An autonomous development team that recruits and manages specialized AI agents to collaborate on software projects following industry best practices and the Karpathy guidelines to prevent common LLM coding pitfalls.

**Team Roles:**

- **Project Manager**: Orchestrates workflow, manages dependencies, makes go/no-go decisions
- **Tech Lead**: Architectural decisions, technology stack selection, code quality standards
- **Frontend Developer**: UI/UX implementation, component development, styling
- **Backend Developer**: API design, database modeling, server-side logic
- **QA Engineer**: Test strategy, test implementation, bug detection
- **DevOps Engineer**: CI/CD pipelines, deployment configuration, infrastructure

**Karpathy Guidelines (Integrated):**

The dev-team skill enforces six core principles to prevent common LLM coding pitfalls:

1. **Think Before Coding** - State assumptions explicitly, present multiple interpretations when ambiguous, push back when simpler approach exists
2. **Simplicity First** - No features beyond what was asked, no abstractions for single-use code, function length ≤50 lines, nesting depth ≤4
3. **Surgical Changes** - Don't improve adjacent code, match existing style, every changed line should trace directly to user's request
4. **Goal-Driven Execution** - Transform imperative tasks into verifiable goals with success criteria, write tests first (TDD)
5. **No Recursive Algorithms** - Reject all recursive implementations, use iterative solutions, verify bounded iteration
6. **No Hardcoding** - Externalize all configuration, use config files, define named constants, prefer data-driven approaches

**Automated Workflow Phases:**

1. **Requirements Analysis** - Extract, validate, and document requirements
2. **Sprint Planning** - Break down into epics, stories, and tasks with dependencies
3. **Development Cycle** - Execute tasks with TDD (Red-Green-Refactor), enforce Karpathy guidelines
4. **Quality Assurance** - Run test suite, check coverage, validate TDD compliance
5. **Deployment** - Build, deploy to staging, validate smoke tests, deploy to production
6. **Delivery Report** - Generate quality metrics, decisions log, handoff documentation

**Quality Gates (Auto-Enforced):**

- Test suite execution
- Coverage thresholds (≥80% lines, ≥70% branches)
- TDD compliance verification
- Code complexity checks (Simplicity First)
- Surgical changes validation
- No hardcoded values detection
- No recursive algorithms detection
- Security vulnerability scan

**Current Limitations:**

The dev-team skill is currently in a documentation-only state. While the SKILL.md and workflows provide comprehensive specifications, the actual implementation does not yet exist. Key components missing:

- No Agent Implementation - Agent definitions exist but no execution code
- No Task Execution Engine - Workflows documented but no execution mechanism
- No State Management System - Mentions state tracking but no implementation
- No Integration with Build Tools - Quality gates mentioned but no actual integration
- Manual Workflow - Relies on user to invoke agents manually

**Roadmap to Full Autonomy:**

A 7-phase implementation plan is documented in SKILL.md:

1. **Phase 1: Core Infrastructure** - Agent Orchestration Engine, State Persistence Layer, Communication Protocol
2. **Phase 2: Quality Integration** - Automated Quality Gates, build tool integration, test runner adapters
3. **Phase 3: Agent Development** - Implement all 6 specialized agents
4. **Phase 4: CI/CD and Deployment** - CI/CD platform integration, deployment pipelines
5. **Phase 5: Project Templates** - Project template system, template registry
6. **Phase 6: Advanced Features** - Autonomous decision making, refactoring automation
7. **Phase 7: User Experience** - Monitoring dashboard, progress visualization

**State Management:**

Persistent state is maintained at project root (``PROJECT_ROOT/.state/``):
- ``project-spec.md`` - Requirements, scope, deliverables
- ``sprint-planner.md`` - Tasks, assignments, progress
- ``team-composition.md`` - Agent assignments and capacity
- ``decisions-log.md`` - Architectural and technical decisions
- ``quality-metrics.md`` - Test coverage, defect density, performance
- ``handover.md`` - Session continuity information

**Integration:**

- Enforces TDD workflow via ``tdd-enforce`` skill
- Uses ``git-manage`` skill for all version control operations
- Invokes ``frontend-tester`` after frontend changes
- Integrates with ``refactor`` skill for code improvements

**Usage:**

.. code-block:: text

    # Build a project with full automation (when implemented)
    dev-team build "Build a task management app with drag-and-drop interface"

    # Check team status
    dev-team status

evaluator
~~~~~~~~~
Guides users through systematic, feature-by-feature testing and evaluation of any project with comprehensive reporting.

**Version:** 1.0.0

**Purpose:**

Provides a structured, user-guided approach to thoroughly test and evaluate any project - web applications, CLI tools, libraries, mobile apps, or any other software project.

**Features:**

- **Project Discovery**: Auto-detects project type and technology stack
- **Feature Extraction**: Builds comprehensive feature checklist from documentation, tests, and code
- **Testing Guidance**: Provides structured testing instructions by project type
- **Progress Tracking**: Maintains state in ``.state/evaluation.md`` for session continuity
- **Issue Tracking**: Categorizes discovered issues by severity with locations
- **Comprehensive Reporting**: Generates detailed evaluation reports with quality metrics
- **Prioritized Recommendations**: Actionable recommendations grouped by priority

**Agent Configuration:**

**Agent Type:** ``evaluator-agent``

**Available Tools:**

- ``read_file`` - Read project files for analysis
- ``list_directory`` - Explore project structure
- ``glob`` - Find specific file patterns
- ``search_file_content`` - Search for feature indicators
- ``web_search`` - Look up public project documentation
- ``web_fetch`` - Fetch reference documentation
- ``image_read`` - Analyze screenshots provided by user

**Excluded Tools:**

- No file modification tools (write_file, replace, xml_escape)
- No system command tools (run_shell_command)

**Note:** The skill only writes to ``.state/evaluation.md`` and ``.state/evaluation-report.md`` for state persistence and report generation.

**Usage:**

.. code-block:: text

    # Start evaluation
    evaluator start

    # Test specific feature
    evaluator test feature 1

    # Report test result
    evaluator pass feature 1
    evaluator fail feature 1: description of issue
    evaluator partial feature 1: partial functionality issue
    evaluator skip feature 1: reason for skipping

    # View status
    evaluator status
    evaluator show checklist

    # Generate report
    evaluator generate report

    # List issues
    evaluator list issues
    evaluator list issues critical

    # Resume evaluation
    evaluator resume

**Workflow Phases:**

1. **Discovery**: Analyzes project structure, detects project type and technology stack
2. **Feature Extraction**: Builds feature checklist from documentation, tests, and code
3. **Testing Guidance**: Provides structured testing instructions for each feature
4. **State Tracking**: Maintains progress and results in ``.state/evaluation.md``
5. **Report Generation**: Creates comprehensive evaluation reports with metrics and recommendations

**Project Types Supported:**

- Web Applications (React, Vue, Angular, Next.js, etc.)
- CLI Tools (Node.js, Python, Rust, Go, etc.)
- Libraries (JavaScript, Python, Rust, etc.)
- Mobile Apps (React Native, Flutter, etc.)
- Desktop Applications (Electron, Tauri, etc.)
- Custom/Hybrid projects

**Quality Metrics:**

- **Feature Completeness**: Percentage of features tested
- **Test Coverage**: Percentage of features with existing tests
- **Reliability**: Percentage of fully working features
- **UX Assessment**: Qualitative assessment based on usability issues
- **Overall Quality Score**: Weighted composite score

**Issue Severity Levels:**

- **Critical**: Feature completely broken, security issue, data loss risk
- **High**: Major functionality broken, significant usability issue
- **Medium**: Feature partially working, minor usability issue
- **Low**: Cosmetic issues, minor enhancements

**Integration:**

- Can use ``git-manage`` to check if issues are in recent commits
- Can use ``tdd-enforce`` to validate if failing features have corresponding tests
- Can use ``dev-team`` skill to fix discovered issues after evaluation
- Uses ``talk`` skill for discussing evaluation results and recommendations

**Exit Codes:**

- ``0`` - Evaluation completed successfully
- ``1`` - Evaluation in progress
- ``2`` - No state file found (use ``evaluator start``)
- ``3`` - Invalid feature number
- ``4`` - Report generation failed

git-manage
~~~~~~~~~~
Provides standardized git operations with safety checks and best practices.

**Version:** 2.0.0

**Features:**

- **Conventional Commits**: Enforced commit message format with type, scope, and description
- **Pre-Commit Checks**: Automated test suite, TDD enforcement, coverage verification
- **Commit Message Formatting**: Automatically generates formatted commit messages with Files changed and Verification sections
- **Safety Mechanisms**: Secrets detection, branch protection, backup before destructive operations
- **Stash Operations**: Save, restore, and manage work in progress
- **Python Implementation**: Fully functional Python-based skill with CLI interface

**Commands:**

.. code-block:: text

    # Status with test results
    python3 .iflow/skills/git-manage/git-manage.py status

    # Stage files
    python3 .iflow/skills/git-manage/git-manage.py add <files...>

    # Commit with conventional format
    python3 .iflow/skills/git-manage/git-manage.py commit <type> <description>
    python3 .iflow/skills/git-manage/git-manage.py commit feat: add user authentication

    # Commit with scope
    python3 .iflow/skills/git-manage/git-manage.py commit <type> --scope <scope> <description>
    python3 .iflow/skills/git-manage/git-manage.py commit feat --scope auth add JWT authentication

    # Commit with body
    python3 .iflow/skills/git-manage/git-manage.py commit <type> <description> --body "<detailed description>"
    python3 .iflow/skills/git-manage/git-manage.py commit feat add authentication --body "Implement secure authentication with JWT tokens.

Changes:
- Add JWT token generation and validation
- Implement bcrypt password hashing
- Add authentication middleware"

    # Skip pre-commit checks
    python3 .iflow/skills/git-manage/git-manage.py commit <type> <description> --no-verify

    # View changes
    python3 .iflow/skills/git-manage/git-manage.py diff
    python3 .iflow/skills/git-manage/git-manage.py diff --staged

    # Undo last commit
    python3 .iflow/skills/git-manage/git-manage.py undo soft
    python3 .iflow/skills/git-manage/git-manage.py undo hard

    # Stash operations
    python3 .iflow/skills/git-manage/git-manage.py stash save <message>
    python3 .iflow/skills/git-manage/git-manage.py stash pop
    python3 .iflow/skills/git-manage/git-manage.py stash list

    # View history
    python3 .iflow/skills/git-manage/git-manage.py log
    python3 .iflow/skills/git-manage/git-manage.py log --full
    python3 .iflow/skills/git-manage/git-manage.py log -n 20

    # Push to remote
    python3 .iflow/skills/git-manage/git-manage.py push origin main

**Commit Types:**

- ``feat`` - New feature
- ``fix`` - Bug fix
- ``refactor`` - Code refactoring
- ``test`` - Adding/updating tests
- ``docs`` - Documentation
- ``chore`` - Maintenance tasks
- ``perf`` - Performance improvements
- ``style`` - Code style changes
- ``build`` - Build system changes
- ``ci`` - CI/CD changes

**Commit Message Format:**

All commits follow this format:

.. code-block:: text

    <type>[<scope>]: <description>

    [optional body with detailed description]

    Changes:
    - <description of change 1>
    - <description of change 2>
    - ...

    ---
    Branch: <branch name>

    Files changed:
    - <file1>
    - <file2>
    - ...

    Verification:
    - Tests: passed/skipped/N/A
    - Coverage: <percentage>%/N/A
    - Architecture: ✓ compliant (only when architecture check runs)
    - TDD: ✓ compliant (only when TDD check runs)

**Pre-Commit Checks:**

Before each commit (unless ``--no-verify`` is used):

1. **Test Suite** - Runs pytest tests/ -v --cov (or project-specific test command)
2. **TDD Enforcement** - Invokes tdd-enforce skill for TDD compliance verification
3. **Coverage Verification** - Ensures coverage meets configured thresholds (default: ≥90% lines, ≥80% branches)

**Configurable Thresholds:**

Coverage thresholds can be configured in ``.iflow/skills/git-manage/config.json``:

.. code-block:: json

    {
      "pre_commit_checks": true,
      "run_tests": true,
      "run_architecture_check": true,
      "run_tdd_check": true,
      "check_coverage": true,
      "detect_secrets": true,
      "branch_protection": true,
      "protected_branches": ["main", "master", "production"],
      "coverage_threshold": 90,
      "branch_coverage_threshold": 80
    }

**Safety Mechanisms:**

- **Secrets Detection**: Scans for API keys, tokens, passwords, private keys before committing
- **Branch Protection**: Prevents direct commits to protected branches (main, master, production)
- **Backup Before Destructive Ops**: Creates backup stash before reset --hard or clean -fd

**Exit Codes:**

- ``0`` - Success
- ``1`` - Tests failed
- ``2`` - Architecture violations
- ``3`` - TDD violations
- ``4`` - No changes to commit
- ``5`` - Secrets detected
- ``6`` - Coverage below threshold
- ``7`` - Branch protection violation

refactor
~~~~~~~~
Automated code refactoring and improvement skill that analyzes codebases to identify and suggest refactoring opportunities.

**Version:** 1.0.0

**Purpose:**

Systematically reviews codebases to identify code quality issues and provide actionable refactoring suggestions for clean, maintainable, and efficient code.

**Features:**

- **Duplicate Code Detection**: Identifies identical or similar code blocks and suggests extraction
- **Magic Literal Extraction**: Converts hardcoded numbers and strings to named constants
- **Function Decomposition**: Breaks down long, complex functions into smaller units
- **Naming Improvements**: Identifies poor naming conventions and suggests improvements
- **Dead Code Elimination**: Finds and suggests removal of unused imports, variables, and functions
- **Complexity Reduction**: Simplifies nested conditionals and complex boolean expressions
- **Code Smell Detection**: Identifies anti-patterns like God Functions, Feature Envy, Data Clumps
- **Import Organization**: Sorts and deduplicates imports
- **10 Language Support**: JavaScript, TypeScript, Python, Java, Go, Rust, C, C++, Ruby

**Capabilities:**

1. **Code Quality Analysis**
   - Comprehensive codebase analysis across multiple dimensions
   - Language-specific pattern matching and anti-pattern detection
   - Configurable thresholds for refactoring decisions

2. **Workflows**
   - ``code-analysis.md``: Main codebase analysis workflow
   - ``duplicate-detection.md``: Duplicate code identification
   - ``constant-extraction.md``: Magic literal extraction
   - ``function-decomposition.md``: Complex function analysis
   - ``dead-code-elimination.md``: Unused code detection
   - ``complexity-reduction.md``: Conditional simplification
   - ``refactoring-report.md``: Report generation

3. **Configuration**
   - ``refactor-rules.json``: Overall refactoring rules and priorities
   - ``language-patterns.json``: Language-specific patterns and anti-patterns
   - ``thresholds.json``: Configurable thresholds (function length, complexity, etc.)

**Usage:**

.. code-block:: text

    # Analyze codebase for refactoring opportunities
    refactor analyze

    # Detect duplicate code
    refactor duplicates

    # Extract magic literals
    refactor constants

    # Decompose complex functions
    refactor decompose

    # Generate refactoring report
    refactor report

**Refactoring Categories:**

- **High Priority**: Duplicates, magic literals (3+ occurrences), complex conditionals
- **Medium Priority**: Long functions, poor naming, dead code, code smells
- **Low Priority**: Import organization, single-occurrence literals

**Output:**

- Prioritized refactoring suggestions with before/after examples
- Impact and effort scores for each suggestion
- Phased action plan (quick wins, medium impact, complex refactorings)
- Risk assessment with mitigation strategies
- Multiple report formats (Markdown, JSON, HTML)

**Integration:**

- Uses ``explore-agent`` for codebase understanding
- Uses ``general-purpose`` agent for applying refactoring suggestions
- Leverages ``search_file_content`` and ``glob`` for pattern matching
- Integrates with ``git-manage`` for version control during refactoring

**Safety:**

- Provides before/after code examples for review
- Highlights potential risks and dependencies
- Groups related refactorings to avoid breaking changes
- Allows selective application of suggestions
- Maintains backward compatibility where possible

talk
~~~~
A conversation-only skill for discussing ideas, brainstorming, getting advice, and exploring concepts without any file modifications or system changes.

**Version:** 1.0.0

**Purpose:**

Pure conversational interaction - talk, discuss, analyze, explore. Nothing gets written or modified.

**Features:**

- **Read-Only Operations**: File reading, searching, and analysis for discussion purposes
- **Web Research**: Search and fetch online resources for informed discussions
- **Image Analysis**: Analyze images for discussion and insights
- **Safe Exploration**: No file modifications, no system commands, no side effects

**Agent Configuration:**

**Agent Type:** ``talk-agent``

**Available Tools:**

- ``read_file`` - read code/files for discussion
- ``glob`` - find files to discuss
- ``search_file_content`` - search to discuss
- ``list_directory`` - explore structure to discuss
- ``web_search`` - research for discussion
- ``web_fetch`` - look up references for discussion
- ``image_read`` - analyze images for discussion

**Excluded Tools:**

- No file modification tools (write_file, replace, xml_escape)
- No system command tools (run_shell_command)

**Usage:**

Automatically triggered when conversation-only interaction is needed:

.. code-block:: text

    # Discuss code architecture
    "Let's talk about the best way to structure this module"

    # Brainstorm ideas
    "Help me brainstorm some approaches for solving this problem"

    # Get advice
    "What are the pros and cons of using this library?"

    # Explore concepts
    "Explain how microservices architecture works"

**Behavior:**

- Read and analyze for discussion purposes only
- Never write, replace, or run commands
- Pure conversational output: insights, analysis, recommendations

**Use Cases:**

- Architecture discussions
- Code reviews without modifications
- Technical planning sessions
- Learning and exploration
- Problem analysis and advice

tdd-enforce
~~~~~~~~~~~
Comprehensive enforcement system that ensures Test-Driven Development (TDD) workflow, project convention compliance, code conciseness, and code quality standards are maintained throughout the development process.

**Version:** 2.0.0

**Purpose:**

Provides unified enforcement of TDD workflow, project conventions, code conciseness, and code quality in a single comprehensive tool.

**Features:**

**TDD Enforcement:**
- **Test-First Lock**: Prevents implementation without corresponding tests
- **TDD Cycle Verification**: Validates Red-Green-Refactor steps
- **Test Structure Validation**: Arrange-Act-Assert pattern, single assertion per test
- **Coverage Thresholds**: ≥90% lines, ≥80% branches (configurable)
- **Critical Coverage**: 100% for integration flow and safety constraints
- **Implementation Restriction**: Cannot modify behavior without test updates
- **Recursion Detection**: Blocks all recursive algorithms (direct, indirect, tail)
- **Infinite Loop Detection**: Blocks while(true), for(;;), unbounded loops
- **Loop Bounding**: Requires explicit termination, max iterations, and timeouts
- **Property-Based Testing**: Validates edge cases with property tests

**Convention Enforcement:**
- **Naming Conventions**: snake_case functions, PascalCase classes, UPPER_SNAKE_CASE constants
- **Code Structure**: Max 50 lines per function, max 10 complexity, max 5 parameters, max 4 nesting
- **Import Organization**: Standard library → third-party → local, sorted alphabetically
- **Type Hints**: Required for all functions with strict mode
- **Docstrings**: Google-style for all public functions

**Code Conciseness Enforcement:**
- **Clean Code Principles**: DRY, KISS, YAGNI, Single Responsibility, Early Returns
- **Comprehensions**: Prefer list/dict/set comprehensions over loops
- **Built-in Functions**: Use sum(), max(), min(), any(), all() instead of manual implementation
- **Minimal Variables**: Max 3 intermediate variables per function
- **One-Liners**: Suggest for simple operations
- **Early Returns**: Reduce nesting depth with guard clauses
- **Ternary Operators**: For simple conditional assignments

**Code Quality Enforcement:**
- **Duplicate Code Detection**: Identical/similar code blocks (≥80% similarity)
- **Magic Literals**: Hardcoded numbers/strings (2+ occurrences, extract to constants)
- **Dead Code Elimination**: Unused imports, variables, functions, classes
- **Code Smells**: God functions, feature envy, data clumps, primitive obsession
- **Complex Conditionals**: Nested if/else (>3 levels), complex boolean expressions

**Usage:**

.. code-block:: text

    # Run TDD enforcement check
    /tdd-enforce

    # Run in watch mode for real-time feedback
    /tdd-enforce watch

**Output Format:**

```
TDD Compliance Report
=====================

Overall Score: 87% (52/60 checks passed)

TDD CYCLE
---------
✓ Test Creation Phase (PASS)
✓ Test Failure (Red) (PASS)
✓ Minimal Implementation (Green) (PASS)
✗ Refactoring Phase (FAIL)

TEST COVERAGE
-------------
Component Coverage: 92% ✓
Integration Flow Coverage: 100% ✓
Safety Constraint Coverage: 95% ✗

CONVENTION COMPLIANCE
----------------------
Naming Conventions: 95% ✓
Code Structure: 88% ✓
Import Organization: 100% ✓
Type Hints: 100% ✓
Docstrings: 90% ✓

CODE CONCISENESS
----------------
Overall Score: 92% ✓

CODE QUALITY
------------
Duplicate Code: 100% ✓
Magic Literals: 95% ✓
Dead Code: 100% ✓
Code Smells: 98% ✓
Complex Conditionals: 90% ✓

RECURSION AND INFINITE LOOPS
-----------------------------
✗ Recursive function detected (FAIL)
✓ All loops have explicit termination (PASS)
✗ Infinite loop pattern detected (FAIL)
```

**Configuration:**

All rules are configurable in ``.iflow/skills/tdd-enforce/config.json``:

.. code-block:: json

    {
      "tdd": {
        "enforceTestFirst": true,
        "requireTestFailure": true,
        "requireMinimalImplementation": true,
        "requireRefactoring": true,
        "coverageThresholds": {
          "lines": 90,
          "branches": 80,
          "functions": 90,
          "statements": 90
        },
        "criticalCoverage": {
          "integrationFlow": 100,
          "safetyConstraints": 100
        }
      },
      "conventions": {
        "naming": {
          "enforceSnakeCase": true,
          "enforcePascalCase": true,
          "minNameLength": 3,
          "forbiddenNames": ["temp", "data", "info", "obj", "var", "item"]
        },
        "structure": {
          "maxFunctionLines": 50,
          "maxComplexity": 10,
          "maxParameters": 5,
          "maxNestingDepth": 4
        }
      },
      "conciseness": {
        "enabled": true,
        "preferComprehensions": true,
        "preferBuiltins": true,
        "maxIntermediateVariables": 3
      },
      "quality": {
        "duplicateCode": {
          "enabled": true,
          "minSimilarityScore": 0.8,
          "minLinesForDuplicate": 5
        },
        "magicLiterals": {
          "enabled": true,
          "minOccurrences": 2,
          "ignoreValues": [0, 1, -1, "", "null", "false", "true"]
        },
        "deadCode": {
          "enabled": true,
          "checkUnusedImports": true,
          "checkUnusedVariables": true
        }
      }
    }

**Integration:**

- Automatically enforced during development when ``dev-team`` skill is active
- Integrates with ``git-manage`` pre-commit checks
- Works with ``refactor`` skill for code quality improvements

**Exit Codes:**

- ``0`` - All checks passed
- ``1`` - Critical violations found (build fails)
- ``2`` - Warnings only (build can continue)
- ``3`` - TDD cycle incomplete
- ``4`` - Convention violations detected
- ``5`` - Code quality issues detected
- ``6`` - Coverage below threshold

**Best Practices:**

1. Always write tests first
2. Ensure tests fail before implementation
3. Write minimal implementation to pass
4. Refactor after green phase
5. Keep tests independent and focused
6. Maintain high coverage (≥90% by default)
7. Update tests when behavior changes
8. Never use recursive algorithms - use iterative solutions
9. Always bound loops with explicit conditions and limits
10. Avoid while(true), for(;;), and infinite loops
11. Follow naming conventions (snake_case, PascalCase, UPPER_SNAKE_CASE)
12. Keep functions small (≤50 lines, ≤10 complexity)
13. Use built-in functions and comprehensions for concise code
14. Extract magic literals to named constants
15. Remove dead code and duplicates

**Anti-Patterns to Avoid:**

- Recursive functions (use iterative solutions)
- Infinite loops (while true, for (;;))
- Over-nesting (use early returns to flatten)
- Verbose loops (use comprehensions)
- Manual implementations of built-in functions
- Forbidden variable names (temp, data, info, obj, var, item)
- Magic numbers and strings
- Duplicate code
- Over-engineered solutions

Skill System Architecture
------------------------

The iFlow CLI skills system is inspired by OpenClaw's architecture and implements AgentSkills-compatible skill folders with several advanced features.

**Skill Loading System with Precedence:**

Skills are loaded from three locations with the following precedence (highest to lowest):

1. **Workspace Skills** - ``<workspace>/skills/`` - Project-specific skills that override others
2. **Managed/Local Skills** - ``~/.iflow/skills/`` - User-managed skills shared across projects
3. **Bundled Skills** - Built-in skills shipped with iFlow CLI

This allows for easy customization and overrides without modifying original skill files.

**Skill Format (AgentSkills Compatible):**

Each skill must have a ``SKILL.md`` file with YAML frontmatter:

.. code-block:: yaml

    ---
    name: skill-name
    description: Brief description of the skill
    version: 1.0.0
    category: development
    ---

    # Skill Name

    Detailed documentation...

**Skill Gating and Filtering:**

Skills are filtered at load time based on metadata:

- **OS Requirements** - ``os: ["darwin", "linux", "win32"]``
- **Binary Dependencies** - ``requires.bins: ["python3", "node"]``
- **Environment Variables** - ``requires.env: ["API_KEY", "DATABASE_URL"]``
- **Configuration Requirements** - ``requires.config: ["git.enabled"]``

This prevents loading skills that can't actually run in the current environment.

**Environment Injection:**

Skills can define environment variables and API keys that are injected only during agent execution:

.. code-block:: yaml

    ---
    name: example-skill
    metadata:
      openclaw:
        primaryEnv: EXAMPLE_API_KEY
    ---

    Configuration in ``openclaw.json``:

    .. code-block:: json

        {
          "skills": {
            "entries": {
              "example-skill": {
                "apiKey": "your-api-key-here"
              }
            }
          }
        }

**User-Invocable Skills:**

Skills can be exposed as slash commands that users can invoke directly:

.. code-block:: yaml

    ---
    name: quick-action
    user-invocable: true
    ---

**Session Snapshot Performance:**

Skills are snapshot when a session starts and reused for performance, with hot-reload capability when skill files change.

**Security Notes:**

- Treat third-party skills as **untrusted code** - read them before enabling
- Prefer sandboxed runs for untrusted inputs and risky tools
- Keep secrets out of prompts and logs

Skill Structure
---------------

Each skill follows this structure::

    .iflow/skills/
    ├── skill-name/
    │   ├── SKILL.md              # Main skill definition with YAML frontmatter
    │   ├── agents/               # Agent definitions (if applicable)
    │   │   ├── project-manager.md
    │   │   ├── tech-lead.md
    │   │   ├── frontend-developer.md
    │   │   ├── backend-developer.md
    │   │   ├── qa-engineer.md
    │   │   └── devops-engineer.md
    │   ├── workflows/            # Workflow documentation
    │   │   ├── development-cycle.md
    │   │   ├── quality-assurance.md
    │   │   └── deployment.md
    │   ├── config/               # Configuration files
    │   │   ├── quality-gates.json
    │   │   ├── accessibility.json
    │   │   └── performance.json
    │   └── .state/               # State management (template only)
    │       └── .gitkeep

Skill Components
----------------

SKILL.md
~~~~~~~~
The main skill definition file containing:
- YAML frontmatter with metadata (name, version, description, category)
- Skill description and purpose
- Usage instructions and examples
- Workflow documentation
- Integration with other skills
- Exit codes and error handling

agents/
~~~~~~~
Directory containing agent definitions for team-based skills:
- Agent roles and responsibilities
- Agent capabilities and specializations
- Interaction protocols and handoff procedures

workflows/
~~~~~~~~~~
Directory containing workflow documentation:
- Phase-by-phase workflows
- Process definitions and checklists
- Best practices and guidelines
- Integration points between phases

config/
~~~~~~~
Directory containing configuration files:
- Quality gates and thresholds
- Accessibility and performance settings
- Browser and platform configurations
- Custom skill-specific settings

.state/
~~~~~~~
State management directory:
- Persistent state tracking
- Session continuity
- Progress tracking
- **Note**: State files are maintained at project root, not in skill directory

Creating a New Skill
--------------------

1. Create a new directory in ``.iflow/skills/``
2. Create a ``SKILL.md`` file with:
   - YAML frontmatter with metadata
   - Skill name, version, description, category
   - Usage instructions and examples
   - Workflow documentation
3. Create additional directories as needed (agents/, workflows/, config/, .state/)
4. Define trigger conditions and integration points
5. Document quality standards and best practices
6. Add skill gating metadata if needed (OS, dependencies, env vars)

**Example SKILL.md:**

.. code-block:: yaml

    ---
    name: my-skill
    description: A brief description of what this skill does
    version: 1.0.0
    category: development
    user-invocable: true
    metadata:
      openclaw:
        os: ["darwin", "linux"]
        requires.bins: ["python3"]
        requires.env: ["MY_API_KEY"]
        primaryEnv: MY_API_KEY
    ---

    # My Skill

    Detailed documentation...

Trigger Conditions
------------------

Skills can be triggered by:
- Keywords in user requests
- Specific commands (e.g., ``/git-manage commit``)
- Context detection (e.g., existing project state)
- Explicit skill activation
- User-invocable slash commands

Usage
-----

How to Use Skills
~~~~~~~~~~~~~~~~~

Skills are automatically loaded and triggered based on their defined conditions.

**Automatic Loading:**

Skills are automatically loaded when:
1. Placed in the ``.iflow/skills/`` directory
2. iFlow CLI scans the skills directory on startup
3. User requests match trigger conditions

**Triggering a Skill:**

.. code-block:: text

    # Trigger dev-team skill
    dev-team build "Create a weather dashboard"

    # Trigger git-manage skill
    python3 .iflow/skills/git-manage/git-manage.py status
    python3 .iflow/skills/git-manage/git-manage.py commit feat: add user authentication

    # Trigger evaluator skill
    evaluator start
    evaluator test feature 1
    evaluator generate report

**Skill Integration:**

Skills work together seamlessly:

.. code-block:: text

    # dev-team automatically uses:
    # - tdd-enforce for development workflow
    # - git-manage for version control

    # git-manage automatically uses:
    # - tdd-enforce for pre-commit validation
    # - refactor for code quality checks

    # evaluator can use:
    # - git-manage to check recent commits
    # - tdd-enforce to validate test coverage
    # - dev-team to fix discovered issues

**Best Practices:**

- Use conventional commit messages with git-manage
- Follow TDD workflow enforced by tdd-enforce
- Leverage dev-team for complex, multi-phase projects (when implemented)
- Use evaluator for systematic project testing and evaluation
- Use refactor for code quality improvements
- Use talk for discussions without modifications
- Check skill status before committing changes

**Inspired by OpenClaw:**

This project draws significant inspiration from OpenClaw's skill system architecture:

- **AgentSkills Compatibility** - Follows the AgentSkills spec for skill format
- **Skill Loading Precedence** - 3-tier system for easy customization
- **Skill Gating** - Filter skills based on OS, dependencies, and environment
- **Environment Injection** - Secure API key management for skills
- **User-Invocable Commands** - Skills as slash commands
- **Session Performance** - Snapshot with hot-reload capability

License
-------

See LICENSE file in the project root.