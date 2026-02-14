---
name: dev-team
description: An autonomous development team that builds complete projects from requirements to deployment
version: 1.0.0
category: development-team
---

# Dev-Team Skill

An autonomous development team that builds complete projects from requirements to deployment.

## Overview

This skill recruits and manages a specialized team of AI agents that collaborate to develop software projects following industry best practices. The team self-organizes, makes architectural decisions, and delivers tested, deployable code.

## Team Roles

- **Project Manager**: Orchestrates workflow, manages dependencies, makes go/no-go decisions
- **Tech Lead**: Architectural decisions, technology stack selection, code quality standards
- **Frontend Developer**: UI/UX implementation, component development, styling
- **Backend Developer**: API design, database modeling, server-side logic
- **QA Engineer**: Test strategy, test implementation, bug detection
- **DevOps Engineer**: CI/CD pipelines, deployment configuration, infrastructure

## Usage

### Initialize a New Project
```
dev-team init "Build a task management app with drag-and-drop interface"
```

### Check Team Status
```
dev-team status
```

### Get Progress Report
```
dev-team standup
```

### Scale Team
```
dev-team scale up frontend  # Add more frontend capacity
dev-team scale down backend  # Reduce backend capacity
```

### Save Session State
```
dev-team handoff
```

## Workflow

1. **Requirements Analysis** - Extract and validate project requirements
2. **Sprint Planning** - Break down into epics, stories, and tasks
3. **Development Cycle** - Parallel execution with continuous integration
4. **Quality Assurance** - Automated testing, code reviews, bug fixing
5. **Deployment** - CI/CD pipeline, staging validation, production rollout

## State Management

The skill maintains persistent state in `.state/` directory for session continuity and progress tracking.

## Integration

- Uses `tdd-enforce` for test-driven development
- Uses `git-manage` for version control operations
- Can integrate `python-project-builder-tdd` as template factory