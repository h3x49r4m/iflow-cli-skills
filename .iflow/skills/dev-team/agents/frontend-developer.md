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

### Best Practices
- Single Responsibility Principle
- Props over context when possible
- Clear prop interfaces with TypeScript
- Consistent naming conventions
- Accessible by default
- Performance optimized (memo, lazy)

## Responsive Design

### Breakpoints
- **Mobile**: <640px
- **Tablet**: 640px - 1024px
- **Desktop**: >1024px
- **Large Desktop**: >1440px

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

### Metrics
- First Contentful Paint (FCP) < 1.8s
- Largest Contentful Paint (LCP) < 2.5s
- Time to Interactive (TTI) < 3.8s
- Cumulative Layout Shift (CLS) < 0.1

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

##交付标准

- All components responsive across breakpoints
- WCAG 2.1 AA compliant
- Lighthouse performance score >90
- No console errors or warnings
- Cross-browser tested (Chrome, Firefox, Safari, Edge)
- Mobile tested on iOS and Android
- Accessibility verified with screen readers