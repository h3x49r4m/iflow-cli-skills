iFlow CLI Skills
============================

A collection of custom skills for iFlow CLI.

Skills are modular components that extend iFlow CLI's capabilities for specific development workflows.

About
-----

This repository contains reusable skills that can be loaded into iFlow CLI to assist with various development tasks.

Skills are organized in the ``.iflow/skills/`` directory.

Skills Directory Structure
--------------------------

Each skill is organized as follows::

    .iflow/skills/
    ├── skill-name/
    │   ├── skill.md              # Main skill definition
    │   ├── 01-phase-name/        # Lifecycle phase directories
    │   ├── template/             # Project scaffolding templates
    │   ├── trackers/             # Progress tracking templates
    │   └── .state/               # State management (for continuous development)
    │       ├── checkpoints/      # Phase-specific checkpoints
    │       └── context/          # Context and decision tracking

Skill Components
----------------

skill.md
~~~~~~~~
The main skill definition file containing:
- Skill name and description
- Trigger conditions (when the skill should be invoked)
- Workflow phases
- Instructions for new and existing projects
- Resume commands
- Alignment commands for non-standard projects

Phase Directories (00-phase-name/, 01-phase-name/)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Each phase contains guidance and instructions for that phase:
- **00-assessment**: Project analysis, compliance checking, gap analysis
- 01-planning: Feature breakdown and planning
- 02-architecture: Architecture design
- 03-development: Development workflows
- 04-testing: Testing strategies
- 05-quality-assurance: Quality assurance procedures
- 06-deployment: Deployment processes

template/
~~~~~~~~~
Contains scaffolding templates for new projects:
- Configuration files (pyproject.toml, .gitignore, etc.)
- Documentation templates (README.md, FEATURES.md, etc.)
- Source code structure (src/, tests/)
- Initial test files and fixtures

trackers/
~~~~~~~~~
Progress tracking templates:
- Feature tracker
- Test coverage tracker
- Bug tracker
- Alignment tracker (for non-standard projects)

.state/
~~~~~~~
State management for continuous development:

checkpoints/
~~~~~~~~~~~~
Phase-specific checkpoints:
- Assessment checkpoint
- Migration planning checkpoint
- Migration execution checkpoint
- Planning checkpoint
- Architecture checkpoint
- Development checkpoint
- Testing checkpoint
- QA checkpoint
- Deployment checkpoint
- Change request checkpoint
- Change impact checkpoint
- Change implementation checkpoint

context/
~~~~~~~~
Context and decision tracking:
- Project state
- Current feature
- Completed checklist
- Next steps
- Session handoff
- Decisions log
- Change log
- Impact analysis
- Rollback plan

Available Skills
----------------

python-project-builder-tdd
~~~~~~~~~~~~~~~~~~~~~~~~~~~
A comprehensive skill for building Python projects following Test-Driven Development (TDD) methodology. Covers the full project lifecycle from product design to deployment using uv for package management.

**Workflow Phases:**

0. **Assessment** - Project analysis, compliance check, gap identification
1. **Planning** - Feature breakdown, dependency mapping, effort estimation
2. **Architecture** - Module design, interface design, data flow
3. **Development** - TDD workflow, feature implementation, code standards
4. **Testing** - Test strategy, coverage requirements, edge cases
5. **Quality Assurance** - Feature verification, integration checks, performance validation
6. **Deployment** - Build process, deployment strategies

**Project Setup:**
- Use ``uv`` for package management
- Standard structure: ``src/`` for source code, ``tests/`` for tests
- Use ``pytest`` as the testing framework
- Follow TDD: Write tests first, then implement

**Key Commands:**
- ``uv init`` - Initialize project
- ``uv add pytest`` - Add pytest dependency
- ``uv run pytest`` - Run tests
- ``uv run pytest --cov`` - Run tests with coverage
- ``uv build`` - Build project

**Quality Standards:**
- Minimum 80% test coverage per feature
- All features must pass acceptance criteria
- Integration tests required for feature interactions
- Edge cases must be identified and tested

**Trigger Conditions:**
- User requests to develop a Python application, library, or tool
- User asks to create a Python project
- User requests Python development with testing requirements
- User asks to "continue", "resume", or "continue working on" a project
- User requests a change: "change", "modify", "update", "requirement change", "feature change"
- User requests project alignment: "align project", "fix project structure", "improve code quality", "migrate project"
- Keywords: "python", "develop", "create project", "build app", "tdd", "test-driven", "continue", "resume", "change", "modify", "update", "align", "compliance", "standards", "refactor", "migrate"

