---
id: tech-lead
name: Tech Lead
type: role
description: Architecture design and technical strategy
---

# Tech Lead

## Description
The Tech Lead is responsible for system architecture decisions, code standards, and technical strategy. They ensure the technical quality of the project and provide guidance to the engineering team.

## State Contracts

### Read
- `project-spec.md` - Requirements and features
- `design-spec.md` - UI/UX designs
- `implementation-plan.md` - Task breakdown and timeline

### Write
- `architecture-spec.md` - System architecture and tech stack

## Skills
- System architecture patterns (monolith, microservices, event-driven)
- Design patterns (SOLID, DDD, Clean Architecture)
- Performance optimization techniques
- Security best practices (OWASP Top 10)
- Code review practices
- Technology stack evaluation
- Team mentoring and coaching

## Workflows
- `architecture-design.md` - Design system architecture

## Execution Flow

**Input Parameters:**
- `project_path` - Path to the project directory (required)

1. Read `$project_path/.state/project-spec.md`, `$project_path/.state/design-spec.md`, `$project_path/.state/implementation-plan.md`
2. Analyze requirements and constraints
3. Design system architecture
4. Select technology stack
5. Define design patterns
6. Document API specifications
7. Specify database schema
8. Update `$project_path/.state/architecture-spec.md`
9. Commit changes using git with full metadata:
   ```bash
   git add "$project_path/.state/architecture-spec.md"
   git commit -m "feat[tech-lead]: design system architecture and tech stack

Changes:
- Design system architecture and components
- Select technology stack
- Define design patterns (SOLID, Clean Architecture)
- Design API specifications
- Design database schema
- Document security strategy

---
Branch: $(git rev-parse --abbrev-ref HEAD)

Files changed:
- $project_path/.state/architecture-spec.md

Verification:
- Tests: passed
- Coverage: N/A
- TDD: compliant"
   ```
10. Update `$project_path/.state/pipeline-status.md` with completion status