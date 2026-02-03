# Effort Estimation Guide

## Purpose
This guide provides a framework for estimating the complexity and effort required for each feature.

## Estimation Factors

### 1. Functional Complexity
How complex is the feature's logic?
- **Simple**: Straightforward logic, no branching
- **Moderate**: Some conditional logic, multiple paths
- **Complex**: Multiple interconnected components, significant business logic
- **Very Complex**: Distributed logic, async operations, state management

### 2. Technical Complexity
How complex is the implementation?
- **Simple**: Standard library only, no external dependencies
- **Moderate**: Few external libraries, some configuration needed
- **Complex**: Multiple integrations, custom algorithms
- **Very Complex**: Complex algorithms, performance optimizations, concurrency

### 3. Testing Effort
How much testing is required?
- **Simple**: Few test cases, minimal edge cases
- **Moderate**: Multiple test cases, some edge cases
- **Complex**: Many test cases, integration tests, edge cases
- **Very Complex**: Extensive testing, performance tests, stress tests

### 4. Integration Complexity
How complex is integrating with other features?
- **Simple**: No integration required
- **Moderate**: Integration with 1-2 other features
- **Complex**: Integration with multiple features, careful coordination
- **Very Complex**: Complex integration with external systems

## Estimation Scale

| Level | Time Estimate | Description |
|-------|---------------|-------------|
| 1 (Simple) | 1-2 hours | Straightforward, minimal testing |
| 2 (Moderate) | 0.5-1 day | Some complexity, standard testing |
| 3 (Complex) | 1-3 days | Significant complexity, extensive testing |
| 4 (Very Complex) | 3+ days | Highly complex, research required |

## Estimation Process

### Step 1: Analyze the Feature
Review the feature specification and understand:
- What the feature does
- What inputs/outputs it has
- What dependencies it has
- What edge cases exist

### Step 2: Assess Each Factor
Rate each factor (1-4):
- Functional complexity: __
- Technical complexity: __
- Testing effort: __
- Integration complexity: __

### Step 3: Calculate Overall Complexity
Take the highest rating among factors.
- If any factor is 4, overall is 4 (Very Complex)
- If any factor is 3, overall is 3 (Complex)
- If any factor is 2, overall is 2 (Moderate)
- If all factors are 1, overall is 1 (Simple)

### Step 4: Refine Estimate
Consider additional factors:
- **Team familiarity**: Familiar domain = lower estimate
- **Available resources**: More resources = lower time
- **Risk factors**: Uncertain requirements = higher estimate
- **Technical debt**: Existing code quality affects estimate

### Step 5: Document Assumptions
Document what assumptions the estimate is based on:
- Requirements are clear
- Dependencies are available
- No major blockers
- Standard development environment

## Estimation Template

```markdown
## Feature: [Feature Name]

### Factor Ratings
| Factor | Rating (1-4) | Notes |
|--------|--------------|-------|
| Functional Complexity | ___ | notes |
| Technical Complexity | ___ | notes |
| Testing Effort | ___ | notes |
| Integration Complexity | ___ | notes |

### Overall Complexity
- [ ] 1 (Simple) - 1-2 hours
- [ ] 2 (Moderate) - 0.5-1 day
- [ ] 3 (Complex) - 1-3 days
- [ ] 4 (Very Complex) - 3+ days

### Time Estimate
__ hours / __ days

### Assumptions
- Assumption 1
- Assumption 2

### Risk Factors
- Risk 1 (could increase estimate by __)
- Risk 2 (could increase estimate by __)

### Contingency
Add __% contingency for risks: __ hours/days

### Final Estimate
__ hours / __ days
```

## Example

## Feature: User Login

### Factor Ratings
| Factor | Rating (1-4) | Notes |
|--------|--------------|-------|
| Functional Complexity | 2 | Basic auth logic |
| Technical Complexity | 2 | bcrypt, JWT libraries |
| Testing Effort | 3 | Multiple scenarios, edge cases |
| Integration Complexity | 2 | Depends on user database |

### Overall Complexity
- [ ] 1 (Simple) - 1-2 hours
- [x] 2 (Moderate) - 0.5-1 day
- [ ] 3 (Complex) - 1-3 days
- [ ] 4 (Very Complex) - 3+ days

### Time Estimate
6 hours / 0.75 days

### Assumptions
- User database exists
- JWT library is compatible
- bcrypt is already available

### Risk Factors
- Password hashing performance (could add 1-2 hours)
- Token security requirements (could add 2-4 hours)

### Contingency
Add 25% contingency for risks: 1.5 hours

### Final Estimate
7.5 hours / 1 day

## Best Practices

1. **Be Conservative**: Underestimating is worse than overestimating
2. **Reference Past Work**: Use previous features as benchmarks
3. **Involve Developers**: Get input from those who will implement
4. **Track Accuracy**: Compare estimates to actuals for future reference
5. **Re-estimate When Needed**: Update estimates if requirements change
6. **Buffer for Uncertainty**: Always add contingency for unknowns

## Tracking Estimates

Use the `feature-tracker.md` to track:
- Original estimates
- Actual time spent
- Variance (estimate vs actual)
- Lessons learned for future estimates