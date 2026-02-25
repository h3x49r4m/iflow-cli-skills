# Nova

A comprehensive iFlow CLI skills for software development team orchestration.

## Overview

This project provides a complete development team simulation with 11 role-based skills and 4 pipeline orchestrators. Each role has specific responsibilities, skills, and workflows, all sharing a common state directory for seamless collaboration.

## Skills

### Role-Based Skills (11)

1. **Client** - Requirements provider and stakeholder
2. **Product Manager** - Feature planning and prioritization
3. **Project Manager** - Sprint planning and resource allocation
4. **UI/UX Designer** - Design creation and user experience
5. **Tech Lead** - Architecture design and technical strategy
6. **Software Engineer** - Full-stack implementation
7. **Testing Engineer** - Test automation and frameworks
8. **QA Engineer** - Quality validation and manual testing
9. **DevOps Engineer** - CI/CD and infrastructure
10. **Security Engineer** - Security validation and scanning
11. **Documentation Specialist** - Documentation creation

### Pipeline Orchestrators (4)

1. **team-pipeline-new-project** - Full end-to-end pipeline for new projects
2. **team-pipeline-new-feature** - Streamlined pipeline for adding features
3. **team-pipeline-fix-bug** - Focused pipeline for bug fixes
4. **team-pipeline-auto-review** - Automated code review pipeline for PRs and commits

## Architecture

```
.iflow/skills/
├── .shared-state/           # Shared state for all skills
│   ├── project-spec.md
│   ├── design-spec.md
│   ├── architecture-spec.md
│   ├── implementation-plan.md
│   ├── implementation.md
│   ├── test-plan.md
│   ├── test-results.md
│   ├── quality-report.md
│   ├── security-report.md
│   ├── deployment-status.md
│   ├── api-docs.md
│   ├── user-guide.md
│   ├── changelog.md
│   └── pipeline-status.md
├── {role}/                  # Each role skill
│   ├── SKILL.md
│   ├── workflows/
│   └── .state/              # Symlink to .shared-state/
└── {pipeline}/              # Each pipeline orchestrator
    ├── SKILL.md
    ├── config.json
    └── .state/              # Symlink to .shared-state/
```

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

## State Management

All skills share a common state directory (`.shared-state/`). Each role:

1. **Reads** relevant state documents before starting
2. **Analyzes** context and previous work
3. **Performs** role-specific tasks
4. **Updates** owned documents in shared state
5. **Reports** completion status in `pipeline-status.md`
6. **Commits** changes using git with full metadata format

## Documentation

- `docs/roles.md` - Role definitions and responsibilities
- `docs/skills.md` - Detailed skills for each role
- `docs/iflow_skills_design.md` - Complete architecture and design documentation
- `docs/team_flow.md` - Visual team flow diagram

## Pipelines

### New Project Pipeline

Executes all 11 roles sequentially to deliver a complete, production-ready application.

**Stages:**
1. client → 2. product-manager → 3. project-manager → 4. ui-ux-designer → 5. tech-lead → 6. software-engineer → 7. testing-engineer → 8. qa-engineer → 9. devops-engineer → 10. security-engineer → 11. documentation-specialist

### New Feature Pipeline

Streamlined pipeline for adding features to existing projects.

**Stages:** Same as new project, but with context from existing state and optional stages.

### Bug Fix Pipeline

Focused pipeline for rapid bug fixing.

**Stages:**
1. client (optional) → 2. tech-lead → 3. software-engineer → 4. testing-engineer → 5. qa-engineer → 6. devops-engineer (if critical) → 7. documentation-specialist (if needed)

### Auto Review Pipeline

Automated code review pipeline for comprehensive quality checks.

**Stages (Parallel Execution):**
1. code-analysis → 2. security-scan → 3. test-suite → 4. tdd-compliance → 5. code-quality → 6. architecture-review → 7. documentation-check

**Quality Gates:**
- Test coverage ≥ 80%
- Zero critical security vulnerabilities
- Code complexity ≤ 10
- TDD compliance ≥ 90%
- Zero test failures

## Key Features

- **Single Source of Truth:** All state in one directory
- **Independent Roles:** Roles can work alone or in pipelines
- **State Persistence:** State survives across sessions
- **Easy Resumption:** Resume from any stage
- **Clear Ownership:** Each document has an owner
- **Traceability:** Full audit trail via state documents
- **Flexibility:** Mix single-role and pipeline workflows
- **Consistency:** State contracts ensure consistency
- **Scalability:** Easy to add new roles or pipelines
- **Automated Commits:** Full git metadata in every commit

## Commit Format

All commits use the git-manage format with full metadata:

```
<type>[<scope>]: <description>

Changes:
- <change 1>
- <change 2>

---
Branch: <branch-name>

Files changed:
- <file1>
- <file2>

Verification:
- Tests: passed/skipped/N/A
- Coverage: <percentage>%/N/A
- TDD: compliant
```

## License

See LICENSE file for details.
