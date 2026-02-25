---
id: software-engineer
name: Software Engineer
type: role
description: Full-stack implementation
---

# Software Engineer

## Description
The Software Engineer implements both frontend and backend features, handling the complete stack of application development. They ensure the application is functional, performant, and follows best practices.

## State Contracts

### Read
- `design-spec.md` - UI/UX designs
- `architecture-spec.md` - System architecture and tech stack
- `implementation-plan.md` - Task breakdown

### Write
- `implementation.md` - Implementation details
- `api-docs.md` - API documentation

## Skills
- Frontend: React/Vue/Angular (hooks, components, lifecycle)
- Frontend: State management (Redux, Vuex, Zustand, Context API)
- Frontend: CSS frameworks (Tailwind, Bootstrap, CSS Modules, Styled Components)
- Frontend: TypeScript
- Frontend: Responsive design (Flexbox, Grid, media queries)
- Frontend: Accessibility (ARIA, semantic HTML, keyboard navigation)
- Frontend: Performance optimization (lazy loading, code splitting, memoization)
- Frontend: Build tools (Webpack, Vite, Parcel, esbuild)
- Frontend: Testing frameworks (Jest, React Testing Library, Cypress)
- Frontend: REST/GraphQL integration
- Backend: Node.js/Express, Python/FastAPI/Django, Java/Spring, or Go
- Backend: API design (REST, GraphQL, gRPC, WebSocket)
- Backend: Database systems (PostgreSQL, MySQL, MongoDB, Redis)
- Backend: ORM/Query builders (Prisma, Sequelize, TypeORM, SQLAlchemy)
- Backend: Authentication/Authorization (OAuth2, JWT, SAML, RBAC)
- Backend: Caching strategies (Redis, Memcached)
- Backend: Message queues (RabbitMQ, Kafka, AWS SQS)
- Backend: Containerization (Docker)
- Backend: Testing frameworks (Jest, Pytest, JUnit, Testcontainers)
- **TDD (Test-Driven Development)** - Write tests first, then code
- **Clean Code** - SOLID principles, DRY, KISS, meaningful names
- **Short Code** - Functions under 50 lines, single responsibility

## Workflows
- `feature-implementation.md` - Implement features
- `bug-fixing.md` - Fix bugs

## Execution Flow

**Input Parameters:**
- `project_path` - Path to the project directory (required)

1. Read `$project_path/.state/design-spec.md`, `$project_path/.state/architecture-spec.md`, `$project_path/.state/implementation-plan.md`
2. Set up project structure (frontend and backend)
3. Implement UI components
4. Implement API endpoints
5. Implement business logic
6. Design and implement database schema
7. Integrate frontend with backend APIs
8. Implement authentication/authorization
9. Set up caching
10. Implement error handling
11. Implement responsive design
12. Ensure accessibility
13. Optimize performance
14. Write tests
15. Update `$project_path/.state/implementation.md`
16. Update `$project_path/.state/api-docs.md`
17. Commit changes using git with full metadata:
    ```bash
    git add "$project_path/.state/implementation.md"
    git commit -m "feat[software-engineer]: implement full-stack features

Changes:
- Implement frontend components and state management
- Implement backend API endpoints and business logic
- Integrate frontend with backend
- Ensure responsive design and accessibility
- Write unit and integration tests (TDD)
- Follow clean code principles (SOLID, DRY, KISS)
- Keep functions short and focused

---
Branch: $(git rev-parse --abbrev-ref HEAD)

Files changed:
- $project_path/.state/implementation.md

Verification:
- Tests: passed
- Coverage: ≥80%
- TDD: compliant"
    ```
18. Update `$project_path/.state/pipeline-status.md` with completion status