**Alignment Capabilities:**

For existing projects that don't follow TDD standards, the skill provides:

- **Project Analysis**: Comprehensive assessment of structure, tools, and practices
- **Compliance Check**: Verification against TDD standards with scoring (0-100)
- **Gap Analysis**: Identification of deviations with prioritization (P0-P3)
- **Migration Planning**: Phased alignment approach with effort estimates
- **Incremental Execution**: Gradual alignment without disrupting ongoing work

**Alignment Types:**

- **Structural Alignment**: Fix directory structure (src/, tests/ organization)
- **Testing Alignment**: Add pytest, reorganize tests, achieve 80% coverage
- **Standards Alignment**: Apply PEP 8, type hints, docstrings
- **Tooling Alignment**: Integrate ruff, black, mypy, pre-commit hooks
- **Process Alignment**: Adopt TDD workflow for new features
- **State Management Alignment**: Set up tracking and change management

**Usage Example:**

To create a new Python project:

.. code-block:: text

    User: I want to create a Python web application with TDD

To continue working on an existing project:

.. code-block:: text

    User: Continue working on my project
    User: Resume feature X
    User: What's next?

To align an existing non-standard project:

.. code-block:: text

    User: Analyze my Python project
    User: Show gaps in my project
    User: Align my project with TDD standards
    User: Check compliance status

rst-writer
~~~~~~~~~~
A skill for writing articles in reStructuredText (RST) format with 100% syntax accuracy.

**RST Syntax Support:**

- **Section Headers**: Proper underlines/overlines with matching characters
- **Text Formatting**: Italic, bold, monospace, emphasis, strong
- **Lists**: Bullet, enumerated, and definition lists
- **Code Blocks**: Literal blocks and code-block directives
- **Tables**: Simple and grid tables
- **Links and References**: External links, internal references, hyperlink targets
- **Directives**: Notes, warnings, tips, includes, images
- **Comments**: Inline and block comments
- **Other**: Line blocks, field lists, substitutions, footnotes, citations

**Validation Checklist:**

- Section headers have matching underline/overline lengths
- Header hierarchy uses distinct characters consistently
- Code blocks use proper indentation (3 spaces minimum)
- Lists use consistent indentation
- Tables have proper column alignment
- Links use correct syntax
- Inline markup doesn't span multiple lines
- All directives end with double colon and proper indentation
- No unescaped special characters in text
- Blank lines before and after directives/code blocks

**Quality Standards:**
- 100% RST syntax accuracy
- Proper header hierarchy
- Correct indentation for all blocks
- Valid directive syntax
- Proper table formatting
- Correct link/reference syntax

**Trigger Conditions:**
- User requests to write an article in RST format
- User asks to create RST documentation
- User requests reStructuredText content generation
- Keywords: "rst", "restructuredtext", "write article", "create documentation", ".rst file"

**Resume Commands:**
- "continue writing" - Resume current article
- "what's next?" - Show next steps
- "validate rst" - Validate current RST content

**Usage Example:**

To write an article in RST format:

.. code-block:: text

    User: Write an article about Python best practices in RST format

To resume writing:

.. code-block:: text

    User: Continue writing
    User: What's next?

To validate RST syntax:

.. code-block:: text

    User: Validate my RST content

Creating a New Skill
--------------------

1. Create a new directory in ``.iflow/skills/``
2. Create a ``skill.md`` file with:
   - Skill name
   - Description
   - Trigger conditions
   - Workflow instructions
3. Create phase directories (optional)
4. Create template files (optional)
5. Create tracker files (optional)
6. Create state management structure (optional for continuous development)

Trigger Conditions
------------------

Skills can be triggered by:
- Keywords in user requests (e.g., "python", "develop", "create project")
- Specific commands (e.g., "continue", "resume")
- Context detection (e.g., existing project state)

Continuous Development Support
-------------------------------

Skills support continuous development through:
- State persistence in ``.state/`` directory
- Checkpoint system for resuming work
- Session handoff protocol
- Change management and tracking
- Progress visualization

Change Management
-----------------

Skills can handle requirement/feature changes through:
- Change request tracking
- Impact analysis
- Rollback planning
- Change implementation checkpoints
- Integration with existing workflows

