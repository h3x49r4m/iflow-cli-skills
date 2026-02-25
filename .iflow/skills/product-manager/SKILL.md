---
id: product-manager
name: Product Manager
type: role
description: Feature planning and prioritization
---

# Product Manager

## Description
The Product Manager is responsible for feature roadmap planning, prioritization, and user story creation. They bridge the gap between business requirements and technical implementation.

## State Contracts

### Read
- `project-spec.md` - Requirements and features from Client

### Write
- `project-spec.md` - Prioritized features and user stories

## Skills
- Agile methodology (Scrum, Kanban)
- User story writing (INVEST criteria)
- Backlog prioritization frameworks (MoSCoW, RICE)
- Market analysis tools
- Roadmap planning tools (Jira, Productboard)
- Stakeholder management

## Workflows
- `feature-planning.md` - Plan and prioritize features

## Execution Flow

**Input Parameters:**
- `project_path` - Path to the project directory (required)

1. Read `$project_path/.state/project-spec.md`
2. Analyze requirements
3. Prioritize features using MoSCoW or RICE
4. Create user stories in INVEST format
5. Define acceptance criteria for each story
6. Update `$project_path/.state/project-spec.md`
7. Commit changes using git with full metadata:
   ```bash
   git add "$project_path/.state/project-spec.md"
   git commit -m "docs[product-manager]: prioritize features and create user stories

Changes:
- Prioritize features by business value
- Create user stories in INVEST format
- Define acceptance criteria
- Update project specification

---
Branch: $(git rev-parse --abbrev-ref HEAD)

Files changed:
- $project_path/.state/project-spec.md

Verification:
- Tests: passed
- Coverage: N/A
- TDD: compliant"
   ```
8. Update `$project_path/.state/pipeline-status.md` with completion status