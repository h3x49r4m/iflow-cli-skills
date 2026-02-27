# Nova

A comprehensive skills-based development system for iFlow CLI that orchestrates team workflows through role-based skills, shared state management, and versioned capabilities.

## Overview

iFlow CLI Skills provides a structured development team of 12 role-based skills and 3 pipeline orchestrators that collaborate through a shared state directory. Each role has defined responsibilities, state contracts, and workflows that enable seamless collaboration in software development projects.

## Features

- **12 Role-Based Skills**: Client, Product Manager, Project Manager, UI/UX Designer, Tech Lead, Software Engineer, Testing Engineer, QA Engineer, DevOps Engineer, Security Engineer, Documentation Specialist, and Git Flow orchestrator
- **3 Pipeline Orchestrators**: New Project, New Feature, and Bug Fix pipelines
- **Shared State Management**: Single source of truth with 14 state documents
- **Version Management**: Semantic versioning for skills with capability tracking and compatibility checking
- **Git Flow Integration**: Gate-based workflow orchestration with role-based branching, review/approval gates, phase tracking, and reversible approvals
- **State-First Approach**: Every role reads state, performs work, and updates state

## Architecture

```
.iflow/
├── skills/                          # All skills and pipelines
│   ├── client/                      # Role: Requirements provider
│   ├── product-manager/             # Role: Feature planning
│   ├── project-manager/             # Role: Sprint planning
│   ├── ui-ux-designer/              # Role: Design creation
│   ├── tech-lead/                   # Role: Architecture design
│   ├── software-engineer/           # Role: Full-stack implementation
│   ├── testing-engineer/            # Role: Test automation
│   ├── qa-engineer/                 # Role: Quality validation
│   ├── devops-engineer/             # Role: CI/CD and infrastructure
│   ├── security-engineer/           # Role: Security validation
│   ├── documentation-specialist/    # Role: Documentation creation
│   ├── git-flow/                    # Workflow orchestration
│   ├── git-manage/                  # Git operations
│   ├── team-pipeline-new-project/   # Pipeline: New projects
│   ├── team-pipeline-new-feature/   # Pipeline: New features
│   ├── team-pipeline-fix-bug/       # Pipeline: Bug fixes
│   ├── team-pipeline-auto-review/   # Pipeline: Code review
│   └── .shared-state/               # Shared state directory
│       ├── project-spec.md
│       ├── design-spec.md
│       ├── architecture-spec.md
│       ├── implementation-plan.md
│       ├── implementation.md
│       ├── test-plan.md
│       ├── test-results.md
│       ├── quality-report.md
│       ├── security-report.md
│       ├── deployment-status.md
│       ├── api-docs.md
│       ├── user-guide.md
│       ├── changelog.md
│       └── pipeline-status.md
└── skill_manager.py                 # Version management system
```

## Roles

### Stakeholder Layer

- **Client** - Requirements provider and acceptance criteria definition

### Product & Planning

- **Product Manager** - Feature roadmap planning, prioritization, and user story creation
- **Project Manager** - Sprint planning, timeline tracking, and resource allocation

### Design

- **UI/UX Designer** - Wireframe creation, prototypes, and visual design systems

### Technical Leadership

- **Tech Lead** - System architecture decisions, code standards, and technical strategy

### Engineering

- **Software Engineer** - Full-stack implementation, API design, and database schema design

### Quality & Operations

- **Testing Engineer** - Unit and integration test development, test automation, and TDD practices
- **QA Engineer** - Manual testing execution, test case creation, and UAT
- **DevOps Engineer** - CI/CD pipeline design, container orchestration, and cloud infrastructure
- **Security Engineer** - Code security reviews, vulnerability scanning, and security best practices
- **Documentation Specialist** - API documentation, user guides, and technical documentation

### Workflow Orchestration

- **Git Flow** - Gate-based workflow orchestration with role-based branching, review/approval gates, phase tracking, and reversible approvals
- **Git Manage** - Standardized git operations with safety checks and best practices

## Pipelines

### New Project Pipeline
Full end-to-end pipeline for creating new projects from scratch. Executes all 11 roles sequentially to deliver a complete, production-ready application.

### New Feature Pipeline
Streamlined pipeline for adding features to existing projects. Optimized sequence for feature development cycles.

### Bug Fix Pipeline
Focused pipeline for fixing bugs. Rapid cycle for critical fixes and hotfixes.

### Auto Review Pipeline
Automated code review pipeline for pull requests and commits.