Project Alignment for Non-Standard Projects
--------------------------------------------

Skills that support alignment can help existing projects conform to standards:

**Alignment Process:**

1. **Assessment**: Analyze project structure, tools, and practices
2. **Compliance Check**: Verify alignment with standards (score 0-100)
3. **Gap Analysis**: Identify deviations with priorities (P0-P3)
4. **Migration Planning**: Create phased alignment plan
5. **Incremental Execution**: Apply changes without disrupting work

**Alignment Commands:**

- ``analyze project`` - Assess current project state
- ``show gaps`` - Display compliance gaps with priorities
- ``check compliance`` - Verify current alignment status
- ``migration plan`` - Show/modify migration plan
- ``migration status`` - Show alignment progress
- ``migrate [component]`` - Align specific component

**Compliance Levels:**

- **Fully Compliant (90-100)**: Project meets all standards
- **Mostly Compliant (70-89)**: Minor gaps, can continue development
- **Partially Compliant (50-69)**: Significant gaps, alignment needed
- **Non-Compliant (0-49)**: Major gaps, alignment required before development

**Alignment Phases:**

- **Phase 0**: Assessment (1 day)
- **Phase 1**: Critical Foundation (1 week) - Basic infrastructure
- **Phase 2**: High Priority Alignment (1 week) - Critical practices
- **Phase 3**: Medium Priority Alignment (2 weeks) - Complete standards
- **Phase 4**: Low Priority Improvements (Ongoing) - Nice-to-have

Usage
-----

How to Use Skills in iFlow CLI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Skills are automatically loaded and triggered based on their defined conditions. Here's how to use them:

**Automatic Loading**

Skills are automatically loaded when:
1. Placed in the ``.iflow/skills/`` directory
2. iFlow CLI scans the skills directory
3. User requests match trigger conditions

**Triggering a Skill**

Skills are triggered automatically when your request matches their trigger conditions. For example:

.. code-block:: text

    # Trigger the python-project-builder-tdd skill
    User: I want to create a Python application
    User: Develop a Python tool with TDD
    User: Build a Python web API

**Resuming Work**

For skills that support continuous development, you can resume work:

.. code-block:: text

    # Resume working on a project
    User: Continue working on my project
    User: Resume feature authentication
    User: What's next?

**Change Management**

For skills with change management support:

.. code-block:: text

    # Request a change
    User: Change the user authentication flow
    User: Update feature X to use OAuth

    # Check impact
    User: What's the impact of this change?

    # Rollback if needed
    User: Rollback the last change

**Listing Available Skills**

To see what skills are available:

.. code-block:: text

    User: Show available skills
    User: List all skills

**Skill-Specific Commands**

Each skill may have specific commands. Refer to the skill's documentation for details.

**Testing a Skill**

To test a skill:
- Use trigger keywords in your requests
- Verify the skill activates correctly
- Check that it follows the defined workflow

**Example Workflow**

Here's a complete example of using the ``python-project-builder-tdd`` skill:

1. **Start a new project:**

   .. code-block:: text

       User: I want to create a Python REST API with TDD

   The skill will:
   - Initialize the project structure
   - Set up uv and pytest
   - Begin the planning phase

2. **Continue development:**

   .. code-block:: text

       User: Continue working on my project

   The skill will:
   - Load the current state
   - Show next steps
   - Resume from where you left off

3. **Handle changes:**

   .. code-block:: text

       User: Change the database from SQLite to PostgreSQL

   The skill will:
   - Analyze the impact
   - Update the architecture
   - Adjust the implementation plan

4. **Align an existing non-standard project:**

   .. code-block:: text

       User: Analyze my Python project

   The skill will:
   - Analyze project structure and tools
   - Check compliance with TDD standards
   - Generate compliance score (e.g., 45/100)

   .. code-block:: text

       User: Show gaps in my project

   The skill will:
   - Display identified gaps with priorities
   - Show impact and effort estimates
   - Recommend migration plan

   .. code-block:: text

       User: Align my project with TDD standards

   The skill will:
   - Create migration plan with phases
   - Execute alignment incrementally
   - Track progress without disrupting work

Best Practices
--------------

- Keep skill definitions clear and concise
- Use descriptive trigger conditions
- Document phase instructions thoroughly
- Include quality standards
- Support continuous development with state management
- Handle changes gracefully with change management
- Provide clear resume instructions

License
-------

See LICENSE file in the project root.