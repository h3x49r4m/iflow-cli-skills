# Nova

A comprehensive iFlow CLI skills ecosystem for software development team orchestration with gate-based workflows, version management, and role-based collaboration.

## Overview

Nova provides a complete development team simulation with 11 role-based skills, 4 pipeline orchestrators, git management, and workflow orchestration. Each role has specific responsibilities, skills, and workflows, all sharing a common state directory for seamless collaboration.

## Skills

### Core Infrastructure Skills

1. **git-manage** - Standardized git operations with safety checks and best practices
   - Conventional commits with LLM integration
   - Pre-commit validation (tests, coverage, secrets detection)
   - Branch operations and stash management
   - Formatted commit messages with verification sections

2. **git-flow** - Gate-based workflow orchestration
   - Role-based branching with auto-creation
   - Review/approval gates with reversible approvals
   - Phase tracking with auto-transitions
   - Dependency management and cascade logic
   - Version management with migration support

### Role-Based Skills (11)

3. **Client** - Requirements provider and stakeholder
4. **Product Manager** - Feature planning and prioritization
5. **Project Manager** - Sprint planning and resource allocation
6. **UI/UX Designer** - Design creation and user experience
7. **Tech Lead** - Architecture design and technical strategy
8. **Software Engineer** - Full-stack implementation (v1.0.0: backend/frontend, v2.0.0: +ML/graphics/data)
9. **Testing Engineer** - Test automation and frameworks
10. **QA Engineer** - Quality validation and manual testing
11. **DevOps Engineer** - CI/CD and infrastructure
12. **Security Engineer** - Security validation and scanning
13. **Documentation Specialist** - Documentation creation

### Pipeline Orchestrators (4)

14. **team-pipeline-new-project** - Full end-to-end pipeline for new projects
15. **team-pipeline-new-feature** - Streamlined pipeline for adding features
16. **team-pipeline-fix-bug** - Focused pipeline for bug fixes
17. **team-pipeline-auto-review** - Automated code review pipeline for PRs and commits

## Architecture

```
.iflow/skills/
├── .shared-state/              # Shared state for all skills
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
├── git-manage/                 # Git operations
│   ├── SKILL.md
│   ├── config.json
│   ├── git-manage.py
│   └── workflows/
├── git-flow/                   # Workflow orchestration
│   ├── SKILL.md
│   ├── config.json
│   ├── git-flow.py
│   ├── pipeline_manager.py      # Version management
│   ├── workflow-state.json
│   ├── branch-states.json
│   └── versions/                # Pipeline versions
│       ├── 1.0.0/
│       │   ├── config.json
│       │   ├── schema.json
│       │   └── migrations/
│       └── 2.0.0/
├── skill_manager.py            # Skill version management
├── skill_cli.py                # Skill management CLI
├── {role}/                     # Each role skill
│   ├── SKILL.md
│   ├── config.json             # Skill version config
│   ├── versions/               # Skill versions
│   │   ├── 1.0.0/
│   │   │   ├── capabilities.json
│   │   │   └── migrations/
│   │   └── 2.0.0/
│   │       ├── capabilities.json
│   │       ├── breaking_changes.json
│   │       └── migrations/
│   └── workflows/
└── {pipeline}/                 # Each pipeline orchestrator
    ├── SKILL.md
    ├── config.json
    └── .state/                  # Symlink to .shared-state/
```

## Usage

### Git Management

```bash
# Commit with LLM integration
/git-manage commit <files>
/git-manage commit <files> --type feat --scope auth --description "add JWT auth"

# View status and changes
/git-manage status
/git-manage diff
/git-manage diff staged

# Branch operations
/git-manage branch create <name>
/git-manage branch switch <name>
/git-manage branch delete <name>
```

### Git-Flow Workflow

```bash
# Start a new workflow
/git-flow start "User Authentication"

# Commit changes (auto-creates role-based branch)
/git-flow commit src/auth.py

# Review dashboard
/git-flow review

# Approve and merge
/git-flow approve tech-lead/auth-architecture --comment "Great design"
/git-flow approve software-engineer/auth-api

# Unapprove and rollback
/git-flow unapprove tech-lead/auth-architecture --cascade

# View workflow status
/git-flow status
/git-flow phase next
/git-flow history
```

### Pipeline Updates

```bash
# Check for updates
/git-flow check-updates

# Update pipeline
/git-flow update [--to version] [--dry-run]

# Rollback
/git-flow rollback --to version [--backup id]

# List versions and backups
/git-flow versions
/git-flow backups [--delete id] [--cleanup N]
```

### Skill Management

