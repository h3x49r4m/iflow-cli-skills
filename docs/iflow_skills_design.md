# iFlow Skills Design Document

## Overview

This document defines the architecture and design for the iFlow CLI skills-based development team. The system consists of 12 role-based skills and 3 pipeline orchestrators, all sharing a common state directory for seamless collaboration.

## Architecture

### Level 1: iFlow CLI Structure

```
.iflow/                              # iFlow CLI root
├── skills/                          # All skills (roles + pipelines)
│   ├── client/                      # Role skill
│   ├── product-manager/             # Role skill
│   ├── project-manager/             # Role skill
│   ├── ui-ux-designer/              # Role skill
│   ├── tech-lead/                   # Role skill
│   ├── software-engineer/           # Role skill
│   ├── testing-engineer/            # Role skill
│   ├── qa-engineer/                 # Role skill
│   ├── devops-engineer/             # Role skill
│   ├── security-engineer/           # Role skill
│   ├── documentation-specialist/    # Role skill
│   ├── team-pipeline-new-project/   # Pipeline orchestrator
│   ├── team-pipeline-new-feature/   # Pipeline orchestrator
│   └── team-pipeline-fix-bug/       # Pipeline orchestrator
│
└── .shared-state/                   # Shared state directory
    ├── project-spec.md
    ├── design-spec.md
    ├── architecture-spec.md
    ├── implementation-plan.md
    ├── implementation.md
    ├── test-plan.md
    ├── test-results.md
    ├── quality-report.md
    ├── security-report.md
    ├── deployment-status.md
    ├── api-docs.md
    ├── user-guide.md
    ├── changelog.md
    └── pipeline-status.md
```

### Level 2: Role Skill Structure

```
.iflow/skills/{role}/
├── SKILL.md                          # Role definition + state contracts
├── workflows/                        # Role workflows
│   └── {workflow-name}.md
└── .state/                           # Symlink to .iflow/.shared-state/
```

### Level 3: Pipeline Orchestrator Structure

```
.iflow/skills/{pipeline}/
├── SKILL.md                          # Pipeline definition
├── config.json                       # Pipeline configuration (role sequence)
└── .state/                           # Symlink to .iflow/.shared-state/
```

## Roles

### 1. Client
- **Owner:** project-spec.md (contributor)
- **Reads:** None (first role)
- **Writes:** project-spec.md
- **Purpose:** Define requirements and acceptance criteria

### 2. Product Manager
- **Owner:** project-spec.md
- **Reads:** project-spec.md
- **Writes:** project-spec.md
- **Purpose:** Prioritize features and create user stories

### 3. Project Manager
- **Owner:** implementation-plan.md
- **Reads:** project-spec.md
- **Writes:** implementation-plan.md, project-spec.md
- **Purpose:** Plan sprints and allocate resources

### 4. UI/UX Designer
- **Owner:** design-spec.md
- **Reads:** project-spec.md
- **Writes:** design-spec.md
- **Purpose:** Create wireframes and prototypes

### 5. Tech Lead
- **Owner:** architecture-spec.md
- **Reads:** project-spec.md, design-spec.md
- **Writes:** architecture-spec.md
- **Purpose:** Define system architecture and tech stack

### 6. Software Engineer
- **Owner:** implementation.md, api-docs.md
- **Reads:** design-spec.md, architecture-spec.md, implementation-plan.md
- **Writes:** implementation.md, api-docs.md
- **Purpose:** Implement full-stack features

### 7. Testing Engineer
- **Owner:** test-plan.md, test-results.md
- **Reads:** implementation.md, implementation-plan.md
- **Writes:** test-plan.md, test-results.md
- **Purpose:** Write automated tests and test frameworks

### 8. QA Engineer
- **Owner:** quality-report.md
- **Reads:** test-plan.md, test-results.md, project-spec.md
- **Writes:** quality-report.md, test-results.md (contributor)
- **Purpose:** Validate quality and perform manual testing

