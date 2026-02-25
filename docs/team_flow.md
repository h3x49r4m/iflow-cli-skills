# Team Flow Diagram

Visual representation of the iFlow Skills team structure and workflow.

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                           iFlow Skills Team                                 ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐                 ║
║  │    Client    │───▶│Product Mgr   │───▶│Project Mgr   │                 ║
║  └──────────────┘    └──────────────┘    └──────────────┘                 ║
║         │                  │                  │                             ║
║         └──────────────────┴──────────────────┘                             ║
║                            │                                               ║
║                    ┌───────▼───────┐                                     ║
║                    │ UI/UX Designer│                                     ║
║                    └───────┬───────┘                                     ║
║                            │                                               ║
║                    ┌───────▼───────┐                                     ║
║                    │   Tech Lead   │                                     ║
║                    └───────┬───────┘                                     ║
║                            │                                               ║
║                    ┌───────▼──────────────────┐                          ║
║                    │ Software Engineer (Full) │                          ║
║                    └───────┬──────────────────┘                          ║
║                            │                                               ║
║           ┌────────────────┼────────────────┐                             ║
║           ▼                ▼                ▼                             ║
║  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                   ║
║  │Testing Eng   │  │  QA Engineer  │  │DevOps Engineer│                   ║
║  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘                   ║
║         │                │                │                               ║
║         └────────────────┴────────────────┘                               ║
║                            │                                               ║
║                    ┌───────▼───────┐                                     ║
║                    │Security Eng   │                                     ║
║                    └───────┬───────┘                                     ║
║                            │                                               ║
║                    ┌───────▼───────┐                                     ║
║                    │Documentation  │                                     ║
║                    │  Specialist   │                                     ║
║                    └───────────────┘                                     ║
║                                                                           ║
║  ╔════════════════════════════════════════════════════════════════════╗  ║
║  ║              Shared State Directory (.shared-state/)                  ║  ║
║  ╠════════════════════════════════════════════════════════════════════╣  ║
║  ║ • project-spec.md     • design-spec.md    • architecture-spec.md     ║  ║
║  ║ • implementation.md   • test-plan.md      • test-results.md          ║  ║
║  ║ • quality-report.md   • security-report.md • deployment-status.md    ║  ║
║  ║ • api-docs.md         • user-guide.md      • changelog.md            ║  ║
║  ║ • pipeline-status.md                                              ║  ║
║  ╚════════════════════════════════════════════════════════════════════╝  ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

## Roles

### Product & Planning
- **Client** - Requirements provider and stakeholder
- **Product Manager** - Feature planning and prioritization
- **Project Manager** - Sprint planning and resource allocation

### Design
- **UI/UX Designer** - Design creation and user experience

### Technical Leadership
- **Tech Lead** - Architecture design and technical strategy

### Engineering
- **Software Engineer** - Full-stack implementation

### Quality & Operations
- **Testing Engineer** - Test automation and frameworks
- **QA Engineer** - Quality validation and manual testing
- **DevOps Engineer** - CI/CD and infrastructure
- **Security Engineer** - Security validation and scanning
- **Documentation Specialist** - Documentation creation

## Pipelines

### New Project Pipeline
Executes all 11 roles sequentially to deliver a complete, production-ready application.

### New Feature Pipeline
Streamlined pipeline for adding features to existing projects.

### Bug Fix Pipeline
Focused pipeline for rapid bug fixing.

## State Management

All roles share a common state directory (`.shared-state/`) with 14 state documents that track project progress, specifications, implementation details, test results, quality reports, security findings, and documentation.