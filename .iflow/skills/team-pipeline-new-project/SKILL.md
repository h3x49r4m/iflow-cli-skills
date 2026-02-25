---
id: team-pipeline-new-project
name: Team Pipeline - New Project
type: pipeline
description: Full pipeline for new projects from scratch
---

# Team Pipeline - New Project

## Description
Full end-to-end pipeline for creating new projects from scratch. This orchestrator executes all 12 roles in sequence to deliver a complete, production-ready application.

## Configuration
Defined in `config.json`

## State Contracts

### Read
- `pipeline-status.md` - Current pipeline status

### Write
- `pipeline-status.md` - Updated pipeline status

## Execution
Orchestrates roles in sequence as defined in config.json. Each role reads state, performs work, updates state, commits changes using git-manage, and reports completion. The orchestrator tracks progress and handles errors.

## Pipeline Stages
1. client - Gather requirements
2. product-manager - Plan features
3. project-manager - Plan sprints
4. ui-ux-designer - Create designs
5. tech-lead - Design architecture
6. software-engineer-frontend - Implement frontend
7. software-engineer-backend - Implement backend
8. testing-engineer - Write tests
9. qa-engineer - Validate quality
10. devops-engineer - Set up deployment
11. security-engineer - Validate security
12. documentation-specialist - Create documentation

## Parallel Execution
- Stage 6 and 7 can run in parallel (frontend and backend implementation)

## Approval Gates
- After tech-lead: Architecture approval required
- After qa-engineer: Quality approval required

## Usage
```bash
Skill(skill: "team-pipeline-new-project")
```

## Error Handling
- If a role fails, pipeline pauses and reports error
- User can fix issues and resume pipeline
- Failed stage can be retried