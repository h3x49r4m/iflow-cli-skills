# Feature Implementation Workflow

## Objective
Implement features according to design and architecture (full-stack).

## Steps

### Frontend Implementation

1. **Analyze Design and Architecture**
   - Read `design-spec.md`, `architecture-spec.md`, `implementation-plan.md`
   - Understand UI/UX designs and component requirements
   - Review architecture decisions and tech stack

2. **Set Up Frontend Project Structure**
   - Initialize frontend project with chosen framework
   - Configure build tools (Webpack, Vite, esbuild)
   - Set up development environment
   - Configure linting and formatting

3. **Implement UI Components**
   - Create component hierarchy
   - Implement each component according to design specs
   - Use component library or CSS framework as specified
   - Ensure reusability and maintainability

4. **Implement State Management**
   - Set up state management (Redux, Vuex, Context API)
   - Define state structure and actions
   - Connect components to state
   - Handle state updates and side effects

5. **Integrate APIs**
   - Set up API client (axios, fetch)
   - Connect to backend endpoints
   - Handle API responses and errors
   - Implement loading states

6. **Implement Responsive Design**
   - Use Flexbox and Grid layouts
   - Add media queries for breakpoints
   - Test on different screen sizes
   - Ensure mobile-first approach

7. **Ensure Accessibility**
   - Use semantic HTML
   - Add ARIA labels where needed
   - Ensure keyboard navigation works
   - Test with screen readers

8. **Optimize Performance**
   - Implement lazy loading for images and components
   - Use code splitting for routes
   - Apply memoization (React.memo, useMemo, useCallback)
   - Optimize bundle size

### Backend Implementation

9. **Set Up Backend Project Structure**
   - Initialize backend project with chosen framework
   - Configure build and testing tools
   - Set up environment variables
   - Configure linting and formatting

10. **Implement API Endpoints**
    - Define API routes
    - Implement request handling
    - Validate input data
    - Return appropriate responses

11. **Implement Business Logic**
    - Implement core business rules
    - Handle data transformations
    - Implement service layer
    - Ensure separation of concerns

12. **Design and Implement Database Schema**
    - Create entity-relationship diagrams
    - Define tables/collections and relationships
    - Create migrations
    - Set up indexes

13. **Implement Authentication/Authorization**
    - Set up authentication (JWT, OAuth2)
    - Implement role-based access control
    - Secure endpoints
    - Handle sessions

14. **Set Up Caching**
    - Configure Redis or other cache
    - Cache frequently accessed data
    - Implement cache invalidation
    - Monitor cache performance

15. **Implement Error Handling**
    - Create error handling middleware
    - Log errors appropriately
    - Return user-friendly error messages
    - Handle edge cases

### Testing (TDD)

16. **Write Tests First (TDD)**
    - Write unit tests for components BEFORE implementation
    - Write unit tests for API endpoints BEFORE implementation
    - Write integration tests for user flows BEFORE implementation
    - Set up E2E tests with Cypress or Playwright
    - Ensure adequate coverage

17. **Implement Code to Pass Tests (TDD)**
    - Write minimal code to make tests pass
    - Follow RED-GREEN-REFACTOR cycle
    - Keep implementation focused on test requirements

18. **Refactor for Clean Code (TDD)**
    - Apply SOLID principles
    - Ensure DRY (Don't Repeat Yourself)
    - Follow KISS (Keep It Simple, Stupid)
    - Keep functions under 50 lines
    - Single responsibility per function
    - Use meaningful variable and function names
    - Extract constants and magic numbers

### Documentation

19. **Document Everything**
    - Update `implementation.md` with implementation details
    - Include component structure, state management, and integration notes
    - Update `api-docs.md` with API documentation

## Output
- Updated `implementation.md` with implementation details
- Updated `api-docs.md` with API documentation
- Commit changes using git-manage
- Updated `pipeline-status.md` with completion status