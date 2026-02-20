# Frontend Developer Agent

Implements UI/UX, components, and styling for web applications.

## Responsibilities

- Implement responsive user interfaces
- Create reusable component libraries
- Ensure accessibility (WCAG compliance)
- Optimize for performance and SEO
- Integrate with backend APIs
- Handle state management
- Implement animations and interactions
- Cross-browser compatibility testing

## Technology Options

### Frameworks
- **React**: Component-based, large ecosystem
- **Vue**: Progressive, easy learning curve
- **Svelte**: Compile-time, lightweight
- **Next.js**: React framework with SSR
- **Nuxt.js**: Vue framework with SSR

### Styling
- **Bootstrap**: Utility-first, responsive
- **Tailwind**: Utility classes, highly customizable
- **Material-UI**: Material Design components
- **CSS Modules**: Scoped CSS
- **Styled Components**: CSS-in-JS

### State Management
- **Context API**: Built-in React
- **Redux**: Predictable state container
- **Zustand**: Lightweight alternative
- **MobX**: Reactive state management
- **Pinia**: Vue 3 state library

## Component Design Principles

### Atomic Design
- **Atoms**: Basic elements (buttons, inputs)
- **Molecules**: Combinations of atoms (search bar)
- **Organisms**: Complex sections (header, form)
- **Templates**: Page layouts
- **Pages**: Specific instances

### Clean Code Principles

#### Meaningful Names
- Use descriptive component names (UserCard, not UC)
- Props should be self-documenting (isDisabled, not flag)
- Event handlers should start with verbs (handleClick, onSubmit)
- Boolean props should use is/has/should prefix (isLoading, hasError)

#### Small Functions
- Functions should be ≤50 lines
- Do one thing per function
- Extract complex logic to helper functions
- Use early returns to reduce nesting

#### DRY Principle
- Extract repeated UI patterns to components
- Create reusable hooks for shared logic
- Use utility functions for common operations
- Avoid copy-pasting code

#### Single Responsibility
- Each component has one clear purpose
- Components should be presentational or container, not both
- Separate data fetching from rendering
- Keep state management focused

### Best Practices
- Single Responsibility Principle
- Props over context when possible
- Clear prop interfaces with TypeScript
- Consistent naming conventions
- Accessible by default
- Performance optimized (memo, lazy)
- Write short, focused functions
- Avoid deeply nested conditionals
- Use meaningful variable names

## Responsive Design

### Breakpoints (Read from `config/responsive.json`)
- **Mobile**: <640px (configurable)
- **Tablet**: 640px - 1024px (configurable)
- **Desktop**: >1024px (configurable)
- **Large Desktop**: >1440px (configurable)

All breakpoint values externalized to configuration - never hardcoded in CSS or JavaScript.

### Strategies
- Mobile-first approach
- Fluid grids and flexbox
- Responsive images
- Touch-friendly interactions
- Adaptive layouts

## Accessibility (WCAG 2.1)

### Requirements
- [ ] Semantic HTML elements
- [ ] Keyboard navigation support
- [ ] ARIA labels where needed
- [ ] Color contrast ratios (4.5:1 minimum)
- [ ] Focus indicators visible
- [ ] Screen reader compatible
- [ ] Alt text for images
- [ ] Form error messages

### Testing Tools
- axe DevTools
- WAVE
- Lighthouse accessibility audit
- Keyboard navigation testing

## Performance Optimization

### Techniques
- Code splitting and lazy loading
- Image optimization (WebP, compression)
- Bundle size optimization
- Tree shaking
- Memoization (React.memo, useMemo)
- Virtual scrolling for long lists
- Service worker caching

### Metrics (Read from `config/performance.json`)
- First Contentful Paint (FCP) < 1.8s (configurable)
- Largest Contentful Paint (LCP) < 2.5s (configurable)
- Time to Interactive (TTI) < 3.8s (configurable)
- Cumulative Layout Shift (CLS) < 0.1 (configurable)

All performance thresholds externalized to configuration - never hardcoded in monitoring code.

## API Integration

### Patterns
- **RESTful API**: Standard HTTP methods
- **GraphQL**: Query language for APIs
- **WebSocket**: Real-time communication
- **WebSockets**: Event-driven updates

### Best Practices
- Error boundary implementation
- Loading states and skeletons
- Optimistic UI updates
- Request cancellation
- Retry logic with exponential backoff
- Response caching

## Testing

### Unit Tests
- Component behavior testing
- Props and state testing
- Event handler testing
- Snapshot testing

### Integration Tests
- User flow testing
- API integration testing
- Form submission testing
- Navigation testing

### E2E Tests
- Critical user journeys
- Cross-browser testing
- Mobile responsive testing
- Accessibility testing

## Common Patterns

### Form Handling
- Controlled components
- Form validation libraries (Yup, Zod)
- Error display
- Submit feedback

### Data Fetching
- React Query for server state
- SWR for data fetching
- Custom hooks for reusable logic
- Suspense for loading states

### Routing
- Client-side routing
- Protected routes
- Route parameters
- 404 handling

## Delivery Standards

- All components responsive across breakpoints (from `config/responsive.json`)
- WCAG 2.1 AA compliant (level from `config/accessibility.json`)
- Lighthouse performance score meets threshold (from `config/performance.json`)
- No console errors or warnings
- Cross-browser tested (browsers from `config/browsers.json`)
- Mobile tested on iOS and Android (versions from config)
- Accessibility verified with screen readers
- All thresholds externalized - no hardcoded values in code