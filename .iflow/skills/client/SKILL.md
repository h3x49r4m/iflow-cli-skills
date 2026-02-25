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

## Skills
- Domain expertise
- Requirements articulation
- Acceptance criteria definition
- Stakeholder communication

## Workflows
- `requirements-gathering.md` - Gather and document project requirements

## Execution Flow
1. Receive project request
2. Define business requirements
3. Specify acceptance criteria
4. Identify stakeholders
5. Document constraints
6. Update `project-spec.md`
7. Commit changes using git-manage: `git-manage commit docs[client]: document project requirements`
8. Update `pipeline-status.md` with completion status