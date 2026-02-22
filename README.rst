iFlow CLI Skills
================

A comprehensive skill set for iFlow CLI that extend its capabilities for specialized development workflows.

About
-----

This repository contains reusable, modular skills that can be loaded into iFlow CLI to assist with various development tasks. Each skill provides domain-specific functionality following best practices and standardized workflows.

Skills are organized in the ``.iflow/skills/`` directory and are automatically loaded based on their trigger conditions.

Available Skills
----------------

dev-team
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
   - `code-analysis.md`: Main codebase analysis workflow
   - `duplicate-detection.md`: Duplicate code identification
   - `constant-extraction.md`: Magic literal extraction
   - `function-decomposition.md`: Complex function analysis
   - `dead-code-elimination.md`: Unused code detection
   - `complexity-reduction.md`: Conditional simplification
   - `refactoring-report.md`: Report generation

3. **Configuration**
   - `refactor-rules.json`: Overall refactoring rules and priorities
   - `language-patterns.json`: Language-specific patterns and anti-patterns
   - `thresholds.json`: Configurable thresholds (function length, complexity, etc.)

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

- Uses `explore-agent` for codebase understanding
- Uses `general-purpose` agent for applying refactoring suggestions
- Leverages `search_file_content` and `glob` for pattern matching
- Integrates with `git-manage` for version control during refactoring

**Safety:**

- Provides before/after code examples for review
- Highlights potential risks and dependencies
- Groups related refactorings to avoid breaking changes
- Allows selective application of suggestions
- Maintains backward compatibility where possible

evaluator
git-manage
~~~~~~~~
An autonomous development team that builds complete projects from requirements to deployment with full automation.

**Version:** 2.0.0

**Features:**

- **Automated Workflow**: Full automation from requirements to delivery
- **Intelligent Task Orchestration**: Agent dispatcher assigns tasks to specialized agents
- **Quality Gates**: Automated pre-commit checks (tests, coverage, TDD compliance, architecture)
- **State Management**: Persistent state tracking at project root for session continuity

**Team Roles:**

- Project Manager - Orchestrates workflow, manages dependencies
- Tech Lead - Architecture, standards, code reviews
- Frontend Developer - UI/UX, components
- Backend Developer - API, database, business logic
- QA Engineer - Testing, quality assurance
- DevOps Engineer - CI/CD, deployment

**Usage:**

.. code-block:: text

    # Build a project with full automation
    dev-team build "Build a task management app with drag-and-drop interface"

    # Check team status
    dev-team status

**Workflow Phases:**

1. Requirements Analysis - Extract and validate requirements
2. Sprint Planning - Break down into epics, stories, and tasks
3. Development Cycle - Parallel execution with continuous integration
4. Quality Assurance - Automated testing, code reviews, bug fixing
5. Deployment - CI/CD pipeline, staging validation, production rollout
6. Delivery Report - Generate project delivery documentation

**Integration:**

- Automatically enforces TDD workflow via ``tdd-enforce`` skill
- Uses ``git-manage`` skill for all version control operations
- Invokes ``frontend-tester`` after frontend changes

git-manage
~~~~~~~~~~
Provides standardized git operations with safety checks and best practices.

**Features:**

- **Conventional Commits**: Enforced commit message format
- **Pre-Commit Checks**: Automated test suite, architecture checks, TDD enforcement, coverage verification
- **Safety Mechanisms**: Secrets detection, branch protection, backup before destructive operations
- **Stash Operations**: Save, restore, and manage work in progress

**Commands:**

.. code-block:: text

    # Status with test results
    /git-manage status

    # Stage files
    /git-manage add <files...>

    # Commit with conventional format
    /git-manage commit <type>[:scope] <description>

    # View changes
    /git-manage diff [staged|unstaged|<commit>]

    # Undo last commit
    /git-manage undo [soft|hard]

    # Stash operations
    /git-manage stash save <message>
    /git-manage stash pop

    # Push with validation
    /git-manage push [remote] [branch]

**Commit Types:**

- ``feat`` - New feature
- ``fix`` - Bug fix
- ``refactor`` - Code refactoring
- ``test`` - Adding/updating tests
- ``docs`` - Documentation
- ``chore`` - Maintenance tasks

**Pre-Commit Checks:**

1. Test suite execution
2. Architecture compliance verification
3. TDD compliance verification
4. Coverage threshold check (≥90%)

**Exit Codes:**

- ``0`` - Success
- ``1`` - Tests failed
- ``2`` - Architecture violations
- ``3`` - TDD violations
- ``4`` - No changes to commit
- ``5`` - Secrets detected
- ``6`` - Coverage below threshold
- ``7`` - Branch protection violation

tdd-enforce
~~~~~~~~~~~
Ensures Test-Driven Development (TDD) workflow is followed throughout the development process.

**Features:**

- **TDD Cycle Enforcement**: Red-Green-Refactor cycle verification
- **Test Coverage Validation**: Ensures adequate test coverage before implementation
- **Quality Gates**: Blocks non-TDD compliant development
- **Integration**: Works seamlessly with git-manage for pre-commit validation

**TDD Workflow:**

1. **Red**: Write a failing test
2. **Green**: Write minimal code to pass the test
3. **Refactor**: Improve code while keeping tests passing

**Usage:**

Automatically enforced during development when ``dev-team`` skill is active. Also integrates with ``git-manage`` pre-commit checks.

**Quality Standards:**

- All features must have tests written first
- Test coverage must be maintained at ≥90%
- All tests must pass before commits
- No implementation without corresponding tests

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

Skill Structure
---------------

Each skill follows this structure::

    .iflow/skills/
    ├── skill-name/
    │   ├── SKILL.md              # Main skill definition
    │   ├── agents/               # Agent definitions (if applicable)
    │   ├── workflows/            # Workflow documentation
    │   └── .state/               # State management
    │       └── .gitkeep          # Placeholder directory

Skill Components
----------------

SKILL.md
~~~~~~~~
The main skill definition file containing:
- Skill name and version
- Description and purpose
- Usage instructions
- Workflow phases
- Integration with other skills

agents/
~~~~~~~
Directory containing agent definitions for team-based skills:
- Agent roles and responsibilities
- Agent capabilities and specializations
- Interaction protocols

workflows/
~~~~~~~~~~
Directory containing workflow documentation:
- Phase-by-phase workflows
- Process definitions
- Best practices

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
   - Skill metadata (name, version, description)
   - Usage instructions
   - Workflow documentation
3. Create additional directories as needed (agents/, workflows/, .state/)
4. Define trigger conditions and integration points
5. Document quality standards and best practices

Trigger Conditions
------------------

Skills can be triggered by:
- Keywords in user requests
- Specific commands (e.g., ``/git-manage commit``)
- Context detection (e.g., existing project state)
- Explicit skill activation

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
    /git-manage status
    /git-manage commit feat: add user authentication

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

    # evaluator can use:
    # - git-manage to check recent commits
    # - tdd-enforce to validate test coverage
    # - dev-team to fix discovered issues

**Best Practices:**

- Use conventional commit messages with git-manage
- Follow TDD workflow enforced by tdd-enforce
- Leverage dev-team for complex, multi-phase projects
- Use evaluator for systematic project testing and evaluation
- Check skill status before committing changes

License
-------

See LICENSE file in the project root.