```bash
# List all skills
python3 .iflow/skills/skill_cli.py list

# View skill details
python3 .iflow/skills/skill_cli.py info software-engineer

# List skill versions
python3 .iflow/skills/skill_cli.py versions software-engineer

# Check for updates
python3 .iflow/skills/skill_cli.py check-updates

# Find skills by capability
python3 .iflow/skills/skill_cli.py find ml

# Check compatibility
python3 .iflow/skills/skill_cli.py check-compatibility team-pipeline-new-feature

# Validate workflow state
python3 .iflow/skills/skill_cli.py validate-state <state-file>
```

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

## Version Management

### Pipeline Versioning

Pipelines use semantic versioning with automatic migration support:

**Features:**
- Semantic versioning (major.minor.patch)
- Automatic migration path detection
- State validation against schema
- Backup and rollback support
- Dry-run updates

**Version Structure:**
```
.iflow/skills/git-flow/versions/
├── 1.0.0/
│   ├── config.json         # Pipeline configuration
│   ├── schema.json         # State schema
│   └── migrations/         # Migration scripts
└── 2.0.0/
    ├── config.json
    ├── schema.json
    └── migrations/
        └── from_1_0_0.py   # Migration from 1.0.0
```

### Skill Versioning

Skills have versioned capabilities with compatibility tracking:

**Software Engineer Example:**

**v1.0.0 Capabilities:**
- Backend development
- Frontend development
- Basic DevOps

**v2.0.0 Capabilities:**
- Backend development
- Frontend development
- Machine Learning
- 2D/3D Graphics
- Data Science
- Advanced DevOps

**Breaking Changes:**
- ML requires TensorFlow 2.8+
- Graphics requires WebGL 2.0
- Data Science requires Python 3.10+

**Migration:**
```python
# Automatic capability expansion
# Existing workflows continue working
# New ML/graphics/data workflows become available
```

### Compatibility Matrix

Pipelines declare required skill versions:

```json
{
  "pipeline": "team-pipeline-new-feature",
  "version": "1.0.0",
  "skills": {
    "software-engineer": {
      "version": "1.0.0",
      "min_version": "1.0.0",
      "max_version": "1.99.99"
    }
  }
}
```

**Upgrade Modes:**
- **Frozen**: Locked to specific version
- **Compatible**: Auto-update within minor version range
- **Latest**: Always use latest compatible version
- **Manual**: Require explicit approval

## Git-Flow Workflow

### Phases

Default 8-phase workflow:

1. **Requirements Gathering** (Client) - Required
2. **Architecture Design** (Tech Lead) - Required
3. **Implementation** (Software Engineer) - Required
4. **Testing** (QA Engineer) - Required
5. **Design** (UI/UX Designer) - Optional
6. **Documentation** (Documentation Specialist) - Optional
7. **Security Review** (Security Engineer) - Optional
8. **Deployment** (DevOps Engineer) - Required

### Branch Naming Convention

```
{role-slug}/{feature-slug}-{short-id}

Examples:
- tech-lead/memory-system-143022
- software-engineer/user-auth-143145
- qa-engineer/auth-tests-143210
```

### State Machine

**Branch Status:**
```
pending → reviewing → approved → merged
                                    ↓
                               unapproved
                                    ↓
                               reverted → pending
needs_changes → pending
rejected → pending
```

**Phase Status:**
```
pending → active → complete
           ↓
        blocked
```

### Complete Workflow Example

```bash
# Initialize workflow
/git-flow start "User Authentication"

# Phase 1: Requirements Gathering
Client: /git-flow commit requirements.md
You: /git-flow review approve client/requirements-abc123

# Phase 2: Architecture Design
Tech Lead: /git-flow commit architecture.md
You: /git-flow review approve tech-lead/architecture-def456

# Phase 3: Implementation
Software Engineer: /git-flow commit src/auth.py
You: /git-flow review approve software-engineer/implementation-ghi789

# Bug found in Phase 2
You: /git-flow unapprove tech-lead/architecture-def456 --cascade

# Tech Lead fixes
Tech Lead: /git-flow commit architecture.md

# Resume workflow
You: /git-flow review approve tech-lead/architecture-fix-jkl012
```

## State Management

All skills share a common state directory (`.shared-state/`). Each role:

1. **Reads** relevant state documents before starting
2. **Analyzes** context and previous work
3. **Performs** role-specific tasks
4. **Updates** owned documents in shared state
5. **Reports** completion status in `pipeline-status.md`
6. **Commits** changes using git with full metadata format

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
- **Gate-Based Workflows:** Review/approval gates for quality control
- **Role-Based Branching:** Automatic branch creation per role
- **Reversible Approvals:** Full unapproval and rollback support
- **Version Management:** Semantic versioning for pipelines and skills
- **Migration Support:** Automatic state migrations between versions
- **Compatibility Tracking:** Skill-pipeline compatibility matrix
- **Backup & Restore:** Full state backup and rollback capabilities

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
- Architecture: ✓ compliant
- TDD: ✓ compliant
```

## License

See LICENSE file for details.