---
id: team-pipeline-new-feature
name: Team Pipeline - New Feature
type: pipeline
description: Pipeline for adding features to existing projects
---

# Team Pipeline - New Feature

## Description
Streamlined pipeline for adding features to existing projects. This orchestrator executes roles in sequence to deliver new features while maintaining existing functionality.

## Configuration
Defined in `config.json`

## State Contracts

### Read
- `pipeline-status.md` - Current pipeline status
- All existing state documents for context

### Write
- `pipeline-status.md` - Updated pipeline status

## Execution
Orchestrates roles in sequence as defined in config.json. Each role reads state, performs work, updates state, commits changes using git-manage, and reports completion. The orchestrator tracks progress and handles errors.

## Pipeline Stages
1. client (optional) - Gather feature requirements
2. product-manager - Plan feature
3. project-manager - Plan sprint for feature
4. ui-ux-designer - Create feature designs
5. tech-lead - Review architecture for feature impact
6. software-engineer-frontend - Implement feature UI
7. software-engineer-backend - Implement feature API/logic
8. testing-engineer - Write tests for feature
9. qa-engineer - Test feature and validate quality
10. devops-engineer - Deploy feature (if needed)
11. security-engineer - Review security for feature
12. documentation-specialist - Update docs for feature

## Parallel Execution
- Stage 6 and 7 can run in parallel (frontend and backend implementation)

## Conditional Execution
- Stage 1 (client) is optional if PM already has requirements

## Usage
```bash
Skill(skill: "team-pipeline-new-feature")
```

## Error Handling
- If a role fails, pipeline pauses and reports error
- User can fix issues and resume pipeline
- Failed stage can be retried