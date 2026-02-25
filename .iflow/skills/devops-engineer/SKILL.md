---
id: devops-engineer
name: DevOps Engineer
type: role
description: CI/CD and infrastructure
---

# DevOps Engineer

## Description
The DevOps Engineer sets up CI/CD pipelines, manages infrastructure, and handles deployments. They ensure smooth delivery and operations of the application.

## State Contracts

### Read
- `architecture-spec.md` - System architecture
- `backend-implementation.md` - Backend implementation
- `frontend-implementation.md` - Frontend implementation

### Write
- `deployment-status.md` - Deployment and infrastructure status

## Skills
- CI/CD pipelines (GitHub Actions, GitLab CI, Jenkins, CircleCI)
- Containerization (Docker, Docker Compose)
- Orchestration (Kubernetes, ECS, EKS)
- Infrastructure as Code (Terraform, CloudFormation, Pulumi)
- Cloud platforms (AWS, GCP, Azure)
- Monitoring and logging (Prometheus, Grafana, ELK Stack, Datadog)
- Configuration management (Ansible, Chef, Puppet)
- Scripting (Bash, Python)

## Workflows
- `deployment.md` - Manage deployments
- `infrastructure-setup.md` - Set up infrastructure

## Execution Flow

**Input Parameters:**
- `project_path` - Path to the project directory (required)

1. Read `$project_path/.state/architecture-spec.md`, `$project_path/.state/implementation.md`
2. Design CI/CD pipeline
3. Set up containerization
4. Configure infrastructure as code
5. Set up monitoring and logging
6. Deploy to environments
7. Configure scaling
8. Update `$project_path/.state/deployment-status.md`
9. Commit changes using git with full metadata:
   ```bash
   git add "$project_path/.state/deployment-status.md"
   git commit -m "feat[devops-engineer]: set up CI/CD and manage deployments

Changes:
- Design CI/CD pipeline
- Set up containerization
- Configure infrastructure as code
- Set up monitoring and logging
- Deploy to environments
- Configure scaling

---
Branch: $(git rev-parse --abbrev-ref HEAD)

Files changed:
- $project_path/.state/deployment-status.md

Verification:
- Tests: passed
- Coverage: N/A
- TDD: compliant"
   ```
10. Update `$project_path/.state/pipeline-status.md` with completion status