### 9. DevOps Engineer
- **Owner:** deployment-status.md
- **Reads:** architecture-spec.md, implementation.md
- **Writes:** deployment-status.md
- **Purpose:** Set up CI/CD and manage deployments

### 10. Security Engineer
- **Owner:** security-report.md
- **Reads:** All implementation documents
- **Writes:** security-report.md
- **Purpose:** Validate security and scan for vulnerabilities

### 11. Documentation Specialist
- **Owner:** api-docs.md, user-guide.md, changelog.md
- **Reads:** All state documents
- **Writes:** api-docs.md, user-guide.md, changelog.md
- **Purpose:** Create and maintain documentation

## State Documents

| Document | Owner | Contributors | Purpose |
|----------|-------|--------------|---------|
| project-spec.md | Product Manager | Client, Project Manager | Project requirements, features, acceptance criteria |
| design-spec.md | UI/UX Designer | Software Engineer | UI/UX designs, wireframes, prototypes |
| architecture-spec.md | Tech Lead | Software Engineer, DevOps Engineer | System architecture, tech stack, patterns |
| implementation-plan.md | Project Manager | All Engineers | Task breakdown, timeline, resource allocation |
| implementation.md | Software Engineer | Tech Lead | Full-stack implementation details |
| test-plan.md | Testing Engineer | QA Engineer | Test strategy, test cases, automation plan |
| test-results.md | Testing Engineer | QA Engineer | Test execution results, coverage reports |
| quality-report.md | QA Engineer | All Engineers | Quality validation, bug reports, UAT results |
| security-report.md | Security Engineer | All Engineers | Security analysis, vulnerability scan results |
| deployment-status.md | DevOps Engineer | All Engineers | Deployment history, environment status |
| api-docs.md | Documentation Specialist | Software Engineer | API documentation, endpoints, schemas |
| user-guide.md | Documentation Specialist | Software Engineer | User documentation, tutorials, guides |
| changelog.md | Documentation Specialist | All Engineers | Change history, version notes |
| pipeline-status.md | Orchestrator | All roles (read-only) | Pipeline progress, stage status |

## Pipelines

### New Project Pipeline
Full end-to-end pipeline for creating new projects from scratch.

**Sequence:**
1. client
2. product-manager
3. project-manager
4. ui-ux-designer
5. tech-lead
6. software-engineer
7. testing-engineer
8. qa-engineer
9. devops-engineer
10. security-engineer
11. documentation-specialist

**Duration:** Complete development lifecycle

### New Feature Pipeline
Streamlined pipeline for adding features to existing projects.

**Sequence:**
1. client (optional)
2. product-manager
3. project-manager
4. ui-ux-designer
5. tech-lead
6. software-engineer
7. testing-engineer
8. qa-engineer
9. devops-engineer (if needed)
10. security-engineer
11. documentation-specialist

**Duration:** Feature development cycle

### Bug Fix Pipeline
Focused pipeline for fixing bugs.

**Sequence:**
1. client (optional, if bug reported by client)
2. tech-lead
3. software-engineer
4. testing-engineer
5. qa-engineer
6. devops-engineer (if critical hotfix)
7. documentation-specialist (if needed)

**Duration:** Rapid bug fix cycle

## Usage

### Single Role Activation

Activate a single role to work independently:

```bash
iflow skill client
iflow skill tech-lead
iflow skill software-engineer-frontend
```

**Workflow:**
1. Role reads `.shared-state/` directory
2. Understands context and previous work
3. Performs its work
4. Updates specific documents in `.shared-state/`
5. Updates `pipeline-status.md` with completion status

### Pipeline Execution

Activate a pipeline to orchestrate multiple roles:

```bash
iflow skill team-pipeline-new-project
iflow skill team-pipeline-new-feature
iflow skill team-pipeline-fix-bug
```

