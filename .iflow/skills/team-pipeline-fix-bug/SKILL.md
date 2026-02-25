---
id: team-pipeline-fix-bug
name: Team Pipeline - Fix Bug
type: pipeline
description: Focused pipeline for rapid bug fixing
---

# Team Pipeline - Bug Fix

## Description
Focused pipeline for fixing bugs rapidly. This orchestrator executes only the necessary roles to identify, fix, test, and deploy bug fixes.

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
1. client (optional) - Receive bug report
2. tech-lead - Analyze bug and determine root cause
3. software-engineer-frontend OR software-engineer-backend - Fix bug (conditional)
4. testing-engineer - Write regression test
5. qa-engineer - Validate fix and perform regression testing
6. devops-engineer - Deploy hotfix (if critical)
7. documentation-specialist - Update changelog (if needed)

## Conditional Execution
- Stage 1 (client) is optional if bug reported internally
- Stage 3 (frontend OR backend) is conditional based on bug location
- Stage 6 (devops) is only for critical hotfixes
- Stage 7 (documentation) is only for significant bugs

## Usage
```bash
Skill(skill: "team-pipeline-fix-bug")
```

## Error Handling
- If a role fails, pipeline pauses and reports error
- User can fix issues and resume pipeline
- Failed stage can be retried

## Speed Priority
- This pipeline prioritizes speed over comprehensive documentation
- Minimal approval gates
- Direct deployment path for critical fixes