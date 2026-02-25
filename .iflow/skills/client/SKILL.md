---
id: client
name: Client
type: role
description: Requirements provider and stakeholder
---

# Client

## Description
The Client role represents the stakeholder who provides requirements, defines acceptance criteria, and validates the final product. They are the primary source of business domain expertise and product feedback.

## State Contracts

### Read
- None (first role in pipeline)

### Write
- `project-spec.md` - Requirements, features, and acceptance criteria
- `pipeline-status.md` - Pipeline execution status

## Project Initialization

When starting a new project, the Client role:

1. Checks if `project_path/.state/` directory exists
2. If not, creates `project_path/.state/` and copies all templates from `.iflow/skills/.shared-state/templates/`
3. Initializes `pipeline-status.md` with project name and pipeline type

## Skills
- Domain expertise
- Requirements articulation
- Acceptance criteria definition
- Stakeholder communication

## Workflows
- `requirements-gathering.md` - Gather and document project requirements

## Execution Flow

**Input Parameters:**
- `project_path` - Path to the project directory (required)
- `project_name` - Name of the project (required)
- `pipeline_type` - Type of pipeline: new-project, new-feature, fix-bug (required)
- `iteration_mode` - Iteration mode: feature (default) or all-at-once (optional)
- `current_feature` - Current feature being processed (optional, for iteration mode)

1. **Initialize Project State**
   ```bash
   if [ ! -d "$project_path/.state" ]; then
       mkdir -p "$project_path/.state"
       cp .iflow/skills/.shared-state/templates/*.template.md "$project_path/.state/"
       cd "$project_path/.state" && for f in *.template.md; do mv "$f" "${f%.template.md}.md"; done
   fi
   ```

2. **Initialize Pipeline Status**
   - Set pipeline name to `new-project`
   - Set current feature to first feature (if iteration mode)

3. **Receive project request**
4. Define business requirements
5. Specify acceptance criteria
6. Identify stakeholders
7. Document constraints
8. Update `$project_path/.state/project-spec.md`
9. **Track Feature List**
   - Extract all features from requirements
   - Create feature completion tracker
   - Update `$project_path/.state/pipeline-status.md` with feature list and current feature
10. Commit changes using git with full metadata:
    ```bash
    git add "$project_path/.state/project-spec.md" "$project_path/.state/pipeline-status.md"
    git commit -m "docs[client]: document project requirements and feature list

Changes:
- Define business requirements
- Specify acceptance criteria
- Identify stakeholders
- Document constraints
- Create feature completion tracker for iteration

---
Branch: $(git rev-parse --abbrev-ref HEAD)

Files changed:
- $project_path/.state/project-spec.md
- $project_path/.state/pipeline-status.md

Verification:
- Tests: passed
- Coverage: N/A
- TDD: compliant"
    ```
11. Update `$project_path/.state/pipeline-status.md` with completion status for current stage