**Workflow:**
1. Orchestrator reads `config.json`
2. Executes roles in defined sequence
3. Each role reads state, performs work, updates state
4. Orchestrator tracks progress via `pipeline-status.md`
5. Pipeline completes when all roles finish

### State-First Approach

Every role follows this pattern:

1. **READ STATE:** Read relevant documents from `.shared-state/`
2. **ANALYZE CONTEXT:** Understand previous work, requirements, constraints
3. **PERFORM WORK:** Execute role-specific tasks
4. **UPDATE STATE:** Write updated documents to `.shared-state/`
5. **REPORT STATUS:** Update `pipeline-status.md`

### Forced State Updates

Each role's `SKILL.md` defines:
- **READ contracts:** What documents to read before starting
- **WRITE contracts:** What documents to update after completing
- **Validation:** Rules for state consistency

The role is forced to:
- Always read state first
- Always update owned documents
- Always report completion status

## State Management

### Shared State Directory

`.iflow/.shared-state/` is the single source of truth for all skills.

### State Persistence

- State persists across all pipeline executions
- Roles can resume from any stage
- Historical state is tracked via `pipeline-status.md`

### State Transitions

- Orchestrator validates state between role transitions
- Each role must complete before next role starts
- Failed transitions are logged and can be retried

### Symlinks

Each skill's `.state/` directory is a symlink to `.iflow/.shared-state/`:
- Ensures all skills access the same state
- Simplifies state management
- Maintains backward compatibility

## SKILL.md Format

Each role's `SKILL.md` contains:

```markdown
# {Role Name}

## Description
Role description and responsibilities.

## State Contracts

### Read
- `project-spec.md` - Requirements and features
- `design-spec.md` - UI/UX designs

### Write
- `{owned-document}.md` - Role-specific output

## Skills
- Skill 1
- Skill 2

## Workflows
- `{workflow-name}.md` - Workflow description
```

Each pipeline's `SKILL.md` contains:

```markdown
# {Pipeline Name}

## Description
Pipeline description and purpose.

## Configuration
Defined in `config.json`

## State Contracts

### Read
- `pipeline-status.md` - Current pipeline status

### Write
- `pipeline-status.md` - Updated pipeline status

## Execution
Orchestrates roles in sequence as defined in config.json
```

## config.json Format

Each pipeline's `config.json` contains:

```json
{
  "name": "team-pipeline-new-project",
  "description": "Full pipeline for new projects",
  "roles": [
    "client",
    "product-manager",
    "project-manager",
    "ui-ux-designer",
    "tech-lead",
    "software-engineer-frontend",
    "software-engineer-backend",
    "testing-engineer",
    "qa-engineer",
    "devops-engineer",
    "security-engineer",
    "documentation-specialist"
  ],
  "parallel_stages": [
    ["software-engineer-frontend", "software-engineer-backend"]
  ],
  "approval_gates": [
    {
      "after": "tech-lead",
      "requires": "architecture approval"
    },
    {
      "after": "qa-engineer",
      "requires": "quality approval"
    }
  ]
}
```

## Benefits

1. **Single Source of Truth:** All state in one directory
2. **Independent Roles:** Roles can work alone or in pipelines
3. **State Persistence:** State survives across sessions
4. **Easy Resumption:** Resume from any stage
5. **Clear Ownership:** Each document has an owner
6. **Traceability:** Full audit trail via state documents
7. **Flexibility:** Mix single-role and pipeline workflows
8. **Consistency:** State contracts ensure consistency
9. **Scalability:** Easy to add new roles or pipelines
10. **Collaboration:** Shared state enables cross-role communication

## Implementation Steps

1. Create `.iflow/.shared-state/` directory with all state documents
2. Create 12 role skills with symlinks to shared state
3. Create 3 pipeline orchestrators with symlinks to shared state
4. Define state contracts in each `SKILL.md`
5. Implement workflow files for each role
6. Configure pipeline execution in `config.json`
7. Implement orchestrator logic using Task tool
8. Test single-role activation
9. Test pipeline execution
10. Validate state transitions