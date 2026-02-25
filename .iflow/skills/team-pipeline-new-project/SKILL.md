---
id: team-pipeline-new-project
name: Team Pipeline - New Project
type: pipeline
description: Full pipeline for new projects from scratch
---

# Team Pipeline - New Project

## Description
Full end-to-end pipeline for creating new projects from scratch with feature-by-feature iteration. This orchestrator executes all 11 roles in sequence for each feature, ensuring all features are completed before pipeline finishes.

## Configuration
Defined in `config.json`

## State Contracts

### Read
- `{project_path}/.state/pipeline-status.md` - Current pipeline status and feature list

### Write
- `{project_path}/.state/pipeline-status.md` - Updated pipeline status and feature completion

## Execution

**Feature-by-Feature Iteration Mode (Default):**

1. **Initialize Project**
   - Client role creates project state from templates
   - Client role extracts all features from project-spec.md
   - Pipeline tracks feature completion status

2. **Iterate Through Features**
   For each feature in the feature list:
   - Execute stages 4-11 for the current feature:
     - ui-ux-designer → tech-lead → software-engineer → testing-engineer → qa-engineer → devops-engineer → security-engineer → documentation-specialist
   - Each role updates implementation with current feature
   - Commit changes for the feature
   - Mark feature as completed
   - Move to next feature

3. **Complete Pipeline**
   - When all features are completed, pipeline finishes
   - Final summary report generated

**All-at-Once Mode:**
- Execute all roles sequentially once
- All features implemented in single pass
- Faster but less granular control

## Pipeline Stages

### One-Time Stages (Run Once)
1. client - Gather requirements and create feature list
2. product-manager - Plan features and create user stories
3. project-manager - Plan sprints and allocate resources

### Feature Iteration Stages (Repeated for Each Feature)
4. ui-ux-designer - Create designs for current feature
5. tech-lead - Review architecture for feature impact
6. software-engineer - Implement current feature
7. testing-engineer - Write tests for current feature
8. qa-engineer - Test current feature and validate quality
9. devops-engineer - Deploy if needed (for critical features)
10. security-engineer - Review security for current feature
11. documentation-specialist - Update documentation for current feature

## Iteration Flow

```
Client → Product Manager → Project Manager
                ↓
         [Feature List Created]
                ↓
         ┌───────────────────┐
         │ Feature 1         │
         └───────────────────┘
                ↓
    UI/UX → Tech Lead → Software Engineer → Testing → QA → DevOps → Security → Docs
                ↓
         [Feature 1 Complete]
                ↓
         ┌───────────────────┐
         │ Feature 2         │
         └───────────┬───────┘
                     ↓
    UI/UX → Tech Lead → Software Engineer → Testing → QA → DevOps → Security → Docs
                ↓
         [Feature 2 Complete]
                ↓
              ...continue...
                ↓
         ┌───────────────────┐
         │ Feature N         │
         └───────────────────┘
                ↓
    UI/UX → Tech Lead → Software Engineer → Testing → QA → DevOps → Security → Docs
                ↓
         [All Features Complete]
                ↓
         [Pipeline Done]
```

## Approval Gates
- After tech-lead: Architecture approval required
- After qa-engineer: Quality approval required

## Usage

```bash
# Feature-by-feature iteration (default)
Skill(skill: "team-pipeline-new-project", project_path: "./workspace/myapp", project_name: "MyApp")

# All-at-once mode
Skill(skill: "team-pipeline-new-project", project_path: "./workspace/myapp", project_name: "MyApp", iteration_mode: "all-at-once")
```

## Error Handling
- If a role fails for a feature, pipeline pauses and reports error
- User can fix issues and resume from that feature
- Failed feature can be retried
- Other features remain unaffected

## Feature Tracking

Pipeline tracks:
- Total number of features
- Current feature being processed
- Completed features list
- Remaining features list
- Feature completion percentage

## Output

**Pipeline Status** (`{project_path}/.state/pipeline-status.md`)
- Overall pipeline status
- Feature list with completion status
- Current feature being processed
- Progress percentage