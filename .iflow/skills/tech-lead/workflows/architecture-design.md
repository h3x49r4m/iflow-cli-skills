# Architecture Design Workflow

## Objective
Design system architecture and select technology stack.

## Steps

1. **Analyze Requirements and Design**
   - Read `project-spec.md`, `design-spec.md`, `implementation-plan.md`
   - Understand requirements, constraints, and timeline
   - Review UI/UX designs and user flows

2. **Design System Architecture**
   - Choose architecture pattern (monolith, microservices, event-driven)
   - Define system components and their interactions
   - Design data flow between components
   - Plan for scalability and performance

3. **Select Technology Stack**
   - Choose frontend framework (React, Vue, Angular)
   - Choose backend framework (Express, FastAPI, Django, Spring)
   - Select database (PostgreSQL, MySQL, MongoDB, Redis)
   - Choose infrastructure tools (Docker, Kubernetes, Terraform)

4. **Define Design Patterns**
   - Apply SOLID principles
   - Use appropriate design patterns (Factory, Strategy, Observer, etc.)
   - Implement Clean Architecture principles
   - Document pattern usage

5. **Design API Specifications**
   - Define API endpoints (REST, GraphQL)
   - Specify request/response schemas
   - Document authentication/authorization requirements
   - Define error handling approach

6. **Design Database Schema**
   - Create entity-relationship diagrams
   - Define tables/collections and relationships
   - Plan for indexing and query optimization
   - Consider data migration strategy

7. **Document Security Strategy**
   - Define authentication method (OAuth2, JWT)
   - Specify authorization approach (RBAC, ABAC)
   - Plan encryption (data at rest, in transit)
   - Document security best practices

8. **Document Everything**
   - Update `architecture-spec.md` with complete architecture design
   - Include diagrams, API specs, and technology choices

## Output
- Updated `architecture-spec.md` with complete architecture design
- Commit changes using git-manage
- Updated `pipeline-status.md` with completion status