## Version Management

The skill version management system provides:

- **Semantic Versioning**: Track skill versions with major, minor, and patch releases
- **Capability Tracking**: Define and track capabilities for each skill version
- **Compatibility Checking**: Verify skill compatibility with pipeline requirements
- **Dependency Resolution**: Resolve skill version requirements and dependencies
- **Breaking Change Tracking**: Track breaking changes between versions
- **Upgrade Path Planning**: Suggest upgrade paths between versions

### Skill Structure

Each skill can have versioned capabilities:

```
.iflow/skills/{skill}/
├── SKILL.md                    # Skill definition
├── config.json                 # Current version configuration
├── versions/                   # Versioned capabilities
│   ├── 1.0.0/
│   │   ├── capabilities.json   # Version 1.0.0 capabilities
│   │   └── schema.json         # Version 1.0.0 schema
│   └── 2.0.0/
│       ├── capabilities.json   # Version 2.0.0 capabilities
│       ├── breaking_changes.json # Breaking changes
│       └── migrations/
│           └── from_1_0_0.py   # Migration from 1.0.0
└── workflows/                  # Skill workflows
    └── {workflow}.md
```

## Git Flow

Git Flow provides gate-based workflow orchestration with:

- **Role-Based Branching**: Automatic branch naming based on role (e.g., `tech-lead/feature-abc123`)
- **Review/Approval Gates**: Branch must be reviewed and approved before merging
- **Phase Tracking**: Track workflow phases (Requirements, Architecture, Implementation, Testing, etc.)
- **Reversible Approvals**: Unapprove branches with cascade reversion of dependent branches
- **State Persistence**: Workflow state persisted across sessions

### Git Flow Commands

```bash
/git-flow start <feature-name>          # Initialize workflow
/git-flow commit [files...]             # Commit changes
/git-flow review                        # Show pending reviews
/git-flow approve <branch>              # Approve and merge branch
/git-flow reject <branch> --reason "..." # Reject branch
/git-flow request-changes <branch>      # Request modifications
/git-flow unapprove <branch>            # Unapprove branch
/git-flow status                        # Show workflow status
/git-flow phase-next                    # Advance to next phase
/git-flow history                       # Show review history
```

## State Documents

| Document | Owner | Purpose |
|----------|-------|---------|
| project-spec.md | Product Manager | Project requirements, features, acceptance criteria |
| design-spec.md | UI/UX Designer | UI/UX designs, wireframes, prototypes |
| architecture-spec.md | Tech Lead | System architecture, tech stack, patterns |
| implementation-plan.md | Project Manager | Task breakdown, timeline, resource allocation |
| implementation.md | Software Engineer | Full-stack implementation details |
| test-plan.md | Testing Engineer | Test strategy, test cases, automation plan |
| test-results.md | Testing Engineer | Test execution results, coverage reports |
| quality-report.md | QA Engineer | Quality validation, bug reports, UAT results |
| security-report.md | Security Engineer | Security analysis, vulnerability scan results |
| deployment-status.md | DevOps Engineer | Deployment history, environment status |
| api-docs.md | Documentation Specialist | API documentation, endpoints, schemas |
| user-guide.md | Documentation Specialist | User documentation, tutorials, guides |
| changelog.md | Documentation Specialist | Change history, version notes |
| pipeline-status.md | Orchestrator | Pipeline progress, stage status |

## Usage

### Single Role Activation

Activate a single role to work independently:

```bash
iflow skill client
iflow skill tech-lead
iflow skill software-engineer
```

### Pipeline Execution

Activate a pipeline to orchestrate multiple roles:

```bash
iflow skill team-pipeline-new-project
iflow skill team-pipeline-new-feature
iflow skill team-pipeline-fix-bug
iflow skill team-pipeline-auto-review
```

### Git Flow Workflow

```bash
# Initialize workflow
/git-flow start "User Authentication"

# Commit changes (auto-creates branch if on main)
/git-flow commit requirements.md

# Review and approve branches
/git-flow review
/git-flow approve client/requirements-abc123

# Continue through phases
/git-flow phase-next
```

## Documentation

- [Design Document](docs/iflow_skills_design.md) - Complete architecture and design specification
- [Roles](docs/roles.md) - Detailed role definitions and responsibilities
- [Skills](docs/skills.md) - Specific skills for each role
- [Team Flow](docs/team_flow.md) - Visual representation of team structure and workflow

## License

Apache License 2.0 - see [LICENSE](LICENSE) for details.
