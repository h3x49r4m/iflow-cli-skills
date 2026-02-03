iFlow CLI Skills Repository
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

Phase Directories (01-phase-name/)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Each phase contains guidance and instructions for that phase:
- Feature breakdown and planning
- Architecture design
- Development workflows
- Testing strategies
- Quality assurance procedures
- Deployment processes

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

.state/
~~~~~~~
State management for continuous development:

checkpoints/
~~~~~~~~~~~~
Phase-specific checkpoints:
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
A comprehensive skill for building Python projects following Test-Driven Development (TDD) methodology.

**Features:**
- Full project lifecycle support (planning to deployment)
- TDD workflow with pytest
- uv for package management
- Continuous development support
- Change management capabilities
- Quality standards (80%+ test coverage)

**Trigger Conditions:**
- "python", "develop", "create project", "build app", "tdd", "test-driven"
- "continue", "resume", "continue working on"

**Usage Example:**

To create a new Python project:

.. code-block:: text

    User: I want to create a Python web application with TDD

To continue working on an existing project:

.. code-block:: text

    User: Continue working on my project
    User: Resume feature X
    User: What's next?

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

Usage
-----

Skills are automatically loaded when:
1. Placed in the ``.iflow/skills/`` directory
2. iFlow CLI scans the skills directory
3. User requests match trigger conditions

To test a skill:
- Use trigger keywords in your requests
- Verify the skill activates correctly
- Check that it follows the defined workflow

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